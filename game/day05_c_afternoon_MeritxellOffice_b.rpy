
default FuckM_Start_Cond = False # Si te has follado a Meritxell.
default TxellPregnant = False

default FuckH_Start_Cond = False

default FuckH_conversation_dungeon_cond = False
default FuckH_conversation_analvirgin_cond = False
default FuckH_conversation_sexpreference_cond = False

default FuckH_action_butt_enema_Cond = False

# Action BodyPart

default FuckH_act_body_ = "back"

# Action Objects # I will have to do it for every single action anyway...

#default FuckH_action_obj_throatSpray = 0
#default FuckH_action_obj_popper = 0

# Action Focus

default FuckH_act_focus_ = "nothing" # default

default FuckH_orn_focus_ = "noone" # default

# BDSM ornament:

default FuckH_orn_mask__ = ""
default FuckH_orn_eyes__ = ""
default FuckH_orn_face__ = ""
default FuckH_orn_mouth__ = ""
default FuckH_orn_neck__ = ""
default FuckH_orn_leash__ = ""
default FuckH_orn_head__ = ""

default FuckH_orn_boobs__ = "" # Pueden ser pintadas
default FuckH_orn_nipples__ = ""
default FuckH_orn_butt__ = "" # Pueden ser pintadas
default FuckH_orn_asshole__ = ""

default FuckH_orn_pussy__ = ""
default FuckH_orn_clitoris__ = ""

# BDSM pose:

default FuckH_pose_ = "onFeet"


################################################################################
################################################################################

################################################################################
################################################################################

label FuckH_underwear_No:

    play sound "audio/sfx/door_close01.ogg"

    scene bg 05afternoon_dungeon_wall_01:
        truecenter
        zoom 0.55

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_body_down panties:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_body_up crossed_bra:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_right_zoom_0_25_pos

    show hiromi_gen_exp_blush 02:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_mouth sad_Silentx01:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_eyes 01:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_piris front01:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_eyebrows normal:
        hiromi_gen_exp_right_zoom_0_25_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_right_zoom_0_25_pos
    with Dissolve(1.0)

    n "Decides entrar y cerrar la puerta."

    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    pm "Supongo que por ahora es suficiente."

########################################################
########################################################

    #$pLockerC.ch_pts_C("hi_dom",1)
    #$pLockerC.ch_pts_C("hi_ple",2)
    #$pLockerC.ch_pts_C("hi_hap",-3)
    #$pLockerC.ch_pts_C("hi_painass",4)
    #$pLockerC.ch_pts_C("hi_love",5)
    #$pLockerC.ch_pts_C("hi_org",6)
     # NOT FINISHED, TEST
    
    #show screen Points()
    #hide screen PointsDungeon
    #with dissolve

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    scene day05
    with fade

    aj "La parte que viene a continuación con Hiromi aún está en proceso."

    menu FuckH_WIP_question:

        aj "Te recomiendo que no la juegues aún."

        "<Tengo curiosidad de ver qué hay>":
            call p_Help

            $ FuckH_Start_Cond = True

            jump FuckH_Start

        "<Mejor me espero>":
            call p_Help

            aj "La historia continúa cuando te diriges a la biblioteca que te ha mencionado Txell."

            if PlatinumHelp == True:
                show screen Points()
                hide screen PointsDungeon
                with dissolve

            jump afternoon05_Library

label FuckH_End:

    jump WIP

    $ FuckH_SUCCESS = True # NOT FINISHED, this is temporal.

    if PlatinumHelp == True:
        show screen Points()
        hide screen PointsDungeon
        with dissolve

    jump afternoon05_Library

#ono "Pum"

#p "Desde luego,"

#p "el nombre de biblioteca le encaja bastante bien a esta habitación..."

#n "En la enorme sala en la que te encuentras,"


########################################################
########################################################

########################################################
########################################################

label WIP_dun:

    #aj "trabajo en proceso"

    #$ renpy.rollback(force=True, checkpoints=2) # Go back 2 choices.

    return

label FuckH_ChangePos_Start:

    $ FuckH_act_focus_ = "nothing" #mirando

    return

label FuckH_Image_Start:

    #########################################################

    if config.version < "00.99.99": # for FUTURE
        call endupdatescript
    
    #######################################################

    #$ debug ("Bitch")

    if FuckH_pose_ == "onFeet":

        # scene 05aft_dun_h_pose_onFeet
        # with fade

        #$ debug ("Hiromi está de pie.")

        if FuckH_act_body_ == "back":

            $ debug("De pie. Te centras en su espalda.")

            pass

            $ debug ("De pie. Te centras en su espalda.")

        elif FuckH_act_body_ == "mouth":

            pass

            $ debug ("De pie. Te centras en su boca.")

        elif FuckH_act_body_ == "boobs":

            pass

            $ debug ("De pie. Te centras en sus pechos.")

        elif FuckH_act_body_ == "butt":

            pass

            $ debug ("De pie. Te centras en su trasero.")

        elif FuckH_act_body_ == "dick":

            pass

            $ debug ("De pie. Te centras en su polla.")

        else:

            pass

            $ debug ("Wtfuck Dude...?")


    elif FuckH_pose_ == "andrewCross":

        pass

        # scene 05aft_dun_h_pose_andrewCross
        # with fade

        $ debug ("Hiromi está en la cruz de San Andrés.")

    elif FuckH_pose_ == "bed":

        pass

        $ debug ("Hiromi está en la cama.")

    elif FuckH_pose_ == "gynoChair":

        pass

        # scene 05aft_dun_h_pose_gynoChair
        # with fade

        $ debug ("Hiromi está en Silla de Ginecólogo.")

    elif FuckH_pose_ == "impaler":

        pass

        # scene 05aft_dun_h_pose_impaler
        # with fade

        $ debug ("Hiromi está en el empalador.")

    elif FuckH_pose_ == "mantisChair":

        pass

        # scene 05aft_dun_h_pose_mantisChair
        # with fade

        $ debug ("Hiromi está en silla Mantis.")

    elif FuckH_pose_ == "paddedWall":

        pass

        # scene 05aft_dun_h_pose_paddedWall
        # with fade

        $ debug ("Hiromi está en la pared acolchada.")

    elif FuckH_pose_ == "prisonBin":

        pass

        # scene 05aft_dun_h_pose_prisonBin
        # with fade

        $ debug ("Hiromi está en la celda.")

    elif FuckH_pose_ == "prisonCage":

        pass

        # scene 05aft_dun_h_pose_prisonCage
        # with fade

        $ debug ("Hiromi está en la celda del taburete de cuclillas.")

    elif FuckH_pose_ == "scorpionBench":

        pass

        # scene 05aft_dun_h_pose_scorpionBench
        # with fade

        $ debug ("Hiromi está en el banco Escropión.")

    #elif FuckH_pose_ == "throne":
        #$ debug ("Hiromi está en el trono, ¿De verdad?")

    # bondage_normal

    elif FuckH_pose_ == "ballStretcher":

        pass

        # scene 05aft_dun_h_pose_ballStretcher
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "ballTie":

        pass

        # scene 05aft_dun_h_pose_ballTie
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "bentOver":

        pass

        # scene 05aft_dun_h_pose_bentOver
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "ebi":

        pass

        # scene 05aft_dun_h_pose_ebi
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "hogTie":

        pass

        # scene 05aft_dun_h_pose_hogTie
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "inversePrayer":

        pass

        # scene 05aft_dun_h_pose_inversePrayer
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "pitDoom":

        pass

        # scene 05aft_dun_h_pose_pitDoom
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    elif FuckH_pose_ == "spreader":

        pass

        # scene 05aft_dun_h_pose_spreader
        # with fade

        $ debug ("Hiromi está en posición BONDAGE: Hog Tie.")

    # bondage_suspension

    elif FuckH_pose_ == "hishiFit":

        pass

        # scene 05aft_dun_h_pose_hishiFit
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    elif FuckH_pose_ == "invertLeg":

        pass

        # scene 05aft_dun_h_pose_invertLeg
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    elif FuckH_pose_ == "invertSaltire":

        pass

        # scene 05aft_dun_h_pose_invertSaltire
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    elif FuckH_pose_ == "peterPan":

        pass

        # scene 05aft_dun_h_pose_peterPan
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    elif FuckH_pose_ == "ropeHammock":

        pass

        # scene 05aft_dun_h_pose_ropeHammock
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    elif FuckH_pose_ == "yokoTzury":

        pass

        # scene 05aft_dun_h_pose_yokoTzury
        # with fade

        $ debug ("Hiromi está en posición BONDAGE SUSPENSION: Hishi Fit.")

    else:

        pass

        $ debug ("What did you choose?")



    $ debug ("Está en [FuckH_pose_], haciendo [FuckH_act_focus_]")

    $ debug ("mask:[FuckH_orn_mask__], eyes:[FuckH_orn_eyes__], face:[FuckH_orn_face__], mouth:[FuckH_orn_mouth__], cuello:[FuckH_orn_neck__], cadena:[FuckH_orn_leash__], cabeza:[FuckH_orn_head__]")
    $ debug ("boobs:[FuckH_orn_boobs__], nipples:[FuckH_orn_nipples__], butt:[FuckH_orn_butt__], asshole:[FuckH_orn_asshole__].")

    #scene expression ("05aft_dun_h_pose_[FuckH_pose_]")
    call expression ("aft_dun_h_pose_" + FuckH_pose_)
    #scene 05aft_dun_h_pose_{}.format(FuckH_pose_)
    with fade

    return


