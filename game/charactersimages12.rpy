
image paris_bg_ = "images/day06/window/paris_bg_.webp"
image paris_bg_blur = "images/day06/window/paris_bg_blur.webp"

image paris_fg_ = "images/day06/window/paris_fg_.webp"
image paris_fg_blur = "images/day06/window/paris_fg_blur.webp"

image paris_mg_ = "images/day06/window/paris_mg_.webp"
image paris_mg_blur = "images/day06/window/paris_mg_blur.webp"



image paris_window_01:

    contains:
        "paris_bg_blur"

        truecenter

    contains:
        "paris_mg_"
        truecenter
        additive 1.0

    contains:
        "paris_fg_"
        truecenter

image paris_window_02:

    contains:
        "paris_bg_"
        truecenter

    contains:
        "paris_mg_blur"
        subpixel True        
        truecenter
        additive 1.0
        easein_quad 30.0 alpha 0.0

    contains:
        "paris_fg_blur"
        truecenter


image barcelona_bg_ = "images/day06/window/barcelona_bg_.webp"
image barcelona_bg_blur = "images/day06/window/barcelona_bg_blur.webp"
image barcelona_bg_blur02 = "images/day06/window/barcelona_bg_blur02.webp"

image barcelona_mg_ = "images/day06/window/barcelona_mg_.webp"
image barcelona_mg_blur = "images/day06/window/barcelona_mg_blur.webp"


image barcelona_window_01:

    contains:
        "barcelona_bg_blur02"
        truecenter

    contains:
        "barcelona_mg_"
        subpixel True        
        truecenter
        zoom 1.2
        additive 1.0

    contains:
        "paris_fg_"
        zoom 1.2
        truecenter

image barcelona_window_02:

    contains:
        "barcelona_bg_blur"
        truecenter

    contains:
        "barcelona_mg_blur"
        subpixel True        
        truecenter
        zoom 1.2
        additive 1.0
        #easein_quad 30.0 alpha 0.0

    contains:
        "paris_fg_blur"
        zoom 1.2
        truecenter
        #easein_quad 30.0 alpha 0.0

image barcelona_window_03:

    contains:
        "barcelona_bg_"
        truecenter

    contains:
        "barcelona_mg_blur"
        truecenter
        zoom 1.2
        additive 1.0
        easein_quad 30.0 alpha 0.0

    contains:
        "paris_fg_blur"
        zoom 1.2
        truecenter
        easein_quad 30.0 alpha 0.0



label day06_ending_window:

    # hide screen Points_PedreraSex
    # hide screen Points
    # hide screen quick_menu

    call c_title

    if day06_ending_city == "paris":

        scene paris_window_01:
            subpixel True
            truecenter
            #zoom 0.4 xpos 0.5 ypos 0.5 # Whole image
            zoom 1.2 xpos 1.5 ypos -0.5 # Beginning?
            easein_quad 50.0 zoom 0.7 xpos 0.0 ypos 0.7 # Eifeel
        show paris_window_02:
            subpixel True
            truecenter
            zoom 1.2 xpos 1.5 ypos -0.5 # Beginning?
            alpha 0.0
            parallel:
                easein_quad 50.0 zoom 0.7 xpos 0.0 ypos 0.7 # Eifeel
            parallel:
                pause 15.0
                ease 20.0 alpha 1.0
        show black02:
            alpha 1.0
            easein 15.0 alpha 0.0

    if day06_ending_city == "barcelona":

        scene barcelona_window_01:
            subpixel True
            truecenter
            zoom 1.0 ypos -0.5 #Beggining
            easein_quad 50.0 zoom 0.7 ypos 0.66 # Sagrada familia

        show barcelona_window_02:
            subpixel True
            truecenter
            zoom 1.0 ypos -0.5 #Beggining
            alpha 0.0
            parallel:
                easein_quad 50.0 zoom 0.7 ypos 0.66 # Sagrada familia
            parallel:
                pause 5.0
                ease 20.0 alpha 1.0

        show barcelona_window_03:
            subpixel True
            truecenter
            zoom 1.0 ypos -0.5 #Beggining
            alpha 0.0
            parallel:
                easein_quad 50.0 zoom 0.7 ypos 0.66 # Sagrada familia
            parallel:
                pause 15.0
                ease 20.0 alpha 1.0


    with Dissolve(1.0)

    pause 3.0

    call credits_label

    show black03:
        alpha 0.0
        easein_quad 5.0 alpha 0.3
        pause 25.0
        easein_quad 25.0 alpha 1.0

    return

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

############################################

image ped_assf_ass = SaturateTint("images/day05/pedrera/ped_assf_ass.webp")
image ped_assf_assOver = SaturateTint("images/day05/pedrera/ped_assf_assOver.webp")
image ped_assf_m_finger = SaturateTint("images/day05/pedrera/ped_assf_m_finger.webp")

# Ass Alone.
image ped_assf_comp01:

    # contains:
    #     "bg_dark_a_blurry_01"
    #     truecenter
    #     zoom 3.0

    contains:
        "bg 01"
        truecenter
        zoom 3.0

    contains:
        "ped_assf_ass"
        truecenter

