# default afternight04__MMouth_dick_Deep_Done = 0
# default afternight04__MMouth_dick_Deep_Success = 0
# default afternight04__MMouth_dick_Deep_Failed = 0
# default afternight04__MMouth_dick_Deep_Success_Cond = False

label MMouth_dick:

######################################################### Dummy_Screen Calls

    if afternight04_SheRapingYou == True:

        call afternight04_SheRapingYou_NotAllowed

######################################################### version_changelog

    if Tendolarsversion == False:

        if (current_pose.id == "pose_1" and config.version < "00.08.05") or (not current_pose.id == "pose_1" and config.version < "00.90.00"):

            call endupdatescript_sexbattle

#########################################################

    $ __suffix = []
    $ __prefix = "MMouth_dick."

#########################################################

    $ mc_body.store["dick"] = "MMouth_dick"

#########################################################

    $ afternight04__prehfix_MMouth_dick = True
    $ afternight04__a_prehfix_MMouth_dick = True
    
    call afternight04_sex_check_before
    
    label .manager:

        if current_pose.id == "pose_3":

            $ afternight04__MMouth_dick_Done += 1

            if mc_body.roll_success:
                $ afternight04__MMouth_dick_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__MMouth_dick_Failed += 1

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
        $ debug ("First Orgasm for his. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04__MMouth_dick_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Putting in her Mouth your Dick (Blowjob).")

        call afternight04__MMouth_dick
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################

    label afternight04__MMouth_dick:

        call afternight04__MMouth_dick_general

        return


    label afternight04__MMouth_dick_his_orgasm:

        call afternight04__MMouth_dick_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04__MMouth_dick_her_orgasm:

        call afternight04__MMouth_dick_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################

label afternight04__MMouth_dick_general:

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 01

    ##############################################################
    #############################################################

    
    #if current_pose.id == "pose_1": Not necessary

    if (mc_body.store["dick"] == "Pussy_dick_low" 
        or mc_body.store["dick"] == "Pussy_dick_med"
        or mc_body.store["dick"] == "Pussy_dick_deep"
        or mc_body.store["dick"] == "Anal_dick_low"
        or mc_body.store["dick"] == "Anal_dick_med"
        or mc_body.store["dick"] == "Anal_dick_deep"):

        $ mc_body.store["dick"] = "Pussy_dick_out"
        $ mc_body.dick_speed = 0

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_mc_dick_pussy empty
            with dissolve

        else: # NOT FINISHED

            show afternight04_sexbattle_mc_dick_pussy empty
            with dissolve

        $ current_girl.enslavement -= 1
        $ current_girl.pleasure -= 3

        if current_girl.total_try == 1: #Apparently, Don??t change this.

            if (mc_body.store["dick"] == "Pussy_dick_low" 
                or mc_body.store["dick"] == "Pussy_dick_med"
                or mc_body.store["dick"] == "Pussy_dick_deep"):

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "????Por qu?? demonios la sacas?!"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            else:

                d "Ya era hora que la sacaras de ah??..."

    else:

        $ mc_body.store["dick"] = "Pussy_dick_out"
        show afternight04_sexbattle_mc_dick_pussy empty
        with dissolve      

    ##############################################################
    #############################################################

    #$ mc_body.store["dick"] = "Pussy_dick_out" ## Not Necessary

    ##############################################################
    #############################################################

    if current_pose.id == "pose_1":

        if current_girl.total_try == 1: # Don??t change this conditional.
        #if afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed == 1:

            show afternight04_sexbattle_d_mouth sad_Talkingx01_a
            show afternight04_sexbattle_d_eyes 01_a
            show afternight04_sexbattle_d_pupils front01_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            d "??Euh?"

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            pt "Mierda..."

            pt "teni??ndola encima es imposible que llegue a meterle la polla en la boca..."

        elif current_girl.total_try == 2:

            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            d "??Se puede saber qu?? intentas hacer moviendo as?? las caderas?"

            show afternight04_sexbattle_d_mouth happy_Silentx02_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve

            pt "Por mucho que lo intente,"

            extend " no se va a mover..."

            pt "Quiz??s si la agarro del brazo,"

            extend " consiga sacarla de encima..."

        else:

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            pt "????Por qu?? diablos insisto en hacer algo que desde esta postura no puedo?!"

        call screen dummy_screen()

    #elif current_pose.id == "pose_2":

        #$ debug ("Here is pose 2, but you can??t put your dick in her mouth.")


####################################
###################################
####################################
###################################
####################################
###################################_ POSE 03

    elif current_pose.id == "pose_3":

        show afternight04_sexbattle_d_mouth_blow_over blowjobx05_c
        show afternight04_sexbattle_d_mouth_blow blowjobx05_c
        show afternight04_sexbattle_d_jaw_blow 05_c

        show afternight04_sexbattle_d_jaw empty
        show afternight04_sexbattle_d_mouth empty

        show afternight04_sexbattle_d_mouth_blowjob_cheek 01_c_action

    ####

        if (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 1:
    
            show afternight04_sexbattle_mc_dick_blowjob condom wet_00_deep05_action_b

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 2:

            show afternight04_sexbattle_mc_dick_blowjob condom wet_00_deep06_action_b


        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 3:

            show afternight04_sexbattle_mc_dick_blowjob condom wet_00_deep05_action_b

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) >= 4:

            show afternight04_sexbattle_mc_dick_blowjob condom wet_00_deep06_action_b

        with dissolve

##############################################################
#############################################################

        # Previous Dick Action

        #$ afternight04__a_prehfix_MMouth_dick = False #Blowjob

        $ afternight04__a_prehfix_Pussy_dick_out = False
        $ afternight04__a_prehfix_Pussy_dick_low = False
        $ afternight04__a_prehfix_Pussy_dick_med = False
        $ afternight04__a_prehfix_Pussy_dick_deep = False

        $ afternight04__a_prehfix_Anal_dick_out = False
        $ afternight04__a_prehfix_Anal_dick_low = False
        $ afternight04__a_prehfix_Anal_dick_med = False
        $ afternight04__a_prehfix_Anal_dick_deep = False

        #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

####################################
###################################
####################################
###################################
#################################### DIALOGUE POSE 03 BLOWJOB.


  #HER REACTION:
