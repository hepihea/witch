default afternight04_Nipple_Lick_Bite_Done = 0
default afternight04_Nipple_Lick_Bite_Success = 0
default afternight04_Nipple_Lick_Bite_Failed = 0
default afternight04_Nipple_Lick_Bite_Success_Cond = False

#########################################################

label RNipple_Lick:

######################################################### Dummy_Screen Calls

    if current_pose.id == "pose_3": ## POSE 03

        if (mc_body.store["dick"] == "Pussy_dick_low" 
            or mc_body.store["dick"] == "Pussy_dick_med" 
            or mc_body.store["dick"] == "Pussy_dick_deep"
            or mc_body.store["dick"] == "Anal_dick_low" 
            or mc_body.store["dick"] == "Anal_dick_med" 
            or mc_body.store["dick"] == "Anal_dick_deep"):

            pt "A menos que saque mi polla de aquí,"

            pt "no conseguiré llegar a lamer su pezón."

            call screen dummy_screen()


######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.03") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "RNipple_Lick."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RNipple_Lick"

    else:

        $ mc_body.store["right_hand"] = "RNipple_Lick"

#######################################################

    $ afternight04__prehfix_RNipple_Lick = True
    $ afternight04__a_prehfix_RNipple_Lick = True 
    
    call afternight04_sex_check_before
    
    label .manager:

        if current_pose.id == "pose_3":

            $ afternight04__RNipple_Lick_Done += 1

            if mc_body.roll_success:
                $ afternight04__RNipple_Lick_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__RNipple_Lick_Failed += 1

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
        $ debug ("First Orgasm for his. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Licking her Right Nipple.")

        call afternight04_RNipple_Lick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RNipple_Lick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Licking her Right Nipple.")

        call afternight04_RNipple_Lick
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_RNipple_Lick:

        call afternight04_Nipple_Lick

        return

    label afternight04_RNipple_Lick_his_orgasm:

        call afternight04_LNipple_Lick

        call afternight04_mostly_her_orgasm

    label afternight04_RNipple_Lick_her_orgasm:

        call afternight04_LNipple_Lick

        call afternight04_mostly_her_orgasm

####################################
###################################
####################################
###################################
####################################
###################################

label afternight04_Nipple_Lick:

    #################################################################################################################
    #################################################################################################################

    # You can´t lick both Nipples at same time.

    #################################################################################################################
    #################################################################################################################

    # FOR POSES this is the right way.

    $ afternight04__prehfix_MClitoris_Tongue = False
    $ afternight04__prehfix_Pussy_Tongue = False

    show afternight04_sexbattle_mc_tongue_clitoris empty
    show afternight04_sexbattle_mc_tongue_pussy empty
    with dissolve

    #if current_pose.id == "pose_1": #NOT NECESSARY, since anything will be visible here.

    if current_pose.id == "pose_3":

        $ mc_body.store["right_hand"] == ""
        show afternight04_sexbattle_mc_handR empty

        show afternight04_sexbattle_mc_tongue nippleR_anim_c

        $ debug ("Here is where I put your tongue licking her right Nipple while she is on her four.")


##############################################################
#############################################################

        if mc_body.roll_success == True: #You succeded.

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

        else: # You Failed

            if (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) == 1:

                $ randomnum_1to5 = renpy.random.randint(1, 5)

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

                if randomnum_1to10 == 1:

                    d "¡¿Otra vez?!"

                elif randomnum_1to10 == 2:

                    d "¡Quita la lengua de ahí!"

                elif randomnum_1to10 == 3:

                    d "¡¿Te crees que tengo pluma?!"

                elif randomnum_1to10 == 4:

                    d "¡¿A qué viene esta mariconada?!"

                elif randomnum_1to10 == 5:

                    d "¡Deja mi pezón en paz!"

                elif randomnum_1to10 == 6:

                    d "¡¿Te he pedido que me lames el pezón?!"

                elif randomnum_1to10 == 7:

                    d "¡Deja el puto pezón en paz!"

                elif randomnum_1to10 == 8:

                    d "¡¿Pero qué coño haces?!"

                elif randomnum_1to10 == 9:

                    d "¡¿Pero qué mierda de mariconada es esta?!"

                elif randomnum_1to10 == 10:

                    d "¡Al final pensaré que eres de la otra cera!"

