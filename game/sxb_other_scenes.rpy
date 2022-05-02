###################################

label endupdatescript_sexbattle:
    
    if Tendolarsversion == True:
    
        if Tendolarsversionvisited == False:
            $ Tendolarsversionvisited = True
            $ debug ("Here is another version.")
            #call endupdate10dolars
            
    else:
        jump endupdate_sexbattle
        
return

###################################

###################################

label endupdate_sexbattle:
    
    #window hide dissolve
    #pause

    aj "ESTA ACCIÓN NO ESTÁ DISPONIBLE EN ESTA VERSIÓN [config.version]." with Dissolve (1.0)
    
    aj "TENDRÁS QUE ESPERAR A FUTURAS ACTUALIZACIONES."

    call screen dummy_screen()
    
    return

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################

################
###############
##############
##      HER SUCCESS --- RAPE OR NOT?

label afternight04_RapeOrNot:

    $ debug ("WANNABE 01")

    if (current_girl.total_fail in range (3, 5) or current_girl.total_success in range (5, 8)): #When she probably will be pissed.

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        #if current_pose.id == "pose_1":  ## Is this really necessasry?

            #show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
            #show afternight04_sexbattle_d_eyes 05_a
            #show afternight04_sexbattle_d_pupils front05_a
            #show afternight04_sexbattle_d_eyebrows angryx04_a
            #with dissolve

        if randomnum_1to10 == 1:

            pt "Si me repito demasiado,"

            extend " tomará la iniciativa y entonces estaré jodido..."

        elif randomnum_1to10 == 2:

            pt "Si sigo así,"

            extend " la cosa puede acabar mal..."

        elif randomnum_1to10 == 3:

            pt "Debería ir pensando en cambiar de táctica..."

        elif randomnum_1to10 == 4:

            pt "No es que le haya encantado..."

        elif randomnum_1to10 == 5:

            pt "Mejor será empezar a pensar en alternativas..."

        elif randomnum_1to10 == 6:

            pt "Como siga así me va a odiar de verdad..."

        elif randomnum_1to10 == 7:

            pt "Me temo que no estaré a tiempo de revertir la situación..."

        elif randomnum_1to10 == 8:

            pt "Como esto siga así, me va a violar hasta el fondo..."

        elif randomnum_1to10 == 9:

            pt "Como no cambie algo pronto,"

            extend " estoy jodido..."

        elif randomnum_1to10 == 10:

            pt "Debería empezar a hacer las cosas algo diferentes..."


###########
###########


    if (current_girl.total_fail >= 4 or current_girl.total_success >= 7): #When she probably will be pissed.

        if current_girl.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            pt "Esto me da mala espina..."

            call afternight04_Didac_Success

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            pt "Parece que esta vez no me va a violar..."

            call afternight04_Didac_AlsoFailed

    #else: # Not necessary.

    return # FINISH ## RAPE OR NOT?

###########
###########

################################################
###############################################
##############################################
#############################################

label afternight04_condom_broken_scene:

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils down04_a
        show afternight04_sexbattle_d_eyebrows angryx01_a
        with dissolve

    d "De eso nada..."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx02_a
        with dissolve

    d "La polla se queda ahí."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
        show afternight04_sexbattle_d_eyes 01_a
        show afternight04_sexbattle_d_pupils front01_a
        show afternight04_sexbattle_d_eyebrows serious_a
        with dissolve

    p "Por..."

    extend " ¡¿por qué?!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx03_a
        with dissolve

    d "Porque lo digo yo."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils down05_a
        show afternight04_sexbattle_d_eyebrows sadx02_a
        with dissolve

    #call afternight04_Didac_Success

    call screen dummy_screen()
    
    return

################################################
###############################################
##############################################
#############################################
############################################################

