########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
####################################################################################################### DICK_a IMAGE

##Dick Low-Med-Deep Slow-Mod-Fast penetration
label afternight04_Pussy_dick_general_image:

    if mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "":
        $ debug ("Dick out &-")

    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0:
        $ debug ("Dick low speed 0 &-")
        #$ afternight04_Pussy_dick_low_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1:
        $ debug ("Dick low speed 1 &-")
        #$ afternight04_Pussy_dick_low_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2:
        $ debug ("Dick low speed 2 &-")
        #$ afternight04_Pussy_dick_low_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3:
        $ debug ("Dick low speed 3 &-")
        #$ afternight04_Pussy_dick_low_Speed_3_Done += 1

    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 0:
        $ debug ("Dick med speed 0 &-")
        #$ afternight04_Pussy_dick_med_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1:
        $ debug ("Dick med speed 1 &-")
        #$ afternight04_Pussy_dick_med_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2:
        $ debug ("Dick med speed 2 &-")
        #$ afternight04_Pussy_dick_med_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3:
        $ debug ("Dick med speed 3 &-")
        #$ afternight04_Pussy_dick_med_Speed_3_Done += 1

    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 0:
        $ debug ("Dick deep speed 0 &-")
        #$ afternight04_Pussy_dick_deep_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1:
        $ debug ("Dick deep speed 1 &-")
        #$ afternight04_Pussy_dick_deep_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2:
        $ debug ("Dick deep speed 2 &-")
        #$ afternight04_Pussy_dick_deep_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3:
        $ debug ("Dick deep speed 3 &-")
        #$ afternight04_Pussy_dick_deep_Speed_3_Done += 1

    else:
        $ debug ("Dick what the fuck? This message should not appear 0841.")


    if current_pose.id == "pose_1":

        $ mc_body.store["tongue"] = ""

        if (mc_body.store["right_hand"] == "LButtock_Massage"):

            $ mc_body.store["right_hand"] == ""
            show afternight04_sexbattle_mc_handR empty

        if (mc_body.store["left_hand"] == "RButtock_Massage"):

            $ mc_body.store["left_hand"] == ""
            show afternight04_sexbattle_mc_handL empty

# MC HAND Right

        if mc_body.store["right_hand"] == "Pussy_Fingers" or mc_body.store["right_hand"] == "MClitoris_Massage":
            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

# MC HandR_PENETRATE

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        #show afternight04_sexbattle_mc_handR_penetrate_anal empty

# MC_TONGUE

        show afternight04_sexbattle_mc_tongue_pussy empty
        show afternight04_sexbattle_mc_tongue_clitoris empty

# PUSSY

        show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
            afternight04_sexbattle_d_pubicpart_pos

# ANAL

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
            afternight04_sexbattle_d_pubicpart_pos

# TOP PUSSY

        show afternight04_sexbattle_d_legs_top_pussy empty:
            afternight04_sexbattle_d_pubicpart_pos

# TOP ANAL

        show afternight04_sexbattle_d_legs_top_anal empty:
            afternight04_sexbattle_d_pubicpart_pos

# LEGS OVER ANAL

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_position

# LEGS OVER ANAL

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_position

# LEGS

        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_empty_position

# STOMACH

        show afternight04_sexbattle_d_legs_stomach_pussy empty:
            afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_position

# DICK
        show afternight04_sexbattle_mc_dick_pussy empty #PUSSY DICK EMPTY POSE 01
        show afternight04_sexbattle_mc_dick_anal empty #PUSSY DICK EMPTY POSE 01


        #show afternight04_sexbattle_mc_dick_pussy general #Dick Penetration for a.
        call afternight04_sexbattle_mc_dick_pussy_pose01_scene #Dick PUSSY Penetration for a.

        with dissolve

