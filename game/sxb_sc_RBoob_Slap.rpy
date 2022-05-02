label RBoob_Slap:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.01") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "RBoob_Slap."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RBoob_Slap"

    else:

        $ mc_body.store["right_hand"] = "RBoob_Slap"

#########################################################

    $ afternight04__prehfix_RBoob_Slap = True
    $ afternight04__a_prehfix_RBoob_Slap = True

    call afternight04_sex_check_before

    label .manager:

        $ afternight04__RBoob_Slap_Done += 1

        if mc_body.roll_success:
            $ afternight04__RBoob_Slap_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__RBoob_Slap_Failed += 1

        ##

        if mc_body.check_if_orgasm():
            $ __suffix.append("his_orgasm_" + str(mc_body.orgasm))

        elif current_girl.check_if_orgasm():
            if current_girl.orgasm >= 4:
                $ __suffix.append("her_orgasm_4_plus")
            else:
                $ __suffix.append("her_orgasm_" + str(current_girl.orgasm))

        else:
            if mc_body.roll_success:
                $ __suffix.append("his_roll")

            if "pass" in mc_body.result:
                $ __suffix.append( "pass" )
            else:
                $ __suffix.append( "fail" )

            if current_girl.roll_success:
                $ __suffix.append("her_roll")
        
            if current_girl.repeat:
                $ __suffix.append( current_girl.repeat )
                
        jump expression __prefix + "_".join(__suffix)

    label .call_screen:
        call afternight04_sex_check_after
        call screen dummy_screen()

    label .his_orgasm_1:
        $ debug ("First Orgasm for his. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Slapping her Right Boob.")

        call afternight04_RBoob_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RBoob_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Slapping her Right Boob.")

        call afternight04_RBoob_Slap
        
        jump expression __prefix + "call_screen"

#########################################################################################################################
########################################################################################################################
#######################################################################################################################

    label afternight04_RBoob_Slap:

        call afternight04_Boob_Slap

        return
        
    #############
    ############
    ## ORGASMS

    label afternight04_RBoob_Slap_his_orgasm:

        call afternight04_Boob_Slap

        call afternight04_mostly_his_orgasm

        return

    label afternight04_RBoob_Slap_her_orgasm:

        call afternight04_RBoob_Slap

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################


############################################################
########################################################### ## IMAGE

label afternight04_LBoob_Slap_image:

    if current_pose.id == "pose_1":


        if afternight04__prehfix_RBoob_Slap == True:
            show afternight04_sexbattle_mc_handL empty

            #if current_girl.total_try == 1:
            if (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 1:
                show afternight04_sexbattle_d_boobR wet_00_smash_01_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 2:
                show afternight04_sexbattle_d_boobR wet_00_smash_02_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 3:
                show afternight04_sexbattle_d_boobR wet_00_smash_03_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 4:
                show afternight04_sexbattle_d_boobR wet_00_smash_04_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 5:
                show afternight04_sexbattle_d_boobR wet_00_smash_05_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 6:
                show afternight04_sexbattle_d_boobR wet_00_smash_06_a_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) >= 7:
                show afternight04_sexbattle_d_boobR wet_00_smash_07_a_smashed
            

        elif afternight04__prehfix_LBoob_Slap == True:
            show afternight04_sexbattle_mc_handR empty

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            #if current_girl.total_try == 1:
            if (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 1:
                show afternight04_sexbattle_d_boobL wet_00_smash_01_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 2:
                show afternight04_sexbattle_d_boobL wet_00_smash_02_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 3:
                show afternight04_sexbattle_d_boobL wet_00_smash_03_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 4:
                show afternight04_sexbattle_d_boobL wet_00_smash_04_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 5:
                show afternight04_sexbattle_d_boobL wet_00_smash_05_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) == 6:
                show afternight04_sexbattle_d_boobL wet_00_smash_06_a_smashed
            elif (afternight04__LBoob_Slap_Success + afternight04__LBoob_Slap_Failed) >= 7:
                show afternight04_sexbattle_d_boobL wet_00_smash_07_a_smashed
            
        with vpunch

    elif current_pose.id == "pose_3":

        $ debug ("GO TO HELL")

        show afternight04_sexbattle_mc_handL empty

        show afternight04_sexbattle_mc_handR empty

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        #show afternight04_sexbattle_d_boobR wet_00_smash_01_c_smashed ## It´s below.

        if afternight04__prehfix_RBoob_Slap == True: # In theory you can´t slap LBoob, but what the hel...

            #if current_girl.total_try == 1:
            if (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 1:
                show afternight04_sexbattle_d_boobR wet_00_smash_01_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 2:
                show afternight04_sexbattle_d_boobR wet_00_smash_02_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 3:
                show afternight04_sexbattle_d_boobR wet_00_smash_03_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 4:
                show afternight04_sexbattle_d_boobR wet_00_smash_04_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 5:
                show afternight04_sexbattle_d_boobR wet_00_smash_05_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) == 6:
                show afternight04_sexbattle_d_boobR wet_00_smash_06_c_smashed
            elif (afternight04__RBoob_Slap_Success + afternight04__RBoob_Slap_Failed) >= 7:
                show afternight04_sexbattle_d_boobR wet_00_smash_07_c_smashed

        with vpunch

        $ debug ("WHAT FUCK BITCH")

    return

