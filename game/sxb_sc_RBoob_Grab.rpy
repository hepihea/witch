label RBoob_Grab:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.07.08") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "RBoob_Grab."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RBoob_Grab"

    else:

        $ mc_body.store["right_hand"] = "RBoob_Grab"

#########################################################

    $ afternight04__prehfix_RBoob_Grab = True
    $ afternight04__a_prehfix_RBoob_Grab = True
        
    call afternight04_sex_check_before

    label .manager:

        $ afternight04__RBoob_Grab_Done += 1

        if mc_body.roll_success:
            
            $ afternight04__RBoob_Grab_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__RBoob_Grab_Failed += 1

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
        $ debug ("First Orgasm for his. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RBoob_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Grabbing her Right Boob.")

        call afternight04_RBoob_Grab
        
        jump expression __prefix + "call_screen"

####################################
###################################

    label afternight04_RBoob_Grab:

        call afternight04_Boob_Grab

        return

    label afternight04_RBoob_Grab_his_orgasm:

        call afternight04_Boob_Grab

        call afternight04_mostly_his_orgasm

        return

    label afternight04_RBoob_Grab_her_orgasm:

        call afternight04_Boob_Grab

        call afternight04_mostly_her_orgasm

        return

##

## GENERAL BOOB GRABBING.

label afternight04_Boob_Grab:

    #################################################################################################################
    #################################################################################################################

    if mc_body.roll_success:

        if (mc_body.store["right_hand"] == "LBoob_Grab") and (mc_body.store["left_hand"] == "RBoob_Grab"):

            $ afternight04__Boob_Grab_Both_Success += 1

    else:

        if not "pass" in mc_body.result:

            if (mc_body.store["right_hand"] == "LBoob_Grab") and (mc_body.store["left_hand"] == "RBoob_Grab"):

                $ afternight04__Boob_Grab_Both_Failed += 1

    #################################################################################################################
    #################################################################################################################

######

    ## progcheck "total.girl_try: [(afternight04__RBoob_Grab_Success or afternight04__LBoob_Grab_Success + afternight04__RBoob_Grab_Failed) or (afternight04__LBoob_Grab_Success + afternight04__LBoob_Grab_Failed)],
    #total.girl_success: [current_girl.total_success],
    #total.girl_fail: [afternight04__RBoob_Grab_Failed or afternight04__LBoob_Grab_Failed]"

    ########if current_pose.id == "pose_1": #If pose is 01.
    ####$ current_pose.id = current_girl.switch_pose("pose_1")
    
    if current_pose.id == "pose_1":

        if afternight04__prehfix_RBoob_Grab == True:

            $ mc_body.store["left_hand"] == "RBoob_Grab"
            show afternight04_sexbattle_mc_handL grab_boobR_action_a
            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
            with dissolve

        elif afternight04__prehfix_LBoob_Grab == True:

            $ mc_body.store["right_hand"] == "LBoob_Grab"
            show afternight04_sexbattle_mc_handR grab_boobL_action_a

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            with dissolve

    elif current_pose.id == "pose_2":

        #if afternight04__prehfix_RBoob_Grab == True: # NOT NECESSARY

        if afternight04__prehfix_LBoob_Grab == True:

            $ mc_body.store["left_hand"] == "LBoob_Grab"
            show afternight04_sexbattle_mc_handL grab_boobL_action_b

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            with dissolve

    elif current_pose.id == "pose_3":

        if afternight04__prehfix_RBoob_Grab == True:

            $ mc_body.store["right_hand"] == "RBoob_Grab"
            show afternight04_sexbattle_mc_handR grab_boobR_c_action
            
            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness

            with dissolve

        #elif afternight04__prehfix_LBoob_Grab == True: # NOT NECESSARY

##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_LArm_Grab = False
        #$ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RArm_Grab = False
        #$ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
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

######################
##################### 

    #HER REACTION:
