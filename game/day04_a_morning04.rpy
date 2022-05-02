##Sábado
    #Neus Foot Job Points.
default Nfjob = 0



##

default morning04_Shopping_NotTogether_Cond = False
default morning04_Shopping_Alone_Cond = False
default morning04_Shopping_Alone_Angry_Cond = False

##

default aftermorning04_calmdidac_Failed = False
default aftermorning04_lingerishopafterpunch_stay = False

##
#default afternoon04_DidacShopingCenter_Cond = False
default morning04_ShoppingDidac_Cond = False
default morning04_DidacHotforyou_Cond = False
default morning04_Shopping_didaccum_Cond = False
default morning04_Shopping_didaccumANAL_Cond = False #Didac cum, but only fingering her anus.
default morning04_Shopping_youcum_Cond = False

default morning04_Shopping_AgentsTalk_Cond = False #Hablas con agentes en los probadores.
default morning04_Shopping_SalesWomanTalkg_Cond = False #Hablas con la dependienta.

default afternoon04_MACBA_Agent01Talk_Cond = False #Habla con el agente 01 en el MACBA.

default aftermorning04_FittingRoom_Masturbation = False
default aftermorning04_FittingRoom_ButtocksDickOver = False
default aftermorning04_FittingRoom_ButtocksDickOverMasturbate = False
default aftermorning04_FittingRoom_FuckherConsent = False
default aftermorning04_RapedNo = False
default aftermorning04_RapedYes = False

default aftermorning04_Mast001_Pussy_insert = False
default aftermorning04_Mast001_Pussy_happy = False
default aftermorning04_Mast001_Anal_insert = False
default aftermorning04_Mast001_Anal_happy = False
default aftermorning04_Mast001_Anal_angry = False

default aftermorning04_Mast001_PussyFast_insert = False
default aftermorning04_Mast001_AnalFast_insert = False

default aftermorning04_Mast001_AnalFast_Happy = False
default aftermorning04_Mast001_AnalFast_Angry = False

default aftermorning04_Mast001_PussyFast_Happy = False
default aftermorning04_Mast001_PussyFast_Angry = False

default aftermorning04_Mast001_PussyFastAfter_Happy = False
default aftermorning04_Mast001_PussyFastAfter_Angry = False

default aftermorning04_Mast001_AnalFastAfter_Happy = False
default aftermorning04_Mast001_AnalFastAfter_Angry = False

default aftermorning04_bg_fittingroom_mast_Fast = False


##Date MACBA

default Martq = 0 #Modern Art Questions
default Cartq = 0 # Classic Art Questions
default inMACBAq = 0 #Inside MACBA Questions
default TxellSlave = 0 #To be slave of Txell.

default afternoon04_TxellMacbaDate = False
default afternoon04_Q_ModernArt = False
default afternoon04_Q_ClassicArt = False

default afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = False
default afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = False
default afternoon04_paint_c_miguelangel_creationofadam_Message_womb = False
default afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = False 
default afternoon04_RedHairGirl_DidacRisk_Cond = False
default afternoon04_MACBA_Mucus_AbsorFig_Cond = False
default afternoon04_MACBA_Mucus_Represent_Cond = False
default afternoon04_MACBA_TxellAge_Cond = False
default afternoon04_MACBA_TxellName_Know = False
default KnowTxellwasEscort_Cond = False
default DislikeTxellwasEscort_Cond = False
default afternoon04_MACBA_TxellTruth_Cond = False
default afternoon04_macba_txellGrabYourBalls_Cond = False


############################################
###########################################

default aftermorning04_fr_rape_anim00 = False
default aftermorning04_fr_rape_anim01 = False
default aftermorning04_fr_rape_anim02 = False
default aftermorning04_fr_rape_anim03 = False
default aftermorning04_fr_rape_anim04 = False
default aftermorning04_fr_rape_anim05 = False
default aftermorning04_fr_rape_anim06 = False
default aftermorning04_fr_rape_anim07 = False

default aftermorning04_fr_rape_cumed_out = False
default aftermorning04_fr_rape_cumed_in = False
default aftermorning04_fr_rape_bite_Cond = False

###

label morning04:

    $ p_ao_n_horns = ""

    $ dad = d_dad

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ saturation_tint_level = "default"
    
    play music "audio/sfx/birds01.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/rubbingPussy01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    scene black with fade
    
    $ renpy.notify("Day 04")
    
    n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."
    
    n "Pero hay otro sonido extraño que te llama la atención."

    play sound "audio/characters/didac/moan03.ogg"
    
    pt "Suena..."

    pt "suenan como gemidos ahogados."
    
    n "Como si alguien estuviera mordiendo algo a la vez que estuviera haciendo algo más..."

    play sound "audio/characters/didac/moanings02.ogg"
    
    gn "Hmmm-Mffhmm..." # Females moans
    
    pt "Es la voz de una chica..."

    pt "¡¿En mi habitación?!"
    
    pt "¡¿Dídac?!"
    
    play music "audio/music/kevinmacleod/last_kiss_goodnight.ogg" fadein 3.0 fadeout 3.0
    
    play sound "audio/characters/didac/moanings07.ogg"
    
    scene morning04_bg bedroom_neus_a # Bitch
    show morning04_bedroom_Neus_body 01a:
        morning04_bedroom_Neus_body_anim
        
    show morning04_bedroom_Neus_bodyass 01a:
        morning04_bedroom_Neus_bodyass_anim02
        
    show border_dream:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        ease 150.0 xanchor 0.0 yanchor 0.0 zoom 0.5

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
    
    window hide dissolve
    pause
    
    n "Entreabres los ojos y te encuentras una borrosa silueta oscura justo encima de ti." 
    
    n "Oyes ahora más claramente esa extraña voz y distingues perfectamente que se tratan de gemidos ahogados."
    
    n "Ves que esa extraña silueta se mueve encima de ti y que además hace temblar tu cuerpo,"
    
    n "como si estuviera saltando encima de ti."
    
    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01b
    with dissolve
    
    pt "¡Es una tía!"
    
    pt "¿Está montándome desnuda?"
    
    n "Por fin logras abrir más los ojos y ves que se trata de"

    extend " {size=60}{b}¿¡Neus!?{/b}{/size}"
    
    play sound "audio/characters/didac/moanings06.ogg"
    
    show morning04_bedroom_Neus_body 01c
    show morning04_bedroom_Neus_bodyass 01b
    with dissolve
    
    pt "¿¡Pero qué hace en mi piso?!"
    
    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01c
    with dissolve
    
    pt "¿Me está violando?"
    
    window hide dissolve
    pause
    
    play sound "audio/characters/neus/giggle03.ogg"
    
    hide morning04_bedroom_Neus_body 
    hide morning04_bedroom_Neus_bodyass
    hide light
    hide morning04_bedroom_DMast_blinkeye
    hide light_screen_01
    show morning04_bg bedroom_neus_a
    show morning04_bedroom_Neus_body_ass 02a: 
        morning04_bedroom_Neus_bodyass_anim01
    show morning04_bedroom_Neus_body_body 02a
    #show morning04_bedroom_Neus_Prove
    show morning04_bedroom_Neus_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_mouth happy_Silentx02:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyes 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyepupils front_green_03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyebrows normal:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_glasses:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_body_hair 02a
    show light 01:
        light01_rightside_position
    #show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Neus acerca su rostro al tuyo con su cuerpo todavía pegado"
    
    n "y -casi rozándote sus labios con los tuyos- te susurra."
    
    show morning04_bedroom_Neus_body_ass 02b
    show morning04_bedroom_Neus_body_body 02b
    show morning04_bedroom_Neus_body_hair 02b
    show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
    show morning04_bedroom_Neus_exp_eyebrows surprisex01
    with Dissolve (1.0)
    
    ne "¿Acaso no te gusta, [protname]?"

    show morning04_bedroom_Neus_exp_eyebrows angryx01
    with dissolve
    
    ne "La tienes bien dura,"

    extend " y se siente bien rica dentro de mí..."

    show morning04_bedroom_Neus_exp_eyebrows surprisex01
    with dissolve
    
    ne "¿Acaso quieres que la saque?"
    
    show morning04_bedroom_Neus_exp_eyebrows normal
    show morning04_bedroom_Neus_exp_mouth happy_Silentx02
    with dissolve 
    
    window hide dissolve
    pause
    
    play music "audio/sfx/birds01.ogg"
    
    scene black
    with fade
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    play sound "audio/characters/didac/moanings05.ogg"
    
    n "De pronto, oyes un gemido más agudo que los anteriores,"
    
    n "pero no viene de Neus, viene de un lugar más lejano."
    
    show morning04_bg bedroom_neus_a
    show light 01:
        light01_rightside_position
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade
    
    n "Abres los ojos y te encuentras mirando la pared de la habitación."
    
    n "Neus ya no está, en realidad se había tratado de un sueño."
    
    show morning04_bg bedroom_neus_b
    with fade
    
    n "Te relajas en la cama, pero sientes que tu polla sigue estando bien dura."
    
    play sound "audio/characters/didac/moanings04.ogg"
    
    gd "Mfff-mmm... aahh..." # Moans masturbating close to him without shame *Gimoteos femeninos* 
    
    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
    
    show morning04_bg bedroom_neus_c
    with fade
    
    pt "¡¿Otra vez esos gemidos?!" 
    
    pt "¡Es la misma voz que antes!"
    
    pt "¡¿Sigo soñando?!"

    n "Intentas girar tu cabeza con el máximo disimulo que te permiten tus cervicales" 
       
    n "para mirar a tu espalda, donde está la cama de tu compañero de piso."
    
    play sound "audio/characters/didac/moanings07.ogg"

    d "Mmm-Agh... mff..." # Moans while masturbating *Gimoteos femeninos* 
    
    pt "¿Qué puñetas estás haciendo Dídac?"
    
    ##NOT FINISHED MUSIC
    
    #stop music fadeout 3.0
    
    scene morning04_bedroom_DMast step01
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade
    
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/rubbingPussy01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/characters/didac/moanings05.ogg"

    n "Sin el más mínimo pudor de taparse o vestirse," 
       
    n "ves a tu compañera/o de clase con el cuerpo retorcido por el placer y con la mano en su entrepierna."

    n "Agitándola con inquietud, así como ondulando sus dedos por esa parte."

    n "Mientras, en la boca tiene su otra mano mordiéndola intentado amortiguar el sonido de sus gemidos."

    $ renpy.music.set_volume(0.7, delay=15.0, channel='sfx1')
    
    play sound "audio/characters/didac/moanings06.ogg"

    p "..."

    extend " ¿¡Pero qué hostias!?"

    pt "Dídac..."

    extend " ¡¿Se puede saber qué demonios estás haciendo?!"

    pt "¡¿No ves que compartimos habitación?!"
    
    play sound "audio/characters/didac/moanings07.ogg"

    n "Sin poderlo evitar, tu miembro viril empieza a aumentar de tamaño considerablemente" 
       
    n "hasta convertirse en una dura piedra."

    pt "¡La madre que te parió!"

    extend " ¡Ahora no es el momento de que te pongas así!"

    pt "Tengo que hacerme el dormido hasta que termine,"

    extend " o esto acabará muy mal..."
    
    play sound "audio/characters/didac/moanings04.ogg"

    pt "No puedo levantarme ahora de la cama disimulando que no lo he escuchado," 
        
    pt "teniendo la polla tan dura como la tengo..."

    menu morning04_masturbation:
        
        pt "Puta polla... ¿Por qué siempre vas a tu bola?"
        
        "Levantarte e ir a la cocina disimulando el bulto entre piernas.":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
                  
            jump morning04_Escape
        
        "Resistir la tentación de masturbarte.":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
            
            jump morning04_AvoidMasturbation
            
        "Masturbarte.":
            
            call p_Help
            
            if pl.dp >= 1:
                $pl.ch_pts("dp",3)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 1[hd]")
                            
                $ morning04_DidacHotforyou_Cond = True
                
                jump morning04_MasturbateYes
                            
            else:
                $pl.ch_pts("dp",1)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 1[hd]")
                            
                jump morning04_MasturbateYes
            
label morning04_Escape:
    
    scene black with fade
    
    n "Intentas apartar la ligera sábana que cubre tu cuerpo semidesnudo."
    
    show morning04_bg_bedroom_youleaving 01
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with dissolve
    play sound "audio/characters/didac/moanings07.ogg"
    
    n "Decides prescindir de tus zapatillas para hacer el mínimo ruido posible."
    
    play sound "audio/sfx/door_open01.ogg"
    show morning04_bg_bedroom_youleaving 02
    #show light_screen_01:
        #light_screen_01_position
    with dissolve
    
    pt "Está tan absorto en lo que hace, que no se da cuenta de que estoy despierto y de pie..."
    
    play sound "audio/sfx/door_close01.ogg"
    scene black with fade
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    stop music fadeout 3.0
    
    $ renpy.music.set_volume(0.1, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=False, fadeout=1.0, synchro_start=True, fadein=1.0)
    
    n "Una vez en el pasillo, crees que lo más sensato es primero saciar tu apetito."
    
    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    show morning04_bg_kitch_toastwithjam
    show light_screen_01:
        light_screen_01_position

    with dissolve
    
    n "Así que te diriges a la cocina para prepararte unas tostadas con mermelada y mantequilla."

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    n "Mientras estás saboreando tu delicioso desayuno, te parece escuchar el ruido de la ducha."
    
    $ renpy.music.play("audio/sfx/door_close01.ogg", channel="sfx1",loop=False, fadeout=0.0, synchro_start=True, fadein=0.0)
    
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    
    n "Poco antes de terminar la última tostada, oyes el lejano ruido de la puerta del baño abriéndose."
    
    pt "Seguramente habrá terminado..."

    n "Vuelves tu mirada a tu entrepierna."
    
    scene morning04_bg_bedroom_erection
    show border_lines 02:
        #xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos 0.0 zoom 0.5
    with hpunch
    
    pt "Será cabrón..."

    p "¡¿Aún sigues así?!"
    
    pt "El hecho de imaginármela saliendo de la ducha mojada,"

    pt "no me habrá ayudado mucho..."
    
    jump morning04_NoSex03
            
label morning04_AvoidMasturbation:
    
    scene black with fade
    
    n "Intentas calmarte y apartar las manos de tu entrepierna."
    
    show morning04_bedroom_DMast step02
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade
    
    play sound "audio/characters/didac/moanings04.ogg"
    
    n "Los gemidos femeninos y sensuales ahogados por la almohada como si estuviera siendo forzada" 
       
    n "no te ayudan a tranquilizarte precisamente."
    
    pt "Mierda..."

    extend " así no hay quien se calme..."
    
    n "Te esfuerzas en recordar que la persona que tienes detrás es la misma persona de siempre,"
    
    play sound "audio/characters/didac/moanings05.ogg"
    
    pt "¡Maldito seas [protname]!"

    pt "¡Se trata de Dídac!"

    extend " ¡Tu amigo de siempre!"
        
    pt "¡No puedes ponerte cachondo por él!"
    
    n "Pero esa voz femenina, esos gemidos ahogados, ese sonido al deslizarse la tela..."
    
    n "Imaginando su cuerpo desnudo sobre la alcoba, esas piernas suaves, esos pechos perfectos,"
       
    n "esos labios carnosos siendo mordidos suavemente y de forma sensual para ahogar el ruido..."
    
    play sound "audio/characters/didac/orgasm04.ogg"
    
    d "{size=32}AAhh...{/size}" # Orgasm Moaning. *Gemido agudo femenino* 
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    scene black
    with fade
    
    pt "Mmm..."
    
    pt "Parece que al fin ha llegado al orgasmo..."
    
    play sound "audio/sfx/footsteps_wood01.ogg"
    
    n "Oyes unos pies desnudos tocando el suelo de la habitación y poco después sus respectivos pasos."
    
    scene afternight03_bg shower
    with fade
    
    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=False, fadeout=3.0, synchro_start=True, fadein=3.0)
    
    n "Decides tomarte una buena ducha fría para calmarte."

    scene beds_morning_lightOff_blindUp_DemptyMCempty
    with fade
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    n "Después de la ducha, vuelves con cautela a la habitación y descubres la cama de Dídac vacía."
    
    n "Te vistes y te diriges al comedor."
    
    jump morning04_NoSex02
    
label morning04_MasturbateYes:
    
    n "Sin poder resistir más la tentación, decides hacer lo mismo que ella," 
    
    show morning04_bedroom_DMast step02
    show morning04_bedroom_DMast_blinkeye
    with fade
       
    n "con la esperanza, a ser posible, de ser algo más disimulado."

    n "Intentas mover el antebrazo sin que tu codo se desplace demasiado."

    n "Por suerte, juegas con una ligera ventaja: tú sí estás cubierto por una sábana."

    n "Empiezas moviéndote despacio, sientes que es peor el remedio que la enfermedad."

    n "Porque ahora sí que estás fuera de tus cabales."

    n "Los gemidos femeninos y sensuales ahogados por la almohada como si estuviera siendo forzada"
       
    n "tampoco ayudan a tranquilizarte precisamente."
    
    scene black with fade

    n "Cierras los ojos y no puedes evitar imaginártela desnuda,"
       
    n "detrás de ti," 
    
    n "haciendo lo que sin duda está haciendo."
    
    show morning04_bedroom_DMast step03
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade

    play sound "audio/characters/didac/orgasm02.ogg"

    d "AAhh-MMMMmmm... Ahhmmmm-Ahh..." # Rapidly moans *Gemidos femeninos acelerados* 

    window hide dissolve
    pause
    
    scene black with fade

    n "Oyes sus gemidos menos ahogados, es como si se hubiera sacado parte de la almohada fuera de la boca."

    pt "¿Me habrá descubierto?"
        
    pt "No..."

    pt "No estaría masturbándose si me hubiera descubierto..."
    
    pt "Se hubiera escandalizado o hubiera dicho otra cosa..."

    n "Sientes como tu polla está tan dura que podrías romper una roca con ella."
    
    if morning04_DidacHotforyou_Cond == True:
        
        jump morning04_DidacCatchYou
        
    else:
        
        jump morning04_MasturbateYes_ButNoWork
        
label morning04_MasturbateYes_ButNoWork:
    
    scene black with fade

    play sound "audio/sfx/footsteps_wood01.ogg"
    
    n "Oyes los pasos de pies descalzos que se dirigen a la ducha."
    
    pt "Creo que va a seguir en la ducha..."
    
    pt "¿Se puede saber qué demonios le pasa?"
    
    pt "¡¿Se ha vuelto ninfómana?!"
    
    pt "Aunque debo reconocer que me ha puesto bastante..."
    
    pt "¡[protname]!"
        
    pt "¡Es tu amigo de la infancia y tu compañero de piso!"
    
    pt "¡Deja de pensar en eso!"
    
    jump morning04_NoSex
                                                                                 
label morning04_DidacCatchYou:

    #$ renpy.music.play("audio/sfx/rubbingPussy01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    $ renpy.music.stop(channel='music', fadeout=3.0)

    play music "audio/sfx/birds01.ogg" fadein 3.0 fadeout 3.0
    
    scene black with fade

    n "De pronto, los gemidos de Dídac cesan paulatinamente."

    p "..."

    pt "¿Habrá terminado?"

    pt "Qué raro..."

    extend " no me ha parecido oír que llegara al clímax..."

    pt "Quizás ha sido cuando se ha quitado la almohada de la boca,"

    pt "pero aun así, ha sido como muy suave..."

    play sound "audio/characters/neus/gigglesinister05.ogg"

    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
    
    show morning04_bg_bedroom_neus_a

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent:
        subpixel True
        xanchor 1.4 yanchor 1.7 zoom 0.8
        easein_quad 3.0 xanchor 1.53 yanchor 1.45 zoom 1.0
    show light 01:
        light01_rightside_position

    show light_screen_01:
        light_screen_01_position
        
    show border_lines 02:
        subpixel True
        #xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos 0.0 zoom 0.5 alpha 2.0
        easeout_quad 3.0 alpha 0.0
        
    with hpunch

    pause

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Talking
    with dissolve

    d "Vaya,"

    extend " vaya..."

    d "¿Tan cachondo te has puesto oyéndome?"
    
    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent
    with dissolve

    p "¡Dídac!"
    
    show border_lines
    show morning04_bg_bedroom_dfrontpov_comp empty

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent:
        subpixel True
        xanchor 0.6 yanchor 3.8 zoom 0.35 #Vagina
        #xanchor 1.4 yanchor 1.8 zoom 0.8 #Tetas

    with fade

    window hide dissolve
    pause

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent:
        subpixel True
        easein_quad 30.0 xanchor 1.18 yanchor 1.0 zoom 0.6 #Face

    n "Te sobresaltas en la cama apartando la mano de tu miembro" 
       
    n "e intentando esconderla bajo las sábanas sin que abulte lo más mínimo."

    n "Dídac estaba en frente de la cama completamente desnuda, con los brazos en cruz bajo sus pechos." 

    n "Con los dedos húmedos y con unas gotas resbalándose por su entrepierna."

    p "Dídac..."

    extend " yo..."
    
    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Talking
    with dissolve

    d "¿En qué estabas pensando?"

    d "¿Acaso me has mirado,"

    d "y luego te has puesto a masturbarte mientras me oías?"

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent
    with dissolve

    pt "¡La madre que te parió!"

    extend " Sabías perfectamente que estaba aquí" 
        
    pt "y encima estabas desnuda,"

    extend " ¡y sin disimular lo más mínimo!"

    pt "¡No es culpa mía que la tenga así!"

    p "..."

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Talking
    with dissolve

    d "¿No dices nada?"

    d "Eres un puto depravado mental."
    
    scene morning04_bg_bedroom_takeoutsheet
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with hpunch

    play sound "audio/sfx/fall07.ogg"

    n "De un tirón agarra la sábana que te cubría el cuerpo y la tira al suelo detrás de ella."
    
    scene morning04_bg_bedroom_hidingdick_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.75
        pause 1.0
        easein_quad 1.0 zoom 0.5 xpos 0.5 ypos 0.5 # Whole Image
    show light_screen_01:
        light_screen_01_position
    with vpunch

    play sound "audio/sfx/fall02.ogg"

    n "Dejándote completamente desnudo y al descubierto sin poder ocultar tu polla de modo alguno" 
       
    n "aparte de con tus manos."

    p "¡Dídac!"

    p "¡¿Qué haces?!"
    
    scene morning04_bg_bedroom_neus_a
    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Talking:
        subpixel True
        xanchor 1.18 yanchor 1.0 zoom 0.6 #Face
        easein_quad 10.0 xanchor -0.34 yanchor 0.66 zoom 0.2 #Completo
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
        
    with dissolve

    # Didac Dick Talk

    d "Serás cabrón..."

    extend "¡Es enorme!"

    d "¡Es como mínimo el doble de grande que la mía!"

    d "Ni con las manos te la puedes tapar entera..."

    show morning04_bg_bedroom_dfrontpov_comp mouth_happy_Silent
    with dissolve

    window hide dissolve
    pause

    scene black
    with fade

    $ saturation_tint_level = "default"

    
#10-08    
    scene morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
        
#07d_face

    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3 
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3 

    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.3 ypos 0.3 zoom 0.3

    show light_screen_01:
        light_screen_01_position
        
    show border_lines 02:
        #xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos 0.0 zoom 0.5
        
    with hpunch

    play sound "audio/sfx/fall06.ogg"

    n "Sin darte tiempo a reaccionar se monta desnuda como está encima de ti."
    
    n "Poniendo a escasos centímetros de tu rostro su ardiente y mojada entrepierna."

    #########################################################################################################
    #########################################################################################################
    
    if config.version <= "00.02.03":
        
        jump endupdate

    #########################################################################################################
    #########################################################################################################
    
    show border_lines empty
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve

    p "Dídac..."

    extend " ¿Qué...?"
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face

    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face

    show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth happy_Talking_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve

    d "¿De verdad te estoy poniendo tan cachondo? payaso."
    
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea: 
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Talking_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx02_comp:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        morning04_bg_bedroom_d69_mc_manopolla_pos #Mano Polla
        
    with dissolve

    d "Déjame verla bien, cacho cerdo." 
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve
    
    p "Dídac..."

    extend " ¿Se puede saber qué...?"
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb serious_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
    show morning04_bg_bedroom_d69_07dface_blush 02_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
    show morning04_bg_bedroom_d69_07dface_mouth sad_Talking_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        subpixel True
        xanchor 2.5 yanchor 2.5
        xpos 1.20 ypos 0.90 zoom 0.85 #Mano Polla
        ease 10.0 xpos 1.0 ypos 1.0 zoom .6
        
    with dissolve

    d "¿En qué estarás pensando para tenerla así de dura...?"
    
    show morning04_bg_bedroom_d69_07dface_eyeb sad_comp
    
    show morning04_bg_bedroom_d69_07dface_pupils right02_comp
    
    show morning04_bg_bedroom_d69_07dface_mouth happy_Talking_comp
    
    with dissolve
    
    d "¿No te da vergüenza ponerte así por tu amigo de la infancia?"
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve
    
    p "Serás hijo de..."
    
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve
    
    pt "¡Me estás meneando la polla estando desnudo encima de mí!"
    
    pt "¡¿Cómo quieres que me ponga?!"
    
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve

    p "Dídac..."

    p "Si sigues así..."

    extend " yo no sé si podré..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb serious_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth happy_Talking_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve

    d "¿Qué?"

    extend " ¿Vas a violarme?"
    
    show morning04_bg_bedroom_d69_07dface_mouth happy_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
    with dissolve
                
    menu morning04_Rape:
        
        pt "¿Violar a mi compañero de piso y amigo de la infancia?"
        
        "Si sigues así lo voy a hacer...":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
                  
            jump morning04_IfYouKeepIWill
        
        "¡Jamás haría eso! ¡Y menos con el peligro de que te pudieras quedar embarazada y que jamás pudieras recuperar tu antiguo cuerpo!":
            
            call p_Help
            
            $pl.ch_pts("dp",3)
            
            jump morning04_Never
            
label morning04_IfYouKeepIWill:
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_blush 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve
    
    d "..."
    
    show morning04_bg_bedroom_d69_07dface_pupils left02_comp
    
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Talking_comp
    with dissolve
    
    d "No hay narices, imbécil..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve
    
    p "Y si luego por accidente te dejo preñada, ¿qué?"
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_blush 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Talking_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve
    
    d "Bueno..."

    d "si realmente es eso lo que te preocupa,"

    d "también existe algo llamado condón..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve

    p "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb sad_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_pupils left02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_blush 03_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve

    d "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show border_lines 02:
        #xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos 0.0 zoom 0.5
    with hpunch

    p "¡¿Qué?!"
    
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx02_comp
    with dissolve
    
    pt "¿Qué acaba de decir?"
    
    pt "¿Me ha insinuado que quiere que me lo folle poniéndome un condón?"
            
    jump morning04_Condon


label morning04_Never:
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    show morning04_bg_bedroom_d69_07dface_mouth sad_Talking_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        
    with dissolve
    
    d "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_pupils left02_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_blush 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos -0.1 ypos 0.9 zoom .5
        ease 20.0 xpos 0.9 ypos 0.80 zoom 0.60 #Mano Polla + lejos
        ease 15.0 xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    with dissolve    


    n "Un incómodo silencio se apodera de la habitación."

    n "El sol de la mañana entra con viveza en el habitáculo"
       
    n "y eres capaz de ver mejor el rostro de Dídac con el pelo cayéndole por la gravedad."

    n "Una mandíbula marcada, con unos labios carnosos, ojos azules saltones;"

    n "y, aunque con el cuerpo reducido, seguía manteniendo su marcada musculatura casi carente grasa."

    n "Sus mejillas se enrojecen por un instante y aparta la mirada de ti."
    
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Talking_comp
    with dissolve
    
    d "Bueno..."

    d "si realmente es eso lo que te preocupa,"

    d "también existe algo llamado condón"
    
    show morning04_bg_bedroom_d69_07dface_mouth sad_Silent_comp
    with dissolve
    
    d "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    with dissolve

    p "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb sad_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_pupils left02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_blush 03_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 1.4 ypos 1.5 zoom .8 #Didac Face02
        
    with dissolve

    d "..."
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_blush 01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show morning04_bg_bedroom_d69_07dface_mouth biting_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#06-05
        
    show morning04_bg_bedroom_d69_mc_06-05 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenea:
        xanchor 2.5 yanchor 2.5
        xpos 0.0 ypos 0.0 zoom 0.5 #MC Face
        
    show border_lines 02:
        #xanchor 0.0 yanchor 0.0
        xpos 0.0 ypos 0.0 zoom 0.5
        
    with hpunch

    pt "¡¿Qué?!"

    extend " ¿Qué acaba de decir?"

    pt "¿Me ha insinuado que quiere que me lo folle poniéndome un condón?"
            
    menu morning04_Condon:
        
        pt "Con condón no la dejaría preñada..."
        
        "La verdad es que no es tan mala idea...":
            
            call p_Help
            
            $pl.ch_pts("dp",3)
                
            show border_lines empty
            
        #10-08    
            show morning04_bg_bedroom_d69_mc_10-08 scenea:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
        #07d_face
            show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
            show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
            show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
            show morning04_bg_bedroom_d69_07dface_blush 03_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
            show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
        #06-05
                
            show morning04_bg_bedroom_d69_mc_06-05 scenea:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
        #04mc_mouth
                
            show morning04_bg_bedroom_d69_04mc_mouth sad_Talkingx01_comp:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
        #03-01
                
            show morning04_bg_bedroom_d69_mc_03-01 scenea:
                xanchor 2.5 yanchor 2.5
                xpos 1.65 ypos 1.70 zoom 1.0 #Didac Face
                
            with dissolve
            
            d "..." 
                  
            jump morning04_CondonAfter
        
        "No... yo jamás te haría eso Dídac, ¡eres mi amigo!":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
            
            jump morning04_CondonAfter_myfriend
            
label morning04_CondonAfter_myfriend:
    
    show border_lines empty
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb angry_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_pupils right02_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_blush 00_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero

# Hair 07
    
    show morning04_bg_bedroom_d69_didac_Hair_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#06-05

    show morning04_bg_bedroom_d69_mc_06-05 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    with dissolve
    
    d "..."
    
    show morning04_bg_bedroom_d69_07dface_pupils left02_comp
    with dissolve
    
    d "..."
    
    jump morning04_DidacLeaving

label morning04_CondonAfter:
    
    hide light_screen_01
    show border_lines empty
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 scenea:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#07d_face
    show morning04_bg_bedroom_d69_07dface_eyeb surprise_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_pupils dick02_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_eyes 02_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_blush 03_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    show morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero

# Hair 07
    
    show morning04_bg_bedroom_d69_didac_Hair_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero

        
#06-05

    show morning04_bg_bedroom_d69_mc_06-05 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero

    show light_screen_01:
        light_screen_01_position
        
    with dissolve
    
    d "..."
    
    jump morning04_DidacLeaving
    
label morning04_DidacLeaving:
    
#10-08    
    show morning04_bg_bedroom_d69_mc_10-08 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#07d_face

    hide morning04_bg_bedroom_d69_07dface_eyeb surprise_comp
        
    hide morning04_bg_bedroom_d69_07dface_pupils dick02_comp
        
    hide morning04_bg_bedroom_d69_07dface_eyes 02_comp
        
    hide morning04_bg_bedroom_d69_07dface_blush 03_comp
        
    hide morning04_bg_bedroom_d69_07dface_mouth sadx2_Silent_comp

# Hair 07
    
    hide morning04_bg_bedroom_d69_didac_Hair_comp
        
#06-05

    show morning04_bg_bedroom_d69_mc_06-05 sceneb:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx01_comp:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
#03-01
        
    show morning04_bg_bedroom_d69_mc_03-01 scenec:
        xanchor 2.5 yanchor 2.5
        xpos .5 ypos .49 zoom .23 #Cuerpo Entero
        
    with hpunch
    play sound "audio/sfx/fall06.ogg"

    n "Poco después se aparta de ti y sale de la habitación corriendo."
    
    p "..."

    pt "Está mal..."

    extend " está muy mal..."
    
    pt "¿Se puede saber qué le pasa?"
    
    pt "Unos minutos más así, y sinceramente, creo que no hubiera respondido de mis actos..."
    
    p "..."
    
#04mc_mouth
        
    show morning04_bg_bedroom_d69_04mc_mouth sad_Silentx02_comp
    with dissolve
    
    pt "¿Y ahora cómo bajo esto...?"
    
    jump morning04_NoSex
    
label morning04_NoSex:

    n "Te quedas varios minutos en la cama estirado y pensativo sin saber cómo reaccionar."
    
    jump morning04_NoSex03
    
label morning04_NoSex03:
    
    scene afternight03_bg shower with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    $ renpy.music.stop(channel='music', fadeout=3.0)
    
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=3.0, synchro_start=True, fadein=3.0)
    
    n "Finalmente, decides darte una ducha fría."

    n "Descubres el baño recién usado,"
       
    n "supones que por poco no te encuentras con Dídac otra vez desnuda." 
       
    n "Cuando terminas, te percatas de que es la misma situación que ayer."

    n "La ropa está en tu cuarto, pero por suerte esta vez," 
       
    n "en teoría,"
                   
    n "la habitación está vacía."

    n "Te tapas con una toalla y te diriges a tu habitación." 
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    #scene bedroom_morning_empty with fade
    scene beds_morning_lightOff_blindUp_DemptyMCempty
    with fade

    play music "audio/music/kevinmacleod/senbazuru_restaurant.ogg" fadein 3.0 fadeout 3.0
       
    n "Con un suspiro de relajación, ves que efectivamente, no hay nadie en el cuarto."

    n "Te vistes con ropa de calle y te diriges a la cocina a prepararte el desayuno."
    