############################################################
###########################################################

    #elif current_pose.id == "pose_3": # Not necessary, already used.

        $ debug ("Kiss in her mouth, POSE 03.") # Pose has no mouth.

        if mc_body.roll_success == False: # You failed.

            if afternight04__MMouth_dick_Failed == 1:

                if current_pose.id == "pose_3":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_c
                    show afternight04_sexbattle_d_eyes 02_c
                    show afternight04_sexbattle_d_pupils front02_c
                    show afternight04_sexbattle_d_eyebrows angryx03_c
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    d "????QU?? COJONES HACE TU POLLA EN MI CARA?!"

                elif randomnum_1to5 == 2:

                    d "????QU?? COJONES?!"

                elif randomnum_1to5 == 3:

                    d "????PERO QU?? PUTA MIERDA EST??S PRETENDES?!"

                elif randomnum_1to5 == 4:

                    d "??????QU?? COJONES PRETENDES?!!"

                elif randomnum_1to5 == 5:

                    d "????PARA QU?? CO??O ME ACERCAS LA POLLA A MI CARETO?!"

                if current_pose.id == "pose_3":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_c
                    show afternight04_sexbattle_d_eyes 05_c
                    show afternight04_sexbattle_d_pupils front05_c
                    show afternight04_sexbattle_d_eyebrows angryx03_c
                    with dissolve

            else:

                if current_pose.id == "pose_3":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_c
                    show afternight04_sexbattle_d_eyes 03_c
                    show afternight04_sexbattle_d_pupils front03_c
                    show afternight04_sexbattle_d_eyebrows angryx04_c
                    with dissolve

                $ randomnum_1to10 = renpy.random.randint(1, 10)

                if randomnum_1to10 == 1:

                    d "????OTRA VEZ?!"

                elif randomnum_1to10 == 2:

                    d "????EN SERIO?!"

                elif randomnum_1to10 == 3:

                    d "????TE CREES QUE SOY UNA PUTA DE BARRIO?!"

                elif randomnum_1to10 == 4:

                    d "????ME TOMAS POR UN SOPLA POLLAS?!"

                elif randomnum_1to10 == 5:

                    d "????EST??S VOLVIENDO A INTENTAR QUE ME PONGA {i}ESTO{/i} EN MI BOCA?!"

                elif randomnum_1to10 == 6:

                    d "????QU?? CO??O TE HAS FUMADO?!"

                elif randomnum_1to10 == 7:

                    d "????ESTO ES A LO QUE LLAMAS FOLLAR?!"

                elif randomnum_1to10 == 8:

                    d "??????TE CREES QUE SOY IMB??CIL Y MARIC??N?!!"

                elif randomnum_1to10 == 9:

                    d "????QU?? CLASE DE MAM??N TE CREES QUE SOY?!"

                elif randomnum_1to10 == 10:

                    d "????DE ESTO NI HABLAR!!"

                if current_pose.id == "pose_3":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_c
                    show afternight04_sexbattle_d_eyes 05_c
                    show afternight04_sexbattle_d_pupils front05_c
                    show afternight04_sexbattle_d_eyebrows angryx05_c
                    with dissolve

    ############################################################ # OFF image

                # POSE 01 and POSE 02 are not necessary.

            $ mc_body.store["dick"] = ""
            show afternight04_sexbattle_mc_dick_blowjob empty

            with hpunch

            if current_pose.id == "pose_3": #Necessary, for pose 02

                show afternight04_sexbattle_d_mouth sad_Silentx04_c
                show afternight04_sexbattle_d_eyes 01_c
                show afternight04_sexbattle_d_pupils front01_c
                show afternight04_sexbattle_d_eyebrows angryx02_c


                show afternight04_sexbattle_d_mouth_blow_over empty
                show afternight04_sexbattle_d_mouth_blow empty
                show afternight04_sexbattle_d_jaw 00_c
                show afternight04_sexbattle_d_jaw_blow empty
                show afternight04_sexbattle_d_mouth_blowjob_cheek empty
                with dissolve

    ############################################################
    ########################################################### # RNipple pose 0p3 Dialogue.

        
        