##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_LArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        #$ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        #$ afternight04__a_prehfix_RBoob_Slap = False
        $ afternight04__a_prehfix_RButtock_Massage = False
        $ afternight04__a_prehfix_RButtock_Slap = False
        
        $ afternight04__a_prehfix_RLeg_Massage = False
        $ afternight04__a_prehfix_RNipple_Pinch = False


    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    $ afternight04__a_prehfix_MClitoris_Massage = False

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

############################################################
###########################################################

label afternight04_Boob_Slap: 

    #################################################################################################################
    #################################################################################################################

    # You can´t at same time.

    #################################################################################################################
    #################################################################################################################

    call afternight04_LBoob_Slap_image

    #HER REACTION:
############################################################
###########################################################

    if mc_body.roll_success == True:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows sadx03_a

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡UHMMmm!"

        elif randomnum_1to5 == 2:

            d "¡HMMmm!"

        elif randomnum_1to5 == 3:

            d "¡AUHMMmm!"

        elif randomnum_1to5 == 4:

            d "¡OUHMMmm!"

        elif randomnum_1to5 == 5:

            d "¡UOUHMMmm!"


    else: # You failed.

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a

            d "¡AU!"

        elif randomnum_1to5 == 2:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a

            d "¡AI!"

        elif randomnum_1to5 == 3:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a

            d "¡OU!"

        elif randomnum_1to5 == 4:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a

            d "¡AUCH!"

        elif randomnum_1to5 == 5:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a

            d "¡OUCH!"

############################################################
    if current_pose.id == "pose_1":

        if afternight04__prehfix_RBoob_Slap == True:

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty

        if afternight04__prehfix_LBoob_Slap == True:

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

            with dissolve

    else:

        if afternight04__prehfix_LBoob_Slap == True:

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty

        if afternight04__prehfix_RBoob_Slap == True:

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

            with dissolve

############################################################
###########################################################

    if mc_body.roll_success == False:

        $ mc_body.store["left_hand"] = ""
        show afternight04_sexbattle_mc_handL empty

        $ mc_body.store["right_hand"] = ""
        show afternight04_sexbattle_mc_handR empty

        with hpunch

############################################################
###########################################################

