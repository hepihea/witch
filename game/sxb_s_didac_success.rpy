    ## LABEL // HER SUCCESS:
##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################

label afternight04_Didac_Success:

##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################

    ## Informing the player about third fail is a bad idea.

    #$ debug ("WANNABE")

    if current_girl.total_fail == 4:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils front05_a
            show afternight04_sexbattle_d_eyebrows serious_a
            with dissolve

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            pt "Esto de repetir algo que no le ha gustado por cuarta vez,"

            pt "creo que ha sido una mala idea..."

        elif randomnum_1to5 == 2:
                
            pt "Me parece que haber repetido cuatro veces el mismo error ha sido una mala idea..."

        elif randomnum_1to5 == 3:
                
            pt "Me da la sensación que si repito por cuarta vez algo que no le ha gustado,"

            pt "querrá tomar el control..."

        elif randomnum_1to5 == 4:

            pt "Debería haber probado algo distinto antes de cabrearla repitiendo lo mismo más de tres veces..."

        elif randomnum_1to5 == 5:
                
            pt "No parece que haya sido buena idea cometer por cuarta vez el mismo error..."


    ## Changing the Pose to 01. NO HERE, it must be done in ##afternight04_Pussy_dick_rape_general_image

    if (current_pose.id == "pose_2" or current_pose.id == "pose_3"):

        $ current_pose.id = "pose_1"
        $ current_pose = pose_1

        call afternight04_sexbattle_scene_pose01
        with vpunch

        $ debug ("In theory if you are in pose02 or pose03 now Should appear pose01 correct... 5778")


#### PROVE - REMOVE THINGS

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
##
    if afternight04_SheRapingYou == True:

        if not (mc_body.store["right_hand"] == "" or mc_body.store["left_hand"] == "" or mc_body.store["tongue"] == "" or mc_body.store["dick"] == ""):

            $ randomnum_1to5 = renpy.random.randint(1, 5) # NOT FINISHED, ADD 10.

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            if randomnum_1to5 == 1:

                d "¡Quita coño!"

            elif randomnum_1to5 == 2:

                if not mc_body.store["right_hand"] == "" and mc_body.store["left_hand"] == "":

                    d "¡Me sobran tus manos ahí!"

                elif not mc_body.store["tongue"] == "":

                    d "¡Me sobra tu lengua ahí!"

                else:

                    d "¡Que pesado!"

            elif randomnum_1to5 == 3:

                d "¡Fuera!"

            elif randomnum_1to5 == 4:

                d "¡Mejor así!"

            elif randomnum_1to5 == 5:

                if not mc_body.store["right_hand"] == "" and mc_body.store["left_hand"] == "":

                    d "¡Aparta las manos!"

                elif not mc_body.store["tongue"] == "":

                    d "¡Aparta esa lengua!"

                else:

                    d "¡¿No sabes cuando parar?!"

####################################################################################################
################################################################################################# IMAGE REMOVAL

        $ mc_body.store["tongue"] = ""

        show afternight04_sexbattle_mc_tongue_pussy empty
        show afternight04_sexbattle_mc_tongue_clitoris empty

        $ mc_body.store["right_hand"] = ""
        $ mc_body.store["left_hand"] = ""
        
        show afternight04_sexbattle_mc_handR empty
        show afternight04_sexbattle_mc_handL empty

        #show afternight04_sexbattle_mc_handR_penetrate_pussy empty

        # penetrate_pussy empty - penetrate_anal empty
        call afternight04_sexbattle_pubic_emptiness

        if not (mc_body.store["right_hand"] == "" or mc_body.store["left_hand"] == "" or mc_body.store["tongue"] == "" or mc_body.store["dick"] == ""):

            with hpunch

####################################################################################################
####################################################################################################

        $ randomnum_1to5 = renpy.random.randint(1, 5) # NOT FINISHED. ADD 10.

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils front04_a
            show afternight04_sexbattle_d_eyebrows angryx02_a
            with dissolve

        if randomnum_1to5 == 1:

            pt "Mierda..."

        elif randomnum_1to5 == 2:

            pt "La he jodido..."

        elif randomnum_1to5 == 3:

            pt "Putada..."

        elif randomnum_1to5 == 4:

            pt "Cagüen..."

        elif randomnum_1to5 == 5:

            pt "Joder..."

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

### BITCH - REMOVE THINGS


