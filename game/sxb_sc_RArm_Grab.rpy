label RArm_Grab:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.90.00") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "RArm_Grab."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["right_hand"] = "RArm_Grab"

    else:

        $ mc_body.store["right_hand"] = "RArm_Grab"

#########################################################

    $ afternight04__prehfix_RArm_Grab = True
    $ afternight04__a_prehfix_RArm_Grab = True

    $ debug ("Arm Grabbed.")
    
    call afternight04_sex_check_before
    
    label .manager:

        $ afternight04__RArm_Grab_Done += 1

        if mc_body.roll_success:
            $ afternight04__RArm_Grab_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__RArm_Grab_Failed += 1

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
        $ debug ("First Orgasm for his. Grabbing her Arm.")

        call afternight04_RArm_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Grabbing her Arm.")

        call afternight04_RArm_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Grabbing her Arm.")

        call afternight04_RArm_Grab_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Grabbing her Arm.")

        call afternight04_RArm_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Grabbing her Arm.")

        call afternight04_RArm_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Grabbing her Arm.")

        call afternight04_RArm_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RArm_Grab_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Grabbing her Arm.")

        call afternight04_RArm_Grab

        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Grabbing her Arm.")

        call afternight04_RArm_Grab
        
        jump expression __prefix + "call_screen"


#########################################################################################################################
########################################################################################################################
#######################################################################################################################
#ORGASMS


    label afternight04_RArm_Grab:

        call afternight04_Arm_Grab

        return

    #############
    ############
    ## ORGASMS

    label afternight04_RArm_Grab_his_orgasm:

        call afternight04_Arm_Grab

        call afternight04_mostly_his_orgasm

        return


    label afternight04_RArm_Grab_her_orgasm:

        call afternight04_Arm_Grab

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################

label afternight04_Arm_Grab:

#################################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["tongue"] = ""
        show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_mc_tongue_pussy empty

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness
        
        show afternight04_sexbattle_mc_handR grab_arm_action_a
        with hpunch

#################################################################

##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        #$ afternight04__a_prehfix_LArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        $ afternight04__a_prehfix_LButtock_Slap = False
        
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        #$ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        $ afternight04__a_prehfix_RButtock_Massage = False
        $ afternight04__a_prehfix_RButtock_Slap = False
        
        $ afternight04__a_prehfix_RLeg_Massage = False
        $ afternight04__a_prehfix_RNipple_Pinch = False


    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    $ afternight04__a_prehfix_MClitoris_Massage = False

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

    if current_pose.id == "pose_1":

        if current_girl.total_try == 1: #Don´t change that.

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            d "¡¿Qué?!"

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 00_a
            show afternight04_sexbattle_d_pupils front00_a
            show afternight04_sexbattle_d_eyebrows normal_a
            with dissolve

            p "Ahora me toca a mi."

            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            n "Agarrándola con fuerza por el brazo,"

        elif current_girl.total_success == 2:

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows normal_a
            with dissolve

            d "¡¿Otra vez?!"

            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "[protname],"

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "al final te voy a..."

        elif current_girl.total_success == 3:

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Serás capaz..."

        elif current_girl.total_success == 4:

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Al final pensaré que te gusta tenerme a cuatro patas..."

            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows sadx02_a
            with dissolve

            d "Enfermo mental..."

        elif current_girl.total_success == 5:

            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            d "Podrías ser un poco más delicado esta vez..."

            show afternight04_sexbattle_d_mouth sad_Talkingx01_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            p "Nop."

        elif current_girl.total_success == 6:

            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

            d "¡¿Es que no te gusta tenerme encima?!"

        elif current_girl.total_success == 7:

            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

            d "¡Por lo menos espero que lo hagas mejor que la última vez!"

        elif current_girl.total_success >= 8:

            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

            d "Tsssk..."

###################################

    elif current_pose.id == "pose_2":

        if current_girl.total_success == 1: # Don´t change that.

            d "¿¡Y ahora qué...?!"

        elif current_girl.total_success == 2:

            d "¡Déjame el brazo en paz!"

        elif current_girl.total_success == 3:

            d "¡¿Por qué tienes qué cogerme del brazo ahora?!"

        elif current_girl.total_success == 4:

            d "¡¿Es que no te gustó a cuatro patas?!"

            p "Me gusta mirarte a la cara mientras te follo bien duro..."

            d "..."

        elif current_girl.total_success == 5:

            d "¡Me estás dando más vueltas que una peonza!"

        elif current_girl.total_success == 6:

            d "¡¿Me vas a dejar de marear de una vez?!"

        elif current_girl.total_success == 7:

            d "¡Coño!"

        elif current_girl.total_success >= 8:

            d "..."