## TRIES

        $ debug ("HERE GOES DIALOGUE FOR MMouth_dick (Blowjob) pose 03")

        if (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 0:

            aj "This text should not appear. 5578"


        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 1:

            if mc_body.roll_success == True: #You succeded.

                d "..."

            else:

                d "????SE PUEDE SABER PARA QU?? CO??O ME HAS PUESTO TU ASQUEROSA POLLA EN MI BOCA?!"

                p "Solo la he puesto sobre tus labios..."

                d "????Y TE PARECE POCO?!"

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    d "??QUE ME HAS PUESTO TU ASQUEROSA POLLA EN MI CULO!"

                    p "..."

                    d "??JODER!"

                p "..."

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 2:

            if afternight04__MMouth_dick_Failed == 1:

                d "????Pero que co??o pasa contigo?!"

                p "??Qu???"

                p "Antes no te has quejado..."

                if afternight04__MMouth_dick_Failed > 1:

                    d "??ME HE QUEJADO YA VARIAS VECES!"

                    p "Pero en una ocasi??n lo has hecho..."

                    d "..."

                d "??Est??s de co??a verdad?"

                p "..."

                d "??No acerques esa cosa a mi cara!"

                p "..."

            elif afternight04__MMouth_dick_Failed == 2:

                d "??YA ES LA SEGUNDA VEZ QUE INTENTAS LO MISMO!"

                d "??Y LAS DOS VECES TE HE DICHO QUE PARES!"

                d "????Acaso no ves que me est??s tocando realmente las putas pelotas?!"

                p "..."

                d "??DEJA DE HACER EL IMB??CIL!"

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 3:

            if afternight04__MMouth_dick_Failed == 1:

                d "??Deja de intentar meterme eso en mi boca!"

                p "Es la primera vez que te quejas..."

                d "Tsssk..."

            elif afternight04__MMouth_dick_Failed == 2:

                d "????No parar??s hasta que te muerda la polla verdad?!"

                p "..."

            elif afternight04__MMouth_dick_Failed == 3:

                d "??T?? QUIERES QUE TE DE UNA PATADA EN LOS HUEVOS!"

                d "????VERDAD?!"

                p "..."

                d "??DEJA DE ACERCARME ESO A LA CARA O TE JURO QUE TE ARREPENTIR??S!"

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 4:

            if afternight04__MMouth_dick_Failed == 1:

                d "Ya basta..."

                d "??No crees?"

                d "????Que clase de amigo eres?!"

                p "El tipo del que ayuda a un amigo necesitado que le pide un favor."

                d "??Te he pedido que me folles el co??o no la boca!"

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    d "??Que me la has metido hasta el fondo de la garganta!"

                    d "Y no es que la tengas precisamente peque??a..."

                p "Tampoco he visto que te quejaras demasiado..."

                d "..."

            elif afternight04__MMouth_dick_Failed == 2:

                d "??Te he dicho que dejes de meter tu polla en mi boca!"

                p "Y en dos ocasiones no has dicho eso."

                d "..."

                d "Est??s empezando a sacarme de mis casillas..."

                p "..."

            elif afternight04__MMouth_dick_Failed == 3:

                d "??Como vuelvas a meter tu polla delante me voy a cabrear de verdad!"

                p "Venga... al fin y al cabo ha habido una vez que no te ha disgustado tanto..."

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    p "Hasta te he metido la polla hasta el fondo de la garganta."

                d "??He dicho que basta!"

                d "????Me explico?!"

                d "????O necesitas sentir dolor para entenderlo?!"

                p "..."

            elif afternight04__MMouth_dick_Failed == 4:

                d "??ME CAGO EN EL MUERTO QUE TE PARI?? HIJO DE LA GRAN PUTA!"

                d "??DEJA DE METERME TU POLLA EN MI CARA!"

                d "??JODER!"

                p "..."

                p "No conoc?? a mi padre,"

                p "pero estoy casi seguro que no me pari?? ??l..."

                d "..."

                d "??Te cachondeas de mi?"

                p "No."

                p "Si tienes que meterte con mi difunta familia,"

                p "puedes irte un poco a tomar por el culo."

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    if afternight04_Anal_dick_med_Speed_0_Done > 1:

                        d "Eres t?? quien me ha dado por el culo varias veces."

                    else:

                        d "Ya me has dado t?? por el culo una vez."

                    p "Y lo bien que lo has disfrutado..."

                    if (afternight04__Anal_dick_med_Failed) > (afternight04__Anal_dick_med_Success):

                        d "????Est??s de co??a?!"

                    else:

                        d "??Tssk...!"

                        d "??Y te crees que me voy a meter eso en la boca?"

                        d "T?? est??s flipando."

                        pt "Ya lo veremos..."

                else:

                    p "..."

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) == 5:

            if afternight04__MMouth_dick_Failed == 1:

                d "De verdad [protname],"

                d "Creo que ya va siendo hora de que dejes de meterme tu jodida polla en mi boca."

                d "Te he pedido que me follaras..."

                d "??Qu?? cojones estamos haciendo ahora?"

                p "??Disfrutar de nuestra compa????a mutua?"

                d "??Foll??ndome la boca?"

                if afternight04__MMouth_dick_Deep_Success > 0:

                    d "Joder..."

                    d "??Si hasta me la has metido hasta el fondo de mi puta garganta!"

                    p "Y en realidad no te ha disgustado tanto..."

                    d "??ESO ES LO QUE M??S ME JODE!"

                    pt "No es f??cil entenderle..."

                d "Tssk..."

                d "No hagas que me sienta una puta barata de barrio,"

                d "y f??llame de una jodida vez."

                pt "No estoy seguro de que entienda bien el concepto de {i}\"puta barata de barrio\"{/i}..."

            elif afternight04__MMouth_dick_Failed == 2:

                d "Ya va siendo hora de que dejes de meterme la polla en la boca..."

                d "????No crees?!"

                d "Ya te he dicho antes que esto no me est?? molando nada..."

                p "Solo es la segunda vez que quejas,"

                p "las otras tres veces no he visto que te quejaras demasiado..."

                d "??Eso te lo habr?? parecido a ti!"

                d "??Que tienes la mente m??s perturbada que {i}\"Dross\"{/i}!"

                p "..."

                p "{i}Dross{/i}es un showman perturbador,"

                p "t?? sin embargo, "

                p "eres un t??o que se ha convertido en una ninf??mana tan desesperada"

                p "que me has pedido a mi, que seguir?? vi??ndote el careto una vez recuperes tu cuerpo,"

                p "el favor de que te folle como si no hubiera ma??ana."

                p "Son cosas distintas."

                d "..."

                d "Te est??s rifando una hostia de aqu?? hasta Canc??n..."

                p "Pero sabes que tengo raz??n."

                d "..."

            elif afternight04__MMouth_dick_Failed == 3:

                d "??Ya es la tercera vez que te digo que dejes de hacer el imb??cil!"

                p "Pero bien que ha habido dos veces que no te ha disgustado tanto la idea..."

                if afternight04__MMouth_dick_Deep_Success > 0:

                    if afternight04__MMouth_dick_Deep_Success == 1:

                        p "Hasta ha habido una vez que te la he metido hasta el fondo sin que te quejaras..."

                    else:

                        p "Hasta te he metido varias veces la polla hasta el fondo sin oirte quejar demasiado..."

                    d "..."

                d "Mi paciencia tiene un l??mite [protname]."

                d "Deja de tocarme los huevos."

                pt "????Qu?? huevos?!"

            elif afternight04__MMouth_dick_Failed == 4:

                d "??En serio [protname]!"

                d "??PARA YA!"

                d "??No te lo voy a repetir!"

                p "..."

            elif afternight04__MMouth_dick_Failed == 5:

                d "??VOY A CONSTRUIR UNA ESCALERA CON LOS HUESOS DE TUS PUTOS MUERTOS!"

                d "??PARA SUBIR Y CAGARME EN TU PUTA MADRE!"

                p "..."

                d "????QU?? MIERDAS TE PASA POR LA CABEZA?!"

                d "??YA ES LA PUTA QUINTA VEZ QUE INTENTAS LO MISMO!"

                d "??LA PR??XIMA VEZ TE VAS A QUEDAR SIN POLLA!"

                pt "??Hace falta que sea tan descriptivo?"

                pt "Aunque no parece que hable en broma..."

        elif (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Failed) >= 6:

            if afternight04__MMouth_dick_Failed == 1:

                d "??Ya basta de ponerme tu polla en mi cara!"

                d "????No crees?!"

                p "Hasta ahora es la primera vez que te quejas..."

                if afternight04__MMouth_dick_Success > 6:

                    p "Y no ser?? por falta de empe??o en quejarte,"

                    p "porque oportunidades has tenido..."

                    d "..."

                if afternight04__MMouth_dick_Deep_Success > 0:

                    p "Adem??s,"

                    p "ya te he metido la polla hasta el fondo de tu garganta..."

                    d "..."

                p "??A qu?? viene que te quejes ahora?"

                d "..."

                d "Esto no es lo que se supone que te ped??."

                d "??Verdad?"

                p "..."

            elif afternight04__MMouth_dick_Failed == 2:

                d "??De verdad!"

                d "????Te crees que soy una puta barata de rotonda?!"

                d "??Te ped?? que me follaras!"

                d "??No que me violaras la boca!"

                p "A duras penas es la segunda vez que te quejas..."

                if afternight04__MMouth_dick_Deep_Success > 0:

                    p "Y no ser?? porque mi polla no ha llegado hasta el fondo de tu garganta..."

                d "..."

                d "Deja de ponerme tu polla delante de mi cara."

            elif afternight04__MMouth_dick_Failed == 3:

                d "????Cuantas veces te tengo que decir que dejes de ponerme tu polla delante?!"

                p "Las veces que hagan falta,"

                p "en realidad lo has disfrutado m??s veces de las que est??s dispuesto a admitir."

                d "..."

                if afternight04__MMouth_dick_Deep_Success > 0:

                    p "Adem??s,"

                    p "bien que te la he metido hasta el fondo de tu garganta..."

                d "Tssk..."

                d "No hagas que pierda la paciencia [protname]..."

                d "No me gustar??a que te quedaras sin polla antes de que terminaras lo que te he pedido."

                p "..."

            elif afternight04__MMouth_dick_Failed == 4:

                d "??Ya es la cuarta vez que te pido que dejes mi boca en paz!"

                d "????Qu?? puto problema tienes con la comprensi??n oral?!"

                p "Pues que me gusta m??s el sexo oral."

                d "..."

                d "Al final ir?? a buscar a \"Michael\","

                d "te lo voy a meter hasta el fondo de la garganta"

                d "y entonces veremos si te gusta tanto el PUTO sexo oral de los cojones..."

                p "..."

            elif afternight04__MMouth_dick_Failed == 5:

                d "??ME CAGO EN TODO LO QUE SE MENEA [protname]!"

                d "??Te lo juro!"

                d "??Como me vuelvas a poner tu polla delante!"

                d "??Te la voy arrancar a mordiscos!"

                d "????Queda claro?!"

                p "..."

            elif afternight04__MMouth_dick_Failed == 6:

                $ mc_body.pleasure -= 3

                p "??AAAUGH!"

                p "??Joder!"

                p "??Me has mordido la polla!"

                d "Te lo advert??."

                d "La pr??xima vez que lo intentes,"

                d "no ir?? con tanto cuidado como ahora."

                pt "????Eso es que ha sido delicado esta vez?!"

            elif afternight04__MMouth_dick_Failed >= 7:

                $ mc_body.pleasure -= 5

                $ randomnum_1to10 = renpy.random.randint(1, 10)

                if randomnum_1to10 == 1:

                    p "??CO??O!"

                elif randomnum_1to10 == 2:

                    p "??JODER!"

                elif randomnum_1to10 == 3:

                    p "??ME CAGO EN LA HOSTIA!"

                elif randomnum_1to10 == 4:

                    p "??AAUUCH!"

                elif randomnum_1to10 == 5:

                    p "??AAAIH!"

                elif randomnum_1to10 == 6:

                    p "??MIERDA!"

                elif randomnum_1to10 == 7:

                    p "??AAUUCH!"

                elif randomnum_1to10 == 8:

                    p "??JODEEER!"

                elif randomnum_1to10 == 9:

                    p "????DIOS!!"

                elif randomnum_1to10 == 10:

                    p "??ME VAS A DEJAR SIN POLLA!"

                if afternight04__MMouth_dick_Failed == 6:

                    p "??D??dac!"

                    p "??Al final me har??s sangrar de verdad!"

                    d "Y cont??ntate que solo sea eso."

                    p "..."

                    d "Te lo advert??."

                p "..."

            #HIS SUCCESS:

#########################################################################
########################################################################
#######################################################################

    # NOT FINISHED Writing DIalogue. -

        if mc_body.roll_success == True:  # Only Blowjob Superficial.

            if afternight04__MMouth_dick_Success == 1:

                $ mc_body.pleasure += 1

                n "Con suma precauci??n,"

                d "[protname]..."

                n "deslizas tu enorme glande por sus carnosos labios con la incertidumbre de como reaccionar??."

                d "??Qu??...?"

                n "Aparentemente no muestra una actitud exageradamente hostil,"

                n "con lo que te permites la osad??a de cruzar el muro de dientes"

                n "que te separa del interior de su boca."

                n "Aunque logras vadear la cerca de sus labios,"

                n "sus mand??bulas siguen completamente cerradas."

                n "Con lo que decides jugar un poco con el borde de estos,"

                n "no sin dejar de observar el airado, pero libidinoso rostro de D??dac."

            elif afternight04__MMouth_dick_Success == 2:

                $ mc_body.pleasure += 1

                if afternight04__MMouth_dick_Deep_Success > 0:

                    n "Regresas tu polla a su boca sin demasiada cautela."

                    pt "Al fin y al cabo ya se la he metido hasta el fondo de la garganta..."

                else:

                    n "Regresas tu polla a su boca con suma cautela."

                    if afternight04__MMouth_dick_Deep_Failed > 0:

                        pt "Despu??s de la mordida que me ha metido,"

                        pt "es mejor ser prudente..."

                d "Est??s de co??a..."

                n "Lentamente,"

                n "consigues que relaje relativamente su mand??bula"

                d "Hhmm..."

                n "y atraviesas el muro de dientes que te bloqueaba hasta el momento;"

                n "penetrando as?? en su c??lido y h??medo interior"

                n "palpando con sutileza la suave y al mismo tiempo ??spera lengua."

                if afternight04__MMouth_dick_Deep_Success < 0:

                    n "No sin tener la mirada fija, t??trica y sombr??a de D??dac directa a tus ojos."

                    n "Observando con desconfianza tus movimientos."

            elif afternight04__MMouth_dick_Success == 3:

                $ mc_body.pleasure += 2

                if afternight04__MMouth_dick_Deep_Failed > 0:

                    n "Con extremada precauci??n, para evitar que te muerda de nuevo;"

                    n "regresas a su boca con tu {i}anaconda{/i}."

                else:

                    n "Sin demasiada precauci??n,"

                    n "regresas a la superficie de su rostro, posando tu glande encima de ellos;"

                n "haciendo una ligera presi??n,"

                d "Hhhm..."

                n "consigues que vuelva a relajar su mand??bula y atravesando sus labios"

                n "introduces tu erecto miembro en su c??lido interior,"

                n "sintiendo como su lengua se desplaza paulatinamente saboreando,"

                n "aunque aparentando desinter??s, la punta del glande."

            elif afternight04__MMouth_dick_Success == 4:

                $ mc_body.pleasure += 2

                n "Sin demasiada demora,"

                n "devuelves tu m??stil sobre sus labios,"

                d "HHmmm..."

                n "que en poco tiempo vuelve a introducirse en su ardiente interior,"

                n "d??nde empiezas apreciar de forma m??s notable,"

                n "el sutil, pero evidente desplazamiento de su lengua alrededor de tu glande,"

                n "as?? como en la parte inferior de este,"

                n "ofreci??ndote un placer extraordinario, a pesar de sus quejas."

                if afternight04__MMouth_dick_Deep_Failed > 0:

                    if afternight04__MMouth_dick_Deep_Failed > 1:

                        n "Y de las n??merosas mordidas que ya llevas."

                    else:

                        n "Y de la fuerte mordida que ya llevas."

            elif afternight04__MMouth_dick_Success == 5:

                $ mc_body.pleasure += 2

                n "Sin pr??cticamente miedo alguno,"

                n "vuelves a introducir tu enorme miembro en el interior de su boca sin demasiada dificultad."

                n "Su mand??bula, no tan solo cesa en su intento de vedarte el paso,"

                n "sino que adem??s, parece empezar a desplazarse para darte m??s libertad de movimiento."

                pt "A pesar de sus quejas y tozudez, da la sensaci??n que poco a poco se va soltando m??s,"

                pt "incluso su lengua empieza a juguetear con menos verg??enza alrededor de mi glande..."

                if afternight04__MMouth_dick_Deep_Failed > 0:

                    pt "Aunque de todos modos,"

                    pt "tendr?? que ir con cuidado de que no me vuelva a morder..."

            elif afternight04__MMouth_dick_Success == 6:

                $ mc_body.pleasure += 3

                d "Hhmmm..."

                n "A pesar de su inicial reticencia,"

                n "en cada nuevo fructuoso intento, los labios de D??dac muestran un mayor inter??s en saborear tu erecto miembro,"

                n "al mismo tiempo que su lengua se desplaza en todas direcciones,"

                n "degustando el l??quido preseminal que forzosamente emerge del glande"

                n "y hasta tienes la sensaci??n de que t??midamente empieza a succionarla simult??neamente."

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    pt "Parece que ya no le importa demasiado que mi polla haya pasado por su agujero anal..."

            elif afternight04__MMouth_dick_Success == 7:

                $ mc_body.pleasure += 4

                d "MMMhmm..."

                n "Sus labios no disimulan ya en absoluto su b??squeda para saborear la punta de tu erecto miembro."

                n "pr??cticamente sacando la lengua por la boca, degusta cada rinc??n de tu glande y m??s all?? de ??l con bastante vigor."

                n "Sientes especial placer cuando esta se desliza por debajo de tu sensible capullo,"

                n "rascando con ning??n tipo de delicadeza perceptivo frenillo,"

                n "al mismo tiempo que reparas en su agitado y ardiente aliento que recorre lo largo y ancho de tu miembro."

                if afternight04__MMouth_dick_Deep_Success > 0:

                    if afternight04__MMouth_dick_Deep_Success > 5:

                        n "En su mirada, completamente lasciva y sumisa,"

                        n "parece impl??cito que te est?? pidiendo que se la vuelvas a meter entera en la garganta."

                        pt "Desde luego,"

                        pt "he convertido a mi compa??ero de piso en una jodida ninf??mana traga pollas..."

                    elif (afternight04__MMouth_dick_Deep_Success) > (afternight04__MMouth_dick_Deep_Failed):

                        n "En su mirada, notablemente lasciva y sumisa,"

                        n "existe el deseo, al mismo tiempo que la duda,"

                        n "de si su garganta volver?? a ser penetrada por tu enorme poll??n,"

                        n "a pesar de tus fracasos,"

                        n "es indudable que ha habido ocasiones en las que lo ha disfrutado m??s de lo que es capaz de confesar."

                    else:

                        n "En su mirada, lasciva y sumisa,"

                        n "a??n hay resquicios de duda en si volver??s o no a intentar met??rsela entera en la garganta,"

                        n "debido a que no han resultado demasiado fructuosos tus anteriores intentos."

                        n "Prueba de ello, es tu dolorida polla que en estos momentos est?? siendo sanada por su c??lida lengua."

                elif afternight04__MMouth_dick_Deep_Failed > 0:

                    n "En su mirada ves reflejada la lujuria por saborear tu polla,"

                    if afternight04__MMouth_dick_Deep_Failed > 4:

                        n "pero al mismo tiempo la advertencia de que ni se te ocurra volver a intentar met??rsela en el fondo de su garganta."

                        pt "No parece que haya tenido demasiada suerte con su {i}garganta profunda{/i}..."

                    else:

                        n "pero al mismo tiempo la incertidumbre de si ser??s capaz"

                        n "de volver a intentar met??rsela por la garganta sin ??xito,"

                        n "como la ??ltima vez."
                else:

                    pt "??La madre que lo pari??!"

                    pt "??Empiezo a pensar que esto le gusta m??s a ??l que a mi!"

                    pt "Quiz??s ser??a hora de probar si le cabe mi polla por su garganta..."

                    pt "??Estar?? lo suficientemente sumisa?"


            elif afternight04__MMouth_dick_Success == 8:

                $ mc_body.pleasure += 5

                d "Mmmmmm..."

                n "Sin ning??n tipo de rubor ni bochorno,"

                n "vuelve a relamer tu miembro en el interior de su boca"

                n "al mismo tiempo que succiona todo el liquido preseminal que se encuentra por en medio,"

                n "d??ndote la sensaci??n que lleva toda la vida chupando pollas como una profesional de lujo."

                pt "Jodeeeer..."

                pt "No s?? si ha sido buena idea esto..."

                pt "as?? no tardar?? en correrme..."

            elif afternight04__MMouth_dick_Success >= 9:

                d "..."

                $ mc_body.pleasure += 5

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    p "Ufff..."

                elif randomnum_1to5 == 2:

                    p "Esa mirada de perra en celo no ayuda..."

                    d "..."

                elif randomnum_1to5 == 3:

                    p "Madre m??a..."

                    p "??Es que te has vuelto adicta a mi polla?"

                    d "Hmm..."

                    n "Sigue chup??ndote la polla ignor??ndote completamente."

                elif randomnum_1to5 == 4:

                    p "??Jodeer...!"

                elif randomnum_1to5 == 5:

                    p "??Puto D??dac!"

                    p "??Que mam??n que eres!"

                    n "Su mirada muestra un tinte de ira,"

                    n "pero se disuelve r??pidamente al volver su atenci??n a lo que est?? haciendo."


