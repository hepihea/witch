label RLeg_Massage:

#########################################################

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.04"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "RLeg_Massage."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RLeg_Massage"

    else:

        $ mc_body.store["right_hand"] = "RLeg_Massage"

#######################################################

    $ afternight04__prehfix_RLeg_Massage = True
    $ afternight04__a_prehfix_RLeg_Massage = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__RLeg_Massage_Done += 1

        if afternight04_SheRapingYou == True:

            if mc_body.roll_success:
                $ afternight04__RLeg_Massage_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__RLeg_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RLeg_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Right Leg with your Left Hand.")

        call afternight04_RLeg_Massage
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################


    label afternight04_RLeg_Massage:

        call afternight04_Leg_Massage

        return


    label afternight04_RLeg_Massage_his_orgasm:

        call afternight04_Leg_Massage

        call afternight04_mostly_his_orgasm

        return

    label afternight04_RLeg_Massage_her_orgasm:

        call afternight04_Leg_Massage

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################


##DESCRIPTION Leg_Massage

label afternight04_Leg_Massage:

    #################################################################################################################
    #################################################################################################################

    if mc_body.roll_success:

        if (mc_body.store["right_hand"] == "LLeg_Massage") and (mc_body.store["left_hand"] == "RLeg_Massage"):

            $ afternight04__Leg_Massage_Both_Success += 1

    else:

        if not "pass" in mc_body.result:

            if (mc_body.store["right_hand"] == "LLeg_Massage") and (mc_body.store["left_hand"] == "RLeg_Massage"):

                $ afternight04__Leg_Massage_Both_Failed += 1

    #################################################################################################################
    #################################################################################################################

    if current_pose.id == "pose_1":

        if afternight04__prehfix_RLeg_Massage == True:
        #if mc_body.store["left_hand"] == "RLeg_Massage":

            $ mc_body.store["left_hand"] == "RLeg_Massage"

            show afternight04_sexbattle_mc_handL massage_legR_action_a
            ###show afternight04_sexbattle_mc_handR_penetrate_pussy empty # This is not Right Hand.
            with dissolve

        if afternight04__prehfix_LLeg_Massage == True:
        #elif mc_body.store["right_hand"] == "LLeg_Massage":

            $ mc_body.store["right_hand"] == "LLeg_Massage"

            show afternight04_sexbattle_mc_handR massage_legL_action_a

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            with dissolve

    elif current_pose.id == "pose_2" or current_pose.id == "pose_3":

        if afternight04__prehfix_RLeg_Massage == True:

            $ mc_body.store["right_hand"] == "RLeg_Massage"

            #show afternight04_sexbattle_mc_handR massage_legR_action_b # Not done yet.
            

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty 

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            with dissolve

        if afternight04__prehfix_LLeg_Massage == True:

            $ mc_body.store["left_hand"] == "LLeg_Massage"

            #show afternight04_sexbattle_mc_handL massage_legL_action_b # Not done yet.
            ###show afternight04_sexbattle_mc_handR_penetrate_pussy empty # This is not Right Hand.
            with dissolve

##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_LArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        
        #$ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        $ afternight04__a_prehfix_RButtock_Massage = False
        $ afternight04__a_prehfix_RButtock_Slap = False
        
        #$ afternight04__a_prehfix_RLeg_Massage = False
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
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
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
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
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

        if current_pose.id == "pose_1":

            if afternight04__prehfix_RLeg_Massage == True:
            #if mc_body.store["left_hand"] == "RLeg_Massage":

                #$ mc_body.store["left_hand"] = ""
                show afternight04_sexbattle_mc_handL empty

                with hpunch

            if afternight04__prehfix_LLeg_Massage == True:
            #if mc_body.store["right_hand"] == "LLeg_Massage":

                #$ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty

                with hpunch

        elif current_pose.id == "pose_2" or current_pose.id == "pose_3":


            if afternight04__prehfix_RLeg_Massage == True:
            #if mc_body.store["right_hand"] == "RLeg_Massage":

                #$ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty

                with hpunch

            if afternight04__prehfix_LLeg_Massage == True:
            #if mc_body.store["left_hand"] == "LLeg_Massage":

                #$ mc_body.store["left_hand"] = ""
                show afternight04_sexbattle_mc_handL empty

                with hpunch


############################################################
###########################################################

