label LNipple_Pinch:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.03") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "LNipple_Pinch."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["right_hand"] = "LNipple_Pinch"

    else:

        $ mc_body.store["left_hand"] = "LNipple_Pinch"

#########################################################
    
    $ afternight04__prehfix_LNipple_Pinch = True
    $ afternight04__a_prehfix_LNipple_Pinch = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__LNipple_Pinch_Done += 1

        if mc_body.roll_success:
            $ afternight04__LNipple_Pinch_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__LNipple_Pinch_Failed += 1

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
        $ debug ("First Orgasm for his. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_LNipple_Pinch_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Pinching her Left Nipple with your Right Hand.")

        call afternight04_LNipple_Pinch
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_LNipple_Pinch:

        call afternight04_Nipple_Pinch_general

        return

    label afternight04_LNipple_Pinch_his_orgasm:

        call afternight04_Nipple_Pinch_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04_LNipple_Pinch_her_orgasm:

        call afternight04_Nipple_Pinch_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################