###################################

    elif current_pose.id == "pose_3":

        if current_girl.total_try == 1: # Don´t change that.

            d "¿¡Y ahora?!"

        elif current_girl.total_success == 2:

            d "¡¿Para qué me has girado entonces?!"

        elif current_girl.total_success == 3:

            d "Eres un mierdas..."

        elif current_girl.total_success == 4:

            d "¡Me estás volviendo loca!"

        elif current_girl.total_success == 5:

            d "¡Al final me vas a marear!"

        elif current_girl.total_success == 6:

            d "¡Lo que te haría si el que tuviera pene fuera yo!"

            p "Pero no lo tienes..."

            d "No tienes ni idea de las cosas que me he comprado..."

            p "..."

        elif current_girl.total_success == 7:

            d "¡Me cago en...!"

        elif current_girl.total_success >= 8:

            d "..."


    # HIS SUCCESS:

#################################################################

    # Not success is necessary here.
    if current_pose.id == "pose_3":

        #################################################################

        $ current_pose = pose_2
        $ current_pose.id = "pose_2"

        $ afternight04_SheRapingYou = False
        #scene d_pose03
        call afternight04_sexbattle_pose_b

        call afternight04_Arm_Grab_Moans

        #################################################################

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        # These DON´T need expressions.

        if randomnum_1to5 == 1:

            d "¡Ugh!"

        elif randomnum_1to5 == 2:

            d "¡Humpf!"

        elif randomnum_1to5 == 3:

            d "¡Ouh!"

        elif randomnum_1to5 == 4:

            d "¡Ey!"

        elif randomnum_1to5 == 5:

            d "¡Serás!"

        ######

        if current_girl.total_try == 1:

            n "Sueltas su brazo, haciendo caer su cuerpo y su rostro de nuevo sobre el blando sofá."

            d "¡¿Ya te has cansado de aguantarme el brazo?!"

            p "Me gusta verte sumisa a cuatro patas."

            p "Además,"

            extend " así tengo esta mano libre para magrearte y azotarte a gusto."

            d "..."

            d "Gilipollas..."

        elif current_girl.total_try == 2:

            d "¿¡Para qué diablos me agarraste el brazo si ahora decides soltarlo?!"

            p "Para darte una cachetada bien fuerte en esta nalga, que se siente solitaria..."

            d "..."

            p "Es broma..."

            p "O quizás no..."

            d "Idiota."

        elif current_girl.total_try == 3:

            d "Tssk..."

            p "¿Ya no me dices nada de porqué te suelto el brazo?"

            d "¿Para qué?"

            d "Acabas haciendo lo que te da la jodida gana..."

            p "Eso es verdad."

            d "..."

        #elif current_girl.total_try == 4:
        #elif current_girl.total_try == 5:

        else:

            d "..."

        return

#################################################################
#################################################################

    if mc_body.roll_success:
        #$ __suffix.append("his_roll")

        if current_pose.id == "pose_1":

            ## MESSAGE to advice WORK IN PROGRESS

            call afternight04_sexbattle_pose_b_WIP

            #################################################################

            #$ current_pose.id = current_girl.switch_pose("pose_2")
            $ current_pose = pose_2
            $ current_pose.id = "pose_2"

            $ afternight04_SheRapingYou = False

            #scene d_pose02
            call afternight04_sexbattle_pose_b

            call afternight04_Arm_Grab_Moans

            #################################################################

            #if afternight04__RArm_Grab_Success == 1:
            if current_girl.total_success == 1:

                n "Consigues darle la vuelta y ponerla a cuatro patas sobre el sofá."

                d "¡¿Se puede saber qué haces gilipollas?!"
                
                p "No te quejes tanto..."

                p "Ya verás como te va a gustar..."

                d "..."

                d "Más te vale..."

            elif current_girl.total_success == 2:

                d "¡¿Otra vez?!"

                p "Por mucho que te empeñes en negarlo."

                p "A cuatro patas lo disfrutas mucho más."

                d "..."

                d "Estás jugando con un hielo muy delgado [protname]..."

                pt "Está claro que si hago algo que no le gusta demasiado,"

                pt "se volverá a poner encima de mí."

            elif current_girl.total_success == 3:

                d "Podrías ser algo más delicado al voltearme..."

                p "Lo dice la chica que ya me ha violado varias veces."

                d "¡Porque no me estás follando como deberías!"

                p "Porque quieres ser tratada como una perra en celo."

                p "Y eso es lo que voy a hacer."

                d "..."

                d "Gilipollas..."

            elif current_girl.total_success == 4:

                d "Eres un cabrón retorcido."

                p "Y tú una ninfómana insaciable."

                d "..."

            elif current_girl.total_success == 5:

                d "Espero que esta vez valga la pena el tenerme a cuatro patas..."

                d "O te volveré a cabalgar sin contemplaciones..."

                p "Si en el fondo te gusta sentirte sumisa."

                d "..."

            elif current_girl.total_success == 6:

                d "No te cansas..."

                p "Sabes que te gusta..."

                d "..."

            else:

                d "..."