############################################################
###########################################################


############################################################
########################################################### # DEEP THROATJOB.

        # Meterle la polla hasta el fondo? Pregunta.

            pt "Puedo seguir jugando superficialmente con su boca o meterle la polla hasta el fondo de la garganta."

############################################################ afternight04_probabilty_checking

            call afternight04_probabilty_checking

############################################################

            menu afternight04__MMouth_dick_Deep_Question:
            
                pt "??Me voy a quedar sin polla...?"
                
                "<Met??rsela hasta el fondo de su garganta>":
                    
                    call p_Help
                    
                    jump afternight04__MMouth_dick_Deep_Yes
                
                "Mejor no tentar a la suerte.":
                    
                    call p_Help
                    
                    jump afternight04__MMouth_dick_Deep_After

#########################################################################
########################################################################
#######################################################################

############################################################

label afternight04__MMouth_dick_Deep_Yes:

    $ afternight04__MMouth_dick_Deep_Success_Cond = False
    $ randomnum_1to100 = renpy.random.randint(1, 100)

############################################################ afternight04_probabilty_checking02

    call afternight04_probabilty_checking02

############################################################
############################################################

    # IMAGE DEEP THROATJOB with dick.

    #$ afternight04__prehfix_RNipple_Lick = False

    #show afternight04_sexbattle_mc_tongue empty
    #with hpunch

