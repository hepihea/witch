label Anal_Fingers:

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### Dummy_Screen Calls

    if afternight04_condom_broken == True:

        $ mc_body.store["right_hand"] = ""

        jump afternight04_condom_broken_scene

    ##

    if current_pose.id == "pose_1": ## POSE 01

        if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            pt "En esta posición,"

            pt "no logro llegar con mis dedos hasta su ano."

            call screen dummy_screen()

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.09.04") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "Anal_Fingers."

#########################################################

    $ mc_body.store["right_hand"] = "Anal_Fingers"

#########################################################

    $ afternight04__prehfix_Anal_Fingers= True
    $ afternight04__a_prehfix_Anal_Fingers= True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__Anal_Fingers_Done += 1

        if mc_body.roll_success:
            $ afternight04__Anal_Fingers_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__Anal_Fingers_Failed += 1

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
        $ debug ("First Orgasm for his. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_Anal_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Penetrating her Anal with two fingers of your Right Hand.")

        call afternight04_Anal_Fingers
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_Anal_Fingers:

        call afternight04_Anal_Fingers_general

        return

    label afternight04_Anal_Fingers_his_orgasm:

        call afternight04_Anal_Fingers_general

        jump afternight04_mostly_his_orgasm

    label afternight04_Anal_Fingers_her_orgasm:

        call afternight04_Anal_Fingers_general

        jump afternight04_mostly_her_orgasm

####################################
###################################
####################################
###################################
####################################
###################################


label afternight04_Anal_Fingers_general:

##############################################################
#############################################################

    if mc_body.store["dick"] == "Anal_dick_out" or mc_body.store["dick"] == "Anal_dick_low" or mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep":
        $ mc_body.store["dick"] = "Anal_dick_out"

    if current_pose.id == "pose_1":

        if mc_body.store["tongue"] == "Anal_Tongue":

            $ mc_body.store["tongue"] = ""

    $ mc_body.store["right_hand"] == "Anal_Fingers"

    ##

    if current_pose.id == "pose_1": ## POSE 01 

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        show afternight04_sexbattle_mc_handR empty
        #show afternight04_sexbattle_mc_dick_pussy empty

        $ debug ("FUCKING HELL!!")

        #show afternight04_sexbattle_mc_handR_penetrate_anal action_a

        $ debug ("Here goes F ANAL Starting A") #Not finished.
        call afternight04_sexbattle_mc_handR_penetrate_anal_starting_a

        with dissolve


    else:  ## POSE 02 and 03

        #show afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b
        #show afternight04_sexbattle_mc_tongue_pussy empty
        #show afternight04_sexbattle_mc_dick_pussy empty
        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        ###show afternight04_sexbattle_mc_handR_penetrate_anal action_b
        # penetrate_pussy empty - penetrate_anal empty
        
        show afternight04_sexbattle_d_legs_anal 005_wet_00_b
        show afternight04_sexbattle_d_legs_anal_over 005_wet_00_b
        show afternight04_sexbattle_mc_tongue_anal empty
        show afternight04_sexbattle_mc_dick_anal empty

        show afternight04_sexbattle_mc_handR empty

        call afternight04_sexbattle_pubic_emptiness ## CALL

        $ debug ("Here goes F ANAL Starting B") #Not finished.
        call afternight04_sexbattle_mc_handR_penetrate_anal_starting_b ## CALL

        with dissolve

##############################################################
#############################################################

    # Previous RHand Action

    $ afternight04__a_prehfix_Pussy_Fingers = False
    #$ afternight04__a_prehfix_Anal_Fingers = False

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

    if mc_body.roll_success == False: # You Failed

        if (afternight04__Anal_Fingers_Success + afternight04__Anal_Fingers_Failed) == 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            if randomnum_1to5 == 1:

                d "¡¿Qué coño?!"

            elif randomnum_1to5 == 2:

                d "¡¿Euh?!"

            elif randomnum_1to5 == 3:

                d "¡¿Pero qué cojones?!"

            elif randomnum_1to5 == 4:

                d "¡La madre que te parió!"

            elif randomnum_1to5 == 5:

                d "¡¿What the fuck?!"

        else: # You failed more than once.

            $ randomnum_1to10 = renpy.random.randint(1, 10)

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            if randomnum_1to10 == 1:

                d "¡¿Otra vez?!"

            elif randomnum_1to10 == 2:

                d "¡Que quites el dedo de ahí!"

            elif randomnum_1to10 == 3:

                d "¡¿Te crees que soy gay?!"

            elif randomnum_1to10 == 4:

                d "¡Deja mi puto agujero anal en paz!"

            elif randomnum_1to10 == 5:

                d "¡No me toques el puto culo!"

            elif randomnum_1to10 == 6:

                d "¡¿Otra vez con el puto agujero anal?!"

            elif randomnum_1to10 == 7:

                d "¡Deja el puto asterisco en paz!"

            elif randomnum_1to10 == 8:

                d "¡¿Pero qué coño buscas ahí dentro?!"

            elif randomnum_1to10 == 9:

                d "¡Deja mi puto ojete!"

            elif randomnum_1to10 == 10:

                d "¡Al final me cagaré encima de tu mano!"