label afternight04_probabilty_checking:

    if (current_girl.enslavement in range (0, 74)):

        pt "Aunque con lo poco sumisa que está,"

        if afternight04__prehfix_RNipple_Lick == True:

            pt "es probable que le haga más daño que placer..."

        if afternight04__prehfix_MMouth_Tongue == True:

            pt "me da la sensación que lo más probable es que me aparte."

        if afternight04__prehfix_MMouth_dick == True:

            pt "tengo miedo de que me arranque la polla con un mordisco..."


    elif (current_girl.enslavement in range (75, 119)):

        pt "Aunque a penas es algo sumisa,"

        if afternight04__prehfix_RNipple_Lick == True:

            pt "tengo el cincuenta por ciento de posibilidades de que no le haga daño..."

        if afternight04__prehfix_MMouth_Tongue == True:

            pt "tengo el cincuenta por ciento de posibilidades de que me aparte..."

        if afternight04__prehfix_MMouth_dick == True:

            pt "es probable que me muerda la polla..."


    elif (current_girl.enslavement in range (120, 159)):

        pt "Está algo sumisa,"

        pt "pero aún existe la posibilidad de que no le guste..."


    elif (current_girl.enslavement >= 160):

        pt "Con lo sumisa que la tengo,"

        pt "no creo que se me queje..."

    if Tendolarsversion == True:

        aj "{size=20}{image=icon_enslavery_didac} > 160 = 100\% de éxito.\n
        {image=icon_enslavery_didac} > 120 = 75\% de éxito,\n
        {image=icon_enslavery_didac} > 75 = 50\% de éxito,\n
        {image=icon_enslavery_didac} < 75 = 25\% de éxito.{/size}"

    return


############################################################ afternight04_probabilty_checking02

label afternight04_probabilty_checking02:

    if afternight04__prehfix_RNipple_Lick == True:
        $ afternight04_Nipple_Lick_Bite_Done += 1

    elif afternight04__prehfix_MMouth_Tongue == True:
        $ afternight04__MMouth_Tongue_Deep_Done += 1

    elif afternight04__prehfix_MMouth_dick == True:
        $ afternight04__MMouth_dick_Deep_Done += 1

    if (current_girl.enslavement in range (0, 74)):

        if (randomnum_1to100 in range (0, 25)):

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = True
                $ afternight04_Nipple_Lick_Bite_Success += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = True
                $ afternight04__MMouth_Tongue_Deep_Success += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = True
                $ afternight04__MMouth_dick_Deep_Success += 1

        else:

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = False
                $ afternight04_Nipple_Lick_Bite_Failed += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = False
                $ afternight04__MMouth_Tongue_Deep_Failed += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = False
                $ afternight04__MMouth_dick_Deep_Failed += 1

    elif (current_girl.enslavement in range (75, 119)):

        if (randomnum_1to100 in range (0, 50)):

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = True
                $ afternight04_Nipple_Lick_Bite_Success += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = True
                $ afternight04__MMouth_Tongue_Deep_Success += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = True
                $ afternight04__MMouth_dick_Deep_Success += 1

        else:

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = False
                $ afternight04_Nipple_Lick_Bite_Failed += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = False
                $ afternight04__MMouth_Tongue_Deep_Failed += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = False
                $ afternight04__MMouth_dick_Deep_Failed += 1

    elif (current_girl.enslavement in range (120, 159)):

        if (randomnum_1to100 in range (0, 75)):

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = True
                $ afternight04_Nipple_Lick_Bite_Success += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = True
                $ afternight04__MMouth_Tongue_Deep_Success += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = True
                $ afternight04__MMouth_dick_Deep_Success += 1

        else:

            if afternight04__prehfix_RNipple_Lick == True:
                $ afternight04_Nipple_Lick_Bite_Success_Cond = False
                $ afternight04_Nipple_Lick_Bite_Failed += 1

            elif afternight04__prehfix_MMouth_Tongue == True:
                $ afternight04__MMouth_Tongue_Deep_Success_Cond = False
                $ afternight04__MMouth_Tongue_Deep_Failed += 1

            elif afternight04__prehfix_MMouth_dick == True:
                $ afternight04__MMouth_dick_Deep_Success_Cond = False
                $ afternight04__MMouth_dick_Deep_Failed += 1

    elif (current_girl.enslavement >= 160):

        if afternight04__prehfix_RNipple_Lick == True:
            $ afternight04_Nipple_Lick_Bite_Success_Cond = True

        elif afternight04__prehfix_MMouth_Tongue == True:
            $ afternight04__MMouth_Tongue_Deep_Success_Cond = True

        elif afternight04__prehfix_MMouth_Tongue == True:
            $ afternight04__MMouth_dick_Deep_Success_Cond = True

    return