###########################################################################
###########################################################################

###########################################################################
###########################################################################

###########################################################################
###########################################################################

style FuckH_Start_style:

    background Frame("gui/bar/left.png",28,9)
    hover_background Frame("gui/bar/right.png",28,9)

screen dun_choice_screen(items):
    zorder 100
    style_prefix "dun_choice"
    #style "dun_choice_style"

    vbox:
        for i in items:
            if i.chosen:
                textbutton i.caption action i.action text_idle_color "#999" text_hover_color "#ddd"
            else:
                textbutton i.caption action i.action

style dun_choice_vbox is vbox
style dun_choice_button is button
style dun_choice_button_text is button_text

style dun_choice_vbox:
    #xalign 0.0
    ypos 80
    spacing gui.dun_choice_spacing
    

style dun_choice_button is default:
    properties gui.button_properties("dun_choice_button")
    #xalign 0.0
    xsize 300

    #idle_background "gui/button/dun_choice_idle_background.png"
    #hover_background "gui/button/dun_choice_hover_background.png"

style dun_choice_button_text is default:
    properties gui.button_text_properties("dun_choice_button")
    #text_align 0.0
    #size 10
    #xpos -0.5
    #area (10, 10, 10, 10)

    

###########################################################################
###########################################################################

###########################################################################
###########################################################################

###########################################################################
###########################################################################

label FuckH_Start:

###########################################################################
###########################################################################

    menu FuckH_Start_question (screen="dun_choice_screen"):

        #style "FuckH_Start_style"

        pt "¿Y ahora qué?"

        "{image=gui/icons/dungeon/dun_ple_pos_mc.png}<Tomar una acción>":
            call p_Help

            jump FuckH_action

        "<Cambiar...>":
            call p_Help

            jump FuckH_decision

        "<Hacerle algunas preguntas>":

            call p_Help

            jump FuckH_conversation

        "<Dar por terminada la terapia>":

            call p_Help

            jump FuckH_endTherapy

            jump FuckH_endTherapy

########################################################
########################################################

########################################################
########################################################

########################################################
########################################################

########################################################
########################################################

label FuckH_action:

    menu FuckH_action_question (screen="dun_choice_screen"):
        
        pt "¿Dónde?"

        "<Espalda>":

            call p_Help

            $ FuckH_act_body_ = "back"

            jump FuckH_action_skin

        "<Boca>":

            call p_Help

            $ FuckH_act_body_ = "mouth"

            jump FuckH_action_mouth

        "<Pechos>":

            call p_Help

            $ FuckH_act_body_ = "boobs"

            jump FuckH_action_boobs

        "<Trasero>":

            call p_Help

            $ FuckH_act_body_ = "butt"

            jump FuckH_action_butt

        "<Polla>":

            call p_Help

            $ FuckH_act_body_ = "dick"

            jump FuckH_action_dick

        "-Volver atrás-":

            call p_Help

            jump FuckH_Start

########################################################
########################################################

########################################################
########################################################

# BACK-Skin / DICK (?) / PUSSY (?)

label FuckH_action_skin:

    menu FuckH_action_skin_question (screen="dun_choice_screen"):

        pt "¿Y ahora qué hago con su [FuckH_act_body_]?"

        "<Electrodos>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_sad_electro"

            call FuckH_Image_Start

            jump FuckH_action_skin

        "<Velas>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_sad_candles"

            call FuckH_Image_Start

            jump FuckH_action_skin

        "<Rueda de Wartenberg>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_sad_wartenberg"

            call FuckH_Image_Start

            jump FuckH_action_skin

        "<Disciplina>":

            call p_Help

            jump FuckH_action_skin_discipline

        "<Eje largo con siete pequeños pinchos (sangriento)>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_sad_sevenStar"

            call FuckH_Image_Start

            jump FuckH_action_skin

        "-Volver atrás-":

            call p_Help

            jump FuckH_action


########################################################

# SKIN DISCIPLINE

label FuckH_action_skin_discipline:

    menu FuckH_action_skin_discipline_question (screen="dun_choice_screen"):

        pt "¿Cómo debería azotarla?"

        "<Mano desnuda>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dis_hand"

            call FuckH_Image_Start

            jump FuckH_action_skin_discipline

        "<Látigo de tiras>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dis_flogger"

            call FuckH_Image_Start

            jump FuckH_action_skin_discipline

        "<Caña Wangi>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dis_wangi"

            call FuckH_Image_Start

            jump FuckH_action_skin_discipline

        "<Correa de cuero tachonado>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dis_strapStud"

            call FuckH_Image_Start

            jump FuckH_action_skin_discipline

        "<Pala de madera>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dis_paddleWood"

            call FuckH_Image_Start

            jump FuckH_action_skin_discipline

        "-Volver atrás-":

            call p_Help

            jump FuckH_action_skin

########################################################
########################################################

########################################################
########################################################

# SKIN PAINT

label FuckH_paint_label:

    menu FuckH_paint_question (screen="dun_choice_screen"):

        pt "¿Qué debería pintarle?"

        "<ESTÚPIDA>":

            call p_Help

            call WIP_dun

            #$ FuckH_act_focus_ = FuckH_act_body_ + "_dis_hand"

            #call FuckH_Image_Start

            jump FuckH_paint_label

        "<ESCLAVA>":

            call p_Help

            call WIP_dun

            #$ FuckH_act_focus_ = FuckH_act_body_ + "_dis_hand"

            #call FuckH_Image_Start

            jump FuckH_paint_label

        "-Volver atrás-":

            call p_Help

            jump expression "FuckH_orn_" + FuckH_orn_focus_ + "_label"