############################################################
###########################################################

    if mc_body.roll_success == True:

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Uhm..."

        elif randomnum_1to10 == 2:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Hm..."

        elif randomnum_1to10 == 3:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Ughm..."

        elif randomnum_1to10 == 4:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Mm..."

        elif randomnum_1to10 == 5:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "mmMmf..."

        elif randomnum_1to10 == 6:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Ahm..."

        elif randomnum_1to10 == 7:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Mmh..."

        elif randomnum_1to10 == 8:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Ughm..."

        elif randomnum_1to10 == 9:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Mhfm..."

        elif randomnum_1to10 == 10:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Hum..."


    else:

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Tssk..."

        elif randomnum_1to10 == 2:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Pff..."

        elif randomnum_1to10 == 3:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Ugh..."

        elif randomnum_1to10 == 4:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "..."

        elif randomnum_1to10 == 5:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Jesús..."

        elif randomnum_1to10 == 6:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Madre mía..."

        elif randomnum_1to10 == 7:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "De verdad..."

        elif randomnum_1to10 == 8:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Joder..."

        elif randomnum_1to10 == 9:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Aishh..."

        elif randomnum_1to10 == 10:

            if current_pose.id == "pose_1":

                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Ahh..."

############################################################

        if mc_body.store["left_hand"] == "RBoob_Grab":

            #$ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty

            with hpunch

        if mc_body.store["right_hand"] == "LBoob_Grab":

            #$ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

            with hpunch

############################################################
###########################################################
    
    $ debug("Test Text")

    # progcheck "RBoob_Grab_Success = [afternight04__RBoob_Grab_Success], 
    #         \nRBoob_Grab_Failed = [afternight04__RBoob_Grab_Failed], 
    #         \nLBoob_Grab_Success = [afternight04__LBoob_Grab_Success], 
    #         \nLBoob_Grab_Failed = [afternight04__LBoob_Grab_Failed]."

    #HER REACTION:

    #if current_girl.total_try == 1:

    if (mc_body.store["right_hand"] == "LBoob_Grab") and (mc_body.store["left_hand"] == "RBoob_Grab"):

        if mc_body.roll_success == True: #You succeded.

            if afternight04__Boob_Grab_Both_Success == 1:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "¿Ahora la otra?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Te crees que mis domingas son el {i}joystick{/i} de un videojuego?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿O qué?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."


            elif afternight04__Boob_Grab_Both_Success == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿Acaso no tenías suficiente con uno?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Que me tocas las narices con el otro!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Success == 3:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Te mola tener ambas manos ocupadas en mis {i}domingas{/i}?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "Quizás no tanto como a ti,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "juzgando por el gemido que has hecho..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Tssk..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Success == 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡¿Me tienes que estar magreando ambas tetas?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡¿Te crees que soy tu juguete sexual?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "¿Nunca has masajeado los pechos a ninguna chica con la que has estado para ponerla a tono?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "[protname];"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Ya voy cachonda."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Lo que quiero es que me folles!"

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¡¿Y qué diablos crees que estoy haciendo?!"

                    if mc_body.dick_speed == 0:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡Pero si la tienes ahí muerta de asco!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Muévela un poco!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        pt "La madre que lo parió..."

                    elif mc_body.dick_speed == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils down02_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Podrías moverte un poco más rápido..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        p "Sino te quejas,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "no estás contento..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Tssk..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                    elif mc_body.dick_speed >= 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows surprisex01_a
                            with dissolve

                        p "¿Qué?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Nada..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows surprisex01_a
                            with dissolve

                        p "Pues estate calladito."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "Pesado."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Tsskk..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                else: # No Fucking

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

            elif afternight04__Boob_Grab_Both_Success == 5:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "Veo que ya no te quejas tanto,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows surprisex02_a
                    with dissolve

                p "parece que te empieza a gustar esto de que te masajee ambos pechos,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "más de lo que eres capaz de confesar..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "No..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "No es lo que parece..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Success == 6:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                pt "Sin duda parece que ya no le incomoda tanto que juegue con ambos a la vez,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve


                pt "Pero tampoco le causa el mismo efecto"

                pt "Y si se cansa,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                pt "es posible que vuelva a tomarla iniciativa..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Success >= 7:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "..."