label morning04_NoSex02:
    
    scene morning04_bg_livingroom_dbreakfast
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with dissolve

    n "Dídac está sentado encima del sofá con un bol de cereales."
       
    n "Ya no estaba desnuda."

    n "La ropa que llevaba era la suya." 
       
    n "Había escogido ropa que antaño le había resultado exageradamente ceñida con su cuerpo musculado;"

    n "pero con el cuerpo actual -más reducido-, la ropa le resultaba algo más bien holgada."

    n "Aun así, no dejaba de parecer una chica vestida con trajes habitualmente más usados en chicos que en chicas."

    call saturation_ting_values_check
    
    scene morning04_bg_livingroom_others_morning

    show didacfbodybelow naked:
        dfbody_atright_little
    #show didacfbodybelow_naked_drops 00:
        #dfbody_atright_little
    show didacfbodycloth_below_pants:
        dfbody_atright_little
    show didacfhandrb spoon:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    #show didacfbodytop_naked_drops 00:
        #dfbody_atright_little
    show didacfbodycloth_top_maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    #show didacfhandl_hip_naked_drops 00:
        #dfbody_atright_little
    show didacf_blush 00:
        dfexpressions_atright_little
    show didacf_eyes 02:
        dfexpressions_atright_little
    show didacf_pupils front02:
        dfexpressions_atright_little
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_little

    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position

    with dissolve

    p "¿Es que tienes pensado ir a la calle?"
    
    if config.version <= "00.02.04":
        
        jump endupdate

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx04
    with dissolve

    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0

    d "¿Y se puede saber por qué no?"

    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Como me quede un minuto más en este jodido cuchitril"

    d "me voy a volver una puta loca..."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    pt "Otra vez refiriéndose a sí mismo de forma femenina..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "¿Y dónde tienes pensado ir?"
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "¿Por qué?"

    extend " ¿Tienes intención de hacerme de niñera?"

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "Quiero ir a comprar algo de ropa..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "Si tardas en ayudarme lo que sueles tardar,"

    extend " puedo esperar sentada..." 

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx02
    with dissolve
       
    d "al menos sería interesante no sentirme tan incómoda..."
    
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Es evidente -con sus movimientos-, que sus pechos están al aire debajo de esa camiseta que lleva," 

    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve
       
    n "hasta los pezones se le notan duros tras la tela."

    show didacf_eyes 05
    show didacf_pupils left05
    with dissolve

    n "Tampoco es de extrañar, en nuestro piso no hay ningún sujetador."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx04
    with dissolve
        
    n "A cada día que pasa, sus pechos parecen más grandes y sus caderas más anchas."
    
    label morning04_Shopping:
    
    scene morning04_bg_livingroom_others_morning

    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_below_pants:
        dfbody_atright_little
    show didacfhandrb spoon:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    show didacfbodytop_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_top_maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_little
    show didacf_blush 00:
        dfexpressions_atright_little
    show didacf_eyes 02:
        dfexpressions_atright_little
    show didacf_pupils left02:
        dfexpressions_atright_little
    show didacf_eyebrows normal:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Silentx02:
        dfexpressions_atright_little

    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position

    with dissolve
    
    #stop music fadeout 3.0
        
    menu morning04_Shopping_question:
        
        pt "¿Llevo a mi compañero de piso a comprar sujetadores...?"
        
        "Yo podría acompañarte.":
            
            call p_Help
            
            if pl.dp >= 4:
            
                $pl.ch_pts("dp",3)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 4[hd]")
                            
                $ morning04_ShoppingDidac_Cond = True
                
                jump morning04_Shopping_Together
                
            else:
                
                $pl.ch_pts("dp",+1)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 4[hd]")

                $ morning04_Shopping_NotTogether_Cond = True
                            
                jump morning04_Shopping_NotTogether
        
        "Será mejor que vayas a ese lugar tú solo...":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)

            $ morning04_Shopping_Alone_Cond = True
            
            jump morning04_Shopping_Alone
            
        "Si no te hubieras comportado como un imbécil tratando de violar a Neus, esto no te habría ocurrido.":
            
            call p_Help
        
            $pl.ch_pts("dp",-7)

            $ morning04_Shopping_Alone_Angry_Cond = True
            
            jump morning04_Shopping_Alone_Angry
            
            
label morning04_Shopping_NotTogether:

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "Agradezco el detalle."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "Pero prefiero ir solo."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Pero..."

    extend " ¿Por qué?"

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "Sinceramente,"

    extend " creo que prefiero estar solo allí."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx01
    with dissolve
    
    d "No tendrás que cuidar de mí hoy,"

    extend " así que disfruta del día."

    play sound "audio/sfx/door_open01.ogg"
    
    scene morning04_bg_livingroom_others_morning
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with hpunch

    play sound "audio/sfx/door_close01.ogg"
    
    n "Oyes cómo se dirige a la entrada y cierra la puerta."
    
    pt "Me da la sensación de que hay algo en mí que no le acaba de gustar..."
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome

            
label morning04_Shopping_Alone:

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "¿Por qué?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "¿Es que te avergüenzas de ir con tu amigo tetudo a comprar sujetadores?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "¿Se está cachondeando de mí?"
    
    p "No..."

    p "mira,"

    extend " es que creo que..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "No,"

    extend " tranquilo."

    d "No hace falta que te excuses, imbécil,"

    d "te has dado a entender de puta madre."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "Quédate en casa matándote a pajas si quieres,"

    extend " pero yo me largo."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "Oye, no te pongas así..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Ya parece que actúes como una tía..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "¿He dicho eso en voz alta?"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "Vete a tomar por el culo [protname]."
    
    scene morning04_bg_livingroom_others_morning
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with hpunch

    play sound "audio/sfx/door_slam01.ogg"
    
    n "Se levanta de mal humor cogiendo la mochila y sale del piso dando un portazo."
    
    p "Genial, [protname],"

    extend " eres un crack."
    
    window hide dissolve
    
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome

label morning04_Shopping_Alone_Angry:

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx01
    with dissolve
    
    d "¿Qué?"

    d "¿De qué demonios estás hablando?"
    
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Oye,"

    extend " se me están calentando las narices con tu forma de olvidar las cosas que no te interesa recordar..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "¡¿Tienes algún problema conmigo gilipollas?!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Eres un completo imbécil y no pienso ir a hacer el ridículo vistiéndote de mujercita."
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡Nadie ha pedido tu ayuda capullo!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "Búscate la vida con eso,"

    extend " te lo has buscado tú mismo."
    
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "Que tenga tetas no significa que no pueda darte una paliza..."
    
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
       
    d "¡¿Entiendes?!"
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    menu morning04_Shopping_Alone_Angry_Fight:
        
        pt "¿Ahora se pone chulito conmigo?"
        
        "Entonces, ¿a qué esperas?":
            
            call p_Help
            
            $pl.ch_pts("dp",+2)
            
            jump morning04_Shopping_Alone_Angry_Fight_Whatareyouwaiting
            
        "No tengo ganas de darle una paliza a una niñata cobarde que solo se atreve con mujeres indefensas.":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
            
            jump morning04_Shopping_Alone_Angry_Coward
            
label morning04_Shopping_Alone_Angry_Fight_Whatareyouwaiting:
    

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx07
    with dissolve
    
    d "..."

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "¿Qué?"

    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "Mucho hablar,"

    extend " pero cuando tienes que poner en práctica lo que predicas, te rajas enseguida..."
    
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "Da igual que tengas tetas o te hayas quedado sin huevos,"

    p "nunca dejarás de ser el mismo imbécil."
    
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx09
    with dissolve
    
    p "Pero forzar a una chica indefensa en un cuarto de baño,"

    p "eso fue un golpe muy bajo,"

    extend " incluso para ti..."
    
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡Que te den capullo!"

    d "¡No tengo por qué aguantar tanta tontería!"
    
    scene morning04_bg_livingroom_others_morning
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with hpunch

    play sound "audio/sfx/door_slam01.ogg"
    
    n "Se levanta de golpe, coge la cartera con las llaves y sale tras la puerta dando un portazo."
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label morning04_Shopping_Alone_Angry_Coward:
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "Sabes que si no tuviera este cuerpo de mujer,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "ahora mismo estarías retorciéndote de dolor en el suelo."
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "No siempre me has ganado,"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx08
    with dissolve

    p "a diferencia de ti, yo pago la parte del alquiler del piso que me corresponde,"

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "más la parte proporcional que le toca al inútil de mi compañero de piso,"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "porque se pasa el día haciendo gilipolleces en el gimnasio en lugar de ganarse la vida."
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    d "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Total, ¿para qué?"

    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Para terminar forzando a chicas indefensas en cuartos de baño?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡Oye, idiota!"

    d "No sé qué demonios hablas de chicas indefensas," 

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
       
    d "¡pero ten claro que nunca te he pedido que me ayudaras con el alquiler del piso!"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡Siempre lo has hecho porque te ha dado la puta gana!"
    
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Quizás a partir de ahora cambie de idea..."
    
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve
    
    d "..."
    
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "..."
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡Haz lo que te salga de los huevos!"
    
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "Al menos yo aún los conservo..."
    
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx09
    with dissolve
    
    d "..."
    
    scene morning04_bg_livingroom_others_morning
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with hpunch
       
    n "Se levanta de golpe, coge la cartera con las llaves y sale por la puerta dando un portazo."
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
            
        
label morning04_Meritxell_Calling:
    
    scene morning04_livingroom_mc_resting_bg feet01
    with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    play music "audio/music/kevinmacleod/senbazuru_restaurant.ogg" fadein 3.0 fadeout 3.0
    
    n "Pasados unos minutos estando a solas en el piso, decides relajarte un poco en el sofá."

    p "..."

    pt "{i}Dime,{/i}"

    pt "{i}¿Haces algo mañana por el mediodía?{/i}"
    
    pt "¡La chica rubia de clase!"
    
    pt "Es cierto..."

    extend " Me dijo..."
    
    pt "{i}Si te apetece hacer algo,{/i}"

    pt "{i}llámame{/i}."
    
    pt "Tengo su número apuntado en el móvil..."
    
    show morning04_livingroom_mc_resting_bg feet02
    
    show morning04_bg_livingroom_mc_resting_phone 01:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with dissolve
    
    n "Sacas el móvil del bolsillo y escribes en el buscador de nombres \"Rubia Tetuda\"."
    
    n "No se te ocurrió un nombre más original para denominar a esa despampanante mujer."

    call screen phonebuttons()
    
    with dissolve
    
#Not finished /  En teoria debo borrar lo de abajo.
    
    menu morning04_Meritxell_Calling_Decision:
        
        pt "La chica era atractiva, pero no sé ni su nombre..."
        
        "<Pasar de todo el mundo mirando la tele en casa solo>":
            
            call p_Help
        
            jump afternoon04_AloneatHome
         
        "<Llamar a la chica desconocida al móvil para quedar>":
            
            call p_Help
             
            jump morning04_Meritxell_Calling_Decision_Accepted
            
label morning04_Meritxell_Calling_Decision_Accepted:
    
    show morning04_bg_livingroom_mc_resting_phone 02
    with dissolve
    
    gm "¡Hola!"

    gm "¿Quién eres?"

    extend " guapa..."
    
    p "Eumm..."
    
    n "Su voz suena femenina, dulce pero firme."
    
    p " Soy [protname],"

    p "hablamos ayer por la mañana en clase de Ilustración y me diste tu número de teléfono."
    
    gm "..."
    
    p "..."
    
    gm "¿[protname]?"
    
    p "Euh..."

    extend " Sí..."
    
    gm "¿Yo te di mi número de teléfono ayer?"
    
    p "..."

    extend " Sí..."
    
    pt "¡¿Se puede saber por qué la gente tiene esa facilidad para olvidar las cosas?!"
    
    p "Me dijiste que este mediodía lo tenías libre para quedar y poder conocernos mejor..."
    
    gm "..."
    
    p "Aunque si no te va bien, no pasa nad..."
    
    gm "Seh..."

    gm "supongo que me va bien..."
    
    p "..."

    extend " ¿Supone?"
    
    gm "¿Te va bien quedar delante del {b}{i}MACBA{/i}{/b}?"
    
    p "{i}¿MACBA?{/i}"

    gm "..."

    gm "Sabes lo que es,"

    extend " ¿no?"
    
    menu morning04_Meritxell_MacbaQuestion01:
        
        pt "Si le digo que no, quedaré como un ignorante..."
        
        "¡Por supuesto que lo sé!":
            
            call p_Help
            
            gm "Entonces, dime,"

            extend " ¿qué es?"
            
            pt "Será desconfiada..."
            
            jump morning04_Meritxell_MacbaQuestion02
            
        "La verdad es que no tengo ni idea...":
            
            call p_Help
                
            $pl.ch_pts("mp",-2)
            
            gm "Vives en Barcelona y no conoces este sitio..."

            gm "Vaya tela..."
            
            gm "Sus siglas significan,"

            extend " {b}{i}Museu d'Art Contemporani de Barcelona{/i}{/b}."
            
            jump morning04_Meritxell_MacbaQuestion_Right02
    
    menu morning04_Meritxell_MacbaQuestion02:
        
        pt "Supongo que las siglas serán acrónimos de palabras en catalán..."
        
        "{i}Mercat Ecológic Cultural de Barcelona Atípic{/i}.":
            
            call p_Help
            
            jump morning04_Meritxell_MacbaQuestion_Wrong
            
        "{i}Mostra d´Entitas Culinaries de Barcelona Actuals{/i}.":
            
            call p_Help
            
            jump morning04_Meritxell_MacbaQuestion_Wrong
            
        "{i}Museu d'Art Contemporani de Barcelona{/i}.":
            
            call p_Help
            
            $pl.ch_pts("mp",+1)
            
            jump morning04_Meritxell_MacbaQuestion_Right
            
        "{i}Museo de Arte Contemporáneo de Buenos Aires{/i}.":
            
            call p_Help
            
            jump morning04_Meritxell_MacbaQuestion_Wrong
            
        "{i}Mirador Estelar d´Astres Collonuts i Ben Adquirits{/i}.":
            
            call p_Help
            
            jump morning04_Meritxell_MacbaQuestion_Wrong
            
        "<Ponerte borde con ella mandándola a la mierda>.":
            
            call p_Help
            
            jump morning04_Meritxell_MacbaQuestion_Impolite
            

label morning04_Meritxell_MacbaQuestion_Wrong:
    
    $pl.ch_pts("mp",-2)
    
    gm "No..."

    extend " no significa eso."
    
    gm "La respuesta correcta es,"

    extend " {i}\"Museu d'Art Contemporani de Barcelona\"{/i}."
    
    jump morning04_Meritxell_MacbaQuestion_Right02
    
label morning04_Meritxell_MacbaQuestion_Impolite:
    
    $pl.ch_pts("mp",-10)
    
    p "¿Acaso me estás haciendo un interrogatorio?"
    
    p "¿Quién te crees que eres?"
       
    gm "..."

    extend " Tampoco hacía falta ponerse así."
    
    gm "Mira,"

    extend " da igual,"

    gm "No importa."

    gm "De todos modos, tengo otras cosas más importantes que hacer."
    
    gm "Que tengas un buen día, [protname]."
    
    n "Oyes el ruido característico del móvil dando por terminada la conversación."
    
    pt "Humm..."

    pt "Quizás hubiera podido ser un poco más educado..."
    
    pt "No creo que vuelva a hablarme..."
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label morning04_Meritxell_MacbaQuestion_Right:
    
    gm "Así es."
    
    gm "Bueno,"

    extend " veo que por lo menos estás algo informado..."

label morning04_Meritxell_MacbaQuestion_Right02:
    
    gm "En español sería:"

    extend " \"Museo de Arte Contemporáneo de Barcelona\","
    
    gm "realmente la última letra no sé muy bien a qué viene..."
    
    gm "Te espero ahí a las tres de la tarde."

    gm "No llegues tarde."

    extend " ¿De acuerdo?"
    
    p "De..."

    extend " de acuerdo."
    
    show morning04_bg_livingroom_mc_resting_phone 01
    with dissolve

    play sound "audio/sfx/click02.ogg"
    
    n "Oyes el ruido característico del móvil cuando se corta la comunicación."
    
    pt "¿Qué demonios haremos en un museo?"

    pt "¿Qué será lo que me quiere enseñar?"
    
#########################################################
    
    if config.version <= "00.06.05": 
        
        call endupdatescript
    
#######################################################
    
    window hide dissolve
    pause
    
    jump afternoon04_TxellMacba
        

label afternoon04_AloneatHome:

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    play music "audio/music/kevinmacleod/bittersweet.ogg" fadeout 1.0 fadein 1.0
    
    scene  morning04_livingroom_mc_resting_bg feet01
    with fade
    
    n "Pasas la tarde mirando la televisión sin saber exactamente qué hacer."

    if aftermorning05_AfterDeepsea_PublicSex_No_DidacAccept_Cond == True:

        n "De tanto en tanto, oyes golpes, gemidos y gruñidos en vuestra habitación,"

        n "pero prefieres no ir a investigar la situación, por si complicas más las cosas."

    else:
    
        n "Más de una vez te pasa por la cabeza ir en busca de Dídac,"
    
        show morning04_livingroom_mc_resting_bg feet02
        
        show morning04_bg_livingroom_mc_resting_phone didac:
            
            xpos 0.485 ypos 0.125
            
        show morning04_livingroom_mc_resting_handphone
        with dissolve
        
        n "pero por mucho que le llames al móvil, no recibes respuesta alguna."

        scene  morning04_livingroom_mc_resting_bg feet01
        with dissolve
        
        n "Está claro que no está de muy buen humor."
    
    n "Pronto será de noche y será hora de tener una segunda cita con la {b}\"bruja\"{/b}."
    
    window hide dissolve
    pause
    
    jump night04_restaurant
            
label morning04_Shopping_Together:
    
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "¿Acompañarme?"
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "¿Qué?"

    p "No sería la primera vez que voy a un centro comercial con una chica para acompañarla de compras."
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx03
    with dissolve

    d "Si al final es galán y todo el capullo este..."
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx03
    with dissolve

    p "Bueno,"

    extend " tranquilo,"

    p "que si voy a molestarte, no vendré."
    
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "Pse..."

    extend " ¿Por qué no?"

    d "Tampoco es que tenga puñetera idea de ropa femenina..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "..."

    pt "Como si yo sí,"

    extend " no te jode..."
    
    window hide dissolve
    pause
    
    jump aftermorning04
    