##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################
    ## BEFORE IMAGE:

    $ debug("Here is a long TEST text")

    # progcheck2 "{size=15}afternight04_Pussy_dick_low_Speed_0_Rape_Done = [afternight04_Pussy_dick_low_Speed_0_Rape_Done],\n
    # afternight04_Pussy_dick_low_Speed_1_Rape_Done = [afternight04_Pussy_dick_low_Speed_1_Rape_Done],\n
    # afternight04_Pussy_dick_low_Speed_2_Rape_Done = [afternight04_Pussy_dick_low_Speed_2_Rape_Done],\n
    # afternight04_Pussy_dick_low_Speed_3_Rape_Done = [afternight04_Pussy_dick_low_Speed_3_Rape_Done],\n\n

    # afternight04_Pussy_dick_med_Speed_0_Rape_Done = [afternight04_Pussy_dick_med_Speed_0_Rape_Done],\n
    # afternight04_Pussy_dick_med_Speed_1_Rape_Done = [afternight04_Pussy_dick_med_Speed_1_Rape_Done],\n
    # afternight04_Pussy_dick_med_Speed_2_Rape_Done = [afternight04_Pussy_dick_med_Speed_2_Rape_Done],\n
    # afternight04_Pussy_dick_med_Speed_3_Rape_Done = [afternight04_Pussy_dick_med_Speed_3_Rape_Done],\n\n

    # afternight04_Pussy_dick_deep_Speed_0_Rape_Done = [afternight04_Pussy_dick_deep_Speed_0_Rape_Done],\n
    # afternight04_Pussy_dick_deep_Speed_1_Rape_Done = [afternight04_Pussy_dick_deep_Speed_1_Rape_Done],\n
    # afternight04_Pussy_dick_deep_Speed_2_Rape_Done = [afternight04_Pussy_dick_deep_Speed_2_Rape_Done],\n
    # afternight04_Pussy_dick_deep_Speed_3_Rape_Done = [afternight04_Pussy_dick_deep_Speed_3_Rape_Done],{/size}"

    ## DIDAC RAPE
