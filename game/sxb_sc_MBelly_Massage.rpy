label MBelly_Massage:

######################################################### Dummy_Screen Calls

    if afternight04_CumOnStomach >= 1:

        call afternight04_WantTouchBellyCumNOT_MBelly_Massage

        call screen dummy_screen()

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.05") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "MBelly_Massage."

#########################################################

    $ mc_body.store["left_hand"] = "MBelly_Massage"

#########################################################
    
    $ afternight04__prehfix_MBelly_Massage = True
    $ afternight04__a_prehfix_MBelly_Massage = True

    #if afternight04_CumOnStomach >= 1:
        #$ afternight04__prehfix_MBelly_Massage = False
        #$ mc_body.roll_success = False

    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__MBelly_Massage_Done += 1

        if mc_body.roll_success:
            $ afternight04__MBelly_Massage_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__MBelly_Massage_Failed += 1

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
        $ debug ("First Orgasm for his. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_MBelly_Massage_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Massaging her Belly Button with your Left Hand.")

        call afternight04_MBelly_Massage
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04_MBelly_Massage:

        call afternight04_MBelly_Massage_general

        return

    label afternight04_MBelly_Massage_his_orgasm:

        call afternight04_MBelly_Massage_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04_MBelly_Massage_her_orgasm:

        call afternight04_MBelly_Massage_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################

label afternight04_MBelly_Massage_general:

    if afternight04_CumOnStomach == 0:

    ##############################################################
    #############################################################

        show afternight04_sexbattle_mc_handL massage_belly_action_a
        with dissolve

    ##############################################################
    ############################################################# # Her reaction is not necessary.

    ##############################################################
    #############################################################

## SUCCESS

        #No need for pose 01 conditional, since this button only exist in position 01.
        #if pose01_belly.get_action("MBelly_Massage").times_done == 1:
        if (afternight04__MBelly_Massage_Success + afternight04__MBelly_Massage_Failed) == 1:

            #if mc_body.roll_success == True: # Necessary? I don´t think so.

            $ current_girl.enslavement += 1 # POINTS

            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "Ugh..."

            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
            with dissolve

            d "¿Qué...?"

            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Para..."

            show afternight04_sexbattle_d_mouth happy_Talkingx06_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows normal_a
            with dissolve

            d "Jajajaja..."

            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡Para de una vez!"

            show afternight04_sexbattle_d_mouth happy_Talkingx07_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            d "Jajajaja"

            show afternight04_sexbattle_d_mouth sad_Talkingx08_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            
            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

            d "¡Que pares!"

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡Ya sabes que tengo cosquillas en el ombligo!"

            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡No me toques más ahí!"

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            p "..."

        elif (afternight04__MBelly_Massage_Success + afternight04__MBelly_Massage_Failed) == 2:

            $ current_girl.enslavement += 1 # POINTS

            show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "Ugh..."

            show afternight04_sexbattle_d_mouth happy_Talkingx08_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows surprisex02_a
            with dissolve

            d "Jajajaja"

            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "¡¡Quieres parar...?!"

            show afternight04_sexbattle_d_mouth sad_Talkingx09_a
            show afternight04_sexbattle_d_eyes 00_a
            show afternight04_sexbattle_d_pupils front00_a
            show afternight04_sexbattle_d_eyebrows angryx03_a

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

            d "¡Para!"

            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡No me seas tocacojones!"

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            pt "Quizás le estoy tocando las narices,"

            pt "pero así consigo controlar mejor la situación..."

        elif afternight04__MBelly_Massage_Success >= 3:

            $ current_girl.enslavement += 1 # POINTS

            show afternight04_sexbattle_d_mouth happy_Talkingx08_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows surprisex02_a
            with dissolve

            d "Jajajaja"

            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows angryx02_a

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

            d "¡Te voy a reventar los huevos!"

            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡Deja el puto ombligo en paz!"

            show afternight04_sexbattle_d_mouth sad_Silentx06_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            pt "Quizás sea buena idea dejarlo así,"

            pt "o al final conseguiré el efecto contrario..."

## Fail is still ELIF.

        #elif pose01_belly.get_action("MBelly_Massage").times_failed == 1:
        elif afternight04__MBelly_Massage_Failed == 1:

            $ current_girl.enslavement -= 1 # POINTS

            show afternight04_sexbattle_d_mouth happy_Talkingx08_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows surprisex02_a
            with dissolve

            d "Jajajaja"

            show afternight04_sexbattle_d_mouth sad_Talkingx08_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows angryx03_a

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

            d "¡PARA YA!"

            show afternight04_sexbattle_d_mouth sad_Silentx07_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

            pt "Me da la sensación que ahora estoy consiguiendo el efecto contrario..."

        elif afternight04__MBelly_Massage_Failed >= 2:

            $ current_girl.enslavement -= 1 # POINTS

            show afternight04_sexbattle_d_mouth happy_Talkingx08_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows surprisex02_a
            with dissolve

            d "Jajajaja"

            show afternight04_sexbattle_d_mouth sad_Talkingx09_a
            show afternight04_sexbattle_d_eyes 00_a
            show afternight04_sexbattle_d_pupils front00_a
            show afternight04_sexbattle_d_eyebrows angryx04_a

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            with hpunch

            d "{size=30}¡PARA YA!{/size}"


        ###########################
        ##########################

        ### RAPE OR NOT?

        call afternight04_RapeOrNot

        ###########################
        ########################## # SPECIAL taking in mind the CUM on belly.

    else:

        aj "THIS TEXT SHOULD NOT BE READABLE. 5595"

    return

label afternight04_WantTouchBellyCumNOT_MBelly_Massage:

    $ afternight04_WantTouchBellyCum += 1
    $ mc_body.roll_success = False

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx05_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils front04_a
        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
        with dissolve

    if afternight04_WantTouchBellyCum == 1:

        pt "¿En serio?"

        pt "No quiero tocar su ombligo teniendo tanta lefa cerca..."

        pt "¿Por qué diablos querría hacer eso?"

    elif afternight04_WantTouchBellyCum == 2:

        pt "¡Joder!"

        pt "¡Que la lechada sigue ahí"

        pt "¡Ni de coña!"

    elif afternight04_WantTouchBellyCum == 3:

        pt "¡Que no!"

        pt "¡No pienso pringarme con ese pastizal!"

    else:

        pt "¡¿Otra vez insisto en lo mismo?!"

        pt "¡¿Es que hay alguien que controla lo que hago?!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx04_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx02_a
        with dissolve

    return