label aftermorning04:
    
    scene aftermorning04_bg lingeriestore
    with fade

    stop music fadeout 3.0

    $ renpy.music.set_volume(0.8, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_shop01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    if config.version <= "00.02.05":
        
        jump endupdate
    
    d "Oye [protname]..."

    d "Esto de copa {b}\"B\"{/b},"

    extend " ¿qué coño significa?"

    $ renpy.music.set_volume(0.5, delay=10.0, channel='sfx1')

    n "Para ser un sábado por la mañana la gran superficie en la que nos encontrábamos estaba bastante llena."

    n "Estábamos en la planta de ropa íntima femenina, que es básicamente la parte que más urgencia le corría a Dídac."

    p "Me imagino que con copa se refieren al tamaño o a la forma del pecho..."

    n "Dídac estaba sujetando un sujetador de color violeta oscuro" 
       
    n "y estaba mirando la etiqueta sin comprender demasiado lo que significa su contenido."

    play music "audio/music/alcaknight/thinking_of_you.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.set_volume(0.05, delay=30.0, channel='sfx1')

    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_below_pants:
        dfbody_atright_little
    show didacfhandrb brabasic:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    show didacfbodytop_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_top_maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_little
    show didacf_blush 00:
        dfexpressions_atright_little
    show didacf_eyes 02:
        dfexpressions_atright_little
    show didacf_pupils downLeft02:
        dfexpressions_atright_little
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_little
    #show didacfbodytop_hair:
        #dfbody_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Talkingx003:
        dfexpressions_atright_little
    with dissolve
    
    d "Entonces,"

    d "¿significa tamaño"

    extend " o forma?"

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "Y si es forma,"

    extend " ¿qué forma es la {b}B{/b}?"

    d "¿Y qué diferencia hay con la puñetera a?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "¿Es como la {b}S{/b} en ropa que significa {i}small{/i}?"
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "..."

    p "Dídac..."

    extend " No tengo ni zorra..."
    
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "Joder..."

    extend " no me atrevo a preguntar."

    d "¡Pensarán que soy una imbécil!"
    
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    pt "Una..."
    
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "[protname]..."

    extend " pregúntale a alguien si sabe lo que significa."
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx01
    with dissolve

    p "Tú estás majara..."

    extend " pensarán que soy un puñetero depravado mental."
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx02
    with dissolve

    play sound "audio/characters/didac/pff01.ogg"

    d "Pfff..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "es lo que eres,"

    extend " ¿no?"
    
    if morning04_DidacHotforyou_Cond == True:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx002
        with dissolve

        d "Lo de esta mañana no ha sido precisamente de niño angelical..."
        
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex02
        show didacf_mouth happy_Silentx02
        with dissolve
        
        p "..."
        
    else:
        
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx04
        with dissolve
        
        p "..."
        
    if morning04_DidacHotforyou_Cond == True:
        
        show didacf_mouth sad_Silentx03
        with dissolve

        p "Como que lo tuyo sí era de niña inocente..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "Oh..."

    extend " vamos,"

    d "puedes ir a preguntárselo a una dependienta sexy si quieres" 
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx03
    with dissolve
       
    d "y te haces el tonto como si intentaras ligar con ella."
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx04
    with dissolve
    
    d "O eres tú mismo,"

    d "tampoco es que haya mucha diferencia..."
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex02
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "Me dirás que nunca has usado esa técnica para ligar."
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Yo no soy de los que liga con mujeres en espacio y horario laboral..." 
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx05
    with dissolve
       
    p "me parece de muy mal gusto."
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "Tú y tus jodidas normas morales estúpidas."
    
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx05
    with dissolve

    d "Aquí todas las que trabajan son unas putas cachondas mentales..."
    
    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx06
    with dissolve
       
    d "se pasan el jodido día tocando ropa íntima,"

    extend " sujetadores,"

    extend " tangas,"

    extend " calcetines..."
    
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "¿Qué tiene que ver ser una cachonda mental con estar tocando calcetines?"
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx001
    with dissolve

    d "Desde luego,"

    extend " qué poca imaginación tienes, macho..."
    
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx04
    with dissolve

    p "O tú estás muy enfermo..."
    
    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve
    
    g01 "{size=15}Pero,{/size}"

    extend "{size=15} ¿Has visto como va vestida?{/size}"
    
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve
    
    g02 "{size=15}Pero si casi se le ve el pezón...{/size}"

    show didacf_eyes 00
    show didacf_pupils down00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx04
    with dissolve
    
    b01 "{size=15}No sé...{/size}"

    extend "{size=15} ¡Pero está un rato buena!{/size}"

    show didacf_eyes 03
    show didacf_pupils down03
    with dissolve
    
    n "Un número considerable de personas estaban observando de forma poco discreta a Dídac."

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx01
    with dissolve
    
    g01 "{size=15}Te das cuenta de que estoy aquí,{/size}"

    extend "{size=15} de que soy tu jodida novia,{/size}"

    extend "{size=15} y de que te he escuchado;{/size}"

    g01 "{size=15}¿¿verdad??{/size}"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    b01 "..."
    
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    g02 "{size=15}Pero ¿Cómo no se va a fijar?{/size}"

    extend "{size=15} ¡Si va vestida como una fulana...!{/size}"
    
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve

    play music "audio/music/alcaknight/bury_it.ogg" fadein 0.0 fadeout 3.0
    
    d "{size=45}¡OID IMBÉCILES!{/size}"

    show didacf_mouth sad_Talkingx08
    with dissolve
       
    d "{size=45}¡Si tenéis algo que decirme!...{/size}"

    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "{size=45}¡¡DECÍDMELO EN LA PUTA CARA!!{/size}"
    
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve

    g02 "..."
    
    g02 "{size=15}Creo que nos ha oído...{/size}"

    g01 "..."
    
    g01 "{size=30}¡¿Tú crees?!{/size}"
    
    p "Dídac,"

    extend " tranquilízate."

    p "Estamos en un centro comercial lleno de gente."
    
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "{size=45}¡Les voy a partir la puta cabeza!{/size}"
    
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    $ morning04_ShoppingDidac_Cond = True
    
    menu aftermorning04_calmdidac:
        
        pt "Si no detengo a Dídac, va a montar un pollo de mil narices..."
        
        "<No hacer nada>":
            
            call p_Help
                  
            jump aftermorning04_calmdidacNo

            $ aftermorning04_calmdidac_Failed = True
        
        "<Hacerle entrar en razón y tranquilizarlo/a>":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
            
            jump aftermorning04_calmdidacYes
            
label aftermorning04_calmdidacNo:
    
    scene aftermorning04_bg lingeriestore
    with dissolve
    
    n "Dídac se dirige con paso firme a plantarles cara a esos desconocidos."
    
    b01 "¡Oye!"

    extend " Que la tía buen..."

    extend " digo,"

    b01 "¡la loca semidesnuda se acerca!"

    scene hit_15:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_16:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_17:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_21:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_22:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_23:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    scene hit_24:
        truecenter
        rotate 90
        zoom 1.5
    pause 0.05
    
    scene aftermorning04_bg_fittingroomout_grabshoulder_bg_02:
        subpixel True
        xalign 0.0
        linear 0.5 xalign 1.0
        repeat
    #scene black
    show aftermorning04_bg_lingerieshop_punch_comp:
        subpixel True
        truecenter
        zoom 0.1
        zoom 0.75
        easein_quad 1.0 zoom 0.5
    with dissolve

    play sound "audio/sfx/punch01.ogg"
    
    g01 "{size=80}¡AAAAAH!{/size}" # *Scream after recieving a punch on her face*
    
    d "¡¡¿A quién llamas fulana ahora?!! ¡¡Asquerosa rata!!"
    
    g02 "{size=50}¡SOCORRO!{/size}"

    g02 " ¡Que alguien nos ayude!"

    extend " ¡Nos ataca una loca!"
    
    scene aftermorning04_bg lingerieshop_punch 02
    with fade_long305s
    
    n "A los pocos minutos llegan unos guardias de seguridad"
       
    n "que detienen a Dídac, el cual seguía golpeando a esas chicas."
    
    menu aftermorning04_lingerishopafterpunch_question:
        
        pt "¿Qué se supone que debo hacer ahora? Ha sido culpa suya..."
        
        "<Irte a casa>":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
                  
            jump aftermorning04_afterpunchGoHome
        
        "<Acompañarlo/a, aunque pierdas toda la tarde, y quizás la noche>":
            
            call p_Help
            
            $pl.ch_pts("dp",+3)

            $ aftermorning04_lingerishopafterpunch_stay = True
            
            jump aftermorning04_afterpunchGoWithDidac
            
label aftermorning04_afterpunchGoHome:
    
    pt "¡¿Por qué debería acompañarlo?!"

    pt "¡Ha sido su puñetera culpa!"
    
    pt  "Él ha decidido venir aquí así y ha sido él quien no ha sabido controlarse..."
    
    pt "Además, si lo acompaño es posible que se haga demasiado tarde y no pueda asistir a la cita con Neus..."
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label aftermorning04_afterpunchGoWithDidac:
    
    n "Decides acompañar a tu compañero a comisaría."
    
    pt "Si lo hubiera detenido antes,"

    extend " esto no habría pasado..."
    
    pt "Es un gilipollas..."

    pt "pero es mi amigo,"

    extend " el gilipollas..."
    
    window hide dissolve
    pause
    
    show aftermorning04_bg lingerieshop_punch 03
    with fade

    play music "audio/music/kevinmacleod/senbazuru_restaurant.ogg" fadein 3.0 fadeout 3.0
    
    n "La burocracia es un proceso lento y tedioso,"
       
    n "así que pasas el resto de la tarde sentado en una sala de espera repleta de caras desconocidas y siniestras."
    
    n "El sol empieza a esconderse en el horizonte y pronto será la hora de la cita con Neus."
    
    window hide dissolve
    pause

    scene aftermorning04_lingerieshop_prison_background
    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_below_pants:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    show didacfbodytop_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_top_maleshirt:
        dfbody_atright_little
    show didacfhandr_leg_maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_little
    show didacf_blush 00:
        dfexpressions_atright_little
    show didacf_eyes 04:
        dfexpressions_atright_little
    show didacf_pupils left04:
        dfexpressions_atright_little
    show didacf_eyebrows sadx01:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_little

    show aftermorning04_lingerieshop_prison_bars
    with fade
    
    d "..."
    
    p "Dídac..."

    extend " ¿Por qué coño lo has hecho?"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "Ya sabes cómo soy..."

    extend " ¡Joder!..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "Si sabes como me pongo;"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡¿Por qué no me detuviste?!"
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve
    
    pt "No..."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve

    pt "si aún será culpa mía,"

    extend " no te jode..."
    
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "Me han dicho que, si me comporto,"

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "podré salir antes de la medianoche."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Putos exagerados de mierda..."
    
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "Para un jodido yonki de la calle que roba a diario lo sueltan en cinco minutos..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Y a mí, que nunca he hecho nada a nadie,"

    extend " me encierran aquí toda una puta tarde..."
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Hombre,"

    extend " teniendo en cuenta que les has dejado una cara nueva a los tres,"
    
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve
       
    p "yo no me quejaría por el castigo que te han dado..."
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "¿Nunca ha hecho nada a nadie?"

    extend " Y encima se lo cree..."
    
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Escucha..."

    p "Me sabe mal dejarte aquí,"

    extend " pero tengo que irme ya."
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "Joder..."

    extend " ¡¿Me vas a dejar solo en este puto tugurio?!"
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Si tu memoria aún recuerda algo,"

    p "sigo intentando ayudarte a volver a tu forma original..."
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    d "..."
    
    p "Y si no me voy ya,"

    p "tendré complicaciones para devolverte la polla..."
    
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."
    
    p "¿Me quedo entonces?"
    
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Lárgate ya."
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx03
    with dissolve
    
    window hide dissolve
    pause
    
    jump night04_restaurant
            
label aftermorning04_calmdidacYes:
    
    p "Y se te van a ver los pechos,"

    p "vas a montar un espectáculo,"

    p "te van a echar a la calle y seguirás igual de vestida e incómoda..."
    
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    d "..."
    
    b01 "{size=15}Quizás deberíamos acercarnos y preguntarle si ese tío es..."

    extend "{size=15} digo pedirle disculpas...{/size}"
    
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx09
    with dissolve

    g01 "..."
    
    g01 "{size=15}¡Larguémonos!{/size}"
    
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve
    
    d "..."
    
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Bueno,"

    extend " supongo que lo mejor será probar estos sujetadores y comprobar qué tal quedan..."
    
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    window hide dissolve
    pause
    
    scene aftermorning04_bg fittingroomout
    with fade

    play music "audio/music/alcaknight/thinking_of_you.ogg" fadein 3.0 fadeout 3.0
    
    n "Te quedas detrás de las cortinas de los probadores," 
       
    n "esperando a que Dídac decida qué sujetador es el que le resulta más cómodo."

    n "Aunque la planta está bastante llena, en los probadores apenas hay otra mujer, Dídac y tú."

    d "Hmmm..."

    d "no sé..."

    d "Creo que este sujetador resulta más agradable a la vista," 
       
    d "pero no creo que sea de mi jodida talla..."

    n "Oyes la voz de Dídac tras la cortina."
    
    scene aftermorning04_bg_fittingroomout_grabshoulder_comp:
        truecenter
        zoom 1.0
        #zoom 1.5 xpos 0.2
        #pause 2.0
        #easein_quad 1.5 zoom 1.0 xpos 0.5
    #with hpunch

    window hide dissolve
    pause

    n "De pronto, sientes un agarrón en el hombro que te arrastra hasta dentro del reducido habitáculo del probador."

    p "¡Dídac!"

    extend " ¿Qué haces?"
    
    #scene aftermorning04_bg fittingroomin #It´s included inside the contain scene.
    show aftermorning04_fittingroomin_didacshh:
        subpixel True
        zoom 3.0 xanchor 0.56  yanchor 0.66 #Down
        easein_quad 25.0 zoom 3.0 xanchor 0.57 yanchor 0.27
        
    with fade


    d "<{size=18}Shhh...{/size}>"

    d "<{size=18}No hagas ruido.{/size}>"

    d "<{size=18}Necesito tu consejo en esto.{/size}>"

    n "Una vez dentro del probador ves a tu amigo de la infancia" 
       
    n "como una preciosa mujer llevando un sujetador violeta evidentemente pequeño para su busto."

    n "Pareciéndose más a un corsé super ajustado, casi como si fuera a estallar."
    
    scene aftermorning04_bg fittingroomin

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties 01:
        dfbody_atright_closex2
    show didacfbodytop brabasic:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 01:
        dfexpressions_atright_closex2
    show didacf_eyes 03:
        dfexpressions_atright_closex2
    show didacf_pupils front03:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happy_Talkingx04:
        dfexpressions_atright_closex2
    with fade

    d "<{size=18}¿Cómo lo ves?{/size}>"
    
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx05
    with dissolve

    p "<{size=18}Euh..."

    extend " Bueno...{/size}>"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx04
    with dissolve

    p "<{size=18}Creo que te va un poco demasiado ajustado...{/size}>"

    show didacf_eyes 01
    show didacf_pupils down01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "¿Tú crees?"
    
    show didacfhandr empty
    show didacfhandl empty

    show didacfbodytop brabasic_grab
    show didacfhandx2 grabtits
    show didacf_eyes 02
    show didacf_pupils down02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx05
    with dissolve

    d "Hummm..."

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "A mí siempre me han gustado las mujeres con el pecho bien apretujado."

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx03
    with dissolve

    d "Yo me veo sexy."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "Aunque quizás sí que me los noto un poco demasiado ajustados..."
    
    show didacfhandx2 empty
    show didacfhandl hip_naked
    show didacfhandr leg_naked
    show didacfbodytop brabasic
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx04
    with dissolve

    pt "Un poco dice..."

    scene aftermorning04_bg fittingroomin

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties 01:
        dfbody_atright_closex2
    show didacfhandrb brablack:
        dfbody_atright_closex2
    show didacfbodytop naked:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 01:
        dfexpressions_atright_closex2
    show didacf_eyes 04:
        dfexpressions_atright_closex2
    show didacf_pupils left04:
        dfexpressions_atright_closex2
    show didacf_eyebrows normal:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happy_Silentx01:
        dfexpressions_atright_closex2
    with dissolve

    d "Hummm..." 

    show didacf_eyes 02
    show didacf_pupils down02
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx02
    with dissolve
       
    d "La verdad es que son bastante incómodos..."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "{size=30}¡Dídac!{/size}"

    extend "{size=30} ¡Que estoy aquí!{/size}"
    
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "Ya lo sé..."

    extend " no me importa."

    d "Nunca hemos tenido pudor tú y yo estando en casa."
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    p "<{size=18}¡Porque antes eras un tío igual que yo!{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx01
    with dissolve
    
    n "Intentas volver a bajar la voz al darte cuenta de que ibais subiendo el volumen al ir alterándoos."
    
    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve

    de "¿Va todo bien ahí dentro?"
    
    #$pl.ch_pts("dp",0) #PROVE POINTS!
    
    scene aftermorning04_fittingrass 01:
        subpixel True
        zoom 3.0 xpos 0.0 ypos -1.0 #Inicio
        ease_cubic 20.0 xpos 0.0 ypos 0.0 #Rostro
        ease_cubic 30.0 zoom 2.0 xpos -1.0 ypos -0.8
    with fade
    
    if config.version <= "00.02.06":
        
        jump endupdate

    n "Oís la voz de la dependienta encargada de la sección que os llama la atención."

    n "Dídac se pone delante de la cortina dándote la espalda abriendo una porción pequeña de la tela"

    n "para hablar con la dependienta."

    d "Sí,"

    extend " sí,"

    d "va todo bien."

    n "Su voz denota que habla con una sonrisa de oreja a oreja."

    n "Sin quererlo, o al menos eso es lo que crees," 
       
    n "sus nalgas están chocando directamente contra tu cadera," 
       
    n "acariciando suavemente tu entrepierna."

    pt "La madre que lo parió..."

    d "Por cierto,"

    d "sé que sonará estúpido,"

    d "pero, exactamente,"

    extend " ¿qué significa copa \"B\"?"

    n "Oyes el ruido de confusión que suelta la dependienta al oír esa pregunta."
    
    show aftermorning04_fittingrass 02:
        subpixel True
        zoom 2.0 xpos -1.0 ypos -0.8 #PrimerplanoPollaculo
        ease_cubic 20.0 zoom 1.5 xpos -0.5 ypos -0.5 #polla dura alejada 
    with dissolve

    n "Sin poder evitarlo, sientes cómo tu miembro va creciendo en tamaño al tener en contacto las suaves nalgas de Dídac."

    de "Bueno..."

    de "Las tallas del sujetador,"

    extend " 85,"

    extend " 90,"

    extend " 95,"

    extend " etcétera..."

    de "Se refieren al contorno de pecho."
    
    if pl.dp >= 15:## FUCKING PROVE NOT FINISHED
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 15[hd]")
        
        show aftermorning04_fittingrass 02tight
        with dissolve
        
        p "..."
        
        pt "Parece como si empezara a humedecerse..."

    de "Las tallas de copa,"

    d "bien sea A,"

    extend " B,"

    extend " C,"

    extend " D," 
        
    de "se refieren al tamaño del aro,"

    extend " y la profundidad de espacio en que se aloja el seno."

    pt "Lo que me faltaba..."

    extend " escuchar sobre senos..."

    pt "¡Qué puñetas!" 
    
    if pl.dp >= 15:## FUCKING PROVE NOT FINISHED
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 15[hd]")
        
        show aftermorning04_fittingrass 04:
            subpixel True
            zoom 1.5 xpos -0.5 ypos -0.5 #polla dura alejada
            ease_cubic 20.0 zoom 1.0 xpos 0.0 ypos 0.0 #All Image 
        with dissolve
        
    elif pl.dp >= 10:
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 10[hd].[p_but] 15[hd]")
        
        show aftermorning04_fittingrass 03:
            subpixel True
            zoom 1.5 xpos -0.5 ypos -0.5 #polla dura alejada
            ease_cubic 20.0 zoom 1.0 xpos 0.0 ypos 0.0 #All Image 
        with dissolve
        
    else:
        
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 10[hd]")
        
        show aftermorning04_fittingrass 02:
            subpixel True
            zoom 1.5 xpos -0.5 ypos -0.5 #polla dura alejada
            ease_cubic 20.0 zoom 1.0 xpos 0.0 ypos 0.0 #All Image 
        with dissolve
        
    if pl.dp >= 10:

        play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
        
        pt "¿Me lo parece a mí o Dídac está moviendo su culo a propósito para restregármelo mejor contra mi polla?"

    de "Si la copa es A,"

    extend " es que tienes busto de deportista de atletismo profesional."

    de "Si la copa es B,"

    extend " es que tienes un busto mediano."

    p "..."

    pt "Estos shorts que lleva son muy finos..." 
        
    pt "en realidad parece que esté desnuda..."

    de "Si la copa es C tienes un busto considerable."
    
    if pl.dp >= 15:
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 15[hd]")
        
        show aftermorning04_fittingrass 04wet
        with dissolve
        
        p "..."
        
        pt "¡¿Qué diablos?!"

        pt "¡Pero si me está dejando empapado!"
        
    elif pl.dp >= 10:
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 10[hd], [p_but] 15[hd]")
        
        show aftermorning04_fittingrass 04
        with dissolve
        
        pt "Parece como si empezara a humedecerse..."
        
    else:
        
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 10[hd]")
        

    de "Y así sucesivamente hasta llegar a la K, al menos en este gran almacén."

    de "Espero que te haya servido de ayuda."
    
    if pl.dp >= 10:

        play sound "audio/characters/didac/moanings06.ogg"

        d "Mmmmm..." # Muffled moaning, while speaking with shop assistant *Gimoteo femenino* 

        n "Su voz reflejaba algo más que duda..."
    
    if pl.dp >= 15:
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 15[hd]")
        
        d "..."

        d "Y si..."

        extend " quiero conseguir un sujetador..."

        d "como este, pero algo más grande..."
           
        extend " ¿dónde puedo encontrarlo...?"
        
    else:
        
        d "Y si quiero conseguir un sujetador como este pero algo más grande,"

        d "¿dónde puedo encontrarlo?"
        
    menu aftermorning04_FittingRoom:
        
        pt "Ya no puedo aguantarlo más... me va a explotar..."
        
        "<Bajarle los pantalones y meterle la polla de golpe>":
            
            call p_Help
            
            if pl.dp >= 20:
            
                $pl.ch_pts("dp",2)
                
                $ aftermorning04_FittingRoom_FuckherConsent = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 20[hd]")
                                  
                jump aftermorning04_FittingRoom_RapeVagina
            
            else:
                            
                jump aftermorning04_FittingRoom_RapeVagina
                
        "<Bajarle los pantalones y poner la polla sobre sus nalgas>":
            
            call p_Help
            
            if pl.dp >= 15:
            
                $pl.ch_pts("dp",2)
                
                $ aftermorning04_FittingRoom_ButtocksDickOver = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 15[hd]")
                                  
                jump aftermorning04_FittingRoom_RapeButtocks
            
            elif pl.dp >= 10:
                
                $pl.ch_pts("dp",1)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 10[hd], [p_but] 15[hd]")
                            
                jump aftermorning04_FittingRoom_RapeButtocks
                
            else:
                
                $pl.ch_pts("dp",-1)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 10[hd]")
                            
                jump aftermorning04_FittingRoom_RapeButtocks
        
        "<Aguantar estoicamente>":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
            
            jump aftermorning04_FittingRoom_Endure
        
label aftermorning04__OutFittingRoom:
    
    if aftermorning04_FittingRoom_FuckherConsent == True:

        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        
        scene aftermorning04_bg lingeriestore

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 02:
            dfexpressions_atright_closex2
        show didacf_eyes 04:
            dfexpressions_atright_closex2
        show didacf_pupils down04:
            dfexpressions_atright_closex2
        show didacf_eyebrows sadx01:
            dfexpressions_atright_closex2
        show didacfbodycloth_top maleshirt:
            dfbody_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Silentx01:
            dfexpressions_atright_closex2
        with fade
        
        d"..."
          
        n "La dependienta seguía observándoos con cara de pocos amigos."

        show didacf_blush 02
        show didacf_eyes 02
        show didacf_pupils left02
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx003
        with dissolve
        
        d "[protname]..."

        d "¿Qué..."

        extend " ha pasado ahí dentro?"

        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx03
        with dissolve
        
        menu aftermorning04__OutFittingRoom_Whathappened:
            
            pt "¡¿Que qué ha pasado?! Tendrá morro..."
            
            "Dídac... Me has estado frotando la polla en toda tu empapada jamona...":
                
                call p_Help
            
                $pl.ch_pts("dp",1)
                                  
                jump aftermorning04__OutFittingRoom_Ashamed
                
            "¿Quizás que has estado frotándome la polla porque querías que te violara?":
                
                call p_Help
            
                $pl.ch_pts("dp",2)
                                  
                jump aftermorning04__OutFittingRoom_Ashamed
                
label aftermorning04__OutFittingRoom_Ashamed:

    show didacf_blush 04
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows surprisex01
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    d "..."

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx01
    with dissolve
    
    d "[protname],"

    extend " creo que lo mejor sería que nos separásemos..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    pt "¡¿Qué?!"

    extend " ¡¿Ahora dirá que es mi culpa?!"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "Adiós."
    
    scene aftermorning04_bg lingeriestore
    with dissolve
    
    n "No te da tiempo a darle una respuesta y ya la ves corriendo escaleras abajo desapareciendo de tu vista."
    
    p "..."

    pt "De todos modos tampoco puedo quedarme aquí."

    pt "Esa jodida dependienta no me ha quitado aún los ojos de encima..."
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
        
label aftermorning04_FittingRoom_RapeVagina:
    
    if aftermorning04_FittingRoom_FuckherConsent == True:
        
        scene aftermorning04_fittingrass 05wetx2penetration
        with vpunch

        d "¡[protname]!"

        extend " ¿Qué...?"
        
        if config.version <= "00.02.07":
            
            jump endupdate
        
        scene aftermorning04_fittingrass 06wetx2penetrated
        with hpunch

        play sound "audio/characters/didac/orgasm01.ogg"
        
        d "{size=70}AAAAAAAAHHH...{/size}" # Loud moan *Gemido agudo* 
        
        de "..."

        de "Por favor,"

        extend " salgan inmediatamente de los probadores,"

        de "o llamaré a seguridad."
            
        window hide dissolve
        pause
            
        jump aftermorning04__OutFittingRoom
        
    elif pl.dp >= 10:
        
        $ pl.ch_pts("dp",-2)
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 10[hd], [p_but] 20[hd]")
        
#image aftermorning04_fittingrass 05wetx2penetration: #-----------MODIFICATED FOR not Consent
    
        scene aftermorning04_fittingrass bg:
            zoom 0.5
        
        show aftermorning04_fittingrass_dface lookback:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_lookback_drops 01:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
         
        show aftermorning04_fittingrass_dface_blush 01:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_eye 02:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18 
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_pupil rightsurprise02:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18 
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_mouth sadx2_Talking:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18 
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18 

        show aftermorning04_fittingrass_dface_eyebrows angry:
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18 
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            subpixel True
            subpixel True
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
        
        show bsmoke 01:
            subpixel True
            xanchor -0.8 yanchor -1.0 rotate -30 size (100, 100) alpha 1.0 #zoom 0.15
            pause 3.0
            easein_cubic 5.0 xanchor 0.5 yanchor 0.5 rotate 0 size (250, 250) alpha 0.0  #2nd Pose
            repeat
        
        show bsmoke 02:
            subpixel True
            alpha 0.0
            pause 3.0
            pause 1.66
            xanchor -0.8 yanchor -1.0 rotate -30 size (100, 100) alpha 1.0 #zoom 0.15
            easein_cubic 5.0 xanchor 0.5 yanchor 0.5 rotate 0 size (250, 250) alpha 0.0  #2nd Pose
            repeat
        
        show bsmoke 03:
            subpixel True
            alpha 0.0
            pause 3.0
            pause 3.33
            xanchor -0.8 yanchor -1.0 rotate -30 size (100, 100) alpha 1.0 #zoom 0.15
            easein_cubic 5.0 xanchor 0.5 yanchor 0.5 rotate 0 size (250, 250) alpha 0.0  #2nd Pose
            repeat
        
        show bsmoke 04:
            subpixel True
            alpha 0.0
            pause 3.0
            pause 5.0
            xanchor -0.8 yanchor -1.0 rotate -30 size (100, 100) alpha 1.0 #zoom 0.15
            easein_cubic 5.0 xanchor 0.5 yanchor 0.5 rotate 0 size (250, 250) alpha 0.0  #2nd Pose
            repeat
        
        show aftermorning04_fittingrass_dbody naked_wet02:
            zoom 0.5
            
        show aftermorning04_fittingrass_dbody_cum empty:
            zoom 0.5
        
        show aftermorning04_fittingrass_dlegr_naked wet01:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0
        
        show aftermorning04_fittingrass_dlegr tightwet01:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down
            
        show aftermorning04_fittingrass_mcbody_dick 03_dry:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.1 ypos 0.0 rotate -90 #inicial and 2nd pose
            pause 1.0
            ease_quad 1.0 xpos 0.2 ypos 0.0 rotate -35 #3rd pose
            ease_expo 1.3 xpos 0.1 ypos 0.0 rotate -35 #4rd pose penetration
            
        show aftermorning04_fittingrass_dlegrover_naked wet01:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 0.0
            pause 0.7 alpha 0.0
            linear 1.0 alpha 1.0
            pause 1.0
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2 alpha 1.0
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0 alpha 1.0
            
        show aftermorning04_fittingrass_mcbody_down_naked 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 # 2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.15 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mcbody_down 02:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.1 ypos 0.6 rotate 0 #pants down
            alpha 0.0
            
        show aftermorning04_fittingrass_mcbody_top 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 #2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.15 ypos 0.0 rotate 0 #4rd pose penetration

        
        show aftermorning04_fittingrass_dlegl_naked wet01:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0
            
        show aftermorning04_fittingrass_dlegl tightwet02:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down
            
        show aftermorning04_fittingrass_mchand empty:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with vpunch

        stop music fadeout 0.5

        play sound "audio/sfx/slap01.ogg"
        
        d "<{size=17}¡¿Qué...?!{/size}>" 
        
        if config.version <= "00.02.07":
            
            jump endupdate
        
        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
             
        show aftermorning04_fittingrass_dface_blush 00:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_dface_eye 06:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2 
            
        show aftermorning04_fittingrass_dface_pupil empty:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_dface_mouth sadx4_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2

        show aftermorning04_fittingrass_dface_eyebrows angryx02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_mcbody_dick 03_wet01:
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.05 ypos 0.0 rotate -36

        show aftermorning04_fittingrass_mcbody_down_naked 03:
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mcbody_top 03:
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mchand:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with hpunch

        play sound "audio/characters/didac/scream05.ogg"
        
        d "{size=60}¡¡¡¡AAAAAAAH!!!!{/size}" # *Scream of Pain after being hardly penetrated*
        
        jump aftermorning04_FittingRoom_RapeVagina_Angry
        
    else:
        
#image aftermorning04_fittingrass 05wetx2penetration: #-----------MODIFICATED FOR not Consent
    
        scene aftermorning04_fittingrass bg:
            zoom 0.5
        
        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
         
        show aftermorning04_fittingrass_dface_blush 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_eye 02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dface_pupil rightsurprise02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18 
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18 
        
        show aftermorning04_fittingrass_dface_mouth sadx2_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eyebrows angry:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
            pause 3.0
            xpos 0.0 ypos 0.0 rotate -18
        
        show aftermorning04_fittingrass_dbody naked_wet01:
            zoom 0.5 
            
        show aftermorning04_fittingrass_dbody_cum empty:
            zoom 0.5
        
        show aftermorning04_fittingrass_dlegr_naked:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0
        
        show aftermorning04_fittingrass_dlegr loss:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down
            
        show aftermorning04_fittingrass_mcbody_dick 03_dry:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.1 ypos 0.0 rotate -90#inicial and 2nd pose
            pause 1.0
            ease_quad 1.0 xpos 0.2 ypos 0.0 rotate -40 #3rd pose
            ease_expo 1.3 xpos 0.1 ypos 0.0 rotate -40 #4rd pose penetration
            
        show aftermorning04_fittingrass_dlegrover_naked:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 0.0
            pause 0.7 alpha 0.0
            linear 1.0 alpha 1.0
            pause 1.0
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2 alpha 1.0
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0 alpha 1.0
            
        show aftermorning04_fittingrass_mcbody_down_naked 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 # 2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.15 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mcbody_down 02:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.1 ypos 0.6 rotate 0 #pants down
            alpha 0.0
            
        show aftermorning04_fittingrass_mcbody_top 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 #2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.15 ypos 0.0 rotate 0 #4rd pose penetration

        
        show aftermorning04_fittingrass_dlegl_naked:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0
            
        show aftermorning04_fittingrass_dlegl loss:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down
            
        show aftermorning04_fittingrass_mchand empty:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with vpunch

        stop music fadeout 0.5

        play sound "audio/sfx/slap01.ogg"
        
        d "<{size=17}¡¿Qué coño ha...?!{/size}>"
        
        if config.version <= "00.02.07":
            
            jump endupdate
            
        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
             
        show aftermorning04_fittingrass_dface_blush 00:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_dface_eye 06:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2 
            
        show aftermorning04_fittingrass_dface_pupil empty:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_dface_mouth sadx4_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2

        show aftermorning04_fittingrass_dface_eyebrows angryx02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -2
            
        show aftermorning04_fittingrass_mcbody_dick 03_wet01:
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.05 ypos 0.0 rotate -36

        show aftermorning04_fittingrass_mcbody_down_naked 03:
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mcbody_top 03:
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration
            
        show aftermorning04_fittingrass_mchand:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with hpunch

        play sound "audio/characters/didac/scream05.ogg"
        
        d "{size=70}¡¡¡¡AAAAAAAH!!!!{/size}" # *Scream of pain after being penetrated*
        
label aftermorning04_FittingRoom_RapeVagina_Angry:
        
        show aftermorning04_fittingrass_dface_eye 07
        show aftermorning04_fittingrass_dface_pupil empty
        show aftermorning04_fittingrass_dface_mouth sadx3_Silent
        show aftermorning04_fittingrass_dface_eyebrows angryx03
        with dissolve
        
        de "¡¿Se puede saber qué están haciendo ahí dentro?!"
        
        show aftermorning04_fittingrass_dface_eye 02
        show aftermorning04_fittingrass_dface_pupil rightsurprise02
        show aftermorning04_fittingrass_dface_mouth sadx3_Silent
        show aftermorning04_fittingrass_dface_eyebrows angryx03
        with dissolve
        
        de "¡Salgan inmediatamente o llamo a seguridad!"
        
        show aftermorning04_fittingrass_dface_eye 04
        show aftermorning04_fittingrass_dface_pupil right04
        show aftermorning04_fittingrass_dface_mouth sadx4_Talking
        show aftermorning04_fittingrass_dface_eyebrows angryx03
        with dissolve
        
        d "¡Hijo de puta!"

        extend " ¡Estás enfermo!"

        hide aftermorning04_fittingrass_dface_lookback_drops
        hide aftermorning04_fittingrass_dface lookback
        hide aftermorning04_fittingrass_dface_blush
        hide aftermorning04_fittingrass_dface_eye
        hide aftermorning04_fittingrass_dface_pupil
        hide aftermorning04_fittingrass_dface_mouth
        hide aftermorning04_fittingrass_dface_eyebrows
        hide aftermorning04_fittingrass_dface_lookback_hairfront
        hide aftermorning04_fittingrass_dbody
        hide aftermorning04_fittingrass_dbody_cum
        hide aftermorning04_fittingrass_dlegr_naked
        hide aftermorning04_fittingrass_dlegrover_naked
        hide aftermorning04_fittingrass_dlegl_naked
        hide vaporbreathing
        
        show aftermorning04_fittingrass bg_02:
            zoom 0.5
        show aftermorning04_fittingrass_mcbody_dick 03_wet01:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.0 ypos 0.0 rotate -39#inicial and 2nd pose
            pause 0.06
            ease_quad 0.3 xpos 0.0 ypos 0.0 rotate 5 
            ease_expo 0.4 xpos 0.0 ypos 0.0 rotate -5 
            ease 0.4 xpos 0.0 ypos 0.0 rotate 0 
            
        with hpunch
        
        n "Ves cómo Dídac se viste a toda prisa y sale del vestidor."
        
        scene aftermorning04_bg lingeriestore
        with fade

        $ renpy.music.set_volume(0.8, delay=10.0, channel='sfx1')
        
        n "Al fracasar en tu intento de encontrarla en algún lugar del centro comercial,"
        
        n "decides que lo más sensato es volver a casa para ver si está ahí."
        if morning03_Meritxell_Phonenumber_Accepted == True:
            
            jump morning04_Meritxell_Calling

        else:
            
            jump afternoon04_AloneatHome
        
label aftermorning04_FittingRoom_RapeButtocks:
        
    if aftermorning04_FittingRoom_ButtocksDickOver == True:

        show aftermorning04_fittingrass bg:
            zoom 0.5
            xpos 0.0 ypos 0.0

        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_drops 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
 
        show aftermorning04_fittingrass_dface_blush 03:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eye 02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_pupil rightsurprise02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_mouth sadx2_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eyebrows surprise:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show vaporbreathing

        show aftermorning04_fittingrass_dbody naked_wet02:
            zoom 0.5 
            
        show aftermorning04_fittingrass_dbody_cum empty:
            zoom 0.5

        show aftermorning04_fittingrass_dlegr_naked wet02:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegr tightwet02:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mcbody_dick 03_dry:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.1 ypos 0.0 rotate -90 #inicial and 2nd pose
            pause 1.0
            ease_quad 1.0 xpos 0.3 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.3 xpos 0.0 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down_naked 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 # 2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down 02:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.1 ypos 0.6 rotate 0 #pants down
            alpha 0.0

        show aftermorning04_fittingrass_mcbody_top 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 #2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_dlegl_naked wet02:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegl tightwet02:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mchand empty:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with vpunch
        
    elif pl.dp >= 10: #BITCHOU

        show aftermorning04_fittingrass bg:
            zoom 0.5
            xpos 0.0 ypos 0.0

        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_drops 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
 
        show aftermorning04_fittingrass_dface_blush 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eye 02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_pupil rightsurprise02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_mouth sadx2_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eyebrows surprise:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show vaporbreathing

        show aftermorning04_fittingrass_dbody naked_wet01:
            zoom 0.5 
            
        show aftermorning04_fittingrass_dbody_cum empty:
            zoom 0.5

        show aftermorning04_fittingrass_dlegr_naked wet01:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegr tightwet01:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mcbody_dick 03_dry:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.1 ypos 0.0 rotate -90 #inicial and 2nd pose
            pause 1.0
            ease_quad 1.0 xpos 0.3 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.3 xpos 0.0 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down_naked 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 # 2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down 02:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.1 ypos 0.6 rotate 0 #pants down
            alpha 0.0

        show aftermorning04_fittingrass_mcbody_top 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 #2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_dlegl_naked wet01:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegl tightwet01:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mchand empty:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with vpunch
        
    else: #Dick ON buttons Angry

        show aftermorning04_fittingrass bg:
            zoom 0.5
            xpos 0.0 ypos 0.0

        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18
 
        show aftermorning04_fittingrass_dface_blush 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eye 02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_pupil rightsurprise02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_mouth sadx2_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_eyebrows surprise:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate -18

        #show vaporbreathing

        show aftermorning04_fittingrass_dbody naked:
            zoom 0.5
            
        show aftermorning04_fittingrass_dbody_cum empty:
            zoom 0.5

        show aftermorning04_fittingrass_dlegr_naked:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegr loss:
            subpixel True
            zoom 0.5 xanchor -0.225 yanchor 0.05 
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mcbody_dick 03_dry:
            subpixel True
            zoom 0.5 xanchor -0.386 yanchor -0.005
            xpos 0.1 ypos 0.0 rotate -90 #inicial and 2nd pose
            pause 1.0
            ease_quad 1.0 xpos 0.3 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.3 xpos 0.0 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down_naked 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 # 2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_mcbody_down 02:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.1 ypos 0.6 rotate 0 #pants down
            alpha 0.0

        show aftermorning04_fittingrass_mcbody_top 03:
            subpixel True
            zoom 0.5 xanchor -0.21 yanchor 0.24
            xpos 0.0 ypos 0.0 rotate 0 #inicial pose
            pause 0.1
            ease_quad 1.0 xpos 0.15 ypos 0.0 rotate -20 #2nd pose
            ease_quad 1.0 xpos 0.35 ypos 0.0 rotate 0 #3rd pose
            ease_expo 1.0 xpos 0.1 ypos 0.0 rotate 0 #4rd pose penetration

        show aftermorning04_fittingrass_dlegl_naked:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0
            pause 2.7
            ease_expo 0.15 xpos -0.01 ypos 0.0 rotate -2
            ease_expo 0.5 xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dlegl loss:
            subpixel True
            zoom 0.5 xanchor -0.08 yanchor 0.085
            xpos 0.0 ypos 0.0 rotate 0 alpha 1.0 #inicial pose
            ease_expo 1.0 xpos -0.2 ypos 0.6 rotate 0 alpha 0.0 #pants down

        show aftermorning04_fittingrass_mchand empty:
            zoom 0.5 xanchor -0.5 yanchor 0.555
            
        with vpunch
        
    if pl.dp >= 10:

        d "<{size=17}[protname]..."

        extend " ¿Qué...?{/size}>"
        
    else:

        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        
        d "<{size=17}[protname]..."

        extend " ¿Qué coño...?{/size}>"
        
    if config.version <= "00.02.07":
        
        jump endupdate
    
    de "En el mismo lugar donde has cogido esta,"

    de "están las demás tallas..."
    
    n "La dependienta seguía hablando sobre sujetadores mientras Dídac no podía apartar sus ojos de tu miembro."
    
    if pl.dp >= 10:
        
        show vaporbreathing:
            xpos -0.01 ypos -0.05
        
        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0
            
        show aftermorning04_fittingrass_dface_lookback_drops 01:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0
            
        show aftermorning04_fittingrass_dface_lookback_drops 01:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0
        
        show aftermorning04_fittingrass_dface_blush 02:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_eye 04:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_pupil right04:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_mouth sad_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_eyebrows angry:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0
            
        with dissolve

        d "<{size=17}[protname]...{/size}>"

        d "<{size=17}¿Qué...?"

        extend " ¿Qué estás haciendo [protname]..?{/size}>"
        
    else:
        
        show aftermorning04_fittingrass_dface lookback:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0
        
        show aftermorning04_fittingrass_dface_blush 00:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_eye 04:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_pupil right04:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_mouth sad_Talking:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_eyebrows angry:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0

        show aftermorning04_fittingrass_dface_lookback_hairfront:
            zoom 0.5 xanchor -0.001 yanchor 0.219
            xpos 0.0 ypos 0.0 rotate 0
            
        with dissolve
        
        d "<{size=17}[protname]..."

        extend " ¡¿Qué coño estás haciendo?!{/size}>"
        
    if pl.dp >= 10:

        show aftermorning04_fittingrass_dface_mouth sad_Silent
            
        with dissolve
        
    else:
        
        show aftermorning04_fittingrass_dface_mouth sad_Silent
        with dissolve
        
    if config.version <= "00.02.07":
        
        jump endupdate
    
    menu aftermorning04__OutFittingRoom_DickOnButtocks_Question:
        
        pt "Ahora me dirá que puso su culo encima de mi polla por accidente..."
        
        "<No moverte>":
            
            call p_Help
        
            $pl.ch_pts("dp",-1)
                              
            jump aftermorning04__OutFittingRoom_DickOnButtocks
            
        "<Usar sus apretadas nalgas para masturbar tu polla en erección>":
            
            call p_Help
        
            $pl.ch_pts("dp",1)
            
            $ aftermorning04_FittingRoom_ButtocksDickOverMasturbate = True
                              
            jump aftermorning04__OutFittingRoom_DickOnButtocks
                
label aftermorning04__OutFittingRoom_DickOnButtocks:
    
    #Dick on Buttocks Masturbating
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: 
    
        if pl.dp >= 17:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 17[hd]")
            
            show aftermorning04_fittingrass_dface lookback:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_lookback_drops 01:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18
     
            show aftermorning04_fittingrass_dface_blush 03:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_eye 04:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_pupil lostheart04:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_mouth bitingx1_Silent:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_eyebrows sad:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18

            show aftermorning04_fittingrass_dface_lookback_hairfront:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18
                
            show aftermorning04_fittingrass_dlegr_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_dick 03_wet01:
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                easeout_quad 2.0 xpos -0.15 ypos 0.0 rotate 25 #PoseFront
                ease 2.0 xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos 0.05 ypos 0.0 rotate 20 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_top 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos -0.05 ypos 0.0 rotate -5 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_dlegl_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat
                
            with dissolve
    
            n "Sientes el calor que desprende su entrepierna y el tacto suave de sus nalgas contra tu polla."
            
        elif pl.dp >= 10:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 10[hd], [p_but]17[hd]")
            
            show aftermorning04_fittingrass_dface lookback:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0
                
            show aftermorning04_fittingrass_dface_lookback_drops_01:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0

            show aftermorning04_fittingrass_dface_eye 02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_pupil rightsurprise02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_mouth bitingx1_Silent:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_eyebrows angryx02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_lookback_hairfront:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0
                
            show aftermorning04_fittingrass_dlegr_naked wet01:
                subpixel True
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_dick 03_wet01:
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                easeout_quad 2.0 xpos -0.15 ypos 0.0 rotate 25 #PoseFront
                ease 2.0 xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos 0.05 ypos 0.0 rotate 20 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_top 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos -0.05 ypos 0.0 rotate -5 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_dlegl_naked wet01:
                subpixel True
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat
                
            with dissolve
        
        else:
            
            if PlatinumHelp:
                $ renpy.notify("[p_neg] 10[hd]")
            
            show aftermorning04_fittingrass_dface lookback:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0

            show aftermorning04_fittingrass_dface_eye 02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_pupil rightsurprise02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_mouth sadx3_Silent:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_eyebrows angryx02:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_dface_lookback_hairfront:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -0
                
            show aftermorning04_fittingrass_dlegr_naked:
                subpixel True
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_dick 03_dry:
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                easeout_quad 2.0 xpos -0.15 ypos 0.0 rotate 25 #PoseFront
                ease 2.0 xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos 0.05 ypos 0.0 rotate 20 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_top 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos -0.05 ypos 0.0 rotate -5 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_dlegl_naked:
                subpixel True
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                pause 1.6
                easeout_expo 0.5 xpos -0.005 ypos 0.0 rotate -1 #PoseFront
                ease 1.9 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat
                
            with dissolve
    
    de "Si quieres saber qué talla usas de pecho,"
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: 
    
        if pl.dp >= 17:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 14[hd]")
            
            show aftermorning04_fittingrass_dface lookback
                
        elif pl.dp >= 10:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 10[hd], [p_but] 17[hd]")
            
            show aftermorning04_fittingrass_dface_mouth sadx3_Talking
            
            d "<{size=17}[protname]..."

            extend " la madre que te...{/size}>"
            
            show aftermorning04_fittingrass_dface_eye 07
            show aftermorning04_fittingrass_dface_pupil empty
            show aftermorning04_fittingrass_dface_mouth sadx3_Silent
            show aftermorning04_fittingrass_dface_eyebrows angry
            show aftermorning04_fittingrass_dface_lookback_hairfront
            with dissolve
            
        else:
            
            if PlatinumHelp:
                $ renpy.notify("[p_neg] 10[hd]")
            
            show aftermorning04_fittingrass_dface_eye 02
            show aftermorning04_fittingrass_dface_pupil rightsurprise02
            show aftermorning04_fittingrass_dface_mouth sadx4_Talking
            show aftermorning04_fittingrass_dface_eyebrows angryx03
            show aftermorning04_fittingrass_dface_lookback_hairfront
            with dissolve
            
            d "<{size=17}¡¿Es que se te ha ido la puta pinza?!{/size}>"
            
            show aftermorning04_fittingrass_dface_mouth sadx3_Talking
            show aftermorning04_fittingrass_dface_eyebrows angryx02
            show aftermorning04_fittingrass_dface_lookback_hairfront
            with dissolve
               
            d "<{size=17}¡Quítame esa mierda de encima!{/size}>"
            
            show aftermorning04_fittingrass_dface_pupil leftsurprise02
            show aftermorning04_fittingrass_dface_mouth sadx3_Silent
            show aftermorning04_fittingrass_dface_eyebrows angryx02
            show aftermorning04_fittingrass_dface_lookback_hairfront
            with dissolve
            
            
    
        pt "Dios..."

        extend " no puedo más..."

        pt "Me va a estallar..."
    
        n "Sigues frotando tu miembro contra su {b}sonrisa vertical{/b}."
        
    if pl.dp >= 10:
    
        n "Sientes cómo su humedad es cada vez más abundante y cómo empiezan a temblarle las piernas."
        
    else:
        
        n "Tienes la sensación, de que si terminas corriéndote, Dídac te va a matar."
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: #Face Didac after moving your dick on her buttocks.
    
        if pl.dp >= 17:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 17[hd]")
    
            show aftermorning04_fittingrass_dlegr_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                easeout_expo 2.0 xpos 0.02 ypos 0.0 rotate 2 #PoseFront
                ease 2.0 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_dick 03_wet02:
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                easeout_quad 2.0 xpos -0.15 ypos 0.0 rotate 25 #PoseFront
                ease 2.0 xpos 0.1 ypos 0.0 rotate -15 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos 0.05 ypos 0.0 rotate 20 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_top 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                easeout_quad 2.0 xpos -0.05 ypos 0.0 rotate -5 #PoseFront
                ease 2.0 xpos 0.2 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_dlegl_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                easeout_expo 2.0 xpos 0.02 ypos 0.0 rotate 3 #PoseFront
                ease 2.0 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat
        
    de "Puedes pedirnos una métrica y te ayudaremos encan..."
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: 
    
        n "Un extraño silencio te deja dubitativo, pero en ese instante, sin poder evitarlo."
        
        n "sientes el flujo que hay en ti surgir con la fuerza de un volcán,"
        
    else:
        
        d "..."
    
    de "¿Ocurre algo, señorita?"
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: #Face Didac after moving your dick on her buttocks.
    
        if pl.dp >= 17:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 17[hd]")
            
            show aftermorning04_fittingrass_dbody_cum 02:
                pause 0.5
    
            show aftermorning04_fittingrass_dlegr_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                easeout_expo 2.0 xpos 0.02 ypos 0.0 rotate 2 #PoseFront
                ease 2.0 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat

            show aftermorning04_fittingrass_mcbody_dick 03_wet02:#Cumming
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.2 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.3 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.5 xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.2 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.3 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.5 xpos 0.1 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_top 03:
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0 

            show aftermorning04_fittingrass_dlegl_naked wet02:
                subpixel True
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                easeout_expo 2.0 xpos 0.02 ypos 0.0 rotate 3 #PoseFront
                ease 2.0 xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                repeat
                
        elif pl.dp >= 10:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 10[hd], [p_but] 17[hd]")
            
            show aftermorning04_fittingrass_dface_eye 06
            with dissolve
            
            pause 0.5
            
            hide aftermorning04_fittingrass_dface_lookback_drops
            hide aftermorning04_fittingrass_dface_eye
            hide aftermorning04_fittingrass_dface_pupil
            hide aftermorning04_fittingrass_dface_mouth
            hide aftermorning04_fittingrass_dface_eyebrows
            hide aftermorning04_fittingrass_dface_blush
            hide aftermorning04_fittingrass_dface_lookback_hairfront
            
            show vaporbreathing:
                xpos 0.0 ypos 0.0
            show aftermorning04_fittingrass_dface lookfront:
                zoom 0.5 xanchor -0.001 yanchor 0.219
                xpos 0.0 ypos 0.0 rotate -18
            
            show aftermorning04_fittingrass_dbody_cum 02:
                pause 0.5
    
            show aftermorning04_fittingrass_dlegr_naked wet01:
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back

            show aftermorning04_fittingrass_mcbody_dick 03_wet02:#Cumming
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.2 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.3 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.5 xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.2 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.3 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.5 xpos 0.1 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_top 03:
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0 

            show aftermorning04_fittingrass_dlegl_naked wet01:
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 #Pose Back
                
            with dissolve
            
            d "..." #Not Finished
            
        else:
            
            if PlatinumHelp:
                $ renpy.notify("[p_neg] 10[hd]")
                    
            show aftermorning04_fittingrass_dface_eye 02
            show aftermorning04_fittingrass_dface_pupil rightsurprise02
            show aftermorning04_fittingrass_dface_mouth sadx3_Talking
            show aftermorning04_fittingrass_dface_eyebrows surprise

            show aftermorning04_fittingrass_dbody_cum 02:
                pause 0.5
            
            show aftermorning04_fittingrass_dlegr_naked:
                zoom 0.5 xanchor -0.225 yanchor 0.05 
                xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_dick 03_dry:#Cumming
                subpixel True
                zoom 0.5 xanchor -0.386 yanchor -0.005
                xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.1 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.2 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.2 xpos -0.01 ypos 0.0 rotate 2 
                ease 0.3 xpos 0.0 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos -0.01 ypos 0.0 rotate 1 
                ease 0.5 xpos 0.0 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_down_naked 03:
                subpixel True
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.1 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.2 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.102 ypos 0.0 rotate 0 
                ease 0.3 xpos 0.1 ypos 0.0 rotate 0
                easeout_quad 0.1 xpos 0.103 ypos 0.0 rotate 0 
                ease 0.5 xpos 0.1 ypos 0.0 rotate 0

            show aftermorning04_fittingrass_mcbody_top 03:
                zoom 0.5 xanchor -0.21 yanchor 0.24
                xpos 0.1 ypos 0.0 rotate 0 

            show aftermorning04_fittingrass_dlegl_naked:
                zoom 0.5 xanchor -0.08 yanchor 0.085
                xpos 0.0 ypos 0.0 rotate 0 
            
            
    
        n "Bañas en semen la espalda y nalgas de Dídac."
        
    else:
        
        hide aftermorning04_fittingrass_dface_lookback_drops
        hide aftermorning04_fittingrass_dface_eye
        hide aftermorning04_fittingrass_dface_pupil
        hide aftermorning04_fittingrass_dface_mouth
        hide aftermorning04_fittingrass_dface_eyebrows
        hide aftermorning04_fittingrass_dface_blush
        hide aftermorning04_fittingrass_dface_lookback_hairfront
        show aftermorning04_fittingrass_dface lookfront
        with dissolve
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: #Face Didac after moving your dick on her buttocks.
            
        if pl.dp >= 10:
            
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 10[hd]")
            
            de "No tiene buena cara."
            
            pt "Mierda..."

            pt "Dídac,"

            extend " ¡reacciona!"
            
        else:
            
            if PlatinumHelp:
                $ renpy.notify("[p_neg] 10[hd]")
            
            show aftermorning04_fittingrass_dface_eye 07
            show aftermorning04_fittingrass_dface_pupil empty
            show aftermorning04_fittingrass_dface_mouth sadx3_Silent
            show aftermorning04_fittingrass_dface_eyebrows angryx03
            with dissolve
            
            de "Señorita..."

            extend " ¿Le ocurre algo?"
            
            hide aftermorning04_fittingrass_dface_lookback_drops
            hide aftermorning04_fittingrass_dface_eye
            hide aftermorning04_fittingrass_dface_pupil
            hide aftermorning04_fittingrass_dface_mouth
            hide aftermorning04_fittingrass_dface_eyebrows
            hide aftermorning04_fittingrass_dface_blush
            hide aftermorning04_fittingrass_dface_lookback_hairfront
            show aftermorning04_fittingrass_dface lookfront
            with dissolve
    
    d "No,"

    extend " no..."

    d "Estoy bien,"

    extend " estoy bien."
    
    if pl.dp >= 10:
        
        n "Su voz es entrecortada y entre suspiros."
        
    else:
        
        n "Su voz es seca y cortante."
    
    d "Me has sido de mucha ayuda, gracias."
    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True:
        
        if pl.dp >= 17:
            
            n "Tu polla está completamente empapada con su flujo vaginal."
        
        elif pl.dp >= 10:
            
            n "Tu polla está parcialmente cubierta por su flujo vaginal."
            
        else:
            
            n "Le habías dejado empapada la espalda con tu corrida."
            
            n "Pero su entrepierna no muestra el más mínimo indicio de humedad."
    
    
    de "Tranquila,"

    extend " para eso estamos, señorita."
    
    if pl.dp >= 17:
        
        n "Apenas es capaz de mantener el equilibrio debido al tembleque que sufren sus piernas."
    
    elif pl.dp >= 10:
        
        p "..."

        pt "Quizás no debería haberme masturbado con sus nalgas..."
        
    else:
        
        n "No solo su voz resulta completamente fría."
    
    de "Pero,"

    extend " solo a modo de recordatorio..."

    de "los probadores de este centro comercial,"
    
    if pl.dp >= 17:
        
        n "En el suelo observas una charca oscura de tamaño considerable entre las piernas de Dídac."
    
    elif pl.dp >= 10:
        
        n "En el suelo observas ciertas manchas oscuras entre las piernas de Dídac."
        
    else:
        
        n "El ambiente resulta bastante tenso."
    
    de "son de uso {b}\"individual\"{/b}."

    de "Espero que usted lo entienda..."
    
    d "Euh..."
    
    pt "Mierda..."

    pt "está claro que nos ha pillado."
    
    d "Sí..."

    d "claro,"

    extend " claro..."
    
    de "Bien,"

    extend " me alegro."
    
    de "Si me necesita, ya sabe dónde estoy."
    
    if pl.dp >= 17:
        
        n "Dídac cierra la cortina y se reincorpora con un rostro algo difícil de definir."
    
    elif pl.dp >= 10:
        
        n "Dídac cierra la cortina y se reincorpora con cara de pocos amigos."
        
    else:
        
        n "Dídac cierra la cortina y se reincorpora mostrando un rostro que destila odio por todos sus poros."
    
    if pl.dp >= 17:

        scene aftermorning04_bg fittingroomin

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 02:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 03:
            dfexpressions_atright_closex2
        show didacf_eyes 04:
            dfexpressions_atright_closex2
        show didacf_pupils front04:
            dfexpressions_atright_closex2
        show didacf_eyebrows angryx03:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Talkingx07:
            dfexpressions_atright_closex2
        with fade
        
    elif pl.dp >= 10:
        
        scene aftermorning04_bg fittingroomin

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 02:
            dfexpressions_atright_closex2
        show didacf_eyes 04:
            dfexpressions_atright_closex2
        show didacf_pupils front04:
            dfexpressions_atright_closex2
        show didacf_eyebrows angryx03:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Talkingx08:
            dfexpressions_atright_closex2
        with fade
        
    else:

        play music "audio/music/alcaknight/bury_it.ogg" fadein 3.0 fadeout 3.0

        scene aftermorning04_bg fittingroomin

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 00:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 00:
            dfexpressions_atright_closex2
        show didacf_eyes 05:
            dfexpressions_atright_closex2
        show didacf_pupils front05:
            dfexpressions_atright_closex2
        show didacf_eyebrows angryx03:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Talkingx09:
            dfexpressions_atright_closex2
        with fade

    d "<{size=17}¡¿Se puede saber en qué estabas pensando?!{/size}>"
            
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: 
        
        if pl.dp >= 17:

            show didacf_eyes 03
            show didacf_pupils downLeft03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx06
            with dissolve
            
            d "<{size=17}¡Me has dejado la espalda empapada!{/size}>"
            
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx08
            with dissolve
            
            d "<{size=17}¡Como mínimo podrías haberlo tirado al suelo o haberte puesto un condón!{/size}>"
            
        elif pl.dp >= 10:

            show didacf_eyes 04
            show didacf_pupils downLeft04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx07
            with dissolve
            
            d "<{size=17}¡Me has dejado la puñetera espalda empapada!{/size}>"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx09
            with dissolve
            
            d "<{size=17}¿¡Por qué coño no lo has tirado al suelo por lo menos!?{/size}>"
            
        else:

            show didacf_eyes 00
            show didacf_pupils downLeft00
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Talkingx06
            with dissolve
            
            d "¡¿Te me has corrido en la espalda?!"

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx08
            with dissolve
            
            p "Euh..."

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx09
            with dissolve
            
            d "¿¡PERO DE QUÉ COÑO VAS!?"
            
    else:
        
        if pl.dp >= 17:

            show didacf_blush 03
            show didacf_eyes 04
            show didacf_pupils left04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx06
            with dissolve
            
            d "..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx04
            with dissolve
            
            d "<{size=17}¡¿Por qué coño me bajas los pantalones y me pones la polla encima?!{/size}>"

            show didacf_eyes 05
            show didacf_pupils left05
            show didacf_eyebrows angryx02
            show didacf_mouth sadbiting_Silentx04
            with dissolve
        
            n "Te grita con una voz afónica y baja en decibelios."
            
        elif pl.dp >= 10:

            show didacf_blush 02
            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx08
            with dissolve
            
            d "<{size=17}¡¿Puedo saber por qué diablos me has bajado los bóxeres y luego me has puesto tu jodida polla encima?!{/size}>"

            show didacf_blush 01
            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx07
            with dissolve
            
            d "<{size=17}¡¿Es que se te ha ido completamente la puta pinza?!{/size}>"
            
        else:

            show didacf_blush 00
            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx08
            with dissolve
            
            d "<{size=17}¡¿Qué coño haces bajándome los pantalones y poniéndome tu puta polla sobre mi?! ¡imbécil!{/size}>"
               
    
    if pl.dp >= 17:    

        show didacf_blush 02
        show didacf_eyes 02
        show didacf_pupils left02
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx05
        with dissolve
        
    elif pl.dp >= 10:

        show didacf_blush 01
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx06
        with dissolve
        
    else:

        show didacf_blush 00
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx07
        with dissolve

    p "<{size=17}¡Pero si has sido tú quien me has puesto como una moto!{/size}>"

    
    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: 
        
        if pl.dp >= 10:

            show didacf_eyes 04
            show didacf_pupils left04
            show didacf_eyebrows angryx03
            with dissolve
    
            pt "Un segundo..."

            pt "¿Como mínimo podría haberlo tirado al suelo o con un condón...?"

            pt "¿Entonces sí me hubiera dejado?"
        
        else:

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx09
            with dissolve
            
            d "¡¡¡¿QUÉ?!!!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx08
            with dissolve
            
            pt "Quizás no ha sido buena idea masturbarme con sus nalgas..."

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx08
            with dissolve
            
            d "¡ESTÁS ENFERMO JODIDO IMBÉCIL!"
            
            scene aftermorning04_bg fittingroomin
            with hpunch
            
            n "Sin darte tiempo a reaccionar, ves cómo sale del probador de malas maneras y desaparece de tu vista."
            
            p "Hummm..."

            pt "parece que no está muy contento, precisamente..."
            
            if morning03_Meritxell_Phonenumber_Accepted == True:
            
                jump morning04_Meritxell_Calling
            
            else:
            
                jump afternoon04_AloneatHome

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "<{size=17}[protname],"

    extend " lo mejor será que te vayas a casa...{/size}>"

    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "<{size=17}¡¿Qué?!"

    extend  " ¡¿Por qué?!{/size}>"
    
    if pl.dp >= 17:

        show didacf_blush 03
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx01
        with dissolve
    
    elif pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx002
        with dissolve
        
    else:

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx06
        with dissolve
    
    d "<{size=17}Porque...{/size}>"

    d "<{size=17}porque la dependienta nos ha pillado...{/size}>"


    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "<{size=17}Podemos ir a otra planta,"

    extend " o a otra tienda...{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve
       
    d "<{size=17}¡Maldito seas [protname]!{/size}>"

    d "<{size=17}¡No te quiero a mi lado!{/size}>"

    d "<{size=17}¡¿Es que no lo entiendes?!{/size}>"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
       
    p "<{size=17}Dídac..."

    extend " yo...{/size}>"
    
    if pl.dp >= 17:

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx00
        with dissolve
    
    elif pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows serious
        show didacf_mouth sad_Talkingx03
        with dissolve
        
    else:  

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx07
        with dissolve

    
    d "<{size=17}Adiós, [protname].{/size}>"

    stop music fadeout 3.0
    
    scene aftermorning04_bg fittingroomin
    with dissolve
    
    p "..."

    p "Supongo que yo también debería irme a casa..."
    
    window hide dissolve
    pause
    
    scene  aftermorning04_bg cataloniapark
    with fade

    $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')

    n "Al salir del centro comercial, sigue habiendo un sol radiante que ilumina el corazón de Barcelona."
    
    pt "Está claro que en el fondo sigue siendo Dídac, mi viejo amigo."
    
    pt "Pero, entonces..."
    
    pt "¿Por qué intenta ponerme tan caliente?"
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome

label aftermorning04_FittingRoom_Endure:
    
    if config.version <= "00.02.08":
        
        jump endupdate

    de "En el mismo lugar donde has cogido esta,"

    extend " están las demás tallas."

    de "Si quieres saber qué talla usas de pecho,"

    extend " puedes pedirnos una métrica y te ayudaremos encantadas."

    d "Gracias,"

    extend " me has sido de mucha ayuda."

    de "Un placer,"

    extend " para lo que quieras estoy al final del pasillo."
    
    if pl.dp >= 17:
        
        n "Dídac cierra la cortina y gira sutilmente la cabeza para mirarte de reojo sin saber dónde mirar."
        
    elif pl.dp >= 10:
        
        n "Dídac cierra la cortina y gira sutilmente la cabeza para mirarte de reojo con una sonrisa pícara y burlona."
        
    else:
        
        n "Dídac cierra la cortina y gira sutilmente la cabeza para mirarte de reojo."
    
    scene aftermorning04_bg fittingroomin

    play music "audio/music/kevinmacleod/march_of_the_spoons.ogg" fadein 3.0 fadeout 3.0
    
    if pl.dp >= 17:

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 02:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 02:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 03:
            dfexpressions_atright_closex2
        show didacf_eyes 02:
            dfexpressions_atright_closex2
        show didacf_pupils left02:
            dfexpressions_atright_closex2
        show didacf_eyebrows sadx01:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Silentx03:
            dfexpressions_atright_closex2
        
    elif pl.dp >= 10:

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 01:
            dfexpressions_atright_closex2
        show didacf_eyes 04:
            dfexpressions_atright_closex2
        show didacf_pupils left04:
            dfexpressions_atright_closex2
        show didacf_eyebrows serious:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Silentx03:
            dfexpressions_atright_closex2
            
    else:

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 00:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandr leg_naked:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2
        show didacf_blush 00:
            dfexpressions_atright_closex2
        show didacf_eyes 05:
            dfexpressions_atright_closex2
        show didacf_pupils left05:
            dfexpressions_atright_closex2
        show didacf_eyebrows angryx01:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Silentx04:
            dfexpressions_atright_closex2
    
    with fade

    p "<{size=17}¡¿Es que te has bebido el entendimiento?!{/size}>"
    
    if pl.dp >= 17:

        show didacf_blush 04
        show didacf_eyes 06
        show didacf_pupils front06
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx03
        with dissolve
        
    elif pl.dp >= 10: 

        show didacf_blush 02
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows suspiciousx01
        show didacf_mouth sad_Silentx04
        with dissolve
    
    else:
        
        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx07
        with dissolve

    n "Le gritas con una voz afónica y baja en decibelios."
    
    if pl.dp >= 17:

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx01
        show didacf_mouth happy_Talkingx03
        with dissolve
        
    elif pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows normal
        show didacf_mouth happy_Talkingx02
        with dissolve
    
    else:

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex02
        show didacf_mouth sad_Talkingx002
        with dissolve
        

    d "<{size=17}Oh...{/size}"

    extend "{size=17} vamos,{/size}>"

    d "<{size=17}no te pongas así,{/size}"

    d "<{size=17}ha sido divertido,{/size}"

    extend "{size=17} ¿no crees?{/size}>"
    
    if pl.dp >= 17:

        show didacf_blush 04
        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows surprisex02
        show didacf_mouth happy_Silentx01
        with dissolve
        
    elif pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx01
        with dissolve
        
    else:

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx03
        with dissolve

    p "<{size=17}¿Eres consciente de que he estado a punto de violarte aquí mismo?!{/size}>"
    
    if pl.dp >= 17:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx002
        with dissolve
                                  
        jump aftermorning04_FittingRoom_Whynot
        
    else:
        
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 17[hd]")
        
        jump aftermorning04_FittingRoom_NotHotEnough
        
label aftermorning04_FittingRoom_NotHotEnough:
    
    if pl.dp >= 10:

        show didacf_blush 03
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows sadx01
        show didacf_mouth happybiting_Silentx03
        with dissolve
        
    else:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows surprisex01
        show didacf_mouth sadbiting_Silentx02
        with dissolve
    
    d "..."
   
    if pl.dp >= 10:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx000
        with dissolve
    
        d "<{size=17}Sí...{/size}>"
        
    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx01
        show didacf_mouth happy_Talkingx01
        with dissolve
        
        d "<{size=17}Seh,{/size}>"

        d "<{size=17}he notado cómo se izaba la bandera...{/size}>"
    
    if pl.dp >= 10:
        
        show didacf_mouth sad_Talkingx01
        with dissolve

        d "<{size=17}Lo sé...{/size}>"
    
    else:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows sadx03
        show didacf_mouth happy_Talkingx02
        with dissolve
        
        d "<{size=17}Puto depravado mental...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows sadx03
        show didacf_mouth sad_Silentx01
        with dissolve
    
        d "..."
        
    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx02
        with dissolve
        
        p "..."
    
    if pl.dp >= 10:

        show didacf_blush 01
        show didacf_eyes 05
        show didacf_pupils downLeft05
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx03
        with dissolve
    
        d "<{size=17}Lo siento, [protname],{/size}>"

        extend "<{size=17} de verdad que lo lamento.{/size}>"
    
    else:

        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows serious
        show didacf_mouth happy_Talkingx02
        with dissolve
        
        p "<{size=17}Vale,"

        extend " reconozco que posar mi culo en tu entrepierna ha sido una mala jugada...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 01
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx02
        with dissolve
        
    else:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx01
        with dissolve
    
    d "<{size=17}No sé qué me pasa...{/size}>"
        

    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows serious
        show didacf_mouth sad_Talkingx002
        with dissolve
        
    else:

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx05
        with dissolve
    
    d "<{size=17}Es estar cerca de ti y me pongo como estúpida...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 01
        show didacf_eyes 05
        show didacf_pupils down05
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx02
        with dissolve
        
    else:

        show didacf_eyes 05
        show didacf_pupils down05
        show didacf_eyebrows angryx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve
    
    p "<{size=17}¿Pero por qué?{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 04
        show didacf_pupils downLeft04
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve
        
    else:

        show didacf_eyes 04
        show didacf_pupils downLeft04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx05
        with dissolve
    
    p "<{size=17}Esta mañana has hecho lo mismo...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 03
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx002
        with dissolve
        
    else:

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx04
        with dissolve
    
    d "<{size=17}Sí,"

    extend " ya lo sé...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 03
        show didacf_eyes 04
        show didacf_pupils downLeft04
        show didacf_eyebrows sadx03
        show didacf_mouth sad_Silentx01
        with dissolve
        
    else:

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils downLeft03
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Silentx04
        with dissolve
    
    p "<{size=17}Tío,"

    extend " que me has estado restregando el culo por...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx08
        with vpunch
        
    else:

        show didacf_blush 00
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx09
        with vpunch
    
    d "<{size=40}¡He dicho que ya lo sé!{/size}>" 
    
    if pl.dp >= 10:

        show didacf_blush 00
        show didacf_eyes 00
        show didacf_pupils right00
        show didacf_eyebrows surprisex02
        show didacf_mouth sad_Silentx04
        with dissolve
        
    else:
    
        show didacf_blush 00
        show didacf_eyes 00
        show didacf_pupils right00
        show didacf_eyebrows surprisex02
        show didacf_mouth sad_Silentx04
        with dissolve
    
    de "¡Ejem!"
    
    p "<{size=17}Mierda...{/size}>"

    p "<{size=17}La dependienta nos ha oído...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils downLeft03
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx002
        with dissolve
        
        d "<{size=17}Lo siento, [protname],"

        extend " creo que lo más sensato es que te vayas...{/size}>"
        
    else:

        show didacf_blush 00
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx003
        with dissolve
        
        d "<{size=17}Mira [protname],"

        extend " lo más sensato sería que te largaras de aquí...{/size}>"
    
    
    if pl.dp >= 10:

        show didacf_blush 01
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows serious
        show didacf_mouth sad_Talkingx01
        with dissolve
    
        d "<{size=17}No sé si ha sido buena idea que vinieras aquí...{/size}>"
    
    else:

        show didacf_blush 00
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx04
        with dissolve
        
        d "<{size=17}Que vinieras aquí ha sido una terrible idea...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils down05
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx02
        with dissolve
    
        p "<{size=17}Dídac,{/size}"

        extend "{size=17} solo querías compañía,{/size}>"

        p "<{size=17}es normal...{/size}>"
        
    else:

        show didacf_blush 00
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sadbiting_Silentx04
        with dissolve
        
        p "..."
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx02
        with dissolve
    
        d "<{size=17}Sí...{/size}>"
        
    else:

        show didacf_blush 00
        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx03
        with dissolve
        
        p "<{size=17}Quizás sea mejor que me vaya entonces...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils downLeft03
        show didacf_eyebrows sadx03
        show didacf_mouth happy_Talkingx01
        with dissolve
    
        p "<{size=17}Tranquilo tío,"

        extend " nos veremos más tarde por la noche.{/size}>"
    
    else:

        show didacf_blush 00
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx003
        with dissolve
        
        d "<{size=17}Sí..."

        extend " será lo mejor...{/size}>"
    
    if pl.dp >= 10:

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve
        
    else:

        show didacf_blush 01
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx01
        show didacf_mouth sadbiting_Silentx05
        with dissolve
        
    window hide dissolve
    pause

    $ morning04_Shopping_SalesWomanTalkg_Cond = True #Hablas con la dependienta.
    
    scene aftermorning04_bg fittingroomout
    #show afternoon04_saleswoman_body crossedarms at right
    #show afternoon04_saleswoman_blush 00 at right
    #show afternoon04_saleswoman_mouth sad_Silent at right
    #show afternoon04_saleswoman_eyes front02 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #show afternoon04_saleswoman_glasses at right
    #with fade

    show afternoon04_saleswoman_body_crossedarms_b:
        afternoon04_saleswoman_body_pos

    show afternoon04_saleswoman_exp_blush 01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_mouth sad_Silentx02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyes 02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_piris front02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyebrows angryx01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_glasses:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_hairfront:
        afternoon04_saleswoman_exp_pos
    with fade
    
    n "Después de salir por la cortina y encontrarte con la dependienta con cara de pocos amigos,"

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Silentx01
    show afternoon04_saleswoman_exp_eyes 01
    show afternoon04_saleswoman_exp_piris down01
    show afternoon04_saleswoman_exp_eyebrows serious
    with dissolve
    
    n "decides salir de ahí cagando leches sin que tenga la necesidad de llamar a seguridad."
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
        
label aftermorning04_FittingRoom_Whynot:

    d "<{size=18}¿Y por qué no lo has hecho...?{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx03
    with dissolve

    p "..."

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    pt "{size=35}¡¡¿WHAT THE FUCK?!!{/size}"

    pt "¡¿Me quiere volver loco o qué está pasando aquí?!"

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "<{size=18}No te muevas de aquí,{/size}>"

    d "<{size=18}voy a buscar otro sujetador que quizás me encaje mejor y vuelvo.{/size}>"
    
    scene aftermorning04_bg fittingroomin
    with dissolve
    
    window hide dissolve
    pause

    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    n "Te pasas un buen rato ahí quieto de pie esperando como un bobalicón." with fade

    pt "¿Qué puñetas estoy haciendo aquí?"

    n "Luego es cuando te miras la entrepierna..."

    pt "¡¿Es que no piensas bajarte nunca?!"

    pt "Si por lo menos tuviera alguna prenda de ropa para disimularlo... "

    pt "Pero no voy a salir de aquí tapándome el paquetón usando un sujetador..."
    
    menu aftermorning04_FittingRoom_Whynot_WaitHere:
    
        pt "¿Qué estoy haciendo aquí? ¿Esperar a Dídac para que me vuelva a provocar?"
        
        "<Largarte>":
            
            call p_Help
            
            $pl.ch_pts("dp",-2)
                  
            jump aftermorning04_FittingRoom_Whynot_Leaving
        
        "<Quedarte>":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
            
            jump aftermorning04_FittingRoom_Whynot_Staying
            
label aftermorning04_FittingRoom_Whynot_Leaving:

    $ morning04_Shopping_SalesWomanTalkg_Cond = True #Hablas con la dependienta.
    
    n "Independientemente de que la cosa baje o no, optas por abrirte camino disimulando en la medida que te es posible"
    
    n "lo que tienes entre piernas, tan deprisa como puedes."
    
    scene aftermorning04_bg_fittingroomout
    #show afternoon04_saleswoman_body crossedarms at right
    #show afternoon04_saleswoman_blush 01 at right
    #show afternoon04_saleswoman_mouth sadx0_Talking at right
    #show afternoon04_saleswoman_eyes frontdown01 at right
    #show afternoon04_saleswoman_eyebrows surprise at right
    #show afternoon04_saleswoman_glasses at right
    #with fade

    show afternoon04_saleswoman_body_crossedarms_b:
        afternoon04_saleswoman_body_pos

    show afternoon04_saleswoman_exp_blush 02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_mouth sad_Talkingx01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyes 01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_piris down01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyebrows surprisex01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_glasses:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_hairfront:
        afternoon04_saleswoman_exp_pos
    with fade
    
    n "Tu intento de ocultarla parece haber sido un fracaso con la primera persona que encuentras..."
    
    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sadbiting_Silentx02
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris down03
    show afternoon04_saleswoman_exp_eyebrows serious
    with dissolve
    
    de "..."
    
    scene aftermorning04_bg lingeriestore
    with fade

    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_panties 01:
        dfbody_atright_little
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_below pants:
        dfbody_atright_little
    show didacfhandrb brared:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    show didacfbodytop_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_top maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_little
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_little
    show didacfhandx2 empty: #both hands
        dfbody_atright_little
    show didacf_blush 00:
        dfexpressions_atright_little
    show didacf_eyes 00:
        dfexpressions_atright_little
    show didacf_pupils front00:
        dfexpressions_atright_little
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_little
    with dissolve
    
    n "A pesar de tu celeridad para largarte de ahí, la fugaz visión de Dídac te descubre en tu intento de fuga."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    menu aftermorning04_FittingRoom_Whynot_WaitHereLeave:
    
        pt "¡Mierda! ¡Me ha pillado!"
        
        "<Largarte>":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
                  
            jump aftermorning04_FittingRoom_WaitHereLeave_Leaving
        
        "<Intentar explicarle el por qué es mejor que te vayas a casa>":
            
            call p_Help
            
            $pl.ch_pts("dp",-2)
            
            jump aftermorning04_FittingRoom_WaitHereLeave_Staying
            
label aftermorning04_FittingRoom_WaitHereLeave_Leaving:

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    n "Empiezas a acelerar el paso bajando las escaleras mecánicas dejando atrás a tu desconcertado compañero de piso."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx000
    with dissolve
    
    n "Aunque te da la sensación de que por su expresión, más que enfadado... parecía... triste."
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label aftermorning04_FittingRoom_WaitHereLeave_Staying:

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    pt "Es absurdo desmentir lo que es evidente. Te ha visto."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx02
    with dissolve
    
    pt "Si me fuera ahora, lo único que conseguiría es parecer un cobarde que no se atreve a afrontar sus problemas."

    scene aftermorning04_bg lingeriestore

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties 01:
        dfbody_atright_closex2
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_below pants:
        dfbody_atright_closex2
    show didacfbodytop naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_top maleshirt:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr_leg_maleshirt:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 02:
        dfexpressions_atright_closex2
    show didacf_eyes 04:
        dfexpressions_atright_closex2
    show didacf_pupils right04:
        dfexpressions_atright_closex2
    show didacf_eyebrows angryx02:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Silentx03:
        dfexpressions_atright_closex2
    with dissolve
    
    n "A paso lento pero seguro te acercas a Dídac."
    
    p "Dídac,"

    extend " escucha..."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "¿No te largabas?"

    extend " Capullo."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡Pues lárgate!"

    d "¿A qué esperas?"

    extend " Imbécil..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Somos compañeros de piso,"

    extend " amigos de infancia..."

    p "¿Qué se supone que estábamos haciendo ahí dentro?" 

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx004
    with dissolve 

    d "¿Has terminado?"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Dídac..."

    p "No quiero peleas contigo..."

    p "Intento ayudarte."

    p "¿Es que no lo entiendes?"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx003
    with dissolve 
    
    d "Lo único que veo,"

    extend " es que sigues sin tener ni puta idea de cómo devolverme la polla."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve 
    
    d "Y aquí estás,"

    extend " jugando al machote sentimentalista..."

    d "No tienes por qué explicarme tu puta vida."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve 
    
    d "Si realmente quieres ayudarme,"

    d "¡dime que me pasó y por qué no me llevaste al puto hospital!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx003
    with dissolve 
    
    d "Porque es evidente que prefieres estar perdiendo el puto tiempo..."  

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve 
    
    pt "¿Qué demonios le pasa ahora?"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx03
    with dissolve 
    
    p "¿Perdiendo el tiempo?"

    p "Todo esto está pasando por tu culpa... "

    show didacf_eyes 01
    show didacf_pupils right01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve 
    
    p "y si te dijera cómo se tiene que arreglar esto,"

    p "¡lo único que harías es estropearlo aún más!"

    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve 
    
    p "¡No he hecho más que ayudarte hasta ahora!"

    p "¡¿Y así me lo agradeces?!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve 
    
    d "Si tu forma de"

    extend " \"ayudar\""

    extend " es esta."

    d "Empiezo a entender cómo sacabas tan buenas notas en el colegio..." 

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve 
    
    p "..."

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx004
    with dissolve 
    
    d "¿No te ibas?"

    d "¡Pues lárgate!"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx05
    with dissolve 
    
    pt "Realmente dan ganas de darle una patada en la cara y que se vaya a la mierda..."
    
    pt "Pero está claro que algo le pasa..."

    pt "Lo mejor será dejarlo solo,"

    extend " así solo empeoraré las cosas..."

    scene aftermorning04_bg lingeriestore

    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_panties 01:
        dfbody_atright_little
    show didacfbodycloth_below pants:
        dfbody_atright_little
    show didacfbodytop naked:
        dfbody_atright_little
    show didacfbodycloth_top maleshirt:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandx2 empty: #both hands
        dfbody_atright_little
    show didacf_blush 03:
        dfexpressions_atright_little
    show didacf_eyes 04:
        dfexpressions_atright_little
    show didacf_pupils right04:
        dfexpressions_atright_little
    show didacf_eyebrows serious:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_little
    with dissolve
    
    n "Apenas unos segundos antes de perderlo de vista al bajar las escaleras mecánicas, ves en su expresión,"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx05
    with dissolve 
    
    n "no un rostro de ira, rabia o cólera..."

    n "sino más bien, de tristeza."
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
            
label aftermorning04_FittingRoom_Whynot_Staying:

    n "Aunque ahora mismo el riego sanguíneo no sea abundante en tu cerebro," 
       
    n "tu nivel de estupidez no es tan elevado como para salir con la trompa silbando;"

    extend " aún."
    
    n "A medida que va pasando el tiempo, la cosa va bajando," 
    
    n "pero en cuanto recuerdas la situación y que en cualquier momento puede volver..."

    n "La cosa se te vuelve a subir..."

    n "y así la cosa se repite como un bucle."

    window hide dissolve
    pause

    n "Cuando por fin parece que la cosa se va calmando finalmente."

    play music "audio/music/kevinmacleod/march_of_the_spoons.ogg" fadein 3.0 fadeout 3.0

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties 01:
        dfbody_atright_closex2
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_below pants:
        dfbody_atright_closex2
    show didacfhandrb brablack:
        dfbody_atright_closex2
    show didacfbodytop naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_top maleshirt:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 01:
        dfexpressions_atright_closex2
    show didacf_eyes 02:
        dfexpressions_atright_closex2
    show didacf_pupils front02:
        dfexpressions_atright_closex2
    show didacf_eyebrows normal:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happy_Talkingx03:
        dfexpressions_atright_closex2
    with dissolve

    d "<{size=18}¿Me has echado de menos, figura?{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx02
    with dissolve 

    n "Dídac entra por la cortina con una cesta grande llena de ropa íntima que deja en el suelo."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx001
    with dissolve 

    d "<{size=18}Dime,"

    extend " de lo que ves en la cesta...{/size}>"

    d "<{size=18}¿Qué te gustaría que me probara primero?{/size}>"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows surprisex01
    show didacf_mouth sadbiting_Silentx02
    with dissolve 

    p "..."

    p "<{size=18}Dídac..."

    extend " se supone que yo debo esperarte fuera,"

    extend " no dentro.{/size}>"

    show didacf_blush 01
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx01
    with dissolve 

    p "<{size=18}Además,"

    extend " esto es la sección de mujeres.{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx01
    with dissolve 

    d "<{size=18}Entonces, en teoría, ni tú ni yo deberíamos estar aquí,"

    extend " ¿verdad?{/size}>"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "<{size=18}Venga,"

    extend " no seas tiquismiquis y ayúdame a elegir.{/size}>"

    show didacfbodycloth_below empty
    show didacfhandrb empty
    show didacfbodytop bracat
    show didacfbodycloth_top empty
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx03
    with dissolve
    
    window hide dissolve
    pause

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "<{size=18}¿Qué te parece este?{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx02
    with dissolve
    
    p "<{size=18}Bueno,"

    extend " es...{/size}>"

    p "<{size=18}poco sutil.{/size}>"

    p "<{size=18}Aparte,{/size}>"

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows surprisex02
    show didacf_mouth sadbiting_Silentx02
    with dissolve
       
    p "<{size=18}no creo que esto sea precisamente \"ropa interior\"...{/size}>"

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows suspiciousx01
    with dissolve
    
    pt "Además..."

    extend " ¿A qué viene lo del cascabel?"

    pt "¿No estaba buscando ropa cómoda?"

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx03
    with dissolve

    n "En el fondo sigue siendo tu amigo de la infancia, al cual le encantan los colores chillones."

    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx05
    with dissolve
       
    n "Su gusto por la ropa es incluso peor que el tuyo... que no es decir poco."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx01
    with dissolve

    d "<{size=18}Sí,{/size}>"

    d "<{size=18}quizás es un poco demasiado exagerado,"

    extend " incluso para mí...{/size}>"

    show didacf_eyes 02
    show didacf_pupils downLeft02
    show didacf_eyebrows normal
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "<{size=18}Entonces,"

    extend " a ver qué te parece el siguiente...{/size}>"

    show didacfbodytop brared
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx03
    with dissolve

    window hide dissolve
    pause

    show didacf_blush 03
    show didacf_eyes 02
    show didacf_pupils downLeft02
    show didacf_eyebrows surprisex01
    show didacf_mouth happybiting_Silentx04
    with dissolve

    p "..."

    p "<{size=18}Bueno,{/size}"

    extend "{size=18} para ser justos,{/size}>"

    p "<{size=18}esto sí se parece más a \"ropa interior\".{/size}>"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx01
    with dissolve


    d "<{size=18}Entonces,{/size}"

    extend "{size=18} ¿te gusta?{/size}>"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows sadx01
    show didacf_mouth happybiting_Silentx05
    with dissolve
    
    p "<{size=18}Euhmmm...{/size}>"

    show didacf_eyes 03
    show didacf_pupils downLeft03
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx04
    with dissolve
    
    d "<{size=18}Espera,"

    extend " aún queda otro.{/size}>"

    show didacfbodytop brablack
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Silentx06
    with dissolve
    
    window hide dissolve
    pause
    
    if config.version <= "00.02.09":
        
        jump endupdate

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx03
    with dissolve
    
    d "<{size=18}Dime..."

    extend " ¿Qué te parece este?{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx01
    show didacf_mouth happybiting_Silentx03
    with dissolve
    
    p "..."

    pt "¡¿En qué puñetera sección ha encontrado esto aquí?!"

    pt "¡¿Esto no es de sadomasoquismo?!"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx000
    with dissolve
    
    d "<{size=18}¿No te gusta...?{/size}>"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx03
    with dissolve

    pt "¿Qué tiene en contra de la lencería femenina normal?"

    pt "Por no mencionar que los tres llevan collarín..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    pt "Mierda, [protname]..."

    pt "¡¿Qué coño estás haciendo?!..."

    pt "Es tu compañero de piso..."

    pt "este no es su comportamiento normal."
    
    pt "Como esto siga así,"

    extend " yo..."

    pt "No sé si podré controlarme..."
    
    pt "Lo mejor sería irme antes de que pueda pasar algo de lo que después podamos lamentarnos..."
    
    menu aftermorning04_FittingRoom_blackbra_Decision:
        
        pt "Creo que lo mejor es que la deje sola..."
        
        "<Hacer recapacitar a tu amigo de la infancia>":
            
            call p_Help
            
            $pl.ch_pts("dp",-3)
            
            jump aftermorning04_FittingRoom_blackbra_Stay
        
        "<Irte>":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
            
            jump aftermorning04_FittingRoom_blackbra_Leave
    
label aftermorning04_FittingRoom_blackbra_Stay:

    show didacf_blush 01
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx01
    with dissolve
    
    p "<{size=18}Dídac,"

    extend " ¿se puede saber qué estamos haciendo aquí?{/size}>"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    d "... "

    show didacf_blush 03
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "<{size=18}Estamos comprando ropa...{/size}>"

    d "<{size=18}Es obvio..."

    extend " ¿No?{/size}>"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "<{size=18}No;{/size}>"

    p "<{size=18}lo que sí es obvio,"

    extend " es que me estás provocando para que haga algo contigo...{/size}>"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."

    show didacf_blush 03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "<{size=18}¿Es eso lo que quieres?"

    extend " ¿Que te viole?{/size}>"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve
    
    d "..."

    show didacf_blush 02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "<{size=18}Dídac..."

    extend " Dime algo...{/size}>"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve

    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}Lárgate...{/size}>"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "<{size=18}¿Qué?{/size}>"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "<{size=60}¡Que te largues!{/size}>"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "<{size=40}¡¿No me has oído?!{/size}>"

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "<{size=18}Dídac,"

    extend " Yo...{/size}>"

    p "<{size=18}¿Por qué...?{/size}>"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve
    
    de "¿Va todo bien ahí dentro?"

    de "¿Llamo a seguridad?"

    show didacf_blush 00
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "No..."

    extend " No pasa nada,"

    d "mi amigo ya se iba."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "<{size=40}¡¿Verdad?!{/size}>"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    window hide dissolve
    pause
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label aftermorning04_FittingRoom_blackbra_Leave:

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    p "<{size=18}Oye Dídac,{/size}>"

    p "<{size=18}creo que yo tendría que irme..."

    extend " de verdad...{/size}>" 
    
    #$pl.ch_pts("dp",-4) # NOT FINISHED just proving alternative.

    p "<{size=18}No creo que sea buena idea que me quede aquí dentro contigo...{/size}>"
    
    #if NOT FINISHED, Didac no te detiene. 20 puntos son necesarios para que te detenga.

    scene aftermorning04_bg fittingroomin #DELETE?
    
    if pl.dp <= 17:
        
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 17[hd]")
        
        show didacfhandrb brablack:
            dfbody_atleft_closex3
        show didacfbodytop naked:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfbodycloth_top maleshirt:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3
        show didacf_blush 01:
            dfexpressions_atleft_closex3
        show didacf_eyes 01:
            dfexpressions_atleft_closex3
        show didacf_pupils front01:
            dfexpressions_atleft_closex3
        show didacf_eyebrows surprisex01:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Silentx03:
            dfexpressions_atleft_closex3
        with dissolve
        
        n "Rozas su cuerpo para poder salir."

        play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Silentx04
        with dissolve
        
        n "Aunque justo antes de que la cortina oculte su rostro, te da la sensación de que su expresión no es precisamente de alegría."
        
        scene aftermorning04_bg fittingroomout
        with fade
        
        n "Ahí fuera encuentras a la dependienta con cara de pocos amigos."
        
        n "Así que decides darte prisa para salir de ahí cagando leches..."
        
        if morning03_Meritxell_Phonenumber_Accepted == True:
        
            jump morning04_Meritxell_Calling
        
        else:
        
            jump afternoon04_AloneatHome
        
    else:
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 17[hd]")

        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3
        show didacf_blush 01:
            dfexpressions_atleft_closex3
        show didacf_eyes 01:
            dfexpressions_atleft_closex3
        show didacf_pupils front01:
            dfexpressions_atleft_closex3
        show didacf_eyebrows surprisex01:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Silentx03:
            dfexpressions_atleft_closex3
        with dissolve

        n "Intentas pasar por su lado con la intención de irte."

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx03
    with hpunch

    n "Su mano te detiene con fuerza."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx03
    with dissolve

    d "<{size=18}Has tenido mucho tiempo para irte antes de que yo llegara.{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "<{size=18}¿Por qué has esperado hasta ahora para irte?{/size}>"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth happy_Silentx01
    with dissolve

    p "..."

    p "<{size=18}¿Por qué...?{/size}>"

    p "<{size=18}Bueno, pues...{/size}>"
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast 001:
        subpixel True
        xpos -0.9 ypos -0.1 zoom 1.0
        easein_quad 30.0 xpos -0.4 ypos -1.5 zoom 0.8
    with hpunch
    