# Going close to the ass.
image ped_assf_comp02:

    # contains:
    #     "bg_dark_a_blurry_01"
    #     truecenter
    #     zoom 3.0

    contains:
        "bg 01"
        truecenter
        zoom 3.0

    contains:
        "ped_assf_ass"
        truecenter

    
    contains:
        "ped_assf_m_finger"
        subpixel True        
        transform_anchor True
        xalign 0.31 yalign 0.26
        rotate 35 xpos 0.5 ypos 3.5 # Down
        easein 5.0 rotate 5 xpos 0.83 ypos 1.3 # Touching Arm Middle
        block:
            ease 2.0 rotate 30 xpos 0.58 ypos 1.2 # Touching Arm to left.
            ease 1.5 rotate -10 xpos 0.98 ypos 1.1 # Touching Arm to right.
            ease 2.5 rotate 5 xpos 0.8 ypos 1.3 # Touching Arm Middle
            ease 2.2 rotate 30 xpos 0.58 ypos 1.2 # Touching Arm to left.
            ease 2.0 rotate 5 xpos 0.8 ypos 1.3 # Touching Arm Middle
            ease 1.5 rotate -10 xpos 0.98 ypos 1.1 # Touching Arm to right.
            repeat
        alpha 0.75


# Going Around
image ped_assf_comp03: 

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 3.0

    contains:
        "ped_assf_ass"
        truecenter

    
    contains:
        "ped_assf_m_finger"
        subpixel True        
        transform_anchor True
        xalign 0.31 yalign 0.26
        rotate 5 xpos 0.83 ypos 1.3 # Touching Arm Middle
        block:
            ease 2.0 rotate 30 xpos 0.58 ypos 1.2 # Touching Arm to left.
            ease 1.5 rotate -10 xpos 0.98 ypos 1.1 # Touching Arm to right.
            ease 2.5 rotate 5 xpos 0.8 ypos 1.3 # Touching Arm Middle
            ease 2.2 rotate 30 xpos 0.58 ypos 1.2 # Touching Arm to left.
            ease 2.0 rotate 5 xpos 0.8 ypos 1.3 # Touching Arm Middle
            ease 1.5 rotate -10 xpos 0.98 ypos 1.1 # Touching Arm to right.
            repeat
        alpha 0.75
    

# Penetrating
image ped_assf_comp04:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 3.0

    contains:
        "ped_assf_ass"
        truecenter
    
    contains:
        "ped_assf_m_finger"
        subpixel True
        transform_anchor True
        xalign 0.31 yalign 0.26
        rotate 5 xpos 0.83 ypos 1.3 # Touching Arm Middle
        ease 5.0 rotate 15 xpos 0.63 ypos 0.8 # Half Finger Up
        easeout_quad 2.0 rotate -10 xpos 0.53 ypos 0.47 # Whole Finger Up
        block:
            #ease_quad 2.0 rotate -40 xpos 0.48 ypos 0.46 # Whole Finger Down
            ease_quad 2.0 rotate 15 xpos 0.63 ypos 0.8 # Half Finger Up
            ease 2.2 rotate -30 xpos 0.82 ypos 0.5 # Half Finger Down
            easein_quad 1.9 rotate -10 xpos 0.53 ypos 0.47 # Whole Finger Up
            easeout_quad 2.0 rotate 15 xpos 0.63 ypos 0.8 # Half Finger Up
            ease 1.0 rotate -10 xpos 0.53 ypos 0.47 # Whole Finger Up
            ease 2.0 rotate 15 xpos 0.63 ypos 0.8 # Half Finger Up
            easein_quad 2.0 rotate -10 xpos 0.53 ypos 0.47 # Whole Finger Up
            repeat

    contains:
        "ped_assf_assOver"
        truecenter

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

############################################

image ped_cs_cunOP_d = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunOP_d.webp")
image ped_cs_cunOP_nTongue = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunOP_nTongue.webp")

image ped_cs_kissBef_d_body = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_d_body.webp")
image ped_cs_kissBef_d_exp_pupil_camera = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_d_exp_pupil_camera.webp")
image ped_cs_kissBef_d_exp_pupil_right = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_d_exp_pupil_right.webp")
image ped_cs_kissBef_d_exp_pupil_rightDown = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_d_exp_pupil_rightDown.webp")
image ped_cs_kissBef_d_hairFront = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_d_hairFront.webp")
image ped_cs_kissBef_m_body = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_m_body.webp")
image ped_cs_kissBef_n_arm_cheek = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_arm_cheek.webp")
image ped_cs_kissBef_n_arm_cheek_bra = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_arm_cheek_bra_[MShooter_Bracelet].webp")
image ped_cs_kissBef_n_arm_down = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_arm_down.webp")
image ped_cs_kissBef_n_body = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_body.webp")
image ped_cs_kissBef_n_glasses = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_glasses.webp")
image ped_cs_kissBef_n_hairFront = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissBef_n_hairFront.webp")

default ped_cs_kiss_eyes_Cond = "right"
default ped_cs_kiss_n_arm_Cond = "down"

image ped_cs_kissBef_nd_01:

    # contains:
    #     "bg_dark_a_blurry_01"
    #     truecenter
    #     zoom 2.5

    contains:
        "bg 01"
        truecenter
        zoom 2.5

# NEUS
    contains:
        "ped_cs_kissBef_n_body"
        truecenter

    contains:
        "ped_cs_kissBef_n_glasses"
        truecenter

    
    contains:
        "ped_cs_kissBef_n_hairFront"
        truecenter