##############################################################
#############################################################

   #HER REACTION:
############################################################
###########################################################
    #if afternight04__MMouth_dick_Deep_Success_Cond == True: #You succeded DEEPTHROATING. Not necessary here, used later.

    if afternight04__MMouth_dick_Deep_Success_Cond == False: # You Failed DEEPTHROATING

        ## NEGATIVE REACTIONS

        if afternight04_Nipple_Lick_Bite_Failed == 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                p "????AUUHH!!"

            elif randomnum_1to5 == 2:

                p "????AARRGHH!!"

            elif randomnum_1to5 == 3:

                p "????AAAII!!"

            elif randomnum_1to5 == 4:

                p "????AAOUCH!!"

            elif randomnum_1to5 == 5:

                p "????COO??OO!!"

        else: # You failed more than once.

            $ mc_body.pleasure -= 5

            $ randomnum_1to10 = renpy.random.randint(1, 10)

            if randomnum_1to10 == 1:

                p "??CO??O!"

            elif randomnum_1to10 == 2:

                p "??JODER!"

            elif randomnum_1to10 == 3:

                p "??ME HACES DA??O!"

            elif randomnum_1to10 == 4:

                p "??AAUUCH!"

            elif randomnum_1to10 == 5:

                p "??AAAIH!"

            elif randomnum_1to10 == 6:

                p "??MIERDA!"

            elif randomnum_1to10 == 7:

                p "??AAUUCH!"

            elif randomnum_1to10 == 8:

                p "??JODEEER!"

            elif randomnum_1to10 == 9:

                p "????DIOS!!"

            elif randomnum_1to10 == 10:

                p "??ME VAS A DEJAR SIN POLLA!"

##############################################################

############################################################
############################################################
### Dialogues of Failed:

    if afternight04__MMouth_dick_Deep_Success_Cond == False:

        $ debug ("Dick out of the mouth.")

        $ current_girl.pleasure -= 2
        $ current_girl.enslavement -= 6

        if afternight04__MMouth_dick_Deep_Failed == 1:

            $ mc_body.pleasure -= 4

            d "??Y tienes suerte de que no he mordido m??s fuerte!"

            p "Joder D??dac,"

            p "que me has hecho da??o..."

            d "??Como lo vuelvas a hacer te vas a quedar sin polla!"

            p "Entonces no te podr?? follar..."

            d "??Pues f??llame y d??jate de mariconadas!"

            if afternight04__MMouth_dick_Deep_Success > 0:

                d "????Qu?? cojones te pasa por la cabeza al pensar que me va a caber tu polla en mi garganta?!"

                d "????Est??s majara o qu???!"

                pt "Eso ya lo veremos..."

        elif afternight04__MMouth_dick_Deep_Failed == 2:
            $ mc_body.pleasure -= 4

            d "????PERO T?? ME ESCUCHAS?!"

            p "T?? quieres que me quede sin polla con que follarte..."

            d "??Lo que quiero es que te dejes de gilipolleces!"

            d "????Es que no has visto el pedazo de tama??o que tienes?!"

            if afternight04__MMouth_dick_Deep_Success > 0:

                d "??Eso no va a caber ni de co??a en mi garganta!"

                pt "Ya,"

                extend " ya..."

                pt "T?? espera..."

            else:

                d "??Eso no volver?? a entrar dentro de mi garganta ni de co??a!"

                p "Si ha entrado una vez,"

                p "puede volverlo a hacer..."

                d "??Joder que casi me ahogo!"

                d "Prefiero que te quedes sin polla que me ahogue con ella."

                p "..."

        elif afternight04__MMouth_dick_Deep_Failed == 3:
            $ mc_body.pleasure -= 5

            p "??CO??O!"

            p "??Haces da??o!"

            p "????Sabes?!"

            d "??POR LO VISTO NO LO SUFICIENTE!"

            p "..."

            d "A la pr??xima te dar?? m??s fuerte."

            p "????M??s a??n?!"

            pt "No parece que hable en broma..."

            pt "Por lo menos me est?? quitando las ganas de correrme..."

            pt "Pero que dolor..."

        elif afternight04__MMouth_dick_Deep_Failed == 4:
            $ mc_body.pleasure -= 6

            d "??T?? EST??S GILIPOLLAS!"

            d "????O QU?? CO??O TE PASA?!"

            d "??Te he dicho ya cuatro veces que no me metas la polla por la garganta!"

            d "A??n no entiendo como te la dejo meter en la boca..."

            d "Pero que me la metas hasta la garganta..."

            d "????DE QU?? COJONES VAS?!"

            if afternight04__MMouth_dick_Deep_Success > 0:

                d "??TU POLL??N NO ME VA A CABER!"

                d "??NI QUIERO QUE QUEPA!"

                d "??Es por mi co??o que la tienes que meter!"

                d "??Al final te voy a encadenar y violar!"

                p "..."

            else:

                p "No ser??a la primera vez que te la meto por la garganta."

                d "..."

                d "??T?? quieres que me ahogue con tu poll??n..."

                d "????No tienes suficiente con mi co??o?!"

                p "..."

                p "??Quieres una respuesta sincera?"

                d "..."

                d "C??llate."

            d "Que sepas que la pr??xima vez te morder?? con m??s fuerza."

            p "..."

        elif afternight04__MMouth_dick_Deep_Failed == 5:
            $ mc_body.pleasure -= 7

            p "??JODER D??DAC!"

            p "??En serio!"

            p "??Me vas a dejar sin polla!"

            d "??De verdad?"

            d "Pues tendr?? que buscarme otra..."

            p "..."

            d "??NI SE TE OCURRA VOLVER A INTENTAR METERME LA POLLA POR LA GARGANTA!"

            d "??Da gracias que no haga lo mismo con solo met??rmela en la boca!"

            d "Que ni eso te deber??a dejar hacer..."

            p "..."

        elif afternight04__MMouth_dick_Deep_Failed == 6:
            $ mc_body.pleasure -= 8

            p "??CO??OOO!"

            p "??ME HACES DA??O JODER!"

            d "Tienes suerte de que a??n no te salga sangre,"

            d "no ser?? porque no lo intento por eso..."

            if afternight04__MMouth_dick_Deep_Success > 5:

                p "??Si ya te la he metido bastantes veces por la garganta y bien que te empieza a gustar!"

                d "??Tssk!"

                d "??Eso es lo que a ti te parece!"

            elif afternight04__MMouth_dick_Deep_Success > 1:

                p "??Pero si ya te la he metido por la garganta varias veces!"

                d "??Y a poco que no me ahogas!"

                d "??Gilipollas!"

            else:

                p "..."

            pt "Si sigo as??,"

            pt "realmente me voy a quedar sin polla..."

        elif afternight04__MMouth_dick_Deep_Failed >= 7:
            $ mc_body.pleasure -= 8

            p "..."