########################################################
########################################################

########################################################
########################################################

# action MOUTH

label FuckH_action_mouth:

    if FuckH_orn_mouth__ == "":

        menu FuckH_action_mouth_question (screen="dun_choice_screen"):

            pt "¿?"

            "<Spray para relajar la garganta>":

                call p_Help

                call WIP_dun

                #$ FuckH_action_obj_throatSpray += 1

                $ FuckH_act_focus_ = FuckH_act_body_ + "_throatSpray"

                call FuckH_Image_Start

                jump FuckH_action_mouth

            "<Besarla en los labios>":

                call p_Help

                call WIP_dun

                $ FuckH_act_focus_ = FuckH_act_body_ + "_kissLips"

                call FuckH_Image_Start

                jump FuckH_action_mouth

            "<Besarla con lengua>":

                call p_Help

                call WIP_dun

                $ FuckH_act_focus_ = FuckH_act_body_ + "_kissTongue"

                call FuckH_Image_Start

                jump FuckH_action_mouth

            "<Introducirle un juguete en la boca>":

                call p_Help

                jump FuckH_action_mouth_toy

            "<Meterle la polla en la boca>":

                call p_Help

                call WIP_dun

                $ FuckH_act_focus_ = FuckH_act_body_ + "_blowjob"

                call FuckH_Image_Start

                jump FuckH_action_mouth

            "-Volver atrás-":

                call p_Help

                jump FuckH_action
    else:

        pt "Antes debería quitarle lo que tiene en la boca."

########################################################
########################################################

# action MOUTH-TOY

label FuckH_action_mouth_toy:

    menu FuckH_action_mouth_toy_question (screen="dun_choice_screen"):

        pt "¿Qué juguete le podría meter?"

        "<Dildo>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_dildo"

            call FuckH_Image_Start

            jump FuckH_action_mouth_toy

        "<Vibrador a distancia>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_vibrator"

            call FuckH_Image_Start

            jump FuckH_action_mouth_toy

        "<Varita Hitachi>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_hitachi"

            call FuckH_Image_Start

            jump FuckH_action_mouth_toy

        "-Volver atrás-":

            call p_Help

            jump FuckH_action_mouth

########################################################
########################################################

########################################################
########################################################

# action BOOBS

label FuckH_action_boobs:

    menu FuckH_action_boobs_question (screen="dun_choice_screen"):

        pt "¿?"

        "<Masajearle los pechos>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_massage"

            call FuckH_Image_Start

            jump FuckH_action_boobs

        "<Pellizcarle los pezones>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_nipPinch"

            call FuckH_Image_Start

            jump FuckH_action_boobs

        "<Morderle los pezones>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_nipBite"

            call FuckH_Image_Start

            jump FuckH_action_boobs

        "<Hacerte una cubana con sus pechos>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_boobjob"

            call FuckH_Image_Start

            jump FuckH_action_boobs

        "<Sadismo>":

            call p_Help

            jump FuckH_action_skin

        "-Volver atrás-":

            call p_Help

            jump FuckH_action

########################################################
########################################################

########################################################
########################################################

# action BUTT

label FuckH_action_butt:

    menu FuckH_action_butt_question (screen="dun_choice_screen"):

        pt "¿Qué le hago a su trasero?"

        "<Métodos de dilatación>":

            call p_Help

            jump FuckH_action_butt_prep

        "<Introducirle un juguete>":

            call p_Help

            jump FuckH_action_butt_toy

        "<Follarle el culo>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_fuck" # How deep, how rude?

            call FuckH_Image_Start

            jump FuckH_action_butt

        "<Sadismo>":

            call p_Help

            jump FuckH_action_skin

        "-Volver atrás-":

            call p_Help

            jump FuckH_action

########################################################
########################################################

label FuckH_action_butt_prep:

    menu FuckH_action_butt_prep_question (screen="dun_choice_screen"):

        pt "¿Para ir abriendo camino...?"

        "<Enema para limpiar recto>" if FuckH_action_butt_enema_Cond == False:

            call p_Help

            call WIP_dun

            $ FuckH_action_butt_enema_Cond = True

            # If she has the mouth free:

            hi "¡¿Te crees que no he venido ya preparada?!"

            hi "Te recuerdo que venía a ver a Txell."

            p "Es mejor prevenir que..."

            hi "..."

            hi "Supongo que tienes razón."

            jump FuckH_action_butt_prep

        "<Beso negro>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_kissBlack"

            call FuckH_Image_Start

            jump FuckH_action_butt_prep

        "<Lubricante>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_lubricant"

            #$ FuckH_action_obj_lubricant = 0

            call FuckH_Image_Start

            jump FuckH_action_butt_prep

        "<\"Popper\" (Droga)>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_popper"

            #$ FuckH_action_obj_popper += 1

            call FuckH_Image_Start

            jump FuckH_action_butt_prep

        "-Volver atrás-":

            call p_Help

            jump FuckH_action_butt

########################################################
########################################################

# action BUTT-TOY

label FuckH_action_butt_toy:

    menu FuckH_action_butt_toy_question (screen="dun_choice_screen"):

        pt "¿Qué juguete le podría meter?"

        #"<Tapón anal>": # It´s not an action, is an ornement, because it remain there.

        "<Dildo>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_toy_dildo"

            call FuckH_Image_Start

            jump FuckH_action_butt_toy

        "<Vibrador>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_toy_vibrator"

            call FuckH_Image_Start

            jump FuckH_action_butt_toy

        "<Varita Hitachi>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_toy_hitachi"

            call FuckH_Image_Start

            jump FuckH_action_butt_toy

        "-Volver atrás-":

            call p_Help

            jump FuckH_action_butt

########################################################
########################################################

########################################################
########################################################

# action DICK

label FuckH_action_dick:

    menu FuckH_action_dick_question (screen="dun_choice_screen"):

        pt "¿Qué se supone que tengo que hacer con esto?"

        "<Lamerle la polla>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_lick"

            call FuckH_Image_Start   

            jump FuckH_action_dick

        "<Chuparle la polla>":

            call p_Help

            call WIP_dun

            $ FuckH_act_focus_ = FuckH_act_body_ + "_blowjob"

            call FuckH_Image_Start

            jump FuckH_action_dick

        "<Sadismo>":

            call p_Help

            jump FuckH_action_skin

        "-Volver atrás-":

            call p_Help

            jump FuckH_action

########################################################
########################################################

########################################################
########################################################

# action PUSSY # for Txell in future (?)

label FuckH_action_pussy:

    menu FuckH_action_pussy_question (screen="dun_choice_screen"):

        pt "¿?"

        "<>":

            call p_Help

            jump FuckH_action_pussy

        "-Volver atrás-":

            call p_Help

            jump FuckH_action

########################################################
########################################################

########################################################
########################################################

########################################################
######################################################## # DECISION