# DIDAC
    contains:
        ConditionSwitch(
            p_girl_active.id == "p_didac", At("ped_cs_kissBef_d_body", truecenter),
            p_girl_active.id == "p_txell", At("ped_cs_kissBef_m_body", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            p_girl_active.id == "p_didac" and ped_cs_kiss_eyes_Cond == "right", At("ped_cs_kissBef_d_exp_pupil_right", truecenter),
            p_girl_active.id == "p_didac" and ped_cs_kiss_eyes_Cond == "rightDown", At("ped_cs_kissBef_d_exp_pupil_rightDown", truecenter),
            p_girl_active.id == "p_didac" and ped_cs_kiss_eyes_Cond == "camera", At("ped_cs_kissBef_d_exp_pupil_camera", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            p_girl_active.id == "p_didac", At("ped_cs_kissBef_d_hairFront", truecenter),
            #p_girl_active.id == "p_txell", At("ped_cs_kissBef_m_hairFront", truecenter),
            "True", Null())

# Neus Arm
    contains:
        ConditionSwitch(
            ped_cs_kiss_n_arm_Cond == "cheek", At("ped_cs_kissBef_n_arm_cheek", truecenter),
            "True", At("ped_cs_kissBef_n_arm_down", truecenter))

# Neus Bracelet
    contains:
        ConditionSwitch(
            ped_cs_kiss_n_arm_Cond == "cheek" and MShooter_Bracelet in MShooter_Bracelet_var, At("ped_cs_kissBef_n_arm_cheek_bra", truecenter),
            "True", Null())


########################################################################################
########################################################################################
########################################################################################
########################################################################################

image ped_cs_kissAf_nd = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissAf_nd.webp")
image ped_cs_kissAf_nm = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissAf_nm.webp")
image ped_cs_kissAf_n_bra = SaturateTint("images/day05/pedrera/cumshare/ped_cs_kissAf_n_bra_[MShooter_Bracelet].webp")

image ped_cs_kissAf_nd_comp_01:

# Background
    # contains:
    #     "bg_dark_a_blurry_01"
    #     truecenter
    #     zoom 2.5

    contains:
        "bg 01"
        truecenter
        zoom 2.5

# Neus Didac Kiss

    contains:
        ConditionSwitch(
            p_girl_active.id == "p_didac", At("ped_cs_kissAf_nd", truecenter),
            p_girl_active.id == "p_txell", At("ped_cs_kissAf_nm", truecenter),
            "True", Null())
    # contains:
    #     "ped_cs_kissAf_nd"
    #     truecenter

# Bracelet
    contains:
        ConditionSwitch(
            MShooter_Bracelet in MShooter_Bracelet_var, At("ped_cs_kissAf_n_bra", truecenter),
            "True", Null())


########################################################################################
########################################################################################
########################################################################################
########################################################################################
        
image ped_cs_cunTop_d = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunTop_d.webp")
image ped_cs_cunTop_m = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunTop_m.webp")
#image ped_cs_cunTop_n_ani = "ped_cs_cunTop_n_ani.png" # Is this necessary?
image ped_cs_cunTop_n_cun = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunTop_n_cun.webp")
image ped_cs_cunTop_n_bra = SaturateTint("images/day05/pedrera/cumshare/ped_cs_cunTop_n_bra_[MShooter_Bracelet].webp")

image ped_cs_cunTop_d_01:

    contains:
        "bg_dark_a_blurry_01"
        truecenter
        zoom 2.5

    contains:
        "ped_cs_cunTop_d"
        truecenter

    contains:
        "ped_cs_cunTop_n_cun"
        truecenter

    contains:
        ConditionSwitch(
            MShooter_Bracelet in MShooter_Bracelet_var, At("ped_cs_cunTop_n_bra", truecenter),
            "True", Null())

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image ped_cs_aniTop_nd = SaturateTint("images/day05/pedrera/cumshare/ped_cs_aniTop_nd.webp")
image ped_cs_aniTop_nm = SaturateTint("images/day05/pedrera/cumshare/ped_cs_aniTop_nm.webp")

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image d06_cuffHand_bg = "images/day06/d06_cuffHand_bg.webp"

image d06_cuffHand_bed_foreground = "images/day06/d06_cuffHand_bed_foreground.webp"
image d06_cuffHand_chain = "images/day06/d06_cuffHand_chain.webp"
image d06_cuffHand_cuff_closed = "images/day06/d06_cuffHand_cuff_closed.webp"
image d06_cuffHand_cuff_open = "images/day06/d06_cuffHand_cuff_open.webp"
image d06_cuffHand_cuff_open_bracelet_01 = "images/day06/d06_cuffHand_cuff_open_bracelet_01_[MShooter_Bracelet].webp"
image d06_cuffHand_cuff_open_bracelet_02 = "images/day06/d06_cuffHand_cuff_open_bracelet_02_[MShooter_Bracelet].webp"

image d06_cuffHand_mc_hand_relaxed = "images/day06/d06_cuffHand_mc_hand_relaxed.webp"
image d06_cuffHand_mc_hand_tensed = "images/day06/d06_cuffHand_mc_hand_tensed.webp"

image d06_cuffHand_mc_hand_comp:

    contains:
        "d06_cuffHand_bg"
        truecenter

## CHAIN
    contains:
        ConditionSwitch(
            mc_cuff_cuffed in ["closed", "open"], At("d06_cuffHand_chain", truecenter),
            "True", Null()
            )

## HAND  
    contains:
        ConditionSwitch(
            mc_cuff_handTensed == True, At("d06_cuffHand_mc_hand_tensed", truecenter),
            "True", At("d06_cuffHand_mc_hand_relaxed", truecenter)
            )

## CUFF
    contains:
        ConditionSwitch(
            mc_cuff_cuffed == "closed", At("d06_cuffHand_cuff_closed", truecenter),
            "True", Null()
            )

## BED FOREGROUND

    contains:
        "d06_cuffHand_bed_foreground"
        truecenter

## CUFF
    contains:
        ConditionSwitch(
            #mc_cuff_cuffed == "closed", At("d06_cuffHand_cuff_closed", truecenter),
            mc_cuff_cuffed == "open", At("d06_cuffHand_cuff_open", truecenter),
            "True", Null()
            )
## BRACELET

    contains:
        ConditionSwitch(
            MShooter_Bracelet in MShooter_Bracelet_var and mc_cuff_cuffed =="open" and mc_cuff_right == True, At("d06_cuffHand_cuff_open_bracelet_01", truecenter),
            MShooter_Bracelet in MShooter_Bracelet_var and mc_cuff_cuffed =="open" and mc_cuff_right == False, At("d06_cuffHand_cuff_open_bracelet_02", truecenter),
            "True", Null())


########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image d06_cuffLeg_bg = "images/day06/d06_cuffLeg_bg.webp"

image d06_cuffLeg_bed_foreground = "images/day06/d06_cuffLeg_bed_foreground.webp"

image d06_cuffLeg_chain = "images/day06/d06_cuffLeg_chain.webp"
image d06_cuffLeg_cuff_bracelet_01 = "images/day06/d06_cuffLeg_cuff_bracelet_01_[MShooter_Bracelet].webp"
image d06_cuffLeg_cuff_bracelet_02 = "images/day06/d06_cuffLeg_cuff_bracelet_02_[MShooter_Bracelet].webp"

image d06_cuffLeg_cuff_closed = "images/day06/d06_cuffLeg_cuff_closed.webp"
image d06_cuffLeg_cuff_open = "images/day06/d06_cuffLeg_cuff_open.webp"
image d06_cuffLeg_toes_relaxed = "images/day06/d06_cuffLeg_toes_relaxed.webp"
image d06_cuffLeg_toes_tensed = "images/day06/d06_cuffLeg_toes_tensed.webp"

image d06_cuffHand_mc_leg_comp:

    contains:
        "d06_cuffLeg_bg"
        truecenter

## CHAIN
    contains:
        ConditionSwitch(
            mc_cuff_cuffed in ["closed", "open"], At("d06_cuffLeg_chain", truecenter),
            "True", Null()
            )

## CUFF
    contains:
        ConditionSwitch(
            mc_cuff_cuffed == "closed", At("d06_cuffLeg_cuff_closed", truecenter),
            "True", Null()
            )

# BED FOREGROUND
    contains:
        "d06_cuffLeg_bed_foreground"
        truecenter

## TOES  
    contains:
        ConditionSwitch(
            mc_cuff_handTensed == True, At("d06_cuffLeg_toes_tensed", truecenter),
            "True", At("d06_cuffLeg_toes_relaxed", truecenter)
            )

## CUFF
    contains:
        ConditionSwitch(
            #mc_cuff_cuffed == "closed", At("d06_cuffLeg_cuff_closed", truecenter),
            mc_cuff_cuffed == "open", At("d06_cuffLeg_cuff_open", truecenter),
            "True", Null()
            )
## BRACELET

    contains:
        ConditionSwitch(
            MShooter_Bracelet in MShooter_Bracelet_var and mc_cuff_cuffed =="open" and mc_cuff_right == True, At("d06_cuffLeg_cuff_bracelet_02", truecenter),
            MShooter_Bracelet in MShooter_Bracelet_var and mc_cuff_cuffed =="open" and mc_cuff_right == False, At("d06_cuffLeg_cuff_bracelet_01", truecenter),
            "True", Null())

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image d06_backThreesome_bg = "images/day06/d06_backThreesome_bg.webp"


image d06_backThreesome_d_01 = "images/day06/d06_backThreesome_d_01.webp"
image d06_backThreesome_d_02 = "images/day06/d06_backThreesome_d_02.webp"

image d06_backThreesome_m_01 = "images/day06/d06_backThreesome_m_01.webp"
image d06_backThreesome_m_02 = "images/day06/d06_backThreesome_m_02.webp"

image d06_backThreesome_n_01 = "images/day06/d06_backThreesome_n_01.webp"
image d06_backThreesome_n_02 = "images/day06/d06_backThreesome_n_02.webp"

image d06_backThreesome_nb_01 = "images/day06/d06_backThreesome_nb_01.webp"
image d06_backThreesome_nb_02 = "images/day06/d06_backThreesome_nb_02.webp"

image d06_backThreesome_comp:

    contains:
        "d06_backThreesome_bg"
        truecenter

# HEADS
    
    contains:
        ConditionSwitch(
            d06_threesomeDidac == True, At("d06_backThreesome_d_02", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            d06_threesomeBigNeus == True, At("d06_backThreesome_nb_02", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            d06_threesomeNeus == True, At("d06_backThreesome_n_02", truecenter),
            "True", Null())

# ASSES
    contains:
        ConditionSwitch(
            d06_threesomeDidac == True, At("d06_backThreesome_d_01", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            d06_threesomeBigNeus == True, At("d06_backThreesome_nb_01", truecenter),
            "True", Null())

    contains:
        ConditionSwitch(
            d06_threesomeNeus == True, At("d06_backThreesome_n_01", truecenter),
            "True", Null())



########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image p_ao_nVagSex_cum_mov = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nVagSex_cum_mov.webp")
image p_ao_nVagSex_cum_rest = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nVagSex_cum_rest.webp")

image p_ao_nVagSex_sex_mov = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nVagSex_sex_mov.webp")
image p_ao_nVagSex_sex_rest = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nVagSex_sex_rest.webp")

image p_ao_nKiss bifid = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nKiss_bifid.webp")
image p_ao_nKiss weird = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nKiss_weird.webp")
image p_ao_nKiss skin = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nKiss_skin.webp")



########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

image p_ao_cumInMouthAdult_bed = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_bed.webp")
image p_ao_cumInMouthAdult_mc_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_mc_body.webp")
image p_ao_cumInMouthAdult_mc_legs = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_mc_legs.webp")

image p_ao_cumInMouthAdult_nReceive_armUp = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_armUp.webp")
image p_ao_cumInMouthAdult_nReceive_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_body.webp")
image p_ao_cumInMouthAdult_nReceive_cumOver = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_cumOver.webp")
image p_ao_cumInMouthAdult_nReceive_cumSplash = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_cumSplash.webp")

image p_ao_cumInMouthAdult_nReceive_mcDick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_mcDick.webp")
image p_ao_cumInMouthAdult_nReceive_over = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nReceive_over.webp")

image p_ao_cumInMouthAdult_nSuck_armAss_below = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_armAss_below.webp")
image p_ao_cumInMouthAdult_nSuck_armAss_over = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_armAss_over.webp")
image p_ao_cumInMouthAdult_nSuck_armRest = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_armRest.webp")
image p_ao_cumInMouthAdult_nSuck_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_body.webp")
image p_ao_cumInMouthAdult_nSuck_headDown = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_headDown.webp")
image p_ao_cumInMouthAdult_nSuck_headUp = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_headUp.webp")
image p_ao_cumInMouthAdult_nSuck_mcDick = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_mcDick.webp")
image p_ao_cumInMouthAdult_nSuck_over = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_nSuck_over.webp")

image p_ao_nABelowIllustration = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nABelowIllustration.webp")

image p_ao_cumInMouthAdult_n_handMast_PROVE = "images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_n_handMast_PROVE.webp"
image p_ao_cumInMouthAdult_n_handMast_idle = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_n_handMast_idle.webp")
image p_ao_cumInMouthAdult_n_handMast_tapClean = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_n_handMast_tapClean.webp")
image p_ao_cumInMouthAdult_n_handMast_tapFull = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_cumInMouthAdult_n_handMast_tapFull.webp")


########################################################################################
########################################################################################
########################################################################################
########################################################################################

transform p_ao_cumInMouthAdult_n_handMast_t_rubbing:
    truecenter
    #alpha 0.75
    xpos 0.5 ypos 0.5 rotate 0 # Down
    # xpos 0.67 ypos 0.22 rotate -5 # High
    block:
        easein_quad 4.0/p_ao_n_vel xpos 0.65 ypos 0.22 rotate -12 # High
        easeout_quad 4.0/p_ao_n_vel xpos 0.5 ypos 0.5 rotate 0 # Down
        repeat

image p_ao_cumInMouthAdult_n_handMast_t_cumming:

    contains:
        "p_ao_cumInMouthAdult_n_handMast_tapClean"
        truecenter
        pause 1.5
        "p_ao_cumInMouthAdult_n_handMast_tapFull" with Dissolve(1.0)

        

image p_ao_cumOnHand_comp_01:

    contains:
        "bg_dark_a_blurry_02"
        truecenter
        zoom 3.5

# BED
    contains:
        "p_ao_cumInMouthAdult_bed"
        truecenter


# MC DICK
    contains:
        "gensex_stan_mc_04_01_dick_01"
        subpixel True
        transform_anchor True
        alpha 0.75
        xalign 0.85 yalign 0.4 # Dick Position
        zoom 0.585 rotate -50 xpos 0.58 ypos 0.25 # Masturbated
        block:
            parallel:
                ease 0.4 rotate -51
                ease 0.4 rotate -50
                repeat
            parallel:
                ease 0.42 xzoom 1.02
                ease 0.38 xzoom 0.993
                repeat
            parallel:
                ease 0.41 yzoom 1.02
                ease 0.39 yzoom 0.998
                repeat

### Neus Mast Hand

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("rubbing"), At("p_ao_cumInMouthAdult_n_handMast_idle", p_ao_cumInMouthAdult_n_handMast_t_rubbing),
            p_ao_action_Cond in ("cumming"), At("p_ao_cumInMouthAdult_n_handMast_t_cumming", truecenter),
            "True", Null())

    # contains:
    #     "p_ao_cumInMouthAdult_n_handMast_idle"
    #     truecenter
    #     alpha 0.75
    #     xpos 0.5 ypos 0.5 rotate 0 # Down
    #     # xpos 0.67 ypos 0.22 rotate -5 # High
    #     block:
    #         easein_quad 2.0 xpos 0.65 ypos 0.22 rotate -12 # High
    #         easeout_quad 2.0 xpos 0.5 ypos 0.5 rotate 0 # Down
    #         repeat


    # contains:
    #     ConditionSwitch(
    #         p_ao_action_Cond in ("slideDown"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_receiveMove),
    #         p_ao_action_Cond in ("cumFace"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_receive),
    #         p_ao_action_Cond in ("sucking", "suckDown", "suckUp"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_suck),
    #         "True", Null())

# MC BODY

    contains:
        "p_ao_cumInMouthAdult_mc_body"
        truecenter

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("rubbing"), At("p_ao_cumInMouthAdult_mc_legs", p_ao_cumInMouthAdult_mc_legs_trans),
            "True", At("p_ao_cumInMouthAdult_mc_legs", truecenter))




########################################################################################
########################################################################################
########################################################################################
########################################################################################




transform p_ao_cumInMouthAdult_move_NslideDown:
    subpixel True
    truecenter
    xpos 1.0
    pause 1.2
    easein_quad 1.0 xpos 0.5


transform p_ao_cumInMouthAdult_dick_receiveMove:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    zoom 0.585 rotate -90 xpos 0.6 ypos 0.25 # DickReceive
    pause 1.2
    ease 0.5 rotate -50
    parallel:
        easein_quad 0.5 yzoom 1.02
        easeout_quad 0.4 yzoom 0.99
        ease 0.6 yzoom 1.01
        easein_quad 0.3 yzoom 0.995
        repeat
    parallel:
        easein_quad 0.4 xzoom 0.999
        easeout_quad 0.5 xzoom 1.01
        ease 0.3 xzoom 0.998
        easein_quad 0.6 xzoom 1.02
        repeat

transform p_ao_cumInMouthAdult_dick_receive:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    zoom 0.585 rotate -50 xpos 0.6 ypos 0.25 # DickReceive
    parallel:
        easein_quad 0.5 yzoom 1.02
        easeout_quad 0.4 yzoom 0.99
        ease 0.6 yzoom 1.01
        easein_quad 0.3 yzoom 0.995
        repeat
    parallel:
        easein_quad 0.4 xzoom 0.999
        easeout_quad 0.5 xzoom 1.01
        ease 0.3 xzoom 0.998
        easein_quad 0.6 xzoom 1.02
        repeat

transform p_ao_cumInMouthAdult_dick_suck:
    subpixel True
    transform_anchor True
    xalign 0.85 yalign 0.4 # Dick Position
    zoom 0.585 rotate -80
    xpos 0.55 ypos 0.25 # Suck
    parallel:
        easein_quad 0.5 yzoom 1.02
        easeout_quad 0.4 yzoom 0.99
        ease 0.6 yzoom 1.01
        easein_quad 0.3 yzoom 0.995
        repeat
    parallel:
        easein_quad 0.4 xzoom 0.999
        easeout_quad 0.5 xzoom 1.01
        ease 0.3 xzoom 0.998
        easein_quad 0.6 xzoom 1.02
        repeat

image p_ao_cumInMouthAdult_nReceive_cum_comp:
    truecenter
    "empty"
    pause 0.5
    "p_ao_cumInMouthAdult_nReceive_cumSplash" with Dissolve(0.5)
    pause 0.5
    "p_ao_cumInMouthAdult_nReceive_cumOver" with Dissolve(0.5)

transform p_ao_cumInMouthAdult_mc_legs_trans:
    subpixel True
    truecenter
    alpha 0.5

image p_ao_cumInMouthAdult_nSuck_headSucking:
    "p_ao_cumInMouthAdult_nSuck_headUp"
    truecenter
    block:
        pause 4.0/p_ao_n_vel
        "p_ao_cumInMouthAdult_nSuck_headDown" with Dissolve(1.0/p_ao_n_vel)
        pause 4.0/p_ao_n_vel
        "p_ao_cumInMouthAdult_nSuck_headUp" with Dissolve(1.0/p_ao_n_vel)
        repeat

image p_ao_cumInMouthAdult_comp_01:

    contains:
        "bg_dark_a_blurry_02"
        truecenter
        zoom 3.5

# BED
    contains:
        "p_ao_cumInMouthAdult_bed"
        truecenter

# # NEUS Body
    
    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("slideDown"), At("p_ao_cumInMouthAdult_nReceive_body", p_ao_cumInMouthAdult_move_NslideDown),
            p_ao_action_Cond in ("cumFace"), At("p_ao_cumInMouthAdult_nReceive_body", truecenter),
            "True", At("p_ao_cumInMouthAdult_nSuck_body", truecenter))

## Cum

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("cumFace"), At("p_ao_cumInMouthAdult_nReceive_cum_comp", truecenter),
            "True", Null())

    # nArm

    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "armAss", At("p_ao_cumInMouthAdult_nSuck_armAss_below", truecenter),
            p_ao_action_Cond in ("slideDown"), At("p_ao_cumInMouthAdult_nReceive_armUp", p_ao_cumInMouthAdult_move_NslideDown),
            p_ao_action_Cond in ("cumFace"), At("p_ao_cumInMouthAdult_nReceive_armUp", truecenter),
            "True", At("p_ao_cumInMouthAdult_nSuck_armRest", truecenter))