############################################################ # OFF image
#############################################################

                $ mc_body.store["tongue"] == ""
                show afternight04_sexbattle_mc_tongue empty
                with hpunch

##############################################################
#############################################################

    # Previous Tongue Action

    $ afternight04__a_prehfix_MClitoris_Tongue = False
    $ afternight04__a_prehfix_MMouth_Tongue = False
    $ afternight04__a_prehfix_Pussy_Tongue = False
    $ afternight04__a_prehfix_Anal_Tongue = False  # Rim Job
    #$ afternight04__a_prehfix_RNipple_Lick = False  # Rim Job

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################
##############################################################
#############################################################

    if current_pose.id == "pose_1":
        
        if current_girl.total_try == 1: # Don´t change that!

            #$ debug ("Total TRY 1 for both Nipples.")

            #if current_pose.id == "pose_1": # Not necessary.
            show afternight04_sexbattle_d_mouth sad_Talkingx01_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            d "¿Euh?"

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            pt "Mierda..."

            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
            with dissolve

            d "¿Qué demonios haces [protname]?"

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve

            pt "No alcanzo a llegar hasta su pezón con mi lengua desde aquí abajo..."

            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows normal_a
            with dissolve

            d "Estás haciendo un careto muy raro..."

            show afternight04_sexbattle_d_mouth sad_Silentx02_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

        elif current_girl.total_try == 2:

            #$ debug ("Total TRY 2 for both Nipples.")

            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            d "¿Otra vez sacando la lengua mientras estiras el cuello?"

            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
            with dissolve

            d "¿Es que es un nuevo tipo de estiramiento y no me he enterado?"

            show afternight04_sexbattle_d_mouth sad_Silentx02_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            p "..."

        elif current_girl.total_try == 3:

            #$ debug ("Total TRY 3 for both Nipples.")

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            d "..."

            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve

            d "De verdad [protname],"

            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "Me estás agotando la paciencia haciendo tanto el imbécil con la lengua..."

            if afternight04_SheRapingYou == True:

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                d "Si sigues así,"

                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                d "te voy a violar hasta que me salga de las pelotas."

            elif (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out"):

                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                d "La próxima vez,"

                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                d "haré lo que tú no haces."

            else:

                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                d "La próxima vez,"

                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

                d "seré yo quien te folle a ti."

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            p "..."

        elif current_girl.total_try == 4:

            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "¿No te cansas de hacer el imbécil?"

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

        elif current_girl.total_try == 5:

            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Estás haciendo el ridículo..."

            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

        elif current_girl.total_try == 6:

            #$ debug ("Total TRY 6 for both Nipples?")

            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Te la estás jugando..."

            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

        elif current_girl.total_try >= 7:

            show afternight04_sexbattle_d_mouth sad_Silentx05_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "..."

            if afternight04_SheRapingYou == False and (mc_body.store["dick"] == "" or mc_body.store["dick"] == "Pussy_dick_out"): 

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                    d "Si quieres hacer el imbécil es tu problema."

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "Pero ya que no lo haces tú,"

                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "lo haré yo."

                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                elif randomnum_1to5 == 2:

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                    d "Me parece muy bien que quieras hacer estiramientos de cuello y de lengua,"

                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front035_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                    d "Pero yo quiero follar."

                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                elif randomnum_1to5 == 3:

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                    d "A veces pienso que te escapaste de un zoo..."

                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                elif randomnum_1to5 == 4:

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                    d "Si a ti te gusta hacer el idiota,"

                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "a mi me gusta violarte."

                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                elif randomnum_1to5 == 5:

                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                    d "Me esperaba algo más de ti,"

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                    d "la verdad..."

                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            ############################################################

            ###########################
            ##########################

            ### RAPE OR NOT?

            call afternight04_RapeOrNot

            ############################################################
            ###########################################################
            ##


############################################################
###########################################################

    #HER REACTION:
############################################################
###########################################################

    elif current_pose.id == "pose_3": #POSE 02 no tiene Nipple.

        if mc_body.roll_success == True:

            $ randomnum_1to10 = renpy.random.randint(1, 10)

            if randomnum_1to10 == 1:

                #if current_pose.id == "pose_3":

                    # DIDAC EXPRESSIONS

                d "Uhmm..."

            elif randomnum_1to10 == 2:

                d "Hmm..."

            elif randomnum_1to10 == 3:

                d "Ughmm..."

            elif randomnum_1to10 == 4:

                d "Auhmm..."

            elif randomnum_1to10 == 5:

                d "mmMmf..."

            elif randomnum_1to10 == 6:

                d "Aughmm..."

            elif randomnum_1to10 == 7:

                d "Mmm..."

            elif randomnum_1to10 == 8:

                d "Uhghmm..."

            elif randomnum_1to10 == 9:

                d "Muhfmm..."

            elif randomnum_1to10 == 10:

                d "Hmmm..."


        else: # You failed.

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "¡Tssk!"

            elif randomnum_1to5 == 2:

                d "¿En serio?"

            elif randomnum_1to5 == 3:

                d "¿Te crees que soy una vaca?"

            elif randomnum_1to5 == 4:

                d "¡¿Qué narices haces?!"

            elif randomnum_1to5 == 5:

                d "¡¿Otra mariconada?!"

    ############################################################ # OFF image

                # POSE 01 and POSE 02 are not necessary.

            $ mc_body.store["tongue"] = ""
            show afternight04_sexbattle_mc_tongue empty

            with hpunch

    ############################################################
    ########################################################### # RNipple pose 03 Dialogue.

        $ debug ("HERE GOES DIALOGUE FOR RNipple_Lick pose 03")


        
## TRIES

        if (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) == 0:

            aj "This text should not appear. 5132"


        #if current_girl.total_try == 1:
        if (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) == 1:

            if mc_body.roll_success == True: #You succeded.

                d "..."

            else:

                d "¿Qué demonios te pasa por la cabeza?"

                p "¿Qué pasa ahora?"

                p "¿¿No te gusta que te lamen el pezón o qué?!"

                d "¡¿Me lo has lamido alguna vez?!"

                d "¡¿Verdad que no?!"

                d "¡¿Pues por qué me lo haces ahora?!"

                p "Por que ahora no tienes pectorales,"

                p "¡tienes tetas enormes!"

                p "Y muy bonitas por cierto..."

                d "¡¿Y eso qué tiene que ver?!"

                p "¿Cómo?"

                d "¡Sigo siendo Dídac!"

                p "¡El mismo que me pide que le folle como a una zorra en celo!"

                d "¡Pues haz lo que te pido y no me hagas mariconadas!"

                p "..."

                pt "Habrá que esperar a tenerla más sumisa..."


        elif (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) == 2:

            #if current_girl.roll_success == False: #Wrong
            if mc_body.roll_success == False: #You didn´t succeded.

                if afternight04__RNipple_Lick_Failed == 1:

                    d "¿Otra vez lamiéndome el pezón?"

                    d "¿Te crees que tengo azúcar ahí?"

                    pt "¡¿Es que no tiene sensibilidad en el pezón?!"

                elif afternight04__RNipple_Lick_Failed == 2:

                    d "¿Otra vez?"

                    d "¿Pretendes que tenga un orgasmo así o qué?"

                    p "¿Para qué te sirven unas tetas tan grandes si luego no tienes sensibilidad en los pezones?"

                    d "Tssk..."


        elif (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) == 3:

            if mc_body.roll_success == False: #You didn´t succeded.

                if afternight04__RNipple_Lick_Failed == 1:

                    d "¿Otra vez lamiéndome el pezón?"

                    p "Hasta ahora no te me habías quejado."

                    d "Si te hace ilusión lamer la teta,"

                    d "pues mira..."

                    d "tampoco es algo que me moleste en exceso..."

                    d "pero,"

                    d "¿No te cansas?"

                elif afternight04__RNipple_Lick_Failed >= 2:

                    d "Vamos a ver..."

                    d "¿Esperas que consiga un orgasmo lamiéndome una teta?"

                    p "No es fácil, pero tampoco es imposible."

                    d "..."

                    p "Además,"

                    p "hay algo que se llama preliminares,"

                    p "para ir calentando el terreno."

                    d "¡Como si necesitara ir más caliente de lo que ya estoy!"

                    p "No me seas tan borde,"

                    p "que te volverás una vieja cascarrabias en tres días."

                    d "..."

                    d "Te estás rifando una hostia [protname]."

                elif afternight04__RNipple_Lick_Failed >= 3:

                    d "¡¿Pero quieres dejar de lamerme el puto pezón de una puñetera vez?!"

                    p "..."


        elif (afternight04__RNipple_Lick_Success + afternight04__RNipple_Lick_Failed) >= 4:

            if mc_body.roll_success == False: #You didn´t succeded.

                if afternight04__RNipple_Lick_Failed == 1:

                    d "Mira que eres pesadito con la lengua..."

                    p "Y mira como te ha gustado hasta ahora."

                    d "Tssk..."

                elif afternight04__RNipple_Lick_Failed == 2:

                    d "¿No has pensado que quizás me gustaría más que me follaras,"

                    d "en lugar de estar ahí jugando con el timbre rosado?"

                    p "No te me has quejado demasiado hasta el momento..."

                    d "Tssk..."

                    pt "Quizás sería bueno intentar algo distinto antes de volver a intentarlo."

                elif afternight04__RNipple_Lick_Failed == 3:

                    d "Si tanto te gusta lamer pezones,"

                    d "será mejor que vayas al campo,"

                    d "quizás ahí encuentres alguna vaca y de ahí puedas sacar leche."

                    p "O quizás te dejo preñada"

                    p "y con el tiempo tus pezones saquen leche que puedan servir para amamantarme también..."

                    d "..."

                    p "..."

                    d "¡¿PERO QUE MIERDAS DICES?!"

                    p "..."

                elif afternight04__RNipple_Lick_Failed == 4:

                    d "¿Te imaginas lamiéndome el pezón con mi antiguo cuerpo masculino?"

                    p "..."

                    d "¿Seguirías lamiéndomelo?"

                    p "..."

                    d "No,"

                    d "¿Verdad?"

                    d "Porque nunca antes lo habías hecho..."

                    p "..."

                    d "¡PUES DEJA DE HACERLO AHORA!"

                elif afternight04__RNipple_Lick_Failed == 5:

                    d "¡PERO QUIERES DEJAR DE LAMER EL PUTO PEZÓN DE UNA JODIDA VEZ!"

                elif afternight04__RNipple_Lick_Failed == 6:

                    d "¡Eres un puto pesado!"

                elif afternight04__RNipple_Lick_Failed >= 7:

                    d "..."
        

            #HIS SUCCESS:

        if mc_body.roll_success == True:
            #$ __suffix.append("his_roll")

            #if current_girl.roll_success == False: #Correct #Is that really necessary?
                ##If you success and she fails:

            #if current_girl.repeat == "once":
            if afternight04__RNipple_Lick_Success == 1:
            #if current.girl.repeat == 1:

                #"He passed, she failed. First SUCESS.

                p "Pagece que te gushtag mag de lo que me imaginabga,"

                d "¡No he gemido porque me estuvieras lamiendo el..."

                d "Humm..."

                pt "Ya..."

            elif afternight04__RNipple_Lick_Success == 2:
            #elif current.girl.repeat == 2:

                #"He passed, she failed. Second SUCCESS.

                p "Digrás lo que te deg la ganag,"

                p "Pero tienegs logs pezgones muy sengsibles..."

                d "Idiota..."

                d "Si tuviera los pechos que tenía antes como hombre,"

                d "¡Nunca me hubieras hecho esto!"

                p "Progbablemente no..."

                d "¡Entonces admites que estás haciéndome una mariconada!"

                p "Porgque follargte el cogño cuangdo erags hombre es muuuy heterogsexgual..."

                d "Tssk..."

            elif afternight04__RNipple_Lick_Success == 3:
            #elif current.girl.repeat == 3:

                d "¿No se te cansa la lengua?"

                p "Si nog te gustarag,"

                p "no estariags gimiendo..."

                d "..."

            elif afternight04__RNipple_Lick_Success == 4:
            #elif current.girl.repeat == 4:

                p "Pensabag que hagbías dichog que estog no te gustaríag nadag de nada..."

                d "..."

            elif afternight04__RNipple_Lick_Success == 5:
            #elif current.girl.repeat == 5:

                d "Confieso que no me disgusta..."

                d "Aunque en esta posición,"

                d "no me das lo que te estoy pidiendo realmente."

                p "..."

            elif afternight04__RNipple_Lick_Success == 6:
            #elif current.girl.repeat == 6:

                p "Log disfrugtas,"

                p "y log sabges."

                d "..."

                p "Maricón..."

                d "¡GILIPOLLAS!"

            else:

                #"repeated_lots"

                pt "Aunque ya no le disgusta,"

                pt "quizás sería hora de probar otras alternativas..."

############################################################
########################################################### # BITE RNipple scene.

        # MORDERLE EL PEZÓN? Pregunta.

            pt "Ya que estoy,"

            pt "podría morderle el pezón,"

########################################################### afternight04_probabilty_checking

            call afternight04_probabilty_checking

############################################################

            menu afternight04_Nipple_Lick_Bite_Question:
            
                pt "¿Le causaré daño o placer...?"
                
                "<Morderle el pezón>":
                    
                    call p_Help
                    
                    jump afternight04_Nipple_Lick_Bite_Yes
                
                "Mejor no tentar a la suerte.":
                    
                    call p_Help
                    
                    jump afternight04_Nipple_Lick_Bite_After
############################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    #call afternight04_RapeOrNot ## Not in this case.

    ###########################
    ##########################

    return

########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
#######################################################################################################################
###########################################################
########################################################################################################################
###########################################################
###########################################################



############################################################

label afternight04_Nipple_Lick_Bite_Yes:

    $ afternight04_Nipple_Lick_Bite_Success_Cond = False
    $ randomnum_1to100 = renpy.random.randint(1, 100)

############################################################ afternight04_probabilty_checking02

    call afternight04_probabilty_checking02

############################################################
############################################################

    # IMAGE BITING Right Nipple.

    $ afternight04__prehfix_RNipple_Lick = False

    show afternight04_sexbattle_mc_tongue empty
    with hpunch

##############################################################
#############################################################

    if afternight04_Nipple_Lick_Bite_Success_Cond == True: #You succeded BITING.

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡AuMhhhm...!"

        elif randomnum_1to5 == 2:

            d "¡AAhmmm...!"

        elif randomnum_1to5 == 3:

            d "¡UMffhmm...!"

        elif randomnum_1to5 == 4:

            d "¡Ahffhm...!"

        elif randomnum_1to5 == 5:

            d "¡AUhfmm...!"

    else: # You Failed Biting

        ## SCREAMS

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¡¡AU!!"

        elif randomnum_1to5 == 2:

            d "¡¡OUCH!!"

        elif randomnum_1to5 == 3:

            d "¡¡AAAI!!"

        elif randomnum_1to5 == 4:

            d "¡¡AAAH!!"

        elif randomnum_1to5 == 5:

            d "¡¡COÑO!!"

        ## NEGATIVE REACTIONS

        if afternight04_Nipple_Lick_Bite_Failed == 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

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

            if randomnum_1to10 == 1:

                d "¡¿Otra vez?!"

            elif randomnum_1to10 == 2:

                d "¡¿Es que me quieres arrancar el pezón de un bocado?!"

            elif randomnum_1to10 == 3:

                d "¡¿Te crees que soy maricón?!"

            elif randomnum_1to10 == 4:

                d "¡Te voy a tirar ácido sulfúrico por tus pezones al final!"

            elif randomnum_1to10 == 5:

                d "¡Me vas a hacer sangre!"

            elif randomnum_1to10 == 6:

                d "¡¿Quieres que te meta yo un bocado en los huevos?!"

            elif randomnum_1to10 == 7:

                d "¡Al final te voy a arrancar el pezón con pinzas!"

            elif randomnum_1to10 == 8:

                d "¡¿Quieres que vaya a buscar la batería de un coche para electrocutar tus putos pezones??!"

            elif randomnum_1to10 == 9:

                d "¡¿Por qué coño me muerdes?!"

            elif randomnum_1to10 == 10:

                d "¡Te voy arrancar la piel a tiras!"


##############################################################

############################################################
############################################################
### Dialogues of Failed:

    if afternight04_Nipple_Lick_Bite_Success_Cond == False:

        $ current_girl.pleasure -= 3
        $ current_girl.enslavement -= 1

        if afternight04_Nipple_Lick_Bite_Failed == 1:

            d "¡¿Por qué coño me muerdes el pezón de las narices?!"

            p "Me dirás que no te ha gustado..."

            d "¡Claro que no me ha gustado!"

            d "¡Duele!"

            d "¡¿Sabes?!"

            d "¡¿Quieres que muerda yo el tuyo?!"

            p "No creo que me lo mordieras igual que yo..."

            d "¡Deja mi pezón en paz!"

            p "..."

        elif afternight04_Nipple_Lick_Bite_Failed == 2:

            d "¡¿Pero qué coño pasa contigo?!"

            d "¡¿Por qué diablos me vuelves a morder el jodido pezón?!"

            d "¡¿No te basta solo con lamerlo?!"

            d "Encima tienes que morderlo..."

            d "¡como si fuera una puta vaca!"

            p "..."

            pt "¿Una vaca?"

        elif afternight04_Nipple_Lick_Bite_Failed == 3:

            d "¡Ya es la tercera vez que me haces daño!"

            if afternight04_Nipple_Lick_Bite_Success >= 5:

                $ current_girl.enslavement += 1

                p "Sí,"

                p "pero te he visto disfrutarlo muchas más veces que no quejarte..."

                d "..."

            elif (afternight04_Nipple_Lick_Bite_Success in range (1, 4)):

                $ current_girl.enslavement -= 1
                $ current_girl.pleasure -= 3

                p "Sí,"

                p "pero ha habido algunas mordidas que te han gustado bastante..."

                d "¡¿Algunas?!"

                d "¡¿Y esa es tu maldita excusa?!"

            else:

                $ current_girl.enslavement -= 3
                $ current_girl.pleasure -= 6

                p "..."

                d "Y no..."

                d "¡No lo he disfrutado ni una sola vez!"

            if afternight04_Nipple_Lick_Bite_Success >= 5:

                d "Idiota..."

            else:

                d "¡Deja mi pezón en paz!"

        elif afternight04_Nipple_Lick_Bite_Failed == 4:

            d "¡Maldita sea [protname]!"

            d "¡¿Acaso quieres hacerme sangrar?!"

            p "Eres un exagerado..."

            d "Y tú un jodido imbécil."

            d "¡No me muerdas más!"

        elif afternight04_Nipple_Lick_Bite_Failed == 5:

            d "¡Eres un puto sádico!"

            d "¡¿Cuantas veces me has mordido ya el jodido pezón de las narices?!"

            d "¡Al final voy a retorcerte el pezón hasta arrancártelo!"

        elif afternight04_Nipple_Lick_Bite_Failed == 6:

            d "¡¿Te mola verme gritar de dolor?!"

            d "¡¿O qué pasa contigo?!"

        elif afternight04_Nipple_Lick_Bite_Failed == 7:

            d "¡JODER!"

            d "¿¡Cuantas veces me has hecho daño ya?!"

            if afternight04_Nipple_Lick_Bite_Success > afternight04_Nipple_Lick_Bite_Failed:

                $ current_girl.enslavement += 1

                p "En realidad,"

                p "lo has disfrutado más veces de las que te has quejado."

                d "..."

                d "¿Esa es tu excusa...?"

                d "¡Me has oído gritar de dolor siete cochinas veces!"

                d "¡¿Hasta cuando esperas dejar de morderme el jodido pezón?!"

            else:

                if afternight04_Nipple_Lick_Bite_Success > 0:

                    $ current_girl.enslavement -= 1
                    $ current_girl.pleasure -= 3

                    p "Te he oído alguna que otra vez gemir de placer por morderte..."

                    d "..."

                    d "¿Y cuantas me has oído gritar de dolor?"

                    p "..."

                    d "Más..."

                    d "¿Verdad?"

                    p "..."

                    d "¡¡PUES PARA DE UNA PUTA VEZ!"

                else:

                    $ current_girl.enslavement -= 3
                    $ current_girl.pleasure -= 6

                    p "..."

                    d "¡NO ME HA GUSTADO NI PUTA JODIDA VEZ!"

                    d "¡¡DEJA MI PUTO PEZÓN EN PAZ DE UNA PUTA JODIDA VEZ!!"

        elif afternight04_Nipple_Lick_Bite_Failed >= 8:

            $ current_girl.enslavement -= 3
            $ current_girl.pleasure -= 6

            d "..."


############################################################
### Dialogues of Success

    elif afternight04_Nipple_Lick_Bite_Success_Cond == True:

        $ current_girl.pleasure += 2
        $ current_girl.enslavement += 3

        if afternight04_Nipple_Lick_Bite_Success == 1:

            d "¡¿Qué diablos?!"

            d "¡¿Por qué demonios me muerdes el pezón?!"

            p "¿Y tú por qué gimes de esa manera cuando te lo muerdo,"

            p "después de estar pasándole la lengua todo este rato?"

            d "..."

            p "No sé,"

            p "digo yo que quizás,"

            p "solo quizás,"

            p "no te ha disgustado tanto..."

            d "Tssk..."

        elif afternight04_Nipple_Lick_Bite_Success == 2:

            d "¡¿Otra vez mordiéndome el pezón?!"

            d "¡¿Te crees que es un biberón?!"

            p "Deja de gemir y no te volveré a morder."

            if afternight04_Nipple_Lick_Bite_Failed > 7:

                d "¡¿Estás de coña?!"

                d "¡Me he quejado más veces de las que soy capaz de contar!"

                p "Pero esta vez no te ha disgustado..."

                d "..."

                d "¡¿Te crees que soy una rata de laboratorio?!"

                d "No hagas que pierda la paciencia..."

                pt "Quizás sí que le he hecho más daño que placer hasta ahora..."

            elif (afternight04_Nipple_Lick_Bite_Failed in range (3, 7)):

                d "¡Ya me he quejado más de tres veces antes!"

                d "¡¿No te parece suficiente?!"

                p "En realidad,"

                extend " no."

                p "Me da la sensación que cada vez te va gustando más..."

                d "..."

                d "Háztelo mirar..."

            else:

                $ current_girl.enslavement += 1

                d "..."

                d "Tssk..."

        elif afternight04_Nipple_Lick_Bite_Success == 3:

            d "..."

            d "¡¿Por qué cojones gimo cuando me muerdes?!"

            p "Eso..."

            p "Solo puedes respondértelo tú mismo..."

            d "..."

            d "¿Lo he dicho en voz alta?"

            p "Euh..."

            p "Sí."

            d "..."

            d "Tssk..."

        elif afternight04_Nipple_Lick_Bite_Success == 4:

            p "¿Por qué no admites que te está gustando más de lo que eres capaz de confesar?"

            d "..."

            d "¡¿Se puede saber qué mierda de retorcido placer te da a ti morderme el jodido pezón?!"

            p "Esta misma cara que pones es mi mayor recompensa."

            d "..."

            d "Gilipollas..."

        elif afternight04_Nipple_Lick_Bite_Success == 5:

            p "Ese gemido no ha sido de dolor precisamente..."

            d "..."

            p "Y ya llevas cinco así..."

            if afternight04_Nipple_Lick_Bite_Failed >= 6:

                d "¡Pero llevo bastantes más gritándote de dolor y tú sigues insistiendo!"

                p "..."

                d "¡GILIPOLLAS!"

                pt "Tiene algo de razón..."

            elif afternight04_Nipple_Lick_Bite_Failed == 5:

                d "¡La misma cantidad de veces que llevo gritándote de dolor,"

                d "y a ti te da completamente igual!"

                p "..."

                d "Tssk..."

            elif (afternight04_Nipple_Lick_Bite_Failed in range (1, 4)):

                d "También llevo algunos gritos de dolor,"

                d "por si no lo has notado."

                p "Humm..."

                p "Pero creo que esos intentos han valido la pena,"

                p "para ahora verte gozar así."

                d "..."

                d "¡¿Te muerdo yo docenas de veces a ver si luego empiezas a disfrutarlo?!"

                p "Yo no te lo he prohibido en ningún momento."

                d "..."

                d "Eres un imbécil."

            if afternight04_Nipple_Lick_Bite_Failed == 0:

                d "¿Cinco veces...?"

                p "Y no te me has quejado ni una sola vez."

                d "¡¿Qué?!"

                d "No..."

                p "Y esa cara teniéndote a cuatro patas,"

                p "la verdad es que me pone bastante..."

                d "..."

                d "..."

                $ current_girl.pleasure += 2
                $ current_girl.enslavement += 3

        elif afternight04_Nipple_Lick_Bite_Success == 6:

            p "No veo que te quejes precisamente..."

            d "Si sigues aparte de que se me está volviendo como un tomate,"

            d "me vas a sacar sangre al final."

            p "Eres un exagerado."

            d "Ya..."

            pt "Lo que sí es verdad es que ya no le afecta del mismo modo que antes..."

            pt "Sería buena idea ir cambiando de táctica,"

            pt "o se me volverá a poner encima..."

        elif afternight04_Nipple_Lick_Bite_Success >= 7:

            d "..."


############################################################
    jump afternight04_Nipple_Lick_Bite_After #End of BITE.

label afternight04_Nipple_Lick_Bite_After:

############################################################
###########################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return


############################################################
###########################################################
############################################################
###########################################################
############################################################
###########################################################
############################################################
###########################################################
############################################################
###########################################################

transform afternight04_sexbattle_mc_tongue_nippleR_pose_c:
    xanchor -1.5 yanchor -0.43 rotate 0

image afternight04_sexbattle_mc_tongue nippleR_anim_c:

    contains:
        "afternight04_sexbattle_mc_tongue nippleR_down_c"
        afternight04_sexbattle_mc_tongue_nippleR_pose_c
        block:
            alpha 1.1
            easeout_quad 0.3 alpha 0.0
            pause 0.3
            easein_quad 0.3 alpha 1.1
            repeat

    contains:
        "afternight04_sexbattle_mc_tongue nippleR_med_c"
        afternight04_sexbattle_mc_tongue_nippleR_pose_c
        block:
            alpha 0.0
            easein_quad 0.3 alpha 1.1
            easeout_quad 0.3 alpha 0.0
            pause 0.3
            repeat

    contains:
        "afternight04_sexbattle_mc_tongue nippleR_up_c"
        afternight04_sexbattle_mc_tongue_nippleR_pose_c
        block:
            alpha 0.0
            pause 0.3
            easeout_quad 0.3 alpha 1.1
            easeout_quad 0.3 alpha 0.0
            repeat