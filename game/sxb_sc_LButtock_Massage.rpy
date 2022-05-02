label LButtock_Massage:

######################################################### version_changelog

    if afternight04_SheRapingYou == True:

        pt "Mientras la tenga encima es imposible que le pueda masajear esa nalga..."

        call screen dummy_screen()

    ##

    if current_pose.id == "pose_1":

        if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" 
            or mc_body.store["dick"] == "Pussy_dick_deep" or mc_body.store["dick"] == "Anal_dick_low" 
            or mc_body.store["dick"] == "Analy_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            pt "Si quiero tener mi polla cerca,"

            pt "no puedo meter mis manos en sus nalgas en esta posición."

            call screen dummy_screen()

    ##

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.02") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "LButtock_Massage."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["right_hand"] = "LButtock_Massage"

    else:

        $ mc_body.store["left_hand"] = "LButtock_Massage"

#########################################################
        
    $ afternight04__prehfix_LButtock_Massage = True
    $ afternight04__a_prehfix_LButtock_Massage = True

    if afternight04_SheRapingYou == True:

        $ afternight04__prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Massage = False

        $ mc_body.store["right_hand"] = ""

        show afternight04_sexbattle_mc_handR empty
        with dissolve

        pt "Mientras sea ella la que me cabalga,"

        pt "no puedo masajearle las nalgas en condiciones..."

        call screen dummy_screen()

    call afternight04_sex_check_before

    label .manager:

        $ afternight04__LButtock_Massage_Done += 1

        if mc_body.roll_success:
            $ afternight04__LButtock_Massage_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__LButtock_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_LButtock_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage 
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Left Buttock.")

        call afternight04_LButtock_Massage  
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_LButtock_Massage:

        call afternight04_Buttock_Massage

        return

    label afternight04_LButtock_Massage_his_orgasm:

        call afternight04_Buttock_Massage

        call afternight04_mostly_his_orgasm

        return

    label afternight04_LButtock_Massage_her_orgasm:

        call afternight04_Buttock_Massage

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################