# MC DICK

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("slideDown"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_receiveMove),
            p_ao_action_Cond in ("cumFace"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_receive),
            p_ao_action_Cond in ("sucking", "suckDown", "suckUp"), At("gensex_stan_mc_04_01_dick_01", p_ao_cumInMouthAdult_dick_suck),
            "True", Null())

# Neus Head:

    contains:
        ConditionSwitch(
            p_ao_action_Cond == "sucking", At("p_ao_cumInMouthAdult_nSuck_headSucking", truecenter),
            p_ao_action_Cond == "suckDown", At("p_ao_cumInMouthAdult_nSuck_headDown", truecenter),
            p_ao_action_Cond == "suckUp", At("p_ao_cumInMouthAdult_nSuck_headUp", truecenter),
            "True", Null())

    # nOver

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("slideDown"), At("p_ao_cumInMouthAdult_nReceive_over", p_ao_cumInMouthAdult_move_NslideDown),
            p_ao_action_Cond in ("sucking", "suckDown", "suckUp"), At("p_ao_cumInMouthAdult_nSuck_over", truecenter),
            "True", At("p_ao_cumInMouthAdult_nReceive_over", truecenter))

# MC BODY

    contains:
        "p_ao_cumInMouthAdult_mc_body"
        truecenter

    contains:
        ConditionSwitch(
            p_ao_action_Cond in ("sucking", "suckDown", "suckUp"), At("p_ao_cumInMouthAdult_mc_legs", p_ao_cumInMouthAdult_mc_legs_trans),
            "True", At("p_ao_cumInMouthAdult_mc_legs", truecenter))