#######
######
#####
####### POSE 02-03

    else:

        $ debug ("PUSSY Bitch")

        $ mc_body.store["tongue"] = ""
        show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_mc_tongue_pussy empty

        if mc_body.store["right_hand"] == "Pussy_Fingers" or mc_body.store["right_hand"] == "MClitoris_Massage":
            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        #show afternight04_sexbattle_mc_tongue_pussy empty
        #show afternight04_sexbattle_mc_tongue_clitoris empty

        #show afternight04_sexbattle_d_legs_anal 002_wet_00_b
        #show afternight04_sexbattle_d_legs_anal_over empty

        #show afternight04_sexbattle_mc_tongue_anal empty
        #show afternight04_sexbattle_mc_handR_penetrate_anal empty

        show afternight04_sexbattle_mc_dick_anal empty #ANAL EMPTY POSE 02

        call afternight04_sexbattle_mc_dick_Pussy_general_doggystyle_scene # Dick Penetration for b and c


        with dissolve

        $ debug ("Final PUSSY Bitch")

    #return

        ####################
        ####################
        #################### SEX after Dialogue

    if mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "":
        $ debug ("Dick out -")

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0:
        $ debug ("Dick low speed 0 -")
        #$ afternight04_Pussy_dick_low_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1:
        $ debug ("Dick low speed 1 -")
        #$ afternight04_Pussy_dick_low_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2:
        $ debug ("Dick low speed 2 -")
        #$ afternight04_Pussy_dick_low_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3:
        $ debug ("Dick low speed 3 -")
        #$ afternight04_Pussy_dick_low_Speed_3_Done += 1

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 0:
        $ debug ("Dick med speed 0 -")
        #$ afternight04_Pussy_dick_med_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1:
        $ debug ("Dick med speed 1 -")
        #$ afternight04_Pussy_dick_med_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2:
        $ debug ("Dick med speed 2 -")
        #$ afternight04_Pussy_dick_med_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3:
        $ debug ("Dick med speed 3 -")
        #$ afternight04_Pussy_dick_med_Speed_3_Done += 1

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 0:
        $ debug ("Dick deep speed 0 -")
        #$ afternight04_Pussy_dick_deep_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1:
        $ debug ("Dick deep speed 1 -")
        #$ afternight04_Pussy_dick_deep_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2:
        $ debug ("Dick deep speed 2 -")
        #$ afternight04_Pussy_dick_deep_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3:
        $ debug ("Dick deep speed 3 -")
        #$ afternight04_Pussy_dick_deep_Speed_3_Done += 1

        ####################
        ####################
        ####################

    else:
        $ debug ("Dick what the fuck? This message should not appear 0842.")

        ####################
        ####################
        ####################

    return



########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
####################################################################################################### RAPE IMAGE

