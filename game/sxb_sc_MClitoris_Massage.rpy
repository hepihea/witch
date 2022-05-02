label MClitoris_Massage:

######################################################### Dummy_Screen Calls

    if mc_body.store["dick"] == "Pussy_dick_low":

        pt "Si tengo mi polla ahí,"

        pt "no puedo acariciarle el clítoris..."

        call screen dummy_screen()

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.07") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "MClitoris_Massage."

#########################################################

    $ mc_body.store["right_hand"] = "MClitoris_Massage"

#########################################################

    $ afternight04__prehfix_MClitoris_Massage = True
    $ afternight04__a_prehfix_MClitoris_Massage = True
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__MClitoris_Massage_Done += 1

        if mc_body.roll_success:
            $ afternight04__MClitoris_Massage_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__MClitoris_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Clitoris with your Right Hand.")

        call afternight04_MClitoris_Massage
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################


    label afternight04_MClitoris_Massage:

        call afternight04_MClitoris_Massage_general

        return

    label afternight04_MClitoris_Massage_his_orgasm:

        call afternight04_MClitoris_Massage_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04_MClitoris_Massage_her_orgasm:

        call afternight04_MClitoris_Massage_general

        call afternight04_mostly_her_orgasm

        return 

####################################
###################################
####################################
###################################
####################################
###################################



################################
###############################
##############################

label afternight04_MClitoris_Massage_general:
    
    # THERE´S ONLY POSE 01

    $ mc_body.store["right_hand"] == "MClitoris_Massage"
    show afternight04_sexbattle_mc_handR massage_clitoris_action_a

    if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep" or mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

        if not mc_body.store["tongue"] == "Pussy_Tongue":

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness
            
            show afternight04_sexbattle_d_legs_over_pussy empty
            show afternight04_sexbattle_d_legs_top_pussy empty

            show afternight04_sexbattle_d_legs_pussy 02_wet_00_a

        if not mc_body.store["tongue"] == "Anal_Tongue":

            show afternight04_sexbattle_mc_handR_penetrate_anal empty
            show afternight04_sexbattle_d_legs_over_anal empty
            show afternight04_sexbattle_d_legs_top_anal empty

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a



    with dissolve

##############################################################
#############################################################
    
    # Previous RHand Action
    
    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    #$ afternight04__a_prehfix_MClitoris_Massage = False

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

    #HER REACTION:
############################################################
###########################################################

    if mc_body.roll_success == True:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows sadx02_a
            with dissolve

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            d "¡MMMmhhh...!"

        elif randomnum_1to10 == 2:

            d "¡AAhhmm...!"

        elif randomnum_1to10 == 3:

            d "¡MMMmffm...!"

        elif randomnum_1to10 == 4:

            d "¡HHUumfm...!"

        elif randomnum_1to10 == 5:

            d "¡AAHhmfm...!"

        elif randomnum_1to10 == 6:

            d "¡AAUughmm...!"

        elif randomnum_1to10 == 7:

            d "¡MMHmm...!"

        elif randomnum_1to10 == 8:

            d "¡UUHghmm...!"

        elif randomnum_1to10 == 9:

            d "¡MUHhfmm...!"

        elif randomnum_1to10 == 10:

            d "¡HHMmmm...!"


    else: # You failed.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve


        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡Ouch!"

        elif randomnum_1to5 == 2:

            d "¡Auch!"

        elif randomnum_1to5 == 3:

            d "¡Ai!"

        elif randomnum_1to5 == 4:

            d "¡Iauch!"

        elif randomnum_1to5 == 5:

            d "¡Auh!"

############################################################

        $ mc_body.store["right_hand"] = ""
        show afternight04_sexbattle_mc_handR empty

        with hpunch

############################################################
###########################################################

        ####

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve


        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            pt "Mierda..."

        elif randomnum_1to5 == 2:

            pt "No puede ser..."

        elif randomnum_1to5 == 3:

            pt "¡¿En serio?!"

        elif randomnum_1to5 == 4:

            pt "Estás de coña..."

        elif randomnum_1to5 == 5:

            pt "No me lo puedo creer..."

        ####

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx07_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            pt "¿Le he hecho daño acariciándole el clítoris?."

        elif randomnum_1to5 == 2:

            pt "Por alguna razón le estoy haciendo más daño que placer."

        elif randomnum_1to5 == 3:

            pt "Por lo visto lo tiene demasiado sensible."

        elif randomnum_1to5 == 4:

            pt "¡¿Tan sensible lo tiene que ahora le he hecho daño?!"

        elif randomnum_1to5 == 5:

            pt "Con lo sensible que lo tiene le ha dolido."


########################################################################
########################################################################

    if mc_body.roll_success == True:

        #if current_girl.repeat == "once":
        if afternight04__MClitoris_Massage_Success == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¿Qué haces imbécil?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            p "Masajearte el clítoris..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "¿No es evidente?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿El clítoris?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "¡¿Para qué?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¡¿Qué cojones haces tú con las tías que te follas?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Pues follar joder!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            pt "Por qué será que no me sorprende su respuesta..."

        elif afternight04__MClitoris_Massage_Success == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Puedes decir misa,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "pero tienes el clítoris realmente sensible..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

        elif afternight04__MClitoris_Massage_Success == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "Por tu gemido no parece que lo odies..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Preferiría..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "que te centraras en otra cosa..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "Ya..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "por eso tu respiración es agitada..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04__MClitoris_Massage_Success == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "¿Estás seguro que no te gusta?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Idiota..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04__MClitoris_Massage_Success == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "¿Sigues pensando que no te gusta?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No he dicho nada!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

        elif afternight04__MClitoris_Massage_Success == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            p "Reconoce que te encanta."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Gilipollas."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04__MClitoris_Massage_Success == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            pt "Está claro que le gusta,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            pt "pero no le afecta del mismo modo que antes..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "Sería bueno cambiar de táctica antes de que tome la iniciativa..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

    else: #elif mc_body.roll_success == False

        #if current_girl.total_fail == 1:
        if afternight04__MClitoris_Massage_Failed == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿Qué haces?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Masajearte el clítoris para ir calentándote."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Ya estoy caliente!"

            if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿Acaso no me la has metido ya?!"

            elif afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿ACASO NO ME LA HE METIDO YA?!"

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿O es que aún no te ha quedado claro?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

        elif afternight04__MClitoris_Massage_Failed == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿Otra vez?..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¡Joder Dídac!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "¡Intento hacer preliminares!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Pues sáltatelos!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Quiero que me folles y te dejes de gilipolleces!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

        elif afternight04__MClitoris_Massage_Failed == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "La próxima vez que me vengas con esta mariconada voy a violarte..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

        elif afternight04__MClitoris_Massage_Failed == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿Pero me estás escuchando?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "..."

        elif afternight04__MClitoris_Massage_Failed == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡Me harás cabrear de verdad!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "..."

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx09_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve


    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return