# Neus Arm Over ass
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "armAss", At("p_ao_cumInMouthAdult_nSuck_armAss_over", truecenter),
            "True", Null())


########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

# oral position where you see her stomach coming and going. with your Dick being masturbated.

# gensex_oral_n_zextra_tongue_01
# or
# p_ao_sex_amazon_front_mc_body

transform p_ao_POVnFuckingYou_bg_pedrera:
    truecenter
    zoom 2.0

image p_ao_POVnFuckingYou:

    contains:
        ConditionSwitch(
            p_ao_background == "pedrera", At("bg_ped_04", p_ao_POVnFuckingYou_bg_pedrera),
            "True", At("gensex_oral_bg_grounddown", truecenter))

    # contains:
    #     "gensex_oral_bg_grounddown"
    #     truecenter

# Neus BODY.
    contains:
        "gensex_oral_n_ride_back_stand"
        subpixel True
        truecenter # Perfect
        ypos 0.909 zoom 0.88 #Back
        block:
            ease 4.0/p_ao_n_vel ypos 0.9 zoom 0.95 # Front
            ease 4.0/p_ao_n_vel ypos 0.909 zoom 0.85 #Back
            repeat
        

# Neus TONGUE
    contains:
        "p_ao_sex_amazon_front_n_tongue_l_02"
        subpixel True
        truecenter
        zoom 1.8 ypos 0.4 # Back
        block:
            ease 4.0/p_ao_n_vel zoom 2.0 ypos 0.3 # Front
            ease 4.0/p_ao_n_vel zoom 1.8 ypos 0.4 # Back
            repeat
        