label afternight04_Pussy_dick_rape_general_image:


    if (afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0) or (afternight04_Pussy_dick_deep_Speed_3_Success > 0):
        $ debug ("Dick deep speed 3 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_deep"
        $ mc_body.dick_speed = 3

    elif (afternight04_Pussy_dick_deep_Speed_2_Rape_Done > 0) or (afternight04_Pussy_dick_deep_Speed_2_Success > 0):
        $ debug ("Dick deep speed 2 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_deep"
        $ mc_body.dick_speed = 2

    elif (afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0) or (afternight04_Pussy_dick_deep_Speed_1_Success > 0):
        $ debug ("Dick deep speed 1 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_deep"
        $ mc_body.dick_speed = 1

    elif (afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0) or (afternight04_Pussy_dick_deep_Speed_0_Success > 0):
        $ debug ("Dick deep speed 0 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_deep"
        $ mc_body.dick_speed = 0

    #

    elif (afternight04_Pussy_dick_med_Speed_3_Rape_Done > 0) or (afternight04_Pussy_dick_med_Speed_3_Done > 0):
        $ debug ("Dick med speed 3 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_med"
        $ mc_body.dick_speed = 3

    elif (afternight04_Pussy_dick_med_Speed_2_Rape_Done > 0) or (afternight04_Pussy_dick_med_Speed_2_Done > 0):
        $ debug ("Dick med speed 2 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_med"
        $ mc_body.dick_speed = 2

    elif (afternight04_Pussy_dick_med_Speed_1_Rape_Done > 0) or (afternight04_Pussy_dick_med_Speed_1_Done > 0):
        $ debug ("Dick med speed 1 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_med"
        $ mc_body.dick_speed = 1

    elif (afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0) or (afternight04_Pussy_dick_med_Speed_0_Done > 0):
        $ debug ("Dick med speed 0 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_med"
        $ mc_body.dick_speed = 0

    #

    elif (afternight04_Pussy_dick_low_Speed_3_Rape_Done > 0) or (afternight04_Pussy_dick_low_Speed_3_Done > 0):
        $ debug ("Dick low speed 3 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_low"
        $ mc_body.dick_speed = 3

    elif (afternight04_Pussy_dick_low_Speed_2_Rape_Done > 0) or (afternight04_Pussy_dick_low_Speed_2_Done > 0):
        $ debug ("Dick low speed 2 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_low"
        $ mc_body.dick_speed = 2

    elif (afternight04_Pussy_dick_low_Speed_1_Rape_Done > 0) or (afternight04_Pussy_dick_low_Speed_1_Done > 0):
        $ debug ("Dick low speed 1 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_low"
        $ mc_body.dick_speed = 1

    elif (afternight04_Pussy_dick_low_Speed_0_Rape_Done > 0) or (afternight04_Pussy_dick_low_Speed_0_Done > 0):
        $ debug ("Dick low speed 0 rape *-")

        $ mc_body.store["dick"] = "Pussy_dick_low"
        $ mc_body.dick_speed = 0

    #
    elif (mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == ""):
        $ debug ("Dick out *-")

    
    # elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3:
    #     $ debug ("Dick low speed 3 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2:
    #     $ debug ("Dick low speed 2 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1:
    #     $ debug ("Dick low speed 1 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0:
    #     $ debug ("Dick low speed 0 rape *-")

    # elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3:
    #     $ debug ("Dick med speed 3 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2:
    #     $ debug ("Dick med speed 2 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1:
    #     $ debug ("Dick med speed 1 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 0:
    #     $ debug ("Dick med speed 0 rape *-")
    

    # elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 0:
    #     $ debug ("Dick deep speed 0 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1:
    #     $ debug ("Dick deep speed 1 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2:
    #     $ debug ("Dick deep speed 2 rape *-")
    # elif mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3:
    #     $ debug ("Dick deep speed 3 rape *-")

    else:
        $ debug ("Dick what the fuck? This message should not appear 0846.")


    $ mc_body.store["right_hand"] = ""
    $ mc_body.store["left_hand"] = ""
    $ mc_body.store["tongue"] = ""
    #$ mc_body.store["dick"] = "Pussy_dick_out" #She´s raping you, so no need to change this.

    #call afternight04_sexbattle_scene_pose01  ## IN THEORY, NOT NECESSARY.

####


    if current_pose.id == "pose_1":

# MC HAND Right

        show afternight04_sexbattle_mc_handR empty

# MC HAND Left

        show afternight04_sexbattle_mc_handL empty

# MC HandR_PENETRATE

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        #show afternight04_sexbattle_mc_handR_penetrate_anal empty

# MC_TONGUE

        show afternight04_sexbattle_mc_tongue_pussy empty
        show afternight04_sexbattle_mc_tongue_clitoris empty

# PUSSY
        if mc_body.store["dick"] == "Pussy_dick_low":
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

# ANAL

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
            afternight04_sexbattle_d_pubicpart_pos

# TOP PUSSY
        if mc_body.store["dick"] == "Pussy_dick_low":
            show afternight04_sexbattle_d_legs_top_pussy empty:
                afternight04_sexbattle_d_pubicpart_pos

# TOP ANAL

        show afternight04_sexbattle_d_legs_top_anal empty:
            afternight04_sexbattle_d_pubicpart_pos

# LEGS OVER ANAL

        show afternight04_sexbattle_d_legs_over_anal empty:
            afternight04_sexbattle_empty_position

# LEGS OVER ANAL

        show afternight04_sexbattle_d_legs_over_pussy empty:
            afternight04_sexbattle_empty_position

# LEGS

        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_empty_position

# STOMACH
        if mc_body.store["dick"] == "Pussy_dick_low":
            show afternight04_sexbattle_d_legs_stomach_pussy empty:
                afternight04_sexbattle_empty_position

        show afternight04_sexbattle_d_legs_stomach_anal empty:
            afternight04_sexbattle_empty_position


# DICK
        show afternight04_sexbattle_mc_dick_pussy empty #PUSSY DICK EMPTY POSE 01
        show afternight04_sexbattle_mc_dick_anal empty #PUSSY DICK EMPTY POSE 01


        #show afternight04_sexbattle_mc_dick_pussy rape_general
        call afternight04_sexbattle_mc_dick_pussy_rape_general

        if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
            with vpunch
        else:
            with dissolve

    $ debug ("BITCH")
    call afternight04_Pussy_dick_rape_general_dialogue

    return


label afternight04_sexbattle_scene_pose01:

    scene afternight04_sexbattle_background a:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_body a:
        afternight04_sexbattle_empty_NOposition

    
    if afternight04_CumOnStomach == 0:
        show afternight04_sexbattle_mc_cum_stomach empty:
            afternight04_sexbattle_empty_NOposition
    if afternight04_CumOnStomach == 1:
        show afternight04_sexbattle_mc_cum_stomach just_01_action_a:
            afternight04_sexbattle_empty_NOposition
    elif afternight04_CumOnStomach == 2:
        show afternight04_sexbattle_mc_cum_stomach over_01-02_action_a:
            afternight04_sexbattle_empty_NOposition
    elif afternight04_CumOnStomach == 3:
        show afternight04_sexbattle_mc_cum_stomach over_01-02-03_action_a:
            afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_blush 00_a:
        afternight04_sexbattle_d_expressions_pos
    show afternight04_sexbattle_d_eyes 01_a:
        afternight04_sexbattle_d_expressions_pos
    show afternight04_sexbattle_d_pupils front01_a:
        afternight04_sexbattle_d_expressions_pos
    show afternight04_sexbattle_d_eyebrows angryx02_a:
        afternight04_sexbattle_d_expressions_pos
    show afternight04_sexbattle_d_hair a:
        afternight04_sexbattle_d_expressions_pos
    show afternight04_sexbattle_d_mouth happy_Silentx03_a:
        afternight04_sexbattle_d_expressions_pos

    show afternight04_sexbattle_d_boobL wet_00_smash_00_a_static: #Apparently they are necessary...
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_d_boobR wet_00_smash_00_a_static:
        afternight04_sexbattle_empty_NOposition

    #if pose01_right_boob.get_action("RBoob_Slap").times_done + pose01_right_boob.get_action("RBoob_Slap").times_failed == 0: 
    if (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 0:
        show afternight04_sexbattle_d_boobR wet_00_smash_00_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 1:
        show afternight04_sexbattle_d_boobR wet_00_smash_01_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 2:
        show afternight04_sexbattle_d_boobR wet_00_smash_02_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 3:
        show afternight04_sexbattle_d_boobR wet_00_smash_03_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 4:
        show afternight04_sexbattle_d_boobR wet_00_smash_04_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 5:
        show afternight04_sexbattle_d_boobR wet_00_smash_05_a_static
    elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) >= 6:
        show afternight04_sexbattle_d_boobR wet_00_smash_06_a_static

    #if pose01_left_boob.get_action("LBoob_Slap").times_done + pose01_left_boob.get_action("LBoob_Slap").times_failed == 0:
    if (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 0:
        show afternight04_sexbattle_d_boobL wet_00_smash_00_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 1:
        show afternight04_sexbattle_d_boobL wet_00_smash_01_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 2:
        show afternight04_sexbattle_d_boobL wet_00_smash_02_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 3:
        show afternight04_sexbattle_d_boobL wet_00_smash_03_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 4:
        show afternight04_sexbattle_d_boobL wet_00_smash_04_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 5:
        show afternight04_sexbattle_d_boobL wet_00_smash_05_a_static
    elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) >= 6:
        show afternight04_sexbattle_d_boobL wet_00_smash_06_a_static

    show afternight04_sexbattle_dvaporbreathing 00:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_legs_base wet_00_a:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
        afternight04_sexbattle_d_pubicpart_pos
    show afternight04_sexbattle_mc_cumshot empty:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_mc_dick_anal empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_mc_tongue_anal empty:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_legs_stomach_anal empty:
        afternight04_sexbattle_empty_NOposition


    show afternight04_sexbattle_mc_handR_penetrate_anal empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_d_legs_over_anal empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_d_legs_top_anal empty:
        afternight04_sexbattle_d_pubicpart_pos

    show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
        afternight04_sexbattle_d_pubicpart_pos

    show afternight04_sexbattle_mc_tongue_pussy empty: 
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_mc_dick_pussy empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_mc_dick_pussy_cumshot empty:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_d_legs_stomach_pussy empty:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_mc_handR_penetrate_pussy empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_d_legs_over_pussy empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_d_legs_top_pussy empty:
        afternight04_sexbattle_d_pubicpart_pos

    show afternight04_sexbattle_mc_handL empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_mc_handR empty:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_didac_squirt 000_a:
        afternight04_sexbattle_empty_NOposition
    show afternight04_sexbattle_mc_tongue_clitoris empty:
        afternight04_sexbattle_empty_NOposition

    show afternight04_sexbattle_effects empty:
        afternight04_sexbattle_empty_NOposition


    return


########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
##
##

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
####################################################################################################### ANAL DICK_a IMAGE

##Dick Low-Med-Deep Slow-Mod-Fast penetration
label afternight04_Anal_dick_general_image:

    if mc_body.store["dick"] == "Anal_dick_out":
        $ debug ("Dick ANAL out -")

    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 0:
        $ debug ("Dick ANAL low speed 0 -")
        #$ afternight04_Anal_dick_low_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 1:
        $ debug ("Dick ANAL low speed 1 -")
        #$ afternight04_Anal_dick_low_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 2:
        $ debug ("Dick ANAL low speed 2 -")
        #$ afternight04_Anal_dick_low_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 3:
        $ debug ("Dick ANAL low speed 3 -")
        #$ afternight04_Anal_dick_low_Speed_3_Done += 1

    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 0:
        $ debug ("Dick ANAL med speed 0 -")
        #$ afternight04_Anal_dick_med_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 1:
        $ debug ("Dick ANAL med speed 1 -")
        #$ afternight04_Anal_dick_med_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 2:
        $ debug ("Dick ANAL med speed 2 -")
        #$ afternight04_Anal_dick_med_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 3:
        $ debug ("Dick ANAL med speed 3 -")
        #$ afternight04_Anal_dick_med_Speed_3_Done += 1

    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 0:
        $ debug ("Dick ANAL deep speed 0 -")
        #$ afternight04_Anal_dick_deep_Speed_0_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 1:
        $ debug ("Dick ANAL deep speed 1 -")
        #$ afternight04_Anal_dick_deep_Speed_1_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 2:
        $ debug ("Dick ANAL deep speed 2 -")
        #$ afternight04_Anal_dick_deep_Speed_2_Done += 1
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 3:
        $ debug ("Dick ANAL deep speed 3 -")
        #$ afternight04_Anal_dick_deep_Speed_3_Done += 1

    else:
        $ debug ("Dick ANAL what the fuck? This message should not appear 0843.")

    if current_pose.id == "pose_1":

        $ mc_body.store["tongue"] = ""

        if (mc_body.store["dick"] == "Anal_dick_low") and (mc_body.store["right_hand"] == "Pussy_Fingers"):

            $ debug ("Anal low, Pussy Fingering must remain same.")

        if (mc_body.store["right_hand"] == "LButtock_Massage"):

            $ mc_body.store["right_hand"] == ""
            show afternight04_sexbattle_mc_handR empty

        if (mc_body.store["left_hand"] == "RButtock_Massage"):

            $ mc_body.store["left_hand"] == ""
            show afternight04_sexbattle_mc_handL empty

        else:

    # MC HAND Right

            if mc_body.store["right_hand"] == "Pussy_Fingers" or mc_body.store["right_hand"] == "Anal_Fingers":
                $ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty

    # MC HandR_PENETRATE

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
            #show afternight04_sexbattle_mc_handR_penetrate_anal empty

    # MC_TONGUE

            #show afternight04_sexbattle_mc_tongue_pussy empty
            #show afternight04_sexbattle_mc_tongue_clitoris empty

    # PUSSY

            #show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                #afternight04_sexbattle_d_pubicpart_pos

    # ANAL

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

    # TOP PUSSY

            #show afternight04_sexbattle_d_legs_top_pussy empty:
                #afternight04_sexbattle_d_pubicpart_pos

    # TOP ANAL

            show afternight04_sexbattle_d_legs_top_anal empty:
                afternight04_sexbattle_d_pubicpart_pos

    # LEGS OVER ANAL

            show afternight04_sexbattle_d_legs_over_anal empty:
                afternight04_sexbattle_empty_position

    # LEGS OVER ANAL

            show afternight04_sexbattle_d_legs_over_pussy empty:
                afternight04_sexbattle_empty_position

    # LEGS

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_empty_position

    # STOMACH

            show afternight04_sexbattle_d_legs_stomach_pussy empty:
                afternight04_sexbattle_empty_position

            show afternight04_sexbattle_d_legs_stomach_anal empty:
                afternight04_sexbattle_empty_position

    # DICK
            show afternight04_sexbattle_mc_dick_pussy empty #PUSSY DICK EMPTY POSE 01
            show afternight04_sexbattle_mc_dick_anal empty #PUSSY DICK EMPTY POSE 01


        call afternight04_sexbattle_mc_dick_anal_pose01_scene
        #show afternight04_sexbattle_mc_dick_anal general

        with dissolve


#######################
######################
#####################
####################
####################### POSE 02-03
    else:

        $ debug ("Anal Bitch")

        $ mc_body.store["tongue"] = ""
        #show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_d_anal_tongue empty

        if mc_body.store["right_hand"] == "Pussy_Fingers" or mc_body.store["right_hand"] == "MClitoris_Massage":
            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty
    
        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        #show afternight04_sexbattle_mc_handR_penetrate_anal empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        #show afternight04_sexbattle_mc_tongue_pussy empty
        #show afternight04_sexbattle_mc_tongue_clitoris empty

        #show afternight04_sexbattle_d_legs_anal 002_wet_00_b

        show afternight04_sexbattle_mc_tongue_anal empty
        show afternight04_sexbattle_mc_handR_penetrate_anal empty

        show afternight04_sexbattle_mc_dick_pussy empty #PUSSY DICK EMPTY POSE 02

        $ debug ("Now ANAL sex.")

        call afternight04_sexbattle_mc_dick_Anal_general_doggystyle_scene # Dick Penetration for b and c
        with dissolve

        $ debug ("Final Anal Bitch")

    #return

        ####################
        ####################
        #################### SEX after Dialogue

    if mc_body.store["dick"] == "Anal_dick_out":
        $ debug ("Dick out -")

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 0:
        $ debug ("Dick low speed 0 -")
        #$ afternight04_Anal_dick_low_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 1:
        $ debug ("Dick low speed 1 -")
        #$ afternight04_Anal_dick_low_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 2:
        $ debug ("Dick low speed 2 -")
        #$ afternight04_Anal_dick_low_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_low" and mc_body.dick_speed == 3:
        $ debug ("Dick low speed 3 -")
        #$ afternight04_Anal_dick_low_Speed_3_Done += 1

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 0:
        $ debug ("Dick med speed 0 -")
        #$ afternight04_Anal_dick_med_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 1:
        $ debug ("Dick med speed 1 -")
        #$ afternight04_Anal_dick_med_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 2:
        $ debug ("Dick med speed 2 -")
        #$ afternight04_Anal_dick_med_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_med" and mc_body.dick_speed == 3:
        $ debug ("Dick med speed 3 -")
        #$ afternight04_Anal_dick_med_Speed_3_Done += 1

        ####################
        ####################
        ####################

    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 0:
        $ debug ("Dick deep speed 0 -")
        #$ afternight04_Anal_dick_deep_Speed_0_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 1:
        $ debug ("Dick deep speed 1 -")
        #$ afternight04_Anal_dick_deep_Speed_1_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 2:
        $ debug ("Dick deep speed 2 -")
        #$ afternight04_Anal_dick_deep_Speed_2_Done += 1

        ####################
    elif mc_body.store["dick"] == "Anal_dick_deep" and mc_body.dick_speed == 3:
        $ debug ("Dick deep speed 3 -")
        #$ afternight04_Anal_dick_deep_Speed_3_Done += 1

        ####################
        ####################
        ####################

    else:
        $ debug ("Dick what the fuck? This message should not appear 0844.")

        ####################
        ####################
        ####################

    return



########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################