############################################################
### Dialogues of Success

    elif afternight04__MMouth_dick_Deep_Success_Cond == True:

        $ current_girl.pleasure += 1
        $ current_girl.enslavement += 6

        if afternight04__MMouth_dick_Deep_Success == 1:

            n "Sin pens??rtelo mucho m??s, meneas con m??s vigor la cadera para profundizar a??n m??s en el interior de su boca."

            call afternight04__MMouth_dick_Deep_Success_Moans

            if afternight04__MMouth_dick_Success == 1:

                n "A pesar de que ni siquiera hab??as llegado a introducir tu miembro viril en su boca;"

            n "Logras penetrar hasta bien profundo en su garganta con tu enorme tranca."

            n "Su rostro se blanquecina,"

            n "y forceja con sus manos para intentar demostrarte que le falta aire,"

            n "pero al mismo tiempo tambi??n la tienes bien agarrada y debido a lo sumisa que est??,"

            n "tampoco demuestra mucha resistencia."

            n "Decides que lo m??s sensato es alejarte por el momento de su rostro."

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "I-"

            extend "Diota...!"

            d "????ACASO INTENTAS MATARME?!"

            d "????ES QUE SE TE HA IDO COMPLETAMENTE LA CABEZA?!"

            p "Cre??as que no cabr??a ah?? dentro"

            p "??Verdad?"

            d "*Kof* *Kof* *Kof*"

            d "??Se te va totalmente la pinza!"

            d "??Como vuelvas a intentar hacer algo as?? te voy a romper las pelotas!"

            pt "Bueno, no ha sido tal y como esperaba,"

            pt "pero con el tama??o que tengo,"

            pt "era dif??cil que no ocurriera esto."

            pt "Al menos la primera vez..."

        elif afternight04__MMouth_dick_Deep_Success == 2:

            n "Por segunda vez,"

            n "Introduces de nuevo tu miembro viril hasta lo m??s profundo,"

            call afternight04__MMouth_dick_Deep_Success_Moans

            n "sintiendo su garganta ardiente y presionando estrechamente toda tu polla."

            n "Sin respiraci??n alguna,"

            n "ves como D??dac empieza a perder color en su rostro"

            n "y empieza a indicarte que falta mucho para que pierda la consciencia."

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "??La Madre que te pari?? [protname]!"

            d "????Te crees que mi boca es un agujero negro?!"

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "Dios..."

            d "????Qu?? diablos pasa por tu cabeza?!"

            d "????No ves que la tienes demasiado grande?!"

            p "..."

        elif afternight04__MMouth_dick_Deep_Success == 3:

            call afternight04__MMouth_dick_Deep_Success_Moans

            n "Introduciendo de nueva tu enorme polla hasta el fondo de su garganta,"

            n "D??dac vuelve a sostener la respiraci??n,"

            n "Esta vez, no obstante, te atreves a empezar a moverla y follar suavemente su profunda garganta."

            d "????HHHMMM!!"

            n "Poco despu??s, vuelves a sacarla para dejarla respirar."

            call afternight04__MMouth_dick_Deep_Success_Cough

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "??EST??S COMO UNA PUTA CABRA!"

            d "??Al final me vas a matar en serio!"

            p "No exageres... Si en el fondo te est?? poniendo caliente y todo..."

            d "..."

            d "Tsssk..."

            d "??T?? flipas en colores!"

            pt "Ya..."

        elif afternight04__MMouth_dick_Deep_Success == 4:

            call afternight04__MMouth_dick_Deep_Success_Moans

            n "Sin demasiada sutileza, introduces el miembro entero en su interior,"

            n "mientras vuelves a desplazarte arriba y abajo,"

            n "foll??ndote lentamente su garganta."

            n "Aunque falta de aire, su rostro apenas muestra ya signos de ira o rabia descontrolada,"

            n "m??s bien parece como si fuera algo que empieza a serle morboso de alg??n modo retorcido."

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "??DIOS!"

            d "????Cuando pensabas sacarla?!"

            d "??Cada vez tardas m??s en quitarla!"

            p "Y t?? cada vez tardas m??s en quejarte..."

            p "con lo que parece que te va gustando..."

            d "..."

            d "Deber??a mord??rtela con fuerza a ver si se te pasan las ganas."

            if afternight04__MMouth_dick_Deep_Failed > 0:

                p "De hecho,"

                if afternight04__MMouth_dick_Deep_Failed == 1:

                    p "ya me la has mordido una vez..."

                    d "??Y no ha sido suficiente por lo visto!"

                elif afternight04__MMouth_dick_Deep_Failed > 1:

                    p "ya me la has mordido varias veces..."

                    d "??No las suficientes por lo visto!"

            p "..."

        elif afternight04__MMouth_dick_Deep_Success == 5:

            call afternight04__MMouth_dick_Deep_Success_Moans

            n "La expresi??n de D??dac va cambiando paulatinamente de un conformismo fr??o y distante a una bastante opuesta."

            n "A pesar del tama??o y de la fuerza con la que mueves tus caderas contra su nariz,"

            n "notas que con sus cuerdas vocales da signos de que empieza a disfrutar de su garganta profunda."

            n "A pesar de ello, crees que lo m??s sabio es no forzar demasiado la situaci??n."

            call afternight04__MMouth_dick_Deep_Success_Cough

            p "Quien te ha visto y quien te ve..."

            p "Hace apenas dos d??as, jam??s hubiera so??ado en que disfrutar??as tanto de mi polla en tu garganta D??dac..."

            d "...Kof KOF kof..."

            d "??Disfrutar...?"

            d "Sigue so??ando imb??cil..."

            d "??Solo espero que no te olvides que tambi??n tengo un co??o y est?? bastante insatisfecho a??n!"

            if current_girl.orgasm > 4:

                p "??Pero si ya llevas m??s de cuatro orgasmos!"

                d "Y puedo tener muchos m??s idiota..."

                d "As?? que no te contentes a??n..."

                pt "Ese rostro de gata en celo..."

                pt "la madre que lo pari??."

            elif current_girl.orgasm == 3:

                p "??Pero si ya llevas tres orgasmos!"

                d "????Y te parecen muchos?!"

                d "??Venga hombre!"

                d "Te ten??a por mejor semental [protname]..."

                p "..."

            elif current_girl.orgasm == 2:

                p "??Pero si ya llevas dos orgasmos!"

                d "..."

                d "????Est??s de co??a verdad?!"

                d "Con eso no tengo ni para empezar!"

                d "??Espero que dures mucho m??s!"

                p "..."

            elif current_girl.orgasm == 1:

                p "Pero llevas un orgasmo ya..."

                if mc_body.orgasm == 0:

                    d "Aunque t?? no te has corrido ninguna vez a??n,"

                    d "espero que dejemos de lado el pre-calentamiento y pasemos a la acci??n pronto."

                    p "..."

                elif mc_body.orgasm == 1:

                    d "????Y te sientes orgulloso?!"

                    d "T?? ya te has corrido una vez..."

                    d "??espero que aguantes bastante m??s!"

                    p "..."

                elif mc_body.orgasm == 2:

                    d "??Y T?? LLEVAS YA DOS IDIOTA!"

                    d "??NO ME TOQUES LAS NARICES!"

                    p "..."

            elif current_girl.orgasm == 0:

                d "????QUE A??N NO LLEVO NI UN JODIDO ORGASMO!!"

                if mc_body.orgasm == 0:

                    p "Yo tampoco..."

                    d "????Pues a qu?? co??o esperas?!"

                elif mc_body.orgasm == 1:

                    d "??Y T?? YA TE HAS CORRIDO UNA VEZ!"

                elif mc_body.orgasm == 2:

                    d "??????Y T?? YA LLEVAS DOS PUTAS CORRIDAS!!!"

                p "..."

        elif afternight04__MMouth_dick_Deep_Success == 6:

            call afternight04__MMouth_dick_Deep_Success_Moans

            n "Sin pudor alguno, arremetes con fuerza su cavidad oral al completo,"

            n "Mientras ella se vuelca para tragar tanto como puede y sientes sus sonidos guturales como vibraciones que avivan a??n m??s la notable sensibilidad de su estrecho pasillo."

            n "Sus labios se aferran a la base de tu polla mientras tus abdominales chocan incesantemente contra su nariz."

            pt "DIOSS..."

            n "Apartas r??pidamente la polla de su garganta para evitar correrte demasiado pronto."

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "Ahh..."

            d "Ya pensaba que te ibas a correr en mi garganta [protname]..."

            p "..."

            p "??Lo dices en serio?"

            if mc_body.orgasm == 2:

                d "Si no fuera por que ya llevas dos y estoy seguro que no aguantar??s una cuarta ronda..."

                d "Quiz??s no me disgustar??a del todo..."

            elif mc_body.orgasm == 1:

                d "Ya llevas un orgasmo,"

                d "si eres capaz luego de aguantar una tercera ronda,"

                d "no veo porque no..."

            elif mc_body.orgasm == 0:

                d "No llevas ning??n orgasmo, mientras reserves los dem??s para mi co??o,"

                d "no lo veo algo tan descabellado..."

            pt "??LA ESTOY CONVIRTIENDO EN UNA JODIDA PUTA NINF??MANA!"

        elif afternight04__MMouth_dick_Deep_Success >= 7:

            call afternight04__MMouth_dick_Deep_Success_Moans

            call afternight04__MMouth_dick_Deep_Success_Cough

            d "..."

