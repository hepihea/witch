label RButtock_Massage:

######################################################### Dummy_Screen Calls

    if current_pose.id == "pose_1":

        if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep" or mc_body.store["dick"] == "Anal_dick_low" or mc_body.store["dick"] == "Analy_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            #$ afternight04__prehfix_RButtock_Massage = False
            #$ afternight04__a_prehfix_RButtock_Massage = False

            #$ mc_body.store["right_hand"] = ""

            pt "Con mis caderas tan cerca de sus nalgas,"

            pt "me resulta imposible masajearlas,"

            pt "quizás si la tuviera a cuatro patas..."

            call screen dummy_screen()

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.02") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "RButtock_Massage."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RButtock_Massage"

    else:

        $ mc_body.store["right_hand"] = "RButtock_Massage"

#########################################################

    $ afternight04__prehfix_RButtock_Massage = True
    $ afternight04__a_prehfix_RButtock_Massage = True
        
    call afternight04_sex_check_before

    label .manager:

        $ afternight04__RButtock_Massage_Done += 1

        if mc_body.roll_success:
            
            $ afternight04__RButtock_Massage_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__RButtock_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage 
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Right Buttock.")

        call afternight04_RButtock_Massage  
        
        jump expression __prefix + "call_screen"

####################################
###################################

    label afternight04_RButtock_Massage:

        call afternight04_Buttock_Massage

        return

    label afternight04_RButtock_Massage_his_orgasm:

        call afternight04_Buttock_Massage

        call afternight04_mostly_his_orgasm

        return

    label afternight04_RButtock_Massage_her_orgasm:

        call afternight04_Buttock_Massage

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################


label afternight04_Buttock_Massage:

    #################################################################################################################
    #################################################################################################################

    if mc_body.roll_success:

        if (mc_body.store["right_hand"] == "LButtock_Massage") and (mc_body.store["left_hand"] == "RButtock_Massage"):

            $ afternight04__Buttock_Massage_Both_Success += 1

    else:

        if not "pass" in mc_body.result:

            if (mc_body.store["right_hand"] == "LButtock_Massage") and (mc_body.store["left_hand"] == "RButtock_Massage"):

                $ afternight04__Buttock_Massage_Both_Failed += 1

    #################################################################################################################
    #################################################################################################################

    if current_pose.id == "pose_1":

        if afternight04__prehfix_RButtock_Massage == True:

            show afternight04_sexbattle_mc_handL grab_buttockR_action_a
            with dissolve

        elif afternight04__prehfix_LButtock_Massage == True:

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            show afternight04_sexbattle_mc_handR grab_buttockL_action_a
            with dissolve

    else: # POSE 02 or 03

        if afternight04__prehfix_RButtock_Massage == True:

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness
            
            show afternight04_sexbattle_mc_handR buttock_massage_R_action_b
            with dissolve

        elif afternight04__prehfix_LButtock_Massage == True:

            show afternight04_sexbattle_mc_handL buttock_massage_L_action_b
            with dissolve

    #else: # POSE 02 and 03

######################
#####################

##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_LArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        #$ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        #$ afternight04__a_prehfix_RButtock_Massage = False
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

    #HER REACTION:
############################################################
###########################################################

    if mc_body.roll_success == True:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            d "Uhmm..."

        elif randomnum_1to10 == 2:

            d "Hmm..."

        elif randomnum_1to10 == 3:

            d "Ughmm..."

        elif randomnum_1to10 == 4:

            d "Auhmm..."

        elif randomnum_1to10 == 5:

            d "mmMmf..."

        elif randomnum_1to10 == 6:

            d "Aughmm..."

        elif randomnum_1to10 == 7:

            d "Mmm..."

        elif randomnum_1to10 == 8:

            d "Uhghmm..."

        elif randomnum_1to10 == 9:

            d "Muhfmm..."

        elif randomnum_1to10 == 10:

            d "Hmmm..."


    else: # You failed.

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "Pff..."

        elif randomnum_1to5 == 2:

            d "Joder..."

        elif randomnum_1to5 == 3:

            d "Aishh..."

        elif randomnum_1to5 == 4:

            d "Hmpfh..."

        elif randomnum_1to5 == 5:

            d "Tsk..."

############################################################

        if mc_body.store["left_hand"] == "RButtock_Massage":

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty

            with hpunch

        if mc_body.store["right_hand"] == "LButtock_Massage":

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

            with hpunch