## BED

    contains:
        "gensex_oral_bg_grounddownMiddle_extBed"
        truecenter



# MC DICK

    contains:
        "gensex_oral_mc_dick_01_wet_00"
        ped05_sex_oral_d_dick_o00_00

## TONGUE

    contains:
        "gensex_oral_n_zextra_tongue_03"
        p_ao_sex_oral_n_zextraTongue_tongue_03


# MC LEGS
    contains:
        "gensex_oral_mc_legs_up"
        truecenter
        ypos 0.65

## MC_Body

    # contains:
    #     "gensex_oral_mc_body_arms"
    #     truecenter
    #     ypos 0.65

    contains:
        "gensex_oral_mc_body_02"
        truecenter
        ypos 0.65
        
## MC_Chest
        
    contains:
        "gensex_oral_mc_chest"
        truecenter
        ypos 0.65

# SMOKE
    # contains:
    #     "night05_Cemetery_smoke_b_comp"
    #     p_ao_nride_smoke_BIGpos




########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################

########################################################################################
########################################################################################
########################################################################################
########################################################################################
## Ankles

# image p_ao_nRap_ankles_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_ankles_back.webp")
# image p_ao_nRap_ankles_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_ankles_front.webp")
image p_ao_nRap_ankles_02_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_ankles_02_back.webp")
image p_ao_nRap_ankles_02_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_ankles_02_front.webp")