#################################################################

        elif current_pose.id == "pose_2":

            #################################################################

            $ current_pose = pose_3
            $ current_pose.id = "pose_3"

            $ afternight04_SheRapingYou = False
            #scene d_pose03
            call afternight04_sexbattle_pose_c

            call afternight04_Arm_Grab_Moans

            #################################################################

            if current_girl.total_success == 1:

                n "Agarrándola por el brazo,"

                n "consigues que deje de ocultar su rostro en el sofá"

                n "y la tengas en frente mientras la sigues teniendo a cuatro patas."

                d "¡¿Qué diablos haces [protname]?!"

                p "Si tengo que follarte,"

                p "prefiero ver la cara de zorra que pones cuando te la estoy metiendo hasta el fondo."

                d "..."

                d "Idiota..."

            elif current_girl.total_success == 2:

                d "¡¿Otra vez?!"

                d "Me puedes follar igualmente sin cogerme del brazo..."

                p "Pero me gusta mirarte a la cara te estoy dando bien duro..."

                d "Gilipollas."

            elif current_girl.total_success == 3:

                d "Eres un idiota."

                p "Y tu una cachonda perdida que no puede disimularlo facialmente,"

                p "y me encanta."

                d "Tsk..."

            elif current_girl.total_success == 4:

                d "Podrías ser más delicado."

                p "Eres tú quien me obliga a ser una bestia."

                p "Y sabes que te gusta."

                d "..."

            #elif current_girl.total_success == 5:

            #elif current_girl.total_success == 6:

            else:

                d "..."


#################################################################

    else: #If you Fail.

        if current_pose.id == "pose_1":

            if current_girl.total_fail == 1:
            #if afternight04__Remove_Success + afternight04__Remove_Failed == 1:

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

                d "¡Ey!"

                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                d "¡¿Qué demonios haces?!"

                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

                p "..."

                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

                d "¡Me estás haciendo daño imbécil!"

                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                show afternight04_sexbattle_mc_handR empty
                with hpunch

                d "¡Quita coño!"

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                pt "Mierda..."

                pt "No está lo suficientemente cachonda como para quitármela de encima y ponerla a cuatro patas..."

            elif current_girl.total_fail == 2:
            #elif afternight04__Remove_Success + afternight04__Remove_Failed == 2:

                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "..."

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "¡Te he dicho que me dejes el puto brazo en paz!"

                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 035_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                d "¡¿Aún no te ha quedado claro?!"

                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                pt "Así solo conseguiré que se cabree más..."

                pt "Si consiguiera ponerla más a tono,"

                pt "es probable que cediera con más facilidad..."

            elif current_girl.total_fail == 3:

                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "Gilipollas..."

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

                d "Eres más pesado que las piedras."

                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "Me gusta estar encima de ti,"

                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "así que por ahora no voy a dejarte cambiar de posición."

                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                d "¿Queda claro?"

                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            elif current_girl.total_fail >= 4:

                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

                d "..."

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    d "¡Déjalo ya!"

                elif randomnum_1to5 == 2:

                    d "¡Eres un jodido pesado!"

                elif randomnum_1to5 == 3:

                    d "¡Suéltame de una vez!"

                elif randomnum_1to5 == 4:

                    d "¡¿Por qué demonios insistes en agarrarme el jodido brazo?!"

                elif randomnum_1to5 == 5:

                    d "¡Pesado!"

                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

        elif current_pose.id == "pose_2":

            if current_girl.total_fail == 1:

                d "¡¿Será posible?!"

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                d "¡Encima de que me tiras de malas maneras sobre el sofá para ponerme a cuatro patas como si fuera un perro!"

                d "¡¿Vuelves a agarrarme el brazo de nuevo?!"

                d "¡¿Te crees que soy un juguete?!"

                p "Solo quiero verte la cara mientras te follo."

                d "..."

                d "Me importa una mierda."

                pt "Voy a tener que calentarla más si quiero conseguir que me mire mientras la follo."

            elif current_girl.total_fail == 2:

                d "¡Maldita sea!"

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                d "¡No quiero que me mires el careto!"

                p "..."

            else:

                d "..."

                show afternight04_sexbattle_mc_handR empty
                with hpunch

                pt "Será mejor esperar a que sea un poco más sumisa..."


        elif current_pose.id == "pose_3": #This should not exist, it should be free to allow him left your hand.

            $ debug ("ERROR. This should not exist, it should be free to allow him left your hand. 2567")