############################################################
###########################################################


############################################################
###########################################################

############################################################
###########################################################
    
    $ debug("Some TEST text")
    
    # progcheck "RButtock_Massage_Success = [afternight04__RButtock_Massage_Success], 
            # \nRButtock_Massage_Failed = [afternight04__RButtock_Massage_Failed], 
            # \nLButtock_Massage_Success = [afternight04__LButtock_Massage_Success], 
            # \nLButtock_Massage_Failed = [afternight04__LButtock_Massage_Failed]."


    #HER REACTION:

    if ((afternight04__RButtock_Massage_Done) + (afternight04__LButtock_Massage_Done)) == 1: # 1rst Time.

        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¿Ahora te da por toquetearme las nalgas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "¿Alguna queja?"

            if mc_body.roll_success == True: #You succeded.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "mientras sigas manteniendo esa {i}Anaconda{/i} tuya aquí dentro,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "no tengo ninguna objeción."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx5_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Pfff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Haz lo que quieras,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "pero no me quites esa polla de ahí."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿En serio [protname]?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿Ahora te da por acariciarme las nalgas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Mira..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Hasta cierto punto,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "no me parece algo descabellado..."

            if mc_body.roll_success == True: #You succeded.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Pero al menos métemela de una jodida vez!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡PERO AL MENOS FÓLLAME!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


            if current_pose.id == "pose_1":

                pt "En esta posición lo tendré un poco complicado para hacer ambas cosas a la vez..."

    elif (mc_body.store["right_hand"] == "LButtock_Massage") and (mc_body.store["left_hand"] == "RButtock_Massage"):

        if mc_body.roll_success == True: #You succeded.

            if afternight04__Buttock_Massage_Both_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Ahora me manoseas las dos a la vez?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Te mola mi culo por lo que veo..."

                if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Como no muevas esa polla,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "me voy a cabrear..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    elif mc_body.dick_speed == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Pero como no muevas un poco más esa polla,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "No me vas a tener contenta..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Intento ponerte cachonda,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "no contenta."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        p "No confundas lo que me has pedido."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Estás fatal..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                    elif mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Por lo menos lo aprovechas mientras usas tu polla."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "Algo es algo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Si por lo menos lo aprovecharas para follarme más fuerte..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Vas a estar mucho rato con tus manos en mis nalgas?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                p "¿Por qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "¿Te molestan?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1": ## Transform these into _c pose 3
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        d "Quizás me molestaría menos si movieras un poco más esa polla tuya."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else: #Dick in movement

                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Aunque si movieras esa polla un poco más rápido,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "sería de agradecer..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils right02_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "Te estoy follando,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¿Verdad?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils right01_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "Entonces no te quejes."
                            
                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Tchh..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_3": #Only Pose 3 is available for fuck
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_c
                                show afternight04_sexbattle_d_eyes 03_c
                                show afternight04_sexbattle_d_pupils front03_c
                                show afternight04_sexbattle_d_eyebrows angryx01_c
                                with dissolve

                            d "En realidad,"

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_c
                                show afternight04_sexbattle_d_eyes 02_c
                                show afternight04_sexbattle_d_pupils front02_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                            d "mientras me sigas follando,"

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_c
                                show afternight04_sexbattle_d_eyes 05_ac
                                show afternight04_sexbattle_d_pupils front05_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                            d "no me voy a quejar."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx02_c
                                show afternight04_sexbattle_d_eyes 01_c
                                show afternight04_sexbattle_d_pupils front01_c
                                show afternight04_sexbattle_d_eyebrows serious_c
                                with dissolve

                            p "Entonces cierra la boca."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_c
                                show afternight04_sexbattle_d_eyes 03_c
                                show afternight04_sexbattle_d_pupils front03_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_c
                                show afternight04_sexbattle_d_eyes 04_c
                                show afternight04_sexbattle_d_pupils right04_c
                                show afternight04_sexbattle_d_eyebrows angryx03_c
                                with dissolve

                            d "Tcch..."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_c
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils right05_c
                                show afternight04_sexbattle_d_eyebrows sadx04_c
                                with dissolve


                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Quizás me pondrías más perra si lo hicieras mientras me la metes..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                        p "Teniéndote encima va a ser complicado."

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                        d "..."

                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                        d "Pfff..."

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    else:
                        # if current_pose.id == "pose_3":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_c
                        show afternight04_sexbattle_d_eyes 02_c
                        show afternight04_sexbattle_d_pupils front02_c
                        show afternight04_sexbattle_d_eyebrows normal_c
                        with dissolve

                        p "Como la perra que eres,"

                        show afternight04_sexbattle_d_mouth sadbiting_Talkingx02_c
                        show afternight04_sexbattle_d_eyes 03_c
                        show afternight04_sexbattle_d_pupils front03_c
                        show afternight04_sexbattle_d_eyebrows angryx01_c
                        with dissolve

                        p "estando a cuatro patas..."

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils right05_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                        with dissolve

                        p "¿Verdad?"

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_c
                        show afternight04_sexbattle_d_eyes 03_c
                        show afternight04_sexbattle_d_pupils front03_c
                        show afternight04_sexbattle_d_eyebrows angryx01_c
                        with dissolve

                        p "Eso te pone toda perraca..."

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils right05_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                        with dissolve

                        d "..."

                        show afternight04_sexbattle_d_mouth sad_Talkingx003_c
                        show afternight04_sexbattle_d_eyes 04_c
                        show afternight04_sexbattle_d_pupils right04_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                        with dissolve

                        d "Gilipollas..."

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils right05_c
                        show afternight04_sexbattle_d_eyebrows sadx02_c
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "¿Qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Veo que te gustan mis nalgas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Son blandas y al mismo tiempo musculosas cuando te pones tensa."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "Tienen un tacto agradable y además,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "Por mucho que intentes negarlo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "te pones más cachonda cuando lo hago."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "No flipes..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Ya..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¿Y esa polla planeas moverla en algún momento?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    if mc_body.dick_speed == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    elif mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Mientras me sigas follando así..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

            elif afternight04__Buttock_Massage_Both_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Reconozco que no se siente tan mal ese masaje a dos manos en mis nalgas..."

                if (afternight04__RButtock_Slap_Success > 2) and (afternight04__LButtock_Slap_Success > 2):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Aunque quizás se sentiría mejor,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "sino tuviera mis nalgas rojas como un tomate..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Aunque esa polla tuya está muy quieta."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    if mc_body.dick_speed == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Aunque mueves tu polla como un caracol..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    elif mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Pero sigue así con tu polla..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

            elif afternight04__Buttock_Massage_Both_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "La verdad es que vas mejorando con el masaje a dos manos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Aunque podrías mover esa polla tuya."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    if mc_body.dick_speed == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Aunque podrías aumentar el ritmo de esa polla tuya..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    elif mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Pero no detengas esa polla tuya..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sad04_a
                            with dissolve

            elif afternight04__Buttock_Massage_Both_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "No voy a negarlo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Reconozco que sabes dar un buen masaje con ambas manos..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Pero mueve la polla de una jodida vez!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡Hostias!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    else: #Dick in movement

                        if current_pose.id == "pose_3": #Pose 1 is possible?
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_c
                            show afternight04_sexbattle_d_eyes 04_c
                            show afternight04_sexbattle_d_pupils front04_c
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_c
                            with dissolve

                        d "Y si lo haces mientras me estás follando,"

                        if current_pose.id == "pose_3":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_c
                            show afternight04_sexbattle_d_eyes 05_c
                            show afternight04_sexbattle_d_pupils front05_c
                            show afternight04_sexbattle_d_eyebrows angryx02_c
                            with dissolve

                        d "mucho mejor..."

                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_c
                                show afternight04_sexbattle_d_eyes 04_c
                                show afternight04_sexbattle_d_pupils front04_c
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_c
                                with dissolve

                            d "aunque si subieras el ritmo..."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_c
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils front05_c
                                show afternight04_sexbattle_d_eyebrows suspiciousx02_c
                                with dissolve

                            d "Ni te cuento..."

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 06_a
                                show afternight04_sexbattle_d_pupils front06_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                            d "Y a este ritmo,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils down03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "se siente genial..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils down05_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                    if current_pose.id == "pose_3":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils front05_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                        with dissolve

                    d "Pero ni se te ocurra sacarla de ahí..."

                    if current_pose.id == "pose_3":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils front05_c
                        show afternight04_sexbattle_d_eyebrows angryx03_c
                        with dissolve

                    d "¡¿Me explico?!"

                    if current_pose.id == "pose_3":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_c
                        show afternight04_sexbattle_d_eyes 05_c
                        show afternight04_sexbattle_d_pupils front05_c
                        show afternight04_sexbattle_d_eyebrows angryx02_c
                        with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pero al menos podrías meterme la polla de una jodida vez!"

                    if (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        p "Pe..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx09_a
                            show afternight04_sexbattle_d_eyes 00_a
                            show afternight04_sexbattle_d_pupils front00_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡NO!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx004_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡No me refiero por el jodido culo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡No hagas que te lo repita!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                p "..."

            elif afternight04__Buttock_Massage_Both_Success >= 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

#################################################################################################################

        if mc_body.roll_success == False: #You Failed.

            if afternight04__Buttock_Massage_Both_Failed == 1:

                if afternight04__Buttock_Massage_Both_Done == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Ahora te da para hacerlo con las dos a la vez?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "Me parece genial que te mole magrearme el culo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "con mi cuerpo de tío no lo hacías,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "pero ahora sí."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Hombre,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "antes no tenías este culo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¡Pero al menos podrías mover un poco esa polla!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                    else: #Dick in movement

                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Por lo menos me lo haces mientras me follas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Algo es algo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            p "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Aunque aumentar el ritmo no estaría mal tampoco..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Y te mola hacerlo mientras me estás follando..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Silentx04_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Eres un sinvergüenza..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            pt "¿Se está poniendo juguetón?"

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Pero al menos podrías follarme!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Failed == 2:

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Agarrándome de ambas nalgas..."

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Si por lo menos te movieras un poco..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else: #Dick in movement

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Al menos estás haciendo lo que te he pedido."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Muy bien eso de estar agarrándome de ambas nalgas,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "y me parece genial que te pongas todo perro con ello..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿PERO CUANDO PIENSAS FOLLARME?!"

                    if (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "Ya lo estoy haciendo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡EN MI CULO!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        pt "Cierto..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

            elif afternight04__Buttock_Massage_Both_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Tú y tu manía de agarrarme por las jodidas nalgas..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¡Por lo menos podrías moverla!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    else: #Dick in movement

                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            d "Aunque podrías ir un poco más deprisa si quisieras..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            d "Por lo menos me estás follando como es debido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Cuando yo hago eso con una tía;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Al menos lo hago mientras me la estoy follando!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es que me queje de que me masajees ambas nalgas..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Aunque si te movieras,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "estaría mejor..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else: #Dick in movement

                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Aunque los he visto más rápidos..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Al menos estás haciendo lo que te he pedido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pero al menos podrías estar follándome!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    if current_pose.id == "pose_1":

                        pt "Mientras te tenga encima,"

                        pt "va a ser complicado hacer ambas cosas a la vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡No hagas que te lo repita [protname]!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Failed == 5:

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "¿Pretendes dejar la polla ahí tiesa como una planta,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "mientras me manoseas ambas piernas?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    else: #Dick in movement
                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "¿Tienes miedo de coger una hernia si vas un poco más rápido?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "¡Dale un poco de brillo a tus caderas!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "¡Narices!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Manoséame lo que quieras."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            d "¡Pero no pares de follarme!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    d "¿Intentas poner mi paciencia a prueba [protname]?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Failed == 6:

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "O mueves tu jodida Anaconda,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡O te voy a meter esas jodidas manos por el orto!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    else: #Dick in movement
                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "O mueves más rápido esa cadera tuya..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "O al final voy a hacerlo yo misma."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "No pares campeón..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

            elif afternight04__Buttock_Massage_Both_Failed >= 7:

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    else: #Dick in movement
                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                d "..."

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: #Dick Stop. #POSE_1 is NOT possilbe.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    else: #Dick in movement
                        if mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                else: #No dick

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx09_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

#################################################################################################################
#################################################################################################################

    else: #Not Both Hands.

        if mc_body.roll_success == True: #You succeded.

            if afternight04__prehfix_RButtock_Massage == True:

                if afternight04__RButtock_Massage_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Ahora te da por toquetearme la otra nalga?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "No te tenía por un sobón..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Por lo visto,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "cuando tú quedas con una chica,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "la pones contra el muro,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "te corres,"

                    extend " y te vas."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "Eres todo un seductor."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Pff..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Te crees que a todas les gusta este tipo de mariconadas?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Con las que has quedado tú lo desconozco,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "Lo que sí tengo claro,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "es que a ti te pone."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Pff..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Sigue soñando."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04__RButtock_Massage_Success == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Otra vez sobándome la nalga?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "¿Es que quieres pulírmela hasta que te veas reflejada en ella?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Por lo menos me la has metido dentro..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Al menos podrías metérmela dentro de una jodida vez..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                elif afternight04__RButtock_Massage_Success == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Debo reconocer que no lo haces tan mal..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is NOT possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pero al menos podrías moverla un poco,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "que así va a coger gangrena..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            pt "Con lo estrecho que tienes tu coño,"

                            pt "me mueva o no me temo que la voy a tener igual..."

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "¡Pero estaría bien que me la metieras de una jodida vez!"

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Aunque estaría bien que la metieras de una vez..."

                        if mc_body.dick_speed >= 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                            p "¿No puedes estar cinco minutos sin tener que mencionarlo?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            p "Si en el fondo te gusta y lo sabes..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Tsskk..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sad01_a
                                with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Pero si por lo menos tuviera tu polla dentro..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Estaría mucho mejor."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                elif afternight04__RButtock_Massage_Success == 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Me lo parece..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¿O empieza a gustarte?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Idiota..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿A quien no le gusta un masaje?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Lo que pasa es que no quiero relajarme,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "quiero desahogarme."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Creo que eres capaz de entender la diferencia."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Para eso tienes mi polla dentro de ti."

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pero sería interesante si la movieras un poco..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve
                        
                            d "Pero moverla un poco más rápido no te haría ningún daño..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve 

                            p "Nunca estás contento,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¿Verdad?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Pfff..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Eso está bien [protname]."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Al final va a resultar que no eres un completo desastre..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            pt "Como si él fuera un ejemplo a seguir..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils down05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                        p "..."

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                elif afternight04__RButtock_Massage_Success == 5:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Vale,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "reconozco que no lo haces tan mal..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "Al menos en esta nalga."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    pt "¿En la otra tiene otra sensibilidad?"

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils down03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                                with dissolve

                            d "Pero esa polla sigue ahí quieta."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Pero sigues moviéndote como un caracol."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sabiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down4_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            d "Pero no detengas esa Anaconda tuya..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Pero usa tu polla de una jodida vez."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                elif afternight04__RButtock_Massage_Success == 6:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Tienes buenas manos [protname]..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils down03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Pero mueve ya tu jodida polla."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Sé que puedes moverla más rápido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils down03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Sigue así..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Pero como no metas pronto tu polla aquí dentro,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "me voy a cabrear."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                elif afternight04__RButtock_Massage_Success == 7:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "Sin duda le encanta,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    pt "pero al mismo tiempo tampoco le afecta del mismo modo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "Quizás debería empezar a pensar en alternativas."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve


                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve


                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve


                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve


                elif afternight04__RButtock_Massage_Success == 8:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Vas a seguir mucho más rato así?"

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Como no empieces a moverte pronto,"

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Como no le metas más caña a esa Anaconda tuya,"

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "¡¿No te estoy follando cómo me has pedido?!"

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "Como no me la metas pronto,"

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "Sí..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    else: #No Fast Dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Voy a tenerlo que hacer yo al final."

                        if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve
                        p "..."

                elif afternight04__RButtock_Massage_Success >= 9:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils down04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    d "..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

################################################################################################################# LBOOB

            elif afternight04__prehfix_RButtock_Massage == False: # LBoob

                if afternight04__LButtock_Massage_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Ahora la otra?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "No estás contento si no masajeas las dos..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿Verdad?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Cualquiera diría que te disgusta."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Hmm..."

                elif afternight04__LButtock_Massage_Success == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Me parece bien que te guste toquetearme el trasero..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Al fin y al cabo es algo que también me encanta de una tía..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "Aunque se me hace raro ser yo la manoseada..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Por tus manos..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Aunque ya te podrías mover de una jodida vez..."

                        elif mc_body.dick_speed == 1:

                            d "Aunque podrías moverte un poco más rápido..."

                        elif mc_body.dick_speed >= 2:

                            d "Pero por lo menos me estás follando como te he pedido..."

                    else: #No dick

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        d "Pero al menos me la podrías meter dentro."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        if current_pose.id == "pose_1":

                            pt "Si te tengo encima es complicado hacer las dos cosas a la vez..."

                elif afternight04__LButtock_Massage_Success == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Aunque se siente raro de narices..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "La verdad es que es agradable..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            d "Especialmente si me follaras de una vez."

                        elif mc_body.dick_speed == 1:

                            d "Especialmente si te movieras..."

                        elif mc_body.dick_speed >= 2:

                            d "Especialmente si lo haces mientras me follas..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve
                        
                        d "Pero si lo hicieras mientras estás follando,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "sería muchísimo mejor..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                elif afternight04__LButtock_Massage_Success == 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "quizás no eres tan mal masajista después de todo..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            d "Aunque desde luego mejoraría si te movieras un poco..."

                        elif mc_body.dick_speed == 1:

                            d "Aunque habría maneras de mejorarlo..."

                        elif mc_body.dick_speed >= 2:

                            d "Mmm..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Pero de follador tienes poco..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                elif afternight04__LButtock_Massage_Success == 5:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No está mal [protname]..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            d "Pero muévete..."

                        elif mc_body.dick_speed == 1:

                            d "Pero sé que puedes ser más rápido follándome..."

                        elif mc_body.dick_speed >= 2:

                            d "Hmm..."

                    else:
                        
                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "Pero si lo hicieras mientras estás follando,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "sería muchísimo mejor..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¿Ya no lo sientes raro que te lo haga yo?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Sigue siendo raro de cojones."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils left03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Pero tampoco voy a convencerte de lo contrario..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "No..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Si raro es,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "pero tampoco veo que mi polla baje o tu coño deje de estar caliente por esto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Ya..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                elif afternight04__LButtock_Massage_Success == 6:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Vale,"

                    extend " vale..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tienes buenas manos para dar masajes."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            d "Pero tu polla sigue ahí quieta..."

                        elif mc_body.dick_speed == 1:

                            d "Pero sigues sin moverte demasiado..."

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_c
                                show afternight04_sexbattle_d_eyes 03_c
                                show afternight04_sexbattle_d_pupils right03_c
                                show afternight04_sexbattle_d_eyebrows angryx01_c
                                with dissolve

                            d "Lo reconozco..."

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_c
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils right05_c
                                show afternight04_sexbattle_d_eyebrows sadx02_c
                                with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Pero como no me folles"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "voy a ser yo quien lo haga al final."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve
                        

                elif afternight04__LButtock_Massage_Success >= 7:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                                show afternight04_sexbattle_d_eyes 03_c
                                show afternight04_sexbattle_d_pupils front03_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_c
                                show afternight04_sexbattle_d_eyes 04_c
                                show afternight04_sexbattle_d_pupils front04_c
                                show afternight04_sexbattle_d_eyebrows angryx01_c
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_c
                                show afternight04_sexbattle_d_eyes 04_c
                                show afternight04_sexbattle_d_pupils front04_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    d "..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0: #Dick Stop. #pose_1 is not possilbe.

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils front05_c
                                show afternight04_sexbattle_d_eyebrows angryx03_c
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_c
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils front05_c
                                show afternight04_sexbattle_d_eyebrows angryx02_c
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_3":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_c
                                show afternight04_sexbattle_d_eyes 05_c
                                show afternight04_sexbattle_d_pupils front05_c
                                show afternight04_sexbattle_d_eyebrows sadx03_c
                                with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

#################################################################################################################
#################################################################################################################

        elif mc_body.roll_success == False: #You Failed.

            if afternight04__prehfix_RButtock_Massage == True: # RButtock

                if afternight04__RButtock_Massage_Failed == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿De verdad tienes que ir tocándome la nalga?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿No se te ocurre otra cosa más gay que hacer?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Cómo meterte mi polla por un agujero que no debería ni de existir?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Exacto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Creo que no ha entendido el sarcasmo..."


                elif afternight04__RButtock_Massage_Failed == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Otra vez manoseándome?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tío..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Qué?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¡¿No le has tocado nunca las nalgas a una tía?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pero es que no soy una tía!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Soy Dídac!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "No me hagas sentir más incómodo de lo que ya me siento!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Su lógica es aplastante..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Fóllame,"

                    pt "pero no me toquetees..."

                    pt "Eso es muy homosexual,"

                    pt "lo otro no..."

                elif afternight04__RButtock_Massage_Failed == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Qué mierdas intentas conseguir pasando tu mano por mis nalgas?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "El erotismo no es tu fuerte."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                elif afternight04__RButtock_Massage_Failed == 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Como vuelvas a pasar tus jodidas manos por mis nalgas,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "pero no tenga mi polla dentro moviéndose,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "me voy a cabrear de verdad."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and (mc_body.dick_speed > 0):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "¡Pero si ya te estoy follando!"

                        if mc_body.dick_speed < 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils right01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pero podrías moverla un poco más rápido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¡¿Es que no estás contento con nada?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pff..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils right00_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pues ni se te ocurra parar."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils right02_a
                                show afternight04_sexbattle_d_eyebrows surprisex01_a
                                with dissolve

                            p "Un gracias no estaría mal..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils left03_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            p "Te recuerdo que te estoy haciendo un favor."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 07_a
                                show afternight04_sexbattle_d_pupils front07_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Tssk..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                            pt "Ni con esas..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        p "..."

                elif afternight04__RButtock_Massage_Failed == 5:

                    if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and (mc_body.dick_speed == 0):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "No te lo voy a repetir [protname]."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "..."

                elif afternight04__RButtock_Massage_Failed >= 6:

                    if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and (mc_body.dick_speed == 0):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx08_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    d "..."

#################################################################################################################

            elif afternight04__prehfix_RButtock_Massage == False: # LButtock

                if afternight04__LButtock_Massage_Failed == 1:

                    if afternight04__LButtock_Massage_Done == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡¿Ahora le toca a la otra nalga?!"

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "De verdad..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Qué diablos pretendes manoseándome las nalgas?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¿No tienes ni la más mínima paciencia para el juego previo?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡¿Eres consciente de que tengo un pollón enorme?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡y que es bastante necesario ese juego previo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡No tienes ni idea de con qué mierdas he estado trasteando antes de que llegaras!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Y aún así tampoco hace falta que me la metas entera..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Ya,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "eso es lo que dices ahora..."

                elif afternight04__LButtock_Massage_Failed == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿De verdad crees que manosearme la jodida nalga,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "va a servir para ensanchar mi coño?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿En qué mierda de página de las narices has leído semejante gilipollez?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "Cuando una mujer se excita,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "su parte vaginal se lubrica y se ensancha para prepararse mejor."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Como si fuera un jodido globo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Tú que te fumas?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿La polla no se te hinchaba cuando te ponías caliente?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Me vas a comparar la polla con un coño..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "Es una pérdida de tiempo intentar razonar con él..."

                elif afternight04__LButtock_Massage_Failed == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Pareces un niñato que nunca ha tenido un culo delante,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "del modo en que me lo estás sobando..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿O es que ya te gustaba antes de volverme chica,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "y ahora estás usando esta situación como excusa?"

                    
                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        pt "La madre que lo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "¡Te estoy follando!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "¡¿no?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        p "¡¿No es lo que querías?!"

                        if mc_body.dick_speed == 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¡Pero si ni siquiera la estás moviendo!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            p "..."

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "También podrías moverla un poco más rápido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "No te contentas con nada."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

                            d "..."

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Eso es verdad..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¡Pues cállate de una jodida vez!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Tchh..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx02_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "Eres un jodido retorcido mental..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡¿Entonces a qué coño esperas para metérmela?!"

                        if (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡Y no!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "¡No me refiero por el jodido culo!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Maricón,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                                with dissolve

                            d "que eres un jodido maricón."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                            pt "¿Yo soy el maricón?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            pt "Huevazos que tiene el cabrón..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "..."

                elif afternight04__LButtock_Massage_Failed == 4:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "¿No dices nada?"

                        if mc_body.dick_speed == 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Que también la podrías mover."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                        elif mc_body.dick_speed == 1:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Solo que podrías follarme un poco más rápido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        elif mc_body.dick_speed >= 2:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Si esto te pone cachondo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Mientras no me dejes de follar."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡EN SERIO!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡Ya basta de toquetearme tanto!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "¡No te lo voy a repetir!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                elif afternight04__LButtock_Massage_Failed >= 5:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and (mc_body.dick_speed > 0):

                        if current_pose.id == "pose_1": # Pose 1 ButtockMassage I think is impossible...
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                    d "..."

#################################################################################################################
#################################################################################################################


############################################################
    if mc_body.roll_success == False:

        if current_pose.id == "pose_1":

            if mc_body.store["left_hand"] == "RButtock_Massage":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["right_hand"] == "LButtock_Massage":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

        if current_pose.id == "pose_2" or current_pose.id == "pose_3":

            if mc_body.store["right_hand"] == "RButtock_Massage":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["left_hand"] == "LButtock_Massage":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch



############################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")) and (mc_body.dick_speed == 0):

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




