label Pussy_Tongue:

######################################################### Dummy_Screen Calls

    if (mc_body.store["dick"] == "Anal_dick_low" or mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

        #$ afternight04__prehfix_Pussy_Tongue = False
        #$ afternight04__a_prehfix_Pussy_Tongue = False

        $ mc_body.store["tongue"] = ""

        pt "¿Y cómo diablos hago eso?"

        pt "Si tengo mi polla en su culo,"

        pt "no voy a llegar ahí con mi lengua..."

        call screen dummy_screen()

    ##

######################################################### 

    if afternight04_condom_broken == True:

        $ mc_body.store["tongue"] = ""

        jump afternight04_condom_broken_scene

    ##

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.09.00") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "Pussy_Tongue."

#########################################################

    $ mc_body.store["tongue"] = "Pussy_Tongue"

#########################################################

    $ afternight04__prehfix_Pussy_Tongue = True
    $ afternight04__a_prehfix_Pussy_Tongue = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__Pussy_Tongue_Done += 1

        if mc_body.roll_success:
            $ afternight04__Pussy_Tongue_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__Pussy_Tongue_Failed += 1

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
                $ afternight04__Pussy_Tongue_Success += 1

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
        $ debug ("First Orgasm for his. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_Pussy_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Penetrating her Pussy with your Tongue.")

        call afternight04_Pussy_Tongue
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_Pussy_Tongue:

        call afternight04_Pussy_Tongue_general

        return

    label afternight04_Pussy_Tongue_his_orgasm:

        call afternight04_Pussy_Tongue_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04_Pussy_Tongue_her_orgasm:

        call afternight04_Pussy_Tongue_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################

label afternight04_Pussy_Tongue_general:


    if mc_body.store["dick"] == "Pussy_dick_out" or mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep":
        
        $ mc_body.store["dick"] = "Pussy_dick_out"

    if mc_body.store["right_hand"] == "Pussy_Fingers":
        $ mc_body.store["right_hand"] = ""

    
    $ mc_body.store["tongue"] == "Pussy_Tongue"

    if current_pose.id == "pose_1":

        show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_mc_tongue_anal empty

        if not mc_body.store["right_hand"] == "Anal_Fingers":

            show afternight04_sexbattle_d_legs_top_anal empty
            show afternight04_sexbattle_d_legs_over_anal empty
        
        show afternight04_sexbattle_mc_dick_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        ###show afternight04_sexbattle_mc_handR_penetrate_anal empty #Not sure if anable this or not.
        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        ##
        show afternight04_sexbattle_d_legs_pussy 04_wet_00_a: #To avoid Move from Dick Actions.
            afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
            afternight04_sexbattle_d_pubicpart_pos

        show afternight04_sexbattle_d_legs_base wet_00_a:
            afternight04_sexbattle_empty_position
        ##

        #show afternight04_sexbattle_mc_tongue_pussy action_a
        $ debug ("Here goes T PUSSY Starting A") #Not finished.
        call afternight04_sexbattle_mc_tongue_pussy_starting_a

        with dissolve

    else:

        show afternight04_sexbattle_d_legs_over_pussy 005_wet_00_b
        show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        show afternight04_sexbattle_mc_dick_pussy empty

        show afternight04_sexbattle_mc_tongue_anal empty


        #show afternight04_sexbattle_mc_tongue_pussy action_b
        $ debug ("Here goes T PUSSY Starting B") #Not finished.
        call afternight04_sexbattle_mc_tongue_pussy_starting_b

        with dissolve

##############################################################
#############################################################

    # Previous Tongue Action

    $ afternight04__a_prehfix_MClitoris_Tongue = False
    $ afternight04__a_prehfix_MMouth_Tongue = False
    #$ afternight04__a_prehfix_Pussy_Tongue = False
    $ afternight04__a_prehfix_Anal_Tongue = False  # Rim Job
    $ afternight04__a_prehfix_RNipple_Lick = False  # Rim Job

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

    #HER REACTION:
############################################################
###########################################################

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils down04_a
        with dissolve

    d "..."

    if mc_body.roll_success == False: # You failed.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡Humm!"

        elif randomnum_1to5 == 2:

            d "¡Tss!"

        elif randomnum_1to5 == 3:

            d "¡Hmm!"

        elif randomnum_1to5 == 4:

            d "¡Hmpfh!"

        elif randomnum_1to5 == 5:

            d "¡Tsk!"

############################################################

        $ mc_body.store["tongue"] == ""

        if current_pose.id == "pose_1": ## POSE 01 

            show afternight04_sexbattle_d_legs_top_pussy empty
            show afternight04_sexbattle_d_legs_over_pussy empty
            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a
            show afternight04_sexbattle_mc_tongue_pussy empty

        else:

            show afternight04_sexbattle_d_legs_top_pussy empty
            show afternight04_sexbattle_d_legs_over_pussy empty
            show afternight04_sexbattle_d_legs_pussy 002_wet_00_b
            show afternight04_sexbattle_mc_tongue_pussy empty

        with hpunch

############################################################
###########################################################

## TRIES

    #if current_girl.total_try == 0:
    if (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) == 0:

        aj "This text should not appear. 5142"


## 1rst TRY.

    #if current_girl.total_try == 1:
    if (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) == 1:

        if mc_body.roll_success == True: #You succeded.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿Qué haces [protname]?"

            if afternight04__MClitoris_Massage_Success > 0 and afternight04__MClitoris_Tongue_Success > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Viendo lo sensible que tienes el clítoris,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "He pensado que como lubricación,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "estaría bien empezar por meterte mi lengua hasta el fondo."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "Estoy lubricando un poco el paso..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Pero de qué {i}lubricación{/i} hablas?!"

            if afternight04_Pussy_dick_med_Speed_0_Done > 0 or afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Si ya me la has metido dentro!"

                if afternight04_Pussy_dick_med_Speed_0_Done < 0 and afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "En realidad has estado tú quien se la ha metido dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Lo que quiero es que me metas la polla."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No tu lengua!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Que por muy larga que la tengas,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "no va a ser lo mismo que tu jodida {i}anaconda{/i}."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Llevo todo el puto día metiéndome consoladores,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "vibradores"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "y otras cosas en general!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿Tú crees que necesito más lubricación?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "Parece que no será tan fácil como pensaba,"

            pt "el coño lo tiene bastante chamuscado..."


############################### YOU FAILED for second time.

    if mc_body.roll_success == False: #You Failed.

        if (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Hay que joderse..."

            if afternight04__Pussy_Tongue_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Deja la lengua en paz"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Y méteme la polla!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04__Pussy_Tongue_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡No me ignores!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Si quieres penetrarme,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡házmelo como es debido!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve


        elif (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) == 3:

            if afternight04__Pussy_Tongue_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Sigues con la lengua..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Hasta ahora no te me has quejado."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Joder!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡Claro que me gusta!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows suspicious01_a
                    with dissolve

                p "¿Entonces?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Voy muy cachonda [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Necesito algo más."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Tongue_Failed >= 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Vamos a ver [protname];"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "claro que me gusta que me folles,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Pero no con tu lengua!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04__Pussy_Tongue_Failed >= 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "En serio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¿No se te ocurre hacer otra cosa?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Intento variar..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Pues no varíes tanto!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Que mierda de amante tiene que ser este tío..."


        elif (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) == 4:

            if afternight04__Pussy_Tongue_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Vas a estar mucho rato jugando con la lengua?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Por mucho que me guste,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "con tu lengua no harás nada que no haya probado el resto del día..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Parece que esta vez no le ha gustado tanto como las anteriores veces..."

            elif afternight04__Pussy_Tongue_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Sigues con la lengua?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "No parece que te haya disgustado demasiado hasta el momento."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Sino me haces algo tú pronto,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "lo haré yo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Quizás sería bueno intentar algo distinto antes de volver a intentarlo."

            elif afternight04__Pussy_Tongue_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Sigues otra vez con la lengua?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Al final no vas a poder ni hablar..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Tongue_Failed >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "De verdad,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 075_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "ya cansas."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "¡¿Es que se ha cargado toda la sensibilidad del coño!"

                pt "¡¿Qué mierda de vibradores ha usado?!"

                pt "¿Por qué se supone que con la polla va a ser distinto?"


        elif (afternight04__Pussy_Tongue_Success + afternight04__Pussy_Tongue_Failed) >= 5:

            if afternight04__Pussy_Tongue_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es que me disguste sentirme penetrada por ti,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Pero con otra parte de tu cuerpo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "quizás lo apreciaría mejor..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Hasta ahora no te me has quejado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils left05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "No he dicho que me disguste."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Entonces?"

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Quiero que seas tú el que me viole."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Quiero que me folles [protname]."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                p "..."

            elif afternight04__Pussy_Tongue_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es por quejarme,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Pero cuando tienes pensando follarme de verdad?"

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¡Pero si ya me has violado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pues espera que no lo vuelva a hacer!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve
                    
                    p "¡Pero si ya te la he metido dentro!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pues vuelve a ello y deja los jodidos dedos!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Cuando me de la gana."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "La paciencia tiene un límite [protname]."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "Todo tiene límite,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "excepto tu zorrería."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Tsk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

            elif afternight04__Pussy_Tongue_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿A ti te gustaría que me pasara todo el día lamiendo superficialmente tu polla?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "No veo porque no..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils right01_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                p "Aunque si de tanto en cuanto también te la metieras en la boca,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "ya sería la hostia."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Gilipollas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04__Pussy_Tongue_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "En serio [protname],"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "varía un poco..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif afternight04__Pussy_Tongue_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Al final me va a violar..."

            elif afternight04__Pussy_Tongue_Failed == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Será mejor probar otra cosa..."

            elif afternight04__Pussy_Tongue_Failed == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Debería cambiar de táctica..."

            elif afternight04__Pussy_Tongue_Failed >= 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
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
    ###

    if mc_body.roll_success == True:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_mc_tongue_clitoris empty
            show afternight04_sexbattle_mc_tongue_anal empty

            if not mc_body.store["right_hand"] == "Anal_Fingers":

                show afternight04_sexbattle_d_legs_top_anal empty
                show afternight04_sexbattle_d_legs_over_anal empty
            
            show afternight04_sexbattle_mc_dick_pussy empty

            call afternight04_sexbattle_pubic_emptiness


            ##
            show afternight04_sexbattle_d_legs_pussy 04_wet_00_a: #To avoid Move from Dick Actions.
                afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_empty_position
            ##

            call afternight04_sexbattle_mc_tongue_pussy_action_a

            with dissolve

        else:

            show afternight04_sexbattle_d_legs_over_pussy 005_wet_00_b
            show afternight04_sexbattle_mc_handR_penetrate_pussy empty
            show afternight04_sexbattle_mc_dick_pussy empty

            show afternight04_sexbattle_mc_tongue_anal empty

            call afternight04_sexbattle_mc_tongue_pussy_action_b

            with dissolve

    #HER REACTION:
############################################################
###########################################################

    #if mc_body.roll_success == True: # Not necessary.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils up05_a
            show afternight04_sexbattle_d_eyebrows sadx03_a
            with dissolve

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            d "¡UUHhmmmm...!"

        elif randomnum_1to10 == 2:

            d "¡HHFHmmmm...!"

        elif randomnum_1to10 == 3:

            d "¡UUGHhmm...!"

        elif randomnum_1to10 == 4:

            d "¡AAHHHmmmm...!"

        elif randomnum_1to10 == 5:

            d "¡MMFHmmmf...!"

        elif randomnum_1to10 == 6:

            d "¡AUGHmmmm...!"

        elif randomnum_1to10 == 7:

            d "¡MMMmmmm...!"

        elif randomnum_1to10 == 8:

            d "¡UHGHhmmmm...!"

        elif randomnum_1to10 == 9:

            d "¡MUHFmmmm...!"

        elif randomnum_1to10 == 10:

            d "¡HHFMmmm...!"


        #HIS SUCCESS:

    #if mc_body.roll_success == True: # Not necessary.

        if afternight04__Pussy_Tongue_Success == 1:
        #if current.girl.repeat == 1:

            #"He passed, she failed. First SUCESS.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Paghece que Noh the dihgushta..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve


            d "Con la lengua así no se te entiende una mierda..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "Ya me has entendido, ya..."

        elif afternight04__Pussy_Tongue_Success == 2:
        #elif current.girl.repeat == 2:

            #"He passed, she failed. Second SUCCESS.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Hijo de puta..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡¿Cómo coño tienes la lengua tan larga?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "¡No solo es la longitud,"

            pt "sino también la capacidad de mantenerla así de firme!"

            pt "Aunque ahora que lo pienso,"

            pt "sí que es verdad que quizás es un poco larga..."

        elif afternight04__Pussy_Tongue_Success == 3:
        #elif current.girl.repeat == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "La madre que te parió..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Puta lengua que tienes mamonazo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__Pussy_Tongue_Success == 4:
        #elif current.girl.repeat == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "Alg fignalgh vasgh a prehferigh mi lenghuahg a mi pogllagh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Eso lo dudo mucho..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "Con tu lengua no llegas a dónde llega tu pedazo de {i}anaconda{/i}..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__Pussy_Tongue_Success == 5:
        #elif current.girl.repeat == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¿Cuándo besas a las chicas no las ahogas con esta lengua?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            p "..."

        elif afternight04__Pussy_Tongue_Success == 6:
        #elif current_girl.repeat == "repetitive": #Less than 7
        #elif current.girl.repeat == 6:
        #
            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Seguro que tú sí llegas a tocarte el codo con esa lengua..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            pt "Está claro que ya no lo disfruta como antes..."

        elif afternight04__Pussy_Tongue_Success == 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            pt "Aunque ya no le disgusta,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            pt "quizás sería hora de probar otras alternativas..."

        elif afternight04__Pussy_Tongue_Success >= 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

    
    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return

 