label FuckH_decision:

    menu FuckH_decision_question (screen="dun_choice_screen"):
        
        pt "¿Qué podría hacer ahora?"

        "<Ornamento>":

            call p_Help

            jump FuckH_orn_label

        #"<Bondage>":

            #call p_Help

            #jump FuckH_decision_bondage

        "<Lugar/Posición>":

            call p_Help

            jump FuckH_decision_pose

        "-Volver atrás-":

            call p_Help

            jump FuckH_Start

########################################################

########################################################
######################################################## ## FURNITURE - GENERAL01

label FuckH_decision_pose:

    menu FuckH_decision_pose_question (screen="dun_choice_screen"):

        "<De pie>":

            call p_Help

            jump FuckH_decision_pose_onFeet

        "<Bondage +>":

            call p_Help

            jump FuckH_decision_pose_bondage

        "<Bondage de suspensión +>":

            call p_Help

            jump FuckH_decision_pose_bondage_suspension

        "<Silla ginecológica>":

            call p_Help

            jump FuckH_decision_pose_gynoChair

        "<Silla mantis>":

            call p_Help

            jump FuckH_decision_pose_mantisChair

        "<Banco de Escorpión>":

            call p_Help

            jump FuckH_decision_pose_scorpionBench

        "-Otros-":

            call p_Help

            jump FuckH_decision_pose_02

        "-Volver atrás-":

            call p_Help

            jump FuckH_decision

########################################################

######################################################## ## FURNITURE - GENERAL02

label FuckH_decision_pose_02:

    menu FuckH_decision_pose_02_question (screen="dun_choice_screen"):

        "<Cruz de San Andrés>": # Andrew Cross

            call p_Help

            jump FuckH_decision_pose_andrewCross

        "<Pared acolchada>": # Padded Wall

            call p_Help

            jump FuckH_decision_pose_paddedWall

        "<Empalador>":

            call p_Help

            jump FuckH_decision_pose_impaler

        "<Prisión +>":

            call p_Help

            jump FuckH_decision_pose_prison

        "<Cama>":

            call p_Help

            jump FuckH_decision_pose_bed

        "-Atrás-":

            call p_Help

            jump FuckH_decision_pose

########################################################

########################################################
######################################################## ## FURNITURE ORNAMENT - GENERAL

#label FuckH_orn_label:
label FuckH_orn_label:

    menu FuckH_orn_question (screen="dun_choice_screen"):
        
        pt "¿Qué ornamentación podría ponerle?"

        "<Liberarla de todo>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_mask__ = ""
            $ FuckH_orn_eyes__ = ""
            $ FuckH_orn_mouth__ = ""
            $ FuckH_orn_neck__ = ""
            $ FuckH_orn_leash__ = ""
            $ FuckH_orn_head__ = ""

            $ FuckH_orn_boobs__ = "" # Pueden ser pintadas
            $ FuckH_orn_nipples__ = ""
            $ FuckH_orn_butt__ = "" # Pueden ser pintadas
            $ FuckH_orn_asshole__ = ""

            $ FuckH_orn_focus_ = ""

            jump FuckH_orn_label

        "<Ojos/Máscara>":

            call p_Help

            $ FuckH_orn_focus_ = "eyes"

            jump FuckH_orn_eyes_label

        "<Boca/Gag>":

            call p_Help

            $ FuckH_orn_focus_ = "mouth"

            jump FuckH_orn_mouth_label

        "<Cuello>":

            call p_Help

            $ FuckH_orn_focus_ = "neck"

            jump FuckH_orn_neck_label

        "-Otros-":

            call p_Help

            jump FuckH_orn_label_02

        "-Volver atrás-":

            call p_Help

            jump FuckH_decision

########################################################
######################################################## ORNAMENT 02

label FuckH_orn_label_02:

    menu FuckH_orn_02_question (screen="dun_choice_screen"):

        "<Pechos>":

            call p_Help

            $ FuckH_orn_focus_ = "boobs"

            jump FuckH_orn_boobs_label

        "<Trasero>":

            call p_Help

            $ FuckH_orn_focus_ = "butt"

            jump FuckH_orn_butt_label

        "<Polla>":

            call p_Help

            $ FuckH_orn_focus_ = "dick"

            jump FuckH_orn_dick_label

        "<Ornamentación de mascota>":

            call p_Help

            $ FuckH_orn_focus_ = "pet"

            jump FuckH_orn_pet_label

        
        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label

########################################################
######################################################## # Ornament EYES/MASK

label FuckH_orn_eyes_label:

    menu FuckH_orn_eyes_question (screen="dun_choice_screen"):
        
        pt "¿Le permito poder ver?"

        "<Vendar ojos>":

            call p_Help

            call WIP_dun

            #$ FuckH_orn_mask__ = ""
            $ FuckH_orn_eyes__ = "blindfold"
            #$ FuckH_orn_mouth__ = ""

            call FuckH_Image_Start

            jump FuckH_orn_eyes_label

        "<Máscara con orificio para ojos y boca>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_mask__ = "black_latex"
            #$ FuckH_orn_eyes__ = ""
            #$ FuckH_orn_mouth__ = ""

            call FuckH_Image_Start

            jump FuckH_orn_eyes_label

        "<Máscara con orificio para boca>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_mask__ = "black_latex"
            $ FuckH_orn_eyes__ = "black_latex"
            #$ FuckH_orn_mouth__ = ""

            call FuckH_Image_Start

            jump FuckH_orn_eyes_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label

########################################################
######################################################## # Ornament MOUTH

label FuckH_orn_mouth_label:

    menu FuckH_orn_mouth_question (screen="dun_choice_screen"):
        
        pt "¿Le permito poder ver?"

        "<Mordaza de bola>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_mouth__ = "gagBall"

            call FuckH_Image_Start

            jump FuckH_orn_mouth_label

        "<Mordaza de polla interna>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_mouth__ = "gagDickIn"

            call FuckH_Image_Start

            jump FuckH_orn_mouth_label

        "<Mordaza de arnés>": # Whole HEad - harness gag

            call p_Help

            call WIP_dun

            $ FuckH_orn_mask__ = "harnessGag"
            $ FuckH_orn_mouth__ = "harnessGag"

            call FuckH_Image_Start

            jump FuckH_orn_mouth_label

        "<Mordaza de araña>": # Open mouth for dick - Spider Gag

            call p_Help

            call WIP_dun

            $ FuckH_orn_mouth__ = "spiderGag"

            call FuckH_Image_Start

            jump FuckH_orn_mouth_label

        "<Sujeción de boca>": # Open mouth for dick - Mouth Clamp

            call p_Help

            call WIP_dun

            $ FuckH_orn_mouth__ = "mouthClamp"

            call FuckH_Image_Start

            jump FuckH_orn_mouth_label

        "<Pintar>": #

            call p_Help

            jump FuckH_paint_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label

########################################################
######################################################## # Ornament NECK

label FuckH_orn_neck_label:

    menu FuckH_orn_neck_question (screen="dun_choice_screen"):
        
        pt "¿Qué collar puedo ponerle?"

        "<Collar de postura>": # Posture Collar

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "postureCollar"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "<Collar con la inscripción \"SLAVE\">": #Slave

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "collarSlave"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "<Collar con la inscripción \"SLUT\">": #Slut

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "collarSlut"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "<Collar con la inscripción \"WHORE\">": #Whore

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "collarWhore"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "<Gargantilla (Choker) ajustada>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "choker"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "<Collar rosado con corazón>": # Daddy's girl pink heart spikes

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "CollarPink"

            call FuckH_Image_Start

            jump FuckH_orn_neck_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label