## NOT FINISHED ## Will there be Cumshot for FACE - MOUTH - DEEPTHROAT for POSE03 ??

############################################################
###########################################################

############################################################
    jump afternight04__MMouth_dick_Deep_After #End of French Deep Kiss.

label afternight04__MMouth_dick_Deep_After:

############################################################
###########################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    if (afternight04__MMouth_dick_Success > 12) or (afternight04__MMouth_dick_Failed > 10) or (afternight04__MMouth_dick_Deep_Failed > 7) or (afternight04__MMouth_dick_Deep_Success > 7):

        call afternight04_RapeOrNot

    ###########################
    ##########################

    return


    ###########################
    ##########################

label afternight04__MMouth_dick_Deep_Success_Moans:

    $ randomnum_1to10 = renpy.random.randint(1, 10)

    if randomnum_1to10 == 1:

        #if current_pose.id == "pose_3":

            # DIDAC EXPRESSIONS

        d "??UHHMMM...!"

    elif randomnum_1to10 == 2:

        d "??HMMM...!"

    elif randomnum_1to10 == 3:

        d "??UGHMM...!"

    elif randomnum_1to10 == 4:

        d "AUHMM...!"

    elif randomnum_1to10 == 5:

        d "??MMFHMM...!"

    elif randomnum_1to10 == 6:

        d "??AUGHMM...!"

    elif randomnum_1to10 == 7:

        d "??MMHmm...!"

    elif randomnum_1to10 == 8:

        d "??UHGHMm...!"

    elif randomnum_1to10 == 9:

        d "??MUHFmm...!"

    elif randomnum_1to10 == 10:

        d "??HMMmm...!"

    return

label afternight04__MMouth_dick_Deep_Success_Cough:

    $ randomnum_1to5 = renpy.random.randint(1, 5)

    if randomnum_1to5 == 1:

        #if current_pose.id == "pose_3":

            # DIDAC EXPRESSIONS

        d "??COF! ??COF! ??COF!"

    elif randomnum_1to10 == 2:

        d "??COUGH! ??COUGH! ??COUGH!"

    elif randomnum_1to10 == 3:

        d "??KOFF! ??KOFF! KHAKK!"

    elif randomnum_1to10 == 4:

        d "??GAaack...! ????COUGH!! ??COUGH!"

    elif randomnum_1to10 == 5:

        d "??GAAAaa...g! ????KCOFF!! ????KOFF!!"

    return