############################################################
###########################################################

    if not current_pose.id == "pose_2" or current_pose.id == "pose_3":

        $ debug("Some TEST text")

        # progcheck "RLeg_Massage_Success = [afternight04__RLeg_Massage_Success], 
                # \nRLeg_Massage_Failed = [afternight04__RLeg_Massage_Failed], 
                # \nLLeg_Massage_Success = [afternight04__LLeg_Massage_Success], 
                # \nLLeg_Massage_Failed = [afternight04__LLeg_Massage_Failed]."


        #HER REACTION:

        if (mc_body.store["right_hand"] == "LLeg_Massage") and (mc_body.store["left_hand"] == "RLeg_Massage"):

            if mc_body.roll_success == True: #You succeded.

                if afternight04__Leg_Massage_Both_Success == 1:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Podrías poner más atención a mover tu polla,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "en lugar de tu mano..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "En lugar de estar tocándome las piernas,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "preferiría que me estuvieras follando como te he pedido..."

                    if afternight04__prehfix_RLeg_Massage == True:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Te gusta,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows surprisex02_a
                            with dissolve

                        p "y lo sabes..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        d "Estás agilipollado perdido..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                    elif afternight04__prehfix_LLeg_Massage == True:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "¿Por qué?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "¿No te gusta lo que te hago?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "No he dicho eso..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                elif afternight04__Leg_Massage_Both_Success == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Es que te crees que me tienes que encerar ambas piernas como si fuera el chasis de un coche?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Deja de quejarte."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Además,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows surprisex02_a
                            with dissolve

                        p "tengo la polla dónde quieres que esté,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        p "¿no?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        p "Cansino,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "que eres un cansino."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Tu polla no está dónde me gustaría que estuviera..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve


                elif afternight04__Leg_Massage_Both_Success == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Eso de que me masajees las dos piernas a la vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿Es algún tipo de ritual?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "¿Extracción de energía?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Viendo como gimes,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "creo puede ser algo distinto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "..."

                elif afternight04__Leg_Massage_Both_Success == 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Dirás lo que quieras,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "pero eres incluso más sensible que la mayoría de las mujeres que he conocido al tacto."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Eso está en tu retorcida imaginación."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "¡¡HHMmm...!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "Sin duda."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Gilipollas!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                elif afternight04__Leg_Massage_Both_Success == 5:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Reconozco que no se te da mal..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Especialmente si usas tu polla para algo."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Me parece muy bien que sepas hacer masajes a dos manos de puta madre."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Pero como no me metas esa polla dentro,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "seré yo quien me la meta."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¿Me explico?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    p "..."

                elif afternight04__Leg_Massage_Both_Success == 6:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Sí,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "me encanta sentir tus manos en mis piernas."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Pero ni se te ocurra sacar tu polla de ahí."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        d "¿Capisci?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "No te lo voy a repetir."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "O me follas."
                        
                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¡O te cabalgo!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡¿Me explico?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    p "..."


                elif afternight04__Leg_Massage_Both_Success >= 7:

                    if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                    d "..."

    #################################################################################################################

            if mc_body.roll_success == False: #You Failed. BOTH hands.

                if afternight04__Leg_Massage_Both_Failed == 1:

                    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):

                        if mc_body.dick_speed < 1: #Slow Fuck

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Muy bonito esto de tocarme las piernas,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Se llame como se llame este fetiche..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Pero también podrías mover esa polla un poco más rápido..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        else: #Pussy fast 02
                            $ afternight04__Leg_Massage_Both_Failed -= 1

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Bueno,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspicious_x01_a
                                with dissolve

                            d "si lo haces mientras te mueves..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                    else: # Not Pussy Fuck

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Me parece muy bien que me quieras masajear con ambas manos y eso..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡¿Pero a qué coño esperas para usar la puta polla?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        p "Eres un ansias."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Y tú un pesado."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                elif afternight04__Leg_Massage_Both_Failed == 2:

                    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):

                        if mc_body.dick_speed < 1: #Slow Fuck

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Si de verdad quieres magrearme"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "me parece muy bien."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡Pero acelera es ritmo!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "He visto orugas moviéndose más rápido!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                        else: #Pussy fast 02
                            $ afternight04__Leg_Massage_Both_Failed -= 1

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            d "Vale,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            d "así sí se siente bien que me acaricies..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                    else: # Not Pussy Fuck

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡¿Estás esperando a mi cumpleaños?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "¿Qué?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx006_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡Que me folles de una vez!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        if afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx005
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¡Pero si ya te la has metido tú sola antes!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx06
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡¿Y estás esperando a que lo haga de nuevo!?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        elif afternight04_Pussy_dick_med_Speed_0_Done > 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¡Pero si ya te la he metido!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¡¿Y no piensas volver a metérmela?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡¿Quieres que lo haga yo?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                elif afternight04__Leg_Massage_Both_Failed == 3:

                    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):

                        if mc_body.dick_speed < 1: #Slow Fuck

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Si tocarme las piernas te va a distraer tanto,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Déjalas en paz."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡Pero mueve un poco más rápido esas caderas!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve
                            

                        else: #Pussy fast 02
                            $ afternight04__Leg_Massage_Both_Failed -= 1

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            d "Esto ya es otra cosa..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pero no pares."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils up05_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                    else: # Not Pussy Fuck

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Sino me la metes pronto..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "me voy a cabrear de verdad..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                elif afternight04__Leg_Massage_Both_Failed >= 4:

                    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):

                        if mc_body.dick_speed < 1: #Slow Fuck

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve


                        else: #Pussy fast 02

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils up05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve


                    else: # Not Pussy Fuck

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx07_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve


                    d "..."

                p "..."

    #################################################################################################################
    #################################################################################################################

        else: #Not Both Hands.

            if mc_body.roll_success == True: #You succeded.

                if afternight04__prehfix_RLeg_Massage == True: # RLeg

                    if afternight04__RLeg_Massage_Success == 1:

                        if afternight04__LLeg_Massage_Done == 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "¡Qué se supone que estás haciendo?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                                with dissolve

                            p "Masajearte la pierna."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 07_a
                                show afternight04_sexbattle_d_pupils front07_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "¿Te he pedido un masaje?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "No."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "¿Entonces?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silenetx03_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¡Por el amor de un perro!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¡Se trata de ir calentando el ambiente!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¡Yo ya voy caliente!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¡Pero quizás yo no!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils down02_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            d "Tu polla está bien dura..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils down05_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            d "¿En serio [protname]?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "¿Ahora con la otra pierna?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "..."

                    elif afternight04__RLeg_Massage_Success == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "¿Te gusta mucho mi pierna derecha?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx01_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Tanto como tu izquierda."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "..."

                    elif afternight04__RLeg_Massage_Success == 3:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "No te cansas..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03_a
                            show afternight04_sexbattle_d_eyes 00_a
                            show afternight04_sexbattle_d_pupils front00_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "Y tú no te callas."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils right02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils right02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Gilipollas..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    elif afternight04__RLeg_Massage_Success == 4:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front1_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "¿Qué?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Nada..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "no he dicho nada..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        pt "No parece que le disguste tanto..."

                    elif afternight04__RLeg_Massage_Success == 5:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Prefería que te centraras en otra cosa y no con mi pierna..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "Déjame elegir a mi lo que crea más conveniente para hacerte el puñetero favor que me has pedido."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "No agotes mi paciencia [protname]..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            pt "Quizás tiene razón y sería mejor no tentar más a la suerte con la misma pierna..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 07_a
                                show afternight04_sexbattle_d_pupils front07_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            p "¿No es lo que querías?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            p "Sentir mi polla dentro."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbotomg_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            p "Puedo hacer ambas cosas a la vez."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Pero no te despistes..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¿Es que nunca estás contento con nada?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "Tssk..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Success == 6:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "¿Cuando piensas meterme la polla?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "¿Soy yo?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¿O parece que empieza a gustarte el masaje...?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Me gusta tener tu polla dentro."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils right02_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "No te hagas otras ideas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            pt "Ya..."

                    elif afternight04__RLeg_Massage_Success == 7:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¡Ya basta de preliminares!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "¿¡No crees?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils down03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Si haces esto mientras tienes tu polla dentro de mi,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "no es algo que me disguste tanto al fin y al cabo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Success == 8:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "No hagas que te lo repita."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 06_a
                                show afternight04_sexbattle_d_pupils front06_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                            p "Mmm..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Success >= 9:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

    ################################################################################################################# LBOOB

                elif afternight04__prehfix_RLeg_Massage == False: # LLeg

                    if afternight04__LLeg_Massage_Success == 1:

                        if afternight04__RLeg_Massage_Done == 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "Con todas las tías que sueles quedar para follar,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "y que te piden que les des duro;"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                                with dissolve

                            d "¿Te pones a toquetearles las piernas?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows surprisex01_a
                                with dissolve

                            d "Te lo pregunto por curiosidad..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "No me extraña que no tengas demasiado éxito con las chicas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "Lo dice el que necesita emborracharlas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows surprisex02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡Eso no es verdad!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            p "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils right03_a
                                show afternight04_sexbattle_d_eyebrows surprisex01_a
                                with dissolve

                            d "No del todo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows serious_a
                                with dissolve

                            d "¿De verdad?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "¿Crees que masajearme la otra pierna va a ser algo distinto?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "Tienes suerte que hace tiempo que nos conocemos..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "Sino te tiraba por la ventana."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils right04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Tsssk..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Success == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Otra vez con la manita en la pierna..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        p "Me negarás que te gusta..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "pff..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        d "Haz lo que quieras..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows surprisex01_a
                            with dissolve

                        p "Es lo que hago."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "..."

                    elif afternight04__LLeg_Massage_Success == 3:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Está claro que te gusta dar masajes..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows surprisex01_a
                            with dissolve

                        p "Y a ti te gusta recibirlo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "..."

                    elif afternight04__LLeg_Massage_Success == 4:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "¿Piensas estar mucho rato con el masajito...?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        p "Puede que sí..."

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Pues puede que yo me cansé y te acabe violando..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Success == 5:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Vale,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Reconozco que el masajito no ha estado mal..."

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Pero tengo otras partes en el cuerpo que les podrías dar mejor uso..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¿Sabes?"

                            if afternight04_Pussy_dick_med_Speed_0_Success == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "¡Como meterme tu jodida polla de una puta vez por todas!"

                            else:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "Como volver a meterme la polla de una jodida vez."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                            p "..."

                    elif afternight04__LLeg_Massage_Success == 6:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Tienes buenas manos,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        d "lo reconozco..."

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Pero solo con eso no vas a conseguir demasiado."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Así que métemela de una jodida vez."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                        else:

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Pero empieza a mover esa jodida polla tuya de una puta vez."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Pero acelera un poco más ese ritmo."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx03_a
                                    with dissolve

                            else:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Pero ni se te ocurra sacar esa polla tuya de ahí..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve


                    elif afternight04__LLeg_Massage_Success == 7:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if afternight04_Pussy_dick_med_Speed_0_Success == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "¡Fóllame de una jodida vez!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "O seré yo quien lo haga por ti."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                            else:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "Como no me la vuelvas a meter pronto,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "al final te voy a violar."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Reconozco que me gusta tener tu polla dentro mientras me masajeas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows sadx01_a
                                with dissolve

                            d "al final resultará que no eres tan mal semental..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Success == 8:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if afternight04_Pussy_dick_med_Speed_0_Success == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                    show afternight04_sexbattle_d_eyes 01_a
                                    show afternight04_sexbattle_d_pupils front01_a
                                    show afternight04_sexbattle_d_eyebrows angryx05_a
                                    with dissolve

                                d "¡Estás empezando a colmar mi paciencia!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                            else:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "¿A qué esperas para metérmela de nuevo?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                show afternight04_sexbattle_d_eyes 06_a
                                show afternight04_sexbattle_d_pupils front06_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                            d "Hmmm..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Que cabrón eres..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx02_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Success >= 9:

                        if (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low"):

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                                show afternight04_sexbattle_d_eyes 07_a
                                show afternight04_sexbattle_d_pupils front07_a
                                show afternight04_sexbattle_d_eyebrows sadx03_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows sadx04_a
                                with dissolve

    #################################################################################################################
    #################################################################################################################

            elif mc_body.roll_success == False: #You Failed.

                if afternight04__prehfix_RLeg_Massage == True: # RLeg

                    if afternight04__RLeg_Massage_Failed == 1:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "En lugar de manosearme la pierna,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Estaría bien que movieras un poco esa {i}\"Anaconda\"{/i} tuya..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Que la tienes ahí muerta de asco."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "En lugar de manosearme la pierna,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "podrías centrarte en lo que estás haciendo con tu polla..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 01_a
                                    show afternight04_sexbattle_d_pupils front01_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                p "¿Acaso no puedo hacer las dos cosas?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "¿A esta velocidad?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Una tortuga sería más salvaje que tú..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils right04_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                pt "Desde luego,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils right05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                                pt "sigue siendo el mismo idiota de siempre..."

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "Por lo menos la estás moviendo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                                pt "Lo dice como si estuviera cumpliendo con una obligación..."

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows surprisex01_a
                                with dissolve

                            d "No es que no desprecie tu \"increíble habilidad para el masaje\"..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            pt "El sarcasmo no es su punto fuerte..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Pero apreciaría si empezaras a hacer realmente lo que te he pedido."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Failed == 2:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "¿Tienes pensado mover esa polla tuya por eso?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                p "..."

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Podrías subir un poco más la velocidad,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                    with dissolve

                                d "en lugar de tocar tanto la piernas de las narices..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                    show afternight04_sexbattle_d_eyes 00_a
                                    show afternight04_sexbattle_d_pupils front00_a
                                    show afternight04_sexbattle_d_eyebrows normal_a
                                    with dissolve

                                p "Tú quieres pasártelo bien,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils right02_a
                                    show afternight04_sexbattle_d_eyebrows serious_a
                                    with dissolve

                                p "¿Verdad?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils right03_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                                d "..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                                    show afternight04_sexbattle_d_eyes 01_a
                                    show afternight04_sexbattle_d_pupils front01_a
                                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                                    with dissolve

                                p "Pues déjame hacerlo a mi manera,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                p "o búscate a otro."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils right05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                                d "..."

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows normal_a
                                    with dissolve

                                d "Si tanto te gusta toquetearme,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "tampoco me voy a quejar,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "siempre y cuando sigas moviendo esa anaconda tuya..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                                p "..."

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "De verdad [protname],"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "si tienes un fetiche con las piernas me parece muy bien,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "pero te he pedido que me folles,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "no que te me pongas cachondo con un delirio tuyo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "A ti te va el sado,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "¿verdad?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "¡¿Cómo?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "¡El sado es eso del dolor y látigos..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "¿Verdad?"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "No creo que me vaya ese rollo [protname]..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows normal_a
                                with dissolve

                            p "¡Pues deja de provocarme o lo comprobarás!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "..."

                    elif afternight04__RLeg_Massage_Failed == 3:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
      
                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "¡Pero mueve un poco tu polla también un poco joder!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Al menos podrías moverte un poco más..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "Veo que sabes hacer las dos cosas a la vez,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Me alegro..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx03_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Joder [protname],"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Deja mis piernas en paz de una vez y haz algo de más provecho narices..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Failed == 4:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Sería de agradecer que movieras esa jodida polla un poco."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Agradecería que movieras esas caderas a un mejor ritmo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "Así no se siente tan mal que me toques..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "Siempre que no disminuyas ese ritmo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx03_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "Me tienes un poco hasta el cojón con tanto masajito en la pierna..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Failed == 5:

                        if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "¡Por lo menos muévela un poco!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "que la tienes ahí muerta de asco."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Si por lo menos esas caderas se movieran un poco más..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "No se siente tan mal si me follas a este ritmo y me masajeas la pierna al mismo tiempo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx03_a
                                    with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "He visto sanguijuelas mucho menos babosas..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Failed == 5:

                        if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):
                            
                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Si al menos te movieras..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Por lo menos sabes moverte un poco mientras me das el masaje..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__RLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "¿Quien lo iba a decir?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "Al final resulta que sabes follar y masajear al mismo tiempo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Y encima no lo haces tan mal..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve
                            
                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Al final te voy a violar..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                    elif afternight04__RLeg_Massage_Failed >= 5:

                        if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):
                            
                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                 if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                        d "..."

                        if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")):
                            
                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                 if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        else:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

    #################################################################################################################

                elif afternight04__prehfix_RLeg_Massage == False: # LLeg

                    if afternight04__LLeg_Massage_Failed == 1:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "¡Pero por lo menos mueve un poco esa polla de las narices!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "No te digo que no me toques la pierna si eso te pone,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "Pero al menos podrías darle mejor uso a esa anaconda tuya;"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Que las he visto más rápidas..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__LLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "Si al menos sabes moverte,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                                d "no me quejaré de que me estés toqueteando..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "¡¿Qué se supone que estás intentando hacer?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "¡¿Ponerme más caliente?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "¡¿Quieres que me vuelva un encendedor?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                show afternight04_sexbattle_d_eyes 00_a
                                show afternight04_sexbattle_d_pupils front00_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "No,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            p "intento hacer que entiendas que eres tú quien me ha pedido el favor"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            p "y por lo tanto hago lo que me sale de las narices;"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            p "sino te gusta,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            p "te buscas a otro."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils right05_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils right01_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Quizás lo haga..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve


                    elif afternight04__LLeg_Massage_Failed == 2:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                    with dissolve

                                d "¿Esa polla la tienes ahí como adorno?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "¿O piensas moverla en algún momento?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Porque vayas un poco más rápido follándome,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                    with dissolve

                                d "en lugar de estar manoseándome la pierna,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "tampoco se acabará el mundo..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 01_a
                                    show afternight04_sexbattle_d_pupils front01_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                p "No te contentas con nada."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sabiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils right05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__LLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 06_a
                                    show afternight04_sexbattle_d_pupils front06_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Mmmm..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                    with dissolve

                                p "Si me muevo bien no te desagrada"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                                    with dissolve


                                p "¿verdad?"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Has tardado,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "pero lo vas pillando..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                                pt "Un gracias tampoco habría estado mal..."


                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Otra vez con la piernecita..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "Mira,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "que te mole toquetearme,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            d "Si eso te ayuda a ponerte cachondo..."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                                with dissolve

                            d "no me parece un mal plan."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                            d "Pero que tu polla siga sin estar dónde deba de estar,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            d "ya me toca un poco más las narices."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Failed == 3:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Sino vas a moverla..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "al final seré yo quien me mueva."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "Me alegra que te guste tocarme la pierna,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows normal_a
                                    with dissolve

                                d "Peros si movieras un poco más esa polla tuya,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "tampoco me quejaría..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__LLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 06_a
                                    show afternight04_sexbattle_d_pupils front06_a
                                    show afternight04_sexbattle_d_eyebrows sadx01_a
                                    with dissolve

                                d "HHMMmm..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                show afternight04_sexbattle_d_eyes 02_a
                                show afternight04_sexbattle_d_pupils front02_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Sino vas a follarme pronto,"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "al final lo haré yo."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Failed == 4:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "Hasta las putas narices estoy ya de que me masajees,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "pero no muevas esa polla tuya."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                                    show afternight04_sexbattle_d_eyes 02_a
                                    show afternight04_sexbattle_d_pupils front02_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "Si me follaras un poco más rápido,"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                    show afternight04_sexbattle_d_eyes 04_a
                                    show afternight04_sexbattle_d_pupils front04_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                                d "tampoco me quejaría..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__LLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 07_a
                                    show afternight04_sexbattle_d_pupils front07_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                                d "MMMmhh..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                                show afternight04_sexbattle_d_eyes 04_a
                                show afternight04_sexbattle_d_pupils front04_a
                                show afternight04_sexbattle_d_eyebrows angryx02_a
                                with dissolve

                            d "Te lo digo en serio."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                            d "O me metes la polla o me la meto yo."

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                    elif afternight04__LLeg_Massage_Failed >= 5:

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                        else: # dick no PUSSY

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx03_a
                                with dissolve

                        d "..."

                        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                            if mc_body.dick_speed == 0:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx01_a
                                    with dissolve

                            elif mc_body.dick_speed == 1:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                            elif mc_body.dick_speed == 2:

                                $ afternight04__LLeg_Massage_Failed -= 1

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows sadx04_a
                                    with dissolve

                        else: # dick no PUSSY

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

            if mc_body.store["left_hand"] == "RLeg_Massage":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["right_hand"] == "LLeg_Massage":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

        if current_pose.id == "pose_2" or current_pose.id == "pose_3":

            if mc_body.store["right_hand"] == "RLeg_Massage":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["left_hand"] == "LLeg_Massage":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

############################################################

    if ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")) and (mc_body.dick_speed > 0):

        $ current_girl.pleasure += 2
        $ current_girl.enslavement += 1

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