########################################################
######################################################## # Ornament BOOBS

label FuckH_orn_boobs_label:

    menu FuckH_orn_boobs_question (screen="dun_choice_screen"):
        
        pt "¿Qué puedo ponerle en estos pechos de silicona?"

        "<Pinzas para pezones>": # nipple Clamps

            call p_Help

            call WIP_dun

            $ FuckH_orn_nipples__ = "clamps"

            call FuckH_Image_Start

            jump FuckH_orn_boobs_label

        "<Fuertes pinzas para pezones>": # Extreme Nipple Clamps

            call p_Help

            call WIP_dun

            $ FuckH_orn_nipples__ = "clampsExtreme"

            call FuckH_Image_Start

            jump FuckH_orn_boobs_label

        "<Succionadora giratoria eléctrica": # Twist n suck electro vacuum

            call p_Help

            call WIP_dun

            $ FuckH_orn_nipples__ = "twistSuckVacuum"

            call FuckH_Image_Start

            jump FuckH_orn_boobs_label

        "<Pintar>": #

            call p_Help

            jump FuckH_paint_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label_02


########################################################
######################################################## # Ornament BUTT

label FuckH_orn_butt_label:

    menu FuckH_orn_butt_question (screen="dun_choice_screen"):
        
        pt "¿Qué puedo ponerle en su trasero?"

        "<>": # nipple Clamps

            call p_Help

            call WIP_dun

            #$ FuckH_orn_nipples__ = "clamps"

            call FuckH_Image_Start

            jump FuckH_orn_butt_label

        "<Juguetes>": # Extreme Nipple Clamps

            call p_Help

            jump FuckH_orn_butt_toys_label

        "<Pintar>": #

            call p_Help

            jump FuckH_paint_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label_02


########################################################
######################################################## # Ornament BUTT

label FuckH_orn_butt_toys_label:

    menu FuckH_orn_butt_toys_question (screen="dun_choice_screen"):
        
        pt "¿Qué juguete puedo usar?"

        "<Tapón anal pequeño>": # 3 Variantes Small=Slave Med=Whore Big=Slut

            call p_Help

            call WIP_dun

            #$ FuckH_act_focus_ = FuckH_act_body_ + "_toy_plugSmall"

            #call FuckH_Image_Start

            jump FuckH_orn_butt_toys_label

        "<Tapón anal mediano>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_butt_toys_label

        "<Tapón anal grande>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_butt_toys_label

        "<>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_butt_toys_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_butt_label

########################################################
######################################################## # Ornament DICK

label FuckH_orn_dick_label:

    menu FuckH_orn_dick_question (screen="dun_choice_screen"):
        
        pt "¿Tengo que tocársela...?"

        "<Jaula de castidad>": # Penis Cage (To lock the penis) It avoids Cum posibilities over 50.

            call p_Help

            call WIP_dun

            #$ FuckH_orn_nipples__ = "clamps"

            call FuckH_Image_Start

            jump FuckH_orn_dick_label

        "<Anilla doble para el pene>": # Double cockring # It reduces the Cum posibilities if it´s high.

            call p_Help

            call WIP_dun

            #$ FuckH_orn_nipples__ = "clampsExtreme"

            call FuckH_Image_Start

            jump FuckH_orn_dick_label

        "<Pintar>": #

            call p_Help

            jump FuckH_paint_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label_02

########################################################
######################################################## # ORNAMENT PET-GENERAL

label FuckH_orn_pet_label:

    menu FuckH_orn_pet_question (screen="dun_choice_screen"):
        
        pt "¿De qué animal?"

        "<De perra>":

            call p_Help

            jump FuckH_orn_pet_dog_label

        "<De gata>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_pet_label

        "<De caballo>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_pet_label

        "<De cerda>":

            call p_Help

            call WIP_dun

            jump FuckH_orn_pet_label

        "-Volver atrás-":

            call p_Help

            jump FuckH_orn_label_02

########################################################
######################################################## # ORNAMENT PET DOG

label FuckH_orn_pet_dog_label:

    menu FuckH_orn_pet_dog_question (screen="dun_choice_screen"):
        
        pt "¿Aceptará que la trate como la perra que es?"

        "<Collar de perro>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_neck__ = "collarDog"

            call FuckH_Image_Start

            jump FuckH_orn_pet_dog_label

        "<Correa>": # Collar is necessary

            call p_Help

            call WIP_dun

            if FuckH_orn_neck__ == "collarDog":

                $ FuckH_orn_leash__ = "leashDog"

                call FuckH_Image_Start

            else:

                pt "Necesitaría primero ponerle el collar de perro."

            jump FuckH_orn_pet_dog_label

        "<Orejas de perro>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_head__ = "earsDog"

            call FuckH_Image_Start

            jump FuckH_orn_pet_dog_label

        "<Cuenco para el esperma>":

            call p_Help

            call WIP_dun

            call FuckH_Image_Start

            jump FuckH_orn_pet_dog_label

        "<Tapón anal con cola de perro>":

            call p_Help

            call WIP_dun

            $ FuckH_orn_asshole__ = "tailDog"

            call FuckH_Image_Start

            jump FuckH_orn_pet_dog_label

        "-Volver atrás-":

            call p_Help

            call WIP_dun

            jump FuckH_orn_pet_label

########################################################
######################################################## # ORNAMENT PET CAT

########################################################
######################################################## # ORNAMENT PET HORSE

########################################################
######################################################## # ORNAMENT PET PIG


########################################################
########################################################

########################################################
######################################################## #Decision_ BONDAGE

label FuckH_decision_pose_bondage:

    menu FuckH_decision_pose_bondage_question (screen="dun_choice_screen"):
        
        pt "Con cuerdas, o..."

        "<Hog Tie>":

            call p_Help

            if FuckH_pose_ == "hogTie":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "hogTie"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage

        "<Barra separadora de tobillos y puños>": # Handcuff Ankle cuffs spreader

            call p_Help

            if FuckH_pose_ == "spreader":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "spreader"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage

        "<Ball Tie>": # Strappado Balltie

            call p_Help

            if FuckH_pose_ == "ballTie":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "ballTie"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage

        "<Encorvada>": # Bent Over bamboo

            call p_Help

            if FuckH_pose_ == "bentOver":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "bentOver"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage


        "-Otros-":

            call p_Help

            jump FuckH_decision_pose_bondage_02


        "-Volver atrás-":

            call p_Help

            jump FuckH_decision_pose


########################################################
########################################################

########################################################
######################################################## #Decision_ BONDAGE 02

label FuckH_decision_pose_bondage_02:

    menu FuckH_decision_pose_bondage_02_question (screen="dun_choice_screen"):
        
        #pt "¿Cómo podría inmovilizarla?"

        "<Ebi>": # Ebi

            call p_Help

            if FuckH_pose_ == "ebi":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "ebi"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_02

        "<Oración inversa japonesa>": # inversePrayer

            call p_Help

            if FuckH_pose_ == "inversePrayer":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "inversePrayer"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_02

        "<Ball stretcher>": # ballStretcher

            call p_Help

            if FuckH_pose_ == "ballStretcher":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "ballStretcher"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_02

        "<Pozo de la condenación>": # pitDoom

            call p_Help

            if FuckH_pose_ == "pitDoom":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "pitDoom"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_02

        "-Volver atrás-":

            call p_Help

            jump FuckH_decision_pose_bondage