label afternight04_SheRapingYou_NotAllowed:

    # Boobs, Nipple, Clitoris, Belly, Stomach. 

    ## NOT FINISHED.

    if mc_body.dick_speed > 0:

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
            show afternight04_sexbattle_d_eyes 03_a
            show afternight04_sexbattle_d_pupils front03_a
            show afternight04_sexbattle_d_eyebrows angryx04_a
            with dissolve

        if randomnum_1to5 == 1:

            d "Si quieres magrearme, hazlo cuando seas tú el que me esté follando."

        elif randomnum_1to5 == 2:

            d "Si te tengo que follar yo, no me toques."

        elif randomnum_1to5 == 3:

            d "Fóllame tú, y entonces quizás te deje manosearme."

        elif randomnum_1to5 == 4:

            d "No veo que me estés follando, para que te tomes la libertad de toquetearme."

        elif randomnum_1to5 == 5:

            d "Para de sobarme, si tengo que follarte yo."

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Silentx03_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows angryx03_a
            with dissolve

        call screen dummy_screen()

    return



label afternight04__LButtock_Slap_Pose01:

    $ afternight04__LButtock_Slap_Attempt += 1

    #if current_girl.total_try == 0:
    if afternight04__LButtock_Slap_Attempt == 0:

        aj "THIS TEXT SHOULD NOT BE VISIBLE 5586"

    elif afternight04__LButtock_Slap_Attempt == 1:

        pt "Teniéndola encima,"

        pt "no puedo darle bien en las nalgas..."

    elif afternight04__LButtock_Slap_Attempt == 2:

        pt "Si la tuviera a cuatro patas se lo podría hacer mejor..."

    elif afternight04__LButtock_Slap_Attempt == 3:

        pt "Si está suficientemente caliente y la cojo por el brazo..."

    else:

        pt "¿Por qué diablos sigo insistiendo?"

## IMAGE # Necessary?

    if afternight04__prehfix_RButtock_Slap == True:

        $ mc_body.store["left_hand"] = ""
        show afternight04_sexbattle_mc_handL empty
        with dissolve

    elif afternight04__prehfix_LButtock_Slap == True:

        $ mc_body.store["right_hand"] = ""
        show afternight04_sexbattle_mc_handR empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        with dissolve

    return








################################################
###############################################
##############################################
#############################################

############################################################

##TIPS

        #if mc_body.store["left_hand"] == grab:                                      # For Knowing if left hand is grabbing.
        #if pose01_left_boob.get_action("LBoob_Slap").times_failed >= 5:             # For knowing how many times slap FAILED.
        #if pose01_left_boob.get_action("LBoob_Slap").times_done >= 5:               # For knowing how many times slap had been SUCCESSFUL.
        #if pose01_right_boob.get_action("RBoob_Slap").times_done + pose01_right_boob.get_action("RBoob_Slap").times_failed == 0:  # TOTAL TRY.

        # current_girl.total_try == 1: ##That´s real "TRY" times.
        # current_girl.total_fail == 1: ##That´s real "FAIL" times.
        # current_girl.total_success >= 3: ## REAL!"SUCCESS" times.

        #$ mc_body.pleasure += 1
        #$ current_girl.pleasure += 1
        #$ current_girl.enslavement += 1
        
        #$ if current_girl.enslavement in range (0, 15) #Means between 0 and 15.
        # if mc_body.dick_speed == 3 #Means Speed is Fast.
        # if mc_body.store["dick"] == "Pussy_dick_low" #Means Deep is Low.

        #if _prefix == "RBoob_Slap" #Only inside same .rpy file
        #if afternight04__prehfix_LBoob_Grab = True #It works in "before" and it becomes false in "after"

        ## Total TRY for pose 01, 02 and 03:

            #if (pose01_right_buttock.get_action("RButtock_Massage").times_done + pose01_right_buttock.get_action("RButtock_Massage").times_failed +
                #pose02_right_buttock.get_action("RButtock_Massage").times_done + pose02_right_buttock.get_action("RButtock_Massage").times_failed +
                #pose03_right_buttock.get_action("RButtock_Massage").times_done + pose03_right_buttock.get_action("RButtock_Massage").times_failed) == 1:

                #"Total TRY 1"


        ## girl_1.enslavement = -90 (For current_girl.enslavement = -90)

        #Search Engine - RegEx - Regular Expressions - .* -
            # "" define .* = False "" - WORKS! -  result example: "" define afternoon04_Q_ClassicArt = False ""

           