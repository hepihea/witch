# default afternight04__MMouth_Tongue_Deep_Done = 0
# default afternight04__MMouth_Tongue_Deep_Success = 0
# default afternight04__MMouth_Tongue_Deep_Failed = 0
# default afternight04__MMouth_Tongue_Deep_Success_Cond = False

label MMouth_Tongue:

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
    $ __prefix = "MMouth_Tongue."

#########################################################

    $ mc_body.store["tongue"] = "MMouth_Tongue"

#########################################################
    
    $ afternight04__prehfix_MMouth_Tongue = True
    $ afternight04__a_prehfix_MMouth_Tongue = True
    
    call afternight04_sex_check_before
    
    label .manager:

        if current_pose.id == "pose_3":

            $ afternight04__MMouth_Tongue_Done += 1

            if mc_body.roll_success:
                $ afternight04__MMouth_Tongue_Success += 1

            else:

                if not "pass" in mc_body.result:

                    $ afternight04__MMouth_Tongue_Failed += 1

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
        $ debug ("First Orgasm for his. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_2:
        $ debug ("Second Orgasm for his. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_orgasm_3:
        $ debug ("Third Orgasm for his. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_his_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_1:
        $ debug ("First Orgasm for her. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_2:
        $ debug ("Second Orgasm for her. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_3:
        $ debug ("Third Orgasm for her. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .her_orgasm_4_plus:

        $ debug ("Infinite Orgasm for her. -description-.")

        call afternight04__MMouth_Tongue_her_orgasm
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_once:
        $ debug ("He passed, she failed. Once. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_twice:
        $ debug ("He passed, she failed. Twice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_thrice:
        $ debug ("He passed, she failed. Twice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fourth:
        $ debug ("He passed, she failed. Fourth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_fifth:
        $ debug ("He passed, she failed. Fifth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_sixth:
        $ debug ("He passed, she failed. Sixth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repetitive:
        $ debug ("He passed, she failed. More than once. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_repeated_lots:
        $ debug ("He passed, she failed. More than seven times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_once:
        $ debug ("He passed, she passed. Once. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_twice:
        $ debug ("He passed, she passed. Twice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_thrice:
        $ debug ("He passed, she passed. Thrice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fourth:
        $ debug ("He passed, she passed. Fourth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_fifth:
        $ debug ("He passed, she passed. Fifth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_sixth:
        $ debug ("He passed, she passed. Sixth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repetitive:
        $ debug ("He passed, she passed. Less than 7. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .his_roll_pass_her_roll_repeated_lots:
        $ debug ("He passed, she passed. More than seven times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_not_happened:
        $ debug ("Both failed on first try. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_once:
        $ debug ("Both failed. Once. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_twice:
        $ debug ("Both failed. Twice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_thrice:
        $ debug ("Both failed. Thrice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_fourth:
        $ debug ("Both failed. Fourth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_fifth:
        $ debug ("Both failed. Fifth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_sixth:
        $ debug ("Both failed. Sixth time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_repetitive:
        $ debug ("Both failed. Less than 7 times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_repeated_lots:
        $ debug ("Both failed. More than 7 times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_not_happened:
        $ debug ("He failed, she passed. Not happened. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_once:
        $ debug ("He failed, she passed. Once. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_twice:
        $ debug ("He failed, she passed. Twice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_thrice:
        $ debug ("He failed, she passed. Thrice. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fourth:
        $ debug ("He failed, she passed. Fourth Time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_fifth:
        $ debug ("He failed, she passed. Fifth Time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_sixth:
        $ debug ("He failed, she passed. Sixth Time. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"


    label .fail_her_roll_repetitive:
        $ debug ("He failed, She passed. Less than 7 times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

    label .fail_her_roll_repeated_lots:
        $ debug ("He failed, She passed. More than 7 times. Kissing her Mouth with your Tongue (French Kiss).")

        call afternight04__MMouth_Tongue
        
        jump expression __prefix + "call_screen"

####################################
###################################
####################################
###################################
####################################
###################################


    label afternight04__MMouth_Tongue:

        call afternight04__MMouth_Tongue_general

        return

    label afternight04__MMouth_Tongue_his_orgasm:

        call afternight04__MMouth_Tongue_general

        call afternight04_mostly_his_orgasm

        return

    label afternight04__MMouth_Tongue_her_orgasm:

        call afternight04__MMouth_Tongue_general

        call afternight04_mostly_her_orgasm

        return

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 01

label afternight04__MMouth_Tongue_general:

    ##############################################################
    #############################################################

    if current_pose.id == "pose_1": # HER REACTION is not necessary.

        $ mc_body.store["tongue"] == ""
        show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_mc_tongue_pussy empty
        with dissolve

    #elif current_pose.id == "pose_2": 

        #$ debug ("You can??t reach her mouth here.")

    elif current_pose.id == "pose_3": 

        ##########

        $ afternight04__MMouth_Tongue_Done += 1

        if mc_body.roll_success:

            $ afternight04__MMouth_Tongue_Success += 1

        else:

            if not "pass" in mc_body.result:

                $ afternight04__MMouth_Tongue_Failed += 1

        ##########

        $ debug ("In this position you can kiss her.")

##############################################################
#############################################################

    # Previous Tongue Action

    $ afternight04__a_prehfix_MClitoris_Tongue = False
    #$ afternight04__a_prehfix_MMouth_Tongue = False
    $ afternight04__a_prehfix_Pussy_Tongue = False
    $ afternight04__a_prehfix_Anal_Tongue = False  # Rim Job
    $ afternight04__a_prehfix_RNipple_Lick = False  # Rim Job

    #$ afternight04__a_prehfix_Remove = False


##############################################################
#############################################################

    ##############################################################
    #############################################################

    if current_pose.id == "pose_1":

        if current_girl.total_try == 1: #Don??t change that.

            show afternight04_sexbattle_d_mouth sad_Talkingx02_a
            show afternight04_sexbattle_d_eyes 02_a
            show afternight04_sexbattle_d_pupils front02_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            d "Se puede saber,"

            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
            with dissolve

            d "??Qu?? diablos est??s haciendo alargando el cuello y sacando la lengua como una jirafa?"

            show afternight04_sexbattle_d_mouth sad_Silentx04_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

            p "..."

            show afternight04_sexbattle_d_mouth sad_Silentx02_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows suspiciousx02_a
            with dissolve

            pt "Mierda,"

            extend " desde esta posici??n no llego..."

        elif current_girl.total_try == 2:

            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            d "??Otra vez sacando la lengua?"

            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            d "??Te est??s volviendo un perro?"

            show afternight04_sexbattle_d_mouth happy_Silentx03_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

            pt "Quiz??s,"

            extend " si lo agarro del brazo,"

            pt "pueda quit??rmelo de encima y as?? me resulte posible..."

        else:

            show afternight04_sexbattle_d_mouth sad_Silentx01_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve

            d "..."

            show afternight04_sexbattle_d_mouth sad_Silentx02_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows suspiciousx01_a
            with dissolve

            pt "??Por qu?? diablos insisto?"

            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

            pt "??Tengo que quit??rmelo de encima cogi??ndolo del brazo si quiero intentarlo!"

            $ current_girl.pleasure -= 5

        call screen dummy_screen()

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 02

    #elif current_pose.id == "pose_2": 

        #$ debug ("You can??t reach her mouth here.")

####################################
###################################
####################################
###################################
####################################
###################################_ POSE 03

   #HER REACTION:
############################################################
###########################################################

    elif current_pose.id == "pose_3": #POSE 02 no tiene Nipple.

        $ debug ("Kiss in her mouth, POSE 03.")

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

            if afternight04__MMouth_Tongue_Failed == 1:

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    d "????ME EST??S INTENTANDO BESAR?!"

                elif randomnum_1to5 == 2:

                    d "????QU?? COJONES?!"

                elif randomnum_1to5 == 3:

                    d "????PERO QU?? DIABLOS INTENTAS HACER?!"

                elif randomnum_1to5 == 4:

                    d "????LA MADRE QUE TE PARI??!!"

                elif randomnum_1to5 == 5:

                    d "????WHAT THE FUCK?!"

            else:

                $ randomnum_1to10 = renpy.random.randint(1, 10)

                if randomnum_1to10 == 1:

                    d "????OTRA VEZ?!"

                elif randomnum_1to10 == 2:

                    d "????EN SERIO?!"

                elif randomnum_1to10 == 3:

                    d "????TE CREES QUE SOY TU NOVIA?!"

                elif randomnum_1to10 == 4:

                    d "????ME TOMAS POR MARIC??N?!"

                elif randomnum_1to10 == 5:

                    d "????HAS INTENTADO METERME LA LENGUA?!"

                elif randomnum_1to10 == 6:

                    d "????TE HAS BEBIDO EL ENTENDIMIENTO?!"

                elif randomnum_1to10 == 7:

                    d "????A ESTO LO LLAMAS FOLLARME?!"

                elif randomnum_1to10 == 8:

                    d "????ESTO NO ES LO QUE TE HE PEDIDO!!"

                elif randomnum_1to10 == 9:

                    d "????QU?? CLASE DE MARIC??N EST??S HECHO?!"

                elif randomnum_1to10 == 10:

                    d "????DE ESTO NI HABLAR!!"

    ############################################################ # OFF image

                # POSE 01 and POSE 02 are not necessary.

            $ mc_body.store["tongue"] = ""
            show afternight04_sexbattle_mc_tongue empty

            with hpunch

    ############################################################
    ########################################################### # RNipple pose 0p3 Dialogue.

        
        
## TRIES

        $ debug ("HERE GOES DIALOGUE FOR RNipple_Lick pose 03")

        if (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 0:

            aj "This text should not appear. 5548"


        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 1:

            if mc_body.roll_success == True: #You succeded.

                d "..."

            else:

                d "????SE PUEDE SABER QUE EST??S HACIENDO ACERC??NDOTE TANTO A MI CARA?!"

                p "..."

                p "Joder D??dac..."

                p "??Nunca has besado a una t??a mientras te la est??s follando?"

                p "????O qu???!"

                d "??A una t??a s??!"

                d "??A un t??o no!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "??Y MUCHO MENOS SI HAS PASADO ESA LENGUA POR MI JODIDO ANO!"

                    d "????Te crees que me mola el sabor a mierda como a ti?!"

                else:

                    d "??Y MUCHO MENOS A TI!"

                    d "??QUE TENGA CO??O NO SIGNIFICA QUE SEA GAY!"

                d "??GILIPOLLAS!"

                p "Que me pidas que te folle el co??o no es nada homosexual..."

                p "Todo el sentido del mundo..."

                d "????Cuando has visto que un gay tenga co??o?!"

                p "??Nunca has visto a una mujer que se ha cambiado el sexo mediante un tratamiento hormonal?"

                d "????QU???!"

                p "Adem??s,"

                p "lo que acabas de decir es muy homof??bico,"

                p "que lo sepas."

                d "??NI SE TE OCURRA BESARME!"

                d "????QUEDA CLARO?!"

                p "..."

                pt "Habr?? que esperar a tenerlo m??s sumiso,"

                pt "o realmente me va a meter una hostia al final..."

        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 2:

            if afternight04__MMouth_Tongue_Failed == 1:

                d "??Me cago en Dios [protname]!"

                d "????Se puede saber qu?? cojones haces?!"

                p "Antes no te me has quejado..."

                d "??Porque me cogiste por sorpresa!"

                d "??No hagamos estas putas mariconadas!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "Y menos habiendo metido tu lengua en mi parte trasera..."

                    d "????Eres consciente del asco que me da esto?!"

                if afternight04__MMouth_Tongue_Deep_Success > 0:

                    p "Pero si te he besado con lengua hasta el fondo sin que te quejaras..."

                    d "..."

                p "No ser?? que ibas tan cachondo,"

                p "que te ha dado completamente igual..."

                p "o incluso quiz??s que no te haya disgustado tanto que no lo quieres ni admitir..."

                d "??No soy gay!"

                d "????Queda claro?!"

                p "Vale,"

                extend " vale..."

                pt "Por ahora..."

            elif afternight04__MMouth_Tongue_Failed == 2:

                d "????Es que hablo Chino?!"

                d "??Aparta tu maldito careto!"

                d "??CO??O!"

        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 3:

            if afternight04__MMouth_Tongue_Failed == 1:

                d "??As?? no [protname]!"

                d "??Esto no es follar!"

                d "??No quiero hacer estas mariconadas contigo!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "??Y mucho menos si me has metido esa lengua por el puto culo!"

                p "??Te refieres a que quieres dejar de follar?"

                d "..."

                d "Ya me has entendido..."

                p "En los dos besos anteriores no te me has quejado as??..."

                if afternight04__MMouth_Tongue_Deep_Success > 0:

                    p "Y eso que te hecho un beso de torniquete..."

                d "..."

                d "Tssk..."

            elif afternight04__MMouth_Tongue_Failed == 2:

                d "??Ya basta!"

                d "????No crees?!"

                d "??No me va besarme con un t??o!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "Y mucho menos si ha habido beso negro previo..."

                if afternight04__MMouth_Tongue_Deep_Success < 0:

                    p "Pero sino he llegado a meterte la lengua en la boca..."

                    if afternight04__MMouth_Tongue_Deep_Failed > 0:

                        d "??No ser?? porque no lo has intentado!"

                        p "..."

                    else:

                        d "??Y ni lo har??s!"

                d "????Lo entiendes?!"

                p "Antes no te ha disgustado tanto..."

                d "??Pues te lo digo ahora!"

                d "??Para ya!"

                pt "Est?? claro que necesita ser m??s sumiso si quiero que no se me queje..."

            elif afternight04__MMouth_Tongue_Failed == 3:

                d "??YA ES LA TERCERA VEZ QUE TE LO REPITO!"

                d "??Y SIGUES INSISTIENDO!"

                d "??No me toques los huevos [protname]!"

                if afternight04__MMouth_Tongue_Deep_Failed > 0:

                    d "??Y ni se te ocurra volver a intentar meterme la jodida lenga!"

                    d "??O te la corto de un bocad!"

                d "??No me van estas mariconadas!"


        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 4:

            if afternight04__MMouth_Tongue_Failed == 1:

                if afternight04__MMouth_Tongue_Deep_Failed > 0:

                    d "????Otra vez intentando meterme la lengua?!"

                    p "Por ahora solo intentaba besarte los labios..."

                d "Al final pensar?? que te gustaba cuando era hombre y no quieres admitirlo."

                p "Quiz??s as?? fuera."

                d "..."

                d "??Qu???"

                p "Es la primera vez que te me quejas,"

                p "no te disgusta tanto como quieres aparentar..."

                d "Tssk..."

            elif afternight04__MMouth_Tongue_Failed == 2:

                d "??Esto empieza a pasar de casta??o oscuro!"

                d "??Deja de intentar besarme!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "??Y mucho menos si ha habido beso negro previo!"

                if afternight04__MMouth_Tongue_Deep_Failed > 0:

                    d "??Que no ser??a la primera vez que me intentas meter la lengua!"

                p "Ya te he besado en los labios cuatro veces,"

                p "y en un par no te ha disgustado tanto..."

                d "Tssk..."

            elif afternight04__MMouth_Tongue_Failed == 3:

                d "??Joder!"

                d "??Deja de besarme!"

                d "??Al final te voy a meter una hostia!"

            elif afternight04__MMouth_Tongue_Failed == 4:

                ono "PUM"

                $ current_girl.pleasure -= 2
                $ current_girl.enslavement -= 3
                $ mc_body.pleasure += 3

                n "Recibes un fuerte golpe en la nariz,"

                n "que no solo te aparta sino que adem??s te causa un da??o considerable."

                d "????CUANTAS VECES TE LO TENGO QUE REPETIR?!"

                d "??ME EST??S CALENTANDO!"

                d "??PERO NO PRECISAMENTE DE LA FORMA QUE TE HE PEDIDO!"

                if afternight04__MMouth_Tongue_Deep_Failed > 0:

                    d "??Y NI SE TE OCURRA VOLVER A METERME LENGUA!"

                d "??JODER!"

                pt "????Por qu?? co??o me pone cachondo que me pegue?!"

                pt "????Soy masoquista o qu?? co??o pasa?!"

        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) == 5:

            if afternight04__MMouth_Tongue_Failed == 1:

                d "??No te cansas de estar bes??ndome como si fuera tu jodida novia?"

                if ((afternight04__MMouth_Tongue_Deep_Failed) or (afternight04__MMouth_Tongue_Deep_Success)) > 0:

                    d "Que encima vas meti??ndome lengua..."

                    if (afternight04__MMouth_Tongue_Deep_Success > afternight04__MMouth_Tongue_Deep_Failed):

                        p "Pero juzgando por tus reacciones,"

                        p "en general parece que no te haya disgustado tanto..."

                        d "..."

                    elif afternight04__MMouth_Tongue_Deep_Success == 0:

                        d "??Y no ha habido ni una sola vez que me haya gustado!"

                        p "..."

                p "Es el quinto beso que te doy en los labios,"

                p "y no me has dicho absolutamente nada en los otros cuatro,"

                if ((afternight04__MMouth_Tongue_Deep_Failed) or (afternight04__MMouth_Tongue_Deep_Success)) > 0:

                    d "En los labios no,"

                    d "pero con tu jodida lengua s??."

                    p "Ya..."

                    if (afternight04__MMouth_Tongue_Deep_Success) > (afternight04__MMouth_Tongue_Deep_Failed):

                        p "Pero bien que en su mayor??a no te ha disgustado tanto como quieres aparentar..."

                    if afternight04__Anal_Tongue_Success > 0:

                        p "y eso que mi lengua ha pasado por tu trasero antes..."

                        d "..."

                p "As?? que quiz??s te guste m??s a ti que a mi..."

                d "??En tus sue??os!"

            elif afternight04__MMouth_Tongue_Failed == 2:

                d "??En serio!"

                d "??Deja de besarme!"

                d "??Se me est?? poniendo la piel de gallina y al final voy a vomitar!"

                p "T?? tampoco hueles a rosas,"

                p "es evidente quien se ha bebido toda la cerveza de la nevera..."

                if afternight04__Anal_Tongue_Success > 0:

                    d "??Y tu lengua sabe a mierda!"

                    p "A tu mierda en todo caso..."

                d "..."

                d "No me refer??a tu aliento..."

                p "??Entonces?"

                d "Yo..."

                d "??Que no me beses m??s!"

                if ((afternight04__MMouth_Tongue_Deep_Failed) or (afternight04__MMouth_Tongue_Deep_Success)) > 0:

                    if (afternight04__MMouth_Tongue_Deep_Failed) > (afternight04__MMouth_Tongue_Deep_Success):

                        d "??Y menos con lengua!"

                d "??Leches!"

                p "..."

                d "Tssk..."

            elif afternight04__MMouth_Tongue_Failed == 3:

                d "??Deja ya de besarme co??o!"

            elif afternight04__MMouth_Tongue_Failed == 4:

                d "??TE EST??S GANANDO UNA BUENA HOSTIA!"

            elif afternight04__MMouth_Tongue_Failed == 5:

                ono "PUM"

                $ current_girl.pleasure -= 2
                $ current_girl.enslavement -= 3
                $ mc_body.pleasure += 3

                d "??ME CAGO EN LOS TORNILLOS QUE SUJETAN LA FAROLA QUE ALUMBRA LA TUMBA DE TU PUTA MADRE!"

                d "??Ya es la quinta vez que te pido que dejes de besarme!"

                d "??Al final pensar?? que te est??s enamorando de mi!"

                p "..."

                d "??Y eso no me mola nada!"

                p "..."

                p "??Hac??a falta decir eso de mi madre?"

                d "..."

                d "??Como vuelvas a intentarlo te voy a dar un puto bofet??n!"

                d "??HABLO EN SERIO!"

                p "..."

                pt "Y me sigue poniendo cachondo que me pegue..."

                pt "Manda narices..."

        elif (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) >= 6:

            if afternight04__MMouth_Tongue_Failed == 1:

                d "????Otra vez con esta mariconada?!"
                
                d "????Es que te est??s enamorando de mi?!"

                p "??Has estado enamorado de todas las chicas a las que has besado?"

                d "..."

                p "Las otras veces te ha gustado m??s de lo que eres capaz de confesar."

                p "No seas tan quejica y disfruta."

                if afternight04__Anal_Tongue_Success > 0:

                    p "Adem??s, he pasado mi lengua por tu culo y no te me has quejado por eso..."

                    d "..."

                if (afternight04__MMouth_Tongue_Deep_Success) > (afternight04__MMouth_Tongue_Deep_Failed):

                    if afternight04__MMouth_Tongue_Deep_Success > 5:

                        p "Eso sin mencionar que has disfrutado un mont??n de que te besara con lengua..."

                    else:

                        p "Eso sin mencionar que has disfrutado bastante de mi beso con lengua..."

                d "Gilipollas..."

            elif afternight04__MMouth_Tongue_Failed == 2:

                d "????Otra vez intentando besarme?!"

                p "Las otras veces no solo lo he intentado,"

                p "sino que no te me has quejado tanto..."

                if (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) > 0:

                    if (afternight04__MMouth_Tongue_Deep_Success) > (afternight04__MMouth_Tongue_Deep_Failed):

                        if afternight04__MMouth_Tongue_Deep_Failed == 0:

                            p "Ni siquiera te me has quejado una sola vez de que te haya besado con lengua..."

                        else:

                            p "Y en general te ha gustado bastante que te besara con lengua."

                d "??Pues me quejo ahora!"

                d "??Se me hace muy raro que t?? y yo nos besemos!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "??Y mucho m??s cuando tu lengua ha pasado hasta el fondo por mi trasero!"

                if (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) > 0:

                    if (afternight04__MMouth_Tongue_Failed) > (afternight04__MMouth_Tongue_Success):

                        d "??Y como vuelvas a besarme con lengua te vas a quedar sin ella!"

                d "??Joder!"

                pt "En eso tengo que coincidir,"

                pt "raro es..."

            elif afternight04__MMouth_Tongue_Failed == 3:

                d "??Ya basta de besitos!"

                d "??No crees?"
                
                d "????Te crees que soy una colegiala quincea??era?!"

                d "????O est??s tratando de ser rom??ntico conmigo?!"

                if afternight04__Anal_Tongue_Success > 0:

                    d "O quiz??s est??s intentando que saboree a mierda"

                    d "despu??s de haber pasado tu lengua entera por mi jodido trasero."

                p "Lo que intento es ponerte m??s cachonda,"

                p "Y no puedes negarme que has disfrutado alg??n que otro beso..."

                d "pff..."

                d "??Lo que quiero es que..."

                p "Te folle como una puta ninf??mana sin juego previo..."

                p "S??,"

                p "lo s??,"

                extend " lo s??..."

                p "te repites m??s que una vieja cascarrabias..."

                d "Tssk..."

            elif afternight04__MMouth_Tongue_Failed == 4:

                d "????No te cansas de tanto besuqueo maripos??n?!"

                if (afternight04__MMouth_Tongue_Success + afternight04__MMouth_Tongue_Failed) > 0:

                    p "Tambi??n te he besado con lengua..."

                    d "??Peor me lo pones!"

                d "Cre?? que eras mejor semental!"

                d "Al final va resultar que eres un bujarr??n profesional y no lo sab??a."

                p "Eres t?? quien me ha pedido que te folle con mi polla hasta el fondo."

                d "..."

                d "??Que man??a tienes en mezclar las cosas!"

                d "????No puede gustarme que me folles sin tener que hacer de julandrones?!"

                p "Quiz??s si dejaras de usar estas palabras tan vulgares para menospreciar algo que no te gusta..."

                d "Ohh..."

                d "??Te sientes ofendido \"pu??alete\"?"

                d "Quiz??s es porque realmente te sientes identificado."

                p "??Y qu?? si as?? fuera?"

                p "??Querr??as que dejara de follarte?"

                d "..."

                d "..."

                d "??Lo eres?"

                p "??Dejo de follarte?"

                d "..."

                d "No."

                $ current_girl.enslavement += 2

                p "??Pues c??llate la puta boca idiota!"

                d "..."

                d "..."

            elif afternight04__MMouth_Tongue_Failed == 5:

                d "??Te lo digo en serio [protname]!"

                d "??La pr??xima vez que intentes besarme,"

                if afternight04__Anal_Tongue_Success > 0:

                    d "Y m??s despu??s de haber metido tu lengua en mi puto ano,"

                d "te voy a dar un bofet??n que te desencajar?? la mand??bula!"

                p "..."

            elif afternight04__MMouth_Tongue_Failed == 6:

                ono "SLAP"

                $ current_girl.pleasure -= 2
                $ current_girl.enslavement -= 3
                $ mc_body.pleasure += 4

                d "Mi mano va a quedar roja,"

                d "pero tu cara va a parecer un poema como no pares."

                p "Abofetear es de chicas."

                d "????Prefieres un golpe de pu??o?!"

                p "..."

                d "No quiero que te pongas a sangrar encima de mi,"

                d "??lo que quiero es que me folles!"

                d "??CO??O!"

                pt "En serio,"

                pt "no es posible que un bofet??n que me dejar?? la mejilla roja durante una semana,"

                pt "me haya puesto tan cachondo..."

            elif afternight04__MMouth_Tongue_Failed >= 7:

                ono "SLAP"

                $ current_girl.pleasure -= 3
                $ current_girl.enslavement -= 3
                $ mc_body.pleasure += 5

                p "..."

            #HIS SUCCESS:

#########################################################################
########################################################################
#######################################################################

    # NOT FINISHED Writing DIalogue. -

        if mc_body.roll_success == True:  # Only Kissing Lips.

            if afternight04__MMouth_Tongue_Success == 1:

                #"He passed, she failed. First SUCESS.

                n "Durante unos segundos, y aunque parezca extra??o, el silencio reina el lugar."

                n "Su expresi??n facial pierde viveza y sus p??rpados decaen lentamente,"

                n "mientras tus labios se acercan a los suyos uni??ndose en un suave y aparentemente inocente beso."

            elif afternight04__MMouth_Tongue_Success == 2:

                d "[protname] Yo..."

                if (afternight04__MMouth_Tongue_Deep_Success < 0) and (afternight04__MMouth_Tongue_Deep_Failed > 0):

                    n "Aunque tus intentos de besarla con lengua han resultado en un fracaso absoluto,"

                    n "Parece que su empe??o para emprender una conversaci??n ha cesado completamente,"

                else:

                    n "A pesar de su intento para emprender una conversaci??n,"

                n "el silencio vuelve a reinar y sus labios se vuelven a enlazar con los tuyos"

                n "en un tierno y discreto beso."

            elif afternight04__MMouth_Tongue_Success == 3:

                d "..."

                n "Apenas ofreciendo resistencia;"

                if (afternight04__MMouth_Tongue_Deep_Success < 0) and (afternight04__MMouth_Tongue_Deep_Failed > 0):

                    pt "Aunque besarla con lengua no ha sido a??n lo que me esperaba,"

                    pt "si me mantengo fuera de su boca,"

                    pt "parece que no le molesta demasiado..."

                n "Tus labios vuelven a mezclarse con los suyos,"

                n "percibiendo c??mo su mand??bula va cediendo poco a poco m??s terreno"

                n "mientras sus p??rpados completamente cerrados,"

                n "demuestran que empieza a abandonarse a las caricias que ofreces con el borde de tu boca."

            elif afternight04__MMouth_Tongue_Success == 4:

                d "Idiota..."

                if (afternight04__MMouth_Tongue_Deep_Success < 0) and (afternight04__MMouth_Tongue_Deep_Failed > 0):

                    n "A pesar de haber fracasado estrepitosamente en tu intento de besarla con lengua,"

                    n "Parece que manteni??ndote en sus labios,"

                n "No solo cesa cualquier intento de resistencia,"

                n "te da hasta la sensaci??n, que su mand??bula empieza a desplazarse,"

                n "acompa????ndote en ese beso discreto pero reservado para ambos."

            elif afternight04__MMouth_Tongue_Success == 5:

                n "Sin pr??cticamente ninguna resistencia,"

                n "sientes el calor de sus labios;"

                if afternight04__MMouth_Tongue_Deep_Success < 0:

                    n "Aunque su boca permanece pr??cticamente cerrada"

                    n "y a??n no logras alcanzar el interior de su boca con tu lengua."

                else:

                    n "y como paulatinamente,"

                    n "empieza a relajar mejor su mand??bula acariciando con cierto disimulo"

                    n "la punta de su lengua entre sus dientes."

            elif afternight04__MMouth_Tongue_Success == 6:

                n "La calidez de vuestros besos va cobrando cada vez m??s pasi??n."

                n "Aunque es un fervor que se mantiene por un fr??gil silencio por ambas partes,"

                n "y que cada vez parece que lo est?? disfrutando m??s;"

                n "pronto no se sentir?? satisfecha solo con besarse."

            elif afternight04__MMouth_Tongue_Success >= 7:

                d "..."

############################################################
###########################################################


############################################################
########################################################### # DEEP French Kiss.

        # Meterle la lengua hasta el fondo? Pregunta.

            pt "Puedo besarle superficialmente por los labios o meterle la lengua y jugar con la suya."

############################################################ afternight04_probabilty_checking

            call afternight04_probabilty_checking

############################################################

            menu afternight04__MMouth_Tongue_Deep_Question:
            
                pt "??Me va a morder la lengua...?"
                
                "<Usar tu lengua para juguetear con la suya>":
                    
                    call p_Help
                    
                    jump afternight04__MMouth_Tongue_Deep_Yes
                
                "Mejor no tentar a la suerte.":
                    
                    call p_Help
                    
                    jump afternight04__MMouth_Tongue_Deep_After


############################################################

label afternight04__MMouth_Tongue_Deep_Yes:

    $ afternight04__MMouth_Tongue_Deep_Success_Cond = False
    $ randomnum_1to100 = renpy.random.randint(1, 100)

############################################################ afternight04_probabilty_checking02

    call afternight04_probabilty_checking02

############################################################
############################################################

    # IMAGE DEEP FRENCH KISS with Tongue.

    #$ afternight04__prehfix_RNipple_Lick = False

    #show afternight04_sexbattle_mc_tongue empty
    #with hpunch

##############################################################
#############################################################

    if afternight04__MMouth_Tongue_Deep_Success_Cond == True: #You succeded BITING.

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "??MNMhh...!"

        elif randomnum_1to5 == 2:

            d "??HuMhfmm...!"

        elif randomnum_1to5 == 3:

            d "??UMffhmm...!"

        elif randomnum_1to5 == 4:

            d "??MMhmfm...!"

        elif randomnum_1to5 == 5:

            d "??HHMMfmm...!"

    else: # You Failed Biting

        ## NEGATIVE REACTIONS

        if afternight04__MMouth_Tongue_Deep_Failed == 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "????[protname]?!"

            elif randomnum_1to5 == 2:

                d "????EUH?!"

            elif randomnum_1to5 == 3:

                d "????Pero qu?? cojones?!"

            elif randomnum_1to5 == 4:

                d "??Pero qu?? diablos!"

            elif randomnum_1to5 == 5:

                d "????Se te ha ido completamente la pinza?!"

        else: # You failed more than once.

            $ randomnum_1to10 = renpy.random.randint(1, 10)

            if randomnum_1to10 == 1:

                d "????Otra vez?!"

            elif randomnum_1to10 == 2:

                d "????Es que quieres que te arranque la lengua de un mordisco?!"

            elif randomnum_1to10 == 3:

                d "????Me est??s metiendo de nuevo la lengua?!"

            elif randomnum_1to10 == 4:

                d "??Qu?? clase de julandr??n crees que soy?!"

            elif randomnum_1to10 == 5:

                d "??Te crees que esto es una pel??cula de {i}Hollywood{/i}?!"

            elif randomnum_1to10 == 6:

                d "????Te crees que somos franceses?!"

            elif randomnum_1to10 == 7:

                d "??Al final te voy a morder la lengua!"

            elif randomnum_1to10 == 8:

                if afternight04__Anal_Tongue_Success > 0:

                    d "????Eres consciente de que has metido esa lengua por mi culo?!"

                else:

                    d "????Pero qu?? diablos pretendes?!"

            elif randomnum_1to10 == 9:

                d "??Al final te voy a escupir en la cara!"

            elif randomnum_1to10 == 10:

                d "??Te morder?? tan fuerte en el labio que te pasar??s una semana comiendo con pajilla!"


##############################################################

############################################################
############################################################
### Dialogues of Failed:

    if afternight04__MMouth_Tongue_Deep_Success_Cond == False:

        $ current_girl.pleasure -= 1
        $ current_girl.enslavement -= 3

        if afternight04__MMouth_Tongue_Deep_Failed == 1:

            d "????Qu?? co??o pasa contigo?!"

            if afternight04__Anal_Tongue_Success > 0:

                d "Primero me metes la lengua por el culo,"

                d "????y ahora pretendes que la saboree?!"

            d "??T??o!"

            if afternight04__MMouth_Tongue_Deep_Success < 0:

                d "??Estabas intentando meterme la lengua en mi boca!"

                d "????Pero te das cuenta de ello?!"

            if afternight04_Pussy_dick_med_Speed_0_Done == 0:

                p "Lo que veo es que te he metido la polla en el co??o y eso no te parece tan raro."

            else:

                p "Y pedirme que te folle,"

                p "no es nada raro."

            if afternight04__MMouth_Tongue_Deep_Success > 0:

                p "Adem??s,"

                if afternight04__MMouth_Tongue_Deep_Success > 4:

                    p "ya llevo bes??ndote con lengua varias veces,"

                    p "y lo has disfrutado todas y cada una de las veces que lo he hecho hasta ahora..."

                else:

                    p "no es la primera vez que te beso con lengua,"

                    p "y no te me has quejado tanto antes..."

            d "..."

            d "No me mola besarme contigo [protname]."

            p "..."

            d "??Me siguen gustando las mujeres!"

            d "????Vale?!"

            d "Es solo que..."

            p "??S???"

            d "No tienes ni puta idea de lo que he pasado este ??ltimo d??a..."

            d "??NI PUTA IDEA!"

            d "Sino quieres follarme me lo dices y punto."

            p "..."

            d "..."

            d "Por favor..."

            p "..."

        elif afternight04__MMouth_Tongue_Deep_Failed == 2:

            d "????No te basta solo con besarme que encima me quieres meter la lengua hasta el fondo?!"

            if afternight04__Anal_Tongue_Success > 0:

                d "????Te crees que no sabe a mierda tu lengua despu??s de hab??rmelo pasado por el culo?!"

                p "Es tu mierda."

                d "????Y qu?? diferencia hay?!"

                if afternight04__Anal_Tongue_Success > afternight04__Anal_Tongue_Failed:

                    p "Pero bien que lo has disfrutado m??s veces de las que te has quejado..."

                    d "..."

                    d "Eso no tiene nada que ver."

            d "??Ya basta!"

        elif afternight04__MMouth_Tongue_Deep_Failed == 3:

            d "????Otra vez meti??ndome lengua?!"

            d "??Si ya me parece de maripos??n el besarnos!"

            d "??No te digo lo que me parece hacerlo con lengua!"

            p "..."

        elif afternight04__MMouth_Tongue_Deep_Failed == 4:

            d "??Ya llevas bes??ndome con lengua [(afternight04__MMouth_Tongue_Deep_Success + afternight04__MMouth_Tongue_Deep_Failed)] veces!"

            if afternight04__MMouth_Tongue_Deep_Success < 0:

                d "????Acaso has visto que me haya gustado alguna vez?!"

                p "Si me dejaras probarlo,"

                p "seguramente te gustar??a m??s de lo que te imaginas."

                d "??QUE ME DEJES LA LENGUA EN PAZ HOSTIAS!"

            else:

                if afternight04__MMouth_Tongue_Deep_Success > 5:

                    p "Y llevas disfrut??ndolo m??s veces de las que te has llegado a quejar..."

                    d "..."

                else:

                    p "Y lo has disfrutado alguna que otra vez..."

                    d "????Esa es tu excusa?!"

                    p "Me parece una excusa razonable,"

                    p "especialmente teniendo en cuenta que no me lo pones nada f??cil."

                    d "..."

        elif afternight04__MMouth_Tongue_Deep_Failed == 5:

            d "??Me da la sensaci??n que has visto demasiadas pel??culas rom??nticas!"

            d "??Deja de besarme con lengua como si fu??ramos una jodida pareja!"

            p "..."

        elif afternight04__MMouth_Tongue_Deep_Failed == 6:

            d "????LA PR??XIMA VEZ TE VOY A MORDER LA LENGUA!"

            d "??Te lo juro!"

        elif afternight04__MMouth_Tongue_Deep_Failed >= 7:

            $ mc_body.pleasure += 3
            $ current_girl.pleasure += 1
            $ current_girl.enslavement -= 5

            p "??AU!"

            with hpunch

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "??No aprendes!"

            elif randomnum_1to5 == 2:

                d "??A ver si hay huevos de volverlo a intentar!"

            elif randomnum_1to5 == 3:

                d "????Lo quieres volver a probar?!"

            elif randomnum_1to5 == 4:

                d "????No te cansas?!"

            elif randomnum_1to5 == 5:

                d "????No te duele suficientemente la lengua?!"

                d "????Quieres que vuelva a mord??rtela?!"

            ### #Your reaction.

            if randomnum_1to5 == 1:

                pt "??Y encima me pone caliente que me muerda!"

            elif randomnum_1to5 == 2:

                pt "??Pero si podr??a haberme hecho sangre!"

                pt "????Por qu?? co??o me pongo m??s caliente?!"

            elif randomnum_1to5 == 3:

                pt "??Para mear y no echar gota!"

                pt "????Por qu?? cojones me pone caliente que me muerda?!"

            elif randomnum_1to5 == 4:

                pt "????En serio?!"

                pt "????Se me pone m??s dura cuando me muerde?!"

                pt "????Qu?? clase de parafilia tengo?!"

            elif randomnum_1to5 == 5:

                pt "????Por qu?? co??o me pone cachondo que me muerda la lengua?!"

############################################################
### Dialogues of Success

    elif afternight04__MMouth_Tongue_Deep_Success_Cond == True:

        $ current_girl.pleasure += 2
        $ current_girl.enslavement += 4

        if afternight04__MMouth_Tongue_Deep_Success == 1:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Sin demasiado disimulo, consigues abrirte paso en su interior"

            n "sintiendo el calor de su aliento, al mismo tiempo que consigues dar el primer contacto con su ardiente y h??meda lengua,"

            n "a pesar de que su mand??bula sigue siendo algo r??gida y su expresi??n facial ya no es tan relajada como antes."

            n "Poco a poco percibes como vuelve a dejarse llevar por la situaci??n."

            d "HhhhMmm..."

            n "Poco despu??s decides que lo m??s acertado es no seguir forzando la situaci??n y separas tus labios de los suyos."

            show afternight04_sexbattle_effects empty
            with dissolve

            d "..."

            d "??A qu?? co??o ha venido esto?"

            p "Ten??a ganas de besarte."

            d "??Y qu?? co??o est??bamos haciendo antes?"

            p "Me refiero a besarnos como personas adultas,"

            p "no como si tuvi??ramos quince a??os."

            d "..."

            d "Esto me da muy mal rollo [protname]."

            p "??Por qu?? te ha gustado m??s de lo que te hab??as imaginado y tienes miedo de querer seguir haci??ndolo?"

            d "..."

            d "????Qu???!"

            d "No..."

            d "??Ni se te ocurra!"

            pt "Ya..."

        elif afternight04__MMouth_Tongue_Deep_Success == 2:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Con cierta tenacidad, consigues introducir tu lengua a trav??s de sus dientes,"

            n "no sin sentir el temor de quedarte sin lengua en cualquier momento."

            n "Poco a poco vas sintiendo como su maxilar inferior se va relajando"

            n "y cayendo por su propio peso, con lo que te permite juguetear con su lengua con mejor soltura."

            show afternight04_sexbattle_effects empty
            with dissolve

            n "Al abrir los ojos, descubres que tu compa??ero de piso sigue con los p??rpados cerrados."

            p "Desde luego,"

            p "te estoy haciendo sufrir de un modo indescriptible."

            d "????Euh?!"

            d "??Tsssk!"

            d "??Voy cachonda!"

            d "??Por eso me puedes hacer estas mariconadas!"

            d "??Pero que no se te pase por la cabeza ni por un solo segundo que esto me est?? gustando lo m??s m??nimo!"

            p "Eres un hip??crita."

            d "..."

            d "Tssk..."

        elif afternight04__MMouth_Tongue_Deep_Success == 3:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Con la mand??bula pr??cticamente suelta, consigues llegar con facilidad a su interior,"

            n "d??nde vuelves a saborear su ardiente lengua, que aunque pr??cticamente de forma inapreciable,"

            n "su lengua empieza a juguetear con la tuya,"

            n "mostrando cierto inter??s al mover su mand??bula"

            n "y saboreando el beso de forma algo t??mida y despreocupada."

            show afternight04_sexbattle_effects empty
            with dissolve

            n "Te apartas con cierta elegancia y artima??a del calor de su boca,"

            n "dej??ndola con los labios a??n entreabiertos."

            p "Sin lugar a dudas,"

            p "se te ve sufriendo de una forma horrorosa..."

            d "..."

            d "Tssk..."

            d "??Idiota!"

        elif afternight04__MMouth_Tongue_Deep_Success == 4:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Con una ??ltima chispa de resistencia por su parte, que ignoras por completo,"

            n "vuelves a introducirte en su interior deslizando tu lengua por debajo de la suya,"

            n "mientras sientes como empieza desplazarla aparentemente de forma distra??da,"

            n "acariciando la parte superior de tu lengua mientras se desplaza por los lados"

            n "y su cabeza empieza a inclinarse mientras se aferra a tus labios."

            show afternight04_sexbattle_effects empty
            with dissolve

            n "Como si cortaras el alioli, apartas tu rostro del suyo en medio del desenfreno,"

            n "dej??ndola completamente abstra??da y con la lengua a??n buscando la tuya."

            d "..."

            p "Pensaba que lo detestabas..."

            p "??Tanto te gusta que quieres continuar?"

            d "Tssk..."

            d "Solo te estoy siguiendo el juego para que me sigas follando y te dejes de gilipolleces."

            d "??No te hagas ideas raras!"

            p "Ya..."

        elif afternight04__MMouth_Tongue_Deep_Success == 5:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Al desplazar tus labios sobre los suyos,"

            n "sin pr??cticamente verg??enza alguna, su lengua empieza a corretear por cada rinc??n de la tuya;"

            n "su cabeza se desplaza en varias inclinaciones,"

            n "mientras su rostro avanza sin disimulo alguno contra el tuyo buscando profundizar a??n m??s el beso."

            n "En ocasiones sientes que hasta te falta el aire,"

            n "para luego percibir como vuelve a dejarte espacio y acto seguido regresa para embestirte con viveza,"

            n "chocando labios con dientes junto con la humedad y el ardor de su boca."

            n "En esta ocasi??n te resulta algo m??s dif??cil detenerte, pero finalmente consigues desprenderte de sus labios."

            d "..."

            p "??Est??s bien?"

            d "..."

            p "Puedes mentirme lo que quieras,"

            p "pero es obvio que esto no te disgusta en absoluto."

            d "..."

            p "Me da la sensaci??n que hasta te gusta m??s que a mi."

            d "No..."

            d "Yo..."

            p "??S???"

            d "F??llame y c??llate de una vez."

        elif afternight04__MMouth_Tongue_Deep_Success == 6:

            show afternight04_sexbattle_effects black
            with dissolve

            n "Sin ning??n pudor, D??dac te besa con ??mpetu,"

            n "saboreando tu lengua,"

            n "jugueteando con ella al mismo tiempo que inclina su cabeza para saborear mejor tus labios"

            n "al suave roce del contacto entre vuestros dientes y el ardor de su boca."

            show afternight04_sexbattle_effects empty
            with dissolve

            n "Pasados unos minutos,"

            extend " aprovechando un despiste,"

            n "logras apartarte de ella mientras te mira con ojos de gata en celo."

            d "F??llame [protname]."

            p "..."

            $ mc_body.pleasure += 2

            pt "C??lmate,"

            extend " no es posible que una sola palabra te haya puesto tan cachondo..."


        elif afternight04__MMouth_Tongue_Deep_Success >= 7:

            show afternight04_sexbattle_effects black
            with dissolve

            p "..."

            show afternight04_sexbattle_effects empty
            with dissolve

            d "..."

############################################################
###########################################################

############################################################
    jump afternight04__MMouth_Tongue_Deep_After #End of French Deep Kiss.

label afternight04__MMouth_Tongue_Deep_After:

############################################################
###########################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    if (afternight04__MMouth_Tongue_Success > 12) or (afternight04__MMouth_Tongue_Failed > 10) or (afternight04__MMouth_Tongue_Deep_Failed > 7) or (afternight04__MMouth_Tongue_Deep_Success > 7):

        call afternight04_RapeOrNot

    ###########################
    ##########################

    return