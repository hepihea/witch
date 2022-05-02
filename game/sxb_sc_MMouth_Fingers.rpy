label MMouth_Fingers:

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.05") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    #if afternight04_SheRapingYou == True:

        #call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "MMouth_Fingers."

#########################################################

    $ mc_body.store["right_hand"] = "MMouth_Fingers"

#########################################################

    $ afternight04__prehfix_MMouth_Fingers = True
    $ afternight04__a_prehfix_MMouth_Fingers = True
    
    call afternight04_sex_check_before
    
    label .manager:

        if current_pose.id == "pose_3":

            $ afternight04__MMouth_Fingers_Done += 1

            if mc_body.roll_success:
                $ afternight04__MMouth_Fingers_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__MMouth_Fingers_Failed += 1

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
        $ debug ("First Orgasm for his. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04__MMouth_Fingers_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Putting in her Mouth your Fingers.")

        call afternight04__MMouth_Fingers
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04__MMouth_Fingers:

        call afternight04__MMouth_Fingers_general

        return


    label afternight04__MMouth_Fingers_his_orgasm:

        call afternight04__MMouth_Fingers_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04__MMouth_Fingers_her_orgasm:

        call afternight04__MMouth_Fingers_general

        call afternight04_mostly_her_orgasm

        return


####################################
###################################

label afternight04__MMouth_Fingers_general:


    ##############################################################
    #############################################################

    if current_pose.id == "pose_1": # HER REACTION is not necessary.

        $ mc_body.store["right_hand"] == "MMouth_Fingers"
        show afternight04_sexbattle_mc_handR massage_mouth_action_a
        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness
        
        with dissolve

    #elif current_pose.id == "pose_2": 

        #$ debug ("You can´t reach her mouth here.")

    elif current_pose.id == "pose_3": 

        ##########

        $ afternight04__MMouth_Fingers_Done += 1

        if mc_body.roll_success:

            $ afternight04__MMouth_Fingers_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__MMouth_Fingers_Failed += 1

        ##########

        $ debug ("In this position you can Put Finges in her mouth?")

    ##############################################################
    #############################################################

##############################################################
#############################################################
    
    # Previous RHand Action
    
    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    #$ afternight04__a_prehfix_MMouth_Fingers = False
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

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 01

    if current_pose.id == "pose_1":

        if current_girl.enslavement < 50:

            if current_girl.total_try == 1: #Don´t change that.

                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

                d "..."

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

                d "¿Se puede saber qué coño intentas hacer poniéndome el puto dedo dentro de la boca?"

                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

                p "..."

                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

                d "..."

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

                p "..."

                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with vpunch

                d "¡Te he hecho una jodida pregunta!"

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                p "..."

                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "¡Pero aparta la jodida mano!"

                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                $ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty
                with vpunch

                d "¡Coño!"

                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                pt "No parece que le haya gustado la idea..."

            elif current_girl.total_try == 2:

                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                d "..."

                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

                d "En serio..."

                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "¿Qué puto problema tienes con el puñetero dedo de los cojones?"

                #if pose01_pussy.get_action("Pussy_Fingers").times_done >= 1:
                if afternight04__Pussy_Fingers_Success > 0:

                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                    p "Pensaba que te gustaba el olor de un coño húmedo..."

                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                    p "Quizás además de cambiar de aspecto,"

                    p "también estás cambiando de gustos..."

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "..."

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "Este olor no es de un coño..."

                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                    d "¡Es de MI coño!"

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                    d "Y no me vengas con gilipolleces,"

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "porque no me lo estás haciendo oler..."

                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 031_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                    d "¡Me lo estás restregando por la boca!"

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                pt "En realidad,"

                extend " lo que intento es meterle el dedo en la boca para ver si consigo que le guste chupar..."

                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows angryx04_a

                $ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty
                with vpunch

                d "¡QUE PARES YA!"

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                pt "Está claro que esto no está funcionando..."

            elif current_girl.total_try >= 3:

                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "Puto [protname]..."

                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                $ mc_body.store["right_hand"] = ""
                show afternight04_sexbattle_mc_handR empty
                with vpunch

                d "¡QUITA COÑO!"

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                d "¡Al final te voy a meter una hostia!"

                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                p "..."

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                pt "¿Por qué sigo insistiendo?"

                ###########################
                ##########################

                ### RAPE OR NOT?

                call afternight04_RapeOrNot

                return

                ###########################
                ##########################

        else:



            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils down03_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "..."

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve


            $ randomnum_1to10 = renpy.random.randint(1, 10)

            if randomnum_1to10 == 1:
                
                d "Eres un puto pesado [protname]..."

            elif randomnum_1to10 == 2:

                d "¿Vas a estar con el puto dedo de las narices todo el día?"

            elif randomnum_1to10 == 3:

                d "¡Aparta tu sucia mano de mi cara!"

            elif randomnum_1to10 == 4:

                d "¡Al final te voy a meter ese dedo por el culo!"
                
            elif randomnum_1to10 == 5:

                d "¡He visto moscas menos cojoneras que tú!"
                
            elif randomnum_1to10 == 6:

                d "¡Pareces un estúpido niño!"
                
            elif randomnum_1to10 == 7:

                d "¡¿Esto es lo que haces con las tías?!"
                
            elif randomnum_1to10 == 8:

                d "¡Eres más pesado que un hipopótamo!"
                
            elif randomnum_1to10 == 9:

                d "¡Déjame la boca en paz!"
                
            elif randomnum_1to10 == 10:

                d "¡Quita ese puto dedo!"
                

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty
            with hpunch


            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils right04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            p "..."

            

        call screen dummy_screen()

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 02

    #elif current_pose.id == "pose_2": 

        #$ debug ("You can´t reach her mouth here.")

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 03

    elif current_pose.id == "pose_3": 

        $ debug ("Fingers in her mouth?")

        aj "Dialogue is still not finished."

        # NOT FINISHED

        return