#################################################################

        if current_girl.enslavement in range (0, 45):

            pt "Está claro que aún estoy muy lejos de conseguirlo..."

        elif current_girl.enslavement in range (46, 80):

            pt "Aunque cada vez estoy más cerca de conseguirlo..."

        elif current_girl.enslavement >= 81:

            pt "A estas alturas no me tendría que resultar complicado someterla..."

        pt "Podría forzarla..."

        pt "pero eso sería peor con el humor de perros que tiene..."


################################################################# # REMOVE

    if mc_body.roll_success:

        #if current_pose.id == "pose_1": # THERE´S NO NEED FOR POSE 01

        if current_pose.id == "pose_2":

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty
            with dissolve

        #if current_pose.id == "pose_3": # YOU MUST KEEP THE HAND ON THE POSE 03


#################################################################

    ###########################
    ########################## # nly if you fail in this case.

    ### RAPE OR NOT?

    call afternight04_RapeOrNot

    ###########################
    ##########################

    return




#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################
##
##
#################################################################
#################################################################
#################################################################
#################################################################
#################################################################

label afternight04_Arm_Grab_Moans:

    $ randomnum_1to10 = renpy.random.randint(1, 10)

    if randomnum_1to10 == 1:

        #if current_pose.id == "pose_3": # Pose 1 has no expressions.

            # EXPRESSIONS

        d "¡AU!"

    elif randomnum_1to10 == 2:

        d "¡AI!"

    elif randomnum_1to10 == 3:

        d "¡OU!"

    elif randomnum_1to10 == 4:

        d "¡AUCH!"

    elif randomnum_1to10 == 5:

        d "¡UGH!"

    elif randomnum_1to10 == 6:

        d "¡JODER!"

    elif randomnum_1to10 == 7:

        d "¡CON MÁS CALMA!"

    elif randomnum_1to10 == 8:

        d "¡LA MADRE QUE TE...!"

    elif randomnum_1to10 == 9:

        d "¡CABRÓN!"

    elif randomnum_1to10 == 10:

        d "¡HIJO DE...!"

    return


#######################################################
###################################################### # Message for Work In Progress for DoggyStyle of Didac, Pose 02 and 03.

label afternight04_sexbattle_pose_b_WIP:

    show afternight04_sexbattle_effects black
    
    show afternight04_sexbattle_d_mouth sad_Silentx03_a
    show afternight04_sexbattle_d_eyes 05_a
    show afternight04_sexbattle_d_pupils front05_a
    show afternight04_sexbattle_d_eyebrows angryx01_a

    hide screen premium_dashboard

    with Dissolve (1.0)

    aj2 " La posición a cuatro patas de Dídac

        \nsigue estando en proceso.
        
        \n\nMi recomendación es que aún no lo juegues.

        \n\nPero si aún así sientes curiosidad,

        \npuedes acceder a él.

        \n\nPero ten en cuenta que estará lleno de errores.

        \n\nY tardaré en terminarlo..."

    show afternight04_sexbattle_effects empty
    with dissolve

    menu afternight04_sexbattle_pose_b_WIP_question:

        "<Ponerla a cuatro patas>":

            call p_Help

            return

        "<Prefiero esperar a que esté más terminado>":

            call p_Help

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty
            with dissolve

            if PlatinumHelp:
                show screen premium_dashboard()
            call screen dummy_screen()
            

#######################################################
######################################################