###############################################################

    if config.version <= "00.03.00": #10$ - 15 January
        
        call endupdatescript
    
###############################################################
        
    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 0.5 fadeout 0.5

    window hide dissolve
    pause
    
    n "Notas el suave tacto de la mano de tu compañero de piso encima de la tela tensa de tus pantalones a causa de tu erección."
    
    n "Sientes el calor que desprende, no solo ahí abajo, sino el de todo su cuerpo al acercarse más a ti."
    
    scene aftermorning04_bg_fittingroomin

    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils front05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows surprisex01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Talkingx05:
        dfexpressions_atleft_closex3
    with dissolve

    d "<{size=18}¿Acaso es por culpa de este que no has podido salir de aquí?{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx03
    with dissolve

    n "Su mirada no mostraba vergüenza alguna, más bien parecía lasciva, atrevida, ajena a los remordimientos."

    p "<{size=18}Dídac..."

    extend " Qué...{/size}>"
    
    window hide dissolve
    
    show aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast 001:
        xpos -0.9 ypos -0.1 zoom 1.0
    with dissolve
    
    pause 0.5
    
    hide aftermorning04_bg_fittingroom_mast 001
    show aftermorning04_bg_fittingroom_mast 002:
        subpixel True
        xpos -0.9 ypos -0.1 zoom 1.0
        easein_quad 30.0 xpos -0.4 ypos -1.5 zoom 0.8
    with dissolve
    
    pause

    n "Te percatas de que su mano se introduce en tus pantalones sin dejar de acariciarte el mástil,"
    
    n "esta vez sin que ninguna tela se interponga en medio."
    
    n "Su mano es aún más cálida y suave, al mismo tiempo que tu miembro empieza a cobrar mayor virilidad."
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 001:
        
        #zoom 0.3
        xpos -0.8 ypos -0.25 zoom 0.8 #Inicial Pose
        ease_quad 10.0 xpos -0.3 ypos -0.3 zoom 0.5
    
    window hide dissolve
    pause
    
    n "Tu muñeca es agarrada por la mano con la que te sujetaba la camiseta," 
    
    #$pl.ch_pts("dp",-3) # NOT FINISHED prove points
    
    n "siendo esta posada cerca donde termina su espalda."
    
    menu aftermorning04_FittingRoom_buttock_Decision:
        
        pt "Creo que lo mejor es que la deje sola..."
        
        "<Agarrarle la nalga con fuerza>":
            
            call p_Help
            
            $pl.ch_pts("dp",2)
            
            jump aftermorning04_FittingRoom_buttock_GrabAss
        
        "<Pararle los pies y hacerlo recapacitar>":
            
            call p_Help
            
            $pl.ch_pts("dp",-3)
            
            jump aftermorning04_FittingRoom_buttock_No
            
