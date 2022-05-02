default afternight04_mc_orgasms = 0

label afternight04_mostly_his_orgasm:

    ######
    ##### Blasfemias

    if current_pose.id == "pose_1":

        show afternight04_sexbattle_d_mouth sad_Silentx03_a
        show afternight04_sexbattle_d_eyes 02_a
        show afternight04_sexbattle_d_pupils front02_a
        show afternight04_sexbattle_d_eyebrows surprisex01_a
        with dissolve

    $ randomnum_1to5 = renpy.random.randint(1, 5)

    if randomnum_1to5 == 1:

        p "¡Mierda!"

    elif randomnum_1to5 == 2:

        p "¡Cagüen!"

    elif randomnum_1to5 == 3:

        p "¡Dios!"

    elif randomnum_1to5 == 4:

        p "¡Joder!"

    elif randomnum_1to5 == 5:

        p "¡Hostias!"

    ######
    ##### Your Notification

    if current_pose.id == "pose_1":

        show afternight04_sexbattle_d_mouth sad_Silentx04_a
        show afternight04_sexbattle_d_eyes 01_a
        show afternight04_sexbattle_d_pupils front01_a
        show afternight04_sexbattle_d_eyebrows surprisex02_a
        with dissolve

    if (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3):

        pt "A este ritmo y sintiendo toda mi polla dentro..."

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3):

        pt "Aunque no esté entera dentro,"

        extend " a este ritmo..."

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3):

        pt "Aunque solo esté frotándome el capullo,"

        extend " a este ritmo..."

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2):

        pt "Aunque vaya a este ritmo,"

        extend " sintiendo toda mi polla dentro..."

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2):

        pt "A pesar de ir a este ritmo"

        extend " y no tenerla toda dentro..."

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2):

        pt "Aunque solo esté frotando el capullo"

        extend " y a medio gas..." 

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1):

        pt "Aunque esté yendo despacio,"

        extend " la sensación de tener toda mi polla dentro..."

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1):

        pt "A pesar de que esté yendo despacio"

        extend " y con la polla a medio camino..."

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1):

        pt "Aunque apenas estoy frotándo la punta y yendo despacio..." 

    elif mc_body.dick_speed == 0:

        pt "¡¿Cómo es posible que me vaya a correr si no la muevo?!"

        if mc_body.store["dick"] == "Pussy_dick_deep":

            pt "Debería haberla sacado..."

            pt "se siente tan..."

            extend " al tenerla entera dentro..."

        elif mc_body.store["dick"] == "Pussy_dick_med":

            pt "Aunque no la tenga toda dentro..."

            extend " igualmente se siente bien..."

        elif mc_body.store["dick"] == "Pussy_dick_low":

            pt "¡Ni siquiera la tengo dentro!"

    else:

        $ debug ("That means you failed in this action and she made you cum. 001")

    pt "Ya no puedo aguantar más..."

    if mc_body.orgasm == 2:

        pt "y lo peor es que es mi segunda vez..."

    elif mc_body.orgasm == 3:

        pt "y lo peor es que es mi última vez..."

    ######
    ##### Her reaction.

    #################################
    ################################
    ############################### Your 1rst Orgasm

    if mc_body.orgasm == 1:

        if current_girl.orgasm == 0:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "¡¿Ya te vas a correr?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            d "¡¿Tan pronto?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

        elif current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "¿Te vas a correr ya?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            d "Veo que te vas a correr..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "¡Ya era hora de que te corrieras!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "¡POR FIN TE CORRES!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Estás hecho todo un semental cabrón!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

    #################################
    ################################
    ############################### Your 2nd Orgasm

    elif mc_body.orgasm == 2:

        if current_girl.orgasm == 0:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿OTRA VEZ?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¿ES QUE NO TIENES RESISTENCIA?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

        elif current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡¿Otra vez?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿Otra vez te vas a correr?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "Así estaremos a la par..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Pensaba que serías mejor semental..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Veo que también disfrutas de mi compañía..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "¡AL FIN TE VUELVES A CORRER!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "¡Pedazo macho cabrío estás hecho!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

    #################################
    ################################
    ############################### Your 3rd Orgasm

    elif mc_body.orgasm >= 3:

        if current_girl.orgasm == 0:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils down00_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡¿¿EN SERIO??!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡¡¿OTRA VEZ?!!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡TE CORTARÉ LOS HUEVOS COMO NO SE TE VUELVA A LEVANTAR!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¿¡¡ME OYES!!?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx10_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

        elif current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils down00_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡¿OTRA VEZ?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Solo he tenido un puñetero orgasmo de mierda!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¡Por tu puta madre espero que no sea tu última corrida!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx08_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡¿En serio?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡¿Te vas a correr ya?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Solo he tenido dos orgasmos!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡¿Otra vez?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Aguanta un poco más joder!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Solo he tenido tres orgasmos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Tu tercera corrida..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "No puedo negar que te lo has currado..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Semental cabronazo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

    else:

        $ debug ("This message should not appear PEDOBEAR 001")

    #################################
    ################################
    ############################### 
    ## Cumshot.

    menu afternight04_dick_orgasm_condom_question:
        
        pt "¿Me corro encima de ella? ¿O lo hago dentro del condón?"
        
        "<Correrse dentro del condón>":
            
            call p_Help

            $ afternight04_condom_on = True

            if afternight04_condom_broken == False:

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                $ mc_body.dick_speed = 0
                call afternight04_Pussy_dick_cum_scene
                #call afternight04_Pussy_dick_general_image
                with hpunch

                pause 0.5

                show afternight04_sexbattle_effects white_cumming
                show afternight04_sexbattle_mc_dick_pussy_cumshot empty
                with dissolve

                p "Aaaaaghh..."

                show afternight04_sexbattle_mc_dick_cumshot empty
                show afternight04_sexbattle_effects black
                with Dissolve (2.0)

            else:

                p "Ughh..."

                n "En el momento en el que decides agarrar la polla para sacarla,"

                jump afternight04_dick_orgasm_condom_broken

        "<Correrse encima de ella>":

            if afternight04_condom_broken == False:

                call p_Help

                $ afternight04_CumOnStomach += 1
                $ afternight04_condom_on = False

                $ debug ("000075")

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                $ debug ("333375")

                call afternight04_Pussy_dick_cum_scene

                $ debug ("032875")

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                show afternight04_sexbattle_effects white_cumming
                with hpunch
                
                p "Aaaaaghh..."

                show afternight04_sexbattle_mc_dick_cumshot empty
                show afternight04_sexbattle_effects black
                show afternight04_sexbattle_mc_dick_pussy_cumshot empty # Cumshot Animation Naked Dick Hide
                with Dissolve (1.0)

            else:

                $ afternight04_condom_on = False

                p "Ughh..."

                n "En el momento en el que decides agarrar la polla para sacarla,"

                jump afternight04_dick_orgasm_condom_broken

    #Here is where comes the Cum Scene

    show afternight04_sexbattle_effects empty
    with Dissolve (3.0)

    ## POST-Corrida.

    if mc_body.orgasm == 1:

        if current_girl.orgasm == 0: #Only a single orgasm for MC  (mc_body.orgasm == 1) (current_girl.pleasure <= 50)

            if afternight04_condom_on == True:

                if current_girl.pleasure < 20:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Te has corrido sin que ni siquiera hayas empezado a hacerme nada!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Hombre..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "algo estoy haciendo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Me estás haciendo cabrear!"

                    d "¡Eso es lo que estás haciendo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Deja de hacer el imbécil y fóllame de una puta vez!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "No parece muy contenta..."

                elif current_girl.pleasure >= 20:
                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Te corres antes de que yo haya tenido ni siquiera uno?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Qué ñordo de semental estás hecho?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Ten claro que no voy a conformarme con uno o dos orgasmos de mierda."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Espero que no me decepciones [protname]..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "Joder con Dídac..."

                    pt "Está que se sube por las paredes..."

                elif current_girl.pleasure >= 40:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿En serio?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Aún no he tenido ni un solo orgasmo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Sí que duras poco..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Te tenía por mejor semental..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "A ver cuantos asaltos más duras..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "campeón..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            else: #Cumming Outside 1rst Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Serás perro!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Encima de precoz..."

                extend " ¡te me corres encima!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Ni siquiera he tenido un puto orgasmo aún!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Qué puta mierda de semental eres?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            pt "No sé si disfruta más follándome,"

            pt "o humillándome..."

        elif current_girl.orgasm == 1:

            if afternight04_condom_on == True:

                if current_girl.pleasure < 45:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Ya...?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Solo he tenido un orgasmo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Te tenía por mejor semental..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Espero que estos solo sean preliminares y dures más..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Me alegro que te hayas corrido [protname],"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pero llevo tan solo un orgasmo de mierda!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Los mismos que yo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "¿No?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¿Con cuantas tías has estado maldito {a=https://es.wikipedia.org/wiki/Macho_ibérico}macho ibérico{/a} de pacotilla?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Probablemente con muchas más que tú."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Je..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Ya te gustaría..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "Puto engreído de mierda..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Demuéstralo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Dudo que puedas aguantar un infinito número corridas."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Así que da la talla antes de correrte otra vez."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Ten por seguro que espero muchísimo más de ti."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Queda claro?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

            else: #Cumming Outside 1rst Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡La madre que te...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Solo me he corrido una vez y encima te me corres encima!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Vaya mierda de semental estás hecho tío..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            pt "No parece que esté bromeando..."

        elif current_girl.orgasm == 2:

            if afternight04_condom_on == True:

                if current_girl.pleasure < 80:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Tu primer orgasmo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Tú llevas dos,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "sino me equivoco..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "así es..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Pero espero llegar pronto al tercero"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "y luego al cuarto"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "y así sucesivamente..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Así que ponte las pilas y no te vuelvas a correr demasiado pronto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿De acuerdo?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "Encima mandona,"

                    extend " tendrá morro..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No está mal..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Ya has conseguido que me corra dos veces,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "pero espero que aguantes un poco más..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Esto no ha hecho más que empezar,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Tigre..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            else: #Cumming Outside 1rst Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Serás jodío!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Para qué coño te doy un condón?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Para que te me corras encima como un animal?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "El condón es para no correr riesgos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¿Te gustaría que yo me corriera encima de ti?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "En cierto modo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "me estás dejando empapado la entrepierna con tus \"flujos vaginales\"..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No es lo mismo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "cacho perro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Esa es tu opinión..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "A ver si por lo menos duras un poco más la próxima vez..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

        elif current_girl.orgasm == 3:

            if afternight04_condom_on == True:

                if current_girl.pleasure < 80:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "Tu primera corrida..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Se nota que ibas cargadito,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx022_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils down02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "has dejado el condón hecho un globo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Pero espero que esto solo sea el precalentamiento..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Tú ya llevas tres orgasmos."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Y espero tener muchísimos más..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Semental..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "Puto Dídac..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Cabrón..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Ya era hora de que te corrieras."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¿Acaso tienes alguna queja...?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Te he dicho que pares?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

            else: #Cumming Outside 1rst Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sads_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Serás cabrón!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "¿Qué pasa?"

                #if afternight04_CumOnStomach == 1: ##Not necessary.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Te me has corrido encima!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Tú ya llevas tres..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "no veo que te hayas quejado hasta el momento,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "de llenarme de tus flujos vaginales por toda mi entrepierna..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No es lo mismo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "imbécil..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "¿Quieres que pare?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Ni te atrevas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

        elif current_girl.orgasm >= 4:

            if afternight04_condom_on == True:

                if current_girl.pleasure < 80:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "La madre que te parió..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Tu primer orgasmo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Y yo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils up04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "ni si quiera sé..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "cuantos llevo ya..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils up05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Pero ni se te ocurra para ahora..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Entendido?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Apenas estoy empezando... "

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Ese es el semental que he estado esperando todo el puto día..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "..."

                    pt "¿Está hablándome en tercera persona?"

                else: 

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Serás cabrón..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¿Hay algún problema?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Sabía que eras bueno en la cama..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "¡Pero no tanto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Y solo me he corrido una vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "espera ver el resto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "No pares..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

            else: #Cumming Outside 1rst Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Mamón..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Te me has corrido encima!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Tú llevas varias veces corriéndote encima de mí."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Tengo la entrepierna empapada por tu culpa,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "y no me he quejado en ningún momento..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "¿Quieres que pare?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Ni se te ocurra..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

        else:

            $ debug ("This message should NOT appear. Jurassic BOOM 003")

    elif mc_body.orgasm == 2:

        if current_girl.orgasm == 0: #Only a single orgasm for MC  (mc_body.orgasm == 1) (current_girl.pleasure <= 50)

            if afternight04_condom_on == True:

                if current_girl.pleasure < 20:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Te lo estás pasando bien;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Verdad?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Bueno..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Te has corrido ya dos veces,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    d "no me dirás que no..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡PUES YO NO LLEVO NI UN PUTO ORGASMO DE MIERDA!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿A qué coño juegas?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Ya solo queda un puto jodido condón!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Te lo advierto;"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "no me conformaré con un solo puto orgasmo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "después de estar esperándote todo el puto día..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿QUEDA CLARO?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    pt "Cualquiera le dice algo..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¿¡Otra vez...?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "[protname],"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "te he pedido que me folles,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "no que te lo pases bien tú solo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Para eso ya me basto yo sola..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Te lo advierto,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "solo queda un puto condón..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "como no lo uses bien,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "Te rompo las pelotas."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¿Me explico?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

            else: #Cumming Outside 2nd Time.

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡¿OTRA VEZ?!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡¿PERO QUÉ COÑO PASA CONTIGO?!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡ENCIMA DE QUE AÚN NO ME HE CORRIDO NI UNA PUTA VEZ!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                if afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿QUÉ?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Te me has corrido encima?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Se puede saber qué coño pasa contigo?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                #else:

                    #$ debug ("This text should not appear MADAFAAAAA 003")

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Tiene parte de razón..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Si te estuvieras más quietecita,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "en lugar de ir meneándomela cada dos por tres..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Ni mi primera vez,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "cuando tenía catorce años,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "con una cuarentona,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "lo hice tan mal como tú..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "¡¿Qué?!"

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Como te vuelvas a correr encima,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "te voy a cortar las pelotas."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿QUEDA CLARO?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    pt "No parece que haga broma..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡No hagas que me arrepienta de esto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Aquí está el último condón."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Y esta vez..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Úsalo!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "pero ni se te ocurra hacerlo pronto..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Te aseguro que no me conformaré con uno o dos orgasmos de mierda..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "A veces da hasta miedo y todo..."


        elif current_girl.orgasm == 1:

            if afternight04_condom_on == True:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Maldito seas [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Ya te has corrido dos puñeteras veces!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡y solo queda un jodido condón de mierda!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Pero tú también te has corrido..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿¿Te crees que me conformo con un puto jodido cutre orgasmo de puta mierda??!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "A mi no me ha parecido que fuera tan cutre..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Como se te ponga flácida y rancia,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "antes que yo tenga por lo menos más de tres orgasmos;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve
                
                d "¡Te la voy a cortar y se la daré a los perros!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿QUEDA CLARO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Mejor no le digo que estoy cada vez más cerca de mi última corrida entonces..."

            else: #Cumming Outside 2nd Time.

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡ES LA SEGUNDA VEZ QUE TE ME CORRES ENCIMA!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿TIENES ALGÚN PUTO PROBLEMA DE SORDERA?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡¿O ERES UN GILIPOLLAS?!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx09_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "No parece muy contento..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve


                elif afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿POR QUÉ NARICES TE ME CORRES ENCIMA?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "No parece que le haya gustado demasiado..."


                else:

                    $ debug ("This text should not Appear. MADAFAAA 002")

        elif current_girl.orgasm == 2:


            if afternight04_condom_on == False: #Cumming Outside 2nd Time.

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Es la segunda vez que te me corres encima!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿Tienes algún problema de sordera?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve


                elif afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Por qué narices te me corres encima?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

            elif afternight04_condom_on == True: #Not Cum Outside.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Bueno..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            p "Dos a dos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "estamos empatados ahora..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿Te crees que esto es un puto partido?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Tu polla no está tan erecta como al principio;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "y me temo que eso es porque no vas a durar una cuarta ronda."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Eso sin mencionar que ya no quedan más condones..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Y te aseguro que no me voy a conformar con solo tres orgasmos,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "no después de haber estado esperándote todo el puto día..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¿Queda claro?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Quizás no eres tan multiorgásmica como piensas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "No todas las chicas tienen infinidad de orgasmos,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "hay algunas que ni siquiera logran tener uno..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "El problema es que eres un puto precoz de mierda."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            pt "Tiene un don a la hora de adularme..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "Haz lo que debas,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "pero no me decepciones;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "o no responderé de mis actos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve



        elif current_girl.orgasm == 3: # mc_body.orgasm = 2

            if afternight04_condom_on == False:#Cumming Outside 2nd Time.

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    d "¿Otra vez te me corres encima?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tienes problemas de sordera..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Verdad?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve


                elif afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils down01_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Por qué diablos te me corres encima?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                        with dissolve

                    p "¿No te gusta?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "No me encanta..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

            d "Con lo que me ha costado convencerte,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "y lo bien que lo estás disfrutando ahora..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "Espero que uses con cabeza el próximo condón,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "porque es el último..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Y no me voy a conformar con un mísero orgasmo más;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "quiero bastantes más..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿Entendido?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "¿Se cree que soy un vibrador con patas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "¿o qué?"


        elif current_girl.orgasm >= 4: # mc_body.orgasm = 2

            if afternight04_condom_on == False:

                if afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Qué?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Nada,"

                    extend " nada..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "total haces lo que te sale de los huevos..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Sí,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "precisamente eso que tienes en la barriga me ha salido de los huevos."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Gilipollas..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                elif afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Te me has corrido encima..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Buena observación,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "querido {i}Watson{/i}..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Eres un imbécil..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            d "El que decía que le daba cosa follar conmigo;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "y míralo ahora..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Dios..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "ya llevo [current_girl.orgasm] putos orgasmos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Yo aún no he terminado."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "No pares [protname],"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "fóllame sin piedad..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve



#############################################
############################################
###########################################
##########################################

        ## END OF THE NIGHT.

    elif mc_body.orgasm >= 3:

        hide screen dummy_screen
        hide screen premium_dashboard
        with dissolve

        if current_girl.orgasm == 0:

            if afternight04_condom_on == True:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils down00_a
                    show afternight04_sexbattle_d_eyebrows surprisex02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Va en serio...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿Por qué no la estoy notando dura?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Ya me he corrido tres veces..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Ese es realmente tu límite?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Aparentemente..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "sí..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¡NO HE TENIDO NI UN PUTO ORGASMO DE MIERDA!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¡ME CAGO EN LOS CLAVOS DE LAS BISAGRAS DE LAS TAPAS DE LAS CAJAS DE TUS MUERTOOOOS!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

            else: #Cumming Outside 3rd Time.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils down00_a
                    show afternight04_sexbattle_d_eyebrows surprisex02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Esto te hace alguna puta gracia?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Por qué se te está volviendo flácida la puta polla?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                p "Bueno..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Ya me he corrido tres veces..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Y?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Ese es mi límite..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Te estás cachondeando de mí..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Verdad?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿TE ME HAS CORRIDO ENCIMA DE LA PUTA BARRIGA SIN QUE YO HAYA TENIDO NI UN JODIDO ORGASMO?!"

                elif afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡¿TE ME HAS CORRIDO DOS PUTAS VECES ENCIMA DE LA PUTA BARRIGA SIN QUE YO HAYA TENIDO NI UN SOLO PUTO ORGASMO?!!"

                elif afternight04_CumOnStomach == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡¿TE ME HAS CORRIDO TRES PUTAS VECES ENCIMA DE LA PUTA BARRIGA SIN QUE YO HAYA TENIDO NI UN SOLO PUTO JODIDO ORGASMO DE MIERDA?!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿Y AHORA ME DICES QUE ESE ES TU PUTO LÍMITE?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Sí..."

            #$ debug ("Here is where Didac goes out with rage, dressing herself and going to street, you´re so weak that you can´t follow her.")

        elif current_girl.orgasm == 1:

            if afternight04_condom_on == True:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Por qué no la estoy notando dura...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Por que esa mi tercera corrida..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "¿Y...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Ese es mi límite..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Estás de coña..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Verdad?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "Aparentemente no..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿ME ESTÁS DICIENDO QUE TE HAS CORRIDO TRES PUTAS VECES Y YO SOLO HE TENIDO UN SOLO PUTO ORGASMO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿Y LO DICES TAN TRANQUILO?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Me lo parece,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿o estás perdiendo la erección..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious
                    with dissolve

                p "Ya me he corrido tres veces..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "¿Y?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Ese es mi límite..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡TE ME HAS CORRIDO ENCIMA DE LA PUTA BARRIGA!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡Y TAN SOLO HE TENIDO UN PUTO ORGASMO!!"

                elif afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡TE ME HAS CORRIDO DOS PUTAS VECES ENCIMA DE LA JODIDA BARRIGA!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡Y SOLO HE TENIDO UN PUTO MÍSERO ORGASMO!!"

                elif afternight04_CumOnStomach == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡TE ME HAS CORRIDO TRES PUTAS VECES ENCIMA DE LA JODIDA BARRIGA!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Y YO SOLO HE TENIDO UN PUTO JODIDO ORGASMO DE MIERDA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Y ME VIENES CON QUE ESTE ES TU PUTO LÍMITE?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "Sí..."

                #$ debug ("Here ALSO is where Didac goes out with rage, dressing herself and going to street, you´re so weak that you can´t follow her.")

        elif current_girl.orgasm == 2:

            if afternight04_condom_on == False:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Te lo pasas bien corriéndote encima de mi barriga?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows suspicious01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspicious02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¿Me lo parece a mi...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows suspicious01_a
                with dissolve

            d "¿o tu erección se está yendo a tomar por el culo...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspicious02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Ha sido mi tercera corrida..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspicious02_a
                with dissolve

            d "¿Me estás diciendo que esa fue tu última carga?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Sí..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Que ya no aguantas ninguna más..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "Sí..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Que me he corrido solo dos putas veces;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "tú tres."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Y te quedas tan tranquilo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "Eres bastante peor de lo que me hubiera imaginado [protname]."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Tú tampoco me lo has puesto fácil..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "Lo que yo te he estado pidiendo desde el principio es que me folles..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "Pero se ve que prefieres correrte tres veces,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "y a mi que me den;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "con dos orgasmos ya tengo suficiente."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "¿No?"

            if afternight04_CumOnStomach == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Por si fuera poco,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "te me corres encima de la barriga..."

            elif afternight04_CumOnStomach == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Por si fuera poco,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "te me has corrido dos veces encima de la barriga."

            elif afternight04_CumOnStomach == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Por si fuera poco,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "te me has corrido tres putas veces encima de la jodida barriga..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx09_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils rightt02_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "Sinceramente me has decepcionado bastante [protname]."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "Voy a tomarme una ducha,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "espérate aquí hasta que acabe..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "luego haz lo que te de la gana,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "yo me iré a la cama."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            scene afternight04_sexbattle_background a
            with vpunch

            n "Con suma sequedad,"

            n "se aparta de ti,"

            d "y se dirige desnuda hacia el oscuro pasillo mientras oyes sus desnudos pasos hasta llegar al baño."

            pt "Hay que joderse..."

            pt "¡Encima que le hago el favor!"

            pt "Puto Dídac..."

            ono "BBBBRRRRRRRRRR"

            pt "Barriga de las narices..."

            n "Con cierta dificultad y falta de fuerza,"

            scene black
            with fade

            $ saturation_tint_level = "superdark"

            n "te pones de pie y te diriges a la cocina para ver si encuentras algo para llevarte a la boca."

            scene morning04_bg_kitch_toastwithjam
            with fade

            ono "Neeec"

            n "A lo lejos,"

            n "oyes la puerta del baño y luego la de la habitación."

            ono "Pum"

            pt "Me imagino que habrá terminado..."

            scene afternight03_bg shower
            with fade

            n "Decides seguir su ejemplo y tomarte una ducha antes de ir a la cama."

            scene beds_night_lightOff_blindDown_DemptyMCempty
            show beds_D03_night_lightOff_blindDown
            with fade

            n "El corto trecho que separa ambas camas,"

            n "no es nada en comparación a la fría distancia emocional que os separa ahora mismo."

            pt "Nunca me había sentido tan raro yendo a dormir al lado de Dídac..."

            pt "ni siquiera una broma,"

            pt "un gesto..."

            pt "Ni un \"buenas noches\"..."

            pt "Encima de que le he hecho el puto favor..."

            pt "Bahh..."

            pt "Da igual,"

            pt "mañana será otro día y será la última cita con Neus..."

            scene beds_night_lightOff_blindDown_DemptyMCbusy
            show beds_D03_night_lightOff_blindDown
            with dissolve

            n "Finalmente te acomodas en tu cama y te reúnes con el sueño."

            $pl.ch_pts("dp", 1) #She Had 2 orgasms.

            jump morning05

            #$ debug ("She is pissed, but doesn´t leave...")

        elif current_girl.orgasm == 3:

            if afternight04_condom_on == False:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..." #Mirando la corrida.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                if afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Hacía falta...?"

                elif afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¿Era necesario que te corrieras por segunda vez encima de mí...?"

                elif afternight04_CumOnStomach == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿Tenías que correrte una tercera puñetera vez encima de mí?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¿Para qué coño te pones el puto condón?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Para que no me corra dentro de ti...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils down02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Parece que tu polla se está empezando a desinflar..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "Eso parece..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Por lo visto no te vas a correr más de tres veces..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Por lo visto no..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Y te parece bien..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¿No?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "Hombre..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "te has corrido tres veces,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "las mismas que yo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¿Qué mierda de puta respuesta es esta?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "O sea,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "como tú con tres ya tienes suficientes,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "para mí debe ser también suficiente..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "¿No?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "¿Cuántas veces se suelen correr las tías con las que quedas tú?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils right01_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Eso no tiene nada que ver."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "No tienes ni la más remota idea;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¿Verdad?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "Porque ni se lo preguntas;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            p "ni si quiera te importa lo más mínimo."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "¿O acaso me equivoco...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡No estamos hablando de mí!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "No,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "estamos hablando de {i}Pepito grillo{/i}."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "Me criticas por que no he satisfecho tus expectativas imaginarias,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "a pesar que has tenido los mismos orgasmos que yo."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Y encima tienes los santos cojones de hacerlo cuando tu trato con las mujeres es básicamente nulo."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "¡Cuando lo único que he procurado es de hacerte un puto favor que me has suplicado!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils left04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "No te lo he suplicado..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Aparte,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "yo no soy una cualquiera;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "y te he pedido un favor a ti,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "[protname]."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils right02_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            d "Además..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "tampoco parece que te lo hayas pasado tan mal..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            pt "Bueno,"

            pt "Eso no se lo puedo negar..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Lo que he intentado es cumplir con lo que me has pedido;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "y lo único que he recibido son quejas y malas maneras."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Creo que no me merezco esto por tu parte."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "No..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "¿Qué?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "No te he oído..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡He dicho que no!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Que no qué?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Que no te mereces como te he tratado..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "Eso está mejor..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            scene afternight04_sexbattle_background a
            with vpunch

            n "Rápidamente se aparta de ti."

            d "Bueno..."

            d "yo voy a ir a tomarme una ducha."

            p "¿Y ya está?"

            if music_play != "torn_apart":
                play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "torn_apart"

            scene morning04_bg livingroom_roomOthersLingerie_night_LightOn_blur01
            show didacfbodybelow naked:
                dfbody_closeX2_
            show didacfbodybelow_panties empty:
                dfbody_closeX2_
            show didacfbodybelow_naked_drops 01:
                dfbody_closeX2_
            show didacfbodytop naked:
                dfbody_closeX2_
            show didacfbodytop_naked_drops 01:
                dfbody_closeX2_
            show didacfbodycloth maleshirt_empty:
                dfbody_closeX2_
            show didacfhandl hip_naked:
                dfbody_closeX2_
            show didacfhandl_hip_naked_drops 01:
                dfbody_closeX2_
            #show dfbody_afternight03_hallway03_b_superdark:
                #dfbody_closeX2
            show didacf_blush 03:
                dexpressions_closeX2_
            show didacf_eyes 01:
                dexpressions_closeX2_
            show didacf_pupils front01:
                dexpressions_closeX2_
            show didacf_eyebrows normal:
                dexpressions_closeX2_
            show didacfbodytop_hair:
                dfbody_closeX2_
            show didacf_mouth sad_Silentx01:
                dexpressions_closeX2_
            show didacfhandr leg_naked:
                dfbody_closeX2_
            show didacfhandr_leg_naked_drops 01:
                dfbody_closeX2_
            with fade

            d "¿Hum?"

            show didacf_eyebrows angryx01
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_mouth sad_Silentx05
            with dissolve

            p "¿No tienes nada que decirme?"

            show didacf_eyebrows sadx01
            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_mouth sad_Talkingx002
            with dissolve

            ## NOT FINISHED

            d "A..."

            extend " A qué..."

            extend " ¿A qué te refieres?"

            show didacf_eyebrows sadx02
            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_mouth sadbiting_Silentx05
            with dissolve

            d "..."

            show didacf_eyebrows surprisex01
            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_mouth sad_Silentx01
            with dissolve

            p "Un gracias por ejemplo."

            show didacf_eyebrows sadx01
            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "Aahh..."

            show didacf_eyebrows sadx02
            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_mouth sad_Talkingx01
            with dissolve

            d "Sí..."

            show didacf_eyebrows sadx01
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_mouth happy_Talkingx01
            with dissolve

            d "Gracias capullo."

            scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
                transform_anchor True
                xalign 0.5 yalign 0.5
                zoom 0.2
            with dissolve

            n "Con cierto nerviosismo ves a tu compañero de piso alejarse hasta desaparecer en la oscuridad del pasillo."

            p "..."

            pt "¿Qué pensaba que le iba a pedir...?"

            show morning04_bg livingroom_room_night_lingerie_others_LightOn
            with hpunch

            ono "BBBBRRRRRRRRRR"

            pt "Jodida barriga..."

            $ saturation_tint_level = "superdark"

            pt "Aunque es cierto que hace horas que prácticamente no he comido nada..."

            scene morning04_bg_kitch_toastwithjam
            with fade

            n "Te diriges a la cocina para ver si encuentras algo para saciar a tu estómago,"

            ono "Neeec"

            n "Pasado un tiempo oyes el ruido del baño abriéndose."

            ono "Pum"

            n "Y acto seguido la puerta de lo que parece ser vuestra habitación cerrándose."

            pt "Me imaginó que habrá terminado de ducharse."

            scene afternight03_bg shower
            with fade

            n "Concluyes tu improvisada cena y decides tomar su ejemplo en el baño."

            scene beds_night_lightOff_blindDown_DemptyMCempty
            show beds_D03_night_lightOff_blindDown
            with fade

            pt "Parece que esté durmiendo..."

            scene beds_night_lightOff_blindDown_DemptyMCbusy
            show beds_D03_night_lightOff_blindDown
            with dissolve

            n "Decides meterte en la cama con cuidado para no despertar a tu compañero de cuarto."

            d "Buenas noches [protname]."

            n "Su voz contenía un tinte de nerviosismo, pero al mismo tiempo era cálida."

            p "..."

            pt "No suele darme las buenas noches..."

            pt "y mucho menos sin propinarme algún insulto..."

            pt "que raro..."

            p "Buenas noches Dídac."

            n "Caes rendido en el sueño poco después."

            $pl.ch_pts("dp", 5) #She Had 3 orgasms.

            jump morning05
            #$ debug ("She is a bit pissed, but doesn´t leave...")
            
        elif current_girl.orgasm >= 4: # It´s your 3rd cum and afternight04_dick_orgasm_condom_broken = False 

            if afternight04_condom_on == False:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "..." #Mirando la corrida.

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

                if afternight04_CumOnStomach == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¿Era necesario...?"

                elif afternight04_CumOnStomach == 2:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¿Tenías que correrte por segunda vez encima de mi barriga...?"

                elif afternight04_CumOnStomach == 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Tenías que correrte una tercera puñetera vez encima de mí?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "¿Por qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿No te lo has pasado suficientemente bien?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve


                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Para qué coño te doy entonces el jodido condón?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "¿Para que no me corra dentro de ti...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "..."

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Parece que tu polla ya no puede más..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Tú también pareces algo agotada..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "¿Cuántos orgasmos has tenido al final?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "{size=15}[current_girl.orgasm]{/size}"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Perdona,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "no te he oído..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¿Cuántos?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡He tenido [current_girl.orgasm] orgasmos!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Ahh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "ahora sí..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Gilipollas..."

            if music_play != "torn_apart":
                play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "torn_apart"

            scene morning04_bg livingroom_roomOthersLingerie_night_LightOn_blur01
            show didacfbodybelow naked:
                dfbody_closeX2_
            show didacfbodybelow_panties empty:
                dfbody_closeX2_
            show didacfbodybelow_naked_drops 02:
                dfbody_closeX2_
            show didacfbodytop naked:
                dfbody_closeX2_
            show didacfbodytop_naked_drops 02:
                dfbody_closeX2_
            show didacfbodycloth maleshirt_empty:
                dfbody_closeX2_
            show didacfhandl hip_naked:
                dfbody_closeX2_
            show didacfhandl_hip_naked_drops 02:
                dfbody_closeX2_
            #show dfbody_afternight03_hallway03_b_superdark:
                #dfbody_closeX2
            show didacf_blush 04:
                dexpressions_closeX2_
            show didacf_eyes 02:
                dexpressions_closeX2_
            show didacf_pupils front01:
                dexpressions_closeX2_
            show didacf_eyebrows normal:
                dexpressions_closeX2_
            show didacfbodytop_hair:
                dfbody_closeX2_
            show didacf_mouth sad_Silentx01:
                dexpressions_closeX2_
            show didacfhandr leg_naked:
                dfbody_closeX2_
            show didacfhandr_leg_naked_drops 02:
                dfbody_closeX2_
            with fade

            p "Así que al final resulta que no soy tan mal amante como creías..."

            show didacf_eyebrows surprisex01
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_mouth sad_Silentx02
            with dissolve

            p "¿No es así?"

            show didacf_eyebrows sadx01
            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_mouth happy_Silentx03
            with dissolve

            d "..."

            show didacf_eyebrows angryx01
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_mouth happy_Talkingx01
            with dissolve

            d "No,"

            show didacf_eyebrows sadx02
            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_mouth happy_Talkingx02
            with dissolve

            d "supongo que no..."

            show didacf_eyebrows serious
            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_mouth happy_Silentx02
            with dissolve

            p "Los dos estamos sudando bastante..."

            show didacf_eyebrows surprisex01
            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_mouth sad_Silentx01
            with dissolve

            d "..."

            show didacf_eyebrows sadx01
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_mouth sad_Talkingx001
            with dissolve

            d "A que..."

            show didacf_eyebrows suspiciousx01
            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "¿A qué te refieres con eso?"

            show didacf_eyebrows surprisex01
            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_mouth sad_Silentx03
            with dissolve

            p "Que necesitamos una ducha,"

            show didacf_eyebrows sadx02
            show didacf_eyes 02
            show didacf_pupils right02
            show didacf_mouth sadbiting_Silentx02
            with dissolve

            p "¿No crees?"

            show didacf_eyebrows sadx03
            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_mouth sadbiting_Silentx05
            with dissolve

            d "..."

            show didacf_eyebrows sadx02
            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_mouth sadbiting_Silentx02
            with dissolve

            p "¿O es que acaso quieres que te vuelva a lavar como el otro día?"

            show didacf_eyebrows angryx02
            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_mouth sad_Talkingx002
            with dissolve

            d "¡Idiota!"

            scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
                transform_anchor True
                xalign 0.5 yalign 0.5
                zoom 0.2
            with dissolve

            n "Rápidamente se aparta de ti"

            n "y con sus pies desnudos se dirige al oscuro pasillo que conduce al baño."

            n "Justo antes de desaparecer en la negrura."

            d "[protname]."

            n "Una voz cálida y femenina se desprende de sus palabras."

            p "..."

            n "como nunca habías oído antes salir de sus labios."

            d "Gracias..."

            p "..."

            pt "Definitivamente,"

            pt "no se parece en nada al Dídac que yo conozco..."

            play sound "audio/sfx/stomach01.ogg"

            show morning04_bg livingroom_room_night_lingerie_others_LightOn
            with hpunch

            ono "BBBBRRRRRRRRRR"

            p "..."

            pt "Jodido estómago de las narices..."

            pt "Supongo que es normal..."

            pt "no he comido nada que haya digerido en horas..."

            pt "Bueno,"

            $ saturation_tint_level = "superdark"

            pt "supongo que habrá algo que picar en la nevera."

            scene morning04_bg_kitch_toastwithjam
            with fade

            n "Al poco rato de estar saciando tu estómago de la peor manera oyes un ruido a lo lejos."

            play sound "audio/sfx/door_open01.ogg"

            ono "Neeeec"

            pt "Esa debe de ser la puerta del baño."

            play sound "audio/sfx/door_close01.ogg"

            ono "Pum"

            pt "Y esa la de la habitación."

            pt "Dídac habrá terminado de ducharse."

            scene afternight03_bg shower
            with fade

            n "Decides hacer lo mismo."

            scene beds_night_lightOff_blindDown_DemptyMCempty
            show beds_D03_night_lightOff_blindDown
            with fade

            n "Poco después entras en la habitación que compartís."

            n "Te encuentras a Dídac desnuda como de costumbre, durmiendo a pierna suelta sobre su cama."

            pt "Parece que está realmente agotada..."

            pt "aunque para ser franco,"

            pt "creo que yo también lo estoy bastante..."

            scene beds_night_lightOff_blindDown_DemptyMCbusy
            show beds_D03_night_lightOff_blindDown
            with dissolve

            n "Sin más dilación, te abres paso en tu alcoba y sin demasiada dificultad caes en un sueño profundo."

            $pl.ch_pts("dp", 10) #She Had +4 orgasms. (Not Pregnant)

            jump morning05

    ## Wearing a new CONDOM Scene.

    if mc_body.orgasm == 1:

        show afternight04_sexbattle_effects newcondom
        with dissolve

        d "Toma,"

        d "el segundo condón."

        d "Espero que este te dure más."

        show afternight04_sexbattle_effects empty
        with dissolve

    if mc_body.orgasm == 2:

        if current_girl.orgasm >= 4:

            $ afternight04_condom_broken = True #Didac gives you a broken Condom. After that you can´t take "dick_out" or "dick_low" her pussy.

            # BROKEN CONDOM SCENE.

            show afternight04_sexbattle_effects black
            hide screen premium_dashboard
            with fade

            p "¡¿Qué haces?!"

            show afternight04_sexbattle_background_a
            show morning04_bedroom_Didac_body_ass 02c
            show morning04_bedroom_Didac_body_body 02c
            show morning04_bedroom_Didac_exp_mouth happy_Silentx02:
                morning04_bedroom_exp_position
            show morning04_bedroom_Didac_exp_eyes 04:
                morning04_bedroom_exp_position
            show morning04_bedroom_Didac_exp_eyepupils front_04:
                morning04_bedroom_exp_position
            show morning04_bedroom_Didac_exp_eyebrows angryx01:
                morning04_bedroom_exp_position
            show morning04_bedroom_Didac_body_hair 02c
            with fade

            n "Con un rápido movimiento,"

            show morning04_bedroom_Didac_exp_mouth happy_Silentx02
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            n "el rostro de Dídac se acerca tanto a ti, que apenas te permite ver nada más."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx01
            show morning04_bedroom_Didac_exp_eyebrows normal
            with dissolve

            d "No te preocupes,"

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "ya te pongo yo misma el último condón..."

            show morning04_bedroom_Didac_exp_mouth sad_Silentx01
            show morning04_bedroom_Didac_exp_eyebrows surprisex01
            with dissolve

            p "¿Por qué?"

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "Por que sí."

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "Has conseguido que me corra [current_girl.orgasm] veces antes de llegar a usar este..."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "Creo que te mereces una recompensa..."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows sadx01
            with dissolve

            d "Aunque ahora esta polla no va a salir de aquí dentro de ninguna puta manera;"

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx01
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "O antes de que seas capaz de sacarla,"

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows angryx04
            with dissolve

            d "retorceré tanto mi cadera que acabarás teniendo que llevarla al hospital."

            show morning04_bedroom_Didac_exp_mouth happy_Silentx05
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            pt "Como si pudiera ir al hospital sin mi polla..."

            show morning04_bedroom_Didac_exp_mouth happy_Silentx06
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            pt "Mejor no me pongo a imaginar de lo que sería capaz..."

            hide afternight04_sexbattle_background_a
            hide morning04_bedroom_Didac_body_ass
            hide morning04_bedroom_Didac_body_body
            hide morning04_bedroom_Didac_exp_mouth
            hide morning04_bedroom_Didac_exp_eyes
            hide morning04_bedroom_Didac_exp_eyepupils
            hide morning04_bedroom_Didac_exp_eyebrows
            hide morning04_bedroom_Didac_body_hair
            with fade



            if afternight04_condom_broken == True:

                if (afternight04_Pussy_dick_deep_Speed_0_Rape_Done == 1 or afternight04_Pussy_dick_deep_Speed_0_Done == 1):

                    $ mc_body.store["dick"] = "Pussy_dick_deep"

                else:

                    $ mc_body.store["dick"] = "Pussy_dick_med"

                $ mc_body.dick_speed = 0

            show afternight04_sexbattle_effects empty
            if PlatinumHelp:
                show screen premium_dashboard()

            $ current_pose.id = "pose_1"
            $ current_pose = pose_1
            call afternight04_sexbattle_scene_pose01
            call afternight04_Pussy_dick_general_image
            # NOT FINISHED change pose
            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve
            with Dissolve (3.0)

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿{i}Capisci{/i}?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "¿Ahora me habla en plan {i}mafia siciliana{/i}?"

        else:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Aquí tienes el último condón."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Repito,"

            extend " el último."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            $ mc_body.store["dick"] = "Pussy_dick_out"
            $ mc_body.dick_speed = 0

            $ current_pose.id = "pose_1"
            $ current_pose = pose_1
            call afternight04_sexbattle_scene_pose01
            # NOT FINISHED change pose
            with Dissolve (3.0)

    if mc_body.orgasm == 3:

        if current_girl.orgasm <= 1:

            scene hit_15
            pause 0.05
            scene hit_16
            pause 0.05
            scene hit_17
            pause 0.05
            scene hit_21
            pause 0.05
            scene black
            with hpunch

            p "¡¡AAAUUUCH!!"

            n "Con un rápido movimiento y debido en parte a tu ausencia absoluta de coordinación y fuerza por tu tercer orgasmo,"

            n "El pie de Dídac consigue propinarte un fuerte golpe en tus testículos que te deja plano en el suelo."

            scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
                transform_anchor True
                xalign 0.5 yalign 0.5
                zoom 1.0 xpos -0.5 ypos -1.0
            show morning04_bedroom_DMast_blinkeye
            with fade

            p "¡Coño...!"

            if afternight04_CumOnStomach == 2:

                $pl.ch_pts("dp", -1)

                scene hit_22
                pause 0.05
                scene hit_23
                pause 0.05
                scene hit_24
                pause 0.05
                scene black
                with hpunch

                p "¡¡OUUCH!!"

                n "Sin poder reaccionar, recibes una segunda patada."

                p "¡Dídac!"

                d "¡Esto por tu segunda corrida en mi estómago!"

                # She smashes Harder

            elif afternight04_CumOnStomach == 3:

                $pl.ch_pts("dp", -1)

                scene hit_01
                pause 0.05
                scene hit_02
                pause 0.05
                scene hit_07
                pause 0.05
                scene hit_08
                pause 0.05
                scene hit_09
                pause 0.05
                scene hit_10
                pause 0.05
                scene hit_06
                pause 0.05
                scene black
                with hpunch

                p "¡¡AAUUU!!"

                d "¡Y ESTO POR TU TERCERA!"

                p "¡Ya basta!"

                p "¡¿No crees?!"

            scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
                transform_anchor True
                xalign 0.5 yalign 0.5
                zoom 1.0 xpos -0.5 ypos -1.0  
            show morning04_bedroom_DMast_blinkeye
            with fade

            d "¡Debería darte de patadas hasta dejarte eunuco del todo!"

            d "Eres un puto imbécil [protname]."

            d "Te pedí un favor;"

            d "y así es como me lo pagas..."

            n "Su voz es temblorosa y contiene una gran dosis de ira contenida."

            n "Oyes sus pasos alejándose a lo que parece ser el baño mientras te retuerces de dolor en el suelo incapaz de moverte."

            n "Poco después el tintineo de las llaves y acto seguido un estruendo portazo que lleva fuera del piso."

            p "La madre que te parió..."

            scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
                transform_anchor True
                xalign 0.5 yalign 0.5
                zoom 1.0 xpos -0.5 ypos -1.0
                easein_quad 50.0 zoom 0.2 xpos 0.5 ypos 0.5
            with fade

            n "Pasados unos minutos consigues recuperar a duras penas la compostura y en el completo silencio del piso te pones en pie."

            p "¿A dónde coño habrá ido?"

            p "Está como una puta cabra..."

            p "A estas alturas a saber dónde estará..."

            p "en realidad;"

            p "¡¿Qué coño me importa?!"

            p "He intentado ayudarle;"

            p "¡y así es como me lo ha agradecido!"

            $ saturation_tint_level = "superdark"

            p "¡Pues que le folle un pez!"

            scene morning04_bg_kitch_toastwithjam
            with fade

            n "Aún con cierta dificultad, logras llegar a la nevera para intentar saciar el hambre que sufre tu estómago."

            scene afternight03_bg shower
            with fade

            n "Poco después te tomas una ducha,"

            scene beds_night_lightOff_blindDown_DemptyMCempty
            with fade

            n "y finalmente decides ir a la cama a esperar un nuevo día."

            scene beds_night_lightOff_blindDown_DemptyMCbusy
            with dissolve

            $pl.ch_pts("dp", -5) #She Had -1 orgasms. (She´s Out of the flat)

            jump morning05

        else:

            "This TEXT should not be visible 9987 ### current_girl.orgasm >= 2: These content is already done in theory."

    if afternight04_condom_broken == False:

        $ mc_body.store["dick"] = "Pussy_dick_out"
        $ mc_body.dick_speed = 0
        call afternight04_Pussy_dick_general_image

    $ afternight04_mc_orgasms += 1

    return


######################################################
#####################################################
####################################################
###################################################

label afternight04_dick_orgasm_condom_broken:

    scene black
    hide screen premium_dashboard
    with fade

    scene afternight04_sexbattle_background_a
    show morning04_bedroom_Didac_body_ass 02c:
        zoom .89
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.50
        easein_quad 1.0 xpos .52 ypos .54 zoom 1.08
        easeout_quad 3.0 xpos 0.49 ypos 0.5 zoom .89
        easein_quad 1.0 xpos .55 ypos .54 zoom 1.05
        easeout_quad 3.0 xpos .50 ypos .50 zoom .89
        repeat
    show morning04_bedroom_Didac_body_body 02c
    show morning04_bedroom_Didac_exp_mouth happy_Silentx02:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows angryx01:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c
    with fade

    n "El rostro de Dídac se acerca a escasos centímetro de tu rostro."

    show morning04_bedroom_Didac_exp_mouth happy_Silentx03
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    pt "¡¿Qué narices hace?!"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows surprisex01
    with dissolve

    d "Tengo que felicitarte [protname],"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    d "Te has comportado como un verdadero hombre hasta el final..."

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    d "Sé muy bien que tu límite siempre han sido tres orgasmos"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows sadx02
    with dissolve

    d "y estás al final de tus fuerzas..."

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx01
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    d "Pero no me voy a quejar,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "has conseguido que me corra [current_girl.orgasm] veces antes de terminar..."

    if afternight04_condom_on == False:

        show morning04_bedroom_Didac_body_ass 02c:
            zoom .89
            xanchor 0.5
            xpos 0.5
            yanchor 0.5
            ypos 0.50
            easein_quad 0.2 xpos .52 ypos .54 zoom 1.08
            easeout_quad 1.0 xpos 0.49 ypos 0.5 zoom .89
            easein_quad 0.2 xpos .55 ypos .54 zoom 1.05
            easeout_quad 1.0 xpos .50 ypos .50 zoom .89
            repeat
        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows sadx02
        with dissolve

        n "Sin darte tiempo a responder, vuelve a mover sus caderas de forma frenética violando tu notablemente sensible polla."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx05
        show morning04_bedroom_Didac_exp_eyebrows sadx03
        with dissolve

        n "Causando que tu corrida terminé ocurriendo en su interior."

        scene black
        with hpunch

        pause 0.5

        show afternight04_sexbattle_effects white_cumming
        with dissolve

        p "Aaaaaghh..."

        show afternight04_sexbattle_effects black
        with Dissolve (2.0)

        d "Hmmm..."

        pt "Coño..."

        pt "que puta corrida..."

        pt "Es curioso,"

        pt "la sensación ha sido completamente distinta a las otras dos..."

    n "Sientes como con cierta delicadeza va alzando sus caderas hasta sacarse tu polla de su interior,"

    n "mientras con suave sutileza sus dedos van quitándote el condón."

    p "Dídac,"

    extend " ¿Qué ha...?"

    scene afternight04_sexbattle_background_a
    show morning04_bedroom_Didac_body_ass 02c
    show morning04_bedroom_Didac_body_body 02c
    show morning04_bedroom_Didac_exp_mouth sad_Talkingx001:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows angryx01:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c
    with fade

    d "Shhhh..."

    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx03
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    n "Con una expresión pícara te silencia sus labios con el índice de la otra mano."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    d "Con tu permiso,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    d "voy a quedarme este último condón como recuerdo..."

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
    show morning04_bedroom_Didac_exp_eyebrows normal
    with dissolve

    p "¿Qué...?"

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx02
    show morning04_bedroom_Didac_exp_eyebrows sadx03
    with dissolve

    p "¿¿Por qué??"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows sadx02
    with dissolve


    d "Descansa un poco mientras me tomo una ducha yo primera..."

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve


    p "Pero..."

    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows sadx02
    with dissolve

    p "Oye..."

    scene black
    with hpunch

    show kiss_ f_d_12:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 1.2
    with dissolve
    pause 0.5
    show kiss_ f_d_10
    with dissolve
    pause 0.5
    show kiss_ f_d_08
    with dissolve
    pause 0.5
    show kiss_ f_d_07
    with Dissolve(1.0)

    n "En el justo momento en que sientes que te ha sacado completamente el condón e intentas reaccionar,"

    show kiss_ f_d_04
    with dissolve
    pause 0.5
    show kiss_ f_d_05
    with dissolve
    pause 0.5
    show kiss_ f_d_02
    with dissolve
    pause 0.5
    show kiss_ f_d_01
    with dissolve
    pause 0.5
    show kiss_ f_d_07
    with Dissolve(1.0)

    n "sus labios se funden con los tuyos en un cálido beso que te descoloca completamente."

    scene afternight04_sexbattle_background_a
    show morning04_bedroom_Didac_body_ass 02c
    show morning04_bedroom_Didac_body_body 02c
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows sadx02:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c
    with fade

    d "Buenas noches [protname]."

    scene afternight04_sexbattle_background a
    with vpunch

    n "Como si de un rayo se tratara, se aparta a toda velocidad de ti dejándote con la polla desnuda tirado en el sofá."

    p "..."

    pt "Pero..."

    pt "¡¿Pero qué coño...?!"

    pt "¿A qué diablos ha venido eso?"

    pt "¡¿Y por qué demonios no me he podido quitar el último condón hasta que me lo ha quitado él mismo hasta el final?!"

    p "..."

    pt "Desde luego,"

    pt "cada día está peor..."

    p "..."

    pt "Aunque el hecho de que haya aceptado follar con él,"

    pt "tampoco dice mucho de mí..."

    scene afternight04_sexbattle_background a
    with hpunch

    ono "BBBRRRRRRRR..."

    p "..."

    pt "Desde luego mi estómago no es nada sutil..."

    pt "Aprovecharé para comer algo mientras él se ducha,"

    pt "Aunque también podríamos habernos duchado juntos..."

    p "..."

    pt "¿Sería demasiado raro...?"

    p "..."

    pt "Ya no sé qué pensar de toda esta situación..."

    ##

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    scene morning04_bg_kitch_toastwithjam
    with fade

    n "A esas alturas de la noche, tomas la decisión de que lo más sabio es tomar algo en frío de la nevera para engañar a tu estómago."

    n "Efectivamente, en el tiempo de haberte tomado algo de comer,"

    scene beds_night_lightOff_blindUp_DemptyMCempty
    show beds_D03b_night_lightOff_blindUp
    with fade

    n "Dídac ya había terminado de ducharse y estaba ya en la cama descansando plácidamente."

    show afternight03_bg_shower
    with fade

    n "Como te ha sugerido, haces lo mismo;"

    scene beds_night_lightOff_blindUp_DemptyMCempty
    show beds_D03b_night_lightOff_blindUp
    with fade

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    show beds_D03b_night_lightOff_blindUp
    with dissolve

    n "y poco después te vuelves a reunir con {i}Morpheo{/i}."

    #$pl.ch_pts("dp", 10) #She Had +4 orgasms. (Not Pregnant) #Just to take in mind

    $pl.ch_pts("dp", 15) #She Had +4 orgasms. (She´s Pregnant)

    $ DidacMCPregnant = True # Didac is pregnant by the Main Character.
    $ DidacPregnant = True # Didac is Pregnant.

    jump morning05









