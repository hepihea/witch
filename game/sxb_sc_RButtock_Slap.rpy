label RButtock_Slap:

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.02") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

######################################################### Dummy_Screen Calls

    if current_pose.id == "pose_1":

        call afternight04__LButtock_Slap_Pose01

######################################################### Dummy_Screen Calls

    #if afternight04_SheRapingYou == True: #Not necessary.

        #call afternight04_SheRapingYou_NotAllowed

#########################################################

    $ __suffix = []
    $ __prefix = "RButtock_Slap."

#########################################################

    if current_pose.id == "pose_1":

        $ mc_body.store["left_hand"] = "RButtock_Slap"

    else:

        $ mc_body.store["right_hand"] = "RButtock_Slap"

#########################################################
        
    $ afternight04__prehfix_RButtock_Slap = True
    $ afternight04__a_prehfix_RButtock_Slap = True

    call afternight04_sex_check_before

    label .manager:

        if not current_pose.id == "pose_1":

            $ afternight04__RButtock_Slap_Done += 1

            if mc_body.roll_success:
                $ afternight04__RButtock_Slap_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__RButtock_Slap_Failed += 1

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
        $ debug ("First Orgasm for his. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04_RButtock_Slap_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap 
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Slapping her Right Buttock.")

        call afternight04_RButtock_Slap  
        
        jump expression __prefix + "call_screen"

####################################
###################################

    label afternight04_RButtock_Slap:

        call afternight04_Buttock_Slap

        return

    label afternight04_RButtock_Slap_his_orgasm:

        call afternight04_Buttock_Slap

        call afternight04_mostly_his_orgasm

        return

    label afternight04_RButtock_Slap_her_orgasm:

        call afternight04_Buttock_Slap

        call afternight04_mostly_her_orgasm

        return


####################################
###################################
####################################
###################################
####################################
###################################


label afternight04_Buttock_Slap:

    #################################################################################################################
    #################################################################################################################

    # You can´t at same time.

    #################################################################################################################
    #################################################################################################################

####################################
###################################
#################################### ## IMAGE


###################################

    #else: # Pose 02 and Pose 03

    if ((current_pose.id == "pose_2") or (current_pose.id == "pose_3")):

        if afternight04__prehfix_RButtock_Slap == True:

            $ mc_body.store["right_hand"] = ""
            show afternight04_sexbattle_mc_handR empty

            #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            # penetrate_pussy empty - penetrate_anal empty
            call afternight04_sexbattle_pubic_emptiness #POSE02

            if (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 1:
                show afternight04_sexbattle_d_buttockR wet_00_smash_01_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 2:
                show afternight04_sexbattle_d_buttockR wet_00_smash_02_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 3:
                show afternight04_sexbattle_d_buttockR wet_00_smash_03_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 4:
                show afternight04_sexbattle_d_buttockR wet_00_smash_04_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 5:
                show afternight04_sexbattle_d_buttockR wet_00_smash_05_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) == 6:
                show afternight04_sexbattle_d_buttockR wet_00_smash_06_b_smashed
            elif (afternight04__RButtock_Slap_Success + afternight04__RButtock_Slap_Failed) >= 7:
                show afternight04_sexbattle_d_buttockR wet_00_smash_07_b_smashed

            with vpunch

        elif afternight04__prehfix_LButtock_Slap == True:

            $ mc_body.store["left_hand"] = ""
            show afternight04_sexbattle_mc_handL empty
            ###show afternight04_sexbattle_mc_handR_penetrate_pussy empty

            if (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 1:
                show afternight04_sexbattle_d_buttockL wet_00_smash_01_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 2:
                show afternight04_sexbattle_d_buttockL wet_00_smash_02_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 3:
                show afternight04_sexbattle_d_buttockL wet_00_smash_03_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 4:
                show afternight04_sexbattle_d_buttockL wet_00_smash_04_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 5:
                show afternight04_sexbattle_d_buttockL wet_00_smash_05_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) == 6:
                show afternight04_sexbattle_d_buttockL wet_00_smash_06_b_smashed
            elif (afternight04__LButtock_Slap_Success + afternight04__LButtock_Slap_Failed) >= 7:
                show afternight04_sexbattle_d_buttockL wet_00_smash_07_b_smashed

            with vpunch


##############################################################
#############################################################
    
    # Previous RHand Action
    if current_pose.id == "pose_1":

        $ afternight04__a_prehfix_LArm_Grab = False
        $ afternight04__a_prehfix_LBoob_Grab = False
        $ afternight04__a_prehfix_LBoob_Slap = False
        $ afternight04__a_prehfix_LButtock_Massage = False
        #$ afternight04__a_prehfix_LButtock_Slap = False
        
        $ afternight04__a_prehfix_LLeg_Massage = False
        $ afternight04__a_prehfix_LNipple_Pinch = False

    else:

        $ afternight04__a_prehfix_RArm_Grab = False
        $ afternight04__a_prehfix_RBoob_Grab = False
        $ afternight04__a_prehfix_RBoob_Slap = False
        $ afternight04__a_prehfix_RButtock_Massage = False
        #$ afternight04__a_prehfix_RButtock_Slap = False
        
        $ afternight04__a_prehfix_RLeg_Massage = False
        $ afternight04__a_prehfix_RNipple_Pinch = False


    $ afternight04__a_prehfix_Pussy_Fingers = False
    $ afternight04__a_prehfix_Anal_Fingers = False

    $ afternight04__a_prehfix_MMouth_Fingers = False
    $ afternight04__a_prehfix_MClitoris_Massage = False

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

####################################
###################################
####################################
##


############################################################
###########################################################

############################################################
###########################################################

    if current_pose.id == "pose_2" or current_pose.id == "pose_3":

        $ debug("Some TEST text")


        # progcheck "RButtock_Slap_Success = [afternight04__RButtock_Slap_Success], 
                # \nRButtock_Slap_Failed = [afternight04__RButtock_Slap_Failed], 
                # \nLButtock_Slap_Success = [afternight04__LButtock_Slap_Success], 
                # \nLButtock_Slap_Failed = [afternight04__LButtock_Slap_Failed]."


        #HER REACTION:
    #################################################################################################################
    #################################################################################################################

        if mc_body.roll_success == True: #You succeded.

            if ((afternight04__RButtock_Slap_Done) + (afternight04__RButtock_Slap_Done)) == 1: # 1rst Time.

                if (afternight04__RBoob_Slap_Done > 0) and (afternight04__RBoob_Slap_Done > 0):

                    d "¡No tenías suficiente con abofetearme las tetas que ahora vas a por mis nalgas?!"

                    d "¡¿Pero a ti que diablos te pasa?!"

                    p "Me dirás que no te gusta..."

                    if (afternight04__RBoob_Slap_Success + afternight04__LBoob_Slap_Success) > (afternight04__RBoob_Slap_Failed + afternight04__LBoob_Slap_Failed):

                        $ current_girl.enslavement += 2

                        d "Eres un jodido retrasado mental."

                        p "Sí,"

                        extend " sí..."

                        p "pero no me puedes negar las veces que has llegado a gemir,"

                        p "han sido bastante más de las que realmente te has quejado..."

                        d "..."

                        p "Y después de haberte azotado el culo,"

                        p "solo puedo asegurar que te gusta ser azotado."

                        d "..."

                        d "Te la estás jugando [protname]."

                    else:

                        $ current_girl.enslavement -= 2

                        d "¡SERÁ POSIBLE!"

                        d "¡¿Cuantas veces me has oído quejarme y tú seguías dándome?!"

                        p "Pero también has gemido de placer en algunas..."

                        d "¡¿EN ALGUNAS?!"

                        d "¡EN LA MAYORÍA NI DE COÑA!"

                        d "¡La madre que te parió!"

                        p "..."

                else:

                    d "¡LA MADRE QUE TE PARIÓ!"

                    d "¡¿Por qué diablos me nalgueas ahora?!"

                    d "¡¿Estás agilipollado?!"

                    p "Ohh..."

                    extend " Venga..."

                    p "¡¿Me dirás que nunca se lo has hecho a ninguna chica mientras la tenías a cuatro patas?!"

                    p "No me seas un jodido hipócrita de mierda."

                    d "..."

                    p "Que encima has gemido como la perra sarnosa que eres."

                    d "¡¿Qué?!"

                    p "¿Quieres que te de otra de nuevo?"

                    d "¡Ni se te ocurra!"

                    p "Ya..."

                    extend " ya..."

#################################################################### # Not the 1rst time anymore.

            elif afternight04__prehfix_RButtock_Slap == True: # R Boob

                if afternight04__RButtock_Slap_Success == 1: # The other one was already Slapped.

                    d "¡¿Otra vez?!"

                    d "¡¿No tenías suficiente con la izquierda que ahora vas con la derecha?!"

                    p "Si quieres vuelvo a la otra..."

                    d "¡No me seas bocazas!"

                elif afternight04__RButtock_Slap_Success == 2:

                    d "Joder [protname],"

                    if (afternight04__RBoob_Slap_Done > 3) and (afternight04__RBoob_Slap_Done > 3):

                        d "¡¿Estás esperando a que se vuelva roja como me has dejado las tetas?!"

                    else:

                        d "¡¿Estás esperando a que se vuelva roja como un tomate?!"

                    p "Quizás..."

                    p "Si veo que eso te pone,"

                    p "no veo porque no."

                    d "¡¿Y quien te dice que me pone?!"

                    p "La forma en que gimes cuando te doy el azote."

                    d "..."

                    d "Tsssk..."

                elif afternight04__RButtock_Slap_Success == 3:

                    d "¡La madre que te parió!"

                    d "¡Ya me has hostiado esta nalga [afternight04__RButtock_Slap_Done] veces!"

                    p "Y lo que has disfrutado..."

                    if afternight04__RButtock_Slap_Success > afternight04__RButtock_Slap_Failed:

                        d "..."

                        d "¡En tus jodidos sueños de marica retorcido imbécil!"

                        p "Ya..."

                        p "lo que tú digas,"

                        p "Ninfómana sado masoquista traga-pollas."

                        d "..."

                        d "¡Repite eso si tienes cojones!"

                        p "Yo sí,"

                        p "tú ya no..."

                        p "¿Verdad?"

                        d "¡Idiota!"

                    else:

                        d "¿¡TENDRÁS COJONES!?"

                        d "¡¿ACASO NO HAS OÍDO CUANTAS VECES HE GRITADO DE DOLOR?!"

                        p "..."

                        p "Pero es la tercera vez que me ha parecido oírte gemir ya..."

                        d "¿¡TE HA PARECIDO!?"

                        d "¡PERO CUANTAS JODIDAS VECES TE HA QUEDADO CLARO QUE NO ERA ASÍ!"

                        d "¡ME VOY A CAGAR EN TUS JODIDOS MUERTOS!"

                        p "..."

                elif afternight04__RButtock_Slap_Success == 4:

                    d "No te cansas"

                    d "¿Verdad?"

                    p "¿De verte esa cara de disfrute mientras te nalgueo?"

                    p "Ni en broma."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep") and (mc_body.dick_speed > 0):

                        $ current_girl.enslavement += 1

                        p "Por lo menos estoy follándote como me has estado pidiendo..."

                        p "¿No?"

                        d "Tssk..."

                    else:

                        d "Al menos podrías hacerlo mientras me follas..."

                        p "¿Entonces sí me dejarías hostiarte las nalgas?"

                        d "..."

                        d "No..."

                        pt "Ya..."

                elif afternight04__RButtock_Slap_Success == 5:

                    d "Dios..."

                    d "¿Te vas a cansar en algún momento?"

                    p "Quizás cuando pares de gemir."

                    d "..."

                elif afternight04__RButtock_Slap_Success == 6:

                    d "Hmmm..."

                    d "Eres un cabronazo de mierda..."

                    p "¿Por qué?"

                    p "Porque cada vez estás disfrutando más de que te esté azotando la nalga?"

                    d "Tssk..."

                    d "Tampoco te flipes."

                elif afternight04__RButtock_Slap_Success == 7:

                    d "¡Hhmmm...!"

                    pt "Es cierto que ya no se queja tan a menudo..."

                    pt "Pero no sé si es buena idea repetir demasiadas veces lo mismo..."

                elif afternight04__RButtock_Slap_Success == 8:

                    d "Mmmm..."

                    pt "Al final parece que va perdiendo el efecto y quizás se aburra..."

                    pt "Eso sin mencionar que ya no puede tener la teta más roja..."

                    pt "No pensaba que le iba a gustar tanto..."

                elif afternight04__RButtock_Slap_Success >= 9:

                    d "..."

################################################################################################################# LBOOB

            elif afternight04__prehfix_RButtock_Slap == False: # LBoob

                if afternight04__LButtock_Slap_Success == 1: # The other one was already Slapped.

                    d "¡¿Ahora la otra?!"

                    d "En serio..."

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        if mc_body.dick_speed == 0:

                            d "Si por lo menos me estuvieras moviendo esa polla tuya..."

                            d "quizás no me molestaría tanto..."

                            pt "Quizás dice..."

                        else:

                            p "¿Acaso no te estoy follando como me pediste?"

                            d "Hmmm..."

                            d "¿Pero hace falta que me cachetees la nalga?"

                            p "Tampoco parece que te disguste tanto..."

                            d "Idiota..."

                    else:

                        d "¡Al menos podrías metérmela!"

                        p "..."

                elif afternight04__LButtock_Slap_Success == 2:

                    d "¡¿Vas a seguir azotándome todo el día?!"

                    p "Es posible..."

                    d "..."

                elif afternight04__LButtock_Slap_Success == 3:

                    d "¡Dios!"

                    d "¡Duele!"

                    d "¡¿Sabes?!"

                    p "¿En serio?"

                    p "Vaya grito de dolor más raro has hecho entonces..."

                    d "Tssk..."


                elif afternight04__LButtock_Slap_Success == 4:

                    d "¡Me estás dejando la nalga completamente roja!"

                    d "¡¿Disfrutas con ello?!"

                    p "Aparentemente no tanto como tú..."

                    p "Si tengo que juzgarte por tus gemidos"

                    p "en lugar de por tus quejas..."

                    d "Tssk..."

                elif afternight04__LButtock_Slap_Success == 5:

                    d "¡¿No te cansas de azotarme?!"

                    p "¿Y tú de quejarte?"

                    p "Ya es la quinta vez que gimes al azotarte esta nalga..."

                    d "..."

                    d "Tssk..."

                elif afternight04__LButtock_Slap_Success == 6:

                    if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                        d "Hmm..."

                        if mc_body.dick_speed == 0:

                            d "Al menos podrías moverla un poco también..."

                            d "Ya que voy a sufrir de todos modos tu puta manía de azotarme las nalgas..."

                    else:

                        d "Si por lo menos me la metieras dentro..."

                        p "¿Entonces sí me dejarías azotarte más las nalgas?"

                        d "..."

                        d "Yo no he dicho eso..."

                        pt "Sí lo ha dicho."

                elif afternight04__LButtock_Slap_Success == 7:

                    d "¡¡Mmmm...!!"

                    pt "Desde luego no le disgusta,"

                    pt "Pero ya no le afecta como antes,"

                    pt "será mejor empezar a pensar en alternativas..."

                elif afternight04__LButtock_Slap_Success == 8:

                    d "¡¡Hmmm...!!"

                    pt "Pronto se va a cansar y se me va a montar encima..."

                elif afternight04__LButtock_Slap_Success >= 9:

                    d "..."

#################################################################################################################
################################################################################################################# # 1rst Time FAIL.

        elif mc_body.roll_success == False: #You Failed.

            if ((afternight04__RButtock_Slap_Success) + (afternight04__RButtock_Slap_Success)) == 1: # 1rst Time.

                if (afternight04__RBoob_Slap_Done > 0) and (afternight04__RBoob_Slap_Done > 0):

                    d "¡¡¿¿EN SERIO??!!"

                    if (afternight04__RBoob_Slap_Done > 4) or (afternight04__RBoob_Slap_Done > 4):

                        d "¡¡DESPUÉS DE DEJARME LAS TETAS ROJAS COMO UN TOMATE?!"

                    else:

                        d "¡¿DEPUÉS DE HOSTIARME COMO UN CAPULLO LAS TETAS?!"

                    p "Bueno..."

                    p "a mi no me ha parecido que te disgustara tanto..."

                    if ((afternight04__RBoob_Slap_Success) + (afternight04__RBoob_Slap_Success)) > ((afternight04__RBoob_Slap_Failed) + (afternight04__RBoob_Slap_Failed)):

                        d "¡¿Estás de coña?!"

                        p "Te he oído disfrutarlo muchas más veces de las que en realidad te has llegado a quejar."

                        p "¿O también me negarás eso?"

                        d "..."

                        d "No es lo que parece..."

                        pt "Ya..."

                    else:

                        d "¡¡¿ESTÁS DE COÑA?!!"

                        d "¡¡¿SABES DIFERENCIAR QUE ES UN GRITO DE DOLOR DE LO QUE NO LO ES?!!"

                        d "¡¡¿TE CUELGO BOCA-ABAJO COLGADO POR TUS PEZONES A VER SI TAMBIÉN GRITAS DE {i}\"PLACER?\"{/i}?!!"

                        p "Yo no he hecho tal cosa..."

                        d "¡NO ME TOQUES LAS NARICES!"

                        d "¡O AL FINAL TE REVENTARÉ LOS PUTOS HUEVOS!"

                        p "Que femenina eres cuando quieres..."

                        d "..."

                        p "Vale,"

                        extend " vale..."

                        pt "Reconozco que no he sido excesivamente afortunado,"

                        pt "ni tampoco he escogido demasiado bien mis acciones..."

################################################################################################################# # Not the 1rst Time.

            elif afternight04__prehfix_RButtock_Slap == True: # RBoob

                if afternight04__RButtock_Slap_Failed == 1:

                    d "¡¿NO TENÍAS SUFICIENTE CON UNA NALGA?!"

                    d "¡¿PRETENDES DEJARMELAS ROJAS TAMBIÉN?!"

                elif afternight04__RButtock_Slap_Failed == 2:

                    d "¡LA MADRE QUE TE PARIÓ!"

                    d "¡¿QUIERES DEJAR MIS NALGAS EN PAZ?!"

                    if afternight04__RButtock_Slap_Success > 2:

                        p "Las otras veces no te han digustado tanto..."

                        d "¡PUES AHORA SÍ!"

                        d "¡¿QUÉ ES LO QUE NO ENTIENDES JODER?!"

                    elif afternight04__RButtock_Slap_Success > 0:

                        p "Pero ha habido alguna vez que te ha gustado..."

                        d "¡¿Y ESO TE PARECE UNA JODIDA PUTA EXCUSA?!"

                elif afternight04__RButtock_Slap_Failed == 3:

                    d "¡COÑO!"

                    d "¡QUE DUELE!"

                    d "¡ME CAGÜEN TODO!"

                elif afternight04__RButtock_Slap_Failed == 4:

                    d "¡¡NO TE LO VOLVERÉ A REPETIR!!"

                    d "¡DEJA DE AZOTARME O ME VOY A CABREAR EN SERIO!"

                elif afternight04__RButtock_Slap_Failed == 5:

                    d "¡YA ES LA PUTA QUINTA VEZ QUE ME AZOTAS ESTA NALGA!"

                    d "¡COMO SIGAS ASÍ TE VOY A ROMPER LAS PELOTAS!"

                elif afternight04__RButtock_Slap_Failed >= 6:

                    d "..."

#################################################################################################################

            elif afternight04__prehfix_RButtock_Slap == False: # LBoob

                if afternight04__LButtock_Slap_Failed == 1:

                    d "¡¿PERO QUÉ COÑO?!"

                    d "¡¿NO TENÍAS SUFICIENTE CON UNA JODIDA NALGA?!"

                    d "¡ME ESTÁS EMPEZANDO A TOCAR LAS NARICES!"

                elif afternight04__LButtock_Slap_Failed == 2:

                    d "¡JODER!"

                    d "¡¿TE CREES GRACIOSO DEJÁNDOME LA NALGA ROJA?!"

                    if afternight04__LButtock_Slap_Success > 2:

                        p "No me seas tan quejica..."

                        p "Bien que no te has quejado antes tantas veces..."

                        d "¡¿SE SUPONE QUE ME TENGO QUE REÍR?!"

                    elif afternight04__LButtock_Slap_Success > 0:

                        p "Pero bien que te ha gustado alguna que otra vez..."

                        d "¡¿TE PATEO LA POLLA A VER SI EN ALGUNA RARA OCASIÓN TAMBIÉN LO DISFRUTAS?!"

                        p "Lo tendría difícil para follarte si hicieras eso..."

                        d "¡Ya buscaría a otra persona que no fuese tan imbécil!"

                elif afternight04__LButtock_Slap_Failed == 3:

                    d "¡EN SERIO!"

                    d "¡DEJA MI PUTA NALGA EN PAZ!"

                elif afternight04__LButtock_Slap_Failed == 4:

                    d "¡NO TE LO VOLVERÉ A REPETIR!"

                    d "¡DEJA DE AZOTARME LA PUTA NALGA!"

                elif afternight04__LButtock_Slap_Failed >= 5:

                    d "..."

            p "..."

#################################################################################################################
#################################################################################################################


############################################################
    if mc_body.roll_success == False:

        if current_pose.id == "pose_1":

            if mc_body.store["left_hand"] == "RButtock_Slap":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["right_hand"] == "LButtock_Slap":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch

        if current_pose.id == "pose_2" or current_pose.id == "pose_3":

            if mc_body.store["right_hand"] == "RButtock_Slap":

                $ mc_body.store["right_hand"] = ""
                #show afternight04_sexbattle_mc_handL empty

                #with hpunch

            if mc_body.store["left_hand"] == "LButtock_Slap":

                $ mc_body.store["left_hand"] = ""
                #show afternight04_sexbattle_mc_handR empty

                #with hpunch



############################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    if not ((mc_body.store["dick"] == "med") or (mc_body.store["dick"] == "deep")) and (mc_body.dick_speed == 0):

        call afternight04_RapeOrNot

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