######### DICK DEEP used at least once.

    if (afternight04_Pussy_dick_deep_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_0_Done >= 1):

    ########################
    ######################## deep speed_3

        #if afternight04_Pussy_dick_deep_Speed_3_Rape_Done >= 4: #Not necessary.

        if afternight04_Pussy_dick_deep_Speed_3_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_3_Done >= 1:

            if afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 1:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils up03_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    d "Joder..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¡Me estás perforando la puta barriga!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Lo dice como si no fuera ella la que me está violando..."

                    pt "Desde luego..."

                else:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Realmente la tienes enorme..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "Dídac,"

                    extend " ¿Estás seguro...?"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    pt "No me gusta esa sonrisa..."

            elif afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 2:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "¡¡DIIOOOSS!!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¡QUE PUTO POLLÓN!!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Quiero volverte a cabalgar hasta el fondo hasta que me dejes muerta en el suelo..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve


            elif afternight04_Pussy_dick_deep_Speed_3_Rape_Done == 3:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "UUFGGHH..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils up03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Si a mi me está doliendo un cojón y medio con lo jodidamente estrecha que tiene la cérvix..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    pt "Ella..."

                    extend " ¡ÉL!"

                    extend " Él..."

                    pt "tiene que tener un dolor de mil demonios..."

                else:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Ya que no lo haces tú,"

                    extend " voy a meterme de nuevo tu polla dentro..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "hasta que la haga desaparecer por completo dentro de mí..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve


            elif afternight04_Pussy_dick_deep_Speed_3_Rape_Done >= 4:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    $ randomnum_1to3 = renpy.random.randint(1, 3)

                    if randomnum_1to3 == 1:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Llevo todo el día soñando con esta situación;"

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "pero no me hubiera imaginado que realmente entraría hasta el fondo..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    elif randomnum_1to3 == 2:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Pollón que gastas hijo de putaaah..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    elif randomnum_1to3 == 3:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "Realmente me estás reventando por dentro..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        pt "Como si fuera una novedad..."

                else:

                    $ randomnum_1to3 = renpy.random.randint(1, 3)

                    if randomnum_1to3 == 1:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "La quiero sentir hasta el fondo..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    elif randomnum_1to3 == 2:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Quiero volverla a sentir toda dentro de mí..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                    elif randomnum_1to3 == 3:

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Mataría por poder sentirla entera dentro de nuevo..."

                        if current_pose.id == "pose_1":

                            show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                #Velocity 3

                $ randomnum_1to3 = renpy.random.randint(1, 3)

                if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                if randomnum_1to3 == 1:
                    
                    d "y así de rápida..."

                elif randomnum_1to3 == 2:

                    d "y a esta velocidad..."

                elif randomnum_1to3 == 3:

                    d "Y follando a todo trapo..."

                if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

            $ mc_body.dick_speed = 3
            $ mc_body.store["dick"] = "Pussy_dick_deep"

    ########################
    ######################## deep speed_2

        elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_2_Done >= 1 :
            if afternight04_Pussy_dick_deep_Speed_2_Rape_Done >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils down02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                pt "No me gusta ni pizca esa mirada suya..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "¿Qué estás pensando hacer Dídac...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Quiero follarte como es debido"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "para demostrarte cómo se hace..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Si haces eso al final te va a salir sangre..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "¡¿No ves que a esta velocidad ya te estoy destrozando la cervix?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Y eso qué coño es?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "La pared con la que estás chocando constantemente cuando intentas meterla hasta el fondo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "Es justo la pared que lleva hasta tu útero..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "Así que aún puede llegar más al fondo...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "¡¿Qué?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "¡No!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¡El útero es dónde se gesta un embrión!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "¡Ahí no tiene que entrar la polla!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Eso habrá que verlo;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Así que es hora de aumentar este ritmo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Está fatal de la cabeza..."

                $ mc_body.dick_speed = 3
                $ mc_body.store["dick"] = "Pussy_dick_deep"

            elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 1:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Como duele;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "coño..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "Dídac,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "no hace falta que me cabalgues hasta el fondo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Ni de puta broma..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Es hora de volver a meter tu monstruo en el lago otra vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "¡¿Se cree que mi polla es {i}Nessie{/i} o qué?!"

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_deep"

            elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 2:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Joder..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "¿Por qué coño tienes la polla tan grande?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "Si tanto te disgusta..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "puedes quitártela e ir más despacio..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Disgustarme?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Me duele mogollón;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils up03_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "¡Pero me encanta!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "Cada día que pasa se parece más a una mujer,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "porque cada vez lo entiendo menos..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "estás temblando..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Lo sé..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "No sé si lo sabes,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx06
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "porque me da la sensación que quieres volver a metértela hasta el fondo de nuevo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Así es..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx06
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "Quien le entienda..."


                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_deep"

            elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done == 3:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils up02_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "Es jodido como duele,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils up03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "pero me encanta sentir tu polla chocando duramente contra el fondo de mi útero..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "En realidad lo que estoy haciendo es machacar tu cérvix..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "Si llegara a penetrar tu cuello uterino,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx06
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils up02_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "entonces sí que me metería dentro de tu útero..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils up01_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Hazlo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "así ya te estoy causando un dolor de mil cojones;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "si llegara más al fondo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No me seas un puto mojigato de mierda [protname]..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "No tiene ni la más jodida idea de lo que está hablando..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Duele;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up4_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "pero me encanta..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Quiero que me folles [protname]!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Pero de momento me conformaré con violarte..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_deep"

        elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done <= 3 or afternight04_Pussy_dick_deep_Speed_2_Done <= 3 : #Velocity 2

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                $ randomnum_1to3 = renpy.random.randint(1, 3)

                if randomnum_1to3 == 1:

                    d "y haciéndolo a este ritmo no está mal..."

                elif randomnum_1to3 == 2:

                    d "y cabalgándote así..."

                elif randomnum_1to3 == 3:

                    d "Aunque pronto lo intentaré a mayor velocidad..."

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_deep"

    ########################
    ######################## deep speed_1

        elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done >= 1 or afternight04_Pussy_dick_deep_Speed_0_Done >= 1:
            if afternight04_Pussy_dick_deep_Speed_1_Rape_Done >= 4 or afternight04_Pussy_dick_deep_Speed_1_Done >= 4:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Esa mirada tuya no me gusta nada..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "¿En qué diablos estás pensando?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Estoy pensando que estoy cabalgándote a ritmo de caracol..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Pero eres consciente de que me has dicho que te duele un huevazo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "¿Verdad?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Me da la sensación que me ha dicho que sí por decir algo..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils up03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    pt "Esa expresión no me gusta nada..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Qué tal si ahora me la meto otra vez dentro hasta el fondo...?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Y esta vez,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "aumento un poco más el ritmo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Teniendo en cuenta que llevas todo el rato gimiendo de dolor,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "y que obviamente tienes que estar teniendo un dolor como si estuvieras pariendo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "Pienso que estás como una puta cabra."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "Es posible..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "Hay que joderse..."

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_deep"

            elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 1 and afternight04_Pussy_dick_deep_Speed_0_Done == 0:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Aughh..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "¿Estás bien?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "Tengo la sensación que te he roto algo ahí dentro..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Claro que no estoy bien!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Tienes un pedazo monstruo por polla!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Duele un cojón!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Tú tampoco la tenías demasiado más pequeña que la mía..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "de hecho creo que era más gorda..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "ahora entiendo mejor el mal genio de algunas de las chicas con las que he estado..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    pt "A saber cómo las trataba..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Hmmm..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Vamos a ver si entra de nuevo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve
                    
                    p "Dídac..."

            elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 1 and afternight04_Pussy_dick_deep_Speed_0_Done => 1:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Sino quieres que me corra pronto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Pobre de ti..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¿Por qué me de la sensación que quieres volver a meterla toda dentro?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Por que tienes buena intuición..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "..."

            elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 2:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "me estás quitando la circulación en la polla..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No me seas nenaza y aguanta."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "¡¿O te crees que a mi no me duele?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¡Pues sácala!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Eres tú quien quiere cabalgarme!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Lo sé..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Y aunque me duela de narices..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "me encanta sentirla toda dentro..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Ni se te ocurra meterla otra vez hasta el fondo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¡¿Acaso no ves que tienes el coño muy estrecho?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "La culpa es tuya que tienes un pollón del tamaño de un bate de {i}béisbol{/i}..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¡Pues no te la metas hasta el fondo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "El caso es que me encanta sentirme llena por tu {i}anaconda{/i}..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    pt "Quien lo entienda..."

            elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done == 3:

                if (mc_body.store["dick"] == "Pussy_dick_deep"):

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Auughh..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Te duele..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "y aún así quieres seguir..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "¿Me equivoco?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Lo que querría es que fueras tú el que me folla en condiciones,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "no que tenga que ser yo, el que te folle a ti."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Imbécil."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Sí,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "encima elogíame;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    pt "Capullo..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Dídac;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "al final te voy a desgarrar el coño si te la vuelves a meter hasta el fondo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Si me follaras como Dios manda es posible..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "Definitivamente,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    pt "le va el masoquismo..."

        elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done <= 3 or afternight04_Pussy_dick_deep_Speed_1_Done <= 3: #Velocity 1

                $ randomnum_1to3 = renpy.random.randint(1, 3)

                if randomnum_1to3 == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "y con pedazo tamaño,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "mejor empezamos lentamente..."

                elif randomnum_1to3 == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Aunque de momento no pueda ir a mayor ritmo..."

                elif randomnum_1to3 == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Y ya sé que es algo lento,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "pero pronto aumentaré..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    pt "Solo me falta eso..."

                $ mc_body.dick_speed = 1
                $ mc_body.store["dick"] = "Pussy_dick_deep"

    ########################
    ######################## deep speed_0

        if afternight04_Pussy_dick_deep_Speed_0_Rape_Done == 0 and afternight04_Pussy_dick_deep_Speed_0_Done == 0:

            if (mc_body.store["dick"] == "Pussy_dick_deep"): #IN

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "¡¡Jo-"

                extend "der...!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils up00_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡Tu pollón me está removiendo el estómago entero..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Dídac..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Creo que ha sido una mala idea meterla tan adentro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Je..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Demasiado tarde..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Aunque me duela un cojón y parte del otro;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Estoy en la puta gloria..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "No estará pensando en moverse;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "¡¿Verdad?!"

            else: #Out

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Dídac..."

            $ mc_body.dick_speed = 1
            $ mc_body.store["dick"] = "Pussy_dick_deep"


    ##
    ########################
    ########################
