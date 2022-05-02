default afternight04_mcbodyorgasm_advise_01 = 0
default afternight04_mcbodyorgasm_advise_02 = 0
default afternight04_mcbodyorgasm_advise_03 = 0

default afternight04_mcbodyorgasm_remind_01 = False
default afternight04_mcbodyorgasm_remind_02 = False
default afternight04_mcbodyorgasm_remind_03 = False

##################
##################
    ## CHECK_AFTER >


label afternight04_sex_check_after:

###########
    ###########
    ###################################################################### SEX POINTS IN GENERAL

    call afternight04_SexPointsGeneral

###########
    ###########
    ###################################################################### POINTS DICK RAPE

    if afternight04_SheRapingYou == True:

        if (mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

    ###

            if mc_body.store["dick"] == "Pussy_dick_deep": ### DEEP RAPE

                if mc_body.dick_speed == 3: # FAST DEEP

                    if afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 1:
                        $ mc_body.pleasure += 48 # default 16
                        $ current_girl.pleasure += 26 # 5
                    elif afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 2:
                        $ mc_body.pleasure += 45 # 15
                        $ current_girl.pleasure += 24 # 4
                    elif afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 3:
                        $ mc_body.pleasure += 42 # 14
                        $ current_girl.pleasure += 22 # 4
                    else:
                        $ mc_body.pleasure += 39 # 13
                        $ current_girl.pleasure += 15 # 3

                elif mc_body.dick_speed == 2: # MOD DEEP

                    if afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 1:
                        $ mc_body.pleasure += 39 #13
                        $ current_girl.pleasure += 20 #4
                    elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 2:
                        $ mc_body.pleasure += 36 #12
                        $ current_girl.pleasure += 15 #3
                    elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 3:
                        $ mc_body.pleasure += 33 #11
                        $ current_girl.pleasure += 13 #2
                    else:
                        $ mc_body.pleasure += 30 #10
                        $ current_girl.pleasure += 10 #2

                elif mc_body.dick_speed == 1: # SLOW DEEP

                    if afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 1:
                        $ mc_body.pleasure += 33 #11
                        $ current_girl.pleasure += 15 #4
                    elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 2:
                        $ mc_body.pleasure += 30 #10
                        $ current_girl.pleasure += 13 #3
                    elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 3:
                        $ mc_body.pleasure += 27 #9
                        $ current_girl.pleasure += 10 #2
                    else:
                        $ mc_body.pleasure += 24 #8
                        $ current_girl.pleasure += 8 #1

                elif mc_body.dick_speed == 0: # STOP DEEP

                    if afternight04_Pussy_dick_deep_Speed_0_Rape_Done == 1:
                        $ mc_body.pleasure += 15 #5
                        $ current_girl.pleasure += 8 #2
                    else:
                        $ mc_body.pleasure += 12 #4
                        $ current_girl.pleasure += 3 #1

    ###

            elif mc_body.store["dick"] == "Pussy_dick_med": ### MEDium RAPE

                if mc_body.dick_speed == 3: # FAST MED

                    if afternight04_Pussy_dick_med_Speed_3_Rape_Done == 1:
                        $ mc_body.pleasure += 36 #12
                        $ current_girl.pleasure += 12 #3
                    elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 2:
                        $ mc_body.pleasure += 33 #11
                        $ current_girl.pleasure += 11 #2
                    elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 3:
                        $ mc_body.pleasure += 30 #10
                        $ current_girl.pleasure += 10 #2
                    else:
                        $ mc_body.pleasure += 30 #10
                        $ current_girl.pleasure += 10 #1

                elif mc_body.dick_speed == 2: # MOD MED

                    if afternight04_Pussy_dick_med_Speed_2_Rape_Done == 1:
                        $ mc_body.pleasure += 30 #10
                        $ current_girl.pleasure += 10 #2
                    elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 2:
                        $ mc_body.pleasure += 28 #9
                        $ current_girl.pleasure += 9 #2
                    elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 3:
                        $ mc_body.pleasure += 24 #8
                        $ current_girl.pleasure += 8 #1
                    else:
                        $ mc_body.pleasure += 14 #7
                        $ current_girl.pleasure += 7 #1

                elif mc_body.dick_speed == 1: # SLOW MED

                    if afternight04_Pussy_dick_med_Speed_1_Rape_Done == 1:
                        $ mc_body.pleasure += 24 #8
                        $ current_girl.pleasure += 8 #2
                    elif afternight04_Pussy_dick_med_Speed_1_Rape_Done == 2:
                        $ mc_body.pleasure += 21 #7
                        $ current_girl.pleasure += 7 #2
                    elif afternight04_Pussy_dick_med_Speed_1_Rape_Done == 3:
                        $ mc_body.pleasure += 18 #6
                        $ current_girl.pleasure += 6 #1
                    else:
                        $ mc_body.pleasure += 15 #5
                        $ current_girl.pleasure += 5 #1

                elif mc_body.dick_speed == 0: # STOP MED

                    if afternight04_Pussy_dick_med_Speed_0_Rape_Done == 1:
                        $ mc_body.pleasure += 12 #4
                        $ current_girl.pleasure += 4 #1
                    else:
                        $ mc_body.pleasure += 9 #3
                        $ current_girl.pleasure += 3 #1

    ###

            elif mc_body.store["dick"] == "Pussy_dick_low": ### LOW RAPE

                if mc_body.dick_speed == 3: # FAST LOW

                    if afternight04_Pussy_dick_low_Speed_3_Rape_Done == 1:
                        $ mc_body.pleasure += 18 #6
                        $ current_girl.pleasure += 6 #2
                    elif afternight04_Pussy_dick_low_Speed_3_Rape_Done == 2:
                        $ mc_body.pleasure += 15 #5
                        $ current_girl.pleasure += 5 #2
                    elif afternight04_Pussy_dick_low_Speed_3_Rape_Done == 3:
                        $ mc_body.pleasure += 15 #5
                        $ current_girl.pleasure += 4 #1
                    else:
                        $ mc_body.pleasure += 12 #4 # TIP: Same Result than her in not raping.
                        $ current_girl.pleasure += 4 #1

                elif mc_body.dick_speed == 2: # MOD LOW

                    if afternight04_Pussy_dick_low_Speed_2_Rape_Done == 1:
                        $ mc_body.pleasure += 15 #5
                        $ current_girl.pleasure += 5 #2
                    elif afternight04_Pussy_dick_low_Speed_2_Rape_Done == 2:
                        $ mc_body.pleasure += 12 #4
                        $ current_girl.pleasure += 4 #2
                    elif afternight04_Pussy_dick_low_Speed_2_Rape_Done == 3:
                        $ mc_body.pleasure += 9 #3
                        $ current_girl.pleasure += 3 #1
                    else:
                        $ mc_body.pleasure += 9 #3
                        $ current_girl.pleasure += 2 #1

                elif mc_body.dick_speed == 1: # SLOW LOW

                    if afternight04_Pussy_dick_low_Speed_1_Rape_Done == 1:
                        $ mc_body.pleasure += 12 #4
                        $ current_girl.pleasure += 4 #1
                    elif afternight04_Pussy_dick_low_Speed_1_Rape_Done == 2:
                        $ mc_body.pleasure += 9 #3
                        $ current_girl.pleasure += 3 #1
                    elif afternight04_Pussy_dick_low_Speed_1_Rape_Done == 3:
                        $ mc_body.pleasure += 6 #2
                        $ current_girl.pleasure += 2 #1
                    else:
                        $ mc_body.pleasure += 6 #2
                        $ current_girl.pleasure += 1 #1

                elif mc_body.dick_speed == 0: # STOP LOW

                    if afternight04_Pussy_dick_low_Speed_0_Rape_Done == 1:
                        $ mc_body.pleasure += 5 #1
                        $ current_girl.pleasure += 1 #1
                    elif afternight04_Pussy_dick_low_Speed_0_Rape_Done == 2:
                        $ mc_body.pleasure += 4 #1
                    else:
                        $ mc_body.pleasure += 3 #1

    ###

            #There´s no need for dick_out for RAPE.

    ############################
    ###########################

        # Slap Action is not acumulative. You need to slap again to gain points.

    if mc_body.store["right_hand"] == "LBoob_Slap":
        $ mc_body.store ["right_hand"] = ""
    if mc_body.store["left_hand"] == "RBoob_Slap":
        $ mc_body.store ["left_hand"] = ""

    ############################
    ###########################

    #if (mc_body.orgasm == 0 and mc_body.pleasure in range (25, 34)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (50, 74)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (75, 110)):
    if (((mc_body.orgasm == 0 and mc_body.pleasure in range (25, 34)) and afternight04_mcbodyorgasm_advise_01 == 0) or 
        ((mc_body.orgasm == 1 and mc_body.pleasure in range (50, 59)) and afternight04_mcbodyorgasm_advise_01 == 1) or 
        ((mc_body.orgasm == 2 and mc_body.pleasure in range (70, 79)) and afternight04_mcbodyorgasm_advise_01 == 2)):

        if (mc_body.orgasm == 0) and (afternight04_mcbodyorgasm_advise_01 == 0):
            $ afternight04_mcbodyorgasm_advise_01 = 1
        elif (mc_body.orgasm == 1) and (afternight04_mcbodyorgasm_advise_01 == 1):
            $ afternight04_mcbodyorgasm_advise_01 = 2
        elif (mc_body.orgasm == 2) and (afternight04_mcbodyorgasm_advise_01 == 2):
            $ afternight04_mcbodyorgasm_advise_01 = 3

        pt "Empiezo a notar que no tardaré demasiado en acabar..."

    #elif (mc_body.orgasm == 0 and mc_body.pleasure in range (35, 40)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (75, 89)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (111, 135)):
    elif (((mc_body.orgasm == 0 and mc_body.pleasure in range (35, 40)) and afternight04_mcbodyorgasm_advise_01 == 0) or  
        ((mc_body.orgasm == 1 and mc_body.pleasure in range (60, 69)) and afternight04_mcbodyorgasm_advise_02 == 1) or 
        ((mc_body.orgasm == 2 and mc_body.pleasure in range (80, 89)) and afternight04_mcbodyorgasm_advise_02 == 2)):

        if (mc_body.orgasm == 0) and (afternight04_mcbodyorgasm_advise_02 == 0):
            $ afternight04_mcbodyorgasm_advise_02 = 1
        elif (mc_body.orgasm == 1) and (afternight04_mcbodyorgasm_advise_02 == 1):
            $ afternight04_mcbodyorgasm_advise_02 = 2
        elif (mc_body.orgasm == 2) and (afternight04_mcbodyorgasm_advise_02 == 2):
            $ afternight04_mcbodyorgasm_advise_02 = 3

        pt "Estoy cerca del orgasmo..."

    #elif (mc_body.orgasm == 0 and mc_body.pleasure in range (41, 50)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (90, 100)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (136, 150)):
    elif (((mc_body.orgasm == 0 and mc_body.pleasure > 41) and (afternight04_mcbodyorgasm_advise_03 == 0)) or  
        ((mc_body.orgasm == 1 and mc_body.pleasure > 70) and (afternight04_mcbodyorgasm_advise_03 == 1)) or 
        ((mc_body.orgasm == 2 and mc_body.pleasure > 90) and (afternight04_mcbodyorgasm_advise_03 == 2))):

        if (mc_body.orgasm == 0) and (afternight04_mcbodyorgasm_advise_03 == 0):
            $ afternight04_mcbodyorgasm_advise_03 = 1
        elif (mc_body.orgasm == 1) and (afternight04_mcbodyorgasm_advise_03 == 1):
            $ afternight04_mcbodyorgasm_advise_03 = 2
        elif (mc_body.orgasm == 2) and (afternight04_mcbodyorgasm_advise_03 == 2):
            $ afternight04_mcbodyorgasm_advise_03 = 3

        pt "Tengo la polla a punto de explotar..."

    #if (mc_body.orgasm == 1 and mc_body.pleasure in range (90, 100)):
    if (((mc_body.orgasm == 1) and (mc_body.pleasure > 65)) and 
        (afternight04_mcbodyorgasm_remind_02 == False)):

        $ afternight04_mcbodyorgasm_remind_02 = True

        pt "Y ya sería mi segundo orgasmo..."

    #elif (mc_body.orgasm == 2 and mc_body.pleasure in range (136, 150)):
    elif ((mc_body.orgasm == 2 and mc_body.pleasure > 90) and 
        (afternight04_mcbodyorgasm_remind_03 == False)):

        $ afternight04_mcbodyorgasm_remind_03 = True

        pt "¡Y será mi último orgasmo!"

    call afternight04_sexbattle_dvaporbreathing_scene
    call afternight04_sexbattle_dblush_scene

    # Scenes Conditionals
    $ afternight04__prehfix_LBoob_Grab = False
    $ afternight04__prehfix_LBoob_Slap = False
    $ afternight04__prehfix_LButtock_Massage = False
    $ afternight04__prehfix_LButtock_Slap = False
    $ afternight04__prehfix_LLeg_Massage = False
    $ afternight04__prehfix_LNipple_Lick = False
    $ afternight04__prehfix_LNipple_Pinch = False
    $ afternight04__prehfix_MBelly_Massage = False
    $ afternight04__prehfix_MClitoris_Massage = False
    $ afternight04__prehfix_MClitoris_Tongue = False
    $ afternight04__prehfix_MMouth_dick = False
    $ afternight04__prehfix_MMouth_Fingers = False
    $ afternight04__prehfix_MMouth_Tongue = False
    $ afternight04__prehfix_MStomach_Massage = False
    $ afternight04__prehfix_Pussy_dick_deep = False
    $ afternight04__prehfix_Pussy_dick_low = False
    $ afternight04__prehfix_Pussy_dick_med = False
    $ afternight04__prehfix_Pussy_dick_out = False
    $ afternight04__prehfix_Anal_dick_deep = False
    $ afternight04__prehfix_Anal_dick_low = False
    $ afternight04__prehfix_Anal_dick_med = False
    $ afternight04__prehfix_Anal_dick_out = False
    $ afternight04__prehfix_Pussy_Fingers= False
    $ afternight04__prehfix_Anal_Fingers= False
    $ afternight04__prehfix_Pussy_Tongue = False
    $ afternight04__prehfix_Anal_Tongue = False
    $ afternight04__prehfix_RArm_Grab = False
    $ afternight04__prehfix_RBoob_Grab = False
    $ afternight04__prehfix_RBoob_Slap = False
    $ afternight04__prehfix_RButtock_Massage = False
    $ afternight04__prehfix_RButtock_Slap = False
    $ afternight04__prehfix_Remove = False
    $ afternight04__prehfix_RLeg_Massage = False
    $ afternight04__prehfix_RNipple_Lick = False
    $ afternight04__prehfix_RNipple_Pinch = False

    return

################################################################################################################################################
###############################################################################################################################################
##############################################################################################################################################
#############################################################################################################################################
############################################################################################################################################

label afternight04_sexbattle_dvaporbreathing_scene:

    #  girl orgasm - orgasm to come = MAX pleasure // 0-1 = 50 // 1-2 = 100 // 2-3 = 150 // 3-4 = 200 // 4-5etc = 250

    if current_pose.id == "pose_1":

        #if (current_girl.orgasm == 0 and current_girl.pleasure in range (30, 50)) or (current_girl.orgasm == 1 and current_girl.pleasure  in range (30, 49)) or (current_girl.orgasm == 2 and current_girl.pleasure  in range (60, 74)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (130, 149)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (170, 189)):

        if (current_girl.orgasm == 0 and current_girl.pleasure in range (30, 50)) or (current_girl.orgasm == 1 and current_girl.pleasure  in range (55, 64)) or (current_girl.orgasm == 2 and current_girl.pleasure  in range (70, 79)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (80, 89)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (100, 119)):

            show afternight04_sexbattle_dvaporbreathing 01_a
            with dissolve

        #if (current_girl.orgasm == 1 and current_girl.pleasure  in range (75, 100)) or (current_girl.orgasm == 2 and current_girl.pleasure  in range (75, 110)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (150, 159)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (190, 209)):
        if (current_girl.orgasm == 1 and current_girl.pleasure  in range (65, 75)) or (current_girl.orgasm == 2 and current_girl.pleasure  in range (80, 89)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (90, 104)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (120, 129)):

            show afternight04_sexbattle_dvaporbreathing 02_a
            with dissolve

        #if (current_girl.orgasm == 2 and current_girl.pleasure  in range (111, 135)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (160, 179)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (210, 229)):
        if (current_girl.orgasm == 2 and current_girl.pleasure  in range (90, 100)) or (current_girl.orgasm == 3 and current_girl.pleasure  in range (105, 114)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (130, 139)):

            show afternight04_sexbattle_dvaporbreathing 03_a
            with dissolve

        #if (current_girl.orgasm == 3 and current_girl.pleasure  in range (180, 200)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (230, 250)):
        if (current_girl.orgasm == 3 and current_girl.pleasure  in range (115, 125)) or (current_girl.orgasm >= 4 and current_girl.pleasure  in range (140, 150)):

            show afternight04_sexbattle_dvaporbreathing 04_a
            with dissolve

    return

label afternight04_sexbattle_dblush_scene:

    #  blush 0 = 0-29  // 1 > 30 // 2 > 75 // 3 > 120 // 4 > 160 // 5 > 200

    if (current_girl.enslavement in range (30, 74)):

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_blush 01_a

        elif current_pose.id == "pose_3":

            show afternight04_sexbattle_d_blush 01_c:
                afternight04_sexbattle_d_expressions_pos_c

    if (current_girl.enslavement in range (75, 119)):

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_blush 02_a

        elif current_pose.id == "pose_3":

            show afternight04_sexbattle_d_blush 02_c:
                afternight04_sexbattle_d_expressions_pos_c

    if (current_girl.enslavement in range (120, 159)):

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_blush 03_a

        elif current_pose.id == "pose_3":

            show afternight04_sexbattle_d_blush 03_c:
                afternight04_sexbattle_d_expressions_pos_c

    if (current_girl.enslavement in range (160, 199)):

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_blush 04_a

        elif current_pose.id == "pose_3":

            show afternight04_sexbattle_d_blush 04_c:
                afternight04_sexbattle_d_expressions_pos_c

    if (current_girl.enslavement >= 200):

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_blush 05_a

        elif current_pose.id == "pose_3":

            show afternight04_sexbattle_d_blush 05_c:
                afternight04_sexbattle_d_expressions_pos_c

    return







##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
##################################################################################################################################################################
#################################################################################################################################################################
################################################################################################################################################################
###################################################################### POINTS!!!

label afternight04_SexPointsGeneral:

    ### 

    ###########
    ###########
    ###################################################################### POINTS CLITORIS MASSAGE

    if mc_body.store["right_hand"] == "MClitoris_Massage":

        if afternight04__prehfix_MClitoris_Massage == True: #One or other are still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 7
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 6
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 5
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 5
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 4
                    $ current_girl.enslavement += 1
                else:
                    $ current_girl.pleasure += 3

        else:

            $ current_girl.pleasure += 3
            $ debug ("Massaging her Clitoris in action but NOT selected") #If it is working and you´re doing another action.
            

    ###########
    ###########

    ###########
    ###########
    ###################################################################### POINTS CLITORIS TONGUE

    if mc_body.store["tongue"] == "MClitoris_Tongue":

        if afternight04__prehfix_MClitoris_Tongue == True: #Still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 8
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 7
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 6
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 6
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 5
                    $ current_girl.enslavement += 1
                else:
                    $ current_girl.pleasure += 4

        else:

            $ current_girl.pleasure += 4
            $ debug ("Licking her Clitoris in action but NOT selected") #If it is working and you´re doing another action.
            

    ###########
    ###########

    ###################################################################### POINTS MBELLY MASSAGE # It´s not necessary.

    #if mc_body.store["left_hand"] == "MBelly_Massage":

        #if afternight04__prehfix_MBelly_Massage == True : #still active.

            #if mc_body.roll_success == True:

    ###########
    ###########

    ###################################################################### POINTS MSTOMACH MASSAGE

    if mc_body.store["left_hand"] == "MStomach_Massage":

        if afternight04__prehfix_MStomach_Massage == True : #still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 3
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 2
                else:
                    $ current_girl.pleasure += 1

        else:

            $ current_girl.pleasure += 1
            #pt "Parece que el masaje en el estómago tampoco le desagrada..." #If only one is working and you´re doing another action.
            

    ###########
    ###########

    ###################################################################### POINTS SLAP BOOBS

    if mc_body.store["right_hand"] == "LBoob_Slap" or mc_body.store["left_hand"] == "RBoob_Slap":

        if (afternight04__prehfix_LBoob_Slap == True or afternight04__prehfix_RBoob_Slap == True): #One or other are still active.

            # if mc_body.store["right_hand"] == "LBoob_Slap" and mc_body.store["left_hand"] == "RBoob_Slap": # You can´t do both of them same time.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 4
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 3
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "fifth":
                    $ current_girl.enslavement += 3
                else:
                    $ current_girl.enslavement += 2

        #else:

            # else is Not necessary for Slap

    ###########
    ###########

    ###################################################################### POINTS SLAP BUTTOCKS

    if (current_pose.id == "pose_2" or current_pose.id == "pose_3") and (mc_body.store["right_hand"] == "RButtock_Slap" or mc_body.store["left_hand"] == "LButtock_Slap"):

        if (afternight04__prehfix_LButtock_Slap == True or afternight04__prehfix_RButtock_Slap == True): #One or other are still active.

            ## You can´t do both of them same time.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 4
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 3
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "fifth":
                    $ current_girl.enslavement += 3
                else:
                    $ current_girl.enslavement += 2

        #else:

            # else is Not necessary for Slap

    ###########
    ###########
    ###################################################################### POINTS GRAB (massage) BOOBS

    if (current_pose.id == "pose_1" and (mc_body.store["right_hand"] == "LBoob_Grab" or mc_body.store["left_hand"] == "RBoob_Grab")) or ((current_pose.id == "pose_2" or current_pose.id == "pose_3") and (mc_body.store["left_hand"] == "LBoob_Grab" or mc_body.store["right_hand"] == "RBoob_Grab")):

        

        if (afternight04__prehfix_LBoob_Grab == True or afternight04__prehfix_RBoob_Grab == True): #One or other are still active.

            if mc_body.store["right_hand"] == "LBoob_Grab" and mc_body.store["left_hand"] == "RBoob_Grab": #Both and you´re doing one of them.

                #$ debug ("Both hands on her boobs in pose 01.")

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 6
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 5
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 1
                    else:
                        $ current_girl.pleasure += 2

            else:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 5
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 4
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 6
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 2
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 2
                    else:
                        $ current_girl.pleasure += 1

        else:

            if mc_body.store["right_hand"] == "LBoob_Grab" and mc_body.store["left_hand"] == "RBoob_Grab": #Both Pinching but you´re doing another action.

                $ current_girl.pleasure += 2
                #$ debug ("Left Grab Boob + Right Grab Boob in action but Not selected (Only on pose 01).")

                #pt "Sigue disfrutando del masaje en ambos pechos..."

                

            else:

                $ current_girl.pleasure += 1
                #$ debug ("Left Grab Boob OR Right Grab Boob in action but NOT selected") #If only one is working and you´re doing another action.

                #pt "Sigue disfrutando del masaje en su pecho..."
                

    ###########
    ###########
    ###################################################################### POINTS MASSAGE BUTTOCKS

    if (current_pose.id == "pose_1" and (mc_body.store["right_hand"] == "LButtock_Massage" or mc_body.store["left_hand"] == "RButtock_Massage")) or ((current_pose.id == "pose_2" or current_pose.id == "pose_3") and (mc_body.store["left_hand"] == "LButtock_Massage" or mc_body.store["right_hand"] == "RButtock_Massage")):

        #if current_pose.id == "pose_1":
            #$ debug ("Massaging Buttocks for pose 01.")
        #elif current_pose.id == "pose_2":
            #$ debug ("Massaging Buttocks for pose 02.")
        #elif current_pose.id == "pose_3":
            #$ debug ("Massaging Buttocks for pose 03.")

        if (afternight04__prehfix_LButtock_Massage == True or afternight04__prehfix_RButtock_Massage == True): #One or other are still active.

            if mc_body.store["right_hand"] == "LButtock_Massage" and mc_body.store["left_hand"] == "RButtock_Massage": #Both and you´re doing one of them.

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 6
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 5
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 1
                    else:
                        $ current_girl.pleasure += 2

                else: # You failed

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
                        if mc_body.dick_speed >= 2:
                            $ afternight04__RButtock_Massage_Failed -= 1

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
                        if mc_body.dick_speed == 1:
                            $ current_girl.enslavement += 2

                        elif mc_body.dick_speed >= 2:
                            $ current_girl.enslavement += 3

            else:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 5
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 4
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 6
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 2
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 2
                    else:
                        $ current_girl.pleasure += 1

                else: # You failed

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
                        if mc_body.dick_speed >= 2:
                            $ afternight04__RButtock_Massage_Failed -= 1

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
                        if mc_body.dick_speed == 1:
                            $ current_girl.enslavement += 1

                        elif mc_body.dick_speed >= 2:
                            $ current_girl.enslavement += 2

        else:

            if mc_body.store["right_hand"] == "LButtock_Massage" and mc_body.store["left_hand"] == "RButtock_Massage": #Both Pinching but you´re doing another action.

                $ current_girl.pleasure += 2
                #pt "Que le acaricie al mismo tiempo ambas nalgas, tampoco le disgusta..."

            else:

                $ current_girl.pleasure += 1
                #pt "Que le esté acariciando una nalga, tampoco le desagrada..."
                
                #$ debug ("Left Grab Boob OR Right Grab Boob in action but NOT selected") #If only one is working and you´re doing another action.
                


    ###########
    ###########
    ###################################################################### POINTS MASSAGE LEGS (only in pose 01)

    if current_pose.id == "pose_1" and (mc_body.store["right_hand"] == "LLeg_Massage" or mc_body.store["left_hand"] == "RLeg_Massage"):

        #if current_pose.id == "pose_1":
            #$ debug ("Massaging Legs for pose 01.")

        #else:
            #$ debug ("This message should not be readable 9845")

        if (afternight04__prehfix_LLeg_Massage == True or afternight04__prehfix_RLeg_Massage == True): #One or other are still active.

            if mc_body.store["right_hand"] == "LLeg_Massage" and mc_body.store["left_hand"] == "RLeg_Massage": #Both and you´re doing one of them.

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 3
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 2
                    else:
                        $ current_girl.pleasure += 2

            else:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 3
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 3
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 2
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 2
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 1
                    else:
                        $ current_girl.pleasure += 1

        else:

            if mc_body.store["right_hand"] == "LLeg_Massage" and mc_body.store["left_hand"] == "RLeg_Massage": #Both Pinching but you´re doing another action.

                $ current_girl.pleasure += 2
                $ debug ("LLeg_Massage + RLeg_Massage in action but Not selected.")

                

            else:

                $ current_girl.pleasure += 1
                $ debug ("LLeg_Massage OR RLeg_Massage in action but NOT selected") #If only one is working and you´re doing another action.
                

    ###########
    ###########
    ###################################################################### POINTS PINCHING NIPPLES

    if mc_body.store["right_hand"] == "LNipple_Pinch" or mc_body.store["left_hand"] == "RNipple_Pinch":

        if (afternight04__prehfix_LNipple_Pinch == True or afternight04__prehfix_RNipple_Pinch == True): #One or other are still active.

            if mc_body.store["right_hand"] == "LNipple_Pinch" and mc_body.store["left_hand"] == "RNipple_Pinch": #Both Pinching and you´re doing one of them.

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 7
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 2
                        $ current_girl.enslavement += 3
                    else:
                        $ current_girl.pleasure += 1
                        $ current_girl.enslavement += 2

            else:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 2
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 1
                        $ current_girl.enslavement += 2
                    else:
                        $ current_girl.enslavement += 1

        else:

            if mc_body.store["right_hand"] == "LNipple_Pinch" and mc_body.store["left_hand"] == "RNipple_Pinch": #Both Pinching but you´re doing another action.


                $ current_girl.enslavement += 2
                $ debug ("Left Pinch Nipple + Right Pinch Nipple Not selected.")

                

            else:

                $ current_girl.enslavement += 1
                $ debug ("Left Pinch Nipple OR Right Pinch Nipple NOT selected") #If only one is working and you´re doing another action.
                

    ###########
    ###########
    ###################################################################### POINTS LICKING NIPPLES

    if mc_body.store["tongue"] == "LNipple_Lick" or mc_body.store["tongue"] == "RNipple_Lick":

        if (afternight04__prehfix_LNipple_Lick == True or afternight04__prehfix_RNipple_Lick == True): #One or other are still active.

            if mc_body.store["tongue"] == "LNipple_Lick" and mc_body.store["tongue"] == "RNipple_Lick": #Both and you´re doing one of them.

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 7
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 6
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 5
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 2
                    else:
                        $ current_girl.pleasure += 2
                        $ current_girl.enslavement += 1

            else:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.pleasure += 6
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 5
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "thrice":
                        $ current_girl.pleasure += 4
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fourth":
                        $ current_girl.pleasure += 3
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "fifth":
                        $ current_girl.pleasure += 2
                        $ current_girl.enslavement += 1
                    else:
                        $ current_girl.pleasure += 1

        else:

            if mc_body.store["tongue"] == "LNipple_Lick" and mc_body.store["tongue"] == "RNipple_Lick": #Both Pinching but you´re doing another action.

                $ current_girl.pleasure += 2
                $ debug ("Left Pinch Nipple + Right Pinch Nipple Not selected.")

                

            else:

                $ current_girl.pleasure += 1
                $ debug ("Left Pinch Nipple OR Right Pinch Nipple NOT selected") #If only one is working and you´re doing another action.
                


    ###########
    ###########
    ###################################################################### POINTS MMOUTH_DICK

    if mc_body.store["dick"] == "MMouth_dick":

        if afternight04__prehfix_MMouth_dick == True: #One or other are still active.

            if mc_body.roll_success == True:

                $ debug ("You had success on Putting your dick in Didac´s mouth.")

                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 6
                    $ current_girl.enslavement += 8
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 6
                    $ current_girl.enslavement += 7
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 6
                    $ current_girl.enslavement += 6
                elif current_girl.repeat == "fourth":
                    $ mc_body.pleasure += 5
                    $ current_girl.enslavement += 5
                elif current_girl.repeat == "fifth":
                    $ mc_body.pleasure += 5
                    $ current_girl.enslavement += 4
                else:
                    $ mc_body.pleasure += 5
                    $ current_girl.enslavement += 4

        else:

            $ mc_body.pleasure += 5
            $ current_girl.enslavement += 4
            $ debug ("MMouth_dick NOT selected") #If only one is working and you´re doing another action.


    ###########
    ###########
    ###################################################################### POINTS MMOUTH_Fingers

    if mc_body.store["right_hand"] == "MMouth_Fingers":

        if afternight04__prehfix_MMouth_Fingers == True: #One or other are still active.

            if mc_body.roll_success == True:

                $ debug ("You had success on Putting your finger in Didac mouth.")

                if current_girl.repeat == "once":
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.enslavement += 2
                else:
                    $ current_girl.enslavement += 1

        else:

            $ current_girl.enslavement += 1
            $ debug ("MMouth_Fingers NOT selected") #If only one is working and you´re doing another action.
            

    ###########
    ###########
    ###################################################################### POINTS MMOUTH_TONGUE

    if mc_body.store["tongue"] == "MMouth_Tongue":

        if afternight04__prehfix_MMouth_Tongue == True: #One or other are still active.

            if mc_body.roll_success == True:

                $ debug ("You had success on Kissing Didac.")

                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 1
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 10
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 1
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 8
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 6
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 4
                else:
                    $ current_girl.enslavement += 2

        else:

            $ current_girl.enslavement += 2
            $ debug ("MMouth_Tongue NOT selected") #If only one is working and you´re doing another action.
            

    ###########
    ###########
    ###################################################################### POINTS PUSSY_FINGERS

    if mc_body.store["right_hand"] == "Pussy_Fingers":

        if afternight04__prehfix_Pussy_Fingers== True: #One or other are still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 7
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 6
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 5
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 4
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 4
                else:
                    $ current_girl.pleasure += 3

        else:

            $ current_girl.pleasure += 3
            $ debug ("Pussy_Fingers NOT selected") #If only one is working and you´re doing another action.
            
    ###########
    ###########
    ###################################################################### POINTS ANAL_FINGERS

    if mc_body.store["right_hand"] == "Anal_Fingers":

        if afternight04__prehfix_Anal_Fingers == True: #One or other are still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 3
                    $ current_girl.enslavement += 7
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 6
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 5
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement+= 4
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 3
                else:
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 1

        else:

            $ current_girl.enslavement += 1
            $ debug ("Anal_Fingers NOT selected") #If only one is working and you´re doing another action.

    ###########
    ###########
    ###################################################################### POINTS PUSSY_TONGUE

    if mc_body.store["tongue"] == "Pussy_Tongue":

        if afternight04__prehfix_Pussy_Tongue == True: #One or other are still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 8
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 7
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 6
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 5
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 4
                else:
                    $ current_girl.pleasure += 3

        else:
            
            $ current_girl.pleasure += 3
            $ debug ("Pussy_Tongue NOT selected") #If only one is working and you´re doing another action.
            

    ###########
    ###########
    ###################################################################### POINTS ANAL_TONGUE

    if mc_body.store["tongue"] == "Anal_Tongue":

        if afternight04__prehfix_Pussy_Tongue == True: #One or other are still active.

            if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 3
                    $ current_girl.enslavement += 8
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 2
                    $ current_girl.enslavement += 7
                elif current_girl.repeat == "thrice":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 6
                elif current_girl.repeat == "fourth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 5
                elif current_girl.repeat == "fifth":
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 4
                else:
                    $ current_girl.pleasure += 1
                    $ current_girl.enslavement += 3

        else:
            
            $ current_girl.pleasure += 1
            $ current_girl.enslavement += 2
            $ debug ("Anal_Tongue NOT selected") #If only one is working and you´re doing another action.


        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
    ###################################################################### POINTS PUSSY DICK

    if afternight04_SheRapingYou == False:

###

        if afternight04__prehfix_Pussy_dick_deep == True: ### DEEP

            #if mc_body.dick_speed == 3: # FAST DEEP
            if afternight04_dick_general_Speed_3_Cond == True:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 35 #8
                        $ current_girl.pleasure += 50 #10
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 33 #8
                        $ current_girl.pleasure += 44 #10
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 30 #8
                        $ current_girl.pleasure += 40 #10
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 40 #10
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 36 #9
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 32 #8
                    else:
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 28 #7

            elif mc_body.dick_speed == 2: # MOD DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 32 #8
                        $ current_girl.pleasure += 45 #10
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 30 #8
                        $ current_girl.pleasure += 40 #9
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 36 #9
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 32 #8
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 28 #7
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 24 #6
                    else:
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 20 #5

            elif mc_body.dick_speed == 1: # SLOW DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 17 #4
                        $ current_girl.pleasure += 36 #9
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 32 #8
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 15 #4
                        $ current_girl.pleasure += 28 #7
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 14 #4
                        $ current_girl.pleasure += 24 #6
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 20 #5
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 16 #4
                    else:
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 12 #3

            elif mc_body.dick_speed == 0: # STOP DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 20 #5
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 16 #3
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 4 #1
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 1
                        $ current_girl.pleasure += 4 #1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Pussy_dick_deep": #if dick is med and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST DEEP # This shouldn´t be visible

                $ debug ("This text should not be visible 98825")

                $ mc_body.pleasure += 16 #4
                $ current_girl.pleasure += 21 #7

            elif mc_body.dick_speed == 2: # MOD DEEP

                $ mc_body.pleasure += 12 #3
                $ current_girl.pleasure += 20 #5

            elif mc_body.dick_speed == 1: # SLOW DEEP

                $ mc_body.pleasure += 4 #1
                $ current_girl.pleasure += 12 #3 #Every time your dick is outside, you earn a point of eslavement.

            #elif mc_body.dick_speed == 0: # STOP DEEP #NOTHING to Point.

###

        elif afternight04__prehfix_Pussy_dick_med == True: ### MEDium

            #if mc_body.dick_speed == 3: # FAST MED
            if afternight04_dick_general_Speed_3_Cond == True:

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 27 #6
                    $ current_girl.pleasure += 40 #9
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 26 #6
                    $ current_girl.pleasure += 38 #9
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 25 #6
                    $ current_girl.pleasure += 36 #9
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fourth":
                    $ mc_body.pleasure += 24 #6
                    $ current_girl.pleasure += 32 #8
                elif current_girl.repeat == "fifth":
                    $ mc_body.pleasure += 20 #5
                    $ current_girl.pleasure += 28 #7
                elif current_girl.repeat == "sixth":
                    $ mc_body.pleasure += 16 #4
                    $ current_girl.pleasure += 24 #6
                else:
                    $ mc_body.pleasure += 12 #3
                    $ current_girl.pleasure += 20 #5

            elif mc_body.dick_speed == 2: # MOD MED

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 24 #6
                    $ current_girl.pleasure += 32 #8
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 20 #5
                    $ current_girl.pleasure += 28 #7
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 16 #4
                    $ current_girl.pleasure += 24 #6
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "fourth":
                    $ mc_body.pleasure += 12 #3
                    $ current_girl.pleasure += 20 #5
                else:
                    $ mc_body.pleasure += 8 #2
                    $ current_girl.pleasure += 16 #4

            elif mc_body.dick_speed == 1: # SLOW MED

                #$ debug ("WHY NOT?")

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    #$ debug ("WHY NOT?01")
                    $ mc_body.pleasure += 12 #3
                    $ current_girl.pleasure += 20 #5
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "twice":
                    #$ debug ("WHY NOT?02")
                    $ mc_body.pleasure += 8 #1
                    $ current_girl.pleasure += 16 #4
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 12 #3
                else:
                    $ mc_body.pleasure += 3 #1
                    $ current_girl.pleasure += 8 #2

            elif mc_body.dick_speed == 0: # STOP MED

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure +=  6 #1
                elif current_girl.repeat == "twice":
                    $ current_girl.pleasure += 3 #1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Pussy_dick_med": #if dick is med and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST MED

                $ debug ("This text should not be visible 98853")

                $ mc_body.pleasure += 12 #3
                $ current_girl.pleasure += 20 #5

            elif mc_body.dick_speed == 2: # MOD MED

                $ mc_body.pleasure += 8 #2 #x10
                $ current_girl.pleasure += 16 #4

            elif mc_body.dick_speed == 1: # SLOW MED

                $ mc_body.pleasure += 4 #1
                $ current_girl.pleasure += 8 #2 #Every time your dick is outside, you earn a point of eslavement.

            #elif mc_body.dick_speed == 0: # STOP MED #NOTHING to Point.

###

        elif afternight04__prehfix_Pussy_dick_low == True: ### LOW

            #if mc_body.dick_speed == 3: # FAST LOW
            if afternight04_dick_general_Speed_3_Cond == True:

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 16 #4
                    $ current_girl.pleasure += 24 #6
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure +=  12 #3
                    $ current_girl.pleasure += 20 #5
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure +=  8 #2
                    $ current_girl.pleasure += 16 #4
                else:
                    $ mc_body.pleasure +=  6 #2 # TIP: Same Result than her.
                    $ current_girl.pleasure += 12 #3

            elif mc_body.dick_speed == 2: # MOD LOW

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 16 #4
                    $ current_girl.pleasure += 20 #5
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 12 #3
                    $ current_girl.pleasure += 16 #4
                    $ current_girl.enslavement += 1
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 8 #2
                    $ current_girl.pleasure += 12 #3
                else:
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 8 #2

            elif mc_body.dick_speed == 1: # SLOW LOW

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ mc_body.pleasure += 8 #2
                    $ current_girl.pleasure += 12 #3
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "twice":
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 8 #2
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "thrice":
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 7 #1
                    $ current_girl.enslavement += 2
                elif current_girl.repeat == "fourth":
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 6 #1
                    $ current_girl.enslavement += 1
                else:
                    $ mc_body.pleasure += 4 #1
                    $ current_girl.pleasure += 5 #1

            elif mc_body.dick_speed == 0: # STOP LOW

                #if mc_body.roll_success == True:
                if current_girl.repeat == "once":
                    $ current_girl.pleasure += 1
                elif current_girl.repeat == "twice":
                    $ current_girl.enslavement += 1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Pussy_dick_low": #if dick is low and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST LOW

                $ debug ("This text should not be visible 6879")

                $ mc_body.pleasure += 8 #2 # TIP: Same Result than her.
                $ current_girl.pleasure += 1 #3

            elif mc_body.dick_speed == 2: # MOD LOW

                $ mc_body.pleasure += 4 #1
                $ current_girl.pleasure += 8 #2

            elif mc_body.dick_speed == 1: # SLOW LOW

                $ mc_body.pleasure += 4 #1
                $ current_girl.pleasure += 6 #1 #Every time your dick is outside, you earn a point of eslavement.

            #elif mc_body.dick_speed == 0: # STOP LOW #NOTHING to Point.

###

        elif afternight04__prehfix_Pussy_dick_out == True: # DICK OUT

            if mc_body.roll_success == True: #You don´t want to fuck her and she accepts it reluctantly.
                
                if current_girl.repeat == "once":
                    $ current_girl.enslavement += 6
                elif current_girl.repeat == "twice":
                    $ current_girl.enslavement += 5
                elif current_girl.repeat == "thrice":
                    $ current_girl.enslavement += 4
                elif current_girl.repeat == "fourth":
                    $ current_girl.enslavement += 3
                elif current_girl.repeat == "fifth":
                    $ current_girl.enslavement += 2
                else:
                    $ current_girl.enslavement += 1

        ###___ Points where you´re doing another action.
        elif mc_body.store["dick"] == "Pussy_dick_out": #if dick is out and it´s not Raping and it´s not actual action, that´s your earn.

            $ current_girl.enslavement += 1 #Every time your dick is outside, you earn a point of eslavement.

    ## < CHECK_BEFORE
##################
##################


        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
        ###########
    ###########
    ###################################################################### POINTS ANAL DICK

    if afternight04_SheRapingYou == False:

###

        if afternight04__prehfix_Anal_dick_deep == True: ### DEEP

            #if mc_body.dick_speed == 3: # FAST DEEP
            if afternight04_dick_general_Speed_3_Cond == True:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 48 #12
                        $ current_girl.pleasure += 20 #5
                        $ current_girl.enslavement += 14
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 44 #11
                        $ current_girl.pleasure += 24 #6
                        $ current_girl.enslavement += 13
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 40 #10
                        $ current_girl.pleasure += 28 #7
                        $ current_girl.enslavement += 12
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 36 #9
                        $ current_girl.pleasure += 32 #8
                        $ current_girl.enslavement += 11
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 32 #8
                        $ current_girl.pleasure += 32 #9
                        $ current_girl.enslavement += 10
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 34 #10
                        $ current_girl.enslavement += 9
                    else:
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 36 #10
                        $ current_girl.enslavement += 8

            elif mc_body.dick_speed == 2: # MOD DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 40 #10
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 10
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 36 #9
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 9
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 32 #8
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 8
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 7
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 16 #4
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 20 #5
                        $ current_girl.enslavement += 5
                    else:
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 24 #6
                        $ current_girl.enslavement += 4

            elif mc_body.dick_speed == 1: # SLOW DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 20 #5
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 16 #4
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 2
                    else:
                        $ mc_body.pleasure += 3 #1
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 1

            elif mc_body.dick_speed == 0: # STOP DEEP

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 2
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 4 #1
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 4 #1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Anal_dick_deep": #if dick is med and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST DEEP

                $ debug ("This text should not be visible.")

                $ mc_body.pleasure += 20 #5
                $ current_girl.pleasure += 16 #4
                $ current_girl.enslavement += 3

            elif mc_body.dick_speed == 2: # MOD DEEP

                $ mc_body.pleasure += 16 #4
                $ current_girl.pleasure += 12 #3
                $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 1: # SLOW DEEP

                $ mc_body.pleasure += 8 #2
                $ current_girl.pleasure += 4 #1 #Every time your dick is outside, you earn a point of eslavement.
                $ current_girl.enslavement += 1

            #elif mc_body.dick_speed == 0: # STOP DEEP #NOTHING to Point.

###

        elif afternight04__prehfix_Anal_dick_med == True: ### MEDium

            #if mc_body.dick_speed == 3: # FAST MED
            if afternight04_dick_general_Speed_3_Cond == True:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 40 #10
                        $ current_girl.pleasure += 20 #5
                        $ current_girl.enslavement += 8
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 36 #9
                        $ current_girl.pleasure += 18 #4
                        $ current_girl.enslavement += 7
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 32 #8
                        $ current_girl.pleasure += 16 #3
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 14 #3
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "fifth":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "sixth":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 3
                    else:
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 12 #2
                        $ current_girl.enslavement += 3

            elif mc_body.dick_speed == 2: # MOD MED

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 32 #8
                        $ current_girl.pleasure += 16 #4
                        $ current_girl.enslavement += 7
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 28 #7
                        $ current_girl.pleasure += 14 #3
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 12 #2
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 10 #1
                        $ current_girl.enslavement += 4
                    else:
                        $ mc_body.pleasure += 16 #3
                        $ current_girl.pleasure += 8 #1
                        $ current_girl.enslavement += 3

            elif mc_body.dick_speed == 1: # SLOW MED

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 3
                    else:
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 0: # STOP MED

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 6 #1
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 1

                    elif current_girl.repeat == "twice":
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 3 #1
                    else:

                        if afternight04__Anal_dick_med_Success >= 1:
                            $ current_girl.enslavement += 1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Anal_dick_med": #if dick is med and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST MED

                $ debug ("Thist text should not be visible.")

                $ mc_body.pleasure += 12 #3
                $ current_girl.pleasure += 8 #2
                $ current_girl.enslavement += 4
                

            elif mc_body.dick_speed == 2: # MOD MED

                $ mc_body.pleasure += 8 #2 #x10
                $ current_girl.pleasure += 4 #1
                $ current_girl.enslavement += 2
                

            elif mc_body.dick_speed == 1: # SLOW MED

                $ mc_body.pleasure += 4 #1
                $ current_girl.pleasure += 3 #1 #Every time your dick is outside, you earn a point of eslavement.
                $ current_girl.enslavement += 1
                

            #elif mc_body.dick_speed == 0: # STOP MED #NOTHING to Point.

###

        elif afternight04__prehfix_Anal_dick_low == True: ### LOW

            #if mc_body.dick_speed == 3: # FAST LOW
            if afternight04_dick_general_Speed_3_Cond == True:

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 24 #6
                        $ current_girl.pleasure += 12 #3
                        $ current_girl.enslavement += 7
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 20 #5
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 3
                    else:
                        $ mc_body.pleasure += 12 #3 # TIP: Same Result than her.
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 2: # MOD LOW

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 16 #4
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 6
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 12 #3
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.enslavement += 4
                    else:
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 1: # SLOW LOW

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ mc_body.pleasure += 8 #2
                        $ current_girl.pleasure += 8 #2
                        $ current_girl.enslavement += 5
                    elif current_girl.repeat == "twice":
                        $ mc_body.pleasure += 7 #1
                        $ current_girl.pleasure += 6 #1
                        $ current_girl.enslavement += 4
                    elif current_girl.repeat == "thrice":
                        $ mc_body.pleasure += 6 #1
                        $ current_girl.pleasure += 4 #1
                        $ current_girl.enslavement += 3
                    elif current_girl.repeat == "fourth":
                        $ mc_body.pleasure += 4 #1
                        $ current_girl.pleasure += 2 #1
                        $ current_girl.enslavement += 2
                    else:
                        $ mc_body.pleasure += 2 #1
                        $ current_girl.enslavement += 1

            elif mc_body.dick_speed == 0: # STOP LOW

                if mc_body.roll_success == True:
                    if current_girl.repeat == "once":
                        $ current_girl.enslavement += 1
                    elif current_girl.repeat == "twice":
                        $ current_girl.enslavement += 1

        ###___  Points where you´re doing another action.
        elif mc_body.store["dick"] == "Anal_dick_low": #if dick is low and it´s not Raping and it´s not actual action, that´s your earn.

            if mc_body.dick_speed == 3: # FAST LOW

                $ debug ("This text should not be visible 6876")

                $ mc_body.pleasure += 8 #2 # TIP: Same Result than her.
                $ current_girl.pleasure += 4 #1
                $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 2: # MOD LOW

                $ mc_body.pleasure += 4 #1
                $ current_girl.enslavement += 2

            elif mc_body.dick_speed == 1: # SLOW LOW

                $ current_girl.enslavement += 1 #Every time your dick is outside, you earn a point of eslavement.

            #elif mc_body.dick_speed == 0: # STOP LOW #NOTHING to Point.

###

        elif afternight04__prehfix_Anal_dick_out == True: # DICK OUT

            if mc_body.roll_success == True: #You don´t want to fuck her and she accepts it reluctantly.

                if afternight04__Anal_dick_med_Success >= 1:
                
                    $ current_girl.enslavement += 1

        ###___ Points where you´re doing another action.
        elif mc_body.store["dick"] == "Anal_dick_out": #if dick is out and it´s not Raping and it´s not actual action, that´s your earn.

            if afternight04__Anal_dick_med_Success >= 1:

                $ current_girl.enslavement += 1 #Every time your dick is outside, you earn a point of eslavement.


##################
##################

    $ afternight04_dick_general_Speed_3_Cond = False


##################
##################

    return


    ##
##################
##################