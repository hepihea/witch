#Images

#####################
####################



image image_prove = "images/image_prove.webp"

image part_empty = "images/sexbattle/dice_roll/part_empty.webp"
image circle_idle = "images/sexbattle/dice_roll/part_select.webp"

image part_empty_:

    contains:
        "images/sexbattle/dice_roll/part_hover.webp"
        alpha 0.01

image circle_hover:

    contains:

        "images/sexbattle/dice_roll/part_hover.webp"
        subpixel True
        easein_quad 2.0 alpha 0.1
        pause 0.5
        easeout_quad 3.0 alpha 1.0
        repeat

    contains:

        "images/sexbattle/dice_roll/part_hover.webp"
        alpha 0.5

        #"part_empty"

## EFFECTS
image afternight04_sexbattle_effects empty = "images/general/empty.webp"

image afternight04_sexbattle_effects white = "#fff"
image afternight04_sexbattle_effects black = "#000"

image afternight04_sexbattle_effects white_cumming:

    contains:
        "#fff"
        subpixel True
        additive 1.0
        alpha 0.0
        easein_quad 0.2 alpha 0.2
        easeout_quad 0.25 alpha 0.0
        easein_quad 0.3 alpha 0.5
        easeout_quad 0.3 alpha 0.0
        easein_quad 0.2 alpha 0.55
        easeout_quad 0.3 alpha 0.0
        easein_quad 0.5 alpha 1.0


image afternight04_sexbattle_effects newcondom:

    contains:
        "an04_Dgrabbingshirt_background"
        zoom 0.5
    contains:
        subpixel True
        "an04_holding_xxlcondom"
        zoom 1.0 xanchor 0.2 yanchor 0.0
        easein_quad 5.0 zoom 0.5 xanchor 0.0 yanchor 0.0
##

image but_grab = "images/sexbattle/dice_roll/but_grab.webp"

image but_hand = "images/sexbattle/dice_roll/but_hand.webp"

image but_fingers = "images/sexbattle/dice_roll/but_fingers.webp"

image but_pinch = "images/sexbattle/dice_roll/but_pinch.webp"

image but_splash = "images/sexbattle/dice_roll/but_splash.webp"

image but_tongue = "images/sexbattle/dice_roll/but_tongue.webp"

image but_dick = "images/sexbattle/dice_roll/but_dick.webp"

image but_forbidden = "images/sexbattle/dice_roll/but_forbidden.webp"

image but_remove = "images/sexbattle/dice_roll/but_remove.webp"

##

