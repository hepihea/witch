label Anal_dick_low:

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### Dummy_Screen Calls

    if afternight04_condom_broken == True:

        $ mc_body.store["dick"] = "Anal_dick_med"

        jump afternight04_condom_broken_scene

    ##

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.90.00") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "Anal_dick_low."

#########################################################

    $ mc_body.store["dick"] = "Anal_dick_low"

#########################################################

    $ afternight04__prehfix_Anal_dick_low = True
    $ afternight04__a_prehfix_Anal_dick_low = True

    call afternight04_sex_check_before
    
    label .manager:

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
        $ debug ("First Orgasm for his. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_Anal_dick_low_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Fucking the tip of her Anal.")

        call afternight04_Anal_dick_low
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_Anal_dick_low:

        call afternight04_Anal_dick_general_image
        call afternight04_Anal_dick_general_dialogue
        #call afternight04_Anal_dick_general_label # not work anymore.

        return

    label afternight04_Anal_dick_low_his_orgasm:

        call afternight04_Anal_dick_general_image
        call afternight04_Anal_dick_general_dialogue

        call afternight04_mostly_his_orgasm

        return

    label afternight04_Anal_dick_low_her_orgasm:

        call afternight04_Anal_dick_general_image
        call afternight04_Anal_dick_general_dialogue

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################