########################################################
########################################################

########################################################
######################################################## #Decision_ BONDAGE_ SUSPENSION

label FuckH_decision_pose_bondage_suspension:

    menu FuckH_decision_pose_bondage_suspension_question (screen="dun_choice_screen"):
        
        pt "¿Cómo podría inmovilizarla?"


        "<Hamaca de cuerda>": # Rope hammock // Basic Horizontal Suspension_01

            call p_Help

            if FuckH_pose_ == "ropeHammock":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "ropeHammock"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "<Hishi Fit>": # Hishi Fit (aka Alpine or Full Rope Harness, based on Rope Sit Harness)_01

            call p_Help

            if FuckH_pose_ == "hishiFit":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "hishiFit"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "<Pierna invertida>": # Inverted Single Leg Suspension_01

            call p_Help

            if FuckH_pose_ == "invertLeg":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "invertLeg"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "<Peter Pan>":

            call p_Help

            if FuckH_pose_ == "peterPan":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "peterPan"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "<Yoko Tzury>": # Yoko Tzury

            call p_Help

            if FuckH_pose_ == "yokoTzury":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "yokoTzury"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "<Aspa invertida>": # Inverted saltire

            call p_Help

            if FuckH_pose_ == "invertSaltire":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "invertSaltire"

                call FuckH_Image_Start

            jump FuckH_decision_pose_bondage_suspension

        "-Volver atrás-":

            call p_Help

            jump FuckH_decision_pose

########################################################
########################################################

########################################################
########################################################

########################################################
########################################################

########################################################
########################################################

label FuckH_pose__already:

    pt "Si ya está en esta posición..."

    return

########################################################
######################################################## #Furniture ON FEET

label FuckH_decision_pose_onFeet:

    if FuckH_pose_ == "onFeet":

        pt "Pero si ya está de pie..."

    else:

        $ FuckH_pose_ = "onFeet"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose

    

########################################################
########################################################

########################################################
######################################################## #Furniture GYNO_CHAIR

label FuckH_decision_pose_gynoChair:

    if FuckH_pose_ == "gynoChair":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "gynoChair"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose

########################################################
########################################################

########################################################
######################################################## #Furniture MANTIS_CHAIR

label FuckH_decision_pose_mantisChair:

    if FuckH_pose_ == "mantisChair":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "mantisChair"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose

########################################################
########################################################

########################################################
######################################################## #Furniture SCORPION_BENCH

label FuckH_decision_pose_scorpionBench:

    if FuckH_pose_ == "scorpionBench":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "scorpionBench"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose

########################################################
########################################################

########################################################
######################################################## #Furniture THRONE   ((REALLY NECESSARSY??))

label FuckH_decision_pose_throne:

    if FuckH_pose_ == "throne":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "throne"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose

########################################################
########################################################

########################################################
######################################################## #Furniture ANDREWCROSS

label FuckH_decision_pose_andrewCross:

    if FuckH_pose_ == "andrewCross":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "andrewCross"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose_02

########################################################
########################################################

########################################################
######################################################## #Furniture PADDED_WALL

label FuckH_decision_pose_paddedWall:

    if FuckH_pose_ == "paddedWall":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "paddedWall"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose_02


########################################################
########################################################

########################################################
######################################################## #Furniture IMPALER

label FuckH_decision_pose_impaler:

    if FuckH_pose_ == "impaler":

        call FuckH_pose__already

    else:

        call WIP_dun

        $ FuckH_pose_ = "impaler"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose_02

########################################################
########################################################

########################################################
######################################################## #Furniture PRISON

label FuckH_decision_pose_prison:

    menu FuckH_decision_pose_prison_question (screen="dun_choice_screen"):
        
        pt "¿?"

        "<Prisión Taburete>": # prison Cage

            call p_Help

            if FuckH_pose_ == "prisonCage":

                call FuckH_pose__already

            else:

                call WIP_dun

                $ FuckH_pose_ = "prisonCage"

                call FuckH_ChangePos_Start

                call FuckH_Image_Start

            jump FuckH_decision_pose_prison

        "<Celda>": # prison Bin

            call p_Help

            if FuckH_pose_ == "prisonBin":

                call FuckH_pose__already

            else:

                call WIP_dun

                if pLockerC.hi_dom < (30 + dundiff):

                    $ FuckH_pose_ = "onFeet"

                    call FuckH_Image_Start

                    show hiromi_gen_exp_mouth sad_Silentx07
                    show hiromi_gen_exp_eyes 07
                    show hiromi_gen_exp_piris front07
                    show hiromi_gen_exp_eyebrows angryx04
                    with dissolve

                    hi "..."

                    show hiromi_gen_exp_mouth sad_Talkingx007
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows angryx05
                    with dissolve

                    hi "¡Estás de coña si crees que me voy a meter ahí!"

                    show hiromi_gen_exp_mouth sad_Silentx07
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx05
                    with dissolve

                    pt "Quizás si consigo someterla un poco más,"

                    extend " logre convencerla."

                else:

                    $ FuckH_pose_ = "prisonBin"

                    call FuckH_ChangePos_Start

                    call FuckH_Image_Start

            jump FuckH_decision_pose_prison

        "-Volver atrás-":

            call p_Help

            jump FuckH_decision_pose_02

########################################################
########################################################

########################################################
######################################################## #Furniture BED

label FuckH_decision_pose_bed:

    if FuckH_pose_ == "bed":

        call FuckH_pose__already

    else:

        # ¿Atarla en la cama?

        call WIP_dun

        $ FuckH_pose_ = "bed"

        call FuckH_ChangePos_Start

        call FuckH_Image_Start

    jump FuckH_decision_pose_02

########################################################
########################################################

########################################################
########################################################

########################################################
########################################################

label FuckH_conversation:

    if FuckH_act_focus_ == "nothing":

        menu FuckH_conversation_question (screen="dun_choice_screen"):
            
            pt "¿Qué le pregunto?"

            "¿Has estado alguna vez en este calabozo?" if FuckH_conversation_dungeon_cond == False:

                call p_Help

                $ FuckH_conversation_dungeon_cond = True

                hi "No en este."

                hi "Pero he estado en varios muy similares."

                jump FuckH_conversation

            "¿Eres virgen analmente?" if FuckH_conversation_analvirgin_cond == False:

                call p_Help

                $pLockerC.ch_pts_C("hi_dom",1)

                $ FuckH_conversation_analvirgin_cond = True

                hi "..."

                hi "No,"

                extend " no lo soy."

                hi "¿Es que Txell no te ha contado absolutamente nada?"

                p "Sí,"

                extend " sí me lo ha contado."

                hi "¡¿Entonces por qué diablos me estás preguntando algo que ya sabes?!"

                p "Porque quiero que seas tú quien me responda."

                hi "..."

                jump FuckH_conversation

            "¿Te gustan más los hombres o las mujeres?" if FuckH_conversation_sexpreference_cond == False:

                call p_Help

                $pLockerC.ch_pts_C("hi_dom",1)

                $ FuckH_conversation_sexpreference_cond = True

                hi "..."

                hi "Eso seguro que ya te lo ha comentado Txell."

                p "Así es."

                hi "¿Entonces...?"

                p "Te atrae el morbo,"

                extend " la curiosidad,"

                extend " y las particularidades del individuo,"

                p "de eso no tengo ninguna duda."

                hi "..."

                p "Del mismo modo que estoy convencido,"

                p "que por muy interesante que fuera una mujer de ciento veinte quilos,"

                p "nunca se te pasaría por la cabeza llevártela a la cama,"

                p "a menos que fuera para un experimento mórbido de una sola noche."

                hi "..."

                hi "Es posible."

                p "Entonces debe existir primero al menos una atracción física."

                hi "Es obvio."

                p "El hecho de que no hayas salido del calabozo aún,"

                p "me indica que por lo menos no he suspendido esa parte."

                p "¿Estoy en lo cierto?"

                hi "..."

                hi "Que seas calvo,"

                hi "no significa que seas feo."

                p "¿Y mi cuerpo?"

                hi "No es de mis favoritos,"

                hi "pero tampoco diré que es horrible."

                p "..."

                jump FuckH_conversation

            "-Volver atrás-":

                call p_Help

                jump FuckH_Start

    else:

        pt "No creo que sea buen momento preguntarle estas cosas."

        jump FuckH_Start