label aftermorning04_FittingRoom_buttock_No:

    scene aftermorning04_bg_fittingroomin

    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils down05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows serious:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Silentx04:
        dfexpressions_atleft_closex3
    with dissolve
    
    p "Dídac,"

    extend " espera..."

    extend " Dídac..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx02
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    p "{size=50}¡Dídac!{/size}>"

    stop music fadeout 0.5
    play sound "audio/sfx/fall07.ogg"

    show didacfbodytop brablack:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 02:
        dfexpressions_atright_closex2
    show didacf_eyes 00:
        dfexpressions_atright_closex2
    show didacf_pupils front00:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Silentx01:
        dfexpressions_atright_closex2
    with hpunch
    
    n "Con un ligero pero contundente empujón lo apartas ligeramente de ti."

    show didacf_blush 03
    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx000
    with dissolve
    
    p "¿Qué...?"

    extend " ¿Qué estás haciendo Dídac?"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    d "..."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Tú no eres así..."

    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Ya me gustaría a mí saber qué harías tú si estuvieras en mi lugar..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "¡¿Te crees que esto es fácil para mí?!"

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "Mira, [protname],"

    extend " será mejor que te vayas a casa,"

    d "sin duda será mucho mejor así."
    
    scene aftermorning04_bg_fittingroomin
    with hpunch
    
    n "Rápidamente ves cómo sale tras la cortina."
    
    pt "¿Se puede saber qué le pasa?"
    
    scene aftermorning04_bg_fittingroomout
    with dissolve

    $ morning04_Shopping_SalesWomanTalkg_Cond = True #Hablas con la dependienta.
    
    n "Intentas perseguirlo, pero, justo cuando pliegas la cortina para salir del probador,"
    
    #show afternoon04_saleswoman_body crossedarms at right
    #show afternoon04_saleswoman_blush 00 at right
    #show afternoon04_saleswoman_mouth sad_Silent at right
    #show afternoon04_saleswoman_eyes front02 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #show afternoon04_saleswoman_glasses at right
    #with dissolve

    show afternoon04_saleswoman_body_crossedarms_b:
        afternoon04_saleswoman_body_pos

    show afternoon04_saleswoman_exp_blush 01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_mouth sad_Silentx03:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyes 03:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_piris front03:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyebrows angryx02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_glasses:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_hairfront:
        afternoon04_saleswoman_exp_pos
    with dissolve
    
    n "te encuentras con la dependienta con cara de pocos amigos."

    show afternoon04_saleswoman_exp_blush 01
    show afternoon04_saleswoman_exp_mouth sad_Talkingx02
    show afternoon04_saleswoman_exp_eyes 02
    show afternoon04_saleswoman_exp_piris front02
    show afternoon04_saleswoman_exp_eyebrows angryx02
    with dissolve
    
    #show afternoon04_saleswoman_mouth sadx1_Talking 
    #show afternoon04_saleswoman_eyes front03
    #show afternoon04_saleswoman_eyebrows angry 
    #with dissolve
    
    de "¿Está usted al corriente de que estos probadores son de uso individual?"

    show afternoon04_saleswoman_exp_blush 02
    show afternoon04_saleswoman_exp_mouth sadbiting_Silentx01
    show afternoon04_saleswoman_exp_eyes 01
    show afternoon04_saleswoman_exp_piris down01
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    #show afternoon04_saleswoman_blush 02
    #show afternoon04_saleswoman_mouth sadx0_Talking
    #show afternoon04_saleswoman_eyes frontdown01 
    #show afternoon04_saleswoman_eyebrows surprise
    #with dissolve
    
    menu aftermorning04_FittingRoom_saleswoman_Rules_Decision:
        
        pt "Está claro que hacía rato que estaba espiando..."
        
        "Sí...":
            
            call p_Help
            
            jump aftermorning04_FittingRoom_saleswoman_Leaving
        
        "No...":
            
            call p_Help
            
            jump aftermorning04_FittingRoom_saleswoman_Leaving
            
        "No lo sabía...":
            
            call p_Help
            
            jump aftermorning04_FittingRoom_saleswoman_Leaving
            
label aftermorning04_FittingRoom_saleswoman_Leaving:

    $ morning04_Shopping_SalesWomanTalkg_Cond = True #Hablas con la dependienta.

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Talkingx02
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    #show afternoon04_saleswoman_mouth sad_Talking 
    #show afternoon04_saleswoman_eyes front01 
    #show afternoon04_saleswoman_eyebrows angry
    #with dissolve
    
    de "Me imagino que ya se va..."

    show afternoon04_saleswoman_exp_mouth sad_Talkingx01
    show afternoon04_saleswoman_exp_eyes 02
    show afternoon04_saleswoman_exp_piris front02
    show afternoon04_saleswoman_exp_eyebrows angryx02
    with dissolve

    de "¿Verdad?"
    
    show afternoon04_saleswoman_exp_mouth sad_Silentx03
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    menu aftermorning04_FittingRoom_saleswoman_Leaving_Decision:
        
        pt "Creo que es una pregunta retórica..."
        
        "Sí...":
            
            call p_Help
            
            jump aftermorning04_FittingRoom_saleswoman_LeavingTrue01
        
        "Aún no...":
            
            call p_Help
            
            jump aftermorning04_FittingRoom_saleswoman_LeavingTrue02
    
label aftermorning04_FittingRoom_saleswoman_LeavingTrue01:
    
    
    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Talkingx01
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve

    #show afternoon04_saleswoman_mouth sad_Talking at right
    #show afternoon04_saleswoman_eyes front02 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #with dissolve
    
    de "Mejor..."
            
label aftermorning04_FittingRoom_saleswoman_LeavingTrue02:

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Talkingx01
    show afternoon04_saleswoman_exp_eyes 02
    show afternoon04_saleswoman_exp_piris front02
    show afternoon04_saleswoman_exp_eyebrows serious
    with dissolve
    
    #show afternoon04_saleswoman_mouth sad_Talking at right
    #show afternoon04_saleswoman_eyes front03 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #with dissolve
    
    de "No creo que sea bueno para usted ni para mí,"

    extend " que llame a seguridad..."

    show afternoon04_saleswoman_exp_blush 02
    show afternoon04_saleswoman_exp_mouth sad_Talkingx02
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    #show afternoon04_saleswoman_mouth sad_Silent at right
    #show afternoon04_saleswoman_eyes front01 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #with dissolve

    de "¿Me equivoco?"

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sadbiting_Silentx03
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris down03
    show afternoon04_saleswoman_exp_eyebrows serious
    with dissolve

    pt "¿No se ha visto en el espejo?"

    show afternoon04_saleswoman_exp_mouth sad_Silentx02
    show afternoon04_saleswoman_exp_eyes 02
    show afternoon04_saleswoman_exp_piris front02
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve

    pt "Como si necesitara ayuda para echarme..."

    show afternoon04_saleswoman_exp_mouth sad_Silentx03
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
            
label aftermorning04_FittingRoom_buttock_GrabAss:
    
    show aftermorning04_bg_fittingroom_mast_dass 002:
        subpixel True
        xpos -0.3 ypos -0.3 zoom 0.5
        pause 0.5
        ease_quad 2.0 xpos -0.2 ypos -0.2 zoom 0.4
    with dissolve
    
    window hide dissolve
    pause

###############################################################

    if config.version <= "00.03.01": #ALL PATRONS= 30 March - Public= 30 of APRIL.
        
        call endupdatescript
    
###############################################################
        

    
    n "Sin olvidar que ha sido ella la que te ha incitado a poner tu mano sobre su nalga, aceptas su invitación con ímpetu."
    
    n "Una tela delgada no te impide agarrarle con fuerza la nalga a tu compañero de piso."
    
    n "Tersa, esponjosa, y sin duda, musculosa."
    
    if pl.dp >= 23:
        
        n "Pero sobre todo caliente, húmeda y hasta cierto punto pegajosa."
        
        n "Cuanto más te acercas a la intersección de sus piernas, mayor es esta sensación."
        
    elif pl.dp >= 20:
        
        n "Te percatas en la punta de tus dedos de que, cuanto más te acercas a la intersección de sus piernas,"
           
        n "mayor es la humedad y el calor que desprende."
        
    else:
        
        n "Además de caliente."


    n "Tienes el reflejo subconsciente de intentar quitar la mano al recordar que se trata de tu amigo de la infancia,"
    
    n "pero sientes cómo te agarra por la muñeca aún con más fuerza."

    scene aftermorning04_bg_fittingroomin

    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 04:
        dfexpressions_atleft_closex3
    show didacf_pupils down04:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Talkingx04:
        dfexpressions_atleft_closex3
    with dissolve

    d "<{size=18}Lo has notado,"

    extend " ¿verdad?{/size}>"

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx03
    show didacf_mouth happybiting_Silentx04
    with dissolve

    p "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "<{size=18}¡Está así por tu culpa imbécil!{/size}>"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows sadx02
    show didacf_mouth happybiting_Silentx05
    with dissolve
    
    pt "¡Que yo sepa solo le he agarrado el culo un segundo!"
    
    scene aftermorning04_bg_fittingroomin
    show aftermorning04_bg_fittingroom_mast 003:
        subpixel True
        xpos -0.9 ypos -0.1 zoom 1.0
        easein_quad 30.0 xpos -0.4 ypos -1.5 zoom 0.8
    with dissolve

    
    n "Regresa su mano para subirte de nuevo la camiseta, hasta que consigue quitártela del todo."
    
    p "..."

    pt "Dios..."

    extend " esto se está poniendo muy mal..."
    
    n "Sientes un fuerte agarrón en tu polla ya con una buena erección."
    
    n "Usando su pulgar para pulsar -sin ninguna delicadeza- la parte inferior del capullo."
    
    n "Casi parece que quiera ahogarte tu miembro viril con su mano."
    
    #Cambio de la cara de Dídac

    scene aftermorning04_bg_fittingroomin

    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 04:
        dfexpressions_atleft_closex3
    show didacf_pupils down04:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happybiting_Silentx03:
        dfexpressions_atleft_closex3
    with dissolve
    
    d "..."
    
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx01
    with dissolve
    
    d "Estás bien dura..."

    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows angryx01
    show didacf_mouth happybiting_Silentx05
    with dissolve

    play sound "audio/characters/didac/moanings06.ogg"
    
    d "Ahh..." # sigh watching your dick and getting excited *gemido femenino* 

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    pt "¿Está hablando conmigo o con mi polla?"

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows sadx01
    show didacf_mouth happybiting_Silentx05
    with dissolve
    
    pt "¡Coño!" #Dídac te baja los pantalones y sale tu polla en erección
    
    scene aftermorning04_bg fittingroomin
    show aftermorning04_bg_fittingroom_mast 004:
        subpixel True
        #zoom 0.3 xpos 0.3 #For Experiments.
        xpos -0.4 ypos -1.5 zoom 0.8 #Close Shot
        easein_quad 2.0 xpos -0.1 ypos -0.5 zoom 0.5 #Far Shot
    with dissolve
    
    window hide dissolve
    
    pause
    
    window hide dissolve
    
    pt "¡La madre que lo parió!"
    
    d "..."

    d "Caray..."
    
    d "Creo que es incluso más grande que la mía..."

    scene aftermorning04_bg_fittingroomin

    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 04:
        dfexpressions_atleft_closex3
    show didacf_pupils down04:
        dfexpressions_atleft_closex3
    show didacf_eyebrows serious:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Talkingx02:
        dfexpressions_atleft_closex3
    with dissolve
    
    d "Tantos años conociéndonos,"

    extend " hasta compartiendo ducha después de los partidos del sábado,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx02
    show didacf_mouth happy_Talkingx05
    with dissolve
    
    d "y creo que es la primera vez que te la veo así de dura..."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx03
    show didacf_mouth happybiting_Silentx05
    with dissolve
    
    pt "Claro,"

    extend " no te jode;"

    pt "con su cuerpo de tío no me ponía así de cachondo." 
    
    #$pl.ch_pts("dp",-3) #NOT FINISHED PROVE POINTS
        
    pt "También hay que tener en cuenta que tampoco me había estado magreando la polla durante media hora..."
    
############################################
############################################

        ##Temporal Conditionals NOT FINISHED, they will be deleted in future.
        
    $ aftermorning04_Mast001_PussyFast_insert = False
    $ aftermorning04_Mast001_AnalFast_insert = False
    
    $ aftermorning04_Mast001_AnalFast_Happy = False
    $ aftermorning04_Mast001_AnalFast_Angry = False
    
    $ aftermorning04_Mast001_PussyFast_Happy = False
    $ aftermorning04_Mast001_PussyFast_Angry = False
    
    $ aftermorning04_Mast001_PussyFastAfter_Happy = False
    $ aftermorning04_Mast001_PussyFastAfter_Angry = False
    
    $ aftermorning04_Mast001_AnalFastAfter_Happy = False
    $ aftermorning04_Mast001_AnalFastAfter_Angry = False
    
    $ aftermorning04_bg_fittingroom_mast_Fast = False
############################################
############################################
    
    menu aftermorning04_Mast01:
        
        pt "Bueno [protname], ¡¿te vas a quedar quieto mientras te está sobando la polla?!"
        
        "Bajarle los pantalones y meterle un dedo en su parte mojada.":
            
            call p_Help
            
            if pl.dp >= 24:
            
                $pl.ch_pts("dp",1)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Pussy_happy = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            elif pl.dp >= 21:
            
                $pl.ch_pts("dp",1)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Pussy_happy = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 21[hd].[p_but] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            else:
            
                $pl.ch_pts("dp",1)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Pussy_happy = False
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 21[hd]")
                
                jump aftermorning04_Mast001_nothing
            
            
        "Bajarle los pantalones y meterle el dedo en el culo.":
            
            call p_Help
        
            if pl.dp >= 24:
            
                $pl.ch_pts("dp",2)
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                $ aftermorning04_Mast001_Anal_happy = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            elif pl.dp >= 21:
            
                $pl.ch_pts("dp",-1)
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 21[hd].[p_but] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            else:
            
                $pl.ch_pts("dp",-3)
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                $ aftermorning04_Mast001_Anal_angry = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 21[hd]")
                
                jump aftermorning04_Mast001_nothing
        
        "Barjarle los pantalones y meterle un dedo en el coño y otro en el culo.":
            
            call p_Help
        
            if pl.dp >= 24:
            
                $pl.ch_pts("dp",3)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Pussy_happy = True
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                $ aftermorning04_Mast001_Anal_happy = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            elif pl.dp >= 21:
            
                $pl.ch_pts("dp",-1)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Pussy_happy = True
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                $ aftermorning04_Mast001_Anal_happy = True
        
                $ aftermorning04_Mast001_Anal_angry = False
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 21[hd].[p_but] 24[hd]")
                
                jump aftermorning04_Mast001_nothing
                
            else:
            
                $pl.ch_pts("dp",-3)
                
                $ aftermorning04_Mast001_Pussy_insert = True
                
                $ aftermorning04_Mast001_Anal_insert = True
                
                $ aftermorning04_Mast001_Anal_angry = True
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 21[hd]")
                
                jump aftermorning04_Mast001_nothing
        
        "No hacer nada.":
            
            call p_Help
        
            jump aftermorning04_Mast001_nothing


label aftermorning04_Mast001_nothing:
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 003:
        subpixel True
        ##zoom 0.3
        
        xpos -0.8 ypos -1.0 zoom 0.8 #Inicial Pose
        easeout_quad 2.0 xpos -0.7 ypos -1.3 zoom 0.7
        easein_quad 10.0 xpos -0.5 ypos -0.5 zoom 0.55
    with fade
    
    window hide dissolve
    pause
        
###################################
    
    if config.version <= "00.03.02": #10$= 30 January / ALL PATREONS= 30 March / FREE= 15 May
        
        call endupdatescript
            
###################################

    if aftermorning04_Mast001_Anal_insert == True and aftermorning04_Mast001_Pussy_insert == True:
        
        jump aftermorning04_Mast001_Pussy_Anal
        
    elif aftermorning04_Mast001_Pussy_insert == True:
        
        jump aftermorning04_Mast001_Pussy
        
    elif aftermorning04_Mast001_Anal_insert == True:
        
        jump aftermorning04_Mast001_Anal
        
    else:
        
        jump aftermorning04_Mast001_NoFingers
        

label aftermorning04_Mast001_Pussy:
    
    if aftermorning04_Mast001_Pussy_happy == False:
        
        pause 13.0
        
        d "<{size=18}¡[protname]!{/size}>"
        
        n "Su mano deja instantáneamente de hacer presión sobre tu miembro."

        scene aftermorning04_bg_fittingroomin
        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 02:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3

        show didacf_blush 02:
            dfexpressions_atleft_closex3
        show didacf_eyes 02:
            dfexpressions_atleft_closex3
        show didacf_pupils front02:
            dfexpressions_atleft_closex3
        show didacf_eyebrows angryx02:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Talkingx004:
            dfexpressions_atleft_closex3

        with vpunch

        d "<{size=18}¡¿Qué coño estamos haciendo?!{/size}>"

        show didacf_blush 03
        show didacf_eyes 03
        show didacf_pupils downLeft03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx06
        with dissolve
        
        n "Te coge la mano con la que estabas trabajando su entrepierna y te la aparta de ella {i}ipso facto{/i}."

        show didacf_blush 02
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx04
        with dissolve
        
        p "<{size=18}¿Qué...?{/size}>"

        show didacf_blush 03
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx04
        with dissolve
    
        d "<{size=18}Esto no está bien, joder..."

        extend " No deberíamos estar haciendo esta puta mierda...{/size}>"

        show didacf_blush 03
        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx003
        with dissolve

        d "<{size=18}¡¿En qué coño pensabas al meterme el dedo ahí!?{/size}>"

        show didacf_blush 03
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx05
        with dissolve
        
        d "<{size=18}¡Ese agujero no debería ni existir!{/size}>"

        show didacf_blush 02
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx02
        show didacf_mouth sadbiting_Silentx02
        with dissolve

        #pause

        #show white
           
        p "<{size=18}¡Serás cabrón!"

        extend " ¡Eres tú quien me has estado tocando la polla!{/size}>"

        show didacf_blush 04
        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx06
        with dissolve
        
        d "<{size=18}¡Y tú deberías haberlo parado!{/size}>"

        show didacf_blush 03
        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05
        with dissolve
        
        d "<{size=18}Maldito imbécil,"

        extend " ¿te crees que me gusta esta puta situación?{/size}>"

        show didacf_blush 02
        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08
        with dissolve
        
        d "<{size=18}¡¿TE CREES QUE NO QUIERO RECUPERAR MI POLLA?!{/size}>"

        show didacf_blush 03
        show didacf_eyes 00
        show didacf_pupils down00
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx04
        with dissolve
        
        p "<{size=18}¿Eres consciente de que tu mano sigue sobre mi polla?{/size}>"

        show didacf_blush 04
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx04
        with hpunch
        
        jump morning04_aftermorning04_Mast001_NotsoHappyEnding
        
    elif aftermorning04_Mast001_Pussy_happy == True:

        play sound "audio/characters/didac/moanings05.ogg"
        
        d "<{size=18}HMMmmm...>" # Muffled moan *Gemido femenino* 

        scene aftermorning04_bg_fittingroomin
        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 02:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3

        show didacf_blush 04:
            dfexpressions_atleft_closex3
        show didacf_eyes 05:
            dfexpressions_atleft_closex3
        show didacf_pupils front05:
            dfexpressions_atleft_closex3
        show didacf_eyebrows angryx01:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Talkingx003:
            dfexpressions_atleft_closex3

        with dissolve
        
        d "<{size=18}¿No se suponía que debías ayudarme a recuperar mi forma masculina?{/size}>"

        show didacf_blush 03
        show didacf_eyes 03
        show didacf_pupils down03
        show didacf_eyebrows serious
        show didacf_mouth sad_Talkingx03
        with dissolve
        
        d "<{size=18}¿Qué haces metiéndome el dedo ahí?{/size}>"

        show didacf_blush 03
        show didacf_eyes 04
        show didacf_pupils down04
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx05
        with dissolve

        p "..."
        
        p "<{size=18}Perdona,"

        extend " pero...{/size}>"

        p "<{size=18}¿Has visto dónde tienes tú la mano?{/size}>"

        show didacf_blush 04
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx02
        with dissolve
        
        d "<{size=18}Bueno,"

        extend " es posible...{/size}>"

        show didacf_blush 04
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx03
        with dissolve
        
        d "<{size=18}Pero, en teoría,"

        extend " yo soy el enfermo...{/size}>"

        d "<{size=18}Tú deberías ser el responsable y no caer en la tentación.{/size}>"

        show didacf_blush 04
        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx01
        show didacf_mouth sadbiting_Silentx05
        with dissolve
        
        pt "A veces se refiere a sí mismo de manera femenina,"

        extend " y otras de forma masculina..."

        pt "Ya no sé qué pensar..."
        
        jump aftermorning04_Mast001_GoodEnding
        
        
label aftermorning04_Mast001_Anal:
    
    if aftermorning04_Mast001_Anal_happy == False and aftermorning04_Mast001_Anal_angry == False: #If points are less than 21 with Didac, not happy, not angry.
        
        play sound "audio/characters/didac/moanings05.ogg"

        d "<{size=18}Aahh...{/size}>" # Muffled excited/angry moan for recieving a finger in her ass *Gemido femenino* 
        
        p "..."
        
        d "<{size=18}¡¿Pero qué coño haces metiéndome el dedo en el puto culo?!{/size}>"
        
        p "<{size=18}¿No te gusta?{/size}>"
        
        d "<{size=18}¡¿Quieres que te lo meta yo a ti?!{/size}>"
        
        p "<{size=18}¿Quieres que lo quite?{/size}>"
        
        d "<{size=18}Gilipollas...{/size}>"
        
        pt "Dirá lo que quiera, pero no veo que haga nada..."
        
        jump aftermorning04_Mast001_GoodEnding
    
    elif aftermorning04_Mast001_Anal_happy == False:

        play sound "audio/characters/didac/scream_au09.ogg"
        stop music fadeout 0.5
        
        d "<{size=18}¡AAAUUU!{/size}>" # *Scream of pain-pleasure after recieving a finger in his/her virgin ass*
        
        p "..."

        scene aftermorning04_bg_fittingroomin
        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 02:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3
        show didacf_blush 00:
            dfexpressions_atleft_closex3
        show didacf_eyes 01:
            dfexpressions_atleft_closex3
        show didacf_pupils front01:
            dfexpressions_atleft_closex3
        show didacf_eyebrows angryx01:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Talkingx03:
            dfexpressions_atleft_closex3

        with vpunch

        play music "audio/music/alcaknight/bury_it.ogg" fadein 0.5 fadeout 0.5
        
        d "<{size=18}¡¿Se puede saber qué coño haces metiéndome el dedo ahí?!{/size}>"

        show didacf_blush 01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx04
        with dissolve
        
        d "<{size=18}¡¿Te piensas que soy maricón o qué?!{/size}>"

        show didacf_blush 02
        show didacf_eyes 03
        show didacf_pupils down03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx04
        with dissolve
        
        p "<{size=18}Lo que estás haciendo con mi polla no es muy hetero que digamos...{/size}>"
        
        jump morning04_aftermorning04_Mast001_NotsoHappyEnding

    elif aftermorning04_Mast001_Anal_happy == True:

        play sound "audio/characters/didac/moanings05.ogg"
        
        d "<{size=18}Ahmmm...{/size}>" # Excited muffled moan *Gemido femenino* 
        
        p "..."
        
        d "<{size=18}¿Qué coño haces metiendo el dedo ahí?{/size}>"
        
        p "<{size=18}¿No te gusta?{/size}>"
        
        d "..."
        
        d "<{size=18}Yo no he dicho eso...{/size}>"
        
        jump aftermorning04_Mast001_GoodEnding
        
label aftermorning04_Mast001_Pussy_Anal:
    
    if aftermorning04_Mast001_Anal_happy == False:

        play sound "audio/characters/didac/scream_au09.ogg"
        stop music fadeout 0.5
        
        d "<{size=18}¡¡AUUU!!{/size}>"
        
        p "..."

        scene aftermorning04_bg_fittingroomin
        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 02:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3

        show didacf_blush 01:
            dfexpressions_atleft_closex3
        show didacf_eyes 01:
            dfexpressions_atleft_closex3
        show didacf_pupils front01:
            dfexpressions_atleft_closex3
        show didacf_eyebrows angryx04:
            dfexpressions_atleft_closex3
        show didacfbodytop_hair:
            dfbody_atleft_closex3
        show didacf_mouth sad_Talkingx07:
            dfexpressions_atleft_closex3

        with vpunch

        play music "audio/music/alcaknight/bury_it.ogg" fadein 0.5 fadeout 0.5
        
        d "<{size=18}¡¿Se puede saber qué coño haces metiéndome el dedo en el culo?!{/size}>"

        show didacf_blush 01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07
        with dissolve
        
        n "Con un fuerte tirón te había sacado la mano de su entrepierna."

        show didacf_blush 01
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx07
        with dissolve
        
        d "<{size=18}¡¿Es que te has vuelto loco?!{/size}>"

        show didacf_blush 01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx06
        with dissolve
        
        pt "Es curioso que solo mencione el dedo en el culo y no el que tenía en el coño..."

        show didacf_blush 01
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "<{size=18}¡¿Acaso te crees que soy marica o qué?!{/size}>"

        show didacf_blush 02
        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx05
        with dissolve
        
        p "<{size=18}Bueno,"

        extend " lo que estamos haciendo no es que sea muy hetero que digamos...{/size}>"
        
        jump morning04_aftermorning04_Mast001_NotsoHappyEnding

    elif aftermorning04_Mast001_Anal_happy == True:

        play sound "audio/characters/didac/moanings05.ogg"
        
        d "<{size=18}Ahmmm...{/size}>" # Acceptance moan after receiving finger in ass. *Gemido femenino* 
        
        p "..."
        
        d "<{size=18}¡¿Qué coño haces metiéndome los dos dedos ahí?!{/size}>"
        
        p "..."
        
        d "<{size=18}Joder..."

        extend " ¡que me has metido uno en el culo hasta el fondo!{/size}>"
        
        p "<{size=18}¿No te gusta?{/size}>"
        
        d "..."
        
        d "<{size=18}Yo no he dicho eso...{/size}>"
        
        jump aftermorning04_Mast001_GoodEnding
            