############################################################
###########################################################

    $ debug("Some TEST text")

    # progcheck "RBoob_Slap_Success = [afternight04__RBoob_Slap_Success], 
            # \nRBoob_Slap_Failed = [afternight04__RBoob_Slap_Failed], 
            # \nLBoob_Slap_Success = [afternight04__LBoob_Slap_Success], 
            # \nLBoob_Slap_Failed = [afternight04__LBoob_Slap_Failed]."


    #HER REACTION:


    if mc_body.roll_success == True: #You succeded.

        if afternight04__prehfix_RBoob_Slap == True:

            if afternight04__RBoob_Slap_Success == 1:

                if afternight04__LBoob_Slap_Done == 0:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils front05_c
                        show afternight04_sexbattle_d_eyebrows angryx04_c
                        with dissolve

                    d "¡¿Qué coño haces?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_c
                        show afternight04_sexbattle_d_eyes 03_c
                        show afternight04_sexbattle_d_pupils front03_c
                        show afternight04_sexbattle_d_eyebrows surprisex02_c
                        with dissolve

                    p "Azotarte."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_c
                        show afternight04_sexbattle_d_eyes 04_c
                        show afternight04_sexbattle_d_pupils front04_c
                        show afternight04_sexbattle_d_eyebrows serious_c
                        with dissolve

                    p "¿No es evidente?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_c
                        show afternight04_sexbattle_d_eyes 04_c
                        show afternight04_sexbattle_d_pupils right04_c
                        show afternight04_sexbattle_d_eyebrows angryx03_c
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils front05_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                    with dissolve

                    d "¡¿Y quien te ha dado permiso para que me azotes la teta?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_c
                        show afternight04_sexbattle_d_eyes 02_c
                        show afternight04_sexbattle_d_pupils front02_c
                        show afternight04_sexbattle_d_eyebrows angryx03_c
                    with dissolve

                    d "¡imbécil!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_c
                        show afternight04_sexbattle_d_eyes 01_c
                        show afternight04_sexbattle_d_pupils front01_c
                        show afternight04_sexbattle_d_eyebrows surprisex01_c
                    with dissolve

                    p "¿Quieres que pare?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    if current_pose.id == "pose_3":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_c
                        show afternight04_sexbattle_d_eyes 04_c
                        show afternight04_sexbattle_d_pupils right04_c
                        show afternight04_sexbattle_d_eyebrows angryx01_c
                    with dissolve

                else: # Not the first time

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    if current_pose.id == "pose_3": # NOT FINISHED, falta ponerlo todo con POSE 3

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_c
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                    with dissolve

                    d "¡¿Ahora el derecho?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    d "¡¿Buscas estar a la par?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "¡Porque yo también te puedo abofetear la cara!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "¡¿Sabes?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows serious_a

                    with dissolve

                    p "¿Eso también te pondría tan cachondo como para volver a gemir cuando te he azotado?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows serious_a

                    with dissolve

                    d "No,"

                    extend " Yo no..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a

                    with dissolve

                    p "Tú no,"

                    extend " ¿Qué?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "Idiota."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

            elif afternight04__RBoob_Slap_Success == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "¡¿Otra vez?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "¡¿Estás sordo o qué?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

            elif afternight04__RBoob_Slap_Success == 3:


                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "No me azotes más la puta teta..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

            elif afternight04__RBoob_Slap_Success == 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "¡¿Qué es lo que no entiendes?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

            elif afternight04__RBoob_Slap_Success == 5:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "En serio..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "Para ya..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a     

                with dissolve

                pt "En realidad no parece que le disguste tanto..."

            elif afternight04__RBoob_Slap_Success == 6:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a   

                with dissolve

                p "Puedes quejarte lo que quieras,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a   

                with dissolve

                p "Pero te estás excitando más que yo con esto..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a   

                with dissolve

                d "Deja de tomar drogas..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a    

                with dissolve

            elif afternight04__RBoob_Slap_Success == 7:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a    

                with dissolve

                p "¿Ya no te molesta?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a  

                with dissolve

                d "Tampoco me vas a hacer ni puto caso..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a  

                with dissolve

                p "Eso es verdad..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a  

                with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a  

                with dissolve

                d "Gilipollas..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a    

                with dissolve

            elif afternight04__RBoob_Slap_Success == 8:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a    

                with dissolve

                p "Te sigue gustando"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a    

                with dissolve

                p "y lo sabes..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows normal_a    

                with dissolve

                d "Tssk..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a    

                with dissolve

                pt "No parece que le disguste,"

                pt "Pero tampoco da la sensación que le afecte igual..."



            elif afternight04__RBoob_Slap_Success >= 9:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a  

                d "..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a  