############################################################################
############################################################################

############################################################################
############################################################################

############################################################################
############################################################################


label FuckH_endTherapy:

    if FuckH_act_focus_ == "nothing":

        menu FuckH_endTherapy_question (screen="dun_choice_screen"):
            
            pt "¿Seguro?"

            "Sí.":

                call p_Help

                jump FuckH_endTherapy_sure

            "Aún no.":

                call p_Help

                jump FuckH_Start

    else:

        pt "Primero debería liberarla y ponerla de pie."

        jump FuckH_Start

label FuckH_endTherapy_sure:

    if PlatinumHelp == True:
        show screen Points()
        hide screen PointsDungeon
        with dissolve

    if pLockerC.hi_dom < (25 + dundiff):

        p "Definitivamente,"

        p "esto está resultando una completa pérdida de tiempo,"

        extend " Hiromi."

        hi "..."

        hi "Me alegro que por fin te hayas dado cuenta de ello."

        n "Rápidamente consigue vestirse,"

        n "y sin apenas dirigirte la mirada,"

        n "pasa rápidamente por tu lado en dirección a la puerta."

        p "..."

        jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02

    else:

        call WIP

        jump afternoon05_Library


##############################################################################################################################
###############################################################
###############################################################
###############################################################
###############################################################

##############################################################################################################################
###############################################################
###############################################################
###############################################################
###############################################################

##############################################################################################################################
###############################################################
###############################################################
###############################################################
###############################################################


label aft_dun_h_pose_onFeet:

    #scene bg 05afternoon_dungeon_bg:
        #truecenter
        ##zoom 0.75 xpos 1.5 ypos 0.5
        #zoom 0.8 xpos 1.55 ypos 0.5

    scene bg 05afternoon_dungeon_wall_01:
        truecenter
        zoom 0.55

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_body_down panties:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_body_up crossed_bra:
        hiromi_gen_body_right_zoom_0_25_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_right_zoom_0_25_pos

    show hiromi_gen_exp_blush 01:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_mouth sad_Silentx04:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_eyes 03:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_piris front03:
        hiromi_gen_exp_right_zoom_0_25_pos
    show hiromi_gen_exp_eyebrows serious:
        hiromi_gen_exp_right_zoom_0_25_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_right_zoom_0_25_pos
    #with fade

    return

label aft_dun_h_pose_andrewCross:

    scene 05aft_dun_h_pose_andrewCross:
        truecenter

    return


label aft_dun_h_pose_bed:

    scene 05aft_dun_h_pose_bed:
        truecenter

    return

label aft_dun_h_pose_gynoChair:

    scene 05aft_dun_h_pose_gynoChair:
        truecenter

    return

label aft_dun_h_pose_impaler:

    scene 05aft_dun_h_pose_impaler:
        truecenter

    return

label aft_dun_h_pose_mantisChair:

    scene 05aft_dun_h_pose_mantisChair:
        truecenter

    return

# on Feet

label aft_dun_h_pose_paddedWall:

    scene 05aft_dun_h_pose_paddedWall:
        truecenter

    return


label aft_dun_h_pose_prisonBin:

    scene 05aft_dun_h_pose_prisonBin:
        truecenter

    return


label aft_dun_h_pose_prisonCage:

    scene 05aft_dun_h_pose_prisonCage:
        truecenter

    return


label aft_dun_h_pose_scorpionBench:

    scene 05aft_dun_h_pose_scorpionBench:
        truecenter

    return

######################### BONDAGE_normal

label aft_dun_h_pose_ballStretcher:

    scene 05aft_dun_h_pose_ballStretcher:
        truecenter

    return

label aft_dun_h_pose_ballTie:

    scene 05aft_dun_h_pose_ballTie:
        truecenter

    return

label aft_dun_h_pose_bentOver:

    scene 05aft_dun_h_pose_bentOver:
        truecenter

    return

label aft_dun_h_pose_ebi:

    scene 05aft_dun_h_pose_ebi:
        truecenter

    return

label aft_dun_h_pose_hogTie:

    scene 05aft_dun_h_pose_hogTie:
        truecenter

    return

label aft_dun_h_pose_inversePrayer:

    scene 05aft_dun_h_pose_inversePrayer:
        truecenter

    return

label aft_dun_h_pose_pitDoom:

    scene 05aft_dun_h_pose_pitDoom:
        truecenter

    return

label aft_dun_h_pose_spreader:

    scene 05aft_dun_h_pose_spreader:
        truecenter

    return

######################### BONDAGE_suspension

label aft_dun_h_pose_hishiFit:

    scene 05aft_dun_h_pose_hishiFit:
        truecenter

    return

label aft_dun_h_pose_invertLeg:

    scene 05aft_dun_h_pose_invertLeg:
        truecenter

    return

label aft_dun_h_pose_invertSaltire:

    scene 05aft_dun_h_pose_invertSaltire:
        truecenter

    return

label aft_dun_h_pose_peterPan:

    scene 05aft_dun_h_pose_peterPan:
        truecenter

    return

label aft_dun_h_pose_ropeHammock:

    scene 05aft_dun_h_pose_ropeHammock:
        truecenter

    return

label aft_dun_h_pose_yokoTzury:

    scene 05aft_dun_h_pose_yokoTzury:
        truecenter

    return

##############################################################################################################################
###############################################################
###############################################################

#     '''

# label afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02:

#     n "Sin demasiada demora sigues sus pasos hasta llegar a la enorme estancia."

#     tx "Ya te he dicho que en persona no pienso tratarte Hiromi."


# label afternoon05_Library:

#     p "Desde luego,"

#     p "el nombre de biblioteca le encaja bastante bien a esta habitación..."

#     n "En la enorme sala en la que te encuentras,"

#     n "rodeado de estanterías repletas de conocimiento y entretenimiento,"

#     n "te destacan los enormes sillones y butacas que hay frente de ti."

#     '''

# '''

#     Le preguntas si había estado ya alguna vez en este calabozo, y te responde que no, pero que ha estado en varios muy parecidos.

#     Le puedes preguntar si es virgen analmente.

#     Preguntarle si te encuentra sexualmente atractivo.

# '''

# ########################################################
# ########################################################

# ########################################################
# ########################################################



# ## TOOLTIP


# ''' 
#     FIRST OPTIONS:


#             Domination
#             Happiness
#             Pleasure
#             Pain Asshole
#             Love
#             Orgasms