label aftermorning04_Mast001_NoFingers:
    
    pt "¿Qué se supone que tengo que hacer ahora?"
    
    pt "Esto no está bien..."
    
    pt "Él me está provocando... ¡Pero Dídac no es así!"
    
    pt "Pero joder... cómo me está poniendo..."
    
    menu aftermorning04_Mast001_NoFingers_Decision:
            
        pt "¿Qué hago?" 
            
        "<Repensártelo mejor...>":
            
            call p_Help
            
            jump aftermorning04_Mast01
            
        "<Detener esta locura>":
            
            call p_Help
            
            $pl.ch_pts("dp",-2)
            
            jump aftermorning04_Masturbation_SadEnding
                    
            
label aftermorning04_Mast001_BadEnding: #Ending con la Dependienta, que no sé si podré usar.
    
    de "¡Ejem!"
    
    d "..."
    
    de "No sé de qué \"pollas\" estáis hablando..."
    
    de "Pero será mejor que salgan de ahí antes de que llame a seguridad."
    
    de "Estos probadores son de uso individual."
    
    d "[protname],"

    extend " será mejor que te vayas."
    
    p "¿Dónde quieres que te espere?"
    
    d "No,"

    extend " no me has entendido."
    
    d "Digo,"

    extend " que quiero que te vayas a casa o donde quieras."
    
    d "Pero no te quiero cerca ahora mismo."
    
    p "Pero..."

    extend " ¿Por qué?"
    
    d "¿Es que no me has entendido?"
    
    d "{size=50}¡¡Lárgate!!{/size}"
    
    de "Señorita,"

    extend " ¿llamo a seguridad?"
    
    d "No,"

    extend " no..."

    d "mi amigo ya se iba."
    
    d "{size=50}¡¿Verdad?!{/size}"
    
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
label morning04_aftermorning04_Mast001_NotsoHappyEnding:
    
    n "De pronto sientes cómo suelta su mano de tu miembro,"

    scene aftermorning04_bg_fittingroomin

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_naked_wet 02:
        dfbody_atright_closex2
    show didacfbodytop brablack:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 04:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils left05:
        dfexpressions_atright_closex2
    show didacf_eyebrows angryx01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Silentx03:
        dfexpressions_atright_closex2
    with vpunch

    play sound "audio/sfx/fall02.ogg"
    
    n "y se aparta ligeramente."

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "<{size=18}[protname]...{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "<{size=18}¿Qué...?{/size}>"
    
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "<{size=18}No podemos seguir haciendo esto...{/size}>"
    
    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    p "<{size=18}¿Por qué?{/size}>"
    
    pt "¡Si has sido tú el que me has provocado!"

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "<{size=18}¡Porque soy tu colega...!{/size}>"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx05
    with dissolve
       
    d "<{size=18}¡joder...!{/size}>"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    n "Habla de forma entrecortada teniendo aún muy recientes los gemidos ahogados"

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "<{size=18}Ya sé que he sido yo quien te ha ido provocando...{/size}>"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "<{size=18}Lo siento,"

    extend " no sé qué me está pasando...{/size}>"

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "<{size=18}Pero, por favor;"

    extend " para.{/size}>"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx04
    with dissolve
    
    menu aftermorning04_StoporNot:
        
        pt "¿Después de lo cachondo que me has puesto?"
        
        "¡Y un cuerno voy a parar!":
            
            call p_Help
            
            $pl.ch_pts("dp",-100)
                
            $ aftermorning04_RapedYes= True
            
            jump aftermorning04_FitttingRoom_RapedYes
            
            #call endupdatebutcontinue
            
            $pl.ch_pts("dp",10)
            
            jump aftermorning04_StoporNot
            
        
        "Sí, quizás tengas razón...":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
            
            $ aftermorning04_RapedNot= True
            
            jump aftermorning04_FittingRoom_RapedNo
            
label aftermorning04_FitttingRoom_RapedYes:

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 02:
        dfexpressions_atleft_closex3
    show didacf_eyes 00:
        dfexpressions_atleft_closex3
    show didacf_pupils front00:
        dfexpressions_atleft_closex3
    show didacf_eyebrows surprisex02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx004:
        dfexpressions_atleft_closex3

    with vpunch
    
    d "<{size=18}¡¿Qué?!{/size}>"
    

    
#############################################
#############################################

        ## Rape Conditionals. Not delete them.
    
    $ aftermorning04_Mast001_PussyFast_insert = True
    $ aftermorning04_Mast001_AnalFast_insert = True
    
    $ aftermorning04_Mast001_AnalFast_Angry = True
    
    $ aftermorning04_Mast001_PussyFast_Angry = True
    
    $ aftermorning04_Mast001_PussyFastAfter_Angry = True
    
    $ aftermorning04_Mast001_AnalFastAfter_Angry = True
    
    $ aftermorning04_bg_fittingroom_mast_Fast = True
    
#############################################
#############################################

    play sound "audio/characters/didac/scream_au09.ogg"
    stop music fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    with vpunch
    
    n "Te acercas a ella, y sin vacilar, le metes un dedo en cada agujero penetrando violentamente sus adentros."

    play sound "audio/characters/didac/scream_au14.ogg"
    
    d "<{size=18}¡AAUH!{/size}>" with hpunch

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 01:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils front05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx04:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx08:
        dfexpressions_atleft_closex3

    with dissolve

    play music "audio/music/kevinmacleod/malicious.ogg" fadein 0.5 fadeout 0.5
       
    d "<{size=18}¡[protname]!"

    extend " ¡¿Qué coño...?!{/size}>"


############################################
###########################################

    transform aftermorning04_fr_rape_camera00:
        #zoom 0.15 xpos 0.2 #Vista general
        xpos -2.3 ypos -0.5  zoom 1.0
        pause 1.0
        easeout_quad 0.5 xpos -1.2 ypos -0.5 zoom 1.0
        easein_expo 5.0 xpos -1.5 ypos -0.5  zoom 1.0
        
    transform aftermorning04_fr_rape_camera01_dickteasing:
        xpos -1.5 ypos -0.5  zoom 1.0
        easein_quad 10.0 xpos -0.2 ypos -1.5 zoom 0.8
        
    transform aftermorning04_fr_rape_camera01_Didactryingtospeak:
        xpos -1.5 ypos -0.5  zoom 1.0
        
    transform aftermorning04_fr_rape_camera02_dickstartpenetrating:
        xpos -1.5 ypos -0.5  zoom 1.0
        easein_quad 10.0 xpos -0.2 ypos -1.6 zoom 0.8
        
    transform aftermorning04_fr_rape_camera03_shortpenetrationfast:
        block:
            easein_quad 1.0 xpos -0.2 ypos -1.6 zoom 0.8
            easeout_expo 0.5 xpos -0.27 ypos -1.7 zoom 0.85
            repeat
            
    transform aftermorning04_fr_rape_camera03_shortpenetface:
        block:
            easein_quad 1.0 xpos -0.8 ypos -0.4  zoom 0.8
            easeout_expo 0.5 xpos -0.9 ypos -0.45 zoom 0.85
            repeat
            
    transform aftermorning04_fr_rape_camera04_deepslowly:
        block:
            easein_quad 2.0 xpos 0.0 ypos -0.7 zoom 0.5
            easeout_expo 1.0 xpos -0.4 ypos -1.2 zoom 0.7
            repeat
            
    transform aftermorning04_fr_rape_camera04_feettoface:
        xpos 0.2 ypos -2.4 zoom 0.6
        easeout_quad 12.0 xpos -1.2 ypos -0.5 zoom 1.0
        block:
            easein_quad 2.0 xpos -0.7 ypos -0.5  zoom 0.8
            easeout_expo 1.0 xpos -1.2 ypos -0.5 zoom 1.0
            repeat
            
    transform aftermorning04_fr_rape_camera04_face:
        block:
            easein_quad 2.0 xpos -0.7 ypos -0.5  zoom 0.8
            easeout_expo 1.0 xpos -1.2 ypos -0.5 zoom 1.0
            repeat
            
    transform aftermorning04_fr_rape_camera05_deepfast:
        block:
            easein_quad 0.4 xpos 0.0 ypos -0.7 zoom 0.5
            easeout_expo 0.1 xpos -0.2 ypos -1.0 zoom 0.6
            repeat
            
    transform aftermorning04_fr_rape_camera05_face:
        block:
            easein_quad 0.4 xpos -0.7 ypos -0.3  zoom 0.8
            easeout_expo 0.1 xpos -1.0 ypos -0.5  zoom 0.9
            repeat
            
    transform aftermorning04_fr_rape_camera06_cumming:
        #zoom 0.15 ypos 0.0 xpos 0.2 #Vista general
        xpos -0.7 ypos -0.3  zoom 0.8 #face
        pause 2.0
        ease_quad 5.0 xpos 0.0 ypos -0.7 zoom 0.5 #Vista cerca
        
    transform aftermorning04_fr_rape_camera07_cummingout:
        #zoom 0.15 ypos 0.0 xpos 0.2 #Vista general
        #xpos -0.7 ypos -0.3  zoom 0.8 #face
        xpos 0.0 ypos -0.7 zoom 0.5 #Vista cerca
        #pause 2.0
        ease_quad 5.0 xpos 0.15 ypos -0.02 zoom 0.3 #Vista lejos
        
    
    $ aftermorning04_fr_rape_anim00 = True
    
    scene day04
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera00
        
    show aftermorning04_fr_rape_FACEexpression_anim 00a:
        aftermorning04_fr_rape_camera00
        
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera00
    with hpunch

    play sound "audio/sfx/hit02.ogg"
    
    window hide dissolve
    pause
    
#########################################################
    
    if config.version <= "00.03.06": #10$ PATREONS= 28 Feb /ALL PATREON = 30 May FREE= 15 Jul
        
        call endupdatescript
    
#######################################################
    
    n "Le das un empujón hasta llevar a Dídac contra la pared."
    
    show aftermorning04_fr_rape_FACEexpression_anim 00b
    with dissolve
    
    d "<{size=18}[protname],"

    extend " ¡¿qué estás haciendo?!{/size}>"

    play sound "audio/sfx/slap01.ogg"
    
    $ aftermorning04_fr_rape_anim00 = False
    $ aftermorning04_fr_rape_anim01 = True
    
    show aftermorning04_fr_rape_anim_below
    show aftermorning04_fr_rape_FACEexpression_anim 01a
    show aftermorning04_fr_rape_anim_top # Hand over mouth.
    with vpunch

    play sound "audio/characters/protagonist/shh01.ogg"
    
    p "<{size=18}Shh...{/size}>"
    
    show aftermorning04_fr_rape_FACEexpression_anim 01b
    with dissolve
    
    p "<{size=18}No hagas tanto ruido...{/size}>"
    
    show aftermorning04_fr_rape_FACEexpression_anim 01c
    with hpunch
    
    n "Acercas tu cadera a su cuerpo desnudo, posando tu miembro sobre sus nalgas."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera01_dickteasing
    show aftermorning04_fr_rape_FACEexpression_anim 01c:
        aftermorning04_fr_rape_camera01_dickteasing
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera01_dickteasing
    with dissolve
    
    n "Con un movimiento sutil, empiezas a acariciar sus labios menores con la parte más rojiza de tu erecto miembro."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera01_Didactryingtospeak
    show aftermorning04_fr_rape_FACEexpression_anim 01d:
        aftermorning04_fr_rape_camera01_Didactryingtospeak
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera01_Didactryingtospeak
    with dissolve
    
    d "<{size=18}¡Mmhimhjo def puhtaff!{/size}>" # Trying to say: Son of a bitch. with covered mouth *boca obstucalizada* 
    
    show aftermorning04_fr_rape_FACEexpression_anim 01e
    with dissolve
    
    d "<{size=18}¡¡hMmm!!{/size}>"
    
    show aftermorning04_fr_rape_FACEexpression_anim 01f
    with dissolve
    
    n "Debido al constante movimiento, consigues frotarle suavemente la parte más sensible de su entrepierna."
    
    show aftermorning04_fr_rape_FACEexpression_anim 01g
    with dissolve
    
    d "<{size=18}¡Grhummm!{/size}>" # Excited/angry grunt (mouth covered) *Gruñido femenino*
    
    show aftermorning04_fr_rape_FACEexpression_anim 01h
    with dissolve
    
    n "Dídac fracasa en su intento de gritar, ahogando su llanto a través de tu mano."
    
    $ aftermorning04_fr_rape_anim01 = False
    $ aftermorning04_fr_rape_anim02 = True
    
    show aftermorning04_fr_rape_FACEexpression_anim 01i
    with hpunch
    
    n "Con la polla bien dura, empiezas a meter la punta dentro de su cavidad totalmente lubricada."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    show aftermorning04_fr_rape_FACEexpression_anim 01d:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    with dissolve

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}¡MMmm!{/size}>" # Painful angry moan (mouth covered, starting rape) *Gemido femenino* 
    
    n "A pesar de estar ligeramente húmeda en esa tierna parte,"
    
    n "la resistencia de Dídac, obstruye la ya complicada tarea de penetrarla en contra de su voluntad."
    
    n "Pero -sin dejar de hacer presión- consigues que vaya entrando poco a poco."
    
    $ aftermorning04_fr_rape_anim02 = False
    $ aftermorning04_fr_rape_anim03 = True
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetrationfast
    show aftermorning04_fr_rape_FACEexpression_anim 01d:
        aftermorning04_fr_rape_camera03_shortpenetrationfast
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetrationfast
    with hpunch
    
    window hide dissolve
    pause
    
#########################################################
    
    if config.version <= "00.03.07": #10$ PATREONS= 15 March /ALL PATREON = ? May FREE= ?
        
        call endupdatescript
    
#######################################################
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03a:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with hpunch

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}¡MMpm!{/size}>" # Painful angry moan, losing strengh (mouth covered, starting rape) *Gemido femenino* 
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03b:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
    
    n "Percibes cómo Dídac va perdiendo poco a poco su fuerza."
    
    pt "Quizás estoy apretando muy fuerte;"

    pt "¿debería aflojar un poco para que respirara?"
    
    menu aftermorning04_fr_rape_handonmouth_decission:
        
        pt "Pero si aflojo, es posible que me muerda, como hizo Neus..."
        
        "<Aflojar tu mano para no arriesgarse a ahogar a tu amigo, que estás violando>":
            
            call p_Help
            
            $aftermorning04_fr_rape_bite_Cond = True
                  
            jump aftermorning04_fr_rape_handonmouth_bite
        
        "<Apretar más fuerte aún si cabe para que no grite ni te muerda>":
            
            call p_Help
            
            jump aftermorning04_fr_rape_handonmouth_strong
        
label aftermorning04_fr_rape_handonmouth_strong:
    
    n "Tu mano se aferra más fuerte a su mandíbula y sientes cómo sus fuerzas decaen aún más."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03c:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
    
    n "A pesar de que su espíritu de lucha sigue ahí."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03d:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
    
    pt "No creo que vaya a tomarse esto por las buenas."

    pt "Quizás haya cometido un error..."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03e:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
    
    pt "Pero desde luego, ahora no es momento de volver atrás,"

    pt "¡él se lo ha buscado!"
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03f:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
        
    pt "¿O debería decir ella...?"
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_FACEexpression_anim 03g:
        aftermorning04_fr_rape_camera03_shortpenetface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera03_shortpenetface
    with dissolve
    
    pt "Aún no he conseguido meter ni la mitad..."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    show aftermorning04_fr_rape_FACEexpression_anim 03g:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera02_dickstartpenetrating
    with dissolve
    
    pt "Quizás si aprieto un poco más..."
    
    $ aftermorning04_fr_rape_anim03 = False
    $ aftermorning04_fr_rape_anim04 = True
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera04_deepslowly
    show aftermorning04_fr_rape_FACEexpression_anim 04a:
        aftermorning04_fr_rape_camera04_deepslowly
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera04_deepslowly
    with dissolve
    
    window hide dissolve
    
    pause
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera04_feettoface
    show aftermorning04_fr_rape_FACEexpression_anim 04b:
        aftermorning04_fr_rape_camera04_feettoface
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera04_feettoface
    with dissolve

    play sound "audio/characters/didac/moanings05.ogg"
    
    d " <{size=18}¡¡HUMFFPHGG!!{/size}>" # Extremely painful groan after receiving the whole dick (being raped, mouth covered) *Gemido femenino*
    
    pt "¡Caray!"

    extend " ¡Casi entra entera!"
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera04_face
    show aftermorning04_fr_rape_FACEexpression_anim 04c:
        aftermorning04_fr_rape_camera04_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera04_face
    with dissolve
    
    n "Con una fuerza y violencia de proporciones considerables, consigues penetrar su cérvix,"
       
    n "una segunda cavidad extremadamente cerrada -en forma de dónut y carnosa-, que sientes en la punta de tu miembro."
    
    n "Con el furor del momento y tu extrema falta de interés por cómo está Dídac,"
       
    n "te abres paso por su cuello uterino."
       
    n "En comparación con su húmeda, cálida y ligeramente estrecha vagina,"
    
    n "esta segunda cavidad, mucho más profunda, ahoga aún más si cabe tu palpitante polla;"
       
    n "para, justo a escasos tres centímetros más adentro, dar paso a una sensación de vacío ardiente."
    
    n "Ahí, donde se forjan las futuras promesas del mañana, en el vientre de una madre."
    
    n "Tu polla consigue chocar al fin con lo que parece el muro de su útero, tierno pero terso."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera04_deepslowly
    show aftermorning04_fr_rape_FACEexpression_anim 04a:
        aftermorning04_fr_rape_camera04_deepslowly
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera04_deepslowly
    with dissolve

    p "..."
    
    pt "Pensé que le rompería el himen al ser virgen..."
        
    pt "Pero, desde luego, esto otro..."

    pt "no tiene nada que ver..."

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}¡¡HUMFFPHGG...!!{/size}>" # Painful groan (being raped, mouth covered) *Gemido femenino* 
    
    pt "Con lo apretada que está,"

    pt "si acelero, es posible que le haga daño..."
    
    pt "¡Al carajo!"

    pt "¡Ha sido él quien me ha provocado desde el principio!"
    
#########################################################
    
    if config.version <= "00.03.08": #10$ PATREONS= 15 March /ALL PATREON = ? May FREE= ?
        
        call endupdatescript
    
#######################################################

    play music "audio/music/kevinmacleod/killers.ogg" fadein 0.5 fadeout 0.5

    $ aftermorning04_fr_rape_anim04 = False
    $ aftermorning04_fr_rape_anim05 = True
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_deepfast
    show aftermorning04_fr_rape_FACEexpression_anim 05a:
        aftermorning04_fr_rape_camera05_deepfast
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_deepfast
    with dissolve
    
    window hide dissolve
    pause

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}¡¡HH...!!¡¡MF...!!¡¡UM...!!{/size}>" # Groaning in pain without strengh (being raped, mouth covered) *Gemido femenino*
    
    n "Debido al forcejeo, la visión de tu polla masacrando su -recién virgen- vagina es escasa,"
    
    n "pero tienes la sensación de que un color rojizo sale de su interior."
    
    n "Algo nada extraño, teniendo en cuenta tu tamaño y la delicadeza con la que la estás penetrando."
    
    pt "Ya no puedo esperar más..."

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    show closetocum_mc
    
    pt "A este ritmo no tardaré en correrme..."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_FACEexpression_anim 05a:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_face
    with vpunch

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=24}¡¡MMFF...!!¡¡HUMFGGH...!!¡¡GUHMHH...!!{/size}>" #Loud groans in pain (being raped, mouth still covered) *Gemido femenino* 
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_FACEexpression_anim 05b:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_face

    play sound "audio/characters/didac/moanings06.ogg"
    
    n "Los gemidos de Dídac traspasan cada vez más el bloqueo de tu mano."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_FACEexpression_anim 05a:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_face
    
    de "Señorita,"

    extend " oigo ruidos extraños;"

    de "¿está usted bien?"
    
    n "Agarras con más fuerza su boca para intentar acallar -sin demasiado éxito- sus ahogados llantos."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_FACEexpression_anim 05c:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_face

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}¡¡MMFFHH...!!{/size}>" # Painful Groans (raped, mouth covered) *Gemido femenino* 
    
    pt "Mierda..."

    extend " estoy a punto de correrme..."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_FACEexpression_anim 05d:
        aftermorning04_fr_rape_camera05_face
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_face
    
    pt "Debería sacar la polla,"

    pt "o le condenaré a ser una mujer por el resto de su vida..."
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera05_deepfast
    show aftermorning04_fr_rape_FACEexpression_anim 05a:
        aftermorning04_fr_rape_camera05_deepfast
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera05_deepfast
    
    menu aftermorning04_fr_rape_cum_decission:
        
        pt "Pero se siente tan a gusto aquí dentro..."
        
        "<Correrte dentro>":
            
            call p_Help
            
            $pl.ch_pts("dp",-100)
            
            $aftermorning04_fr_rape_cumed_in = True
                  
            jump aftermorning04_fr_rape_cum_inside
        
        "<Correrte fuera>":
            
            call p_Help
            
            $pl.ch_pts("dp",-10)
            
            $aftermorning04_fr_rape_cumed_out = True
                  
            jump aftermorning04_fr_rape_cum_outside
            
label aftermorning04_fr_rape_cum_inside:
    
    $ aftermorning04_fr_rape_anim05 = False
    $ aftermorning04_fr_rape_anim06 = True
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera06_cumming
    show aftermorning04_fr_rape_FACEexpression_anim 06a:
        aftermorning04_fr_rape_camera06_cumming
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera06_cumming
    
    window hide dissolve
    pause 8.0
    show cumming_mc
    pause
    
#########################################################
    
    if config.version <= "00.04.00": #10$ PATREONS= 30 April /ALL PATREON = ? May FREE= ?
        
        call endupdatescript
    
#######################################################
    
    jump aftermorning04_fr_rape_aftercum
    
label aftermorning04_fr_rape_cum_outside:
    
    $ aftermorning04_fr_rape_anim05 = False
    $ aftermorning04_fr_rape_anim07 = True
    
    show aftermorning04_fr_rape_anim_below:
        aftermorning04_fr_rape_camera07_cummingout
    show aftermorning04_fr_rape_FACEexpression_anim 07a:
        aftermorning04_fr_rape_camera07_cummingout
    show aftermorning04_fr_rape_anim_top:
        aftermorning04_fr_rape_camera07_cummingout
    
    window hide dissolve
    pause 7.0
    show cumming_mc
    pause
    
#########################################################
    
    if config.version <= "00.03.09": #10$ PATREONS= 15 March /ALL PATREON = ? May FREE= ?
        
        call endupdatescript
    
#######################################################

    jump aftermorning04_fr_rape_aftercum

label aftermorning04_fr_rape_aftercum:
    
    scene white
    
    de "{size=17}¿Señorita?{/size}>"

    stop music fadeout 3.0

    $ renpy.music.set_volume(1.0, delay=0.5, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"
    
    #scene aftermorning04_fr_rapeafter_prove #Posible to eliminate prove
    scene aftermorning04_fr_rapeafter_d_anim:
        subpixel True
        xpos -1.55 ypos 0.0 zoom 1.0 
        ease_quad 50.0 xpos 0.0 ypos 0.0 zoom 0.4 #Final
    with fade
    
    window hide dissolve
    pause
    
    n "El jadeo constante de los labios liberados de Dídac llena el vacío de la estancia."

    $ renpy.music.set_volume(0.2, delay=15.0, channel='sfx1')
    
    n "Sus manos se agarran con apenas fuerzas a la pared"
    
    n "mientras sus piernas, abiertas y rendidas en el suelo, siguen aún temblando incontroladamente."
    
    n "Su vagina había quedado totalmente abierta, casi del mismo radio que tu polla."
    
    if aftermorning04_fr_rape_cumed_in == True:
    
        n "Incluso la obertura del cuello uterino ha quedado levemente abierta, por el cual brota tu abundante semilla."
        
        n "Al correrte ahí dentro, gran parte ha quedado aún atrapada."
        
    elif aftermorning04_fr_rape_cumed_out == True:
        
        n "Incluso la obertura del cuello uterino ha quedado levemente abierta."
        
        n "Toda tu corrida sigue empapando en su espalda."

    
    de "¿Señorita?"

    de "¿Se encuentra bien?"
    
    n "Dídac sigue jadeando sin dar respuesta a la mujer encargada de la sección en la tienda."
    
    p "<{size=18}¡Dí-"

    extend "Dídac...{/size}>"

    p "<{size=18}¿Estás bien?{/size}>"

    play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}Hi-"

    extend "Hijo...{/size}>"
    
    p "<{size=18}¡¿Qué?!{/size}>"
    
    d "<{size=18}¡Hijo de puta...!{/size}>"
    
    d " <{size=18}Ahh... Ahhh... Ahhh...{/size}>" # Heavy breathing after being raped  *Suspiros*
    
    de "Señorita,"

    extend " voy a abrir la cortina para ver cómo se encuentra."

    de "¿De acuerdo?"
    
    pt "¡¿Qué?!"

    extend " ¡¡Mierda!!"
    
    d "¡No!..."

    d "Estoy bien,"

    extend " no se preocupe..."
    
    de "¿Está segura?"

    de "Hace rato que la estoy llamando y no me ha respondido hasta ahora..."
    
    de "¿Quiere que llame a urgencias?"
    
    d "¡He dicho que estoy bien!"
    
    de "..."
    
    p "..."
    
    d "Por favor,"

    d "ahora saldré,"

    extend " no se preocupe."
    
    de "Como..."

    extend " quiera..."
    
    n "Oyes los pasos inseguros de la dependienta alejándose, aunque no demasiado."

    p "..."
    
    p "<{size=18}Dídac..."

    extend " ¿Estás...?{/size}>"
    
    d "<{size=18}¡Cállate!{/size}>"
    
    p "..."
    
    d "<{size=18}Quiero dejar bien clara una cosa.{/size}>"
    
    d "<{size=18}Si le he dicho a la dependienta que estoy bien,"

    extend " no ha sido por ti.{/size}>"
    
    p "..."
    
    d "<{size=18}No tengo ganas de ir a un juicio donde me pregunten quién soy y de dónde vengo...{/size}>"
    
    d "<{size=18}Por mí te puedes pudrir en el pozo de una letrina.{/size}>"
    
    p "<{size=18}Dídac,"

    extend " Yo...{/size}>"
    
    d "¡He dicho que te calles!"
    
    scene aftermorning04_bg fittingroomin
    with fade
    
    n "Ves cómo alarga su mano, palpando el suelo, hasta que encuentra sus pantalones,"
    
    if aftermorning04_fr_rape_cumed_in == True:
    
        n "de donde saca un pañuelo, que usa para limpiar su entrepierna."
        
    elif aftermorning04_fr_rape_cumed_out == True:
        
        n "de donde saca un pañuelo, que usa para limpiar su espalda."
        
    #show aftermorning04_fr_rape_after_body_naked at Position (xpos = 0.0, xanchor=0.16, ypos =0.035, yanchor=0.0)
    show aftermorning04_fr_rape_after_body naked:
        aftermorning04_fr_rape_after_pos
    show aftermorning04_fr_rape_after_face front:
        aftermorning04_fr_rape_after_pos
    with dissolve

    $ renpy.music.stop(channel='sfx2', fadeout=15.0)
    
    n "Acto seguido, se viste con dificultades -perdiendo el equilibrio en ocasiones-,"
    
    show aftermorning04_fr_rape_after_body:
        aftermorning04_fr_rape_after_pos
    show aftermorning04_fr_rape_after_face front:
        aftermorning04_fr_rape_after_pos
    with dissolve
       
    n "sin dirigirte la más mínima palabra, gesto, ni mirada."
    
    n "Decides hacer lo mismo y vestirte rápidamente también,"
       
    n "no fuera el caso que dejara la cortina abierta al salir y te viera la dependienta en pelotas."
    
    s "¿Se puede saber qué estaban haciendo ahí dentro?"
    
    n "No te equivocabas, justo cuando Dídac hubo terminado de vestirse, abrió de golpe la cortina del probador."
    
    jump aftermorning04_fr_rape_outoffittingroom
    