#################################################################################################################

        if mc_body.roll_success == False: #You Failed.

            if afternight04__Boob_Grab_Both_Failed == 1:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿No tienes suficiente con uno que tienes que hacérmelo con las dos jodidas tetas?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "Ya basta de esta mariconada,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿No crees?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "..."

            elif afternight04__Boob_Grab_Both_Failed == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "¡¿Otra vez con las dos manos?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Podrías usar mejor tus manos en otras cosas..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Failed == 3:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "De verdad que eres cansino..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No te lo volveré a repetir."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "A la próxima voy a empezar a moverme encima de ti."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__Boob_Grab_Both_Failed >= 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

#################################################################################################################
#################################################################################################################

    else: #Not Both Hands.

        $ debug ("You´re using one hand.")

        if mc_body.roll_success == True: #You succeded.

            if afternight04__prehfix_RBoob_Grab == True:

                if afternight04__RBoob_Grab_Success == 1:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿Por qué demonios me agarras la teta?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¿Nunca has masajeado los pechos de una mujer?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Te parezco un ligue de noche?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                elif afternight04__RBoob_Grab_Success == 2:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Dirás lo que quieras..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Pero no parece que te disguste tanto como quieres aparentar..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "pff..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils left04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    d "Que te jodan..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                elif afternight04__RBoob_Grab_Success == 3:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¿Ya no te molesta?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Tampoco he dicho que me encante..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Ya..."

                elif afternight04__RBoob_Grab_Success == 4:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "¡¿No ves que la teta no es precisamente mi lugar favorito!?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Si realmente te disgustara lo que te estoy haciendo,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "hace rato que me hubieras sacado la mano."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows agnryx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Gilipollas..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                elif afternight04__RBoob_Grab_Success == 5:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "¡¿De verdad no se te ocurre ninguna otra cosa que hacer?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Quizás..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Pero eres tú quien me ha pedido el favor,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "así que disfruta y calla."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                elif afternight04__RBoob_Grab_Success == 6:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¿Ya no dices nada...?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Vete a la mierda."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                elif afternight04__RBoob_Grab_Success == 7:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Parece que ya no le molesta del todo,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    pt "pero tampoco le hace el mismo efecto que antes..."

                    pt "Sería bueno probar otras cosas."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve


                elif afternight04__RBoob_Grab_Success >= 8:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

################################################################################################################# LBOOB

            elif afternight04__prehfix_RBoob_Grab == False: # LBoob

                if afternight04__LBoob_Grab_Success == 1:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿Qué coño haces con la teta?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Masajearte..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿Y se supone que esa es tu respuesta?!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Sino te gusta,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    p "ya sabes dónde está la puerta."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "{size=12}Mariconazo...{/size}"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¿Qué?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Nada..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                elif afternight04__LBoob_Grab_Success == 2:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    d "De verdad..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿Qué clase de retorcida satisfacción te da remover un pectoral con exceso de grasa?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    pt "Que forma más jodidamente anti-erótica de definir el pecho femenino..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¿A qué demonios ha venido ese gemido de placer entonces?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Te lo habrás imaginado..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    pt "Ya..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                elif afternight04__LBoob_Grab_Success == 3:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Me da la sensación que te quejas por vicio..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Me quejo porque te he pedido que me folles,"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "no que me hagas mariconadas con mis pechos."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "Estás disfrutándolo,"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "y lo sabes."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Idiota..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                elif afternight04__LBoob_Grab_Success == 4:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "¡¿Eres consciente de que mi pecho no es la parte que más me pone?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Sí."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Pero también te he oído gemir,"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    p "así que tanto no te debe de disgustar."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Deja de quejarte narices..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "¡que pareces mi abuela!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "¡¿Le hacías esto a tu abuela?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "¡¿Qué?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happy_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "¡NO!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happy_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Joder!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Ya sabes que no tengo abuela."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¡Ni aunque la tuviera se lo haría!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happy_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happy_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "En esta ocasión el muy cabrón ha sabido jugar a mi juego..."

                elif afternight04__LBoob_Grab_Success == 5:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Eres pesadito con la teta..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Disfruta y calla."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve


                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Bah..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "si terminas haciendo lo que te da la gana..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Exacto."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Subnormal..."

                elif afternight04__LBoob_Grab_Success == 6:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Que no te estés quejando es una buena señal..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve


                elif afternight04__LBoob_Grab_Success == 7:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    pt "No se queja tanto,"

                    pt "pero no parece que esté disfrutando igual que antes..."

                    pt "Quizás sería bueno probar algo distinto."

                elif afternight04__LBoob_Grab_Success >= 8:

                     d"..."