################################################################################################################# LBOOB

        elif afternight04__prehfix_LBoob_Slap == True: # LBoob

            $ debug ("FILL DE PUTA!!!")

            if afternight04__LBoob_Slap_Success == 1:

                if afternight04__RBoob_Slap_Done == 0:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    d "¡¿A Qué coño ha venido esto?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a

                    with dissolve

                    p "Eso me pregunto yo..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows serious_a

                    with dissolve

                    p "Pensé que gritarías o dirías \"Auh\" o algo por el estilo..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a

                    with dissolve

                    p "Y en lugar de eso has gemido..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a

                    with dissolve

                    p "¿Te va el sado Dídac?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    p "Me lo puedes decir si quieres,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                    with dissolve

                    p "podríamos decir que no hay demasiada intimidad entre nosotros..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a

                    with dissolve

                    p "especialmente ahora..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a

                    with dissolve

                    d "¡¡Tú te fumas algo!!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "Revísate el oído porque no lo tienes muy fino..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    pt "Ya..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                else: #Not the first time.

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

                    d "¡¿Ahora el otro?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "¡¿Pero a ti que te pasa?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows normal_a

                    with dissolve

                    p "Que me encanta oírte gemir de placer."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows serious_a

                    with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "Eres gilipollas."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows normal_a

                    with dissolve

                    p "Y tú una ninfómana sadomasoquista."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a

                    with dissolve

                    d "¡Idiota!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a

                    with dissolve

            elif afternight04__LBoob_Slap_Success == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                with dissolve

                d "En serio..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                with dissolve

                d "¿No te cansas?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a

                with dissolve

                p "¿De oírte gemir?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a

                with dissolve

                p "No."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a

                with dissolve

                d "..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 3:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                d "Eres cansino cuando quieres..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                with dissolve

                p "Eso no te lo puedo negar."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "¡¿No ves que me estás dejando la teta roja?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                with dissolve

                p "Y también noto que cada vez te gusta más..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "Cada vez me duele más..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                d "y como sigas así te voy a romper la puta nariz..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 5:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "Al final te voy a zurrar..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a

                with dissolve

                p "Sino te gustara,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                p "no me pondrías esa cara,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a

                with dissolve

                d "¡¿Qué cara?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a

                with dissolve

                p "¿Hace falta que lo diga?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                d "Tsssk..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 6:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                p "Dirás lo que quieras..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a

                with dissolve

                p "Pero con lo mojada que estás,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a

                with dissolve

                p "no parece que te disguste demasiado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a

                with dissolve

                p "Es más,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a

                with dissolve

                p "parece que lo disfrutas de una manera retorcida y todo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                d "Tú sí que eres retorcido..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                p "No veo que te quejes..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "¿Serviría de algo?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a

                with dissolve

                p "Probablemente no."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a

                with dissolve

                d "Idiota..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

            elif afternight04__LBoob_Slap_Success == 8:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                p "¿Ya no dices nada...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a

                with dissolve

                d "Vete a la mierda."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

                pt "Parece que ya no le disgusta del todo..."

                pt "Pero también da la sensación que ya no le afecta de igual modo..."

            elif afternight04__LBoob_Slap_Success >= 9:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a

                with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a

                with dissolve

#################################################################################################################
#################################################################################################################

    elif mc_body.roll_success == False: #You Failed.

        if afternight04__prehfix_RBoob_Slap == True: # RBoob

            if afternight04__RBoob_Slap_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿QUÉ COÑO HACES?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡¿QUIEN TE HA DICHO QUE ME AZOTES LA PUTA TETA?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡GILIPOLLAS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Está claro que no le ha gustado..."

                pt "Quizás cuando esté más caliente..."

            elif afternight04__RBoob_Slap_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡La madre que te parió!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No te lo repetiré..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Deja la puta teta en paz."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Y fóllame!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__RBoob_Slap_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡ES QUE NO ME HAS OÍDO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡TE VOY A PARTIR LA CARA AL FINAL!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__RBoob_Slap_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡JODER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡DEJA DE AZOTARMELA O AL FINAL SERÉ YO QUIEN TE VIOLE!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__RBoob_Slap_Failed == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿PERO NO VES QUE ME LA ESTÁS DEJANDO ROJA COMO UN TOMATE?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__RBoob_Slap_Failed >= 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentgx10_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            p "..."

#################################################################################################################

        elif afternight04__prehfix_RBoob_Slap == False: # LBoob

            if afternight04__LBoob_Slap_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿¡POR QUÉ COÑO ME AZOTAS LA PUTA TETA?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Reconoce que te ha gustado más de lo que imaginabas."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡PUES TE EQUIVOCAS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Quizás si consigo que se ponga algo más caliente..."

            elif afternight04__LBoob_Slap_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Serás imbécil..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "No hagas que te lo repita..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Fóllame y deja la puta teta en paz!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04__LBoob_Slap_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿OTRA VEZ?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿PADCES SORDERA?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿O QUÉ COÑO QUE TE PASA?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04__LBoob_Slap_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡ME CAGO EN LA HOSTIA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡SINO ME FOLLAS TÚ ACABARÉ HACIÉNDOLO YO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__LBoob_Slap_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

#################################################################################################################
#################################################################################################################


############################################################
    if mc_body.roll_success == False:

        if current_pose.id == "pose_1":

            if mc_body.store["left_hand"] == "RBoob_Slap":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["right_hand"] == "LBoob_Slap":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

        if current_pose.id == "pose_2" or current_pose.id == "pose_3":

            if mc_body.store["right_hand"] == "RBoob_Slap":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["left_hand"] == "LBoob_Slap":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch



############################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return

########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
###########################################################