label aftermorning04_fr_rape_outoffittingroom:

    stop music fadeout 3.0
    $ renpy.music.set_volume(0.1, delay=0.5, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_shop01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    $ morning04_Shopping_AgentsTalk_Cond = True #Hablas con agentes en los probadores.
    
    if aftermorning04_fr_rape_bite_Cond == True:
        
        scene aftermorning04_bg fittingroomout
        #show afternoon04_securityagent_prove
        show afternoon04_securityagent02_body:
            afternoon04_securityagent02_pos
        show afternoon04_securityagent01_body:
            afternoon04_securityagent01_pos
        show afternoon04_securityagent01_mouth Silent:
            afternoon04_securityagent01_mouth_pos
        with fade
        
        n "Una vez vestidos, abrís la cortina y veis a un par de agentes de seguridad."
    
    else:
        
        scene aftermorning04_bg fittingroomout
        show afternoon04_securityagent02_body:
            afternoon04_securityagent02_pos
        show afternoon04_securityagent01_body:
            afternoon04_securityagent01_pos
        show afternoon04_securityagent01_mouth Silent:
            afternoon04_securityagent01_mouth_pos
        show aftermorning04_fr_rape_after_body blur:
            aftermorning04_fr_rape_after_pos
        show aftermorning04_fr_rape_after_face front_blur:
            aftermorning04_fr_rape_after_pos
        with fade
        
        window hide dissolve
    
        pause
    
        n "Solo para encontraros a un par de agentes de seguridad justo enfrente,"
    
    n "Y más al fondo un grupo de curiosos que cada vez era más numeroso observando la situación."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
    show aftermorning04_fr_rape_after_body:
        aftermorning04_fr_rape_after_pos
    show aftermorning04_fr_rape_after_face front:
        aftermorning04_fr_rape_after_pos
    with dissolve
    
    d "..."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
    show aftermorning04_fr_rape_after_body blur
    show aftermorning04_fr_rape_after_face front_blur
    with dissolve
    
    p "..."
    
    n "Un silencio incómodo."
    
    pt "Quizás debería decir algo..."

    extend " no creo que Dídac esté en condiciones de..."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
    show aftermorning04_fr_rape_after_body
    show aftermorning04_fr_rape_after_face front
    with dissolve
    
    d "Lo sentimos mucho, agentes,"

    d "le pedí que entrara para que opinara sobre un sujetador..."
    
    d "Y, sin darnos cuenta, empezamos a discutir."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
        #show afternoon04_securityagent_agent1_mouth sad_Talking at Transform(zoom=0.666), Position(xpos = 0.0, xanchor=-11.9, ypos=0.0, yanchor=-3.0)
    show afternoon04_securityagent01_mouth Talking

    show aftermorning04_fr_rape_after_body blur
    show aftermorning04_fr_rape_after_face front_blur
    with dissolve
        
    # else:
        
    #     show afternoon04_securityagent01_mouth Talking
    #     with dissolve
    
    s "La dependienta dice que hace más de veinte minutos que estaban ahí dentro."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
        #show afternoon04_securityagent_agent1_mouth sad_Silent at Transform(zoom=0.666), Position(xpos = 0.0, xanchor=-11.9, ypos=0.0, yanchor=-3.0)
    show afternoon04_securityagent01_mouth Silent

    show aftermorning04_fr_rape_after_body blur
    show aftermorning04_fr_rape_after_face front_blur
    with dissolve
        
    # else:
    #     show afternoon04_securityagent01_mouth Silent
    #     with dissolve
    
    pt "Jodida dependienta..."
    
    #if aftermorning04_fr_rape_bite_Cond == False:
        #show afternoon04_securityagent_agent1_mouth sad_Talking at Transform(zoom=0.666), Position(xpos = 0.0, xanchor=-11.9, ypos=0.0, yanchor=-3.0)
    show afternoon04_securityagent01_mouth Talking

    show aftermorning04_fr_rape_after_body blur
    show aftermorning04_fr_rape_after_face front_blur
    with dissolve
        
    # else:
        
    #     show afternoon04_securityagent01_mouth Talking
    #     with dissolve
    
    s "¿Este señor le causa alguna molestia?"

    extend " Señorita."
    
    # if aftermorning04_fr_rape_bite_Cond == False:
        #show afternoon04_securityagent_agent1_mouth sad_Silent at Transform(zoom=0.666), Position(xpos = 0.0, xanchor=-11.9, ypos=0.0, yanchor=-3.0)
    show afternoon04_securityagent01_mouth Silent

    show aftermorning04_fr_rape_after_body
    show aftermorning04_fr_rape_after_face front
    with dissolve
    
    # else:
        
    #     show afternoon04_securityagent01_mouth Silent
    #     with dissolve
    
    d "..."
    
    if aftermorning04_fr_rape_bite_Cond == True:

        show aftermorning04_fr_rape_after_face back
        with dissolve
    
        n "Dídac te mira con cara de circunstancias."

        show aftermorning04_fr_rape_after_face back_blur
        show aftermorning04_fr_rape_after_body blur
        with dissolve


        
    else:
    
        pt "Ni siquiera gira el rostro para mirarme."
    
    pt "Es evidente que los agentes sospechan algo por su tono de voz y por la cara que debe de estar poniendo..."
    
    n "Un sudor frío recorre tu cuerpo."

    if aftermorning04_fr_rape_bite_Cond == True:
        show aftermorning04_fr_rape_after_face front
        show aftermorning04_fr_rape_after_body
        with dissolve
    
    d "No se preocupe, señor agente;"
    
    d "en realidad ya me había decidido por un par de piezas."
    
    d "Le pedimos perdón si les hemos causado alguna molestia..."

    show aftermorning04_fr_rape_after_face front_blur
    show aftermorning04_fr_rape_after_body blur
    with dissolve
    
    n "Dídac consiguió calmar a los agentes de seguridad del almacén."

    $ renpy.music.set_volume(0.2, delay=5.0, channel='sfx1')
    
    scene aftermorning04_bg lingeriestore
    with fade
    
    n "Compra un par de sujetadores bajo la atenta mirada de estos,"
    
    show afternoon04_securityagent02_body:
        afternoon04_securityagent02_pos
    show afternoon04_securityagent01_body:
        afternoon04_securityagent01_pos
    show afternoon04_securityagent01_mouth Silent:
        afternoon04_securityagent01_mouth_pos
    with dissolve
    
    n "que nos siguen durante el transcurso de la transacción,"
    
    n "hasta que salimos por la puerta principal a la calle."
    
    window hide dissolve
    pause

    $ renpy.music.set_volume(1.0, delay=5.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    if aftermorning04_fr_rape_bite_Cond == True:
        
        scene aftermorning04_bg cataloniapark
        with fade

        p "Dídac,"

        extend " yo..."

        $ renpy.music.set_volume(0.2, delay=10.0, channel='sfx1')
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_naked_wet 02:
            dfbody_atright_closex2
        show didacfbodytop naked:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 00:
            dfbody_atright_closex2
        show didacfbodycloth_top maleshirt:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandr empty:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright_closex2
        show didacfhandx2 empty: #both hands
            dfbody_atright_closex2

        show didacf_blush 01:
            dfexpressions_atright_closex2
        show didacf_eyes 00:
            dfexpressions_atright_closex2
        show didacf_pupils front00:
            dfexpressions_atright_closex2
        show didacf_eyebrows angryx03:
            dfexpressions_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Talkingx08:
            dfexpressions_atright_closex2

        with dissolve
        
        d "Cállate."

        show didacf_blush 00
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with dissolve
        
        d "GILIPOLLAS."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx07
        with dissolve
        
        d "Sobre las siete de la tarde iré al piso a buscar mis cosas."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx06
        with dissolve
        
        d "Espero no verte ahí al menos durante 2 horas."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx07
        with dissolve
        
        p "Dídac..."

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with vpunch
        
        d "{size=40}¡He dicho que te calles!{/size}"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08
        with dissolve
        
        d "Eres un puto imbécil,"

        extend " y no quiero verte el careto nunca más."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "Nunca me imaginé que harías algo así..." 

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx06
        with dissolve
           
        d "¡Y menos a mí!"

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx05
        with dissolve
        
        d "A saber qué habrás hecho con otras."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx03
        with dissolve
        
        d "Eres escoria."
        
        scene aftermorning04_bg cataloniapark
        with hpunch

        p "..."
        
    else:
        
        scene aftermorning04_bg cataloniapark
        with fade
    
        p "Dídac,"

        extend " yo..."

        $ renpy.music.set_volume(0.2, delay=10.0, channel='sfx1')
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        
        show aftermorning04_fr_rape_after_body:
            aftermorning04_fr_rape_after_pos
        show aftermorning04_fr_rape_after_face front:
            aftermorning04_fr_rape_after_pos
        with dissolve
        
        d "Cállate."
        
        d "Sobre las siete de la tarde iré al piso a buscar mis cosas."
        
        d "Espero no verte ahí al menos durante {size=32}DOS PUTAS{/size} horas."
        
        p "Dídac..."
        
        show aftermorning04_fr_rape_after_face back_cry01
        with vpunch
        
        d "{size=32}¡¡HE DICHO QUE TE CALLES!!{/size}"

        extend " {size=50}¡¡COÑO!!{/size}"
        
        show aftermorning04_fr_rape_after_face front
        with dissolve
        
        n "El grito es de tal magnitud, que llamáis la atención de gran parte de la gente que rodea la plaza."
        
        if aftermorning04_fr_rape_cumed_in == True:
            
            show aftermorning04_fr_rape_after_face front_cry01
            with dissolve
        
            d "Te has corrido dentro..."
            
            n "Su voz es temblorosa, y unas lágrimas empiezan a desprenderse de sus ojos con la mirada perdida."
            
            d "Sabiendo que..."

            extend " soy Dídac..."

            d "Ya..."

            extend " nunca más..."

            extend " volveré a serlo..."
            
            show aftermorning04_fr_rape_after_face front_cry02
            with dissolve
            
            n "Su respiración se descontrola por momentos, las lágrimas empiezan a brotar en cantidad por sus mejillas."
            
        elif aftermorning04_fr_rape_cumed_out == True:
            
            d "Me has violado."
            
            n "Su voz es temblorosa y una lágrima empieza a desprenderse de uno de sus ojos con la mirada perdida."

        d "Si alguien me hubiera dicho que serías capaz de hacer esto,"
           
        d "le habría dado tal paliza que no creo que hubiera llegado vivo al hospital..."
           
        d "Jamás..."

        extend " Me habría imaginado esto..."
        
        d "No eramos solo amigos,"

        extend " eramos mucho más que hermanos..."
        
        d "Te hubiera dado un riñón."

        d "Hubiera matado por ti..."

        extend " o hasta mi vida para salvar la tuya."
        
        if aftermorning04_fr_rape_cumed_in == True:
        
            p " Dídac..."
            
        elif aftermorning04_fr_rape_cumed_out == True:
            
            p "No tienes nada que reprocharme."

            p "¡Tú ibas a hacer lo mismo con Neus!"
               
            p "¡¿O es que por casualidad ahora tampoco lo recuerdas?!"
            
        show aftermorning04_fr_rape_after_face back_cry02
        with hpunch
        
        n "Te apartas instintivamente al recibir una mirada asesina tras la que parecía que iba a alzar el puño contra ti."
        
        show aftermorning04_fr_rape_after_face front_cry02
        with dissolve
        
        d "No te mereces ni que te dé una hostia..."
        
        d "Para mí ya no eres nada."
        
        d "Eres menos que la mierda que evito del suelo para no pisarla."
        
        hide aftermorning04_fr_rape_after_body
        hide aftermorning04_fr_rape_after_face
        with dissolve
        
        n "Observas con impotencia cómo se aleja de ti, desapareciendo entre la multitud de la {i}Rambla{/i}."
        
        p "..."

        extend " ¿Qué coño he hecho?"
        
        pt "Lo critiqué hace dos días por intentar violar a Neus en el cuarto de baño..."
        
        if aftermorning04_fr_rape_cumed_in == True:
        
            pt "Y, ahora..."

            pt "He condenado a mi mejor amigo desde la infancia a pasar el resto de su vida con un cuerpo que no es el suyo."
            
        elif aftermorning04_fr_rape_cumed_out == True:
            
            pt "Y ahora lo he hecho yo..."

            pt "con la diferencia de que yo he llegado hasta el final."
            
            pt "Dios..."

            pt "si le salía sangre y todo..."

            pt "Encima me he corrido en su espalda..."


    window hide dissolve
    pause 1.0

    $ renpy.music.stop(channel='sfx1', fadeout=5.0)
    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    $ renpy.music.stop(channel='sfx3', fadeout=5.0)  
    
    scene aftermorning04_bg gothicquarter_01
    with fade

    pause 1.0   

    show aftermorning04_bg gothicquarter_02
    with Dissolve (5.0)

    window hide dissolve
    pause
    
    n "Te pasas la tarde deambulando por el barrio antiguo de Barcelona sin rumbo aparente."
    
    scene aftermorning04_bg gothicquarter_03
    with Dissolve (2.0)
    
    window hide dissolve
    pause

    scene beds_night_lightOff_blindUp_DemptyMCempty
    with fade
    
    n "Cuando llegas al piso, no encuentras rastro alguno de Dídac."
    
    n "Quizás había pedido asilo en casa de algún amigo."
    
    scene morning02_bg schoolwall
    with fade
    
    n "El Lunes vuelves al {b}máster de Diseño{/b} donde tampoco encuentras a Neus por ningún sitio."
    
    n "Ni el martes, ni el miércoles, ni el jueves..."
    
    n "Había desaparecido como por arte de magia."
    
    n "Nunca volviste a verla."
    
    n "Es posible que de alguna manera se hubiera enterado de lo sucedido,"
    
    n "o que Dídac mismo se lo hubiera contado y hubiera elegido no volver a verte jamás."
    
    ##
    $ aftermorning04_fr_aftercum_park_d_eyestoscreen = False
    ##
    
    scene aftermorning04_fr_aftercum_park_scene:
        subpixel True
        xpos 0.0 ypos -1.0 zoom 1.0
        easein_quad 10.0 xpos -0.5 ypos -0.8 zoom 1.0 #Dídac very visible.
    with fade
    
    n "Pasados unos días por casualidad, en un parque lejos de donde vives,"
    
    $ aftermorning04_fr_aftercum_park_d_eyestoscreen = True
    
    show aftermorning04_fr_aftercum_park_scene:
        xpos -0.5 ypos -0.8 zoom 1.0
    with dissolve
       
    n "cruzaste la mirada con tu antiguo compañero de piso."
    
    if aftermorning04_fr_rape_cumed_in == True:

        show aftermorning04_fr_aftercum_park_d_body female
        hide aftermorning04_fr_aftercum_park_d_body
        
        $ aftermorning04_fr_aftercum_park_d_eyestoscreen = False
        
        show aftermorning04_fr_aftercum_park_scene
        with dissolve
    
        n "Vestía con ropajes masculinos, algo más ceñidos, por lo que se hacía evidente que llevaba sujetador."
        
    elif aftermorning04_fr_rape_cumed_out == True or aftermorning04_fr_rape_bite_Cond == True:

        show aftermorning04_fr_aftercum_park_d_body male
        hide aftermorning04_fr_aftercum_park_d_body
        
        n "Había recuperado su forma masculina."
        
        $ aftermorning04_fr_aftercum_park_d_eyestoscreen = False
        show aftermorning04_fr_aftercum_park_scene
        with dissolve
        
        n "De alguna forma -probablemente por compasión-, Neus se había apiadado de él y le devolvió su estado original."
    
    show aftermorning04_bg fr_aftercum_park:
        subpixel True
        xpos -0.5 ypos -0.8 zoom 1.0 #Dídac very visible.
        easein_quad 10.0 xpos 0.0 ypos 0.0 zoom 0.5 #Whole park visible.
    with dissolve

    n "Ni siquiera te devolvió el saludo que intentaste ofrecerle."

    scene beds_morning_lightOff_blindDown_DemptyMCempty
    with fade
    
    n "Se apuntó a otro máster de Diseño de la ciudad por los rumores que pudiste oír entre chismorreos de compañeros."
    show beds_night_lightOff_blindUp_DemptyMCempty:
        subpixel True
        alpha 0.0
        easeout_quad 6.0 alpha 1.0
    
    n "Y nunca más volviste a saber nada de él ni de Neus."
    
    if aftermorning04_fr_rape_cumed_in == True:
    
        n "En el fondo, te alegraste de que tu amigo hubiera podido adaptarse a su nuevo estilo de vida."
        
        n "La verdad, es que después de lo sucedido, te habías temido lo peor..."
        
    elif aftermorning04_fr_rape_cumed_out == True or aftermorning04_fr_rape_bite_Cond == True:
        
        n "En el fondo, te alegraste de que tu amigo hubiera podido recuperar su cuerpo original."
    
    show black:
        subpixel True
        alpha 0.0
        easeout_quad 6.0 alpha 1.0

    n "Aunque te entristecía profundamente no poder volver a tener la oportunidad de disculparte"
    
    n "y de recuperar esa buena amistad que tenías con aquel amigo que mantenías desde que tienes memoria."
    
    n "Con aquel que considerabas incluso más que un hermano."

    $ persistent.gameOver_aftmor04_fr_rape_general = True
    
    if aftermorning04_fr_rape_cumed_in == True:

        $ persistent.gameOver_aftmor04_fr_rape_cumIn = True
    
        aj "Final alternativo 02a." with dissolve
        
    elif aftermorning04_fr_rape_cumed_out == True:

        $ persistent.gameOver_aftmor04_fr_rape_cumOut = True
        
        aj "Final alternativo 02b." with dissolve
        
    elif aftermorning04_fr_rape_bite_Cond == True:

        $ persistent.gameOver_aftmor04_fr_rape_bite = True

        aj "Final alternativo 02c"
    
    jump gameover

###########################################
##########################################
    
                    ##Left for later.
                    
label aftermorning04_fr_rape_handonmouth_bite:
    
    scene aftermorning04_fr_rape_bite
    show border_lines 04:
        subpixel True
        truecenter
        zoom 0.6
        xpos 0.61 ypos 0.64
        easein_bounce 1.0 zoom 0.32
        easein_quad 1.0 zoom 0.5

    with vpunch

    play sound "audio/characters/protagonist/scream01.ogg"
    
    p "{size=72}¡AARHHG!{/size}" with vpunch
    
    scene black
    with hpunch
    
#########################################################
    
    if config.version <= "00.03.09": #10$ PATREONS= 15 March /ALL PATREON = ? May FREE= ?
        
        call endupdatescript
    
#######################################################
    
    ##vpunch and  Image of she kicking you with her foot.

    play sound "audio/sfx/punch01.ogg"
    stop music fadeout 0.5
    
    ono "{size=62}¡PUM!{/size}"

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_naked_wet 02:
        dfbody_atright_closex2
    show didacfbodytop brablack:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_top empty:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2


    show didacf_blush 04:
        dfexpressions_atright_closex2
    show didacf_eyes 00:
        dfexpressions_atright_closex2
    show didacf_pupils front00:
        dfexpressions_atright_closex2
    show didacf_eyebrows angryx04:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Talkingx09:
        dfexpressions_atright_closex2
    with fade

    

    play music "audio/music/alcaknight/bury_it.ogg" fadein 0.5 fadeout 0.5
    
    d "{size=32}¡¿SE PUEDE SABER QUÉ ESTÁS HACIENDO IMBÉCIL?!{/size}"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "¡Has sido tú quien me ha estado provocando todo este tiempo!"

    show didacf_blush 03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx08
    with dissolve
       
    p "¡¿Ahora te quejas?!"

    show didacf_blush 04
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡SERÁS GILIPOLLAS!"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡¿No te das cuenta de que solo estaba bromeando?!"

    show didacf_blush 03
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "¡¿A eso lo llamas bromear?!"

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Imbécil de mierda..."

    show didacf_blush 03
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "¡Soy Dídac!"

    show didacf_blush 03
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "¡¿Acaso no te das cuenta de lo que me has hecho?!"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡Soy un tío!"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "Nadie lo diría por lo mojada que estabas..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Y aunque no lo fuera..."
    
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "En el momento en que te he dicho que quería parar." 
    
    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve
       
    d "¡Es porque quería parar!"

    show didacf_blush 02
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "¡Cuando le hiciste lo mismo a Neus en el baño no pensabas igual!"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx04
    with dissolve
    
    pt "Hablando de eso, espero que ahora yo no me convierta en una chica después de la mordida..."

    show didacf_blush 01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "¡¿De qué demonios me estás hablando?! ¡capullo!"

    show didacf_blush 01
    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx06
    with hpunch
    
    s "¡Será mejor que salgan ambos del probador inmediatamente!"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    s "¡¿Se han creído que esto es un circo?!"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx08
    with dissolve
    
    n "La voz autoritaria de lo que parecía obviamente un agente de seguridad"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    n "detuvo en seco la discusión que estabas teniendo con Dídac."
    
    show didacf_blush 02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "..."

    extend " ¡Mierda!"

    show didacfbodytop naked

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve
    
    n "Ambos empezáis a vestiros tan deprisa como podéis."

    show didacfbodycloth_top maleshirt

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "Es tu culpa."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "Idiota."

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve
    
    s "No nos obliguéis a entrar."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx08
    with dissolve
    
    jump aftermorning04_fr_rape_outoffittingroom

label aftermorning04_FittingRoom_RapedNo:

    scene aftermorning04_bg_fittingroomin

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_naked_wet 02:
        dfbody_atright_closex2
    show didacfbodytop brablack:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 02:
        dfexpressions_atright_closex2
    show didacf_eyes 02:
        dfexpressions_atright_closex2
    show didacf_pupils left02:
        dfexpressions_atright_closex2
    show didacf_eyebrows sadx02:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_closex2
    with dissolve

    p "<{size=18}Tienes razón, Dídac...{/size}>"

    show didacf_eyes 04
    show didacf_pupils left04
    with dissolve
    
    p "<{size=18}Es solo que,"
    
    extend " joder...{/size}>"

    show didacf_blush 03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx01
    with dissolve 
    
    p "<{size=18}Estás como un puto tren...{/size}>"

    show didacf_blush 04
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx03
    show didacf_mouth happybiting_Silentx03
    with dissolve 
    
    d "..." # She blushes

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_eyebrows sadx02
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    p "<{size=18}Y tus provocaciones tampoco ayudan demasiado...{/size}>"

    show didacf_blush 04
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve 
    
    d "..." # She is ashamed.

    show didacf_blush 03
    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve 
    
    d "<{size=18}Sí,"

    extend " ya lo sé...{/size}>"

    d "<{size=18}Lo siento [protname];{/size}>"

    d "<{size=18}No sé qué me pasa...{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx02
    with dissolve 
    
    d "<{size=18}Es tenerte cerca, y me pongo estúpido.{/size}>"

    d "<{size=18}Creo que lo más sensato sería que te fueras...{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx000
    with dissolve 
    
    p "<{size=18}¿Quieres que me vaya?{/size}>"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx01
    with dissolve 
    
    d "<{size=18}¿Qué harás si te quedas?{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx02
    with dissolve 
    
    d "..." # Blushes

    show didacf_blush 04
    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx05
    with dissolve 
    
    p "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx02
    with dissolve 
    
    d "<{size=18}¿Lo ves?{/size}>"

    d "<{size=18}Es una mala idea...{/size}>"

    d "<{size=18}Vete [protname],"

    extend " ya nos veremos en casa.{/size}>" # Look other place, Sad Mood.

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve 
    
    d "<{size=18}Pero por ahora, es mejor que me quede aquí solo...{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx04
    with dissolve 

    n "Accedes a desgana."
    
    scene aftermorning04_bg_fittingroomin at Transform(zoom=1.3), Position(xpos = -0.3, xanchor=0.0, ypos=0.0, yanchor=0.0)

    show didacfhandrb brablack:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfbodycloth_top empty:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3
    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils right05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows sadx01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sadbiting_Silentx05:
        dfexpressions_atleft_closex3
    with dissolve
    
    n "Justo antes de irte, tienes la sensación de que Dídac quiere decirte algo,"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve 
    
    n "pero luego aparta la mirada y se distancia de ti."

    stop music fadeout 5.0
    $ renpy.music.set_volume(0.1, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_shop01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    $ morning04_Shopping_SalesWomanTalkg_Cond = True #Hablas con la dependienta.

    scene aftermorning04_bg fittingroomout
    #show afternoon04_saleswoman_body crossedarms at right
    #show afternoon04_saleswoman_blush 01 at right
    #show afternoon04_saleswoman_mouth sad_Silent at right
    #show afternoon04_saleswoman_eyes front02 at right
    #show afternoon04_saleswoman_eyebrows angry at right
    #show afternoon04_saleswoman_glasses at right
    #with fade

    show afternoon04_saleswoman_body_crossedarms_b:
        afternoon04_saleswoman_body_pos

    show afternoon04_saleswoman_exp_blush 02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_mouth sad_Silentx02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyes 02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_piris front02:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_eyebrows angryx01:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_glasses:
        afternoon04_saleswoman_exp_pos
    show afternoon04_saleswoman_exp_hairfront:
        afternoon04_saleswoman_exp_pos
    with fade
    
    n "Al apartar la cortina descubres sin demasiada sorpresa que la dependienta estaba ahí, con cara de pocos amigos, "
    

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Silentx03
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris front03
    show afternoon04_saleswoman_exp_eyebrows angryx02
    with dissolve
    
    n "aunque con cierto rubor en su rostro, escuchando tras la cortina."

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Silentx01
    show afternoon04_saleswoman_exp_eyes 02
    show afternoon04_saleswoman_exp_piris down02
    show afternoon04_saleswoman_exp_eyebrows normal
    with dissolve
    
    pt "Esta situación se me está escapando de las manos..."

    show afternoon04_saleswoman_exp_blush 03
    show afternoon04_saleswoman_exp_mouth sad_Silentx03
    show afternoon04_saleswoman_exp_eyes 03
    show afternoon04_saleswoman_exp_piris left03
    show afternoon04_saleswoman_exp_eyebrows angryx01
    with dissolve
    
    n "Vuelves en metro al piso que compartís."
        
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
        
label aftermorning04_Mast001_GoodEnding:
    
    d "<{size=18}Hummm...{/size}>"

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils front05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Talkingx05:
        dfexpressions_atleft_closex3

    with dissolve
    
    
    d "<{size=18}Así que quieres jugar duro..."

    extend " ¿Verdad?{/size}>"
    
    #Aquí es donde Dídac empieza a masturbarte en serio. Didac Masturbación step 01 (normal speed).
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast 005:
        subpixel True
        #zoom 0.3 xpos 0.3 #For Experiments.
        xpos -1.0 ypos -1.0 zoom 1.0 #Close Shot
        easein_quad 10.0 xpos -0.25 ypos -0.9 zoom 0.7
        #easein_quad 2.0 xpos -0.1 ypos -0.5 zoom 0.5 #Far Shot
    with dissolve
    
    window hide dissolve
    
    pause
    
    n "Su mano se impone desde abajo agarrándote la polla con fuerza."
    
    n "Deslizándose de arriba abajo con cierta celeridad."

    play sound "audio/characters/didac/moanings04.ogg"
    
    d "Ahhh-mmm... AHmmmm..." # Feminine Moans  *gemidos femeninos* 
    
    n "Sientes su cálida y agitada respiración en tu cuello al mismo tiempo que oyes sus ahogados gemidos."
    
    n "A pesar de tus constantes movimientos de cadera, tu polla sigue firmemente aferrada a su mano."
       
    n "Te percatas del leve escalofrío que recorre tu cuerpo, claro indicio de que pronto vas a estallar."
    
    p "Dídac,"

    extend " si sigues así,"

    extend " yo no sé si podré..."
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast 005:
        subpixel True
        xpos -0.25 ypos -0.9 zoom 0.7
        block:
            easein_quad 2.0 xpos -0.25 ypos -0.9 zoom 0.7
            easeout_quad 2.0 xpos -0.28 ypos -0.95 zoom 0.73
            repeat
    
    n "Sus dedos se contraen aún más, aumentando la asfixia que sufre tu palpitante y erecta polla."

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 02:
        dfexpressions_atleft_closex3
    show didacf_eyes 03:
        dfexpressions_atleft_closex3
    show didacf_pupils down03:
        dfexpressions_atleft_closex3
    show didacf_eyebrows surprisex02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx004:
        dfexpressions_atleft_closex3

    with dissolve
    
    d "No tienes mucho aguante..."

    extend " ¿Verdad...?"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx06
    with dissolve 

    d "¿Haces siempre lo mismo?"

    d "¿Terminar antes...?"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx06
    with dissolve 
    
    d "Vaya semental estarás hecho..."

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx06
    with dissolve

    play sound "audio/characters/didac/giggle01.ogg"
    
    p "..."    #Una risa burlona aparece en sus labios.
    
    menu aftermorning04_Mast001_EndingMast:
            
        pt "Me está provocando..." 
            
        "<Detener esta locura>":
            
            call p_Help
                
            $pl.ch_pts("dp",-1)
                    
            jump aftermorning04_Masturbation_SadEnding
            
        "<Ir más rápido metiéndole el dedo en el culo>" if aftermorning04_Mast001_Anal_insert == True and aftermorning04_Mast001_Pussy_insert == False:
            
            call p_Help
            
            #Si es anal:
            
            if pl.dp >= 28: #21 is the minimum so Didac Allow Anal Fingers
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 28[hd]")
                
                $pl.ch_pts("dp",4) #If points are HIGH. Didac Will love it! Cum ONLY BY ANAL! and you don´t cum.
                
                $ aftermorning04_Mast001_AnalFast_Happy = True #CUM Didac TWICE. (High Points)
                
            else:
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 28[hd]")
            
                $pl.ch_pts("dp",-1) #If points are MED/Low. Didac Will not like it very much. You´ll not cum, neither her.
                
                $ aftermorning04_Mast001_AnalFast_Angry = True #Didac gets angry, No one , Rape?
            
            $ aftermorning04_Mast001_AnalFast_insert = True 
                    
            jump aftermorning04_Masturbation_Ending #Pondrá cara de sorprendida cuando se corra cagándose en ti por haber sido solo anal.
            
        "<Ir más rápido metiéndole el dedo en el coño>" if aftermorning04_Mast001_Pussy_insert == True and aftermorning04_Mast001_Anal_insert == False:
            
            call p_Help
            
            if pl.dp >= 27: #21 is the minimum so Didac Allow Pussy Fingers
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 27[hd]")
                
                $pl.ch_pts("dp",2) #She´ll cum twice and you not a single one.
                
                $ aftermorning04_Mast001_PussyFast_Happy = True #CUM Didac TWICE. (High Points) ONLY BY VAGINA
                
            else:
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 27[hd]")
                
                $pl.ch_pts("dp",1) #She´ll cum just once and then you cum.
                
                $ aftermorning04_Mast001_PussyFast_Angry = True #Didac gets sad, You did cum fast.
            
            $ aftermorning04_Mast001_PussyFast_insert = True # CUM MC first. (if Points are not High)
                    
            jump aftermorning04_Masturbation_Ending #Algo previsible, pero que no le disgustará.
            
        "<Metérselo también por el agujero negro y aumentar el ritmo de ambos>" if aftermorning04_Mast001_Pussy_insert == True and aftermorning04_Mast001_Anal_insert == False:
            
            call p_Help
            
            if pl.dp >= 24: #21 es el mínimo que acepta vaginalmente también. y suma 1
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 24[hd]")
            
                $pl.ch_pts("dp",3)
                
                $ aftermorning04_Mast001_PussyFast_insert = True
            
                $ aftermorning04_Mast001_AnalFast_insert = True #CUM Didac TWICE. (If points are High)
                
                $ aftermorning04_Mast001_AnalFastAfter_Happy = True
                    
                jump aftermorning04_Masturbation_Ending #Te reprochará que le hayas tenido que meter también el dedo en el ano, pero le habrá encantado.
                
            else: #Didac se cabrea porque le metes un dedo por el ano.

                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 24[hd]")
                
                $pl.ch_pts("dp",-1)
                
                $ aftermorning04_Mast001_PussyFast_insert = True
            
                $ aftermorning04_Mast001_AnalFast_insert = True #CUM Didac TWICE. (If points are High)
                
                $ aftermorning04_Mast001_AnalFastAfter_Angry = True
                
                jump aftermorning04_Masturbation_Ending #Se enfadará contigo.
            
            
        "<Metérselo también por su agujero húmedo y aumentar el ritmo de ambos>" if aftermorning04_Mast001_Anal_insert == True and aftermorning04_Mast001_Pussy_insert == False: 
            
            call p_Help
            
            $pl.ch_pts("dp",2) #La sensación le gusta sin necesidad de Condicionales de según que puntuación.
            
            $ aftermorning04_Mast001_PussyFast_insert = True
            
            $ aftermorning04_Mast001_AnalFast_insert = True #CUM MC first. (if points are not high)
            
            $ aftermorning04_Mast001_PussyFastAfter_Happy = True
            
            # d "Hummm... Sí... por este agujero también me gusta..."
                    
            jump aftermorning04_Masturbation_Ending #Te reprochará el que hubieras empezado por el culo, pero que no le ha disgustado del todo. 
            
        "<Aumentar el ritmo de la mano y profundizar más en ambos agujeros>" if aftermorning04_Mast001_Anal_insert == True and aftermorning04_Mast001_Pussy_insert == True:
            
            call p_Help
                
            $pl.ch_pts("dp",2) #La sensación le gusta sin necesidad de Condicionales de según que puntuación.
            
            $ aftermorning04_Mast001_PussyFast_insert = True
            $ aftermorning04_Mast001_AnalFast_insert = True #CUM MC first. (if points are not high)
            
            $ aftermorning04_Mast001_PussyFastAfter_Happy = True #Estos dos son un error, pero ya están puestos aquí... así que da igual.
            $ aftermorning04_Mast001_AnalFastAfter_Happy = True
                    
            jump aftermorning04_Masturbation_Ending #Te reprochará que le haysa tenido que meter también el dedo en el ano, pero le habrá encantado.

            
label aftermorning04_Masturbation_Ending:
    
    #Image of FAST masturbate.
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 004:
        subpixel True
        xpos -0.8 ypos -1.0 zoom 0.8 #Inicial Pose
        easein_quad 1.0 xpos -0.45 ypos -0.5 zoom 0.5

    with fade
    pause 1.0
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        subpixel True
        block:
            easein_quad 0.32 xpos -0.46 ypos -0.51 zoom 0.51
            easeout_quad 0.32 xpos -0.45 ypos -0.5 zoom 0.5
            repeat
        #zoom 0.3
    with dissolve

    window hide dissolve
    pause
    
#########################################################
    
    if config.version <= "00.03.03": #ALL PATREONS= 30 April / FREE= ?
        
        call endupdatescript
        
#######################################################
    
    if aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFastAfter_Happy == True and aftermorning04_Mast001_PussyFastAfter_Angry == False and aftermorning04_Mast001_AnalFastAfter_Happy == True and aftermorning04_Mast001_AnalFastAfter_Angry == False:
        
        $ debug ("BothHoles")
        jump aftermorning04_FastMast_BothHoles
        
    elif aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFastAfter_Happy == True and aftermorning04_Mast001_PussyFastAfter_Angry == False and aftermorning04_Mast001_AnalFastAfter_Happy == False and aftermorning04_Mast001_AnalFastAfter_Angry == False:
        
        $ debug ("NowPussy Happy")
#########################################################
    
        if config.version <= "00.03.04": #10$ PATREONS= 15 Feb /ALL PATREON = ? FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_NowPussy_Happy #There´s no Pussy_Angry
        
    elif aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFastAfter_Happy == False and aftermorning04_Mast001_PussyFastAfter_Angry == False and aftermorning04_Mast001_AnalFastAfter_Happy == True and aftermorning04_Mast001_AnalFastAfter_Angry == False:
        
        # progcheck  "NowAnal Happy"
#########################################################
    
        if config.version <= "00.03.04": #10$ PATREONS= 15 Feb /ALL PATREON = ? FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_NowAnal_Happy
        
    elif aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFastAfter_Happy == False and aftermorning04_Mast001_PussyFastAfter_Angry == False and aftermorning04_Mast001_AnalFastAfter_Happy == False and aftermorning04_Mast001_AnalFastAfter_Angry == True:
        
        # progcheck  "NowAnal Angry"
#########################################################
    
        if config.version <= "00.03.05": # FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_NowAnal_Angry
        
    elif aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFast_Happy == True and aftermorning04_Mast001_AnalFast_Happy == False:
        
        # progcheck   "OnlyPussy Happy"
#########################################################
    
        if config.version <= "00.03.04": #10$ PATREONS= 15 Feb /ALL PATREON = ? FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_OnlyPussy_Happy
        
    elif aftermorning04_Mast001_PussyFast_insert == True and aftermorning04_Mast001_PussyFast_Angry == True and aftermorning04_Mast001_AnalFast_Happy == False:
        
        # progcheck  "OnlyPussy Angry"
#########################################################
    
        if config.version <= "00.03.05": # FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_OnlyPussy_Angry
        
    elif aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_AnalFast_Happy == True and aftermorning04_Mast001_PussyFast_Happy == False:
        
        # progcheck  "OnlyAnal Happy"
#########################################################
    
        if config.version <= "00.03.04": #10$ PATREONS= 15 Feb /ALL PATREON = ? FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_OnlyAnal_Happy
        
    elif aftermorning04_Mast001_AnalFast_insert == True and aftermorning04_Mast001_AnalFast_Angry == True and aftermorning04_Mast001_PussyFast_Happy == False:
        
        # progcheck  "OnlyAnal Angry"
#########################################################
    
        if config.version <= "00.03.04": #10$ PATREONS= 15 Feb /ALL PATREON = ? FREE= ?
            
            call endupdatescript
        
#######################################################
        jump aftermorning04_FastMast_OnlyAnal_Angry
        
        
label aftermorning04_FastMast_BothHoles:

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    #n "Aquí es cuando ya tenías ambos agujeros ocupados y decides meterle caña a los dos."

    $ morning04_Shopping_didaccum_Cond = True #Conditional Didac cums.
    
    n "Sientes cómo sus gemidos aumentan en rapidez y fuerza, cómo se retuerce encima de ti,"
    
    call aftermorning04_FastMastDick
    
    n "cómo arrastra su cabeza por tu pecho al descubierto."
    
#######################################

    transform aftermorning04_bg_fittingroom_mast_dass_005_beforecumming:
        subpixel True
        block:
            easein_quad 0.32 xpos -0.46 ypos -0.51 zoom 0.51
            easeout_quad 0.32 xpos -0.45 ypos -0.5 zoom 0.5
            repeat
                
    transform aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming:
        subpixel True
        block:
            easein_quad 0.32 xpos -0.65 ypos -0.7 zoom 0.6
            easeout_quad 0.32 xpos -0.46 ypos -0.51 zoom 0.51
            repeat

#######################################
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming

    with dissolve
    
    n "El movimiento de tus dedos no cesa en absoluto penetrando sin compasión ambas cavidades."
    
    n "Percibes en la palma de tu mano la suave y tierna piel de sus muslos."

    n "El calor que desprenden sus labios internos es cada vez más evidente al introducir frenéticamente tus dedos en ella." 
       
    n "Adviertes la succión al vacío en sus adentros por su abundante y cálida humedad,"
    
    n "cada vez que te retiras para coger impulso y volver a entrar violentamente."

    n "Sus gemidos se aceleran y paulatinamente va perdiendo la capacidad de controlar su tono de voz."
       
    n "A duras penas, puede mover ya la mano con la que te estaba masturbando -con celeridad- hace apenas unos segundos,"
    
    n "Si hubiera seguido ese ritmo, a estas alturas ya habrías manchado su vientre y el suelo con tu cálida semilla."
    
    n "Te percatas de que poco a poco, va perdiendo totalmente la fuerza, y su cuerpo ya no le responde."
    
    #scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    
    show closetocum_other #Image becoming black at 70% in 1 second interval.
    with dissolve

    n "Penetras sin piedad en sus adentros y consigues que ambos dedos profundicen tanto como tus nudillos te lo permiten."

    n "Una vez ahí dentro, los desplazas como si fueran tentáculos en forma de tijeras que se contraen y se expanden."
    
    show cumming_other #Image becomes white in 1 second.

    play sound "audio/characters/didac/orgasm03.ogg"

    d "<{size=18}AAhhh... mmm-ffffh... aaah... {/size}>" #Soft feminine moans *Gemidos femeninos* 
    
    #show aftermorning04_bg_fittingroomin_ground_PROVE: ##To pose objects
        #zoom 0.5
        
##############################################################################
        
    transform aftermorning04_bg_fittingroom_DKneels_anim_pose: #Didac Panting Camera Move
        subpixel True
        xpos -2.5 ypos -2.5 zoom 1.8
        easein_quad 10.0 xpos -0.1 ypos -0.1 zoom 0.6
        block:
            easein_quad 1.5 xpos -0.09 ypos -0.09 zoom 0.59
            easeout_quad 1.0 xpos -0.1 ypos -0.1 zoom 0.6
            repeat
            
##############################################################################

    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"
    
    scene aftermorning04_bg fittingroomin_ground: #background
        aftermorning04_bg_fittingroom_DKneels_anim_pose

    show aftermorning04_bg_fittingroom_DKneels_anim: #Didac Panting
        aftermorning04_bg_fittingroom_DKneels_anim_pose
    with fade
    #Imagen de rodillas (?)
    
    window hide dissolve
    pause

    n "Se desprende de lo que tenía en ambas manos por completo como si se hubiera rendido a la gravedad" 
       
    n "y cae al suelo de rodillas."

    p "Dídac,"

    extend " ¿estás bien?"

    d "Ah... Ah... Ah..." # Heavy breathing after ORGASM *Aliento acelerado* 

    n "La oyes jadear cabizbaja arrodillada en el suelo, intentando recuperar el aliento."

    d "Serás cabronazo..."
    
    #n "Observas como se reincorpora levántandose."

    d "Mi idea era hacer que te corrieras tú primero..."

    play sound "audio/characters/protagonist/giggle01.ogg"

    n "No puedes evitar sonreír ante esa curiosa confesión de tu compañero de piso."

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils down05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows sadx03:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sadbiting_Silentx05:
        dfexpressions_atleft_closex3
    with fade
    
    n "Con movimiento torpe, Dídac consigue ponerse de pie, con su cuerpo semidesnudo y empapado en sudor."
    
    jump aftermorning04_Masturbation_SadEnding02
    
    #de "¡Oiga! ¡¿Está usted bien?!"

label aftermorning04_FastMast_NowPussy_Happy:
    
    #n "Aquí es cuando tenías un dedo en el culo y decides metérselo ahora por el coño."

    $ morning04_Shopping_didaccum_Cond = True #Conditional Didac cums.
    
    n "Desplazas también tu dedo corazón en su zona púbica y empiezas a mover de forma acelerada tu muñeca"
    
    n "para penetrar ambas cavidades al unísono."
    
    d "<{size=18}¿Se puede saber qué haces?{/size}>"
    
    p "<{size=18}¿Por qué?"

    extend " ¿Preferías que me quedara solo con tu agujero anal?{/size}>"

    play sound "audio/characters/didac/moanings04.ogg"
    
    d "<{size=18}Aahh...{/size}>" # Muffled moan being a bit angry *Gemido femenino*
    
    d "<{size=18}Hijo de..."

    extend " puta...{/size}>"

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Aahh...{/size}>" # Muffled moan angry with herself *Gemido femenino*
    
    p "<{size=18}No parece que te disguste...{/size}>"
    
    call aftermorning04_FastMastDick
    
    d "<{size=18}Sabes que aquí donde me has metido el dedo,{/size}>"

    d "<{size=18}debería haber lo que yo te estoy tocando,"

    extend " ¿verdad?{/size}>"
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming
    with dissolve

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Aahh-Ahhh... Mmm...{/size}>" # Moaning excited/angry with herself for losing the bet *Gemido femenino*
    
    p "<{size=18}¿Eso significa que quieres que quite el dedo de tu húmedo coño?"

    extend " ¿O de tu jugoso culo?{/size}>"
    
    p "<{size=18}Porque ahora mismo no sabría decirte cuál de los dos resulta más homosexual...{/size}>"
    
    d "<{size=18}Vete a la mierda..."

    extend " cabrón, hijo de..."

    extend " Ahh...{/size}>" # Feminine Moan

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    show closetocum_other
    with fade

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Aahh-Ahhh... Hmmm...{/size}>" # Moaning (trying to win the bet) *Gemido femenino*
    
    d "<{size=18}Seguro que..."

    extend " no tardarás en..."

    extend " corrert...{/size}>"
    
    show cumming_other

    play sound "audio/characters/didac/orgasm04.ogg"
    
    d "¡AAAH-AAAHHH... AAAHAHHH!" # Loud feminine moans (Having an ORGASM) *Gemido agudo femenino* 

    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"

    scene aftermorning04_bg fittingroomin_ground:#background
        aftermorning04_bg_fittingroom_DKneels_anim_pose

    show aftermorning04_bg_fittingroom_DKneels_anim: #Didac Panting
        aftermorning04_bg_fittingroom_DKneels_anim_pose
    with fade
    #Imagen de rodillas (?)
    
    window hide dissolve
    pause

    d "Ahh... Ahh... Ahhhh..." # Heavy breathing after ORGASM *Respiración agitada* 
    
    p "<{size=18}Parece que no te ha disgustado tanto al fin y al cabo que te metiera también el dedo por ahí...{/size}>"
    
    n "Su cuerpo empieza a temblar dando indicios de querer reincorporarse."

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 08:
        dfexpressions_atleft_closex3
    show didacf_pupils front08:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx001:
        dfexpressions_atleft_closex3
    with fade

    d "..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "<{size=18}Hijoh..."

    extend " putah...{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "<{size=18}Cá-"

    extend "cállate...{/size}>"
    
    jump aftermorning04_Masturbation_SadEnding02
    
    #de "¡Oiga! ¡¿Está usted bien?!"
    
label aftermorning04_FastMast_NowAnal_Happy:
    
    #n "Aquí es cuando tenías un dedo en el coño y decides metérselo ahora por el culo."

    $ morning04_Shopping_didaccum_Cond = True #Conditional Didac cums.
    
    n "Después de estar acariciando sus carnes internas húmedas y ardientes con tu dedo corazón,"
    
    n "extiendes el dedo índice y -sin demasiada dificultad-, logras penetrar casi en su totalidad su oscuro agujero;"
    
    n "con menor humedad que su recién aparecida concha, pero muchísimo más estrecho."
    
    d "<{size=18}¡¿Dónde coño estás poniendo el dedo?!{/size}>"
    
    p "<{size=18}¿No te gusta...?{/size}>"
    
    d "<{size=18}¿Te crees que soy marica o qué?{/size}>"
    
    p "..."
    
    d "..."
    
    p "<{size=18}No me has dicho nada mientras tenía el dedo en el otro sitio...{/size}>"
    
    d "<{size=18}¿Y qué?{/size}>"
    
    p "<{size=18}Pues que eso tampoco es muy hetero...{/size}>"
    
    d "..."
    
    p "<{size=18}¿Quieres que pare?{/size}>"
    
    p "<{size=18}Porque no parece que te disguste la idea tampoco...{/size}>"
    
    call aftermorning04_FastMastDick
    
    d "<{size=18}No..."

    extend " No sé por qué lo dices...{/size}>"
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming
    
    p "<{size=18}Bueno,"

    extend " viendo que tú no paras,{/size}>"

    p "<{size=18}no seré yo quien lo haga...{/size}>"
    
    d "<{size=18}Je..."

    extend " Con lo bocachancla que eres,"
       
    d "<{size=18}estoy seguro de que no aguantarás ni un minuto antes de que...{/size}>"

    #stop music fadeout 3.0
    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    show closetocum_other
    with fade

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Aaah-Aaahmm... Mmmfff...{/size}>" # muffled moans *Gemido femenino* 
    
    d "<{size=18}¡Cabrón!..."

    extend " ¡Para de...!{/size}>"
    
    p "<{size=18}¿De verdad quieres que pare?{/size}>"
    
    d "<{size=18}¡Para, joder!{/size}>"

    d "<{size=18}Que me voy a...{/size}>"
    
    show cumming_other
    with vpunch

    play sound "audio/characters/didac/orgasm03.ogg"
    
    d "AAAH-AAAHHH... AAAHAHHH" # *Loud feminine moans, having an ORGASM* *Gemido agudo femenino* 

    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"
    
    scene aftermorning04_bg fittingroomin_ground: #background
        aftermorning04_bg_fittingroom_DKneels_anim_pose

    show aftermorning04_bg_fittingroom_DKneels_anim: #Didac Panting
        aftermorning04_bg_fittingroom_DKneels_anim_pose
    with fade
    #Imagen de rodillas (?)
    
    window hide dissolve
    pause

    d "Ahh... Ahh... Ahhhh..." # Heavy Breathing after ORGASM *Respiración agitada* 
    
    p "<{size=18}Parece que no te ha disgustado tanto al fin y al cabo que te metiera un dedo por el culo...{/size}>"
    
    n "Su cuerpo empieza a tambalearse mostrando voluntad de ponerse en pie."
    
    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 08:
        dfexpressions_atleft_closex3
    show didacf_pupils front08:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx001:
        dfexpressions_atleft_closex3
    with fade

    d "..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}Hijoh..."

    extend " Putah...{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "<{size=18}Cá-"

    extend "Cállate...{/size}>"
    
    jump aftermorning04_Masturbation_SadEnding02
    
    #de "¡Oiga! ¡¿Está usted bien?!"
    
label aftermorning04_FastMast_NowAnal_Angry:
    
    #n "Aquí es cuando tenías un dedo en el coño y decides metérselo ahora por el culo, pero se enfada."
    
    n "Con menor humedad que su recién aparecida concha,"

    n "metes sin piedad en su otro agujero -muchísimo más estrecho-, el dedo índice."
    
    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 01:
        dfexpressions_atleft_closex3
    show didacf_eyes 01:
        dfexpressions_atleft_closex3
    show didacf_pupils front01:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx05:
        dfexpressions_atleft_closex3
    with dissolve
    
    d "<{size=18}¡¿Dónde coño estás poniendo el puto dedo?!{/size}>"

    show didacf_blush 01
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with hpunch
    
    n "Te coge por la muñeca y te aparta la mano de su entrepierna sin vacilar."

    show didacf_blush 01
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "<{size=18}¿No te gusta...?{/size}>"
    
    show didacf_blush 01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "<{size=18}¡¿A ti te parece que eso me puede gustar?!{/size}>"

    show didacf_blush 01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "<{size=18}¡Tú estás enfermo!{/size}>"

    d "<{size=18}¡¿Te crees que soy maricón o algo?!{/size}>"

    show didacf_blush 01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "<{size=18}Mira,{/size}>"

    d "<{size=18}lo mejor será que te vayas y me dejes solo,"

    extend " gilipollas...{/size}>"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "<{size=18}¿Pero qué te pasa ahora?{/size}>"

    p "<{size=18}¿Te molesta que te haya puesto el dedo en el culo?{/size}>"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "<{size=18}Vale,"

    extend " lo siento,{/size}>"

    p "<{size=18}pensé que sería una buena idea probar suerte viendo lo que te gustaba por el otro lado...{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "<{size=18}Tío...{/size}"

    extend " {size=18}Joder...{/size}>"

    d "<{size=18}¡¿Pero te estás oyendo?!{/size}>"

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "<{size=18}¡Me estabas metiendo un dedo por un puto agujero que no debería ni existir!{/size}>"


    show didacf_blush 01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "<{size=18}¡Soy Dídac!{/size}"

    extend "{size=18} ¡¿Te acuerdas?!{/size}>"

    d "<{size=18}¡Camaradas de copas!"

    extend "{size=18} ¡Compañeros de equipo de fútbol desde los ocho años!{/size}>"

    show didacf_blush 01
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "<{size=18}¡Me hubieras hecho esto hace tres días y te hubiera roto la puta espalda!{/size}>"

    show didacf_blush 01
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "<{size=18}Hace tres días no eras así,{/size}>"

    p "<{size=18}además,{/size}"

    extend "{size=18} ¡has sido tú quien me ha estado provocando todo este tiempo!{/size}>"

    show didacf_blush 01
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "<{size=18}Ya lo sé,{/size}"

    extend "{size=18} lo sé...{/size}>"

    show didacf_blush 01
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "<{size=18}Lo siento,{/size}"

    extend "{size=18} no sé qué me está pasando...{/size}>"


    show didacf_blush 01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "<{size=18}Pero, por favor...{/size}>"

    d "<{size=18}Para.{/size}>"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    jump aftermorning04_StoporNot #Rape
    
label aftermorning04_FastMast_OnlyPussy_Happy:
    
    #n "Aquí es cuando decides no tocar el culo y meter más rápido el dedo en el coño y consigue 2 orgasmos debido a que iba cachonda."

    $ morning04_Shopping_didaccum_Cond = True #Conditional Didac cums.
    
    n "Decides permanecer únicamente dentro de sus carnes internas húmedas y ardientes con tu dedo corazón,"
    
    n "pero no sin aumentar considerablemente el ritmo de penetración,"
    
    n "moviendo aceleradamente tu muñeca chocando con más intensidad contra sus labios vaginales."
    
    #Face Dídac Enjoying it.

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Ahh... Ahhh...{/size}>" # *Gemido femenino* 
    
    p "<{size=18}Dídac,{/size}>"

    p "<{size=18}sabes que estás dejándome la mano empapada...{/size}"

    extend "{size=18} ¿Verdad?{/size}>"

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 06:
        dfexpressions_atleft_closex3
    show didacf_pupils front06:
        dfexpressions_atleft_closex3
    show didacf_eyebrows sadx03:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx003:
        dfexpressions_atleft_closex3
    with dissolve
    
    d "<{size=18}Puto imbécil de mierda...{/size}"

    d "{size=18}¿Acaso no te das cuenta de que lo que estás tocando no debería ni existir,"

    extend " Capullo...{/size}>"
    
    call aftermorning04_FastMastDick
    
    p "<{size=18}Puedo saber entonces,{/size}>"

    p "<{size=18}¿qué está haciendo tu mano con mi polla?{/size}>"
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming
    with fade

    play sound "audio/characters/didac/moanings02.ogg"
    
    d "<{size=18}Cá-" # Between moans being excited/angry for losing *Entre gemidos* 

    extend " Ahh..." 

    extend "-llate..."

    d "Ahh..."

    extend" Idiota...{/size}>" 

    play sound "audio/characters/didac/moanings03.ogg"
    
    d "<{size=18}Seguro que no tardarás...{/size}"

    extend "{size=18} na-{/size}"

    extend "{size=18}nada...{/size}"

    extend "{size=18} en corrert...{/size}>"

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    show closetocum_other
    with fade

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Aaahmm... Aaah... mmmfff...{/size}>" # muffled moans *Gemido femenino* 
    
    d "<{size=18}¡Cabrón...{/size}"

    extend "{size=18} ¡Para...!{/size}>"
    
    p "<{size=18}¿De verdad quieres que pare?{/size}>"
    
    d "<{size=18}¡Para, joder!{/size}>"

    d "<{size=18}Que me voy a...{/size}>"
    
    show cumming_other
    with vpunch

    play sound "audio/characters/didac/orgasm02.ogg"
    
    d "¡AAAH-AAAHHH...! ¡AAAHAHHH...!" # loud moans, having an ORGASM *Gemido agudo femenino* 

    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"
    
    scene aftermorning04_bg fittingroomin_ground: #background
        aftermorning04_bg_fittingroom_DKneels_anim_pose

    show aftermorning04_bg_fittingroom_DKneels_anim: #Didac Panting
        aftermorning04_bg_fittingroom_DKneels_anim_pose
    with fade
    #Imagen de rodillas (?)
    
    window hide dissolve
    pause
    
    d "Ahh... Ahh... Ahhhh..." # Heavy breathing after orgasm *Respiración agitada* 
    
    p "<{size=18}Parece que disfrutaste más con lo que tienes ahora entre las piernas,{/size}>"

    p "<{size=18}que yo, con lo mismo que tenías antes tú...{/size}>"
    
    n "Su cuerpo empieza a tambalearse mostrando voluntad de ponerse en pie."

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 08:
        dfexpressions_atleft_closex3
    show didacf_pupils front08:
        dfexpressions_atleft_closex3
    show didacf_eyebrows sadx01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx001:
        dfexpressions_atleft_closex3
    with fade

    d "..."

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx002
    with dissolve

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}Put-{/size}"

    extend "{size=18}Ahh...{/size}"

    extend "{size=18} cá-{/size}"

    extend "{size=18}cállate...{/size}>"
    
    jump aftermorning04_Masturbation_SadEnding02
    
label aftermorning04_FastMast_OnlyPussy_Angry:
    
    #n "Aquí es cuando decides no tocar el culo y meter más rápido el dedo en el coño, pero solo consigue un orgasmo debido a que no iba suficientemente cachonda y tú también te corres."
    
    $ morning04_Shopping_youcum_Cond = True #Conditional You cum.

    n "Decides permanecer únicamente dentro de sus carnes internas con tu dedo corazón,"
    
    n "pero no sin aumentar considerablemente el ritmo de penetración,"
    
    n "moviendo aceleradamente tu muñeca chocando con más intensidad contra sus labios vaginales."

    play sound "audio/characters/didac/moanings05.ogg"
    
    d "<{size=18}Mmm...{/size}>" # Feminine malicious Groan *Gemido femenino* 
    
    d "<{size=18}¿Te crees que yo no sé jugar al mismo juego?{/size}>"
    
    call aftermorning04_FastMastDick
    
    n "Las palpitaciones de tu polla son cada vez más aceleradas."

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming
    show closetocum_mc
    with dissolve
    
    p "<{size=18}Ahhh-Ahh... Mmmh...{/size}>" # Moaning having your dick masturbated *Gemido masculino* 

    play sound "audio/characters/didac/moanings02.ogg"
    
    d "<{size=18}MMm..." # Between moans *Entre gemidos femeninos* 

    extend " Creo que...{/size}>"

    d "<{size=18}no vas a tardar mucho...{/size}>"

    d "<{size=18}ahh..."

    extend " en..."

    extend " correrte...{/size}>" 
    
    pt "Mierda... no voy a aguantar mucho más así..."
    
    n "Intentas no perder el ritmo metiéndole el dedo con ferocidad en su interior,"
    
    scene aftermorning04_bg fittingroomin
    show aftermorning04_bg_fittingroom_mast 006:
        subpixel True
        block:
            easein_quad 0.2250 xpos -0.37 ypos -1.05 zoom 0.8 #Close Shot
            easeout_quad 0.2250 xpos -0.38 ypos -1.08 zoom 0.81 #Close Shot
            repeat
            
    show closetocum_mc
    with dissolve
    
    n "pero poco a poco vas perdiendo las fuerzas."
    
    ##scene aftermorning04_bg fittingroomin
    show aftermorning04_bg_fittingroom_mast 007:
        subpixel True
        ##zoom 0.3 xpos 0.3 #For Experiments.
        xpos 0.18 ypos -0.22 zoom 0.45
        block:
            easein_bounce 0.3 xpos 0.18 ypos -0.22 zoom 0.45
            easeout_bounce 2.0 xpos 0.14 ypos -0.28 zoom 0.5
            repeat
    show closetocum_mc
    with dissolve
    pause 5.0
    show cumming_mc
        
    window hide dissolve
    pause
    
    #Corrida masculina

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 02:
        dfexpressions_atleft_closex3
    show didacf_eyes 05:
        dfexpressions_atleft_closex3
    show didacf_pupils front05:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth happy_Silentx05:
        dfexpressions_atleft_closex3
    with fade
    
    n "Sin poder evitarlo un segundo más, dejas el suelo empapado con tu semilla."

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx05
    with dissolve
    
    d "<{size=18}Mira el galán,"

    extend " no ha podido aguantarlo más...{/size}>"

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Silentx04
    with dissolve
    
    p "<Ahh... ahh... Ahh...>" # Heavy breathing after Orgasm, being defeated by Didac. *Suspiros de cansancio* 

    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "<{size=18}Vaya..."

    extend " ¿Estás cansado?...{/size}>"

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx06
    with dissolve
    
    n "Tu rostro no puede evitar poner una mueca de orgullo herido."

    show didacf_blush 02
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Talkingx07
    with dissolve

    play sound "audio/characters/didac/laugh01.ogg"
    
    d "{size=60}¡¡JajAjaJaja!!{/size}" # Loud Laugh after winning the non-written bet *Risa femenina aguda* 

    show didacf_blush 02
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    with dissolve
    
    pt "Está claro que la sutileza no es lo suyo."

    pt "Espero que nadie la haya oído..."

    show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx06
    with dissolve
    
    n "Intentas reincorporarte en la medida de lo posible después de la corrida,"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows normal
    show didacf_mouth happybiting_Silentx05
    with dissolve
       
    n "para volver a meterle los dedos dentro de ella y que Dídac consiga también su orgasmo."
    
    jump aftermorning04_Masturbation_SadEnding02
    
label aftermorning04_FastMast_OnlyAnal_Happy:
    
    #n "Aquí es cuando decides no tocar el coño y meterlo más rápido, consiguiendo que se corra analmente, se enfada pero le pone super burra."

    $ morning04_Shopping_didaccumANAL_Cond = True #Didac cum, but only for anal.

    d "<{size=18}Ahhhh-Ahh... Hmmm...{/size}>"# Feminine Moan *Gemido femenino* 
    
    n "Sin piedad, empiezas a penetrar duramente su cavidad anal chocando violentamente contra sus glúteos."
    
    d "<{size=18}Ahh..." # Among Moans *Entre gemidos femeninos* 

    extend " Euhh...{/size}>"

    d "<{size=18}¿Por qué...{/size}"

    extend "{size=18} coño...{/size}"

    extend "{size=18} me sigues metiendo el dedo ahí?{/size}>"

    play sound "audio/characters/didac/moanings03.ogg"

    d "Hhmmm..." # Moaning
    
    p "<{size=18}¿Acaso te disgusta?{/size}>"

    play sound "audio/characters/didac/moanings03.ogg"
    
    d "<{size=18}Ahh-ahh...{/size}>" # Moaning angry/excited *Gemidos femeninos* 
    
    p "<{size=18}Es irónico que te guste tanto algo para lo que no necesitabas convertirte en chica...{/size}>"

    p "<{size=18}¿No crees?{/size}>"

    play sound "audio/characters/didac/moanings02.ogg"
    
    d "<{size=18}Ahh..."  # Moan angry/excited *Gemidos femeninos* 

    extend " Hmmm...{/size}>"

    d "<{size=18}Serás...{/size}"

    extend "{size=18} hijo de...{/size}>"
    
    call aftermorning04_FastMastDick
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_beforecumming
    with fade

    play sound "audio/characters/didac/moanings03.ogg"
    
    d "Ahh-Ahh... Ahhhh..." # Moanings with Heavy breathing angry/excited being anally fingered *Respiración agitada* 
    
    n "Su agujero anal está cada vez más dilatado y su resistencia disminuye considerablemente."

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5
    
    scene aftermorning04_bg fittingroomin02
    show aftermorning04_bg_fittingroom_mast_dass 005:
        aftermorning04_bg_fittingroom_mast_dass_005_justbeforecumming
    show closetocum_other
    with fade
    
    n "Aun así no reduces lo más mínimo el ritmo,"
       
    n "en su lugar, aumentas las embestidas que realizas con tu dedo índice."

    play sound "audio/characters/didac/moanings02.ogg"
    
    d "<{size=18}Ahh...{/size}"

    extend "{size=18} Te crees muy...{/size}"

    extend "{size=18} machito...{/size}>"

    d "<{size=18}aaah...{/size}" # moan

    extend "{size=18} pero...{/size}"

    extend "{size=18} verás cómo te vas...{/size}>"

    d "<{size=18}ahh...{/size}"

    extend "{size=18} correr tú...{/size}>"
    
    show cumming_other
    with vpunch

    play sound "audio/characters/didac/orgasm03.ogg"
    
    d "¡AAAH-AAAHHH... AAAHAHHH!" # *Having an ORGASM, moans* *Gemido agudo femenino*

    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/characters/didac/breath_heavy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play sound "audio/sfx/fall08.ogg"
    
    scene aftermorning04_bg fittingroomin_ground: #background
        aftermorning04_bg_fittingroom_DKneels_anim_pose

    show aftermorning04_bg_fittingroom_DKneels_anim: #Didac Panting
        aftermorning04_bg_fittingroom_DKneels_anim_pose
    with fade
    #Imagen de rodillas (?)
    
    window hide dissolve
    pause
    
    d "<{size=18}Ahh... Ahh... Ahhhh...{/size}>" # heavy breathing after being defeated for having first an orgasm *Respiración agitada* 
    
    p "<{size=18}No sabía que te gustara tanto que te metieran el dedo ahí,{/size}>"

    p "<{size=18}¿ibas a decir que me iba a correr yo primero?{/size}>"
    
    p "<{size=18}Tampoco hubiera sido raro,"

    extend " normalmente un tío se corre cuando le masajean esta parte...{/size}"

    p "{size=18}pero tú...{/size}>"
    
    n "Su cuerpo empieza a tambalearse mostrando voluntad de ponerse en pie."

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 08:
        dfexpressions_atleft_closex3
    show didacf_pupils front08:
        dfexpressions_atleft_closex3
    show didacf_eyebrows sadx01:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx001:
        dfexpressions_atleft_closex3
    with fade

    d "..."
    
    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx002
    with dissolve

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}Putah-"

    extend "Ahh...{/size}>"

    d "<{size=18}Ca-{/size}"

    extend "{size=18}Aahh...{/size}"

    extend "{size=18} Cállate...{/size}>"
    
    jump aftermorning04_Masturbation_SadEnding02
    
label aftermorning04_FastMast_OnlyAnal_Angry:
    
    #n "Aquí es cuando decides no tocar el coño y meterlo más rápido analmente, consiguiendo que se enfade."

    play sound "audio/characters/didac/scream_au09.ogg"
    
    d "<{size=18}¡Aauh...!{/size}>" # Painful muffled scream *Gemido de dolor* 
    
    n "Después de estar acariciando con suavidad su cavidad anal con tu dedo índice,"
    
    n "Aceleras el ritmo con el que movías la palma de tu mano a casi el doble de velocidad,"
    
    n "en un agujero que desde un inicio ya no se ofrecía demasiado dilatado ni lubricado."

    play sound "audio/characters/didac/scream_au01.ogg"
    
    d "<{size=18}¡[protname]...!{/size}>" # muffled painful groin *Gemido de dolor* 
    
    n "Haces como que no le escuchas y sigues penetrando analmente a tu amigo de la infancia."

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 0.5 fadeout 0.5

    play sound "audio/characters/didac/scream_au11.ogg"

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 04:
        dfexpressions_atleft_closex3
    show didacf_eyes 00:
        dfexpressions_atleft_closex3
    show didacf_pupils front00:
        dfexpressions_atleft_closex3
    show didacf_eyebrows angryx03:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Talkingx08:
        dfexpressions_atleft_closex3
    with vpunch
    
    d "<{size=18}¡¿Quieres parar de una puta vez?!"

    extend " ¡imbécil!{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with hpunch

    play sound "audio/sfx/hit02.ogg"
    
    n "Un fuerte agarrón en tu muñeca aparta tu dedo de donde estaba."

    play music "audio/music/alcaknight/bury_it.ogg" fadein 3.0 fadeout 3.0

    show didacf_blush 01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "<{size=18}¡¿Se puede saber qué coño estabas haciendo?!{/size}>"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "<{size=18}¿Y tú?"

    extend " ¿Te recuerdo dónde tenías puesta tu mano?{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "<{size=18}¡Me estabas metiendo el dedo en el culo!{/size}>"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "<{size=18}¡¿Qué clase de maricón eres?!{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "<{size=18}¿Y qué clase de maricón eres tú?{/size}>"

    p "<{size=18}Que no te has quejado hasta que te he metido caña...{/size}>"

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "<{size=18}Hace rato que te estaba metiendo el dedo ahí,{/size}>"

    p "<{size=18}y no me has dicho nada hasta ahora...{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve
    
    d "..."

    show didacf_blush 03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx09
    with dissolve
    
    p "<{size=18}Quizás debería habértelo metido también por el otro lado...{/size}>"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "<{size=18}¡Pero te estás oyendo?!{/size}>"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "<{size=18}¡¿Qué lado?!"

    extend " ¡¿El lado en el que debería tener la polla que no tengo?!{/size}>"

    show didacf_blush 02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx003
    with dissolve

    play sound "audio/characters/didac/breath_sigh01.ogg"

    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    d "<{size=18}AAaaaaahh...{/size}>" # prolonged sigh *Suspiro femenino prolongado* 

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "<{size=18}Esto se nos ha ido de las manos..."

    extend " [protname],{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx04
    with dissolve
       
    d "<{size=18}por favor,"

    extend " vete a casa.{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "<{size=18}¡Pero si has sido tú quien me ha estado provocando todo este tiempo!{/size}>"

    show didacf_blush 04
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx01
    with dissolve
    
    d "<{size=18}Ya lo sé..."

    extend " Lo sé...{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "<{size=18}Lo siento..."

    extend " no sé qué me está pasando...{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "<{size=18}Pero, por favor,"

    extend " entiéndelo.{/size}>"

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx01
    with dissolve
    
    jump aftermorning04_StoporNot #Rape
    

##########################################################

label aftermorning04_FastMastDick: #Masturba tu miembro más fuerte y más rápido, paso 2.
    
    #image Didac Masturbating you Hard and Fast. 2ndpass
    
    scene aftermorning04_bg fittingroomin
    show aftermorning04_bg_fittingroom_mast 005:
        subpixel True
        #zoom 0.3 xpos 0.3 #For Experiments.
        xpos -0.1 ypos -0.5 zoom 0.5 #Far Shot
        easein_quad 2.0 xpos -0.37 ypos -1.05 zoom 0.8 
         
    with dissolve
    
    n "Tienes la sensación de que su mano se está preparando para acelerar su ritmo..."
    
    $ aftermorning04_bg_fittingroom_mast_Fast = True #With that, it will go faster masturbating if it´s true. :)
    show aftermorning04_bg_fittingroom_mast 006:
        subpixel True
        #truecenter
        #xpos 0.2 ypos 0.5 zoom 0.4
        xpos -0.38 ypos -1.08 zoom 0.81 #Close Shot
        block:
            easein_quad 0.2250 xpos -0.37 ypos -1.05 zoom 0.8 #Close Shot
            easeout_quad 0.2250 xpos -0.38 ypos -1.08 zoom 0.81 #Close Shot
            repeat
    with dissolve
    
    n "Sientes claramente sus dedos ahogando tu polla al ritmo de sus suspiros ahogados."
    
    n "El glande de tu polla está cada vez más hinchado y rojizo."
    
    n "Las palpitaciones son cada vez más evidentes, al mismo tiempo que percibes el hormigueo cada vez más acentuado."
    
    n "Sientes tus testículos contrayéndose a cada golpe que te da con su muñeca."
     
    return

    
    #jump aftermorning04_Masturbation_SadEnding02
    
label aftermorning04_Masturbation_SadEnding:

    stop music fadeout 5.0
    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0

    scene aftermorning04_bg_fittingroomin
    show didacfbodybelow naked:
        dfbody_atleft_closex3
    show didacfbodybelow_naked_wet 02:
        dfbody_atleft_closex3
    show didacfbodytop brablack:
        dfbody_atleft_closex3
    show didacfbodytop_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandl hip_naked:
        dfbody_atleft_closex3
    show didacfhandl_hip_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandr empty:
        dfbody_atleft_closex3
    show didacfhandr_leg_naked_drops 00:
        dfbody_atleft_closex3
    show didacfhandx2 empty: #both hands
        dfbody_atleft_closex3

    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 00:
        dfexpressions_atleft_closex3
    show didacf_pupils front00:
        dfexpressions_atleft_closex3
    show didacf_eyebrows surprisex02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Silentx04:
        dfexpressions_atleft_closex3

    with vpunch
    
    p "<{size=18}¡Dídac!{/size}>"

    show didacf_blush 04
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "<{size=18}¿Qué...?{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    p "<{size=18}No podemos seguir haciendo esto...{/size}>"

    show didacf_blush 04
    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx001
    with dissolve
    
    d "<{size=18}¿Por...?"

    extend " ¿Por qué?{/size}>"

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx05
    with dissolve
    
    pt "¡¿Cómo que por qué?!"
    
    pt "¡Porque eres mi puto amigo!"

    extend " ¡Mi compañero de piso!"
    
    pt "¡Y porque me estás poniendo como una puta moto!"
    
    p "<{size=18}Nos van a oír...{/size}>"
    
    jump aftermorning04_Masturbation_SadEnding02
    
label aftermorning04_Masturbation_SadEnding02:

    scene aftermorning04_bg_fittingroomin

    if aftermorning04_Mast001_PussyFastAfter_Happy == True or aftermorning04_Mast001_AnalFastAfter_Happy == True or aftermorning04_Mast001_PussyFast_Happy == True or aftermorning04_Mast001_AnalFast_Happy == True:

        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 02:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3

    else:

        show didacfbodybelow naked:
            dfbody_atleft_closex3
        show didacfbodybelow_naked_wet 00:
            dfbody_atleft_closex3
        show didacfbodytop brablack:
            dfbody_atleft_closex3
        show didacfbodytop_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandl hip_naked:
            dfbody_atleft_closex3
        show didacfhandl_hip_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandr empty:
            dfbody_atleft_closex3
        show didacfhandr_leg_naked_drops 00:
            dfbody_atleft_closex3
        show didacfhandx2 empty: #both hands
            dfbody_atleft_closex3


    show didacf_blush 03:
        dfexpressions_atleft_closex3
    show didacf_eyes 00:
        dfexpressions_atleft_closex3
    show didacf_pupils right00:
        dfexpressions_atleft_closex3
    show didacf_eyebrows surprisex02:
        dfexpressions_atleft_closex3
    show didacfbodytop_hair:
        dfbody_atleft_closex3
    show didacf_mouth sad_Silentx04:
        dfexpressions_atleft_closex3
    with vpunch

    stop music fadeout 0.5
    play sound "audio/sfx/meme_surprise02.ogg"

    de "¡Oiga!"

    extend " ¡¿Está usted bien?!"

    show didacf_blush 03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx05
    with dissolve

    de "He oído ruidos extraños..."

    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx01
    with dissolve

    play music "audio/music/alcaknight/memories_of_the_east.ogg" fadein 3.0 fadeout 3.0

    p "..."

    show didacf_blush 02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    show didacf_mouth happybiting_Silentx03
    with dissolve
    
    pt "Dídac,"

    extend " no..."

    show didacf_blush 02
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows angryx02
    show didacf_mouth happybiting_Silentx05
    with dissolve
    
    p "<{size=17}¡Shhh...!"

    extend " ¡¿Que no ves que nos va a oír?!{/size}>"

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx01
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    d "<{size=17}Lo sé,"

    extend " lo sé...{/size}>"

    d "<{size=17}Tranquilo...{/size}>"

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "Hmm..." # Trying to keep the moans muffled, while talking to the clerk.

    d "Aah..."

    extend" Sí..."

    d "¡Estoy bien!"

    d "¡Sí!"

    extend " ¡Gracias!"

    show didacf_blush 03
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows angryx01
    show didacf_mouth happybiting_Silentx05
    with dissolve

    de "Vale..."

    de "Llámame si"

    extend " \"necesitáis\""

    extend " algo..."

    stop music fadeout 0.5
    play sound "audio/sfx/meme_surprise02.ogg"

    show didacf_blush 02
    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx04
    with dissolve

    n "Ese detalle de hablar en plural no se te había escapado,"

    n "y por lo visto a Dídac tampoco."

    show didacf_blush 02
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Dídac..."

    p "será mejor que me vaya largando de aquí,"

    extend " creo que nos han pillado."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0

    d "Espera,"

    extend " ¿a dónde vas?"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "Bueno..."

    p "teniendo en cuenta que nos han pillado,"

    p "y que como siga teniéndote cerca voy a reventar aún más..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx05
    with dissolve
       
    p "creo que lo más sensato es que te espere en casa."

    p "Tampoco vas a comprar tanto como para necesitarme de burro de carga,"

    extend " ¿no?"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "No..."

    extend " supongo que no..."

    d "En realidad solo quería tu compañía."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx01
    with dissolve

    d "Sabía que si preguntaba un poco por aquí alguien me ayudaría a elegir la ropa adecuada."

    show didacf_blush 02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows normal
    show didacf_mouth happy_Talkingx02
    with dissolve

    d "Pero te agradezco el detalle de haber venido,"

    d " y..."

    extend " bueno,"

    d "de haberme complacido así también..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx02
    with dissolve

    pt "Ya no sé en qué diablos piensa este tío..."
    
    window hide dissolve
    pause
    if morning03_Meritxell_Phonenumber_Accepted == True:
    
        jump morning04_Meritxell_Calling
    
    else:
    
        jump afternoon04_AloneatHome
    
    
    
    