image but_grab_idle = im.MatrixColor("images/sexbattle/dice_roll/but_grab.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_hand_idle = im.MatrixColor("images/sexbattle/dice_roll/but_hand.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_fingers_idle = im.MatrixColor("images/sexbattle/dice_roll/but_fingers.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_pinch_idle = im.MatrixColor("images/sexbattle/dice_roll/but_pinch.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_splash_idle = im.MatrixColor("images/sexbattle/dice_roll/but_splash.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_tongue_idle = im.MatrixColor("images/sexbattle/dice_roll/but_tongue.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_dick_idle = im.MatrixColor("images/sexbattle/dice_roll/but_dick.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_forbidden_idle = im.MatrixColor("images/sexbattle/dice_roll/but_forbidden.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.
image but_remove_idle = im.MatrixColor("images/sexbattle/dice_roll/but_remove.webp",
                                                                                                        im.matrix.colorize("#000", "#fff")) #Black, #White.



image but_grab_hover = im.MatrixColor("images/sexbattle/dice_roll/but_grab.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_hand_hover = im.MatrixColor("images/sexbattle/dice_roll/but_hand.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_fingers_hover = im.MatrixColor("images/sexbattle/dice_roll/but_fingers.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_pinch_hover = im.MatrixColor("images/sexbattle/dice_roll/but_pinch.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_splash_hover = im.MatrixColor("images/sexbattle/dice_roll/but_splash.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_tongue_hover = im.MatrixColor("images/sexbattle/dice_roll/but_tongue.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_dick_hover = im.MatrixColor("images/sexbattle/dice_roll/but_dick.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_forbidden_hover = im.MatrixColor("images/sexbattle/dice_roll/but_forbidden.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.
image but_remove_hover = im.MatrixColor("images/sexbattle/dice_roll/but_remove.webp",
                                                                                                        im.matrix.colorize("#000", "#666")) #Black, #White.

## DICES

image dice_you = im.MatrixColor("images/sexbattle/premium_dashboard/dice10.webp",
                                                                                                        im.matrix.colorize("#000", "#399")) #Black, #White.
image dice_didac = im.MatrixColor("images/sexbattle/premium_dashboard/dice10.webp",
                                                                                                        im.matrix.colorize("#000", "#c63")) #Black, #White.


image dice_you_shine = im.MatrixColor("images/sexbattle/premium_dashboard/dice10_shine.webp",
                                                                                                        im.matrix.colorize("#000", "#399")) #Black, #White.
image dice_didac_shine = im.MatrixColor("images/sexbattle/premium_dashboard/dice10_shine.webp",
                                                                                                        im.matrix.colorize("#000", "#c63")) #Black, #White.


## ICON you
image icon_pleasure_you = im.MatrixColor("images/sexbattle/premium_dashboard/icon_pleasure.webp",
                                                                                                        im.matrix.colorize("#000", "#399")) #Black, #White.
image icon_orgasm_you = im.MatrixColor("images/sexbattle/premium_dashboard/icon_orgasm.webp",
                                                                                                        im.matrix.colorize("#000", "#399")) #Black, #White.

## ICON Didac
image icon_pleasure_didac = im.MatrixColor("images/sexbattle/premium_dashboard/icon_pleasure.webp",
                                                                                                        im.matrix.colorize("#000", "#c63"))
image icon_enslavery_didac = im.MatrixColor("images/sexbattle/premium_dashboard/icon_enslavery.webp",
                                                                                                        im.matrix.colorize("#000", "#c63"))
image icon_orgasm_didac = im.MatrixColor("images/sexbattle/premium_dashboard/icon_orgasm.webp",
                                                                                                        im.matrix.colorize("#000", "#c63"))

##Pleasure Bars

image bar_pleasure_you = im.MatrixColor("images/sexbattle/premium_dashboard/bar_pleasure_color.webp",
                                                                                                        im.matrix.colorize("#399", "#fff")) #Black, #White.
image bar_pleasure_didac = im.MatrixColor("images/sexbattle/premium_dashboard/bar_pleasure_color.webp",
                                                                                                        im.matrix.colorize("#c63", "#fff")) #Black, #White.

############################################################
###########################################################
############################################################
############################################## POSE 01

image afternight04_sexbattle_background_a = "images/sexbattle/d_pose01/afternight04_sexbattle_background_a.webp"
image afternight04_sexbattle_background a = "images/sexbattle/d_pose01/afternight04_sexbattle_background_a.webp"

image d_pose01 = "images/sexbattle/d_pose01/d_pose01.webp"
image d_pose02 = "images/sexbattle/d_pose02/d_pose02.webp"
image d_pose03 = "images/sexbattle/d_pose03/d_pose03.webp"


##### HIS CUMSHOT
image afternight04_sexbattle_mc_cumshot empty = "images/general/empty.webp"

image afternight04_sexbattle_mc_cumshot 01_a ="images/sexbattle/d_pose01/afternight04_sexbattle_mc_cumshot_01_a.webp"

##### HIS CUM a (on Stomach)

image afternight04_sexbattle_mc_cum_stomach empty = "images/general/empty.webp"

image afternight04_sexbattle_mc_cum_stomach just_01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_cum_stomach_just_01_a.webp"

image afternight04_sexbattle_mc_cum_stomach over_01-02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_cum_stomach_over_01-02_a.webp"

image afternight04_sexbattle_mc_cum_stomach over_01-02-03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_cum_stomach_over_01-02-03_a.webp"

##### HER CUM scene 01

image afternight04_sexbattle_didac_squirt 000_a = "images/general/empty.webp"
image afternight04_sexbattle_didac_squirt 01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_didac_squirt_01_a.webp"
image afternight04_sexbattle_didac_squirt 02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_didac_squirt_02_a.webp"
image afternight04_sexbattle_didac_squirt 03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_didac_squirt_03_a.webp"
image afternight04_sexbattle_didac_squirt 04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_didac_squirt_04_a.webp"


###
transform afternight04_sexbattle_didac_squirt_action_a:
    subpixel True
    xanchor 0.1218 yanchor -0.005 rotate 0 #Normal
    alpha 0.0
    easein_quad 0.5 alpha 1.0
###

image afternight04_sexbattle_didac_squirt 001_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 01_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 002_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 02_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 003_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 03_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 004_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 04_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 005_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 01_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 02_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 006_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 01_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 03_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 007_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 01_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 04_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 008_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 02_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 03_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 009_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 02_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 04_a"
        afternight04_sexbattle_didac_squirt_action_a

image afternight04_sexbattle_didac_squirt 010_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "afternight04_sexbattle_didac_squirt 03_a"
        afternight04_sexbattle_didac_squirt_action_a
    contains:
        "afternight04_sexbattle_didac_squirt 04_a"
        afternight04_sexbattle_didac_squirt_action_a

################################################
##############################################
############################################# SQUIRT B and C
##

transform afternight04_sexbattle_didac_squirt_position_b:
    xanchor 0.118 yanchor -0.01 rotate 0 #Normal

transform afternight04_sexbattle_didac_squirt_action_b:
    subpixel True
    xanchor 0.118 yanchor -0.01 rotate 0 #Normal
    alpha 0.0
    easein_quad 0.5 alpha 1.0
    easeout_quad 0.5 alpha 0.0

transform afternight04_sexbattle_didac_squirt_bed_disappearing_b:
    subpixel True
    xanchor 0.118 yanchor -0.01 rotate 0 #Normal
    alpha 1.0
    pause 1.2
    easein_quad 1.0 alpha 0.0

transform afternight04_sexbattle_didac_squirt_bed_appearing_b:
    subpixel True
    xanchor 0.118 yanchor -0.01 rotate 0 #Normal
    alpha 0.0
    pause 1.0
    easein_quad 1.0 alpha 1.0

###

# squirt 001_b

image afternight04_sexbattle_didac_squirt 001_b:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 01_b"
        afternight04_sexbattle_didac_squirt_action_b

image afternight04_sexbattle_didac_squirt_bed appearing_001_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 01_b"
        afternight04_sexbattle_didac_squirt_bed_appearing_b

# squirt 002_b

image afternight04_sexbattle_didac_squirt 002_b:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 02_b"
        afternight04_sexbattle_didac_squirt_action_b

image afternight04_sexbattle_didac_squirt_bed appearing_002_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 01_b"
        afternight04_sexbattle_didac_squirt_bed_disappearing_b

    contains:
        "afternight04_sexbattle_didac_squirt_bed 02_b"
        afternight04_sexbattle_didac_squirt_bed_appearing_b

# squirt 003_b

image afternight04_sexbattle_didac_squirt 003_b:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 03_b"
        afternight04_sexbattle_didac_squirt_action_b

image afternight04_sexbattle_didac_squirt_bed appearing_003_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 02_b"
        afternight04_sexbattle_didac_squirt_bed_disappearing_b

    contains:
        "afternight04_sexbattle_didac_squirt_bed 03_b"
        afternight04_sexbattle_didac_squirt_bed_appearing_b

# squirt 004_b

image afternight04_sexbattle_didac_squirt 004_b:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 04_b"
        afternight04_sexbattle_didac_squirt_action_b

image afternight04_sexbattle_didac_squirt_bed appearing_004_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 03_b"
        afternight04_sexbattle_didac_squirt_bed_disappearing_b

    contains:
        "afternight04_sexbattle_didac_squirt_bed 04_b"
        afternight04_sexbattle_didac_squirt_bed_appearing_b

# squirt 005_b

image afternight04_sexbattle_didac_squirt 005_b:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_didac_squirt 05_b"
        afternight04_sexbattle_didac_squirt_action_b

image afternight04_sexbattle_didac_squirt_bed appearing_005_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 04_b"
        afternight04_sexbattle_didac_squirt_bed_disappearing_b

    contains:
        "afternight04_sexbattle_didac_squirt_bed 05_b"
        afternight04_sexbattle_didac_squirt_bed_appearing_b


################################################
##############################################
#############################################
## SQUIERT_BED STATIC

image afternight04_sexbattle_didac_squirt_bed static_001_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 01_b"
        afternight04_sexbattle_didac_squirt_position_b

image afternight04_sexbattle_didac_squirt_bed static_002_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 02_b"
        afternight04_sexbattle_didac_squirt_position_b

image afternight04_sexbattle_didac_squirt_bed static_003_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 03_b"
        afternight04_sexbattle_didac_squirt_position_b

image afternight04_sexbattle_didac_squirt_bed static_004_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 04_b"
        afternight04_sexbattle_didac_squirt_position_b

image afternight04_sexbattle_didac_squirt_bed static_005_b:

    contains:
        "afternight04_sexbattle_didac_squirt_bed 05_b"
        afternight04_sexbattle_didac_squirt_position_b


################################################
##############################################
#############################################

################################################
##############################################
#############################################

##### BODY

## prove

image afternight04_sexbattle_d_body_prove a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_body_prove_a.webp"
image afternight04_sexbattle_prove_a = "images/sexbattle/d_pose01/afternight04_sexbattle_prove_a.webp"
image afternight04_sexbattle_prove_02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_prove_02_a.webp"

## MC dick

#pussy A
image afternight04_sexbattle_mc_dick_pussy empty = "images/general/empty.webp" # This is definetly Useful! POSE 02-03
image afternight04_sexbattle_mc_dick_pussy condom_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_dick_condom_wet_00_a.webp"
image afternight04_sexbattle_mc_dick_pussy naked_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_dick_naked_wet_00_a.webp"


#For Cumshot
image afternight04_sexbattle_mc_dick_pussy_cumshot empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_dick_pussy_cumshot naked_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_dick_naked_wet_00_a.webp"

#anal A
image afternight04_sexbattle_mc_dick_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_dick_anal condom_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_dick_condom_wet_00_a.webp"
image afternight04_sexbattle_mc_dick_anal naked_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_dick_naked_wet_00_a.webp"

## MC hands

image afternight04_sexbattle_smash boob_a = "images/sexbattle/d_pose01/afternight04_sexbattle_smash_boob_a.webp"


image afternight04_sexbattle_mc_handL empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_handL grab_boobR_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handL_grab_boobR_a.webp"
image afternight04_sexbattle_mc_handL grab_buttockR_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handL_grab_buttockR_a.webp"
image afternight04_sexbattle_mc_handL massage_belly_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handL_massage_belly_a.webp"
image afternight04_sexbattle_mc_handL massage_legR_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handL_massage_legR_a.webp"
image afternight04_sexbattle_mc_handL massage_stomach_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handL_massage_stomach_a.webp"


image afternight04_sexbattle_mc_handR empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_handR pinch_boobL_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_pinch_boobL_a.webp"

image afternight04_sexbattle_mc_handR grab_arm_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_grab_arm_a.webp"
image afternight04_sexbattle_mc_handR grab_arm_impact_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_grab_arm_impact_a.webp"
image afternight04_sexbattle_mc_handR grab_boobL_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_grab_boobL_a.webp"
image afternight04_sexbattle_mc_handR grab_buttockL_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_grab_buttockL_a.webp"
image afternight04_sexbattle_mc_handR massage_clitoris_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_massage_clitoris_a.webp"
image afternight04_sexbattle_mc_handR massage_legL_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_massage_legL_a.webp"

# PENETRATE

#image afternight04_sexbattle_mc_handR_penetrate empty = "images/general/empty.webp"
#image afternight04_sexbattle_mc_handR_penetrate a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_penetrate_a.webp"

image afternight04_sexbattle_mc_handR_penetrate_pussy empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_handR_penetrate_pussy a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_penetrate_a.webp"

image afternight04_sexbattle_mc_handR_penetrate_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_handR_penetrate_anal a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_handR_penetrate_a.webp"

## MC tongue_clitoris
image afternight04_sexbattle_mc_tongue_clitoris empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_tongue_clitoris down_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_down_a.webp"
image afternight04_sexbattle_mc_tongue_clitoris med_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_med_a.webp"
image afternight04_sexbattle_mc_tongue_clitoris up_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_up_a.webp"

image afternight04_sexbattle_mc_tongue_clitoris_down_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_down_a.webp"
image afternight04_sexbattle_mc_tongue_clitoris_med_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_med_a.webp"
image afternight04_sexbattle_mc_tongue_clitoris_up_a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_clitoris_up_a.webp"


## MC tongue_pussy

image afternight04_sexbattle_mc_tongue_pussy empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_tongue_pussy a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_pussy_a.webp"

## MC tongue_anal

image afternight04_sexbattle_mc_tongue_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_mc_tongue_anal a = "images/sexbattle/d_pose01/afternight04_sexbattle_mc_tongue_pussy_a.webp"

## boobL

image afternight04_sexbattle_d_boobL wet_00_smash_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_00_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_01_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_02_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_03_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_04_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_05_a.webp"
image afternight04_sexbattle_d_boobL wet_00_smash_06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobL_wet_00_smash_06_a.webp"

## boobR

image afternight04_sexbattle_d_boobR wet_00_smash_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_00_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_01_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_02_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_03_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_04_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_05_a.webp"
image afternight04_sexbattle_d_boobR wet_00_smash_06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_boobR_wet_00_smash_06_a.webp"

# legs Smashes

image afternight04_sexbattle_d_buttockL_smash 00_a = "images/general/empty.webp"
image afternight04_sexbattle_d_buttockL_smash 01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_01_a.webp"
image afternight04_sexbattle_d_buttockL_smash 02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_02_a.webp"
image afternight04_sexbattle_d_buttockL_smash 03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_03_a.webp"
image afternight04_sexbattle_d_buttockL_smash 04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_04_a.webp"
image afternight04_sexbattle_d_buttockL_smash 05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_05_a.webp"
image afternight04_sexbattle_d_buttockL_smash 06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockL_smash_06_a.webp"

image afternight04_sexbattle_d_buttockR_smash 00_a = "images/general/empty.webp"
image afternight04_sexbattle_d_buttockR_smash 01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_01_a.webp"
image afternight04_sexbattle_d_buttockR_smash 02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_02_a.webp"
image afternight04_sexbattle_d_buttockR_smash 03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_03_a.webp"
image afternight04_sexbattle_d_buttockR_smash 04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_04_a.webp"
image afternight04_sexbattle_d_buttockR_smash 05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_05_a.webp"
image afternight04_sexbattle_d_buttockR_smash 06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_buttockR_smash_06_a.webp"


## legs_over_pussy

image afternight04_sexbattle_d_legs_over_pussy empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_over_pussy 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_over_pussy_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_over_pussy_06_wet_00_a.webp"
image afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_over_pussy_06b_wet_00_a.webp"

## legs_over_anal

image afternight04_sexbattle_d_legs_over_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_over_anal  04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_over_anal_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_over_anal  06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_over_anal_06_wet_00_a.webp"

## legs top_pussy-anal

#image afternight04_sexbattle_d_legs_pussy 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_04_wet_00_a.webp"
#image afternight04_sexbattle_d_legs_pussy 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_06_wet_00_a.webp"

image afternight04_sexbattle_d_legs_top_pussy empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_top_pussy 02_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_02_wet_00_a.webp"
image afternight04_sexbattle_d_legs_top_pussy 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_top_pussy_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_top_pussy_06_wet_00_a.webp"
image afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_top_pussy_06b_wet_00_a.webp"

image afternight04_sexbattle_d_legs_top_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_top_anal 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_top_anal_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_top_anal 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_top_anal_06_wet_00_a.webp"

## legs_stomach PUSSY
image afternight04_sexbattle_d_legs_stomach_pussy empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_stomach_pussy wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_stomach_wet_00_a.webp"

## legs_stomach ANAL
image afternight04_sexbattle_d_legs_stomach_anal empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_stomach_anal  wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_stomach_wet_00_a.webp"

## legs

image afternight04_sexbattle_d_legs_base empty = "images/general/empty.webp"
image afternight04_sexbattle_d_legs_base wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_base_wet_00_a.webp"

image afternight04_sexbattle_d_legs_base PROVE_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_base_PROVE_a.webp"

image afternight04_sexbattle_d_legs empty = "images/general/empty.webp"
#image afternight04_sexbattle_d_legs wet_00_pussy_01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_wet_00_pussy_01_a.webp"
image afternight04_sexbattle_d_legs_pussy 01_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_01_wet_00_a.webp"
image afternight04_sexbattle_d_legs_pussy 02_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_02_wet_00_a.webp"
image afternight04_sexbattle_d_legs_pussy 03_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_03_wet_00_a.webp"
image afternight04_sexbattle_d_legs_pussy 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_pussy 05_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_05_wet_00_a.webp"
image afternight04_sexbattle_d_legs_pussy 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_pussy_06_wet_00_a.webp"

image afternight04_sexbattle_d_legs_anal 01_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_01_wet_00_a.webp"
image afternight04_sexbattle_d_legs_anal 02_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_02_wet_00_a.webp"
image afternight04_sexbattle_d_legs_anal 03_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_03_wet_00_a.webp"
image afternight04_sexbattle_d_legs_anal 04_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_04_wet_00_a.webp"
image afternight04_sexbattle_d_legs_anal 05_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_05_wet_00_a.webp"
image afternight04_sexbattle_d_legs_anal 06_wet_00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_legs_anal_06_wet_00_a.webp"

## body-face

image afternight04_sexbattle_d_body a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_body_a.webp"

## background

image afternight04_background_a = "images/sexbattle/d_pose01/afternight04_background_a.webp" 

############################################################
###########################################################

#### EXPRESSIONS

## hair

image afternight04_sexbattle_d_hair a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_hair_a.webp"

## eyebrows

image afternight04_sexbattle_d_eyebrows angryx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_angryx01_a.webp"
image afternight04_sexbattle_d_eyebrows angryx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_angryx02_a.webp"
image afternight04_sexbattle_d_eyebrows angryx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_angryx03_a.webp"
image afternight04_sexbattle_d_eyebrows angryx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_angryx04_a.webp"
image afternight04_sexbattle_d_eyebrows angryx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_angryx05_a.webp"

image afternight04_sexbattle_d_eyebrows normal_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_normal_a.webp"

image afternight04_sexbattle_d_eyebrows sadx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_sadx01_a.webp"
image afternight04_sexbattle_d_eyebrows sadx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_sadx02_a.webp"
image afternight04_sexbattle_d_eyebrows sadx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_sadx03_a.webp"
image afternight04_sexbattle_d_eyebrows sadx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_sadx04_a.webp"

image afternight04_sexbattle_d_eyebrows serious_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_serious_a.webp"

image afternight04_sexbattle_d_eyebrows surprisex01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_surprisex01_a.webp"
image afternight04_sexbattle_d_eyebrows surprisex02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_surprisex02_a.webp"

image afternight04_sexbattle_d_eyebrows suspiciousx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_suspiciousx01_a.webp"
image afternight04_sexbattle_d_eyebrows suspiciousx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyebrows_suspiciousx02_a.webp"

## pupils

image afternight04_sexbattle_d_pupils down00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down00_a.webp"
image afternight04_sexbattle_d_pupils down01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down01_a.webp"
image afternight04_sexbattle_d_pupils down02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down02_a.webp"
image afternight04_sexbattle_d_pupils down03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down03_a.webp"
image afternight04_sexbattle_d_pupils down04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down04_a.webp"
image afternight04_sexbattle_d_pupils down05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_down05_a.webp"

image afternight04_sexbattle_d_pupils front00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front00_a.webp"
image afternight04_sexbattle_d_pupils front01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front01_a.webp"
image afternight04_sexbattle_d_pupils front02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front02_a.webp"
image afternight04_sexbattle_d_pupils front03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front03_a.webp"
image afternight04_sexbattle_d_pupils front04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front04_a.webp"
image afternight04_sexbattle_d_pupils front05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_front05_a.webp"
image afternight04_sexbattle_d_pupils front06_a = "images/general/empty.webp"
image afternight04_sexbattle_d_pupils front07_a = "images/general/empty.webp"

image afternight04_sexbattle_d_pupils left00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left00_a.webp"
image afternight04_sexbattle_d_pupils left01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left01_a.webp"
image afternight04_sexbattle_d_pupils left02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left02_a.webp"
image afternight04_sexbattle_d_pupils left03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left03_a.webp"
image afternight04_sexbattle_d_pupils left04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left04_a.webp"
image afternight04_sexbattle_d_pupils left05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_left05_a.webp"

image afternight04_sexbattle_d_pupils right00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right00_a.webp"
image afternight04_sexbattle_d_pupils right01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right01_a.webp"
image afternight04_sexbattle_d_pupils right02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right02_a.webp"
image afternight04_sexbattle_d_pupils right03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right03_a.webp"
image afternight04_sexbattle_d_pupils right04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right04_a.webp"
image afternight04_sexbattle_d_pupils right05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_right05_a.webp"

image afternight04_sexbattle_d_pupils up00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up00_a.webp"
image afternight04_sexbattle_d_pupils up01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up01_a.webp"
image afternight04_sexbattle_d_pupils up02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up02_a.webp"
image afternight04_sexbattle_d_pupils up03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up03_a.webp"
image afternight04_sexbattle_d_pupils up04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up04_a.webp"
image afternight04_sexbattle_d_pupils up05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_pupils_up05_a.webp"

## eyes

image afternight04_sexbattle_d_eyes 00_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_00_a.webp"
image afternight04_sexbattle_d_eyes 01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_01_a.webp"
image afternight04_sexbattle_d_eyes 02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_02_a.webp"
image afternight04_sexbattle_d_eyes 03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_03_a.webp"
image afternight04_sexbattle_d_eyes 04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_04_a.webp"
image afternight04_sexbattle_d_eyes 05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_05_a.webp"
image afternight04_sexbattle_d_eyes 06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_06_a.webp"
image afternight04_sexbattle_d_eyes 07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_eyes_07_a.webp"

## mouth

image afternight04_sexbattle_d_mouth happy_Silentx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx01_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx02_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx03_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx04_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx05_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx06_a.webp"
image afternight04_sexbattle_d_mouth happy_Silentx07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Silentx07_a.webp"

image afternight04_sexbattle_d_mouth happy_Talkingx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx01_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx02_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx03_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx04_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx05_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx06_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx07_a.webp"
image afternight04_sexbattle_d_mouth happy_Talkingx08_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happy_Talkingx08_a.webp"

image afternight04_sexbattle_d_mouth happybiting_Silentx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx01_a.webp"
image afternight04_sexbattle_d_mouth happybiting_Silentx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx02_a.webp"
image afternight04_sexbattle_d_mouth happybiting_Silentx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx03_a.webp"
image afternight04_sexbattle_d_mouth happybiting_Silentx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx04_a.webp"
image afternight04_sexbattle_d_mouth happybiting_Silentx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx05_a.webp"
image afternight04_sexbattle_d_mouth happybiting_Silentx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_happybiting_Silentx06_a.webp"

image afternight04_sexbattle_d_mouth sad_Silentx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx01_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx02_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx03_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx04_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx05_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx06_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx07_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx08_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx08_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx09_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx09_a.webp"
image afternight04_sexbattle_d_mouth sad_Silentx10_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Silentx10_a.webp"

image afternight04_sexbattle_d_mouth sad_Talkingx001_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx001_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx002_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx002_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx003_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx003_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx004_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx004_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx005_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx005_a.webp"

image afternight04_sexbattle_d_mouth sad_Talkingx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx01_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx02_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx03_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx04_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx05_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx06_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx07_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx08_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx08_a.webp"
image afternight04_sexbattle_d_mouth sad_Talkingx09_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sad_Talkingx09_a.webp"

image afternight04_sexbattle_d_mouth sadbiting_Silentx01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx01_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx02_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx03_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx04_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx05_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx06_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx06_a.webp"
image afternight04_sexbattle_d_mouth sadbiting_Silentx07_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_mouth_sadbiting_Silentx07_a.webp"

## blush

image afternight04_sexbattle_d_blush 00_a = "images/general/empty.webp"
image afternight04_sexbattle_d_blush 01_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_blush_01_a.webp"
image afternight04_sexbattle_d_blush 02_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_blush_02_a.webp"
image afternight04_sexbattle_d_blush 03_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_blush_03_a.webp"
image afternight04_sexbattle_d_blush 04_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_blush_04_a.webp"
image afternight04_sexbattle_d_blush 05_a = "images/sexbattle/d_pose01/afternight04_sexbattle_d_blush_05_a.webp"



############################################################
########################################################### Empty

transform afternight04_sexbattle_empty_NOposition:
    subpixel False

############################################################
########################################################### Expressions

transform afternight04_sexbattle_d_expressions_pos:
    xanchor -0.955 yanchor 0.171

############################################################
########################################################### Pussy-Anal

transform afternight04_sexbattle_d_pubicpart_pos:
    xanchor -0.39 yanchor -0.67 rotate 0 zoom 1.0 xzoom 1.0 yzoom 1.0

############################################################
########################################################### Empty_action

transform afternight04_sexbattle_empty_position:
    xanchor 0.0 yanchor 0.0

############################################################
########################################################### CumShot a

image afternight04_sexbattle_mc_cumshot 01_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_cumshot 01_a"
        xanchor -0.09 yanchor -0.04 rotate 0 alpha 0.75 # Base Pose

############################################################
########################################################### Cum STOMACH a

    ## 1rst CUM
image afternight04_sexbattle_mc_cum_stomach just_01_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_cum_stomach just_01_a"
        xanchor -0.09 yanchor -0.04 rotate 0 alpha 0.75 # Base Pose

    ## 2nd CUM
image afternight04_sexbattle_mc_cum_stomach over_01-02_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_cum_stomach over_01-02_a"
        xanchor -0.09 yanchor -0.04 rotate 0 alpha 0.75 # Base Pose

    ## 3rd CUM
image afternight04_sexbattle_mc_cum_stomach over_01-02-03_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_cum_stomach over_01-02-03_a"
        xanchor -0.09 yanchor -0.04 rotate 0 alpha 0.75 # Base Pose

############################################################
########################################################### handL

    ## handL grab_boobR_a

image afternight04_sexbattle_mc_handL grab_boobR_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL grab_boobR_a"
    subpixel True
    xanchor -0.125 yanchor 0.075 rotate 0 # Start
    easein_quad 0.8 xanchor -0.13 yanchor 0.075 rotate 2 # 02
    easeout_quad 0.8 xanchor -0.12 yanchor 0.07 rotate -3 # 03
    easein_quad 0.8 xanchor -0.13 yanchor 0.075 rotate 4 # 04
    easeout_quad 0.8 xanchor -0.12 yanchor 0.07 rotate -1 # 03
    ease_quad 0.8 xanchor -0.125 yanchor 0.075 rotate 0 # Start
    repeat

    ## handL grab_buttockR_a

image afternight04_sexbattle_mc_handL grab_buttockR_action_a: # Not finished

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL grab_buttockR_a"
    subpixel True

    xanchor -0.0 yanchor -0.89 rotate 30 # Start
    easein_quad 1.5 xanchor -0.1 yanchor -0.9 rotate 0 # 01
    easeout_quad 1.5 xanchor -0.05 yanchor -0.85 rotate -25 # 02
    easein_quad 1.5 xanchor -0.1 yanchor -0.9 rotate -5 # 03
    easeout_quad 1.5 xanchor -0.0 yanchor -0.89 rotate 30 # Start
    repeat

    ## handL massage_belly_a

image afternight04_sexbattle_mc_handL massage_belly_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL massage_belly_a"
    subpixel True
    xanchor -0.22 yanchor -0.18 rotate 0 #Start
    easein_quad 1.0 xanchor -0.24 yanchor -0.17 rotate -10 #01
    easeout_quad 0.8 xanchor -0.21 yanchor -0.16 rotate 8 #02
    ease 0.5 xanchor -0.22 yanchor -0.18 rotate 0 #Start
    repeat

    ## handL mouth_Fingers

image afternight04_sexbattle_mc_handR massage_mouth_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL massage_belly_a"
    subpixel True
    xanchor -0.4 yanchor 0.16 rotate 0 zoom 0.85 xzoom -1.0 #Start
    easein_quad 2.0 rotate 5
    easein_quad 2.0 rotate -5
    easein_quad 2.0 rotate 0
    repeat

    ## handL massage_legR_a

image afternight04_sexbattle_mc_handL massage_legR_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL massage_legR_a"
    subpixel True

    xanchor 0.3 yanchor -0.58 rotate 0 #Up Start
    ease 3.0 xanchor 0.0 yanchor -0.8 rotate -10 #Down 01
    ease 3.0 xanchor 0.5 yanchor -0.35 rotate -20 #Up 02
    ease 3.0 xanchor 0.0 yanchor -0.7 rotate 30 #Down 02
    ease 3.0 xanchor 0.3 yanchor -0.58 rotate 0 #Up Start
    repeat

    ## handL massage_stomach_a

image afternight04_sexbattle_mc_handL massage_stomach_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handL massage_stomach_a"
    subpixel True

    xanchor -0.42 yanchor -0.3 rotate 0 #Start
    ease 3.0 xanchor -0.5 yanchor -0.3 zoom 1.05 rotate 30 # Down 01
    ease 3.0 xanchor -0.38 yanchor -0.25 zoom 0.95 rotate -30 # Up 01
    ease 3.0 xanchor -0.25 yanchor -0.38 zoom 1.05 rotate -20 # Down 02
    ease 3.0 xanchor -0.65 yanchor -0.25 zoom 0.95 rotate 15 # Up 02
    ease 3.0 xanchor -0.42 yanchor -0.3 rotate 0 #Start
    repeat

############################################################
########################################################### handR

    ## handR pinch_boobL_a

image afternight04_sexbattle_mc_handR pinch_boobL_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR pinch_boobL_a"
    subpixel True
    xanchor -0.76 yanchor 0.125 rotate 5
    easein_quad 1.0 rotate 15
    easeout_quad 1.0 rotate 5
    repeat

    ## handR pinch_boobL_c

image afternight04_sexbattle_mc_handR pinch_boobR_action_c:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_mc_handR pinch_boobL_a"
        subpixel True

        xanchor -0.72 yanchor -0.15 rotate 5

        block:
            easein_quad 1.0 rotate 15
            easeout_quad 1.0 rotate 5
            repeat

    ## handL pinch_boobR_a

image afternight04_sexbattle_mc_handL pinch_boobR_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_handR pinch_boobL_a"
        subpixel True
        xanchor -0.1 yanchor 0.05 rotate -25 xzoom -1.0
        easein_quad 1.0 rotate -35
        easeout_quad 1.0 rotate -25
        repeat


    ## handR grab_arm_a

image afternight04_sexbattle_mc_handR grab_arm_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_handR grab_arm_impact_a"
        subpixel True
        additive 0.5

        parallel:
            alpha 0.0
            ease 0.3 alpha 1.0
            easein_quad 0.5 alpha 0.0

        parallel:
            xanchor -1.5 yanchor -0.5 rotate 0 zoom 0.8 # Start Little
            linear 0.1 xanchor -1.085 yanchor -0.3 rotate 0 zoom 1.0 # Original Pose
            easeout_quad 0.2 xanchor -0.82 yanchor -0.17 rotate 0 zoom 1.2 # End Big

    contains:
        
        "afternight04_sexbattle_mc_handR grab_arm_a"
        xanchor -1.085 yanchor -0.3 rotate 0

    ## handR grab_boobL_a

image afternight04_sexbattle_mc_handR grab_boobL_action_a:
    
    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR grab_boobL_a"
    subpixel True
    xanchor -0.81 yanchor 0.1 rotate 0 # Start
    easein_quad 0.8 xanchor -0.82 yanchor 0.1 rotate 3 # 01
    easeout_quad 0.8 xanchor -0.8 yanchor 0.105 rotate -3 # 02
    easein_quad 0.8 xanchor -0.81 yanchor 0.1 rotate 1 # 03
    easeout_quad 0.8 xanchor -0.8 yanchor 0.105 rotate -5 # 04
    easein_quad 0.8 xanchor -0.81 yanchor 0.1 rotate 0 # Start
    repeat

    ## handR grab_buttockL_a

image afternight04_sexbattle_mc_handR grab_buttockL_action_a: #Not Finished

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR grab_buttockL_a"
    subpixel True
    xanchor -0.65 yanchor -0.63 rotate -20 # Start
    easein_quad 1.5 xanchor -0.6 yanchor -0.68 rotate 0 # 02
    easeout_quad 1.5 xanchor -0.55 yanchor -0.7 rotate 20 # 03
    easein_quad 1.5 xanchor -0.6 yanchor -0.68 rotate 3 # 04
    easeout_quad 1.5 xanchor -0.65 yanchor -0.63 rotate -20 # Start
    repeat

    ## handR massage_clitoris_a

image afternight04_sexbattle_mc_handR massage_clitoris_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR massage_clitoris_a"
    subpixel True

    xanchor -0.11 yanchor -0.315 rotate 0 #Start
    easein_quad 0.5 xanchor -0.1 yanchor -0.325 rotate 20 #02
    easeout_quad 0.5 xanchor -0.12 yanchor -0.32 rotate -5 #03
    easein_quad 0.5 xanchor -0.12 yanchor -0.34 rotate -20 #04
    easeout_quad 0.5 xanchor -0.11 yanchor -0.315 rotate 0 #Start
    ease 1.0 xanchor -0.1 yanchor -0.325 rotate 20 #02
    easeout 1.0 -0.12 yanchor -0.34 rotate -20 #04
    easein_quad 0.5 xanchor -0.11 yanchor -0.315 rotate 0 #Start
    repeat

    ## handR massage_legL_a

image afternight04_sexbattle_mc_handR massage_legL_action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR massage_legL_a"
    subpixel True

    xanchor -0.7 yanchor -0.315 rotate 10 #Start Down01
    ease 3.0 xanchor -1.1 yanchor 0.05 rotate -20 #Up01
    ease 3.0 xanchor -0.6 yanchor -0.4 rotate -40 #Down 02
    ease 3.0 xanchor -1.0 yanchor 0.01 rotate 0 #Up 02
    ease 3.0 xanchor -0.7 yanchor -0.315 rotate 10 #Start Down01
    repeat

############################################################
########################################################### tongue_licking

    ## tongue_clitoris

image afternight04_sexbattle_mc_tongue_clitoris action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        "afternight04_sexbattle_mc_tongue_clitoris_down_a"
        subpixel True
        xanchor -0.955 yanchor -1.235 rotate 0 
        parallel:
            easein 0.2 alpha 1.5
            easein 0.2 alpha 0.0
            easein 0.2 alpha 0.0
            repeat

    contains:

        "afternight04_sexbattle_mc_tongue_clitoris med_a"
        subpixel True
        xanchor -0.955 yanchor -1.235 rotate 0 alpha 0.5
        parallel:
            easein 0.2 alpha 0.0
            easein 0.2 alpha 1.5
            easein 0.2 alpha 0.0
            repeat

    contains:

        "afternight04_sexbattle_mc_tongue_clitoris_up_a"
        subpixel True
        xanchor -0.955 yanchor -1.235 rotate 0 alpha 0.5
        parallel:
            easein 0.2 alpha 0.0
            easein 0.2 alpha 0.0
            easein 0.2 alpha 1.5
            repeat

############################################################
########################################################### tongue_penetrating

    ## tongue_pussy

#image afternight04_sexbattle_mc_tongue_pussy action_a:  # DOES ONE HAS ANY USE?! NOT FINISHED

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    #"afternight04_sexbattle_mc_tongue_pussy a"
    #xanchor -0.11 yanchor -0.315 rotate 0

############################################################
########################################################### handR_penetrate

    ## handR_penetrate a

image afternight04_sexbattle_mc_handR_penetrate_pussy action_a:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    "afternight04_sexbattle_mc_handR_penetrate_pussy a"
    alpha 0.5
    #xanchor -0.11 yanchor -0.315 rotate 0 #Original
    xanchor -0.12 yanchor -0.3 rotate -5

############################################################
########################################################### boobL static

transform afternight04_sexbattle_d_boobL_a_static_pos:
    xanchor -0.67 yanchor -0.03 rotate 0 yzoom 1.0 xzoom 1.0 

image afternight04_sexbattle_d_boobL wet_00_smash_00_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_00_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_01_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_01_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_02_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_02_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_03_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_03_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_04_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_04_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_05_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_05_a"
    afternight04_sexbattle_d_boobL_a_static_pos

image afternight04_sexbattle_d_boobL wet_00_smash_06_a_static:
    
    "afternight04_sexbattle_d_boobL wet_00_smash_06_a"
    afternight04_sexbattle_d_boobL_a_static_pos

############################################################
########################################################### boobR static

transform afternight04_sexbattle_d_boobR_a_static_pos:
    xanchor -0.45 yanchor -0.071 rotate 0 yzoom 1.0 xzoom 1.0 

image afternight04_sexbattle_d_boobR wet_00_smash_00_a_static: 
    
    "afternight04_sexbattle_d_boobR wet_00_smash_00_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_01_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_01_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_02_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_02_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_03_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_03_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_04_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_04_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_05_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_05_a"
    afternight04_sexbattle_d_boobR_a_static_pos

image afternight04_sexbattle_d_boobR wet_00_smash_06_a_static:
    
    "afternight04_sexbattle_d_boobR wet_00_smash_06_a"
    afternight04_sexbattle_d_boobR_a_static_pos

############################################################
########################################################### BoobL smashed

transform afternight04_sexbattle_d_boobL_smash_action_a: #BoobL Squash-Strech.
    subpixel True

    xanchor -1.4 yanchor -0.2 rotate 10 zoom 0.3 alpha 0.0 additive 0.0 #Start
    linear 0.1 xanchor -0.49 yanchor 0.155 rotate 0 zoom 0.5 alpha 1.0 additive 0.7 #Medium
    easein_quad 0.2 xanchor -0.12 yanchor 0.23 rotate -20 zoom 0.7 alpha 0.0 additive 0.0 #End

transform afternight04_sexbattle_d_boobL_a_smashed_action: #BoobL Squash-Strech.
    subpixel True

    xanchor -0.67 yanchor -0.03 rotate 0 yzoom 1.0 xzoom 1.0 #Start
    ease 0.2 xanchor -0.65 yanchor -0.0 rotate -5 yzoom 1.2 xzoom 0.8 #Squash boobL
    ease 0.3 xanchor -0.68 yanchor -0.03 rotate 5 yzoom 0.9 xzoom 1.1 #Stretch boobL
    easein_bounce 0.5 xanchor -0.67 yanchor -0.03 rotate 0 yzoom 1.0 xzoom 1.0 #Start

transform afternight04_sexbattle_d_boob_smashed_appearing: #For boobL and boobR
    alpha 0.0
    pause 1.0
    easein_quad 3.0 alpha 1.0


    #Smashing boobL wet00 smash01

image afternight04_sexbattle_d_boobL wet_00_smash_01_a_smashed:
    
    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_00_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_01_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash02

image afternight04_sexbattle_d_boobL wet_00_smash_02_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_01_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_02_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash03

image afternight04_sexbattle_d_boobL wet_00_smash_03_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_02_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_03_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash04

image afternight04_sexbattle_d_boobL wet_00_smash_04_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_03_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_04_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash05

image afternight04_sexbattle_d_boobL wet_00_smash_05_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_04_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_05_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash06

image afternight04_sexbattle_d_boobL wet_00_smash_06_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_05_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_06_a_static" #New BoobL appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

    #Smashing boobL wet00 smash07

image afternight04_sexbattle_d_boobL wet_00_smash_07_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobL wet_00_smash_06_a" #BoobL Smashed
        afternight04_sexbattle_d_boobL_a_smashed_action

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobL_smash_action_a #~Smash L

############################################################
########################################################### BoobR smashed

transform afternight04_sexbattle_d_boobR_smash_action_a: #SMASH
    subpixel True
    xanchor -0.25 yanchor -0.35 rotate -30 xzoom -1.0 zoom 0.3 alpha 0.0 additive 0.0 #Start
    linear 0.1 xanchor -0.10 yanchor 0.15 rotate 5 xzoom -1.0 zoom 0.5 alpha 1.0 additive 0.7  #Med 
    easein_quad 0.2  xanchor -0.02 yanchor 0.22 rotate 40 xzoom -1.0 zoom 0.8 alpha 0.0 additive 0.0  #End


transform afternight04_sexbattle_d_boobR_a_smashed_action: #BoobR Squash-Strech.
    subpixel True

    xanchor -0.45 yanchor -0.071 rotate 0 yzoom 1.0 xzoom 1.0 #Start boob R
    ease 0.2 xanchor -0.46 yanchor -0.06 rotate 15 yzoom 1.2 xzoom 0.8 #Squash boobR
    ease 0.3 xanchor -0.43 yanchor -0.08 rotate -5 yzoom 0.9 xzoom 1.1 #Stretch boobR
    easein_bounce 0.5 xanchor -0.45 yanchor -0.071 rotate 0 yzoom 1.0 xzoom 1.0 #Start boob R


    #Smashing boobR wet00 smash01

image afternight04_sexbattle_d_boobR wet_00_smash_01_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_00_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_01_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash02

image afternight04_sexbattle_d_boobR wet_00_smash_02_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_01_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_02_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash03

image afternight04_sexbattle_d_boobR wet_00_smash_03_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_02_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_03_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash04

image afternight04_sexbattle_d_boobR wet_00_smash_04_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_03_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_04_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash05

image afternight04_sexbattle_d_boobR wet_00_smash_05_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_04_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_05_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash06

image afternight04_sexbattle_d_boobR wet_00_smash_06_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_05_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_06_a_static" #New BoobR appearing
        afternight04_sexbattle_d_boob_smashed_appearing

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

    #Smashing boobR wet00 smash07

image afternight04_sexbattle_d_boobR wet_00_smash_07_a_smashed:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:

        "afternight04_sexbattle_d_boobR wet_00_smash_06_a" #BoobR Smashed
        afternight04_sexbattle_d_boobR_a_smashed_action

    contains:

        "afternight04_sexbattle_smash boob_a"
        afternight04_sexbattle_d_boobR_smash_action_a #~Smash R

############################################################
########################################################### Scene d_Pussy empty

#image afternight04_sexbattle_mc_dick_pussy empty= "images/general/empty.webp" # This is definetly Useful! POSE 02-03

#image afternight04_sexbattle_mc_dick_pussy empty = "images/general/empty.webp" # POSE 01

image afternight04_sexbattle_mc_handR_penetrate_pussy empty = "images/general/empty.webp"

image afternight04_sexbattle_mc_tongue_pussy empty = "images/general/empty.webp"

############################################################
########################################################### Scene d_Anal empty                                  ANAL

image afternight04_sexbattle_mc_dick_anal empty= "images/general/empty.webp" # This is definetly Useful! POSE 02-03
image afternight04_sexbattle_mc_dick_anal empty = "images/general/empty.webp" # Is this useful? POSE 01

image afternight04_sexbattle_mc_handR_penetrate_anal empty = "images/general/empty.webp"

image afternight04_sexbattle_d_anal_finger empty = "images/general/empty.webp"
image afternight04_sexbattle_d_anal_tongue empty = "images/general/empty.webp" # This is useful.

############################################################
########################################################### Scene d_Pussy fingers

label afternight04_sexbattle_mc_handR_penetrate_pussy_starting_a:

    #if not (mc_body.store["dick"] == "Anal_dick_low"):
    show afternight04_sexbattle_d_legs_base:
        afternight04_sexbattle_empty_position

    show afternight04_sexbattle_d_legs_over_pussy empty:
        afternight04_sexbattle_empty_position

        # TIMON Y PUMBA

    show afternight04_sexbattle_d_legs_stomach_pussy empty:
        afternight04_sexbattle_empty_position


    show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
        afternight04_sexbattle_d_pubicpart_pos

    show afternight04_sexbattle_mc_handR_penetrate_pussy a:
        subpixel True
        xanchor -0.14 yanchor -0.38 rotate -10 #Tip
        block:
            easeout_quad 0.6 xanchor -0.135 yanchor -0.36 rotate -7 #Over_Tip
            easein_quad 0.6 xanchor -0.14 yanchor -0.38 rotate -10 #Tip
            repeat

    return


label afternight04_sexbattle_mc_handR_penetrate_pussy_action_a:

    if not (mc_body.store["dick"] == "Anal_dick_low"):
        show afternight04_sexbattle_d_legs_base:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_position

        # TIMON Y PUMBA

    show afternight04_sexbattle_d_legs_stomach_pussy empty:
        afternight04_sexbattle_empty_position


    show afternight04_sexbattle_d_legs_pussy 04_wet_00_a:
        afternight04_sexbattle_d_pubicpart_pos

    show afternight04_sexbattle_mc_handR_penetrate_pussy a:
        subpixel True
        xanchor -0.14 yanchor -0.38 rotate -10 #Tip
        block:
            easeout_quad 0.3 xanchor -0.133 yanchor -0.34 rotate -5 #Med
            easein_quad 0.3 xanchor -0.13 yanchor -0.3 rotate -3 #Deep
            easeout_quad 0.3 xanchor -0.133 yanchor -0.34 rotate -5 #Med
            easein_quad 0.3 xanchor -0.14 yanchor -0.38 rotate -10 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_pussy 04_wet_00_a

    show afternight04_sexbattle_d_legs_top_pussy 04_wet_00_a: #SHAZUM
        subpixel True
        xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
        block:
            easeout_quad 0.3 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
            easein_quad 0.3 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 1.0 yzoom 0.98  #Deep
            easeout_quad 0.6 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
            repeat

    return

############################################################
########################################################### Scene d_Anal fingers                                   ANAL

label afternight04_sexbattle_mc_handR_penetrate_anal_starting_a:

    show afternight04_sexbattle_mc_handR_penetrate_anal a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

        xanchor -0.17 yanchor -0.48 rotate -10 #Tip
        block:
            easeout_quad 0.6 xanchor -0.17 yanchor -0.46 rotate -8 #OverTip
            easein_quad 0.6 xanchor -0.17 yanchor -0.48 rotate -10 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_anal  empty:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

    show afternight04_sexbattle_d_legs_top_pussy 02_wet_00_a:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
        afternight04_sexbattle_d_pubicpart_pos


    show afternight04_sexbattle_d_legs_top_anal empty: # SHAZAM
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

    return

label afternight04_sexbattle_mc_handR_penetrate_anal_action_a:

    show afternight04_sexbattle_mc_handR_penetrate_anal a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

        xanchor -0.17 yanchor -0.48 rotate -10 #Tip
        block:
            easeout_quad 0.3 xanchor -0.16 yanchor -0.43 rotate -5 #Med
            easein_quad 0.3 xanchor -0.165 yanchor -0.38 rotate 3 #Deep
            easeout_quad 0.3 xanchor -0.16 yanchor -0.43 rotate -5 #Med
            easein_quad 0.3 xanchor -0.17 yanchor -0.48 rotate -10 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_anal  04_wet_00_a:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

    #show afternight04_sexbattle_d_legs_top_pussy 02_wet_00_a:
        #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
        #afternight04_sexbattle_d_pubicpart_pos


    show afternight04_sexbattle_d_legs_top_anal 04_wet_00_a: # SHAZAM
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

        xanchor -0.43 yanchor -0.73 rotate 0 xzoom 0.93 yzoom 1.0 #Tip
        block:
            easeout_quad 0.3 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip
            easein_quad 0.3 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 1.0 yzoom 0.98  #Deep
            easeout_quad 0.6 xanchor -0.43 yanchor -0.73 rotate 0 xzoom 0.93 yzoom 1.0 #Tip
            repeat

    return


############################################################
########################################################### Scene d_Pussy tongue

label afternight04_sexbattle_mc_tongue_pussy_starting_a:

    show afternight04_sexbattle_d_legs_pussy 02_wet_00_a

    show afternight04_sexbattle_mc_tongue_pussy a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        xanchor -0.47 yanchor -0.83 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        block:
            easein_quad 3.0 xanchor -0.47 yanchor -0.85 rotate 0 xzoom 1.0 yzoom 0.88 # Below Tip
            easeout_quad 4.0 xanchor -0.47 yanchor -0.83 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_pussy empty:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    show afternight04_sexbattle_d_legs_top_pussy empty:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    return

label afternight04_sexbattle_mc_tongue_pussy_action_a:

    show afternight04_sexbattle_mc_tongue_pussy a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        xanchor -0.47 yanchor -0.83 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        block:
            easeout_quad 0.5 xanchor -0.455 yanchor -0.73 rotate 5 xzoom 0.95 yzoom 0.95 #Med
            easein_quad 0.5 xanchor -0.44 yanchor -0.67 rotate -5 xzoom 0.88 yzoom 1.0 #Deep
            easeout_quad 0.5 xanchor -0.455 yanchor -0.73 rotate 5 xzoom 0.95 yzoom 0.95 #Med
            easein_quad 0.5 xanchor -0.47 yanchor -0.83 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_pussy 04_wet_00_a:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    show afternight04_sexbattle_d_legs_top_pussy 04_wet_00_a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
        block:
            easeout_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
            easein_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 1.0 yzoom 0.98  #Deep
            easeout_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
            easein_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Tip #Correct
            repeat

    return

############################################################
########################################################### Scene d_Anal tongue

label afternight04_sexbattle_mc_tongue_anal_starting_a:

    show afternight04_sexbattle_mc_tongue_anal a: #No need for MC ANAL
        subpixel True

        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        block:
            easeout_quad 3.0 xanchor -0.515 yanchor -0.99 rotate 0 xzoom 1.0 yzoom 0.88 # Below Tip
            easein_quad 0.5 xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
            repeat

    show afternight04_sexbattle_d_legs_over_anal  empty:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    show afternight04_sexbattle_d_legs_top_anal empty:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to

    return

label afternight04_sexbattle_mc_tongue_anal_action_a:

    show afternight04_sexbattle_mc_tongue_anal a: #No need for MC ANAL
        subpixel True

        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        block:
            easeout_quad 0.5 xanchor -0.51 yanchor -0.87 rotate 5 xzoom 0.95 yzoom 0.95 #Med
            easein_quad 0.5 xanchor -0.485 yanchor -0.8 rotate -5 xzoom 0.88 yzoom 1.0 #Deep
            easeout_quad 0.5 xanchor -0.51 yanchor -0.87 rotate 5 xzoom 0.95 yzoom 0.95 #Med
            easein_quad 0.5 xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
            repeat


    #show afternight04_sexbattle_d_legs_top_pussy 02_wet_00_a:
        #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
        #afternight04_sexbattle_d_pubicpart_pos


    show afternight04_sexbattle_d_legs_over_anal  04_wet_00_a:
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    #show afternight04_sexbattle_d_legs_top_anal 04_wet_00_a:

        #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

        #xanchor -0.46 yanchor -0.77 rotate 0 zoom 0.93 #Tip
        #easeout_quad 0.5 xanchor -0.41 yanchor -0.7 rotate -1 zoom 0.975 #Med
        #easein_quad 0.5 xanchor -0.39 yanchor -0.66 rotate 0 zoom 1.0 #Deep
        #easeout_quad 0.5 xanchor -0.41 yanchor -0.7 rotate -1 zoom 0.975 #Med
        #easein_quad 0.5 xanchor -0.46 yanchor -0.77 rotate 0 zoom 0.93 #Tip
        #repeat

    show afternight04_sexbattle_d_legs_top_anal 04_wet_00_a:
        subpixel True
        afternight04_sexbattle_empty_position # puts xanchor and yanchor to 

        xanchor -0.43 yanchor -0.73 rotate 0 xzoom 0.93 yzoom 1.0 #Tip
        block:
            easeout_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Med
            easein_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 1.0 yzoom 0.98  #Deep
            easeout_quad 0.5 xanchor -0.4 yanchor -0.679 rotate 0 xzoom 0.98 yzoom 1.0 #Med
            easein_quad 0.5 xanchor -0.43 yanchor -0.73 rotate 0 xzoom 0.93 yzoom 1.0 #Tip
            repeat


    return


#image afternight04_sexbattle_mc_tongue_anal action_a: NOT FINISHED, DELETE THIS.

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    #contains:
    
        #"afternight04_sexbattle_mc_tongue_pussy a" #No need for MC ANAL

        #xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        #easeout_quad 0.5 xanchor -0.51 yanchor -0.87 rotate 5 xzoom 0.95 yzoom 0.95 #Med
        #easein_quad 0.5 xanchor -0.485 yanchor -0.8 rotate -5 xzoom 0.88 yzoom 1.0 #Deep
        #easeout_quad 0.5 xanchor -0.51 yanchor -0.87 rotate 5 xzoom 0.95 yzoom 0.95 #Med
        #easein_quad 0.5 xanchor -0.515 yanchor -0.97 rotate 0 xzoom 1.0 yzoom 0.88 #Tip
        #repeat

    #contains:

        #"afternight04_sexbattle_d_legs_over_anal  04_wet_00_a" #Correct

    #contains:
        #"afternight04_sexbattle_d_legs_top_anal 04_wet_00_a" #Correct

        ###xanchor -0.435 yanchor -0.73 rotate 0 zoom 0.95 #Tip #Original Tip
        #xanchor -0.46 yanchor -0.77 rotate 0 zoom 0.93 #Tip
        #easeout_quad 0.5 xanchor -0.41 yanchor -0.7 rotate -1 zoom 0.975 #Med
        #easein_quad 0.5 xanchor -0.39 yanchor -0.66 rotate 0 zoom 1.0 #Deep
        #easeout_quad 0.5 xanchor -0.41 yanchor -0.7 rotate -1 zoom 0.975 #Med
        #easein_quad 0.5 xanchor -0.46 yanchor -0.77 rotate 0 zoom 0.93 #Tip
        #repeat

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # PUSSY DICK TRANSFORM


############################################################
###########################################################
############################################################
########################################################### TRANSFORM DICK

    ## DICK DEEP

transform afternight04_sexbattle_d_pussy_dick_deep_stop_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 3.0 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 5.0 xanchor 0.239 yanchor 0.225 rotate 0 zoom 0.515# Deep

transform afternight04_sexbattle_d_pussy_dick_deep_slow_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 2.0 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 2.0 xanchor 0.239 yanchor 0.225 rotate 0 zoom 0.515# Deep
    easeout_quad 2.0 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 2.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_deep_mod_action: # moderate
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6 # Tip
    easeout_quad 0.2 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 0.5 xanchor 0.239 yanchor 0.225 rotate 0 zoom 0.515# Deep
    easeout_quad 0.2 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 0.5 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_deep_fast_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 0.04 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 0.1 xanchor 0.239 yanchor 0.225 rotate 0 zoom 0.515# Deep
    easeout_quad 0.04 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easein_quad 0.1 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

    ## DICK MED

transform afternight04_sexbattle_d_pussy_dick_med_stop_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 3.0 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 5.0 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med

transform afternight04_sexbattle_d_pussy_dick_med_slow_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 2.0 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 2.0 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easeout_quad 2.0 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 2.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_med_mod_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 0.2 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 0.5 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easeout_quad 0.2 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 0.5 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_med_fast_action:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 0.03 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 0.1 xanchor 0.238 yanchor 0.19 rotate 0 zoom 0.54# Med
    easeout_quad 0.03 xanchor 0.247 yanchor 0.19 rotate 1  zoom 0.57 # Semi-Med
    easein_quad 0.1 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    repeat

    ## DICK LOW

transform afternight04_sexbattle_d_pussy_dick_low_stop_action:
    subpixel True
    xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip 
    easeout_quad 3.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 5.0 xanchor 0.255 yanchor 0.14 rotate 3  zoom 0.6 # Over_Tip

transform afternight04_sexbattle_d_pussy_dick_low_slow_action:
    subpixel True
    xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip 
    easeout_quad 2.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 2.0 xanchor 0.255 yanchor 0.14 rotate 3  zoom 0.6 # Over_Tip
    easeout_quad 2.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 2.0 xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_low_mod_action:
    subpixel True
    xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip 
    easeout_quad 1.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 1.0 xanchor 0.255 yanchor 0.14 rotate 3  zoom 0.6 # Over_Tip
    easeout_quad 1.0 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 1.0 xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_low_fast_action:
    subpixel True
    xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip 
    easeout_quad 0.15 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 0.15 xanchor 0.255 yanchor 0.14 rotate 3  zoom 0.6 # Over_Tip
    easeout_quad 0.15 xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easein_quad 0.15 xanchor 0.255 yanchor 0.13 rotate -6 zoom 0.63 # Previous_Tip # Previous_Tip
    repeat

transform afternight04_sexbattle_d_pussy_dick_out_stop_action:
    xanchor 0.255 yanchor 0.0 rotate 0 zoom 0.63 # Offscreen

############################################################
###########################################################
############################################################
########################################################### TRANSFORM STOMACH

    ## STOMACH DEEP

transform afternight04_sexbattle_d_pussy_stomach_deep_stop_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 3.0 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 5.0 xpos 0.37 ypos 0.435 rotate -3 xzoom 0.9 yzoom 1.2 #Deep

transform afternight04_sexbattle_d_pussy_stomach_deep_slow_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 2.0 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 2.0 xpos 0.37 ypos 0.435 rotate -3 xzoom 0.9 yzoom 1.2 #Deep
    easeout_quad 2.0 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 2.0 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_stomach_deep_mod_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 0.2 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 0.5 xpos 0.37 ypos 0.435 rotate -3 xzoom 0.9 yzoom 1.2 #Deep
    easeout_quad 0.2 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 0.5 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_stomach_deep_fast_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 0.04 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 0.1 xpos 0.37 ypos 0.435 rotate -3 xzoom 0.9 yzoom 1.2 #Deep
    easeout_quad 0.04 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easein_quad 0.1 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

    ## STOMACH MED

transform afternight04_sexbattle_d_pussy_stomach_med_stop_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 3.0 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 5.0 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med

transform afternight04_sexbattle_d_pussy_stomach_med_slow_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 2.0 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 2.0 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 2.0 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 2.0 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_stomach_med_mod_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 0.2 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 0.5 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 0.2 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 0.5 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_stomach_med_fast_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    easeout_quad 0.03 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 0.1 xpos 0.39 ypos 0.52 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 0.03 xpos 0.4 ypos 0.55 rotate 3 xzoom 0.9 yzoom 0.5 # Semi-Med
    easein_quad 0.1 xpos 0.405 ypos 0.635 rotate 3 xzoom 0.8 yzoom 0.1 #Tip
    repeat

    ## STOMACH LOW
transform afternight04_sexbattle_d_pussy_stomach_low_stop_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_stomach_low_slow_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_stomach_low_mod_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_stomach_low_fast_action:
    alpha 0.0

############################################################
###########################################################
############################################################
########################################################### TRANSFORM PUSSY

    ## PUSSY DEEP

transform afternight04_sexbattle_d_pussy_deep_stop_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 3.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 5.0 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
transform afternight04_sexbattle_d_pussy_deep_slow_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 2.0 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 2.0 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_pussy_deep_mod_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.2 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.5 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 0.2 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.5 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_pussy_deep_fast_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.04 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.1 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 0.04 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.1 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat

## PUSSY MED

transform afternight04_sexbattle_d_pussy_med_stop_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 3.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 5.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med

transform afternight04_sexbattle_d_pussy_med_slow_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 2.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 2.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 2.0 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_pussy_med_mod_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.2 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.5 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 0.2 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.5 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_pussy_med_fast_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.03 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.1 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 0.03 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.1 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat

## PUSSY LOW

transform afternight04_sexbattle_d_pussy_low_stop_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_low_slow_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_low_mod_action:
    alpha 0.0
transform afternight04_sexbattle_d_pussy_low_fast_action:
    alpha 0.0

############################################################
###########################################################
############################################################
########################################################### TRANSFORM LEGS
## LEGS DEEP

transform afternight04_sexbattle_d_pussy_legs_deep_stop_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 3.0 yanchor 0.0 # Med
    easein_quad 5.0 yanchor 0.01 # Deep
    easein_quad 10.0 yanchor 0.0 #Tip

transform afternight04_sexbattle_d_pussy_legs_deep_slow_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 2.0 yanchor 0.0 # Med
    easein_quad 2.0 yanchor 0.01 # Deep
    easeout_quad 2.0 yanchor 0.0# Med
    easein_quad 2.0 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_legs_deep_mod_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.2 yanchor 0.0 # Med
    easein_quad 0.5 yanchor 0.01 # Deep
    easeout_quad 0.2 yanchor 0.0# Med
    easein_quad 0.5 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_legs_deep_fast_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.04 yanchor 0.0 # Med
    easein_quad 0.1 yanchor 0.01 # Deep
    easeout_quad 0.04 yanchor 0.0# Med
    easein_quad 0.1 yanchor 0.0 #Tip
    repeat



## LEGS MED
transform afternight04_sexbattle_d_pussy_legs_med_stop_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 3.0 yanchor 0.0 # Semi-Med
    easein_quad 5.0 yanchor 0.005 #Med
    easeout_quad 10.0 yanchor 0.0 #Tip

transform afternight04_sexbattle_d_pussy_legs_med_slow_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 2.0 yanchor 0.0 # Semi-Med
    easein_quad 2.0 yanchor 0.005 #Med
    easeout_quad 2.0 yanchor 0.0# Semi-Med
    easein_quad 2.0 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_legs_med_mod_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.2 yanchor 0.0 # Semi-Med
    easein_quad 0.5 yanchor 0.005 #Med
    easeout_quad 0.2 yanchor 0.0# Semi-Med
    easein_quad 0.5 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_legs_med_fast_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.03 yanchor 0.0 # Semi-Med
    easein_quad 0.1 yanchor 0.005 #Med
    easeout_quad 0.03 yanchor 0.0# Semi-Med
    easein_quad 0.1 yanchor 0.0 #Tip
    repeat

## LEGS LOW
transform afternight04_sexbattle_d_pussy_legs_low_stop_action:
    yanchor 0.0

############################################################
###########################################################
############################################################
########################################################### TRANSFORM PUBIC
## PUBIC DEEP

transform afternight04_sexbattle_d_pussy_pubic_deep_stop_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 3.0 yanchor -0.67 # Med
    easein_quad 5.0 yanchor -0.658 # Deep
    easein_quad 10.0 yanchor -0.67 #Tip

transform afternight04_sexbattle_d_pussy_pubic_deep_slow_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 2.0 yanchor -0.67 # Med
    easein_quad 2.0 yanchor -0.658 # Deep
    easeout_quad 2.0 yanchor -0.67# Med
    easein_quad 2.0 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_pubic_deep_mod_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 0.2 yanchor -0.67 # Med
    easein_quad 0.5 yanchor -0.658 # Deep
    easeout_quad 0.2 yanchor -0.67 # Med
    easein_quad 0.5 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_pubic_deep_fast_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 0.04 yanchor -0.67 # Med
    easein_quad 0.1 yanchor -0.658 # Deep
    easeout_quad 0.04 yanchor -0.67 # Med
    easein_quad 0.1 yanchor -0.67 #Tip
    repeat

## PUBIC MED

transform afternight04_sexbattle_d_pussy_pubic_med_stop_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 3.0 yanchor -0.67 # Semi-Med
    easein_quad 5.0 yanchor -0.665 #Med
    easeout_quad 10.0 yanchor -0.67 #Tip

transform afternight04_sexbattle_d_pussy_pubic_med_slow_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 2.0  yanchor -0.67 # Semi-Med
    easein_quad 2.0 yanchor -0.665 #Med
    easeout_quad 2.0 yanchor -0.67 # Semi-Med
    easein_quad 2.0 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_pubic_med_mod_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.2 yanchor -0.67 # Semi-Med
    easein_quad 0.5 yanchor -0.665 #Med
    easeout_quad 0.2 yanchor -0.67 # Semi-Med
    easein_quad 0.5 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_pussy_pubic_med_fast_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.03 yanchor -0.67 # Semi-Med
    easein_quad 0.1 yanchor -0.665 #Med
    easeout_quad 0.03 yanchor -0.67 # Semi-Med
    easein_quad 0.1 yanchor -0.67 #Tip
    repeat

## PUBIC LOW
transform afternight04_sexbattle_d_pussy_pubic_low_stop_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 3.0 yanchor -0.665 # Tip
    easein_quad 5.0 yanchor -0.67 # Previous_Tip-original

transform afternight04_sexbattle_d_pussy_pubic_low_slow_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 2.0 yanchor -0.66 # Tip
    easein_quad 2.0 yanchor -0.67 # Previous_Tip-original
    easeout_quad 2.0 yanchor -0.665 # Tip
    easein_quad 2.0 yanchor -0.67 # Previous_Tip-original
    repeat

transform afternight04_sexbattle_d_pussy_pubic_low_mod_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 1.0 yanchor -0.66 # Tip
    easein_quad 1.0 yanchor -0.67 # Previous_Tip-original
    easeout_quad 1.0 yanchor -0.665 # Tip
    easein_quad 1.0 yanchor -0.67 # Previous_Tip-original
    repeat

transform afternight04_sexbattle_d_pussy_pubic_low_fast_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.15 yanchor -0.66 # Tip
    easein_quad 0.15 yanchor -0.67 # Previous_Tip-original
    easeout_quad 0.15 yanchor -0.665 # Tip
    easein_quad 0.15 yanchor -0.67 # Previous_Tip-original
    repeat





############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # PUSSY DICK_a POSE 01 SCENE

label afternight04_sexbattle_mc_dick_pussy_pose01_scene:

### DICK OUT

    if mc_body.store["dick"] == "Pussy_dick_out":

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_legs_base wet_00_a :
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_out_stop_action

            # HIDING

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                    afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_d_legs_over_pussy empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_stomach_pussy empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_top_pussy empty:
                    afternight04_sexbattle_d_pubicpart_pos

### DICK LOW

    elif mc_body.store["dick"] == "Pussy_dick_low":

        # HIDING

        show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_stomach_pussy empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_top_pussy empty:
                afternight04_sexbattle_d_pubicpart_pos


        # DICK

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_stop_action

        if mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_slow_action

        if mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_mod_action

        if mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_fast_action

        # LEGS

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_legs_base wet_00_a :
                afternight04_sexbattle_d_pussy_legs_low_stop_action

        # PUBIC PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_fast_action


### DICK MED

    elif mc_body.store["dick"] == "Pussy_dick_med":


        # PUBIC PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_fast_action


        # LEGS

        if current_pose.id == "pose_1":

            if mc_body.dick_speed == 0:

                #show afternight04_sexbattle_d_legs_base PROVE_a:
                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_stop_action

            elif mc_body.dick_speed == 1:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_slow_action

            elif mc_body.dick_speed == 2:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_mod_action

            elif mc_body.dick_speed == 3:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_fast_action

        # DICK

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_stop_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_slow_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_mod_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_fast_action

        # STOMACH

        if mc_body.dick_speed == 0:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_stop_action

        elif mc_body.dick_speed == 1:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                #alpha 0.9
                afternight04_sexbattle_d_pussy_stomach_med_slow_action

        elif mc_body.dick_speed == 2:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_mod_action

        elif mc_body.dick_speed == 3:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_fast_action

        # LEGS_OVER_PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_med_stop_action 

        if mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
                #alpha 0.2
                afternight04_sexbattle_d_pussy_legs_med_slow_action 

        if mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_med_mod_action 

        if mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_med_fast_action 


        # LEGS_TOP_PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                #alpha 0.2
                afternight04_sexbattle_d_pussy_med_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_fast_action

### DICK DEEP

    elif mc_body.store["dick"] == "Pussy_dick_deep":

        # DICK PUSSY DEEP

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_stop_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_slow_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_mod_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_fast_action

        # STOMACH PUSSY DEEP

        if mc_body.dick_speed == 0:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_stop_action

        elif mc_body.dick_speed == 1:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                #alpha 0.9
                afternight04_sexbattle_d_pussy_stomach_deep_slow_action

        elif mc_body.dick_speed == 2:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_mod_action

        elif mc_body.dick_speed == 3:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_fast_action

        # LEGS_OVER_PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_deep_stop_action 

        if mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
                #alpha 0.2
                afternight04_sexbattle_d_pussy_legs_deep_slow_action 

        if mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_deep_mod_action 

        if mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_deep_fast_action 

        # LEGS_TOP_PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                #alpha 0.2
                afternight04_sexbattle_d_pussy_deep_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_fast_action


        # PUBIC PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                #alpha 0.2
                afternight04_sexbattle_d_pussy_pubic_deep_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_fast_action

        # LEGS

        if current_pose.id == "pose_1":

            if mc_body.dick_speed == 0:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_stop_action

            elif mc_body.dick_speed == 1:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    #alpha 0.2
                    afternight04_sexbattle_d_pussy_legs_deep_slow_action

            elif mc_body.dick_speed == 2:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_mod_action

            elif mc_body.dick_speed == 3:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_fast_action


    return

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # PUSSY DICK DOGGYSTYLE TRANSFORM


############################################################
###########################################################
############################################################
########################################################### TRANSFORM DICK

    ## DICK DEEP

transform afternight04_sexbattle_mc_dick_pussy_deep_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    #xanchor -0.0035 yanchor -0.52 rotate 0 # Out
    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    ease_quad 5.0 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep

transform afternight04_sexbattle_mc_dick_pussy_deep_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.4 rotate 0 # Half
        repeat

transform afternight04_sexbattle_mc_dick_pussy_deep_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.27 rotate 0 # Deep
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.4 rotate 0 # Half
        repeat

transform afternight04_sexbattle_mc_dick_pussy_deep_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.23 rotate 0 # Deep
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.45 rotate 0 # Half-bitless
        repeat

    ## DICK MED

transform afternight04_sexbattle_mc_dick_pussy_med_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.52 rotate 0 # Out
    ease_quad 5.0 xanchor -0.0035 yanchor -0.4 rotate 0 # Half

transform afternight04_sexbattle_mc_dick_pussy_med_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.49 rotate 0 # Not Totally Out
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.35 rotate 0 # Half-bitmore
        repeat

transform afternight04_sexbattle_mc_dick_pussy_med_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.49 rotate 0 # Not Totally Out
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.27 rotate 0 # Half-bitmore
        repeat

transform afternight04_sexbattle_mc_dick_pussy_med_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.49 rotate 0 # Not Totally Out
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.2 rotate 0 # Half-bitmore
        repeat

    ## DICK LOW

transform afternight04_sexbattle_mc_dick_pussy_low_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.75 rotate 0 # OffScreen
    easein_quad 5.0 xanchor -0.0035 yanchor -0.51 rotate 0 #Tip

transform afternight04_sexbattle_mc_dick_pussy_low_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.51 rotate 0 #Tip
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.46 rotate 0 # 
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.5 rotate 0 #
        repeat

transform afternight04_sexbattle_mc_dick_pussy_low_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.51 rotate 0 #Tip
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.44 rotate 0 # 
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.5 rotate 0 #
        repeat

transform afternight04_sexbattle_mc_dick_pussy_low_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.51 rotate 0 #Tip
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.4 rotate 0 # # It goes below Pussy.
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.5 rotate 0 #
        repeat

transform afternight04_sexbattle_mc_dick_pussy_offscreen_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # # It goes below Pussy
    easein_quad 1.0 xanchor -0.0035 yanchor -0.85 rotate 0 #Offscreen


############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # PUSSY DICK_b-c

#image afternight04_sexbattle_mc_dick_pussy general_doggystyle ## WRONG


## PUSSY_OVER 001

image afternight04_sexbattle_d_legs_over_pussy 001_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 01_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 02_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 003_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 03_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 004_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 04_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 005_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 05_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 005b_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 05b_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 006_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 06_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 007_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 008_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 08_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 009_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 09_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 010_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 10_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 011_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 11_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_over_pussy 012_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_over_pussy 12_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos


## PUSSY 001

image afternight04_sexbattle_d_legs_pussy 001_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 01_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 002_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 02_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 003_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 03_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 004_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 04_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 005_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 05_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 005b_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 05b_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 006_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 06_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 007_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 07_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 008_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 08_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 009_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 09_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 010_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 10_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 011_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 11_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

image afternight04_sexbattle_d_legs_pussy 012_wet_00_b:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "afternight04_sexbattle_d_legs_pussy 12_wet_00_b"
        afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

#################################################
################################################
###############################################

transform afternight04_sexbattle_d_legs_pussy_stop_pubic_pos:  # Pubic
    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    xanchor -1.13 yanchor -1.83 rotate 0

transform afternight04_sexbattle_d_legs_pussy_stop_frame_pos: #Legs
    xanchor -0.58 yanchor -0.73 rotate 0

#################################################
################################################
###############################################

label afternight04_sexbattle_mc_dick_Pussy_general_doggystyle_scene:

    ## DICK OUT

    if (mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == ""):

        show afternight04_sexbattle_d_legs_pussy_below 02_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy 001_wet_00_b

        #show afternight04_sexbattle_d_legs_over_pussy empty:
            #afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_mc_dick_pussy empty

    ## DICK DEEP

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 0):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy 007_wet_00_b


        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b:  ## DICK DEEP STOP
            afternight04_sexbattle_mc_dick_pussy_deep_stop_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy deep_slow_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 09_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block:    
                    ease 0.5 alpha 0.0 # 7 seconds
                    pause 5.0
                    ease 0.5 alpha 1.0
                    pause 1.0
                    repeat


            contains:

                "afternight04_sexbattle_d_legs_over_pussy 10_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block:    
                    pause 0.5
                    ease 0.5 alpha 0.0 # 7 seconds
                    pause 5.5
                    ease 0.5 alpha 1.0
                    pause 0.0
                    repeat

        #easein_quad 4.0 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep
        #easeout_quad 3.0 xanchor -0.0035 yanchor -0.4 rotate 0 # Half
        #repeat

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b:  ## DICK DEEP SLOW
            afternight04_sexbattle_mc_dick_pussy_deep_slow_action_b # 7 seconds

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos


        show afternight04_sexbattle_d_legs_over_pussy deep_mod_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 08_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 09_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds // 0.7 seconds
                    pause 0.1
                    ease 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    linear 0.1 alpha 1.0
                    pause 0.1
                    repeat


                    #pause 0.2
                    #ease 0.25 alpha 1.0
                    #pause 0.1
                    #ease 0.1 alpha 0.0
                    #pause 0.05
                    #repeat
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 10_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds
                    pause 0.1
                    linear 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    ease 0.1 alpha 1.0
                    repeat

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 11_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds
                    linear 0.1 alpha 1.0
                    ease 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    repeat

        #easein_quad 1.0 xanchor -0.0035 yanchor -0.27 rotate 0 # Deep
        #easeout_quad 0.75 xanchor -0.0035 yanchor -0.4 rotate 0 # Half

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b:  ## DICK DEEP MOD
            afternight04_sexbattle_mc_dick_pussy_deep_mod_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos


        show afternight04_sexbattle_d_legs_over_pussy deep_fast_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 08_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 10_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block: # 0.35 seconds // 0.3 seconds
                    pause 0.05
                    pause 0.05
                    linear 0.05 alpha 0.0
                    pause 0.05
                    pause 0.05
                    linear 0.05 alpha 1.0
                    repeat

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 12_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0
                block: # 0.35 seconds
                    pause 0.05
                    linear 0.05 alpha 0.0
                    pause 0.05
                    pause 0.05
                    pause 0.05
                    linear 0.05 alpha 1.0
                    repeat

        #easein_quad 0.25 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep
        #easeout_quad 0.1 xanchor -0.0035 yanchor -0.35 rotate 0 # Half-bitmore

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b:  ## DICK DEEP FAST
            afternight04_sexbattle_mc_dick_pussy_deep_fast_action_b

    ## DICK MED

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 0):


        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy med_stop_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 06_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0 # 5 seconds

                pause 2.0
                ease 0.5 alpha 1.0
                pause 0.5
                ease 0.5 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 05_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0 # 5 seconds

                pause 1.25
                ease 0.5 alpha 1.0
                pause 0.5
                ease 0.5 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 01_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 1.0 # 5 seconds

                pause 1.5
                ease 1.0 alpha 0.0

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK MED STOP
            afternight04_sexbattle_mc_dick_pussy_med_stop_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy med_slow_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 05_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0

                block:# 7 seconds

                    pause 2.0
                    ease 0.5 alpha 1.0
                    pause 3.0
                    ease 0.5 alpha 0.0
                    pause 1.0
                    repeat

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK MED SLOW
            afternight04_sexbattle_mc_dick_pussy_med_slow_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy med_mod_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 05_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0

                block:# 1.75 seconds // 0.7 seconds
                    pause 0.2
                    ease 0.25 alpha 1.0
                    pause 0.1
                    ease 0.1 alpha 0.0
                    pause 0.05
                    repeat

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK MED MOD
            afternight04_sexbattle_mc_dick_pussy_med_mod_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_d_legs_pussy_below 07_wet_00_b:
            afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_over_pussy med_fast_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_over_pussy 07_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 05_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos
                alpha 0.0

                block:# 0.6 seconds // 0.3 seconds
                    pause 0.0
                    ease 0.2 alpha 1.0
                    pause 0.0
                    ease 0.05 alpha 0.0
                    pause 0.05
                    repeat

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK MED FAST
            afternight04_sexbattle_mc_dick_pussy_med_fast_action_b

    ## DICK LOW

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0):

        show afternight04_sexbattle_d_legs_over_pussy low_stop_b:

            contains:
                "afternight04_sexbattle_d_legs_over_pussy 05b_wet_00_b"
                afternight04_sexbattle_d_legs_pussy_stop_pubic_pos

        show afternight04_sexbattle_d_legs_pussy_below empty

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK LOW STOP
            afternight04_sexbattle_mc_dick_pussy_low_stop_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK LOW SLOW 
            afternight04_sexbattle_mc_dick_pussy_low_slow_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2):

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK LOW MOD
            afternight04_sexbattle_mc_dick_pussy_low_mod_action_b

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b: ## DICK LOW FAST
            afternight04_sexbattle_mc_dick_pussy_low_fast_action_b

    return


#################################################
################################################
###############################################

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # ANAL DICK_b-c

## ANAL

image afternight04_sexbattle_d_legs_anal 001_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 01_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 002_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 02_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 003_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 03_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 004_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 04_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 005_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 05_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 005b_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 05b_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 006_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 06_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 007_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 07_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 008_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 08_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 009_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 09_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 010_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 10_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 011_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 11_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal 012_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal 12_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

## ANAL_OVER 00

image afternight04_sexbattle_d_legs_anal_over 001_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 01_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 002_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 02_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 003_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 03_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 004_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 04_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 005_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 05_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 005b_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 05b_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 006_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 06_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 007_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 07_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 008_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 08_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 009_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 09_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 010_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 10_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 011_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 11_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

image afternight04_sexbattle_d_legs_anal_over 012_wet_00_b:

    contains:
        "afternight04_sexbattle_d_legs_anal_over 12_wet_00_b"
        afternight04_sexbattle_d_legs_anal_stop_pubic_pos

############################################################
###########################################################
############################################################
########################################################### TRANSFORM ANAL DICK

    ## DICK DEEP

transform afternight04_sexbattle_mc_dick_anal_deep_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    ease_quad 5.0 xanchor -0.0035 yanchor -0.23 rotate 0 # Deep

transform afternight04_sexbattle_mc_dick_anal_deep_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.4 rotate 0 # Half
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.23 rotate 0 # Deep
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.39 rotate 0 # Half
        repeat

transform afternight04_sexbattle_mc_dick_anal_deep_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.39 rotate 0 # Half
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.22 rotate 0 # Deep
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.39 rotate 0 # Half
        repeat

transform afternight04_sexbattle_mc_dick_anal_deep_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.38 rotate 0 # Half
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.21 rotate 0 # Deep
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.39 rotate 0 # Half-bitless
        repeat

    ## DICK MED

transform afternight04_sexbattle_mc_dick_anal_med_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.45 rotate 0 # Out
    ease_quad 5.0 xanchor -0.0035 yanchor -0.35 rotate 0 # Half

transform afternight04_sexbattle_mc_dick_anal_med_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.34 rotate 0 # Half
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.4 rotate 0 # Not Totally Out
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.32 rotate 0 # Half-bitmore
        repeat

transform afternight04_sexbattle_mc_dick_anal_med_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.34 rotate 0 # Half
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.4 rotate 0 # Not Totally Out
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.27 rotate 0 # Half-bitmore
        repeat

transform afternight04_sexbattle_mc_dick_anal_med_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.34 rotate 0 # Half
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.4 rotate 0 # Not Totally Out
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.25 rotate 0 # Half-bitmore
        repeat

    ## DICK LOW

transform afternight04_sexbattle_mc_dick_anal_low_stop_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.75 rotate 0 # OffScreen
    easein_quad 5.0 xanchor -0.0035 yanchor -0.458 rotate 0 # ANAL Tip

transform afternight04_sexbattle_mc_dick_anal_low_slow_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.47 rotate 0 #Tip
    block:
        easein_quad 4.0 xanchor -0.0035 yanchor -0.452 rotate 0 # 
        easeout_quad 3.0 xanchor -0.0035 yanchor -0.47 rotate 0 #
        repeat

transform afternight04_sexbattle_mc_dick_anal_low_mod_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.51 rotate 0 #Tip
    block:
        easein_quad 0.5 xanchor -0.0035 yanchor -0.45 rotate 0 # 
        easeout_quad 0.2 xanchor -0.0035 yanchor -0.47 rotate 0 #
        repeat

transform afternight04_sexbattle_mc_dick_anal_low_fast_action_b:
    subpixel True

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    xanchor -0.0035 yanchor -0.51 rotate 0 #Tip
    block:
        easein_quad 0.2 xanchor -0.0035 yanchor -0.445 rotate 0 # # It goes below Pussy.
        easeout_quad 0.1 xanchor -0.0035 yanchor -0.48 rotate 0 #
        repeat


#############
############

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # ANAL DICK_b-c SCENE

transform afternight04_sexbattle_d_legs_anal_stop_frame_pos:
    xanchor -0.58 yanchor -0.73 rotate 0
        

transform afternight04_sexbattle_d_legs_anal_stop_pubic_pos:
    xanchor -1.13 yanchor -1.83 rotate 0
        

label afternight04_sexbattle_mc_dick_Anal_general_doggystyle_scene:

    ## DICK OUT

    if (mc_body.store["dick"] == "Anal_dick_out" or mc_body.store["dick"] == ""):

        show afternight04_sexbattle_mc_dick_pussy empty
        show afternight04_sexbattle_mc_dick_anal empty

    ## DICK DEEP

    elif (mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 0):


        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b:  ## DICK DEEP STOP
            afternight04_sexbattle_mc_dick_anal_deep_stop_action_b

    elif (mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_d_legs_anal_over deep_slow_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_anal_over 07_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_anal_over 09_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block:    
                    ease 0.5 alpha 0.0 # 7 seconds
                    pause 5.0
                    ease 0.5 alpha 1.0
                    pause 1.0
                    repeat


            contains:

                "afternight04_sexbattle_d_legs_anal_over 10_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block:    
                    pause 0.5
                    ease 0.5 alpha 0.0 # 7 seconds
                    pause 5.5
                    ease 0.5 alpha 1.0
                    pause 0.0
                    repeat

        #easein_quad 4.0 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep
        #easeout_quad 3.0 xanchor -0.0035 yanchor -0.4 rotate 0 # Half
        #repeat

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b:  ## DICK DEEP SLOW
            afternight04_sexbattle_mc_dick_anal_deep_slow_action_b # 7 seconds

    elif (mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 2):


        show afternight04_sexbattle_d_legs_anal_over deep_mod_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            
            contains:

                "afternight04_sexbattle_d_legs_anal_over 08_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_anal_over 09_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds // 0.7
                    pause 0.1
                    ease 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    ease 0.1 alpha 1.0
                    pause 0.1
                    repeat

            contains:

                "afternight04_sexbattle_d_legs_anal_over 10_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds
                    pause 0.1
                    ease 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    ease 0.1 alpha 1.0
                    repeat

            contains:

                "afternight04_sexbattle_d_legs_anal_over 11_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block: # 1.75 seconds
                    ease 0.1 alpha 1.0
                    ease 0.1 alpha 0.0
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    pause 0.1
                    repeat

        #easein_quad 1.0 xanchor -0.0035 yanchor -0.27 rotate 0 # Deep
        #easeout_quad 0.75 xanchor -0.0035 yanchor -0.4 rotate 0 # Half

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b:  ## DICK DEEP MOD
            afternight04_sexbattle_mc_dick_anal_deep_mod_action_b

    elif (mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_d_legs_anal_over deep_fast_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

            contains:

                "afternight04_sexbattle_d_legs_anal_over 08_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos

            contains:

                "afternight04_sexbattle_d_legs_anal_over 10_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block: # 0.35 seconds // 0.3
                    pause 0.05
                    ease 0.05 alpha 0.0
                    pause 0.05
                    pause 0.05
                    ease 0.05 alpha 1.0
                    pause 0.05
                    repeat

            contains:

                "afternight04_sexbattle_d_legs_anal_over 12_wet_00_b"
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                block: # 0.35 seconds
                    ease 0.05 alpha 1.0
                    ease 0.05 alpha 0.0
                    pause 0.05
                    pause 0.05
                    pause 0.05
                    pause 0.05
                    repeat

        #easein_quad 0.25 xanchor -0.0035 yanchor -0.28 rotate 0 # Deep
        #easeout_quad 0.1 xanchor -0.0035 yanchor -0.35 rotate 0 # Half-bitmore

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b:  ## DICK DEEP FAST
            afternight04_sexbattle_mc_dick_anal_deep_fast_action_b

    ## DICK MED

    elif (mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 0):

        show afternight04_sexbattle_d_legs_pussy_below empty #These are necessary here.
        show afternight04_sexbattle_d_legs_over_pussy empty

        show afternight04_sexbattle_d_legs_anal med_stop_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

            contains:

                "afternight04_sexbattle_d_legs_over_pussy 05b_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 1.0
                pause 1.0
                easeout_quad 0.6 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_anal 04_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 1.0
                pause 0.5
                easeout_quad 0.6 alpha 0.0
            
            contains:

                "afternight04_sexbattle_d_legs_anal 05_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                pause 0.5
                easein_quad 0.5 alpha 1.0
                easeout_quad 0.6 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_anal 07_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0
                pause 1.0
                easein_quad 0.5 alpha 1.0

        show afternight04_sexbattle_d_legs_anal_over med_stop_b:

            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

            ## WHERE´S THE PUSSY? Here or should be in another place?
        
            contains:

                "afternight04_sexbattle_d_legs_anal_over 05_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 1.0 # 5 seconds
                pause 2.0
                easeout_quad 0.6 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_anal_over 06_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0 # 5 seconds

                pause 2.0
                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.6 alpha 0.0

            contains:

                "afternight04_sexbattle_d_legs_anal_over_07_wet_00_b"
                subpixel True
                afternight04_sexbattle_d_legs_anal_stop_pubic_pos
                alpha 0.0 # 5 seconds

                pause 3.0
                easein_quad 0.5 alpha 1.0


        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK MED STOP
            afternight04_sexbattle_mc_dick_anal_med_stop_action_b

    elif (mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK MED SLOW
            afternight04_sexbattle_mc_dick_anal_med_slow_action_b

    elif (mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 2):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK MED MOD
            afternight04_sexbattle_mc_dick_anal_med_mod_action_b

    elif (mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK MED FAST
            afternight04_sexbattle_mc_dick_anal_med_fast_action_b

    ## DICK LOW

    elif (mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 0):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK ANAL LOW STOP
            afternight04_sexbattle_mc_dick_anal_low_stop_action_b

    elif (mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 1):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK ANAL LOW SLOW 
            afternight04_sexbattle_mc_dick_anal_low_slow_action_b

    elif (mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 2):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK ANAL LOW MOD
            afternight04_sexbattle_mc_dick_anal_low_mod_action_b

    elif (mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 3):

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b: ## DICK ANAL LOW FAST
            afternight04_sexbattle_mc_dick_anal_low_fast_action_b

    return

#############
############

######################################################################################################################################################
#####################################################################################################################################################
####################################################################################################################################################
     ## DICK PUSSY RAPE

############################################################
###########################################################
############################################################
########################################################### TRANSFORM RAPE DICK

    ## DICK RAPE_DEEP

transform afternight04_sexbattle_d_pussy_dick_deep_stop_rape_action:

    xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_Deep_TopHigh_DEEP

transform afternight04_sexbattle_d_pussy_dick_deep_slow_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_Deep_TopHigh_DEEP
    pause 3.0
    easein_quad 1.0 xanchor 0.21 yanchor 0.2 rotate 13 zoom 0.515# Rape_TopLow_DEEP
    easeout_quad 1.0 xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_TopHighw_DEEP
    pause 3.0
    repeat

transform afternight04_sexbattle_d_pussy_dick_deep_mod_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_Deep_TopHigh_DEEP
    pause 1.5
    easein_quad 0.5 xanchor 0.21 yanchor 0.2 rotate 13 zoom 0.515# Rape_TopLow_DEEP
    easeout_quad 0.5 xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_TopHighw_DEEP
    pause 1.5
    repeat

transform afternight04_sexbattle_d_pussy_dick_deep_fast_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_Deep_TopHigh_DEEP
    pause 0.15
    easein_quad 0.15 xanchor 0.21 yanchor 0.18 rotate 13 zoom 0.515# Rape_TopLow_DEEP
    easein_bounce 0.3 xanchor 0.21 yanchor 0.21 rotate 13 zoom 0.515# Rape_TopHighw_DEEP
    repeat

    ## DICK RAPE_MED

transform afternight04_sexbattle_d_pussy_dick_med_stop_rape_action:
    
    xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED

transform afternight04_sexbattle_d_pussy_dick_med_slow_rape_action:
    subpixel True
    
    xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    pause 3.0
    easein_quad 1.0 xanchor 0.21 yanchor 0.155 rotate 13 zoom 0.515# Rape_TopBelow_MED
    easeout_quad 1.0 xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    pause 3.0
    repeat

transform afternight04_sexbattle_d_pussy_dick_med_mod_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    pause 1.5
    easein_quad 0.5 xanchor 0.21 yanchor 0.155 rotate 13 zoom 0.515# Rape_TopBelow_MED
    easeout_quad 0.5 xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    pause 1.5
    repeat

transform afternight04_sexbattle_d_pussy_dick_med_fast_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    pause 0.15
    easein_quad 0.15 xanchor 0.21 yanchor 0.155 rotate 13 zoom 0.515# Rape_TopBelow_MED
    easeout_bounce 0.3 xanchor 0.21 yanchor 0.16 rotate 13 zoom 0.515# Rape_TopHigh_MED
    repeat

    ## DICK RAPE_LOW

transform afternight04_sexbattle_d_pussy_dick_low_stop_rape_action:
    
    xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW

transform afternight04_sexbattle_d_pussy_dick_low_slow_rape_action:
    subpixel True

    xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    pause 1.0
    easeout_quad 3.0 xanchor 0.21 yanchor 0.11 rotate 5 zoom 0.515# Rape_TopBelow_LOW
    ease_quad 4.0 xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    repeat

transform afternight04_sexbattle_d_pussy_dick_low_mod_rape_action:
    subpixel True
    
    xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    easeout_quad 0.5 xanchor 0.21 yanchor 0.11 rotate 5 zoom 0.515# Rape_TopBelow_LOW
    ease_quad 0.8 xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    pause 0.1
    repeat

transform afternight04_sexbattle_d_pussy_dick_low_fast_rape_action:
    subpixel True
    
    xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    easeout_quad 0.2 xanchor 0.21 yanchor 0.11 rotate 5 zoom 0.515# Rape_TopBelow_LOW
    ease_bounce 0.3 xanchor 0.21 yanchor 0.12 rotate 5 zoom 0.515# Rape_TopHigh_LOW
    pause 0.1
    repeat

############################################################
###########################################################
############################################################
########################################################### TRANSFORM RAPE STOMACH

    ## STOMACH RAPE_DEEP

transform afternight04_sexbattle_d_pussy_stomach_deep_stop_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    easein_quad 8.0 xpos 0.425 ypos 0.465 rotate 6 xzoom 1.1 yzoom 1.5 # rape_TopBeloww_DEEP

transform afternight04_sexbattle_d_pussy_stomach_deep_slow_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    easein_quad 4.0 xpos 0.425 ypos 0.465 rotate 6 xzoom 1.1 yzoom 1.5 # rape_TopBeloww_DEEP
    easeout_quad 4.0 xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_stomach_deep_mod_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    easein_quad 0.7 xpos 0.425 ypos 0.465 rotate 6 xzoom 1.1 yzoom 1.5 # rape_TopBeloww_DEEP
    easeout_quad 0.7 xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_stomach_deep_fast_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 # Anchor Stomach
    xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    easein_quad 0.13 xpos 0.425 ypos 0.465 rotate 6 xzoom 1.1 yzoom 1.5 # rape_TopBeloww_DEEP
    easeout_quad 0.13 xpos 0.42 ypos 0.46 rotate 12 xzoom 0.8 yzoom 0.4 # rape_TopHigh02_DEEP
    repeat

    ## STOMACH RAPE_MED

transform afternight04_sexbattle_d_pussy_stomach_med_stop_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 #Anchor Stomach
    #xpos 0.42 ypos 0.555 rotate 10 xzoom 0.8 yzoom 1.0 # rape_TopHigh_MED
    xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    easein_quad 8.0 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.8 yzoom 1.0 # rape_TopBelow_MED

transform afternight04_sexbattle_d_pussy_stomach_med_slow_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 #Anchor Stomach
    xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    easein_quad 4.0 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.8 yzoom 1.0 # rape_TopBelow_MED
    easeout_quad 4.0 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    repeat

transform afternight04_sexbattle_d_pussy_stomach_med_mod_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 #Anchor Stomach
    xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    easein_quad 0.7 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.8 yzoom 1.0 # rape_TopBelow_MED
    easeout_quad 0.7 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    repeat

transform afternight04_sexbattle_d_pussy_stomach_med_fast_rape_action:
    subpixel True
    transform_anchor True
    truecenter
    xanchor 0.5 yanchor 0.15 #Anchor Stomach
    xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    easein_quad 0.13 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.8 yzoom 1.0 # rape_TopBelow_MED
    easeout_quad 0.13 xpos 0.42 ypos 0.555 rotate 10 xzoom 0.75 yzoom 0.35 # rape_TopHigh_MED
    repeat

    ## STOMACH RAPE_LOW

#transform afternight04_sexbattle_d_pussy_stomach_low_mod_rape_action

############################################################
###########################################################
############################################################
########################################################### TRANSFORM RAPE_PUSSY

    ## PUSSY RAPE_DEEP

transform afternight04_sexbattle_d_pussy_deep_stop_rape_action:
    subpixel True

    xanchor -0.435 yanchor -0.5 rotate 0 xzoom 0.9 yzoom 1.0 # Top High_DEEP
    easein_quad 8.0 xanchor -0.435 yanchor -0.83 rotate 0 xzoom 1.0 yzoom 0.9 # Top Beloww_DEEP

transform afternight04_sexbattle_d_pussy_deep_slow_rape_action:
    subpixel True

    xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top High_DEEP
    easein_quad 4.0 xanchor -0.435 yanchor -0.79 rotate 0 xzoom 1.0 yzoom 0.9 # Top Beloww_DEEP
    easeout_quad 4.0 xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top Highw_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_deep_mod_rape_action:
    subpixel True

    xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top High_DEEP
    easein_quad 0.7 xanchor -0.435 yanchor -0.79 rotate 0 xzoom 1.0 yzoom 0.9 # Top Beloww_DEEP
    easeout_quad 0.7 xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top Highw_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_deep_fast_rape_action:
    subpixel True

    xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top High_DEEP
    easein_quad 0.13 xanchor -0.435 yanchor -0.79 rotate 0 xzoom 1.0 yzoom 0.9 # Top Beloww_DEEP
    easeout_quad 0.13 xanchor -0.435 yanchor -0.456 rotate 0 xzoom 0.9 yzoom 1.0 # Top Highw_DEEP
    repeat

    ## PUSSY RAPE_MED

transform afternight04_sexbattle_d_pussy_med_stop_rape_action:
    subpixel True

    #alpha 0.5
    xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    easein_quad 8.0 xanchor -0.49 yanchor -0.92 rotate 0 xzoom 0.9 yzoom 0.9 # Top Below _ MED

transform afternight04_sexbattle_d_pussy_med_slow_rape_action:
    subpixel True

    #alpha 0.5
    xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    easein_quad 4.0 xanchor -0.49 yanchor -0.92 rotate 0 xzoom 0.9 yzoom 0.9 # Top Below _ MED
    easeout_quad 4.0 xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_med_mod_rape_action:
    subpixel True

    #alpha 0.5
    xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    easein_quad 0.7 xanchor -0.49 yanchor -0.92 rotate 0 xzoom 0.9 yzoom 0.9 # Top Below _ MED
    easeout_quad 0.7 xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_med_fast_rape_action:
    subpixel True

    #alpha 0.5
    xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    easein_quad 0.13 xanchor -0.49 yanchor -0.92 rotate 0 xzoom 0.9 yzoom 0.9 # Top Below _ MED
    easeout_quad 0.13 xanchor -0.435 yanchor -0.6 rotate 0 xzoom 0.9 yzoom 1.0 # Top High MED
    repeat

    ## PUSSY RAPE_LOW

#transform afternight04_sexbattle_d_pussy_low_mod_rape_action:

############################################################
###########################################################
############################################################
########################################################### TRANSFORM RAPE_LEGS

    ## LEGS RAPE_DEEP

transform afternight04_sexbattle_d_pussy_legs_deep_stop_rape_action:
    subpixel True

    yanchor 0.13 #Top High
    easein_quad 8.0 yanchor -0.05 #Top Below_DEEP

transform afternight04_sexbattle_d_pussy_legs_deep_slow_rape_action:
    subpixel True

    yanchor 0.13 #Top High
    easein_quad 4.0 yanchor -0.05 #Top Below_DEEP
    easeout_quad 4.0 yanchor 0.13 #Top High_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_legs_deep_mod_rape_action:
    subpixel True

    yanchor 0.13 #Top High
    easein_quad 0.7 yanchor -0.05 #Top Below_DEEP
    easeout_quad 0.7 yanchor 0.13 #Top High_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_legs_deep_fast_rape_action:
    subpixel True

    yanchor 0.13 #Top High
    easein_quad 0.13 yanchor -0.05 #Top Below_DEEP
    easeout_quad 0.13 yanchor 0.13 #Top High_DEEP
    repeat

    ## LEGS RAPE_MED

transform afternight04_sexbattle_d_pussy_legs_med_stop_rape_action:
    subpixel True

    yanchor 0.06 #Top High MED
    easein_quad 8.0 yanchor -0.07 #Top Below MED

transform afternight04_sexbattle_d_pussy_legs_med_slow_rape_action:
    subpixel True

    yanchor 0.06 #Top High MED
    easein_quad 4.0 yanchor -0.07 #Top Below MED
    easeout_quad 4.0 yanchor 0.06 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_legs_med_mod_rape_action:
    subpixel True

    yanchor 0.06 #Top High MED
    easein_quad 0.7 yanchor -0.07 #Top Below MED
    easeout_quad 0.7 yanchor 0.06 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_legs_med_fast_rape_action:
    subpixel True

    yanchor 0.06 #Top High MED
    easein_quad 0.13 yanchor -0.07 #Top Below MED
    easeout_quad 0.13 yanchor 0.06 #Top High MED
    repeat

    ## LEGS RAPE_LOW

transform afternight04_sexbattle_d_pussy_legs_low_stop_rape_action:
    subpixel True

    #alpha 0.5
    yanchor 0.08 #Top High LOW
    easein_quad 8.0 yanchor 0.03 #Top Below

transform afternight04_sexbattle_d_pussy_legs_low_slow_rape_action:
    subpixel True

    yanchor 0.08 #Top High LOW
    easein_quad 4.0 yanchor 0.03 #Top Below
    easeout_quad 4.0 yanchor 0.08 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_legs_low_mod_rape_action:
    subpixel True

    yanchor 0.08 #Top High LOW
    easein_quad 0.7 yanchor 0.03 #Top Below
    easeout_quad 0.7 yanchor 0.08 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_legs_low_fast_rape_action:
    subpixel True

    yanchor 0.08 #Top High LOW
    easein_quad 0.3 yanchor -0.06 #Top02 Below
    easeout_quad 0.3 yanchor 0.08 #Top High MED
    repeat

############################################################
###########################################################
############################################################
########################################################### TRANSFORM RAPE_PUBIC

## PUBIC RAPE_DEEP

transform afternight04_sexbattle_d_pussy_pubic_deep_stop_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.45 #Top High_DEEP
    easein_quad 8.0 yanchor -0.72 #Top Below_DEEP

transform afternight04_sexbattle_d_pussy_pubic_deep_slow_rape_action:
    subpixel True

    yanchor -0.45 #Top High_DEEP
    easein_quad 4.0  yanchor -0.72 #Top Below_DEEP
    easeout_quad 4.0 yanchor -0.45 #Top High_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_pubic_deep_mod_rape_action:
    subpixel True

    yanchor -0.45 #Top High_DEEP
    easein_quad 0.7  yanchor -0.72 #Top Below_DEEP
    easeout_quad 0.7 yanchor -0.45 #Top High_DEEP
    repeat

transform afternight04_sexbattle_d_pussy_pubic_deep_fast_rape_action:
    subpixel True

    yanchor -0.45 #Top High_DEEP
    easein_quad 0.13  yanchor -0.72 #Top Below_DEEP
    easeout_quad 0.13 yanchor -0.45 #Top High_DEEP
    repeat

## PUBIC RAPE_MED

transform afternight04_sexbattle_d_pussy_pubic_med_stop_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.57 #Top High MED
    easein_quad 8.0 yanchor -0.78 #Top Below MED

transform afternight04_sexbattle_d_pussy_pubic_med_slow_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.57 #Top High MED
    easein_quad 4.0 yanchor -0.78 #Top Below MED
    easeout_quad 4.0 yanchor -0.57 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_pubic_med_mod_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.57 #Top High MED
    easein_quad 0.7 yanchor -0.78 #Top Below MED
    easeout_quad 0.7 yanchor -0.57 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_pubic_med_fast_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.57 #Top High MED
    easein_quad 0.13 yanchor -0.78 #Top Below MED
    easeout_quad 0.13 yanchor -0.57 #Top High MED
    repeat


## PUBIC RAPE_LOW

transform afternight04_sexbattle_d_pussy_pubic_low_stop_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    #xanchor -0.39 yanchor -0.67 rotate 0 zoom 1.0 xzoom 1.0 yzoom 1.0

    yanchor -0.53 #Top High LOW
    easein_quad 8.0 yanchor -0.62 #Top Below

transform afternight04_sexbattle_d_pussy_pubic_low_slow_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.53 #Top High LOW
    easein_quad 4.0 yanchor -0.62 #Top Below
    easeout_quad 4.0 yanchor -0.53 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_pubic_low_mod_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.53 #Top High LOW
    easein_quad 0.7 yanchor -0.62 #Top Below
    easeout_quad 0.7 yanchor -0.53 #Top High MED
    repeat

transform afternight04_sexbattle_d_pussy_pubic_low_fast_rape_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos

    yanchor -0.53 #Top High LOW
    easein_quad 0.3 yanchor -0.77 #Top02 Below
    easeout_quad 0.3 yanchor -0.53 #Top High MED
    repeat

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # PUSSY RAPE_DICK_a

label afternight04_sexbattle_mc_dick_pussy_rape_general:

#################
#################
################# DEEP

    if mc_body.store["dick"] == "Pussy_dick_deep":

## DICK PUSSY DEEP

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_stop_rape_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_slow_rape_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_mod_rape_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_deep_fast_rape_action

## STOMACH PUSSY DEEP

        if mc_body.dick_speed == 0:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                #alpha 0.95
                afternight04_sexbattle_d_pussy_stomach_deep_stop_rape_action

        elif mc_body.dick_speed == 1:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_slow_rape_action

        elif mc_body.dick_speed == 2:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_mod_rape_action

        elif mc_body.dick_speed == 3:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_deep_fast_rape_action

## LEGS_OVER_PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_legs_deep_stop_rape_action 

        if mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_pussy_legs_deep_slow_rape_action 

        if mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_pussy_legs_deep_mod_rape_action 

        if mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_over_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_pussy_legs_deep_fast_rape_action

## LEGS_TOP_PUSSY (ClitorisVagina)

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                #alpha 0.8
                afternight04_sexbattle_d_pussy_deep_stop_rape_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_slow_rape_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_mod_rape_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_deep_fast_rape_action

## PUBIC PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_pubic_deep_stop_rape_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_slow_rape_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_mod_rape_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_fast_rape_action

## ASSHOLE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_pubic_deep_stop_rape_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_slow_rape_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_mod_rape_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_deep_fast_rape_action

## LEGS

        if current_pose.id == "pose_1":

            if mc_body.dick_speed == 0:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    #alpha 0.5
                    afternight04_sexbattle_d_pussy_legs_deep_stop_rape_action

            elif mc_body.dick_speed == 1:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_slow_rape_action

            elif mc_body.dick_speed == 2:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_mod_rape_action

            elif mc_body.dick_speed == 3:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_deep_fast_rape_action

#################
#################
################# MED


    elif mc_body.store["dick"] == "Pussy_dick_med":

## DICK PUSSY MED RAPE

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_stop_rape_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                #alpha 0.5
                afternight04_sexbattle_d_pussy_dick_med_slow_rape_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_mod_rape_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_med_fast_rape_action

## STOMACH PUSSY MED RAPE

        if mc_body.dick_speed == 0:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_stop_rape_action

        elif mc_body.dick_speed == 1:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                #alpha 0.5
                afternight04_sexbattle_d_pussy_stomach_med_slow_rape_action

        elif mc_body.dick_speed == 2:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_mod_rape_action

        elif mc_body.dick_speed == 3:
        
            show afternight04_sexbattle_d_legs_stomach_pussy wet_00_a:
                afternight04_sexbattle_d_pussy_stomach_med_fast_rape_action

## LEGS_OVER_PUSSY MED RAPE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
               afternight04_sexbattle_d_pussy_legs_med_stop_rape_action 

        if mc_body.dick_speed == 1:
            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_legs_med_slow_rape_action

        if mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:

                afternight04_sexbattle_d_pussy_legs_med_mod_rape_action 

        if mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_legs_med_fast_rape_action

## LEGS_TOP_PUSSY MED RAPE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_stop_rape_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_med_slow_rape_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_mod_rape_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_med_fast_rape_action


## PUBIC PUSSY MED RAPE (Coño abierto)

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_stop_rape_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                #alpha 0.1
                afternight04_sexbattle_d_pussy_pubic_med_slow_rape_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_mod_rape_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_pussy 06_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_fast_rape_action

## ASSHOLE MED RAPE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_stop_rape_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_slow_rape_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_mod_rape_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_med_fast_rape_action

## LEGS MED RAPE

        if current_pose.id == "pose_1":

            if mc_body.dick_speed == 0:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_stop_rape_action

            elif mc_body.dick_speed == 1:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    #alpha 0.1
                    afternight04_sexbattle_d_pussy_legs_med_slow_rape_action

            elif mc_body.dick_speed == 2:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_mod_rape_action

            elif mc_body.dick_speed == 3:

                show afternight04_sexbattle_d_legs_base wet_00_a:
                    afternight04_sexbattle_d_pussy_legs_med_fast_rape_action

#################
#################
################# LOW

    elif mc_body.store["dick"] == "Pussy_dick_low":

        # HIDING

        show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_stomach_pussy empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_top_pussy empty:
                afternight04_sexbattle_d_pubicpart_pos

## DICK LOW RAPE
        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_stop_rape_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_slow_rape_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_mod_rape_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_low_fast_rape_action

## LEGS LOW RAPE

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_pussy_legs_low_stop_rape_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_pussy_legs_low_slow_rape_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_pussy_legs_low_mod_rape_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_pussy_legs_low_fast_rape_action

## PUSSY LOW RAPE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_stop_rape_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_slow_rape_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_mod_rape_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_fast_rape_action

## ASSHOLE LOW RAPE

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_stop_rape_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_slow_rape_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_mod_rape_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pussy_pubic_low_fast_rape_action

    return


##################################################################################################################
#################################################################################################################
################################################################################################################
###############################################################################################################
##############################################################################################################
#############################################################################################################
############################################################################################################
###########################################################################################################
##########################################################################################################


image afternight04_sexbattle_mc_dick_pussy rape_general: # NOT FINISHED, this one has to be deleted once the scene is done. Necessary to delete?

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains: # LEGS

        ConditionSwitch(
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_pussy_legs_low_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_pussy_legs_low_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_pussy_legs_low_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_pussy_legs_low_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_fast_rape_action),
            "True", Null())

    contains: # DICK

        ConditionSwitch(
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_low_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_low_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_low_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_low" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_low_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_med_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_med_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_med_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_med_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_deep_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_deep_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_deep_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_pussy condom_wet_00_a", afternight04_sexbattle_d_pussy_dick_deep_fast_rape_action),
            "True", Null())

    contains: # STOMACH
        #alpha 0.5
        ConditionSwitch(
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_med_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_med_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_med_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_med_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_deep_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_deep_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_deep_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_pussy_stomach_deep_fast_rape_action),
            "True", Null())

    contains: # OVER_PUSSY

        ConditionSwitch(
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_med_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_legs_deep_fast_rape_action),
            "True", Null())

    contains: # TOP_PUSSY (MOVEABLE PART)

        ConditionSwitch(
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_med_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_med_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_med_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_med_fast_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_deep_stop_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_deep_slow_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_deep_mod_rape_action),
            mc_body.store["dick"] == "Pussy_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_pussy_deep_fast_rape_action),
            "True", Null())

############################################################
########################################################### 
############################################################
########################################################### 
############################################################
########################################################### 
############################################################
########################################################### Scene Background A

image afternight04_sexbattle_d_scene a:

    contains:
        "black"

    contains:
        "afternight04_sexbattle_background a"
        alpha 0.1

    #contains:
        #"afternight04_sexbattle_prove_a"

############################################################
###########################################################
############################################################
###########################################################
############################################################
########################################################### ## vapor breathing animation

image afternight04_sexbattle_dvaporbreathing 00 = "images/general/empty.webp"

############################################################
###########################################################

image afternight04_sexbattle_dvaporbreathing 01_a: #vapor breathing animation

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:
        "bsmoke 01"
        subpixel True
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.1 #First Pose
        easein_cubic 7.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 16.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.1 #First Pose
        easein_cubic 7.0 xanchor -0.8 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 04"
        subpixel True
        alpha 0.0
        pause 35.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.1 #First Pose
        easein_cubic 7.0 xanchor -0.72 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 50.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.1 #First Pose
        easein_cubic 7.0 xanchor -0.78 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

############################################################
###########################################################

image afternight04_sexbattle_dvaporbreathing 02_a: #vapor breathing animation

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "bsmoke 01"
        subpixel True
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.22 #First Pose
        easein_cubic 7.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 7.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.22 #First Pose
        easein_cubic 7.0 xanchor -0.8 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 04"
        subpixel True
        alpha 0.0
        pause 15.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.22 #First Pose
        easein_cubic 7.0 xanchor -0.72 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 22.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.22 #First Pose
        easein_cubic 7.0 xanchor -0.78 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

############################################################
###########################################################

image afternight04_sexbattle_dvaporbreathing 03_a: #vapor breathing animation

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "bsmoke 01"
        subpixel True
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.75 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 1.66
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.8 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 04"
        subpixel True
        alpha 0.0
        pause 3.33
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.72 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat
        
    contains:
        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 5.0
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.78 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:

        "bsmoke 01"
        subpixel True
        alpha 0.0
        pause 8.33
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.78 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:

        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 11.66
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.78 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:

        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 15.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.35 #First Pose
        easein_cubic 5.0 xanchor -0.78 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

############################################################
###########################################################

image afternight04_sexbattle_dvaporbreathing 04_a: #vapor breathing animation

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
    
    contains:
        "bsmoke 01"
        subpixel True
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 1.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 1.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 04"
        subpixel True
        alpha 0.0
        pause 2.5
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 01"
        subpixel True
        alpha 0.0
        pause 2.5
        xanchor -2.0 yanchor -0.5 rotate 120 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 90 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 04"
        subpixel True
        alpha 0.0
        pause 5.5
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 03"
        subpixel True
        alpha 0.0
        pause 7.2
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

    contains:
        "bsmoke 09"
        subpixel True
        alpha 0.0
        pause 7.0
        xanchor -2.0 yanchor -0.5 rotate 30 size (85, 85) alpha 0.55 #First Pose
        easein_cubic 4.0 xanchor -0.75 yanchor 0.6 rotate 0 size (200, 200) alpha 0.0 #Second Pose
        repeat

############################################################
###########################################################
############################################################
###########################################################
############################################################ MC CUMMING SCENES.

label afternight04_Pussy_dick_cum_scene:
    
    $ debug ("HOLULUUU")

    show afternight04_sexbattle_mc_handL empty
    show afternight04_sexbattle_mc_handR empty

    $ debug ("HOLULAAA")

    show afternight04_sexbattle_mc_tongue_clitoris empty

    #if current_pose.id == "pose_1":

    if afternight04_condom_on == True:
        call afternight04_sexbattle_mc_dick_pussy_cumshot_in

    else:
        call afternight04_sexbattle_mc_dick_pussy_cumshot_out

    show afternight04_sexbattle_mc_handR_penetrate_pussy empty
    show afternight04_sexbattle_mc_handR_penetrate_anal empty
    show afternight04_sexbattle_mc_tongue_pussy empty
    show afternight04_sexbattle_mc_tongue_anal empty

    if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
        with vpunch
    else:
        with dissolve

    if afternight04_condom_on == False:

        pause 2.0

        show afternight04_sexbattle_mc_cumshot empty
        with dissolve

        pause 0.5

        if afternight04_CumOnStomach == 1:

            show afternight04_sexbattle_mc_cum_stomach just_01_action_a

        elif afternight04_CumOnStomach == 2:

            show afternight04_sexbattle_mc_cum_stomach over_01-02_action_a

        elif afternight04_CumOnStomach == 3:

            show afternight04_sexbattle_mc_cum_stomach over_01-02-03_action_a

        ####################
        ####################

    $ mc_body.store["right_hand"] = ""
    $ mc_body.store["left_hand"] = ""
    $ mc_body.store["tongue"] = ""
    #$ mc_body.store["dick"] == ""
    #$ mc_body.store["dick"] = "Pussy_dick_out" #She´s raping you, so no need to change this.

    return

        ####################
        ####################

label afternight04_sexbattle_mc_dick_pussy_cumshot_in:


    if current_pose.id == "pose_1":

        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            call afternight04_Pussy_dick_general_image

        elif (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            call afternight04_Anal_dick_general_image

        else: #Dick is not inside pussy or anal.

            $ mc_body.store["dick"] == "Pussy_dick_out"

            call afternight04_Pussy_dick_general_image

    else:

        $ mc_body.dick_speed = 0

        $ debug ("Velocity 0")

        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            call afternight04_sexbattle_mc_dick_Pussy_general_doggystyle_scene

        elif (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            call afternight04_sexbattle_mc_dick_Anal_general_doggystyle_scene

        else: #Dick is not inside pussy or anal.

            $ mc_body.store["dick"] == ""

            call afternight04_sexbattle_mc_dick_Pussy_general_doggystyle_scene

            show afternight04_sexbattle_mc_dick_pussy empty
            show afternight04_sexbattle_mc_dick_anal empty



    return

#image afternight04_sexbattle_mc_dick_pussy cumshot_in:

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    #contains:
        #alpha 0.5

        #ConditionSwitch(
            #(afternight04_Pussy_dick_deep_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_0_Rape_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 05_wet_00_a", afternight04_sexbattle_d_pussy_legs_low_stop_action),
            #(afternight04_Pussy_dick_med_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_0_Rape_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 03_wet_00_a", afternight04_sexbattle_d_pussy_legs_low_stop_action),
            #(afternight04_Pussy_dick_low_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_low_Speed_0_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", afternight04_sexbattle_d_pussy_legs_low_stop_action),
            #"True", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", afternight04_sexbattle_d_pussy_legs_low_stop_action))

    #contains:
        #alpha 0.5

        #"afternight04_sexbattle_mc_dick_pussy condom_wet_00_a"
        #afternight04_sexbattle_d_pussy_dick_low_stop_action

    #contains:
        #alpha 0.5

        #"afternight04_sexbattle_d_legs_stomach_pussy wet_00_a"
        #afternight04_sexbattle_d_pussy_stomach_med_stop_action

    #contains:
        #alpha 0.0

        #"afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a"
        #afternight04_sexbattle_d_pussy_med_stop_action

    #contains:
        #alpha 0.5

        #"afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a"
        #afternight04_sexbattle_d_pussy_med_stop_action


############################################################
########################################################### 
############################################################
########################################################### 

transform afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a:
    subpixel True
    xanchor 0.255 yanchor 0.16 rotate -2 zoom 0.6# Tip
    easeout_quad 1.0 xanchor 0.26 yanchor 0.0 rotate 5 zoom 0.63 # OffScreen
    

transform afternight04_sexbattle_d_pussy_dick_cum_out_framein_action:
    subpixel True
    alpha 0.0
    pause 1.0
    alpha 1.0
    xanchor 0.26 yanchor 0.0 rotate 5 zoom 0.63 # OffScreen
    easein_quad 1.0 xanchor 0.26 yanchor 0.17 rotate 5 zoom 0.6 #Final POse

    block:
        easein_quad 0.2 xanchor 0.259 yanchor 0.169 rotate 4 zoom 0.6 #01
        easeout_quad 0.2 xanchor 0.261 yanchor 0.171 rotate 6 zoom 0.6 #02
        easein_quad 0.2 xanchor 0.26 yanchor 0.17 rotate 5 zoom 0.6 #Final POse
        repeat 3
        easeout_quad 10.0 xanchor 0.26 yanchor 0.17 rotate 5 zoom 0.6 #Final POse

transform afternight04_sexbattle_d_pussy_legs_cum_out_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 1.0 yanchor 0.0 # Semi-Med
    easein_quad 1.0 yanchor 0.005 #Med
    easeout_quad 1.0 yanchor 0.0# Semi-Med
    easein_quad 1.0 yanchor 0.0 #Tip

############################################################
########################################################### 

label afternight04_sexbattle_mc_dick_pussy_cumshot_out:

    if current_pose.id == "pose_1": ## POSE 01
        $ debug ("HAKUNAMATATA")

        show afternight04_sexbattle_mc_cumshot 01_action_a:
            alpha 0.0
            pause 2.5
            easein_quad 0.25 alpha 1.0
            pause 0.25
            easeout_quad 0.5 alpha 0.0

        # HIDING

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_position
        show afternight04_sexbattle_d_legs_stomach_pussy empty:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_position
        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos


        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_top_anal empty:
                afternight04_sexbattle_d_pubicpart_pos
        show afternight04_sexbattle_d_legs_top_pussy empty:
                afternight04_sexbattle_d_pubicpart_pos

        ##

        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a

        elif (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a

        else:
            show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a

        show afternight04_sexbattle_mc_dick_pussy_cumshot naked_wet_00_a:
            afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            afternight04_sexbattle_d_pussy_dick_cum_out_framein_action

    else:

        $ debug ("hakunomatato")

        $ mc_body.store["dick"] = ""
        $ mc_body.dick_speed = 0

        call afternight04_sexbattle_pubic_emptiness

        show afternight04_sexbattle_mc_dick_pussy condom_wet_00_b:
            afternight04_sexbattle_mc_dick_pussy_offscreen_action_b
        show afternight04_sexbattle_mc_dick_anal condom_wet_00_b:
            afternight04_sexbattle_mc_dick_pussy_offscreen_action_b

        show afternight04_sexbattle_mc_cumshot 01_b:
            alpha 0.0
            pause 1.5
            easein_quad 0.5 alpha 1.0
            pause 0.5
            easeout_quad 0.5 alpha 0.0


        show afternight04_sexbattle_mc_dick_cumshot naked_wet_00_b:
            subpixel True
            alpha 0.0
            pause 1.0
            alpha 1.0
            xanchor -0.0035 yanchor -0.85 rotate 0 #Offscreen
            easein_quad 1.0 xanchor -0.0035 yanchor -0.4 rotate 0 # # It goes below Pussy

        show afternight04_sexbattle_mc_cum_back 001_b:
            subpixel True

            "afternight04_sexbattle_mc_cum_back 01_b"
            afternight04_sexbattle_didac_squirt_b_pos
            alpha 0.0
            pause 2.0
            easein_quad 0.5 alpha 1.0

        $ debug ("WTF?!")

    return




#image afternight04_sexbattle_mc_dick_pussy cumshot_out: # NOT FINISHED, DELETE THIS WHEN CUMSHOT OUT WORKS FINE.

    #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    #contains:
        #alpha 0.5

        #ConditionSwitch(
            #(afternight04_Pussy_dick_deep_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_0_Rape_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 05_wet_00_a", afternight04_sexbattle_d_pussy_legs_cum_out_action),
            #(afternight04_Pussy_dick_med_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_0_Rape_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 03_wet_00_a", afternight04_sexbattle_d_pussy_legs_cum_out_action),
            #(afternight04_Pussy_dick_low_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_low_Speed_0_Done >= 1), At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", afternight04_sexbattle_d_pussy_legs_cum_out_action),
            #"True", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", afternight04_sexbattle_d_pussy_legs_cum_out_action))
    #contains:

        #alpha 0.0
        #pause 2.5
        #"afternight04_sexbattle_mc_cumshot 01_action_a"
        #easein_quad 0.25 alpha 1.0
        #pause 0.25
        #easeout_quad 0.5 alpha 0.0

    #contains:
        #alpha 0.5

        #"afternight04_sexbattle_mc_dick_pussy condom_wet_00_a"
        #afternight04_sexbattle_d_pussy_dick_cum_out_frameout_action_a

    #contains:
        #alpha 0.5

        #"afternight04_sexbattle_mc_dick_pussy naked_wet_00_a"
        #afternight04_sexbattle_d_pussy_dick_cum_out_framein_action


############################################################
########################################################### 
############################################################
########################################################### 
############################################################
########################################################### 
############################################################
##
##
##
##
##
##
##
##
##











############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # ANAL DICK TRANSFORM pose 01


############################################################
###########################################################
############################################################
########################################################### TRANSFORM DICK ANAL

    ## DICK DEEP

transform afternight04_sexbattle_d_anal_dick_deep_stop_action:
    subpixel True

    xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 3.0 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 5.0 xanchor 0.257 yanchor 0.22 rotate -5 zoom 0.55 # Deep ANAL

transform afternight04_sexbattle_d_anal_dick_deep_slow_action:
    subpixel True

    xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 2.0 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 2.0 xanchor 0.257 yanchor 0.22 rotate -5 zoom 0.55 # Deep ANAL
    easeout_quad 2.0 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 2.0 xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_deep_mod_action:
    subpixel True

    xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 0.2 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 0.5 xanchor 0.257 yanchor 0.22 rotate -5 zoom 0.55 # Deep ANAL
    easeout_quad 0.2 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 0.5 xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    repeat
transform afternight04_sexbattle_d_anal_dick_deep_fast_action:
    subpixel True

    xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 0.04 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 0.1 xanchor 0.257 yanchor 0.22 rotate -5 zoom 0.55 # Deep ANAL
    easeout_quad 0.04 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easein_quad 0.1 xanchor 0.24 yanchor 0.12 rotate -2 zoom 0.6# Tip ANAL
    repeat

    ## DICK MED

transform afternight04_sexbattle_d_anal_dick_med_stop_action:
    subpixel True

    xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 3.0 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 5.0 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL

transform afternight04_sexbattle_d_anal_dick_med_slow_action:
    subpixel True
    xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 2.0 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 2.0 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easeout_quad 2.0 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 2.0 xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_med_mod_action:
    subpixel True
    xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 0.2 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 0.5 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easeout_quad 0.2 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 0.5 xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_med_fast_action:
    subpixel True
    xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    easeout_quad 0.03 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 0.1 xanchor 0.24 yanchor 0.165 rotate 0 zoom 0.58 # Med ANAL
    easeout_quad 0.03 xanchor 0.238 yanchor 0.145 rotate 1  zoom 0.59 # Semi-Med
    easein_quad 0.1 xanchor 0.24 yanchor 0.1 rotate -2 zoom 0.6# Tip ANAL
    repeat

    ## DICK LOW

transform afternight04_sexbattle_d_anal_dick_low_stop_action:
    subpixel True

    xanchor 0.255 yanchor 0.0 rotate -6 zoom 0.63 # OffScreen ANAL
    easeout_quad 3.0 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 5.0 xanchor 0.245 yanchor 0.08 rotate 3  zoom 0.6 # Over_Tip ANAL

transform afternight04_sexbattle_d_anal_dick_low_slow_action:
    subpixel True
    xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    easeout_quad 2.0 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 2.0 xanchor 0.245 yanchor 0.08 rotate 3  zoom 0.6 # Over_Tip ANAL
    easeout_quad 2.0 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 2.0 xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_low_mod_action:
    subpixel True
    xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    easeout_quad 1.0 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 1.0 xanchor 0.245 yanchor 0.08 rotate 3  zoom 0.6 # Over_Tip ANAL
    easeout_quad 1.0 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 1.0 xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_low_fast_action:
    subpixel True
    xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    easeout_quad 0.15 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 0.15 xanchor 0.245 yanchor 0.08 rotate 3  zoom 0.6 # Over_Tip ANAL
    easeout_quad 0.15 xanchor 0.24 yanchor 0.09 rotate -2 zoom 0.6# Tip ANAL
    easein_quad 0.15 xanchor 0.242 yanchor 0.09 rotate -6 zoom 0.63 # #Previous_Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_dick_out_stop_action:

    xanchor 0.255 yanchor 0.0 rotate -6 zoom 0.63 # OffScreen ANAL

############################################################
###########################################################
############################################################
########################################################### TRANSFORM STOMACH ANAL

    ## STOMACH DEEP

transform afternight04_sexbattle_d_anal_stomach_deep_stop_action:
    subpixel True

    xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    easeout_quad 3.0 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 5.0 xanchor -0.24 yanchor -0.46 rotate -6 xzoom 0.9 yzoom 1.2 #Deep ANAL

transform afternight04_sexbattle_d_anal_stomach_deep_slow_action:
    subpixel True
    xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    easeout_quad 2.0 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 2.0 xanchor -0.24 yanchor -0.46 rotate -6 xzoom 0.9 yzoom 1.2 #Deep ANAL
    easeout_quad 2.0 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 2.0 xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_stomach_deep_mod_action:
    subpixel True
    xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    easeout_quad 0.2 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 0.5 xanchor -0.24 yanchor -0.46 rotate -6 xzoom 0.9 yzoom 1.2 #Deep ANAL
    easeout_quad 0.2 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 0.5 xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    repeat

transform afternight04_sexbattle_d_anal_stomach_deep_fast_action:
    subpixel True
    xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    easeout_quad 0.04 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 0.1 xanchor -0.24 yanchor -0.46 rotate -6 xzoom 0.9 yzoom 1.2 #Deep ANAL
    easeout_quad 0.04 xanchor -0.35 yanchor -0.72 rotate 3 xzoom 1.0 yzoom 0.9 #Med ANAL
    easein_quad 0.1 xanchor -0.74 yanchor -1.1 rotate 3 xzoom 0.8 yzoom 0.5 #Tip ANAL
    repeat

    ## STOMACH MED

transform afternight04_sexbattle_d_anal_stomach_med_stop_action:
    subpixel True
    xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    easeout_quad 3.0 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 5.0 xanchor -0.345 yanchor -0.575 rotate 3 xzoom 1.0 yzoom 0.9 #Med

transform afternight04_sexbattle_d_anal_stomach_med_slow_action:
    subpixel True
    xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    easeout_quad 2.0 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 2.0 xanchor -0.345 yanchor -0.575 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 2.0 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 2.0 xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    repeat

transform afternight04_sexbattle_d_anal_stomach_med_mod_action:
    subpixel True
    xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    easeout_quad 0.2 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 0.5 xanchor -0.345 yanchor -0.575 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 0.2 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 0.5 xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    repeat

transform afternight04_sexbattle_d_anal_stomach_med_fast_action:
    subpixel True
    xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    easeout_quad 0.03 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 0.1 xanchor -0.345 yanchor -0.575 rotate 3 xzoom 1.0 yzoom 0.9 #Med
    easeout_quad 0.03 xanchor -0.405 yanchor -0.68 rotate 3 xzoom 0.9 yzoom 0.9 # Semi-Med
    easein_quad 0.1 xanchor -0.7 yanchor -1.03 rotate 3 xzoom 0.8 yzoom 0.5 #Tip
    repeat

    ## STOMACH LOW
transform afternight04_sexbattle_d_anal_stomach_low_stop_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_stomach_low_slow_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_stomach_low_mod_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_stomach_low_fast_action:
    alpha 0.0

############################################################
###########################################################
############################################################
########################################################### TRANSFORM ANAL

    ## ANAL DEEP

transform afternight04_sexbattle_d_anal_deep_stop_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 3.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 5.0 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
transform afternight04_sexbattle_d_anal_deep_slow_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 2.0 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 2.0 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_anal_deep_mod_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.2 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.5 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 0.2 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.5 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_anal_deep_fast_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.04 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.1 xanchor -0.443 yanchor -0.745 rotate 0 xzoom 0.98  yzoom 0.9#Deep
    easeout_quad 0.04 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easein_quad 0.1 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat

## ANAL MED

transform afternight04_sexbattle_d_anal_med_stop_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 3.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 5.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med

transform afternight04_sexbattle_d_anal_med_slow_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 2.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 2.0 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 2.0 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 2.0 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_anal_med_mod_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.2 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.5 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 0.2 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.5 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat
transform afternight04_sexbattle_d_anal_med_fast_action:
    subpixel True
    xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    easeout_quad 0.03 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.1 xanchor -0.44 yanchor -0.73 rotate 1 xzoom 0.95 yzoom 0.95 #Med
    easeout_quad 0.03 xanchor -0.435 yanchor -0.73 rotate 0 xzoom 0.93  yzoom 0.98# Semi-Med
    easein_quad 0.1 xanchor -0.435 yanchor -0.735 rotate 0 xzoom 0.9  yzoom 1.0#Tip
    repeat

## ANAL LOW

transform afternight04_sexbattle_d_anal_low_stop_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_low_slow_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_low_mod_action:
    alpha 0.0
transform afternight04_sexbattle_d_anal_low_fast_action:
    alpha 0.0

############################################################
###########################################################
############################################################
########################################################### TRANSFORM LEGS ANAL
## LEGS DEEP

transform afternight04_sexbattle_d_anal_legs_deep_stop_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 3.0 yanchor 0.0 # Med
    easein_quad 5.0 yanchor 0.01 # Deep
    easein_quad 10.0 yanchor 0.0 #Tip

transform afternight04_sexbattle_d_anal_legs_deep_slow_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 2.0 yanchor 0.0 # Med
    easein_quad 2.0 yanchor 0.01 # Deep
    easeout_quad 2.0 yanchor 0.0# Med
    easein_quad 2.0 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_anal_legs_deep_mod_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.2 yanchor 0.0 # Med
    easein_quad 0.5 yanchor 0.01 # Deep
    easeout_quad 0.2 yanchor 0.0# Med
    easein_quad 0.5 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_anal_legs_deep_fast_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.04 yanchor 0.0 # Med
    easein_quad 0.1 yanchor 0.01 # Deep
    easeout_quad 0.04 yanchor 0.0# Med
    easein_quad 0.1 yanchor 0.0 #Tip
    repeat



## LEGS MED
transform afternight04_sexbattle_d_anal_legs_med_stop_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 3.0 yanchor 0.0 # Semi-Med
    easein_quad 5.0 yanchor 0.005 #Med
    easeout_quad 10.0 yanchor 0.0 #Tip

transform afternight04_sexbattle_d_anal_legs_med_slow_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 2.0 yanchor 0.0 # Semi-Med
    easein_quad 2.0 yanchor 0.005 #Med
    easeout_quad 2.0 yanchor 0.0# Semi-Med
    easein_quad 2.0 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_anal_legs_med_mod_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.2 yanchor 0.0 # Semi-Med
    easein_quad 0.5 yanchor 0.005 #Med
    easeout_quad 0.2 yanchor 0.0# Semi-Med
    easein_quad 0.5 yanchor 0.0 #Tip
    repeat

transform afternight04_sexbattle_d_anal_legs_med_fast_action:
    subpixel True
    yanchor 0.0 #Tip
    easeout_quad 0.03 yanchor 0.0 # Semi-Med
    easein_quad 0.1 yanchor 0.005 #Med
    easeout_quad 0.03 yanchor 0.0# Semi-Med
    easein_quad 0.1 yanchor 0.0 #Tip
    repeat

## LEGS LOW
transform afternight04_sexbattle_d_anal_legs_low_stop_action:
    yanchor 0.0


############################################################
###########################################################
############################################################
########################################################### TRANSFORM PUBIC ANAL
## PUBIC DEEP

transform afternight04_sexbattle_d_anal_pubic_deep_stop_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 3.0 yanchor -0.67 # Med
    easein_quad 5.0 yanchor -0.658 # Deep
    easein_quad 10.0 yanchor -0.67 #Tip

transform afternight04_sexbattle_d_anal_pubic_deep_slow_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 2.0 yanchor -0.67 # Med
    easein_quad 2.0 yanchor -0.658 # Deep
    easeout_quad 2.0 yanchor -0.67# Med
    easein_quad 2.0 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_anal_pubic_deep_mod_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 0.2 yanchor -0.67 # Med
    easein_quad 0.5 yanchor -0.658 # Deep
    easeout_quad 0.2 yanchor -0.67 # Med
    easein_quad 0.5 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_anal_pubic_deep_fast_action:
    subpixel True
    yanchor -0.67 #Tip
    easeout_quad 0.04 yanchor -0.67 # Med
    easein_quad 0.1 yanchor -0.658 # Deep
    easeout_quad 0.04 yanchor -0.67 # Med
    easein_quad 0.1 yanchor -0.67 #Tip
    repeat

## PUBIC MED

transform afternight04_sexbattle_d_anal_pubic_med_stop_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 3.0 yanchor -0.67 # Semi-Med
    easein_quad 5.0 yanchor -0.665 #Med
    easeout_quad 10.0 yanchor -0.67 #Tip

transform afternight04_sexbattle_d_anal_pubic_med_slow_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 2.0  yanchor -0.67 # Semi-Med
    easein_quad 2.0 yanchor -0.665 #Med
    easeout_quad 2.0 yanchor -0.67 # Semi-Med
    easein_quad 2.0 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_anal_pubic_med_mod_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.2 yanchor -0.67 # Semi-Med
    easein_quad 0.5 yanchor -0.665 #Med
    easeout_quad 0.2 yanchor -0.67 # Semi-Med
    easein_quad 0.5 yanchor -0.67 #Tip
    repeat

transform afternight04_sexbattle_d_anal_pubic_med_fast_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.03 yanchor -0.67 # Semi-Med
    easein_quad 0.1 yanchor -0.665 #Med
    easeout_quad 0.03 yanchor -0.67 # Semi-Med
    easein_quad 0.1 yanchor -0.67 #Tip
    repeat

## PUBIC LOW
transform afternight04_sexbattle_d_anal_pubic_low_stop_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 3.0 yanchor -0.665 # Tip
    easein_quad 5.0 yanchor -0.67 # Previous_Tip-original

transform afternight04_sexbattle_d_anal_pubic_low_slow_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 2.0 yanchor -0.66 # Tip
    easein_quad 2.0 yanchor -0.67 # Previous_Tip-original
    easeout_quad 2.0 yanchor -0.665 # Tip
    easein_quad 2.0 yanchor -0.67 # Previous_Tip-original
    repeat

transform afternight04_sexbattle_d_anal_pubic_low_mod_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 1.0 yanchor -0.66 # Tip
    easein_quad 1.0 yanchor -0.67 # Previous_Tip-original
    easeout_quad 1.0 yanchor -0.665 # Tip
    easein_quad 1.0 yanchor -0.67 # Previous_Tip-original
    repeat

transform afternight04_sexbattle_d_anal_pubic_low_fast_action:
    subpixel True
    afternight04_sexbattle_d_pubicpart_pos
    easeout_quad 0.15 yanchor -0.66 # Tip
    easein_quad 0.15 yanchor -0.67 # Previous_Tip-original
    easeout_quad 0.15 yanchor -0.665 # Tip
    easein_quad 0.15 yanchor -0.67 # Previous_Tip-original
    repeat

############################################################
###########################################################
############################################################
########################################################### 
############################################################
###########################################################
############################################################
###########################################################  # ANAL DICK_a ANAL

label afternight04_sexbattle_mc_dick_anal_pose01_scene:

### DICK OUT

    if (mc_body.store["dick"] == "Anal_dick_out" or mc_body.store["dick"] == ""):

        # HIDING

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_top_anal empty:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
            #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
            afternight04_sexbattle_d_anal_dick_out_stop_action


### DICK LOW

    elif mc_body.store["dick"] == "Anal_dick_low":

        # HIDING

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_NOposition

        show afternight04_sexbattle_d_legs_top_anal empty:
                afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a

        # LEGS

        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_d_pussy_legs_low_stop_action

        # PUBIC PUSSY

        show afternight04_sexbattle_d_legs_pussy:
            afternight04_sexbattle_d_pubicpart_pos

        # PUBIC ANAL

        show afternight04_sexbattle_d_legs_anal:
            afternight04_sexbattle_d_pubicpart_pos

        # DICK ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_anal_dick_low_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_anal_dick_low_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_anal_dick_low_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_anal_dick_low_fast_action


### DICK MED

    elif mc_body.store["dick"] == "Anal_dick_med":

        show afternight04_sexbattle_d_legs_pussy empty


        # PUBIC PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        # TOP PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_fast_action


        # TOP ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_stop_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_slow_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_mod_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_med_fast_action

        # LEGS OVER ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_stop_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_slow_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_mod_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_fast_action

        # LEGS ANAL

        if mc_body.dick_speed == 0:

            #show afternight04_sexbattle_d_legs_base PROVE_a:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_med_fast_action

        # DICK

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_med_stop_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_med_slow_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_med_mod_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_med_fast_action

### ANAL DEEP

    elif mc_body.store["dick"] == "Anal_dick_deep":

        show afternight04_sexbattle_d_legs_pussy empty

        # PUBIC ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_anal 06_wet_00_a

        # TOP PUSSY

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_top_pussy 06b_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_fast_action


        # TOP ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_stop_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_slow_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_mod_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_top_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_pubic_deep_fast_action

        # LEGS OVER ANAL

        if mc_body.dick_speed == 0:

            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_stop_action

        elif mc_body.dick_speed == 1:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_slow_action

        elif mc_body.dick_speed == 2:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_mod_action

        elif mc_body.dick_speed == 3:
            
            show afternight04_sexbattle_d_legs_over_anal 06_wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_fast_action

        # LEGS ANAL

        if mc_body.dick_speed == 0:

            #show afternight04_sexbattle_d_legs_base PROVE_a:
            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_stop_action

        elif mc_body.dick_speed == 1:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_slow_action

        elif mc_body.dick_speed == 2:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_mod_action

        elif mc_body.dick_speed == 3:

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_d_anal_legs_deep_fast_action

        # DICK ANAL DEEP

        if mc_body.dick_speed == 0:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_deep_stop_action

        elif mc_body.dick_speed == 1:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_deep_slow_action

        elif mc_body.dick_speed == 2:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_deep_mod_action

        elif mc_body.dick_speed == 3:
            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                afternight04_sexbattle_d_anal_dick_deep_fast_action

        # STOMACH PUSSY DEEP

        if mc_body.dick_speed == 0:
        
            show afternight04_sexbattle_d_legs_stomach_anal wet_00_a:
                afternight04_sexbattle_d_anal_stomach_deep_stop_action

        elif mc_body.dick_speed == 1:
        
            show afternight04_sexbattle_d_legs_stomach_anal wet_00_a:
                afternight04_sexbattle_d_anal_stomach_deep_slow_action

        elif mc_body.dick_speed == 2:
        
            show afternight04_sexbattle_d_legs_stomach_anal wet_00_a:
                afternight04_sexbattle_d_anal_stomach_deep_mod_action

        elif mc_body.dick_speed == 3:
        
            show afternight04_sexbattle_d_legs_stomach_anal wet_00_a:
                afternight04_sexbattle_d_anal_stomach_deep_fast_action


    return


image afternight04_sexbattle_mc_dick_anal general:

    afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0

    contains:

        ConditionSwitch(
            mc_body.store["dick"] == "Anal_dick_out", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_anal_legs_low_stop_action),
            mc_body.store["dick"] == "Anal_dick_low", At ("afternight04_sexbattle_d_legs_pussy 02_wet_00_a", 
                afternight04_sexbattle_d_anal_legs_low_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_slow_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_mod_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_fast_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_stop_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_slow_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_mod_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_fast_action),
            "True", Null())

    contains:

        #alpha 0.5

        ConditionSwitch(
            mc_body.store["dick"] == "Anal_dick_out", At ("afternight04_sexbattle_mc_dick_anal empty", 
                afternight04_sexbattle_d_anal_dick_low_stop_action),
            mc_body.store["dick"] == "", At ("afternight04_sexbattle_mc_dick_anal empty", 
                afternight04_sexbattle_d_anal_dick_low_stop_action),
            mc_body.store["dick"] == "Anal_dick_low" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_low_stop_action),
            mc_body.store["dick"] == "Anal_dick_low" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_low_slow_action),
            mc_body.store["dick"] == "Anal_dick_low" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_low_mod_action),
            mc_body.store["dick"] == "Anal_dick_low" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_low_fast_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_med_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_med_slow_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_med_mod_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_med_fast_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_deep_stop_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_deep_slow_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_deep_mod_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_mc_dick_anal condom_wet_00_a", afternight04_sexbattle_d_anal_dick_deep_fast_action),
            "True", Null())

    contains:
        #alpha 0.5
        ConditionSwitch(
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_med_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_med_slow_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_med_mod_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_med_fast_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_deep_stop_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_deep_slow_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_deep_mod_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_stomach_pussy wet_00_a", afternight04_sexbattle_d_anal_stomach_deep_fast_action),
            "True", Null())

    contains:

        #ConditionSwitch(
            #mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a"),
            #"True", Null())

        ConditionSwitch(
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_slow_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_mod_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_med_fast_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_stop_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_slow_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_mod_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_over_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_legs_deep_fast_action),
            "True", Null())

    contains:

        ConditionSwitch(
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_med_stop_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_med_slow_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_med_mod_action),
            mc_body.store["dick"] == "Anal_dick_med" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_med_fast_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 0", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_deep_stop_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 1", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_deep_slow_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 2", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_deep_mod_action),
            mc_body.store["dick"] == "Anal_dick_deep" and "mc_body.dick_speed == 3", At ("afternight04_sexbattle_d_legs_top_pussy 06_wet_00_a", afternight04_sexbattle_d_anal_deep_fast_action),
            "True", Null())