##############################################################

        $ mc_body.store["right_hand"] = ""

        if current_pose.id == "pose_1": ## POSE 01 

            show afternight04_sexbattle_d_legs_over_anal empty
            show afternight04_sexbattle_d_legs_top_anal empty
            show afternight04_sexbattle_d_legs_anal 01_wet_00_a

            call afternight04_sexbattle_pubic_emptiness

            with hpunch

        else:  ## POSE 02 and 03

            show afternight04_sexbattle_mc_handR_penetrate_anal empty
            show afternight04_sexbattle_d_legs_over_pussy 002_wet_00_b

            show afternight04_sexbattle_d_legs_anal 003_wet_00_b
            show afternight04_sexbattle_d_legs_anal_over empty

            with hpunch

##############################################################
#############################################################

## TRIES

    if (afternight04__Anal_Fingers_Success + afternight04__Anal_Fingers_Failed) == 0:

        aj "This text should not appear. 5132"


    if (afternight04__Anal_Fingers_Success + afternight04__Anal_Fingers_Failed) == 1:

        if mc_body.roll_success == True: #You succeded.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿QUÉ COJONES HACES [protname]?!"

            if afternight04_Anal_dick_med_Speed_1_Done >= 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Viendo lo que has disfrutado mi polla en tu culo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "he pensado que quizás te gustaría probar con mis dedos,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "al fin y al cabo mi polla es más gruesa..."

            elif afternight04__MClitoris_Massage_Success > 0 and afternight04__MClitoris_Tongue_Success > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Después de ver cómo has disfrutado con el clítoris,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "he pensado que quizás te gustaría probar mis dedos aquí dentro."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Estoy preparando un poco el terreno,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "Como calentamiento..."

            if afternight04_Anal_dick_med_Speed_1_Done == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Por el puto trasero?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Es que te has bebido el puto entendimiento?!"

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿No has tenido suficiente con meterme tu puta anaconda ahí?!"

                if afternight04__Anal_dick_med_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Y no!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡No me ha gustado una puta mierda!"

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "Tampoco parece que te hubiera disgustado tanto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "Gilipollas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿Tan difícil es que me folles como una persona normal?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "Ahora resulta que eres una persona normal..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx09_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "El agujero por dónde tienes que meter tu \"POLLA\","

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "no tus dedos,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "está más arriba [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Como me toques mucho más las narices,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡te juro que voy a coger a {i}\"Michael\"{/i} y te lo voy a meter hasta que te salga por la boca!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "¿{i}Michael{/i}?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "Si quieres ya me has entendido..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "¿Le has puesto nombre a los consoladores?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡Déjame en paz y fóllame de una vez!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "..."


    elif (afternight04__Anal_Fingers_Success + afternight04__Anal_Fingers_Failed) == 2:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Anal_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Por qué coño sigues metiéndome el dedo por el culo?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "En realidad te estoy metiendo dos dedos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡No me toques las narices [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif afternight04__Anal_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Al final te voy a meter un sopapo que van a tener que cambiarte la dentadura entera."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Me hubieras metido el dedo por el culo cuando era chico?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Me hubieras pedido que te follara cuando eras chico?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "Las opiniones pueden cambiar según la circunstancia..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "No me vengas con gilipolleces [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Deja el puto ano."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


    elif (afternight04__Anal_Fingers_Success + afternight04__Anal_Fingers_Failed) == 3:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Anal_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Otra vez hurgándome el culo?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Es que te aburres?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Hasta ahora no te me habías quejado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡No en voz alta!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Acaso te crees que soy maricón o algo?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Fóllame el coño y deja de hacer mariconadas!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Hay que joderse..."

            elif afternight04__Anal_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Veamos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¿Quieres que te meta los putos dedos por tu jodido asqueroso ano?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Hombre,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "si crees que es tan asqueroso,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "no te lo recomiendo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "El tuyo parece particularmente limpio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "No me trolees [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "No me des pie a ello..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Me pregunto para qué coño te he pedido ayuda..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Porque vas más caliente que el aceite del churrero."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Gilipollas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04__Anal_Fingers_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Pero quieres dejar mi puto culo en paz de una puta jodida vez?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."


    elif afternight04__Anal_Fingers_Failed >= 4:

        if mc_body.roll_success == False: #You didn´t succeded.

            if afternight04__Anal_Fingers_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Estás buscando que salga algo de ahí dentro?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils right01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "¿Tienes ganas de ir de vientre?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "No he dicho eso idiota."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Ah..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sads_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Por qué demonios no me dejas de urgar dentro de mi jodido ano?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "No te has quejado de ello hasta ahora."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Tsk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "No hagas que me arrepienta de haberte pedido ayuda."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04__Anal_Fingers_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Sigues con la manía de meterme los dedos por detrás?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "No parece que te haya disgustado demasiado hasta el momento."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "Sino me haces algo tú pronto,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "lo haré yo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Quizás sería bueno intentar algo distinto antes de volver a intentarlo."

            elif afternight04__Anal_Fingers_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¿Sigues otra vez con los dedos?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Al final sacarás algo de ahí..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

            elif afternight04__Anal_Fingers_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿PERO QUIERES DEJAR MI PUTO CULO EN PAZ?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04__Anal_Fingers_Failed == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Te voy a dejar la mano marrón al final!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Debería empezar a cambiar de táctica..."

            elif afternight04__Anal_Fingers_Failed == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Pesado de mierda..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04__Anal_Fingers_Failed >= 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                
    
##############################################################
#############################################################

    # YOUR SUCCESS:
############################################################
###########################################################


    if mc_body.roll_success == True: #You succeded.
    ##

        if current_pose.id == "pose_1": ## POSE 01 
            call afternight04_sexbattle_pubic_emptiness
            show afternight04_sexbattle_mc_handR empty

            call afternight04_sexbattle_mc_handR_penetrate_anal_action_a

            with dissolve


        else:  ## POSE 02 and 03
            
            show afternight04_sexbattle_d_legs_anal 005_wet_00_b
            show afternight04_sexbattle_d_legs_anal_over 005_wet_00_b
            show afternight04_sexbattle_mc_tongue_anal empty
            show afternight04_sexbattle_mc_dick_anal empty

            show afternight04_sexbattle_mc_handR empty

            call afternight04_sexbattle_pubic_emptiness ## CALL
            call afternight04_sexbattle_mc_handR_penetrate_anal_action_b ## CALL

            with dissolve

    # HER SUCCESS REACTION:
############################################################
###########################################################

    #if mc_body.roll_success == True: #You succeded.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡Mhhhm...!"

        elif randomnum_1to5 == 2:

            d "¡Ahmmm...!"

        elif randomnum_1to5 == 3:

            d "¡Mffhmm...!"

        elif randomnum_1to5 == 4:

            d "¡Huffhm...!"

        elif randomnum_1to5 == 5:

            d "¡Ahfmm...!"

    # SUCCESS DIALOGUES:
############################################################
###########################################################

    #if mc_body.roll_success == True:

        if afternight04__Anal_Fingers_Success == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Gimiendo mientras te meto el dedo por aquí..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "No pensé que te gustaría tanto..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¿¡Por el culo?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Estás gilipollas?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            pt "Dirá lo que quiera,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            pt "pero no veo que me aparte la mano..."

        elif afternight04__Anal_Fingers_Success == 2:
        #elif current.girl.repeat == 2:

            #"He passed, she failed. Second SUCCESS.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "Se me hace curioso que con mis dedos consiga ponerte más caliente,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "que cuando tú tratas de masturbarte por el otro lado..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "¿No será que realmente te gusta más por detrás...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿Quieres que te meta yo el puño por el culo y comprobamos si te gusta?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "¿Eso es que me estás pidiendo que lo compruebe con el tuyo?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡NO!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Dios..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¿¿Has perdido la noción del sarcasmo?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "No,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "pero me encanta hacerte cabrear..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Tssk..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04__Anal_Fingers_Success == 3:
        #elif current.girl.repeat == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Por qué no confiesas que te encanta tener mis dedos metidos en el orto hasta el fondo?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Tú estás mal de la cabeza!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Y tú gimes como una perra."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Te voy a meter una hostia!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Ughmm..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¿Lo ves?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Idiota."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

        elif afternight04__Anal_Fingers_Success == 4:
        #elif current.girl.repeat == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Al final,"

            if afternight04__Anal_dick_med_Success >= 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "te va a gustar y todo que te meta la polla y los dedos por el culo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Se te va la pinza..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "vas a querer que te meta la polla por el culo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Se te va la puta olla."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

        elif afternight04__Anal_Fingers_Success == 5:
        #elif current.girl.repeat == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Pensaba que habías dicho que esto no te gustaría nada..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

        elif afternight04__Anal_Fingers_Success == 6:
        #elif current.girl.repeat == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "Lo disfrutas,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "y lo sabes."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils right00_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Maricón..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡GILIPOLLAS!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        else:

            #"repeated_lots"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            pt "Aunque ya no le disgusta,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "quizás sería hora de probar otras alternativas..."

    
    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return