image p_ao_nRap_ankles_02 general_comp_01:
# BG
    
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0
## Bodies
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_ankles_02_front", truecenter),
            "True", At("p_ao_nRap_ankles_02_back", truecenter))

## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

image p_ao_nRap_ankles_02 anim_comp_01:
# BG
    
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0
    contains:
        "p_ao_nRap_ankles_02_back"
        truecenter
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_ankles_02_front" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_ankles_02_back" with Dissolve(3.0/p_ao_n_vel)
            repeat
## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


########################################################################################
########################################################################################
## Doggy

#image p_ao_nRap_doggy_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_back.webp")
image p_ao_nRap_doggy_back_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_back_body.webp")
image p_ao_nRap_doggy_back_n_eyes_bright = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_back_n_eyes_bright.webp")
image p_ao_nRap_doggy_back_n_eyes_color = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_back_n_eyes_color.webp")


#image p_ao_nRap_doggy_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_front.webp")
image p_ao_nRap_doggy_front_body = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_front_body.webp")
image p_ao_nRap_doggy_front_n_eyes_bright = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_front_n_eyes_bright.webp")
image p_ao_nRap_doggy_front_n_eyes_color = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggy_front_n_eyes_color.webp")


transform p_ao_nRap_eyes_color:
    truecenter
    alpha ped_neus_whispers_sfx04

transform p_ao_nRap_eyes_bright:
    truecenter
    additive 1.0
    alpha ped_neus_whispers_sfx04

image p_ao_nRap_doggy general_comp_01:

# BG
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0

## Ghosts

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 2.5 xpos 0.5 ypos 0.4 # Center

## Bodies
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggy_front_body", truecenter),
            "True", At("p_ao_nRap_doggy_back_body", truecenter))

    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggy_front_n_eyes_color", p_ao_nRap_eyes_color),
            "True", At("p_ao_nRap_doggy_back_n_eyes_color", p_ao_nRap_eyes_color))

    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggy_front_n_eyes_bright", p_ao_nRap_eyes_bright),
            "True", At("p_ao_nRap_doggy_back_n_eyes_bright", p_ao_nRap_eyes_bright))

## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


############
######

