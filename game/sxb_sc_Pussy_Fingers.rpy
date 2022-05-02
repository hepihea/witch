label Pussy_Fingers:

######################################################### Dummy_Screen Calls

    if afternight04_condom_broken == True:

        #$ mc_body.store["right_hand"] = ""

        jump afternight04_condom_broken_scene

######################################################### 

    if (mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

        #$ afternight04__prehfix_Pussy_Fingers = False
        #$ afternight04__a_prehfix_Pussy_Fingers = False

        #$ mc_body.store["right_hand"] = ""

        pt "Tiene el coño tan apretado,"

        pt "que los dedos no me caben ahí dentro..."

        call screen dummy_screen()

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.09") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "Pussy_Fingers."

#########################################################

    $ mc_body.store["right_hand"] = "Pussy_Fingers"

#########################################################

    $ afternight04__prehfix_Pussy_Fingers = True
    $ afternight04__a_prehfix_Pussy_Fingers = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__Pussy_Fingers_Done += 1

        if mc_body.roll_success:
            $ afternight04__Pussy_Fingers_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__Pussy_Fingers_Failed += 1

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
        $ debug ("First Orgasm for his. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_Pussy_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Penetrating her Pussy with two fingers of your Right Hand.")

        call afternight04_Pussy_Fingers
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_Pussy_Fingers:

        call afternight04_Pussy_Fingers_general

        return

    label afternight04_Pussy_Fingers_his_orgasm:

        call afternight04_Pussy_Fingers_general

        jump afternight04_mostly_his_orgasm

    label afternight04_Pussy_Fingers_her_orgasm:

        call afternight04_Pussy_Fingers_general

        jump afternight04_mostly_her_orgasm

####################################
###################################
####################################
###################################
####################################
###################################


label afternight04_Pussy_Fingers_general:

##############################################################
#############################################################


    if mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep":
        
        $ mc_body.store["dick"] = "Pussy_dick_out"

    if mc_body.store["tongue"] == "Pussy_Tongue": 

        $ mc_body.store["tongue"] = ""

    $ mc_body.store["right_hand"] == "Pussy_Fingers"

    if current_pose.id == "pose_1": ## POSE 01

        show afternight04_sexbattle_mc_handR empty
        #show afternight04_sexbattle_mc_anal_pussy empty

        # penetrate_pussy empty - penetrate_pussy empty
        call afternight04_sexbattle_pubic_emptiness
        
            ##
        #call afternight04_sexbattle_mc_handR_penetrate_pussy_action_a
        $ debug ("Here goes F PUSSY Starting A") #Not finished.
        call afternight04_sexbattle_mc_handR_penetrate_pussy_starting_a

        with dissolve

    else:  ## POSE 02 and 03

        show afternight04_sexbattle_d_legs_over_pussy 005_wet_00_b
        
        show afternight04_sexbattle_mc_handR empty
        show afternight04_sexbattle_mc_handR_penetrate_anal empty
        
        show afternight04_sexbattle_mc_tongue_pussy empty
        show afternight04_sexbattle_mc_dick_pussy empty

        call afternight04_sexbattle_pubic_emptiness ## CALL

        #show afternight04_sexbattle_mc_handR_penetrate_pussy action_b

        $ debug ("Here goes F PUSSY Starting B") #Not finished.
        call afternight04_sexbattle_mc_handR_penetrate_pussy_starting_b ## CALL

        with dissolve


##############################################################
#############################################################
    
    # Previous RHand Action
    
    #$ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    $ afternight04__a_prehfix_MClitoris_Massage = False

    $ afternight04__a_prehfix_RArm_Grab = False
    $ afternight04__a_prehfix_RBoob_Grab = False
    $ afternight04__a_prehfix_RBoob_Slap = False
    $ afternight04__a_prehfix_RButtock_Massage = False
    $ afternight04__a_prehfix_RButtock_Slap = False
    #$ afternight04__a_prehfix_Remove = False
    $ afternight04__a_prehfix_RLeg_Massage = False
    $ afternight04__a_prehfix_RNipple_Pinch = False


##############################################################
#############################################################

##############################################################
#############################################################

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils down04_a
        with dissolve


    d "..."

    if mc_body.roll_success == False: # You failed.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "Humm..."

        elif randomnum_1to5 == 2:

            d "Tss..."

        elif randomnum_1to5 == 3:

            d "Hmm..."

        elif randomnum_1to5 == 4:

            d "Hmpfh..."

        elif randomnum_1to5 == 5:

            d "Tsk..."

##############################################################

        $ mc_body.store["right_hand"] = ""

        if current_pose.id == "pose_1": ## POSE 01 


            show afternight04_sexbattle_d_legs_top_pussy empty
            show afternight04_sexbattle_d_legs_over_pussy empty
            #show afternight04_sexbattle_mc_tongue_pussy empty

            # penetrate_pussy empty - penetrate_pussy empty
            call afternight04_sexbattle_pubic_emptiness

            ###show afternight04_sexbattle_mc_handR_penetrate_anal empty
            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            show afternight04_sexbattle_mc_handR empty # Necessary?
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a
            with hpunch

        else:  ## POSE 02 and 03

            # penetrate_pussy empty - penetrate_pussy empty

            call afternight04_sexbattle_pubic_emptiness

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            show afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b

            with hpunch

##############################################################
#############################################################

## TRIES

    if (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) == 0:

        aj "This text should not appear. 5132"


    #if current_girl.total_try == 1:
    if (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) == 1:

        if mc_body.roll_success == True: #You succeded.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "¿Qué haces [protname]?"

            if afternight04__MClitoris_Massage_Success > 0 and afternight04__MClitoris_Tongue_Success > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Después de ver cómo has disfrutado con el clítoris tan sensible que tienes,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "como calentamiento,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a_a
                    with dissolve

                p "he pensado que quizás te gustaría probar mis dedos dentro de ti."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Estoy preparando un poco el terreno,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "Como calentamiento..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿Pero de qué {i}calentamiento{/i} hablas?!"

            if afternight04_Pussy_dick_med_Speed_0_Done > 0 or afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Si ya me la has metido dentro!"

                if afternight04_Pussy_dick_med_Speed_0_Done < 0 and afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "En realidad has estado tú quien se la ha metido dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Lo que quiero es que me metas la polla."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡No tus dedos!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Llevo todo el puto día metiéndome consoladores,"

            extend " vibradores"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "y otras cosas en general!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Probaste con tus dedos?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡CLARO QUE PROVÉ CON MIS DEDOS!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "Parece que no será tan fácil como pensaba,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "el coño lo tiene bastante chamuscado..."


    elif (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) == 2:

        #if current_girl.roll_success == False: #Wrong
        if mc_body.roll_success == False: #You didn´t succeded.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Hay que joderse..."

            if afternight04__Pussy_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Deja de meterme los dedos,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Y méteme la polla!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04__Pussy_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡No me ignores!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Si quieres penetrarme,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "házmelo como es debido!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


    elif (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) == 3:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Pussy_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Sigues con lo mismo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Hasta ahora no te me has quejado."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Joder!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Porque claro que me gusta!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils right01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Entonces?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Voy muy cachonda [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Necesito algo más."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Fingers_Failed >= 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Vamos a ver [protname];"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "claro que me gusta que me folles,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Pero no con tus dedos!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04__Pussy_Fingers_Failed >= 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "En serio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿No se te ocurre hacer otra cosa?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Intento variar..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx006_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Pues no varíes tanto!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Que mierda de amante tiene que ser este tío..."


    elif (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) == 4:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Pussy_Fingers_Failed == 1:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Vas a estar mucho rato haciendo lo mismo?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Por mucho que me guste,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "con tus dedos no harás nada que no haya probado el resto del día..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Parece que esta vez no le ha gustado tanto como las anteriores veces..."

            elif afternight04__Pussy_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Sigues con los dedos?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "No parece que te haya disgustado demasiado hasta el momento."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "Sino me haces algo tú pronto,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "lo haré yo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Quizás sería bueno intentar algo distinto antes de volver a intentarlo."

            elif afternight04__Pussy_Fingers_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Sigues otra vez con los dedos?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Al final te harás daño con ellos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Fingers_Failed >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a_a
                    with dissolve

                d "De verdad,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "ya cansas;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "en serio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¡¿Es que se ha cargado toda la sensibilidad del coño!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¡¿Qué mierda de vibradores ha usado?!"

                pt "¿Por qué se supone que con la polla va a ser distinto?"


    elif (afternight04__Pussy_Fingers_Success + afternight04__Pussy_Fingers_Failed) >= 5:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Pussy_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es que me disguste sentirme penetrada por ti,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Pero con otra parte de tu cuerpo, quizás lo apreciaría mejor..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Hasta ahora no te me has quejado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No he dicho que me disguste."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "¿Entonces?"

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Quiero que seas tú el que me viole."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Quiero que me folles [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es por quejarme,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Pero cuando tienes pensando follarme de verdad?"

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "¡Pero si ya me has violado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pues espera que no lo vuelva a hacer!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                elif afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve
                    
                    p "¡Pero si ya te la he metido dentro!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pues vuelve a ello y deja los jodidos dedos!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    p "Cuando me de la gana."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "La paciencia tiene un límite [protname]."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Todo tiene límite,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "excepto tu perrería."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tsk..."

            elif afternight04__Pussy_Fingers_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿A ti te gustaría que me pasara todo el día masturbándote?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "No he visto que me la toques en ningún momento."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "No necesito cogértela con la mano para hacerte correr..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Fingers_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "En serio [protname], varía un poco..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Fingers_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Al final me va a violar..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04__Pussy_Fingers_Failed == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Será mejor probar otra cosa..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04__Pussy_Fingers_Failed >= 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Debería cambiar de táctica..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


################
################
################ # YOUR SUCCESS

    if mc_body.roll_success == True: #You succeded.

        if current_pose.id == "pose_1": ## POSE 01

            show afternight04_sexbattle_mc_handR empty
            #show afternight04_sexbattle_mc_anal_pussy empty

            # penetrate_pussy empty - penetrate_pussy empty
            call afternight04_sexbattle_pubic_emptiness
            
                ##
            #show afternight04_sexbattle_mc_handR_penetrate_pussy action_a
            call afternight04_sexbattle_mc_handR_penetrate_pussy_action_a

            with dissolve

        else:  ## POSE 02 and 03

            show afternight04_sexbattle_d_legs_over_pussy 005_wet_00_b
            
            show afternight04_sexbattle_mc_handR empty
            show afternight04_sexbattle_mc_handR_penetrate_anal empty
            
            show afternight04_sexbattle_mc_tongue_pussy empty
            show afternight04_sexbattle_mc_dick_pussy empty

            call afternight04_sexbattle_pubic_emptiness ## CALL

            #show afternight04_sexbattle_mc_handR_penetrate_pussy action_b
            call afternight04_sexbattle_mc_handR_penetrate_pussy_action_b ## CALL

            with dissolve

###############

    if mc_body.roll_success == True: #You succeded.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows sadx03_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡MMMhhhm...!"

        elif randomnum_1to5 == 2:

            d "¡AAAHHhmmm...!"

        elif randomnum_1to5 == 3:

            d "¡MMMffhmm...!"

        elif randomnum_1to5 == 4:

            d "¡HUMMffhm...!"

        elif randomnum_1to5 == 5:

            d "¡AAHHMfmm...!"

        #HIS SUCCESS:

    if mc_body.roll_success:
        #$ __suffix.append("his_roll")

        #if current_girl.roll_success == False: #?
            #If you success and she fails:

        #if current_girl.repeat == "once":
        if afternight04__Pussy_Fingers_Success == 1:
        #if current.girl.repeat == 1:

            #"He passed, she failed. First SUCESS.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Con ese gemido,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "no hace falta que te pregunte si quieres continuar."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Gilipollas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__Pussy_Fingers_Success == 2:
        #elif current.girl.repeat == 2:

            #"He passed, she failed. Second SUCCESS.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Es curioso que mis dedos consigan ponerte más caliente que cuando tú te tocas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "¿Será que te resulta extraño por tener este cuerpo nuevo?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "¿O quizás será que te falta experiencia en masturbar coños?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Lo que tienes es envidia de la mía!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__Pussy_Fingers_Success == 3:
        #elif current.girl.repeat == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "¿Te das cuenta que te entran mis dedos hasta el fondo?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Estás realmente cachonda..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Ahora te das cuenta?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "No,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "pero me gusta que seas consciente de lo perra que eres."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04__Pussy_Fingers_Success == 4:
        #elif current.girl.repeat == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Al final vas a preferir mis dedos a mi polla aquí dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Tus dedos no son tan gordos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "¿Quieres que te meta el puño?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talking05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Ni de broma!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            pt "No sé yo si habría mucha diferencia..."

        elif afternight04__Pussy_Fingers_Success == 5:
        #elif current.girl.repeat == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Pensaba que habías dicho que esto no te gustaría nada..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Solo digo que me gustaría más que metieras tu polla..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Todo a su debido tiempo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

        elif afternight04__Pussy_Fingers_Success == 6:
        #elif current.girl.repeat == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Como lo disfrutas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "¿Verdad Perra?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Estás sobre un hielo muy delgado [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            p "Pero te encanta."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Hhhmm..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Gilipollas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__Pussy_Fingers_Success == 7:

            pt "Aunque ya no le disgusta,"

            pt "quizás sería hora de probar otras alternativas..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "..."



    
    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return