######### DICK MED used at least once.

    elif (afternight04_Pussy_dick_med_Speed_0_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_0_Done >= 1):

    ########################
    ######################## med Introduction

        if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            ## NOT FINISHED #Do it by Tries, not by random.

            if randomnum_1to5 == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Aunque sería buena idea moverla un poco..."

            elif randomnum_1to5 == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Ya que tienes menos hombría que un {i}pavo real{/i},"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Voy a tener que ser yo quien tome las riendas y violarte como es debido..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "..."

            elif randomnum_1to5 == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "Disfrutas cuando me meto tu polla dentro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Verdad?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

            elif randomnum_1to5 == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "Quiero volverla a sentir dentro..."

            elif randomnum_1to5 == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Quiero tu puta anaconda dentro de mí."

            $ mc_body.store["dick"] = "Pussy_dick_med"

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "Voy a violarte hasta que decidas actuar como un hombre..."

            elif randomnum_1to5 == 2:

                d "Me tendrás cabalgándote hasta que decidas tomar cartas en el asunto..."

            elif randomnum_1to5 == 3:

                d "Quizás te juzgué mal y eres el tipo de hombre que disfruta siendo un perro sumiso..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif randomnum_1to5 == 4:

                d "¿Te gusta que te viole una mujer?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿No es así?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Eres un perro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif randomnum_1to5 == 5:

                d "¿Quieres que te folle duro?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Nenaza..."