image p_ao_nRap_doggy anim_comp_01:
# BG
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0
## Ghosts

    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 2.5 xpos 0.5 ypos 0.4 # Center
    ## Bodies
    contains:
        "p_ao_nRap_doggy_back_body"
        truecenter
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_front_body" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_back_body" with Dissolve(3.0/p_ao_n_vel)
            repeat
    # Eyes Color
    contains:
        "p_ao_nRap_doggy_back_n_eyes_color"
        truecenter
        alpha ped_neus_whispers_sfx04
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_front_n_eyes_color" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_back_n_eyes_color" with Dissolve(3.0/p_ao_n_vel)
            repeat
    # Eyes Bright
    contains:
        "p_ao_nRap_doggy_back_n_eyes_bright"
        truecenter
        additive 1.0
        alpha ped_neus_whispers_sfx04
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_front_n_eyes_bright" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggy_back_n_eyes_bright" with Dissolve(3.0/p_ao_n_vel)
            repeat
## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos


########################################################################################
########################################################################################
## DogyyHard


# image p_ao_nRap_doggyHard_back = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_back.webp")
# image p_ao_nRap_doggyHard_front = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_front.webp")

image p_ao_nRap_doggyHard_back_general = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_back_general.webp")
image p_ao_nRap_doggyHard_back_n_eyes_bright = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_back_n_eyes_bright.webp")
image p_ao_nRap_doggyHard_back_n_eyes_color = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_back_n_eyes_color.webp")
image p_ao_nRap_doggyHard_front_general = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_front_general.webp")
image p_ao_nRap_doggyHard_front_n_eyes_bright = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_front_n_eyes_bright.webp")
image p_ao_nRap_doggyHard_front_n_eyes_color = SaturateTint("images/day05/pedrera/afterOrgasm/p_ao_nRap_doggyHard_front_n_eyes_color.webp")


image p_ao_nRap_doggyHard general_comp_01:
# BG
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0
## Ghosts
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 2.5 xpos 0.5 ypos 0.4 # Center
## Bodies
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggyHard_front_general", truecenter),
            "True", At("p_ao_nRap_doggyHard_back_general", truecenter))
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggyHard_front_n_eyes_color", p_ao_nRap_eyes_color),
            "True", At("p_ao_nRap_doggyHard_back_n_eyes_color", p_ao_nRap_eyes_color))
    contains:
        ConditionSwitch(
            p_ao_action_b_Cond == "front", At("p_ao_nRap_doggyHard_front_n_eyes_bright", p_ao_nRap_eyes_bright),
            "True", At("p_ao_nRap_doggyHard_back_n_eyes_bright", p_ao_nRap_eyes_bright))
## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

############
######

#image p_ao_nRap_doggyHard_comp_01:
image p_ao_nRap_doggyHard anim_comp_01:

# BG
    contains:
        "bg_ped_04"
        truecenter
        zoom 3.0
## Ghosts
    contains:
        "p_ao_ghost_standing_comp"
        truecenter
        zoom 2.5 xpos 0.5 ypos 0.4 # Center

## Bodies

    contains:
        "p_ao_nRap_doggyHard_back_general"
        truecenter
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_front_general" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_back_general" with Dissolve(3.0/p_ao_n_vel)
            repeat
# Eyes Color
    contains:
        "p_ao_nRap_doggyHard_back_n_eyes_color"
        truecenter
        alpha ped_neus_whispers_sfx04
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_front_n_eyes_color" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_back_n_eyes_color" with Dissolve(3.0/p_ao_n_vel)
            repeat
# Eyes Bright
    contains:
        "p_ao_nRap_doggyHard_back_n_eyes_bright"
        truecenter
        additive 1.0
        alpha ped_neus_whispers_sfx04
        block:
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_front_n_eyes_bright" with Dissolve(3.0/p_ao_n_vel)
            pause 4.0/p_ao_n_vel
            "p_ao_nRap_doggyHard_back_n_eyes_bright" with Dissolve(3.0/p_ao_n_vel)
            repeat
## FOG
    contains:
        "night05_Cemetery_smoke_b_comp"
        p_ao_nride_smoke_pos

########################################################################################
########################################################################################

########################################################################################
########################################################################################

########################################################################################
########################################################################################

########################################################################################
########################################################################################

########################################################################################
########################################################################################

########################################################################################
########################################################################################


transform p_ao_smashTrans:
    additive 1.0
    alpha 0.0
    easein_quad 0.2 alpha 1.0
    easeout_quad 0.5 alpha 0.0


label p_ao_smashImage:

    $ randomnum_1to10 = renpy.random.randint(1, 10)

    show black03:
        alpha 0.0
        easein_quad 0.3 alpha 0.3
        easeout_quad 0.4 alpha 0.0

    if randomnum_1to10 == 1:
        show hit 15:
            p_ao_smashTrans
    elif randomnum_1to10 == 2:
        show hit 16:
            p_ao_smashTrans
    elif randomnum_1to10 == 3:
        show hit 17:
            p_ao_smashTrans
    elif randomnum_1to10 == 4:
        show hit 09:
            p_ao_smashTrans
    elif randomnum_1to10 == 5:
        show hit 10:
            p_ao_smashTrans
    elif randomnum_1to10 == 6:
        show hit 11:
            p_ao_smashTrans
    elif randomnum_1to10 == 7:
        show hit 01:
            p_ao_smashTrans
    elif randomnum_1to10 == 8:
        show hit 22:
            p_ao_smashTrans
    elif randomnum_1to10 == 9:
        show hit 03:
            p_ao_smashTrans
    elif randomnum_1to10 == 10:
        show hit 24:
            p_ao_smashTrans

    return