#                 News:
#             Pain Dick
#             Anal Dilatation
#             Throat Dilatation
#             Close To orgasm

#                 MC:
#             Close to Orgasm
#             Orgasms


#                 FURNITURE
                
#     - Throne Chair. (Just used as DOM)
#     - Andrew Cross.
#     - Padded Wall.
#     - Gyno Chair. (Ginecólogo)
#     - Mantis Chair (Sit down, open legs, arms up.)
#     - Scorpion Bench.
#     - Impaler (o Tower).

#         + prisonS
#     - Cage. (Taburete)
#     - prison. (Sin Bin)


#                 ACTIONS

#         * MOUTH
#     - Kiss her
#     - Deepthroat Spray (Gag-reflex aid)

#         + gags
#     - Ball Gag
#     - Spider Gag (OPen mouth for dick)
#     - Harness Gag (Ball gag, whole head.)
#     - Mouth Clamp

#         * ANAL STIMULATION
#     - Black Kiss
#     - Lubricant
#     - Popper (Drug)
#     - Anal Plug
#         - small = Slave
#         - medium = Whore
#         - Big = Slut
#     - Dildo
#     - Vibrator
#     - Hitachi Wand
#     - Strapon (?)
#     - MC DICK

#         * BOOBS STIMULATION
#     - Suck Nipples
#     - Bite Nipples
#     - Boobjob

#     - Extreme Nipple/Breast Clamps
#     - Twist n suck electro vacuum

#         * DICK/SKIN STIMULATION
    
#         * STIMULATION EQUIPMENT
#     - Seven Star (Correctional long shaft with 7 tiny pins (bloody))
#     - Electrode
#     - Candles
#     - Wartenberg Wheel (7 or 1?)

#         * BONDAGE
#     - Naked Hand
#     - Hog Tie
#     - Spreader Bar
#     - Flogger

#         * CANES & WHIPS
#     - Wanjii cane
#     - Headmasters Hook Cane
#     - Studded Leather Strap
#     - Black Tiger Paddle


#         * ORNAMENT

#         + COLLARS
#     - Posture Collar
#     - Dog Collar

#         + DICK
#     - Rings
#     - Chastity Cage with Spikes
#     - Stretcher Balls 

#         + PET ORNAMENT
#     - But Tail
#     - Dog Ears
#     - Cum Bowl
#     - Leash

# '''

# # Una vez dentro del "calabozo", observas a tu alrededor, sin duda un lugar siniestro, oscuro y envuelto en todo tipo de objetos perturbadores.

# # Al cabo de un rato oyes la puerta abrirse.
# # No sé que le habrás dicho a Txell para convencerla de esta estupidez, peor será mejor que vuelvas a hablar con ella.


# # Básicamente entra enfadada y con cara de malas pulgas exigiéndote que vuelvas a hablar con Txell para que le devuelvas el sentido común y logres que ella la ayude mientras tú te vas a dar una vuelta.

# # Cuando ve que te niegas a ello, no se lo toma muy bien. Le expones lo que ocurrirá si sale por esa puerta, que ella tendrá que irse con la cola entre las piernas porque nadie la va ayudar aquí, él es su última oportunidad. Txell no le hubiera dejado en el mando sino creyese que puedo ayudarte.

# # Lo primero será que te desnudes. Acepta desnudarse hasta quedarse en ropa interior. más allá de ahí no quiere desnudarse más. (Tampoco querrá ponerse ningún tipo traje de latex ni nada parecido.)

# # Tendrás que convencerla con palabras, pero si lo haces demasiado a menudo te dirá que si lo único que vais a hacer ahí es hablar sobre sus miserias.


#     # No he dicho nada de follar.


#     # Hacer otro PHOTHOMERGE del lugar del BDSM.

#     ## http://www.thesecretdungeon.co.uk/facilities/virtual-tour-of-the-dungeon.html

#     # Así sabré que herramientas podré usar y cómo...

# ## Throne Chair.
# ## St. Andrew Cross. (Cruz en Aspa)
#     ## Cahterine Wheel, like St. Andrew Cross, but with Rotation.
# ## Padded Wall. (With Hosiptal Cuffs, Padded Leather).
# ## Gyno Chair. (Mesa de ginecólogo, para mantener las piernas abiertas.)
# ## Scorpion Bench # Como Gyno Chair pero pudiéndote atar por todas partes, me parece).
# ## Cage. (Prisión Taburete.)
# ## Sin Bin. (Prostíbulo, Prisión).
# ## Bench (Para tenerla a cuatro patas reposando sobre un algo...?)
# ## Box (With Holes... not sure what´s worth it yet...)
# ## Impaler (Las piernas atadas con el palo que impala (Vibrador), también se puede inmovilizar muñecas con el cuello).
# ## O Tower (Parecido al impaler...)
# ## Hitachi wand Massager Over Tower (Hitachi = Marca) (Se usa la torre.)
# ## Mantis Chair (Sentada con las piernas abiertas y atadas y con los brazos en alto en forma de cruz.) Tiene la particularidad que el coño queda al aire por debajo.
# ## Leather Swing (Para quedar colgado del techo como si fuera un columpio, pero con las muñecas y los pies atados..)
# ## 2 Electric Hoists (Eletrico porque sube y baja automáticamente) (Para dejarte suspendido en el aire por las muñecas o por los pies.)
# ## 1 Manual Hoist (No baja y sube automáticamente)
# ## Four Poster Bed (To tie with ropes or chains your client.)
# ## Sybian (Vibrador con posaderas para los muslos que da vueltas y tiembla segúna la potencia elegida.)
# ## Fucking Machine (Se estira y la polla la penetra sola.)
# ## Whips and Chains.

# ## https://es.sexmachinereviews.co.uk/advice/electrosex-and-estim-electrode-positions.html

# ####


# ''' 
# Cuerdas Shibari y Kinbaku

# El dominante: Nawashi.
# El sumiso: Jojun.

# Shibari: no se enfoca en el ser sumiso si no en cómo realizar los nudos de tal manera que sea un camino para llegar al placer.
#     En el shibari se ata y se usan nudos muy estilizados para atar al ser sumiso sin necesariamente restringir su movimiento.

# Kinbaku: Va muy de la mano con el shibari, pero es aún más estética y artística que se enfoca en dar placer al ser sumiso atando con cuerdas ciertas partes del cuerpo provocando placer.


# Bondage = busca restringir el movimiento 
# Shibari = busca llegar al placer por medio de las ataduras. «shibari significa atadura>>
# Kinbaku = da placer por medio de la presión de cuerdas en ciertas partes del cuerpo. <<Atar fuertemente>>



# Aro para shibari de Acero inoxidable.



# E-stim Electro estimulador sexual. (Parches para piel eléctricos)

# Armbinder de doble correa - corset para brazos.

# Camisa de Fuerza de cuero.

# bondage-ball-stretcher-ref-9443

# Capucha de cuero sintético privación sensorial.

# Arnés de cuero Fetish Masculino.

# Anchor But Plug

# Anal inflatable butt expander silicone

# Pinzas regulables con cascabel para pezones.

# Pinzas japonesas Mariposas - Clover Japanese Clamps -

# Candado nasal con correa - Nose shackle lock -


# Vestido Txell:
#     Arnés de cuero Fetish Femenino (?)
#     Catsuit de lycra brillante con escote y doble cremallera.
#     Catsuit de Lycra brillante ajustado hasta el cuello.

# '''