## CALL IMAGE HERE?!

    ########################
    ######################## med speed_3

        if afternight04_Pussy_dick_med_Speed_3_Rape_Done >= 4 or afternight04_Pussy_dick_med_Speed_3_Done >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Hmmm..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "No me gusta esa mirada..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "¿En qué estás pensando Dídac...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Estoy pensando que tienes un pollón enorme..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            pt "¿Se supone que le tengo que decir gracias...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Pero estoy segura que con lo mojada,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "dilatada y lubricada que estoy,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "puede llegar hasta el fondo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "Estás de coña..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¿verdad?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Quería que me follaras tú!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Al final lo único que estoy haciendo en realidad es violarte!"

                ##

            if current_girl.orgasm <= 3:

                if mc_body.orgasm == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Además ya te has corrido una vez!"

                elif mc_body.orgasm == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡ADEMÁS YA TE HAS CORRIDO DOS PUTAS VECES!"

                ##

            if current_girl.orgasm == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡Y NI SI QUIERA HE TENIDO UN SOLO PUTO ORGASMO!!"

            if current_girl.orgasm == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡Y yo solo he tenido un puto orgasmo!!"

            elif current_girl.orgasm == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Y yo solo he tenido dos orgasmos!"

            elif current_girl.orgasm == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "A pesar de que ya lleve tres orgasmos..."

            elif current_girl.orgasm >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Aunque confieso que ya llevo [current_girl.orgasm] orgasmos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "No está mal [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Pero aún así estoy segura que puedo mover mis caderas algo más rápidamente..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Dídac..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No me vengas con hostias [protname]!"

            if mc_body.orgasm == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Ya te me has corrido una puta vez y ni siquiera has llegado hasta el fondo!"

            elif mc_body.orgasm >= 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡Si ya te has corrido [mc_body.orgasm] veces!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡Y NI SIQUIERA HAS LLEGADO HASTA EL FONDO!!"

                if current_girl.orgasm <= 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Como no tenga por lo menos 4 o 5 orgasmos te reventaré la puta cara!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "No pide poco ni nada el muy cabrón..."

            if (mc_body.orgasm >= 1 and current_girl.orgasm <= 3):

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Espero que me aguantes mucho más que lo has hecho hasta ahora!"

            $ mc_body.dick_speed = 0
            $ mc_body.store["dick"] = "Pussy_dick_deep"

        #elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 3 or afternight04_Pussy_dick_med_Speed_3_Done == 3:

        #elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 2 or afternight04_Pussy_dick_med_Speed_3_Done == 2:

        #lif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 1 or afternight04_Pussy_dick_med_Speed_3_Done == 1:

    ########################
    ######################## med speed_3

        elif afternight04_Pussy_dick_med_Speed_3_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_3_Done >= 1:

            if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"): #Dick Out

                if afternight04_Pussy_dick_med_Speed_3_Rape_Done == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Me encanta lo duro que tienes el rabo [protname];"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "la putada es que lo tienes jodidamente enorme..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "¿Eso es una crítica o un elogio?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Pero como no me folles pronto como Dios manda..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Al final me la meteré yo misma hasta el fondo;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Te lo juro."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Solo me faltaría eso para terminar de correrme en menos que canta un gallo..."

                elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Espero que abajes el ritmo Dídac,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Como me sigas cabalgando tan rápidamente como la última vez,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "dudo que pueda aguantar mucho más tiempo así..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Como me dejes a medias por que tu puto {i}Piolín{/i} no ha dado la talla;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡mañana te inyectaré una sobredosis de viagra por el culo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Me explico?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "De{i}Anaconda{/i},"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "mi polla se ha transformado ahora en {i}Piolín{/i}..."

                    pt "Genial..."

                elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    $ randomnum_1to3 = renpy.random.randint(1, 3)
                        
                    if randomnum_1to3 == 1:

                        d "Voy a cabalgarte como si no hubiera mañana..."

                    elif randomnum_1to3 == 2:

                        p "Voy a prenderle fuego a tu sacapuntas..."

                    elif randomnum_1to3 == 3:

                        pt "Dejaré tu polla más roja que una gamba..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "..."


            else: #Dick INside

                if afternight04_Pussy_dick_med_Speed_3_Rape_Done == 1:

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    d "Es una sensación realmente extraña..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "lo de cabalgarte para intentar que me llegue hasta el fondo;"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "y no al revés..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "Dídac..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Calla!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Ya que no me follas tú!"

                    d "¡Al menos no me desconcentres!"

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "No creo que pueda aguantar durante mucho tiempo este ritmo..."

                elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Vas..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "un pelín rápido Dídac..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "He visto tortugas gigantes follando más rápido que tú."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Que tú me folles mal,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "no significa que yo deba imitarte..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Así que,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "se buen chico;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "déjate violar,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "y ni se te ocurra correrte."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "¿Capisci?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    pt "¿Me va de mafioso italiano ahora...?"

                elif afternight04_Pussy_dick_med_Speed_3_Rape_Done == 3:

                    $ randomnum_1to3 = renpy.random.randint(1, 3)
                        
                    if randomnum_1to3 == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Ugh..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        pt "Se nota que el ritmo tan acelerado que lleva,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        pt "poco a poco lo está agotando..."

                    elif randomnum_1to3 == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        p "¿No estás yendo demasiado rápido...?"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "¡Eso me lo dice el que hace el idiota moviendo las manos,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "y espera a que otro le haga el trabajo!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡Si me follaras tú no tendría que hacerlo yo!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "¡¿Y por qué debo ser yo el que tenga que follarte a ti?!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 00_a
                            show afternight04_sexbattle_d_pupils front00_a
                            show afternight04_sexbattle_d_eyebrows surprisex01_a
                            with dissolve

                        p "¡Eres tú quien me ha pedido el favor!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils right02_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "Tranquilo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "quédate quieto sin hacer nada si es lo que quieres..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils right04_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "total,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "eres más inútil que un vibrador sin pilas..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        pt "¡Será hijo de mil padres!"

                    elif randomnum_1to3 == 3:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        p "Dídac;"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "si te lo tomarás con más calma,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                            show afternight04_sexbattle_d_eyes 07_a
                            show afternight04_sexbattle_d_pupils front07_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        p "quizás duraría un poco más..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡No quiero tomármelo con calma!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                            show afternight04_sexbattle_d_eyes 00_a
                            show afternight04_sexbattle_d_pupils front00_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "¡Llevo todo el día esperándote!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "¡Estoy hasta los cojones de esperar!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "Si tengo que hacerlo yo,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils front02_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        d "lo haré yo..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                            show afternight04_sexbattle_d_eyes 00_a
                            show afternight04_sexbattle_d_pupils front00_a
                            show afternight04_sexbattle_d_eyebrows angryx05_a
                            with dissolve

                        d "¡pero no te me corras como un típico puto empollón pajillero de mierda!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows angryx04_a
                            with dissolve

                        p "..."

            $ mc_body.dick_speed = 3
            $ mc_body.store["dick"] = "Pussy_dick_med"

    ########################
    ######################## med speed_2

        elif afternight04_Pussy_dick_med_Speed_2_Rape_Done >= 4 or afternight04_Pussy_dick_med_Speed_2_Done >= 4 :

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Pero aún así estoy segura que puedo mover mis caderas algo más rápido..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Dídac..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡No me vengas con hostias [protname]!"

            if mc_body.orgasm == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Ya te me has corrido una puta vez y ni siquiera has llegado hasta el fondo!"

            elif mc_body.orgasm >= 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡Si ya te has corrido [mc_body.orgasm] veces!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡Y NI SIQUIERA HAS LLEGADO HASTA EL FONDO!!"

                if current_girl.orgasm <= 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Como no tenga por lo menos 4 o 5 orgasmos te reventaré la puta cara!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "No pide poco ni nada el muy cabrón..."

            if (mc_body.orgasm >= 1 and current_girl.orgasm <= 3):

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Espero que me aguantes mucho más que lo has hecho hasta ahora!"

            $ mc_body.dick_speed = 3
            $ mc_body.store["dick"] = "Pussy_dick_med"

        elif afternight04_Pussy_dick_med_Speed_2_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_2_Done >= 1:

            if not (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"): #Dick Out

                if afternight04_Pussy_dick_med_Speed_2_Rape_Done == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Y si te cabalgo a una velocidad decente,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "la cosa inclusa mejora..."

                elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Y si por lo menos vuelvo a cabalgarte moviéndome un poco,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "mejor que mejor..."

                elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 3:

                    $ randomnum_1to3 = renpy.random.randint(1, 3)
                        
                    if randomnum_1to3 == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Y al menos así puedo hacer lo que tú no haces..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "follarte."

                    elif randomnum_1to3 == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Y quizás así te anime a que me folles igual,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "o mejor..."

                    elif randomnum_1to3 == 3:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils down03_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Y posiblemente de este modo puedas animarte a follarme tú,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows serious_a
                            with dissolve

                        d "en lugar de tener que cabalgarte yo..."


            else: #Dick In.

                if afternight04_Pussy_dick_med_Speed_2_Rape_Done == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Y con este ritmo no te me puedes quejar..."

                elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Y a este ritmo se siente de maravilla..."

                elif afternight04_Pussy_dick_med_Speed_2_Rape_Done == 3:

                    $ randomnum_1to3 = renpy.random.randint(1, 3)

                    if randomnum_1to3 == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Y con este ritmo,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        d "se disfruta algo mejor..."

                    elif randomnum_1to3 == 2:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Y al ritmo que te estoy cabalgando,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        d "se siente bien gustirrinín..."

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "¿No crees?"

                    elif randomnum_1to3 == 3:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils down04_a
                            show afternight04_sexbattle_d_eyebrows sadx02_a
                            with dissolve

                        d "Y mientras te cabalgué yo,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils down05_a
                            show afternight04_sexbattle_d_eyebrows sadx03_a
                            with dissolve

                        d "para que preocuparse,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils front05_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "¿No?"

            $ mc_body.dick_speed = 2
            $ mc_body.store["dick"] = "Pussy_dick_med"


    ########################
    ######################## med speed_1

        elif afternight04_Pussy_dick_med_Speed_1_Rape_Done >= 4 or afternight04_Pussy_dick_med_Speed_1_Done >= 4 :

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Aunque sinceramente..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "a este ritmo se nos hará de día..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Dídac..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "si vas más rápido es posible que me vaya a correr antes de..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡He dicho un poco más rápido!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No me vengas con mariconadas!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Un poco más rápido tampoco te hará ningún daño."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            $ mc_body.dick_speed = 2
            $ mc_body.store["dick"] = "Pussy_dick_med"

        elif afternight04_Pussy_dick_med_Speed_1_Rape_Done >= 1 or afternight04_Pussy_dick_med_Speed_1_Done >= 1:

            if afternight04_Pussy_dick_med_Speed_1_Rape_Done == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Aunque sería buena idea moverla un poco..."

            elif afternight04_Pussy_dick_med_Speed_1_Rape_Done == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Eso sí,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "moviéndome un poco,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "sino..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "que puta la gracia..."

            elif afternight04_Pussy_dick_med_Speed_1_Rape_Done == 3:

                $ randomnum_1to3 = renpy.random.randint(1, 3)

                if randomnum_1to3 == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Me voy a mover yo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "ya que parece que el macho alfa aquí solo sirve como estatua..."

                elif randomnum_1to3 == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Además te gusta que sea yo quien me mueva..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "¿Verdad que sí...?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Puto vago de mierda..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Oye!"

                elif randomnum_1to3 == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Por culpa de tu incompetencia,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02
                        with dissolve

                    d "al final tengo que ser yo quien te viola..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "O quizás lo haces expresamente porque disfrutas siendo un esclavo obediente..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

            $ mc_body.dick_speed = 1
            $ mc_body.store["dick"] = "Pussy_dick_med"

    ########################
    ######################## med speed_0

        elif afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0 and afternight04_Pussy_dick_med_Speed_0_Done == 0:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "La quiero dentro de mi..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            pt "Joder..."

            pt "Que raro y bizarro me parece eso viniendo de Dídac..."

            $ mc_body.dick_speed = 0
            $ mc_body.store["dick"] = "Pussy_dick_med"

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Es hora de moverse un poco..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¿No crees?"

            $ mc_body.dick_speed = 1
            $ mc_body.store["dick"] = "Pussy_dick_med"



######################################################
######################################################
######################################################
######################################################


        

    ##
######### DICK OUT OR LOW. Never used MED or DEEP. after 3rd Fail, LOW is never used again.

    else: #dick low or out. Never had dick in med.

    # NOT FINISHED RAPE COLOCATIONS.

        $ mc_body.store["dick"] = "Pussy_dick_low"  ### RAPE PUSSY DICK POSITION

        ###########################
        ###########################
        ########################### low speed_3

        if (afternight04_Pussy_dick_low_Speed_3_Rape_Done >= 1 or afternight04_Pussy_dick_low_Speed_3_Done >= 1): # Speed 3

            if afternight04_Pussy_dick_low_Speed_3_Done >= 1:

                if afternight04_Pussy_dick_low_Speed_3_Rape_Done == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Si te gusta frotar de forma rápida,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Quien soy yo para discutírtelo...?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    #$ mc_body.dick_speed = 3 ## Not necessary.

            if afternight04_Pussy_dick_low_Speed_3_Rape_Done == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Ya que no te atreves a meterla aún dentro,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "espero que no te disguste este ritmo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                $ mc_body.dick_speed = 3
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_3_Rape_Done == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Espero que no te me corras con los preliminares,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "ni siquiera me la has metido dentro aún..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                $ mc_body.dick_speed = 3
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_3_Rape_Done == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Como no me la metas dentro pronto,"
                
                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "lo acabaré haciendo yo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                $ mc_body.dick_speed = 3
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_3_Rape_Done >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡A tomar por culo!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Ya que no te da la puta gana de meterla tú mismo...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                $ mc_body.dick_speed = 0
                $ mc_body.store["dick"] = "Pussy_dick_med"

            #n "El ritmo de sus caderas se mueve de forma frenética frotando su entrepierna contra tu frenillo."

            #d "a mi también..."

        ###########################
        ###########################
        ########################### low speed_2

        elif (afternight04_Pussy_dick_low_Speed_2_Rape_Done >= 1 or afternight04_Pussy_dick_low_Speed_2_Done >= 1): # Speed 2

            if afternight04_Pussy_dick_low_Speed_1_Done >= 1:

                if (afternight04_Pussy_dick_low_Speed_1_Rape_Done == 1 or afternight04_Pussy_dick_low_Speed_1_Rape_Done == 1):

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happyTalkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Ya que veo que te gusta frotar tu polla contra mi coño..."

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    # $ mc_body.dick_speed = 2 ## Not necessary, it´s on the next.

            if afternight04_Pussy_dick_low_Speed_2_Rape_Done == 1:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Veamos cómo de dura se pone tu polla si te cabalgo a esta velocidad..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_low"
                
            elif afternight04_Pussy_dick_low_Speed_2_Rape_Done == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Te gusta que sea yo el que se frote contra tu polla..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Verdad?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Siempre he sabido que eras un salido..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Mira quien habla..."

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_low"

                #d "Espero que no te me corras con los preliminares, ni siquiera me la has metido dentro aún..."

            elif afternight04_Pussy_dick_low_Speed_2_Rape_Done == 3:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "¿Debo ser siempre yo quien toma la iniciativa?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Como no espabiles,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "la próxima vez aumentaré el ritmo..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                $ mc_body.dick_speed = 2 #Later is 3.
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_2_Rape_Done >= 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Si jugamos a preliminares,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "hagámoslo bien..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                $ mc_body.dick_speed = 3
                $ mc_body.store["dick"] = "Pussy_dick_low"

        ###########################
        ###########################
        ########################### low speed_1

        elif (afternight04_Pussy_dick_low_Speed_1_Rape_Done >= 1 or afternight04_Pussy_dick_low_Speed_1_Done >= 1): # Speed 1

            if afternight04_Pussy_dick_low_Speed_0_Done >= 1:

                if (afternight04_Pussy_dick_low_Speed_0_Rape_Done == 1 or afternight04_Pussy_dick_low_Speed_0_Rape_Done == 1):

                    if current_pose.id == "pose_1":

                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "No me vas a calentar demasiado teniendo tu pollón quieto encima de mí..."

                    # $ mc_body.dick_speed = 2 ## Not necessary, it´s on the next.

            if afternight04_Pussy_dick_low_Speed_1_Rape_Done == 1:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Mejor la muevo un poco,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve   

                d "para ir calentando..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "¿No crees...?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "Con ese tono de voz..."

                pt "Se está volviendo toda una zorra..."

                $ mc_body.dick_speed = 1
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_1_Rape_Done == 2:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Veo que la tienes bastante dura..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Cualquiera diría que tu compañero de piso te pone cachondo..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                $ mc_body.dick_speed = 1
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_1_Rape_Done == 3:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Acaso no te gustaría que hiciera algo más que frotar mi {i}horno{/i}..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "contra tu {i}anaconda{/i}..?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

                $ mc_body.dick_speed = 1 # Later will be 2.
                $ mc_body.store["dick"] = "Pussy_dick_low"

            elif afternight04_Pussy_dick_low_Speed_1_Rape_Done >= 4:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Si me sigo moviendo a esta velocidad,"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "acabaré sobándome..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Qué tal darle un poco más de vidilla a esto...?"

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                $ mc_body.dick_speed = 2
                $ mc_body.store["dick"] = "Pussy_dick_low"

        ###########################
        ###########################
        ########################### low speed_0

        elif (afternight04_Pussy_dick_low_Speed_0_Rape_Done >= 0 or afternight04_Pussy_dick_low_Speed_0_Done >= 0): # Speed 0

            if afternight04_Pussy_dick_low_Speed_0_Rape_Done == 0 and afternight04_Pussy_dick_low_Speed_0_Done == 0:

                $ mc_body.dick_speed = 0

                $ randomnum_1to5 = renpy.random.randint(1, 5) #Al ser 0, Només hi ha una oportunitat de llegirlos.

                if randomnum_1to5 == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "Es hora de comprobar como de dura la tienes [protname]..."

                elif randomnum_1to5 == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Quiero sentirla sobre mi piel..."

                elif randomnum_1to5 == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Si la montaña no va a {i}Mahoma{/i},"

                    extend " {i}Mahoma{/i} irá a la montaña..."

                elif randomnum_1to5 == 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Llevo todo el día esperando a sentir el tacto de tu polla..."

                elif randomnum_1to5 == 5:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Quiero notar en mi piel lo dura y caliente que la tienes [protname]..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve


            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Sentir tu ardiente polla sobre mi panocha,"

                extend " está bien..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "Pero,"

                extend " estaría bien moverse un poquito también..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                $ mc_body.dick_speed = 1


        else:

            $ debug ("This text should not be visible 257/8")

##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################
    ## Preparing Rape Battleground.

    if afternight04_SheRapingYou == False:

        #$ debug ("She´s now raping you 4815") #DELETE THIS

        $ afternight04_SheRapingYou = True # This conditional is active while she rapes you.

    #else:

        #$ debug ("You´re already being raped. 6187")
        

        

##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################
    ## CALLING IMAGE:
    
    call afternight04_Pussy_dick_rape_general_image #Dialogue is implemented inside the image.

##################################################################################################
#################################################################################################
################################################################################################
###############################################################################################
    ## DESCRIPTION:


    ## Advice to the player.

    if current_girl.total_fail == 2:

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            pt "Si vuelvo a repetir la misma acción sin éxito,"

            extend " me temo que la cosa va a empeorar..."

        elif randomnum_1to5 == 2:

            pt "Dudo que vaya a ser una buena idea repetir el mismo error tres veces..."

        elif randomnum_1to5 == 3:

            pt "Ya es la segunda vez que se queja haciendo lo mismo,"

            pt "si lo hago una tercera vez,"

            extend " puede ser peligroso..."

        elif randomnum_1to5 == 4:

            pt "Está claro que repetir más de dos veces el mismo error no va a ser una buena idea..."

        elif randomnum_1to5 == 5:

            pt "Me da la sensación que si hago lo mismo la próxima vez y no le gusta demasiado,"

            pt "se tomará la iniciativa..."

        

    return