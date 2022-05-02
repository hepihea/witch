label MStomach_Massage:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.06"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "MStomach_Massage."

#########################################################

    $ mc_body.store["left_hand"] = "MStomach_Massage"

#########################################################

    $ afternight04__prehfix_MStomach_Massage = True
    $ afternight04__a_prehfix_MStomach_Massage = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__MStomach_Massage_Done += 1

        if mc_body.roll_success:
            $ afternight04__MStomach_Massage_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__MStomach_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_MStomach_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Stomach with your Left Hand.")

        call afternight04_MStomach_Massage
        
        jump expression __prefix + "call_screen"


####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_MStomach_Massage:

        call afternight04_MStomach_Massage_general

        return

    label afternight04_MStomach_Massage_his_orgasm:

        call afternight04_MStomach_Massage_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04_MStomach_Massage_her_orgasm:

        call afternight04_MStomach_Massage_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################


label afternight04_MStomach_Massage_general:

    if afternight04_CumOnStomach == 0:

    ##############################################################
    #############################################################

        show afternight04_sexbattle_mc_handL massage_stomach_action_a
        with dissolve

    ##############################################################
    #############################################################

        if mc_body.roll_success == True: #You succeded.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "Mmm..."

            elif randomnum_1to5 == 2:

                d "Humm..."

            elif randomnum_1to5 == 3:

                d "Hmm..."

            elif randomnum_1to5 == 4:

                d "Nghn..."

            elif randomnum_1to5 == 5:

                d "Uhhm..."

        else: # You failed.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "Pff..."

            elif randomnum_1to5 == 2:

                d "Tss..."

            elif randomnum_1to5 == 3:

                d "Ugh..."

            elif randomnum_1to5 == 4:

                d "..."

            elif randomnum_1to5 == 5:

                d "Tsk..."

    ##############################################################

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

    ##############################################################
    #############################################################

        if mc_body.roll_success == True: # You succeded

            #if current_girl.total_success == 1:
            #if pose01_stomach.get_action("MStomach_Massage").times_done == 1:
            if afternight04__MStomach_Massage_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Qué coño haces?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Dándote un masaje para ir preparando el terreno."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡¿Tú te crees que necesito más preliminares?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿Después de todo lo que te he dicho sobre lo cachonda que voy hoy?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Sino te gusta,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "te aguantas."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Me has pedido ayuda,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "así que lo haré a mi manera."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Parece que por el momento puedo dominar la situación..."

            elif afternight04__MStomach_Massage_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿No te cansas con la manita?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "No parece que te disguste..."

                if mc_body.store["dick"] == "Pussy_dick_low":

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Me gustaría más me la metieras dentro,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "en lugar de tenerla solo encima..."

                elif (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: # STOP 

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Preferiría que movieras la puta polla en lugar de tenerla ahí quieta..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    elif mc_body.dick_speed == 1: # SLOW

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "¿Te criaste entre babosas?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        p "¿Qué?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "Que mueves tu polla como un puto caracol."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¡Dale más vida coño!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                    elif mc_body.dick_speed == 2: # MOD

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                            with dissolve

                        d "Si te dejaras de hostias con las manos,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve


                        d "y movieras un poco más rápido esa polla tuya estaría mucho mejor!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        p "No estás nunca contento..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        p "¿Verdad?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "..."

            elif afternight04__MStomach_Massage_Success == 3: # = elif current_girl.total_success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Mucho quejarte,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "pero poco a poco te va gustando más..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No digas gilipolleces..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve


            elif afternight04__MStomach_Massage_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "¿No dices nada ya?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Idiota..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__MStomach_Massage_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Quita esa estúpida sonrisa de tu cara."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__MStomach_Massage_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "No niego que haces buenos masajes,"

                if mc_body.store["dick"] == "Pussy_dick_low":

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows normalx01_a
                        with dissolve

                    d "pero lo agradecería si me metieras la polla dentro de una jodida vez."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Tus preliminares son jodidamente lentos..."

                elif (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: # STOP 

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                            with dissolve

                        d "Preferiría que no tuvieras la puta polla ahí quieta muriéndose de asco."

                    elif mc_body.dick_speed == 1: # SLOW

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¿Te criaste entre estrellas de mar?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        p "¿Cómo?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Que como muevas más lentamente esa polla,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "voy a pensar que estamos retrocediendo en el tiempo!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡¿Qué?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "Que te centres algo más en tu polla,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¡y me la metas más rapido!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Coño!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                    elif mc_body.dick_speed == 2: # MOD

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Si dejaras de hacer de masajista de las narices"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "y le dieras un poco más de vidilla a esa polla tuya,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "Te lo agradecería mucho más..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows normal_a
                            with dissolve

                        pt "¿Más aún?"

                    elif mc_body.dick_speed == 3: # FAST Not sure if this is actually POSSIBLE? Yes, it´s possible, unless she rapes you.

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows suspicious_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        p "¿Y qué...?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        d "Si quieres tocarme,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "tócame,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "pero no me dejes de follar como lo estás haciendo."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Creo que ya basta de preliminares..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿No crees...?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                pt "Creo que debería de cambiar de estrategia o acabará cansándose y violándome hasta el final..."

            elif afternight04__MStomach_Massage_Success >= 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "Pesadito con el masajito..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            else:

                prgcheck "THIS TEXT SHOULD NOT BE VISIBLE 2687"

                

        else: # You Failed

            #if current_girl.total_fail == 1:
            if afternight04__MStomach_Massage_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Qué cojones estás haciendo?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Dándote un masaje para ir preparando el terreno."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "[protname]..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Te he dicho que llevo todo el puto día masturbándome por todas partes..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Tú te crees que necesito más preliminares?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Sino te gusta,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "te aguantas."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Me has pedido ayuda,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "así que lo haré a mi manera."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No me vengas con amenazas de mierda [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "O cojo unas tijeras y te corto la polla..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿QUEDA CLARO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Quiero creer que lo dice en coña..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Pero con esa cara de psicópata,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "ya no sé ni que pensar..."

            elif afternight04__MStomach_Massage_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Te lo pasas bien?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "¿No te gusta?"

                if mc_body.store["dick"] == "Pussy_dick_low":

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Preferiría que en lugar de poner tu polla sobre mi coño..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡LA PUSIERAS DENTRO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                    if mc_body.dick_speed == 0: # STOP 

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "Preferiría que movieras la puta polla en lugar de tenerla ahí quieta..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                    elif mc_body.dick_speed == 1: # SLOW

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "¿Me has tomado por una hembra de perezoso?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡¿Acaso quieres me corra la próxima década?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        d "Déjate de masajes de mierda y dale más brillo al puto manubrio!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    elif mc_body.dick_speed == 2: # MOD

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "Si te dejaras de hostias con las manos y movieras un poco más rápido esa polla tuya estaría mucho mejor!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "No veo que estés usando tu polla contra mi coño..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Que me folles!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡COÑO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                pt "Quizás necesito controlar mejor la situación antes de volverlo a intentar..."

            elif afternight04__MStomach_Massage_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Me estás empezando a tocar las narices con tanto toqueteo en mi barriga..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04__MStomach_Massage_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Otra vez?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04__MStomach_Massage_Failed == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿En serio...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Eres pesado de narices con la manita de los cojones..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


        ###########################
        ##########################

        ### RAPE OR NOT?

        call afternight04_RapeOrNot

        ###########################
        ########################## ## This is special, so LEAVE IT HERE, Cum of stomach should not be punished.


        
        ###########################
        ##########################
        ### CUM on her STOMACH.

    else: 

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

        $ afternight04_WantTouchStomachCum += 1

        if afternight04_WantTouchStomachCum == 1:

            pt "¿Estoy majara?"

            pt "Tiene mi corrida en su barriga..."

            pt "¿Por qué diablos querría embadurnar mi mano con mis mocos blancos?"

        elif afternight04_WantTouchStomachCum == 2:

            pt "¡Coño!"

            pt "¡Que el queso blanco sigue ahí!"

            pt "¡Paso!"

        elif afternight04_WantTouchStomachCum == 3:

            pt "¡Cagüen Dios!"

            pt "Pedazo gotelé le he dejado..."

            pt "No pienso tocar eso ni con guantes..."

        else:

            pt "¡¿Otra vez insisto en lo mismo?!"

            pt "¡¿Es que hay alguien que controla lo que hago?!"

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx02_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve


    return