#################################################################################################################
#################################################################################################################

        elif mc_body.roll_success == False: #You Failed.

            if afternight04__prehfix_RBoob_Grab == True: # RBoob

                if afternight04__RBoob_Grab_Failed == 1:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Puedes ser más mariposón?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿Te magreao yo tus domingas?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Yo aún tengo pectorales,"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "pero si quieres,"

                    extend " puedes tocármelos."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "¡En los años que hace que nos conocemos!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Cuando nos hemos magreado los pectorales?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡Exacto!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Nunca!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Deja en paz mis pechos!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04__RBoob_Grab_Failed == 2:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Esto es lo que sueles hacer con las tías?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Jugar con sus pechos como si fueran pelotas anti-estrés?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04__RBoob_Grab_Failed == 3:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Vaya mierda de amante estás hecho"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "si esta es tu mejor forma de calentar..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04__RBoob_Grab_Failed == 4:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Me estás empezando a tocar las narices y mi paciencia se está agotando..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "No te lo voy a repetir."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                elif afternight04__RBoob_Grab_Failed >= 5:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx09_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

#################################################################################################################

            elif afternight04__prehfix_RBoob_Grab == False: # LBoob

                if afternight04__LBoob_Grab_Failed == 1:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve
                    
                    d "¡Esto es una jodida mariconada!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡¿Pero tú te escuchas?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Cómo te sentirías si te masajeara a ti los pectorales?!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Nadie te detiene..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils left02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Ese no es el caso..."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils left04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                elif afternight04__LBoob_Grab_Failed == 2:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Con mis pechos mariconadas no!"

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04__LBoob_Grab_Failed == 3:
    
                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Te masajeo yo los pectorales?!"
    
                    if current_pose.id == "pose_1":
        
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve    

                    d "¡¿Verdad que no?!"
    
                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve    

                    d "¡Pues deja los míos en paz!"

                elif afternight04__LBoob_Grab_Failed == 4:
    
                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Como vuelvas a tocarme el jodido pecho,"
    
                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve    

                    d "Voy a tomar la jodida iniciativa."

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve    

                elif afternight04__LBoob_Grab_Failed >= 5:

                    if current_pose.id == "pose_1":
                        
                        show afternight04_sexbattle_d_mouth sad_Silentx09_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

            p "..."

#################################################################################################################
#################################################################################################################


############################################################
    if mc_body.roll_success == False:

        if current_pose.id == "pose_1":

            if mc_body.store["left_hand"] == "RBoob_Grab":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["right_hand"] == "LBoob_Grab":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

        if current_pose.id == "pose_2" or current_pose.id == "pose_3":

            if mc_body.store["right_hand"] == "RBoob_Grab":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["left_hand"] == "LBoob_Grab":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch



############################################################

    ###########################
    ##########################

    if not ((mc_body.store["dick"] == "low") or (mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")) and (mc_body.dick_speed == 0):

        call afternight04_RapeOrNot 

    ###########################
    ##########################

    return

