
default afternight04_dick_general_Speed_3_Cond = False

################################################
###############################################
##############################################
############################################# DICK PUSSY (WORK IN PROGRESS!!!!)

label afternight04_Pussy_dick_general_dialogue:

    #aj "Work in progress"

    #return

    
#label afternight04_Pussy_dick_rape_general_dialogue: # THE one used as reference.

        ####################
        ####################
        ####################

        ####################      
        ####################
        #################### DEEP

####################
    ####################
        #################### DEEP 3

    if (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 3): ##### DEEP 3
        $ debug ("Dick deep speed 3 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_deep_Speed_3_Done += 1

        if mc_body.roll_success == False: #Huge pain.
            $ afternight04_Pussy_dick_deep_Speed_3_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_deep_Speed_3_Success += 1

                #HER REACTION: PUSSY DEEP 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_3
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "{size=60}¡¡¡¡AAAAAUUUUUUHH!!!!{/size}"

            elif randomnum_1to5 == 2:

                d "{size=60}¡¡¡¡OOOOOOUUUUUCH!!!!{/size}"

            elif randomnum_1to5 == 3:

                d "{size=60}¡¡¡¡AAAAAIIUUUCHH!!!!!{/size}"

            elif randomnum_1to5 == 4:

                d "{size=60}¡¡¡¡IIIIAAAAAAAUUUUUUH!!!!{/size}"

            elif randomnum_1to5 == 5:

                d "{size=60}¡¡¡¡AAAAAAUUUUUUHH!!!!{/size}"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx10_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

    ## Success Reactions



        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            if afternight04_Pussy_dick_deep_Speed_3_Done == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_3
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "{size=32}¡¡HOSTIAS!!{/size}"

                elif randomnum_1to5 == 2:

                    d "{size=32}¡¡LA MADRE QUE TE PARIÓ!!{/size}"

                elif randomnum_1to5 == 3:

                    d "{size=32}¡¡COÑOOO!!{/size}"

                elif randomnum_1to5 == 4:

                    d "{size=32}¡¡COo-JOOo-NEess...!!{/size}"

                elif randomnum_1to5 == 5:

                    d "{size=30}¡¡ME VAS A REVENTAR!!{/size}"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils up02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "{size=32}¡¡JOODEER!!{/size}"

                elif randomnum_1to5 == 2:

                    d "{size=32}¡¡HOSTIAAA PUTA!{/size}"

                elif randomnum_1to5 == 3:

                    d "{size=32}¡¡LA CONCHA DE TU MADRE!!{/size}"

                elif randomnum_1to5 == 4:

                    d "{size=32}¡¡JODER CON EL POLLÓN!!{/size}"

                elif randomnum_1to5 == 5:

                    d "{size=32}¡¡DIOO-OOO-OSS!!{/size}"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                # PAIN # DEEP 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            call afternight04_Pussy_dick_general_pain

            ############################################################
            ###########################################################


                # DESCRIPTION: PUSSY DEEP 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == True:

            if afternight04_condom_broken == False:

                if afternight04_Pussy_dick_deep_Speed_3_Success == 1:

                    n "No solo tus embestidas son muchísimo más dinámicas,"

                    n "sino que además la fuerza con la que arremetes es mucho más violenta y despiadada."

                    n "El glande de tu polla no solo alcanza fácilmente su muro vaginal,"

                    n "sino que además tienes la sensación que puede abrirse camino a través de su cérvix."

                elif afternight04_Pussy_dick_deep_Speed_3_Success == 2:

                    n "Chocas contra sus nalgas sin ninguna compasión mientras ves desaparecer tu polla completamente en su interior."

                    n "El fuerte y constante choque contra su cérvix,"

                    n "le dibuja una expresión entre dolor y placer difícil de describir."

                elif afternight04_Pussy_dick_deep_Speed_3_Success == 3:

                    n "En cada fuerte y rápida zancada, sientes como tu glande pretende abrirse camino a través de su cuello uterino,"

                    n "forzando un camino por el cual se supone que solo debe de ser abierto para extraer una nueva vida."

                    n "No un pollón del tamaño de un embrión."


                elif afternight04_Pussy_dick_deep_Speed_3_Success == 4:

                    n "En su deleite desmesurado por la ruda y presurosa forma de follarla,"

                    n "consigues embestida tras embestida,"

                    n "ir abriéndole paso a través del prohibido cuello uterino"

                    n "a tu monstruoso miembro viril."

            else:

                call afternight04_Pussy_dick_condom_broken

                # HER DIALOGUES: PUSSY DEEP 3
            ############################################################
            ###########################################################

    ## Sexual REACTIONS # FAILED

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_deep_Speed_3_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¡HIJO DE PUTA!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡ME VAS A PARTIR EN DOS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿ES QUE TE HAS BEBIDO EL PUTO JODIDO CEREBRO?!"

                if afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "¡No me vengas con hostias Dídac!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡Cuando me estuviste violando de esta forma yo no me quejé tanto!"

                elif afternight04_Pussy_dick_deep_Speed_3_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Cuando te he estado follando antes así no te me has quejado..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Ufff..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Bueno,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "eres tú quien me está pidiendo ayuda..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿QUIERES QUE VAYA A BUSCAR UN PEPINO Y TE LO METO POR EL CULO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡A VER SI TE HACE TANTA GRACIA!"

                if afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "Si te violo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Soy yo quien controla el jodido ritmo!"

                elif afternight04_Pussy_dick_deep_Speed_3_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Que no me quejara no significa que no me doliera!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "Ya..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Te he pedido ayuda para que me follaras!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡No hace falta que me la metas entera!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Qué es lo que no entiendes?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Que tú puedes pedirme el favor de hacerte un favor,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "pero luego me echas encara que intente ayudarte haciendo lo que me has pedido."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Te he pedido que me folles."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡NO QUE ME DIVIDAS EN DOS!!"

                if afternight04_Pussy_dick_deep_Speed_3_Success > 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Textualmente me has dicho que no parase..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡PERO CON CUIDADO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¡Eso es como pedirle a un leñador que corte un árbol con cuidado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡¿Quieres que lo haga con una pluma?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡No soy un jodido árbol!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "Tsssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkginx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Si quieres ya me has entendido!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "Creo que no te entiendes ni tú mismo."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡JODER!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

            elif afternight04_Pussy_dick_deep_Speed_3_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡LA MADRE QUE TE PARIÓ!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡¿ERES CONSCIENTE DE QUE ME ESTÁS DESTROZANDO POR DENTRO?!!"

                if afternight04_Pussy_dick_deep_Speed_3_Success > 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Pero si me has dicho que no parase!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "Además..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "No he visto que sangres..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿¿ES QUE ME QUIERES HACER SANGRAR??!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Dicho así suena realmente mal..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡JODER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡TEN UN POCO MÁS DE CUIDADO COÑO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                if afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0:

                    pt "¡Como si ella lo hubiera tenido conmigo cuando me estaba violando!"

            elif afternight04_Pussy_dick_deep_Speed_3_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¡JOOODEEEEER!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿¿DE QUÉ COJONES VAS?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿QUÉ COÑO TE HE DICHO YA POR TERCERA PUTA VEZ?!!"

                if afternight04_Pussy_dick_deep_Speed_3_Success > 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx09_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "¡Joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡Pero si textualmente me has dicho que no pare de follarte de esta manera hace nada!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Voy cachonda [protname]."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡¿Y?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¡Que no sé lo que me digo!!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "¡Joder Dídac!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils left04_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "¡Que no es una jodida enfermedad ni un estado etílico tan grave!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils left05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "No tienes ni puta idea de lo que es..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "..."

                    pt "Empieza a preocuparme..."

                elif afternight04_Pussy_dick_deep_Speed_3_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¡Pero ha habido alguna vez que no te ha disgustado tanto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿ESA ES TU JODIDA EXCUSA?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "¡Intenta calentarme un poco antes!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Llevas toda la noche diciéndome lo contrario..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡POR QUE NO PENSABA QUE ME IBAS A FOLLAR COMO UN PUTO CABALLO EN CELO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Que duele un montón!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Hostias!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡JODER!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡SE UN POCO MÁS DELICADO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡BAJA EL RITMO COÑO!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx08_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

            elif afternight04_Pussy_dick_deep_Speed_3_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¡COOOÑOOOO!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡TE LO DIGO EN SERIO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡COMO VUELVAS A METERME LA VERGA ENTERA DE ESTA MANERA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡TE VOY A METER UN PUTO SOPAPO EN TODA LA PUTA CARA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿ME EXPLICO?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_3_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡JODEER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡TE LA ESTÁS JUGANDO [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_3_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

    ## Sexual REACTIONS # SUCCESS

        if mc_body.roll_success == True:

            if afternight04_Pussy_dick_deep_Speed_3_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils up02_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "¡¡DIOO-OOO-OSS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡¡ME VAS A..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils up02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "A PARTIR..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "EN DOOOoS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "UUUfff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "¡Mierda...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "¡¡SE LA ESTOY METIENDO ENTERA A TODA LECHE!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                pt "¡Madre mía...!"

                if afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "¡Ni cuando lo tenía encima violándome la sentía tan apretada!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "UUUFFFFFF..."

                if afternight04_Pussy_dick_deep_Speed_3_Failed > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡Por lo menos esta vez no te quejas tanto como las otras veces!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡ME DUELE UN HUEVO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡PERO TAMBIÉN ME ENCANTA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                pt "Me voy a quedar sin circulación en las caderas..."

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡¡DIOOOOSSS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡QUE BRUTO ERES JODER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils up00_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡APENAS ME SIENTO LAS JODIDAS PIERNAS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                if afternight04_Pussy_dick_deep_Speed_3_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "Bien que las movías cuando me hacías lo mismo,"

                    pt "so cabrón hipócrita..."

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡¡COÑOOO!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡¿TIENES QUE FOLLARME ASÍ?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                d "¡¡A MENOS VELOCIDAD,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils up02_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "O METIÉNDOME MENOS POLLA,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "TAMBIÉN DISFRUTARÍA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡¿SABES?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils up00_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡¡JOODEEEER!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Dios!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡QUE PUTO POLLÓN COÑO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡ME VOY A PASAR UNA SEMANA SIN PODER CAMINAR!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¿Da por hecho que se va a quedar así más de una semana?"

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡ME CAGO EN TODO LO QUE SE MENEA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡MALDITA JODIDA ANACONDA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡QUE PUTO DAÑO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¡¿Qué?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡QUE NO PARES COÑO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡SSSIIIHHH!!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡DIOS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡ME ESTÁS REVENTANDO EL ESTÓMAGO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡PERO NO PARES JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡JODEEEEEER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡¿POR QUÉ COÑO ME PONE TAN CALIENTE?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡SI ME ESTÁS DESTROZANDO EL COÑO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "No es que quiera..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Pero sí me resulta extraño que no le salga sangre..."

                pt "No suelo follarme en la primera cita a ninguna mujer de esta manera..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¡Pero que cojones!"

                pt "¡Es el coño más estrecho que me he follado en mi vida!"

                pt "¡Y lo jodido no es solo que me está volviendo loco...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "¡SINO QUE ES DÍDAC!"

                pt "¡¡JODER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¡PERO HOSTIAS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                pt "¡QUE COÑO!"

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 8:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils up00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡JODER JODER JODER JODER JODER JODER!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡COMO ME ESTÁS PONIENDO MALDITO CABRÓN!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡NI SE TE OCURRA PARAR!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¡REVIÉNTAME TODA!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_3_Success == 9:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡NO PARES!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡POR LO QUE MÁS QUIERAS!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_3_Success >= 10:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                # SLOW DOWN DICK: DEEP 3
            ############################################################
            ###########################################################

            call afternight04_Pussy_dick_general_slowdown

####################
    ####################
        #################### DEEP 2

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 2): ##### DEEP 2
        $ debug ("Dick deep speed 2 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_deep_Speed_2_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_deep_Speed_2_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_deep_Speed_2_Success += 1

                #HER REACTION: PUSSY DEEP 2
            ############################################################
            ###########################################################

        if mc_body.roll_success == False: 

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_2
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "{size=27}¡¡¡AAAUUUUHH!!!{/size}"

            elif randomnum_1to5 == 2:

                d "{size=27}¡¡¡OOOOUUUUCH!!!{/size}"

            elif randomnum_1to5 == 3:

                d "{size=27}¡¡¡AAAAIIUUUCHH!!!!{/size}"

            elif randomnum_1to5 == 4:

                d "{size=27}¡¡¡IIAAAAUUUUUUH!!!{/size}"

            elif randomnum_1to5 == 5:

                d "{size=27}¡¡¡AAAUUUUHH!!!{/size}"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx09_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            if afternight04_Pussy_dick_deep_Speed_2_Done == 1:

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_2
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡¡MADRE MÍA!!"

                elif randomnum_1to5 == 2:

                    d "¡¡ME ESTÁS REVENTANDO POR DENTRO!!"

                elif randomnum_1to5 == 3:

                    d "¡¡COÑO!!"

                elif randomnum_1to5 == 4:

                    d "¡¡QUE PUTO POLLÓN!!"

                elif randomnum_1to5 == 5:

                    d "¡¡COJONES!!"

            else:

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_2
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡¡JODER!!"

                elif randomnum_1to5 == 2:

                    d "¡¡HOSTIAA!!"

                elif randomnum_1to5 == 3:

                    d "¡¡LA CONCHA DE TU MADRE!!"

                elif randomnum_1to5 == 4:

                    d "¡¡JODER CON EL POLLÓN!!"

                elif randomnum_1to5 == 5:

                    d "¡¡DIOOS...!!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

                # PAIN # DEEP 2
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            call afternight04_Pussy_dick_general_pain

            ############################################################
            ###########################################################


                # DESCRIPTION: PUSSY DEEP 2
            ############################################################
            ###########################################################

        if mc_body.roll_success == True:

            if afternight04_condom_broken == False:

                if afternight04_Pussy_dick_deep_Speed_2_Success == 1:

                    n "El movimiento de tus caderas ya no es nada sutil,"

                    n "tus embestidas son cada vez más pronunciadas y el choque contra su muro vaginal es más pronunciado,"

                    n "dando al glande un mayor placer."

                elif afternight04_Pussy_dick_deep_Speed_2_Success == 2:

                    n "Sientes sus nalgas empotrándose sobre tu entrepierna en cada embestida,"

                    n "logrando hundir tu polla hasta el fondo de ella."

                    n "Su expresión es una mezcla de dolor y placer."

                    n "Sientes tu polla ahogada en su interior por la presión de su pared vaginal,"

                    n "pero al mismo tiempo un gozo enorme."

                elif afternight04_Pussy_dick_deep_Speed_2_Success == 3:

                    n "La sensación de llegar hasta el fondo y notar como eso le produce una mezcla de placer y suplicio,"

                    n "hace que tu polla se ponga a palpitar con más energía, lo cual no te facilita la labor de retardar el orgasmo."

            else:

                call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY DEEP 2
            ############################################################
            ###########################################################

    ## Sexual REACTIONS # FAILED

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_deep_Speed_2_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡COÑO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿PERO NO VES EL PEDAZO DE POLLÓN QUE TIENES?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "Pero si..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡CÁLMATE UN POCO COÑO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡A duras penas entiendo cómo coño me la has llegado a meter entera"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "y ya empiezas a violarme a esa velocidad!"

                if afternight04_Pussy_dick_deep_Speed_2_Success > 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Pero si has sido tú quien me lo ha pedido!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Que yo te violo?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¡Serás hipócrita!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 045_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                d "..."

                if afternight04_Pussy_dick_deep_Speed_2_Success > 4:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Solo te pido que seas un poco más delicado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "¡Joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿No tienes suficiente con metérmela entera?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Como se nota que no eres tú el que recibe la polla!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Eres un puto bestia egoísta de mierda!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Repíteme eso si tienes cojones"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows surprisex02_a
                        with dissolve

                    p "y te dejo a dos velas ahora mismo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Vale..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Lo siento,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "me he pasado..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡Pero es que me has hecho daño coño!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Intenta ponerte en mi lugar!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Leches!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_2_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡ME CAGO EN LA HOSTIA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡TE HE DICHO QUE ME DUELE UN COJÓN Y MEDIO A ESTA VELOCIDAD!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿PERO TÚ ME OYES?!"

                if afternight04_Pussy_dick_deep_Speed_3_Done > 0:

                    if afternight04_Pussy_dick_deep_Speed_3_Success > 0:
                        
                        if afternight04_Pussy_dick_deep_Speed_3_Success > 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx01_a
                                with dissolve

                            p "Pero si ya te la he metido más rápido y no me has dicho nada..."

                            if afternight04_Pussy_dick_deep_Speed_3_Failed > afternight04_Pussy_dick_deep_Speed_3_Success:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                    show afternight04_sexbattle_d_eyes 03_a
                                    show afternight04_sexbattle_d_pupils front03_a
                                    show afternight04_sexbattle_d_eyebrows angryx04_a
                                    with dissolve

                                d "¡¿Cómo que no te he dicho nada?!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx05_a
                                    with dissolve

                                d "¡La madre que te parió!"

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                            else:

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils front05_a
                                    show afternight04_sexbattle_d_eyebrows angryx03_a
                                    with dissolve

                                d "..."

                                if current_pose.id == "pose_1":
                                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                                    show afternight04_sexbattle_d_eyes 05_a
                                    show afternight04_sexbattle_d_pupils right05_a
                                    show afternight04_sexbattle_d_eyebrows sadx02_a
                                    with dissolve

                        elif afternight04_Pussy_dick_deep_Speed_3_Success == 0:

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                                show afternight04_sexbattle_d_eyes 01_a
                                show afternight04_sexbattle_d_pupils front01_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            "¡QUE ENCIMA HABÍAS INTENTADO SUBIR MÁS EL RITMO!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                                show afternight04_sexbattle_d_eyes 03_a
                                show afternight04_sexbattle_d_pupils front03_a
                                show afternight04_sexbattle_d_eyebrows angryx05_a
                                with dissolve

                            "¡¿TE CREES QUE MI COÑO ES UNA BATIDORA?!"

                            if current_pose.id == "pose_1":
                                show afternight04_sexbattle_d_mouth sad_Silentx07_a
                                show afternight04_sexbattle_d_eyes 05_a
                                show afternight04_sexbattle_d_pupils front05_a
                                show afternight04_sexbattle_d_eyebrows angryx04_a
                                with dissolve

                elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Pero si tú ya me has violado a esta velocidad metiéndote la polla entera hasta el fondo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "¡¿Qué mierdas me estás contando ahora?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "¡Pero era yo quien controlaba el ritmo!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "¡Te tenía que doler igual!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils left05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    d "..."

                elif afternight04_Pussy_dick_deep_Speed_2_Success > 0:

                    if afternight04_Pussy_dick_deep_Speed_2_Success == 1:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve

                        p "Pero si antes te he dado al mismo ritmo"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 02_a
                            show afternight04_sexbattle_d_pupils right02_a
                            show afternight04_sexbattle_d_eyebrows silent_a
                            with dissolve

                        p "y no me has dicho nada..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                            show afternight04_sexbattle_d_eyes 01_a
                            show afternight04_sexbattle_d_pupils front01_a
                            show afternight04_sexbattle_d_eyebrows angryx01_a
                            with dissolve
                        
                        p "¡Si ya te la he metido a este ritmo varias veces!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils right03_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        p "¡y no te me has quejado tanto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pues te lo digo ahora!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Me estás haciendo daño!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Coño!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Tsskk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_2_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¡¿QUE COÑO NO ENTIENDES DE ME ESTÁS HACIENDO DAÑO?!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "Creí que querías que te violara sin contemplaciones durante toda la noche..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Entiendes la jodida diferencia entre \"violar\"y \"desgarrar\"?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "¿Él se escucha?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Me está empezando a hacer daño de verdad!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Hombre,"

                pt "un poco de razón tiene..."

            elif afternight04_Pussy_dick_deep_Speed_2_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡ME CAGO EN LA HOSTIA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡[protname]!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡A ESTE RITMO ME VAS A DEJAR INVÁLIDA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Me estás empezando a cabrear..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_2_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

    ## Sexual REACTIONS # SUCCESS

        if mc_body.roll_success == True:

            if afternight04_Pussy_dick_deep_Speed_2_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡AAAA-aaaa-hhh...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡CON MÁS CALMA JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "¡AL FINAL"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "ME REVENTARÁS ALGO AHÍ DENTRO!"

                if afternight04_Pussy_dick_deep_Speed_1_Success > 5:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Eres tú quien me ha pedido que te folle más duro."

                elif afternight04_Pussy_dick_deep_Speed_2_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "No me seas hipócrita,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Tú mismo me estabas violando así hace no mucho rato..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Y lo que te gusta..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Me haces daño joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Quieres que pare?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Solo te pido que seas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Uff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Algo más delicado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "La verdad es que estoy perdiendo la sensibilidad de mi polla por momentos,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                pt "no solo es estrecho,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "encima parece que me la quiera ahogar..."

            elif afternight04_Pussy_dick_deep_Speed_2_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡ME CAGO EN DIOS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿ME LA QUIERES METER HASTA EL ESÓFAGO?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡NNnghh!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils up02_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "¡Me estás revolviendo toda por dentro!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "Y aún así no me pide que pare..."

            elif afternight04_Pussy_dick_deep_Speed_2_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils down02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡JO-ooo-deer...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡Te pedí que me follaras!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "¿Y qué estoy haciendo?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Uff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Me estás destrozando!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_2_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils up01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Hoo-oosti-aaas!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Me vas a dejar estéril!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "¿Planeas quedarte embarazada?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Y lo que te está gustando..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Imbécil!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                pt "Encima..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_2_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Uughh..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "{size=15}Viólame...{/size}"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "¿Qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Uuugh..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Ya me has oído imbécil!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Sí,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "pero me gusta oírtelo decir."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Tsskk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Uff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "¡Idiota!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_2_Success == 6:
                
                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡HHHMMMmm...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Fóllame más duro."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "¿Pero no me has dicho...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡REVIÉNTAME!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                if afternight04_Pussy_dick_deep_Speed_2_Failed > 0:

                    pt "Eso dices ahora,"

                    pt "pero bien que te has quejado ya [afternight04_Pussy_dick_deep_Speed_2_Failed] veces..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve


            elif afternight04_Pussy_dick_deep_Speed_2_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡UUUFFHHMM...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils up00_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "¡REVIÉNTAME [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_2_Success >= 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

####################
    ####################
        #################### DEEP 1

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 1): ##### DEEP 1
        $ debug ("Dick deep speed 1 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_deep_Speed_1_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_deep_Speed_1_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_deep_Speed_1_Success += 1

                #HER REACTION: PUSSY DEEP 1
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_1
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡¡AAUUUUHH!!"

            elif randomnum_1to5 == 2:

                d "¡¡OOOUUCH!!"

            elif randomnum_1to5 == 3:

                d "¡¡AAIIUCHH!!!!!"

            elif randomnum_1to5 == 4:

                d "¡¡IIAAAUUUUUH!!"

            elif randomnum_1to5 == 5:

                d "¡¡AAAUUUHH!!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_deep_Speed_1_Done == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_1
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡¡JOoo-DEEeeer...!!"

                elif randomnum_1to5 == 2:

                    d "¡¡DIii-Oooos...!!"

                elif randomnum_1to5 == 3:

                    d "¡¡LA HOS-TIAAaa...!!"

                elif randomnum_1to5 == 4:

                    d "¡¡COo-JOOo-NEess...!!"

                elif randomnum_1to5 == 5:

                    d "¡¡ME CAa-Goo En Laa HOs-TIAAaa...!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans deep_speed_1
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡Jodeeer...!"

                elif randomnum_1to5 == 2:

                    d "¡Coñooo...!"

                elif randomnum_1to5 == 3:

                    d "¡La Hostia con tu polla...!"

                elif randomnum_1to5 == 4:

                    d "¡JODER CON EL POLLÓN!"

                elif randomnum_1to5 == 5:

                    d "¡Diooos...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                # PAIN # DEEP 1
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            call afternight04_Pussy_dick_general_pain

            ############################################################
            ###########################################################


                # DESCRIPTION: PUSSY DEEP 1
            ############################################################
            ###########################################################

        if mc_body.roll_success == True:

            if afternight04_condom_broken == False:

                if afternight04_Pussy_dick_deep_Speed_1_Success == 1:

                    n "El movimiento de tus caderas es sutil, pero su interior es tan estrecho que sientes tu polla ahogada en su interior."

                    n "En cada oscilación sientes como tu polla topa contra el inicio de su duro y cerrado cérvix."


                elif afternight04_Pussy_dick_deep_Speed_1_Success == 2:

                    n "Tus caderas se desplazan lentamente, pero sientes toda tu polla arropada en su ardiente interior."

                elif afternight04_Pussy_dick_deep_Speed_1_Success == 3:

                    n "El calor de su interior no es nada en comparación a la sensación de tener atrapada toda tu polla en sus ardientes carnes."

                    n "Sientes en cada lenta arremetida el techo de su vagina en tu sensible glande."

            else:

                call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY DEEP 1
            ############################################################
            ###########################################################

    ## Sexual REACTIONS # FAILED

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_deep_Speed_1_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡ME CAGO EN LA HOSTIA!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡[protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Te he dicho que me hace daño joder!"

                if afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Pero si cuanto te me has puesto encima te la has metido entera,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¡y te has movido a esta velocidad!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "¿A qué viene que te quejes ahora?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡Está claro que sé ser más delicada que tú!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                elif afternight04_Pussy_dick_deep_Speed_0_Success > 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "También me has dicho que podría empezar a moverla..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Pues está claro que me he equivocado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Llevas toda la noche diciéndome que te folle violentamente."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿PERO TÚ HAS VISTO EL PEDAZO DE POLLA QUE TIENES?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡VE UN POCO MÁS DESPACIO JODER!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡No puedo ir más despacio!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pues ve con cuidado!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

            elif afternight04_Pussy_dick_deep_Speed_1_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡DIOS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡NO ERES CONSCIETE DEL POLLÓN QUE GASTAS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Verdad?!"

                if afternight04_Pussy_dick_deep_Speed_2_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Antes te la he metido más rápido y no te me has quejado tanto..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Quizás porque has sabido hacerlo mejor..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    pt "¡Pero si lo he hecho igual!"

                elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Cuando me has violado haciendo exactamente lo mismo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "no he visto que te me quejaras tanto."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Por que tú eres un jodido animal!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Sino aprendes a hacerlo bien tendré que hacerlo yo misma!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx031_a
                        with dissolve

                    p "..."

                elif afternight04_Pussy_dick_deep_Speed_1_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Pero antes no te ha dolido..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "¡Pues me ha dolido ahora joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "¡¿Qué es lo que no entiendes?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Si quieta me duele un montón,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿Cómo crees que me va a doler si empiezas a moverte imbécil?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Pues no me vayas diciendo que quieres que te viole como una perra en celo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "porque en realidad eres una muñeca de porcelana."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "Espera que vaya a por \"Michael\","

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "y verás quien es muñeco de porcelana aquí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "Me imagino que se refiere al consolador más grande que se ha comprado..."

            elif afternight04_Pussy_dick_deep_Speed_1_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡PERO ESTÁTE QUIETO COÑO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿NO VES QUE SIN MOVERLA YA ME DUELE UN COJÓN Y MEDIO?!"

                if afternight04_Pussy_dick_deep_Speed_0_Success > 3:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Pero si has sido tú quien me ha pedido que empezara a moverme!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx004_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Voy cachonda!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡¿no lo ves?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡¿Entonces?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Eso no quita que duele un cojón y medio!"

                if afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "No te me has quejado con la misma intensidad cuando eras tú quien se montaba encima..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Pff..."

                if afternight04_Pussy_dick_deep_Speed_2_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Además antes te he follado más duramente y no te me has quejado tanto..."

                elif afternight04_Pussy_dick_deep_Speed_1_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "Además no es la primera vez que me muevo y no te me has quejado tanto antes..."

                    if afternight04_Pussy_dick_deep_Speed_1_Failed > afternight04_Pussy_dick_deep_Speed_1_Success:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡Me he quejado bastantes veces más!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Silentx04_a
                            show afternight04_sexbattle_d_eyes 04_a
                            show afternight04_sexbattle_d_pupils front04_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        p "..."

                    else:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                            show afternight04_sexbattle_d_eyes 05_a
                            show afternight04_sexbattle_d_pupils right05_a
                            show afternight04_sexbattle_d_eyebrows sadx01_a
                            with dissolve

                        d "Tssk..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Solo te pido que vayas un poco más con cuidado."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿Tanto te estoy pidiendo?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "De por si,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "siempre has sido un gilipollas egoísta,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                    with dissolve

                p "pero ahora,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "además eres una jodida ninfómana consentida que no sabe ni lo que quiere."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Te estás ganando una hostia..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¡Y tú que te envíe a la mierda y me vaya a dormir!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Tsskk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_1_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡EN SERIO!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡TE ESTÁS GANANDO UNA HOSTIA [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_1_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

    ## Sexual REACTIONS # SUCCESS

        if mc_body.roll_success == True:

            if afternight04_Pussy_dick_deep_Speed_1_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡Ve despacio coño!"

                if afternight04_Pussy_dick_deep_Speed_1_Failed > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Que antes me has hecho un daño de mil narices!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "No puedo ir más despacio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Ufff..."

                if afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Además,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    p "antes te la metiste tú mismo hasta el fondo y empezaste a moverte."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿Y te crees que no me dolió?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Pero bien que te moviste..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 06_a
                        show afternight04_sexbattle_d_pupils front06_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Me vas a romper el coño con ese pollón!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

            if afternight04_Pussy_dick_deep_Speed_1_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡[protname]...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "¿Siih...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "Si sigues moviéndote así..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Joder..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡Tienes la polla enorme!"

                if afternight04_Pussy_dick_deep_Speed_2_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "También podría volver a ir más rápido..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Ve con calma joder!"

                elif afternight04_Pussy_dick_deep_Speed_1_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Eso ya lo sabes de cuando me has estado violando la polla hasta el fondo jodío..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "Y tú tienes el coño súper estrecho."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Jodeeer..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                pt "La verdad es que se siente exageradamente estrecho"

                pt "y eso no me ayudará a aguantar mucho rato así..."


            elif afternight04_Pussy_dick_deep_Speed_1_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Dios!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡La tienes jodidamente enorme!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Quieres que pare?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Ni en broma!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "Pero ve con cuidado,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "duele un huevo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Tengo la sensación de que me vas a romper por dentro en cualquier momento..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "La verdad es que tu coño es la hostia de estrecho,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "la siento ahogada y succionada al mismo tiempo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "nunca había follado un coño tan musculado y estrecho..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Jodeer..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Me estás destrozando por dentro"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "y mi coño se mueve solo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "Así no voy a durar mucho..."

            elif afternight04_Pussy_dick_deep_Speed_1_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Ufff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Si te estuviera follando yo verías lo que duele..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Pero si eres tú quien me pide que no pare."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Joder!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Porque me estás poniendo a cien cabrón!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Y porque te encanta..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Eres un jodido masoquista del copón"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "y aún no no eres capaz de reconocerlo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Te voy a meter una hostia al final!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_1_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                d "Madre mía..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Aún no me puedo creer que me la hayas metido entera y que puedas moverte..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Y lo que te gusta..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "..."

            elif afternight04_Pussy_dick_deep_Speed_1_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Joder [protname],"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Me parece increíble que te diga esto..."

                if afternight04_Pussy_dick_deep_Speed_2_Success == 0:

                    if afternight04_Pussy_dick_deep_Speed_2_Failed > 0:

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx02_a
                            with dissolve

                        d "Fóllame más fuerte,"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                            show afternight04_sexbattle_d_eyes 03_a
                            show afternight04_sexbattle_d_pupils front03_a
                            show afternight04_sexbattle_d_eyebrows angryx03_a
                            with dissolve

                        d "¡pero por lo que más quieras!"

                        if current_pose.id == "pose_1":
                            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                            show afternight04_sexbattle_d_eyes 06_a
                            show afternight04_sexbattle_d_pupils front06_a
                            show afternight04_sexbattle_d_eyebrows sadx04_a
                            with dissolve

                        d "¡Se más jodidamente delicado que la última vez!"

                elif afternight04_Pussy_dick_deep_Speed_2_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Pero fóllame más fuerte otra vez..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¿Pero a qué coño esperas para follarme más fuerte de una jodida vez?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_1_Success == 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Fóllame [protname]."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_1_Success >= 8:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

    # NOT FINISHED

####################
    ####################
        #################### DEEP 0

    elif (mc_body.store["dick"] == "Pussy_dick_deep" and mc_body.dick_speed == 0): ##### DEEP 0
        $ debug ("Dick deep speed 1 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_deep_Speed_0_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_deep_Speed_0_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_deep_Speed_0_Success += 1

                #HER REACTION: PUSSY MED 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡AAAUUHH!"

            elif randomnum_1to5 == 2:

                d "¡OUuuCH!"

            elif randomnum_1to5 == 3:

                d "¡AAiiuhc!"

            elif randomnum_1to5 == 4:

                d "¡IAAUUH!"

            elif randomnum_1to5 == 5:

                d "¡AAUUHH!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

    ## Success Reactions



        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            if afternight04_Pussy_dick_deep_Speed_0_Done == 1:

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡¡JOoo-DEEeeer...!!"

                elif randomnum_1to5 == 2:

                    d "¡¡DIii-Oooos...!!"

                elif randomnum_1to5 == 3:

                    d "¡¡LA HOS-TIAAaa...!!"

                elif randomnum_1to5 == 4:

                    d "¡¡COo-JOOo-NEess...!!"

                elif randomnum_1to5 == 5:

                    d "¡¡ME CAa-Goo En Laa HOs-TIAAaa...!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                    #if current_pose.id == "pose_1":

                if randomnum_1to5 == 1:

                    d "¡Jodeeer...!"

                elif randomnum_1to5 == 2:

                    d "¡Coñooo...!"

                elif randomnum_1to5 == 3:

                    d "¡La Hostia con tu polla...!"

                elif randomnum_1to5 == 4:

                    d "¡JODER CON EL POLLÓN!"

                elif randomnum_1to5 == 5:

                    d "¡Diooos...!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                # PAIN # DEEP 0
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            call afternight04_Pussy_dick_general_pain

            ############################################################
            ###########################################################


                # DESCRIPTION: PUSSY DEEP 0
            ############################################################
            ###########################################################

        if mc_body.roll_success == True:

            if afternight04_condom_broken == False:

                if afternight04_Pussy_dick_deep_Speed_0_Success == 1:

                    n "Con suma delicadeza, adentras tu miembro viril más allá de lo que habías hecho hasta ahora;"

                    n "a medida que ahondas en sus adentros, sientes sus paredes vaginales más estrechas"

                    n "y como tu polla va perdiendo lentamente la circulación por la presión,"

                    n "así como notas en la parte más sensible de tu glande,"

                    n "la forma clara del inicio de su cérvix."

                elif afternight04_Pussy_dick_deep_Speed_0_Success == 2:

                    n "Con la máxima lentitud que te es posible,"

                    n "desplazas tu enorme polla a través de lo largo y ancho de su estrecha cavidad vaginal"

                    n "hasta presionar fuertemente el inicio de su cuello uterino."

                elif afternight04_Pussy_dick_deep_Speed_0_Success == 3:

                    n "El calor de su interior no es nada en comparación"

                    n "a la sensación de tener arropada toda tu polla en sus ardientes carnes."

            else:

                call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY DEEP 0
            ############################################################
            ###########################################################

    ## Sexual REACTIONS # FAILED

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_deep_Speed_0_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¡COÑO!!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿QUÉ COJONES?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿ES QUE PRETENDES REVENTARME?!"

                if afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "¡Pero si antes te la has metido hasta el fondo tú sola!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pero fui yo quien me la metí!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "¿Y qué jodida diferencia hay?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Que eres un jodido bruto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "La diferencia es que ibas tan cachonda cabalgándome que te daba igual."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    pt "Hipócrita de mierda..."

                elif afternight04_Pussy_dick_deep_Speed_0_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "Pero si ya te la he metido hasta el fondo antes y no me has dicho nada..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils right01_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pues te lo digo ahora!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Me vas a joder el jodido coño!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "No..."

                    pt "si jodido está."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "Pero si llevas todo el día diciéndome que te la meta hasta el fondo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡Es una manera de hablar!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡¿Acaso no has visto el pedazo de pollón que tienes?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    p "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Tómatelo con calma joder..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Joder!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡No tan al fondo hostias!"

                if afternight04_Pussy_dick_deep_Speed_0_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Pero si ya te la he metido hasta el fondo narices!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pues ahora me ha dolido coño!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Ve con más cuidado."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

                elif afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Si no te me hubieras montado encima"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils right02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "y te la hubieras metido tú solo hasta el fondo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "quizás ahora sería más delicado."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Solo te estoy ofreciendo lo que me das."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡¿No te he dicho que vayas con cuidado?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Pensé que habías dicho que habías estado jugando con todo tipo de juguetes y tamaños."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "¡Pero es que tú eres muy bruto!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    pt "Mira quien habla..."

            elif afternight04_Pussy_dick_deep_Speed_0_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Hostias!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿No te he dicho que no me la metas tan al fondo tres veces ya?!"

                if afternight04_Pussy_dick_deep_Speed_0_Success == 1:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 00_a
                        show afternight04_sexbattle_d_pupils front00_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "Y también has dejado de quejarte alguna que otra vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pues aún me duele carajos!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡Al final me voy a cabrear de verdad!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_deep_Speed_0_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡QUE ME HACES DAÑO JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡No te lo volveré a repetir!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                # RAPE damn it!

    ## Sexual REACTIONS # SUCCESS

        if mc_body.roll_success == True:

            if afternight04_Pussy_dick_deep_Speed_0_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡JODER!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡La madre que te parió [protname]!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡¿Se puede saber qué diablos estás haciendo?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Follarte."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "¿No es lo que llevas pidiéndome toda la jodida noche?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "¡Dios!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils left05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡¿Pero hacía falta metérmela toda entera?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                p "Ya sabes el tamaño que tengo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "no te me pongas pusilánime ahora..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¡Como si no te la hubieras metido entera tú solito cuando me estabas violando!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "So cabrón,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "no me seas hipócrita."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "Tssk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Además,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "aún no la estoy moviendo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿Aún?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡DIOS!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡Es la segunda vez que me la metes entera y sigue doliendo un cojón!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "¿Quieres que la quite?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Ve con cuidado,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¿Vale?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Me cago en tu polla!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡Pedazo de polla que tienes!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Sino recuerdo mal de aquella vez en los vestuarios..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Tu polla es ligeramente más grande que la mía..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Y estoy seguro que tú no eres tan delicado con las chicas,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "como lo estoy siendo yo contigo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Tsskk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "Aunque me pregunto por qué se le puso tan dura en los vestuarios de chicos..."

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "¡Es la cuarta vez que me la metes entera"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "y me sigue pareciendo una jodida pasada!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Ufff..."

                if afternight04_Pussy_dick_deep_Speed_1_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Ahora sería hora de quizás empezaras a moverla de nuevo..."

                elif afternight04_Pussy_dick_deep_Speed_1_Failed > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "Aunque ve con cuidado si quieres volverla a mover..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "que duele un jodido montón."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Aunque estaría bien que empezaras a moverla..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Dios..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils up03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Tu polla entera dentro,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "sigo sin creérmelo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Madre mía [protname],"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils up05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "no te pares ahí..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "Sigue moviendo esa {i}\"Anaconda\"{/i} tuya..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success == 7:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Creo que puedes empezar a moverla..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            elif afternight04_Pussy_dick_deep_Speed_0_Success >= 8:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve


        ####################
        ####################
        ####################

        ####################      
        ####################
        #################### MED

####################
    ####################
        #################### MED 3

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 3): ##### MED 3
        $ debug ("Dick med speed 3 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_med_Speed_3_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_3_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_3_Success += 1

                #HER REACTION: PUSSY MED 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡Esto está algo mejor!"

            elif randomnum_1to5 == 2:

                d "¡Jodido pollón que tienes cabrón!"

            elif randomnum_1to5 == 3:

                d "¡Esto es un ritmo!"

            elif randomnum_1to5 == 4:

                d "¡Sigue así!"

            elif randomnum_1to5 == 5:

                d "¡Joder!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡Uhhmm!"

            elif randomnum_1to5 == 2:

                d "¡Mmhn!"

            elif randomnum_1to5 == 3:

                d "¡AHhm!"

            elif randomnum_1to5 == 4:

                d "¡Sihh!"

            elif randomnum_1to5 == 5:

                d "¡Hunmm!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve


                # DESCRIPTION: PUSSY MED 3
            ############################################################
            ###########################################################

        if afternight04_condom_broken == False:

            if afternight04_Pussy_dick_med_Speed_3_Done == 1:

                n "No solo tus caderas se mueven con una celeridad más que considerable,"

                n "el calor producido por el roce, junto con la opresión que ofrece su musculatura vaginal y la estrechez de su vagina,"

                n "consigue poner en apuros tu capacidad para retrasar el orgasmo."

                n "Aunque esta claro que en ella le causa un efecto parecido."

            elif afternight04_Pussy_dick_med_Speed_3_Done == 2:

                n "El sonido de sus sudorosos glúteos cuando chocas contra ellos en cada embestida,"

                n "junto a sus constantes gemidos,"

                n "no ayuda en absoluto a olvidar el enorme placer que sientes al tener casi la mitad de tu polla en su interior."

            elif afternight04_Pussy_dick_med_Speed_3_Done == 3:

                n "A pesar de que la embistes sin ningún tipo de compasión y a toda velocidad,"

                n "intentas, por el momento, no sobrepasar más allá de la mitad de tu polla en su interior."

                n "Su expresión facial delata un enorme gozo, pero también un punzante dolor en cada nueva fuerte y veloz embestida."

        else:

            call afternight04_Pussy_dick_condom_broken



                # HER DIALOGUES: PUSSY MED 3
            ############################################################
            ###########################################################

    ## Sexual REACTIONS #There´S NO FAIL in MED PUSSY sex.

        if afternight04_Pussy_dick_med_Speed_3_Done == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡Joder [protname]!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¡¿Qué?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "¡¿No es esto lo que me has estado pidiendo toda la jodida noche?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Que sí coño!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve
            
            d "Ufff..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡Pero vaya pollón tienes!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "..."

        elif afternight04_Pussy_dick_med_Speed_3_Done == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Dios!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡A esta velocidad me vas a reventar!"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Pues espera a que te la vuelva a meter entera."

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Pero eres consciente del daño que me has hecho cabrón?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    p "¿Y tú eres consciente de lo caliente que me has estado poniendo toda la jodida noche?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "Solo te pido que seas más delicado..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    p "¡¿Más aún?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Sí joder!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡No hace ni dos días que he estrenado este coño!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¡Eres tú la que lleva todo el rato pidiéndome que te viole!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Tssk..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Pues espera a que te la meta entera..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡¿Realmente crees que me va a caber entera?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "Como si no me lo hubieras estado pidiendo toda la noche..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "..."


        elif afternight04_Pussy_dick_med_Speed_3_Done == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "¡DIOS!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡Esto es lo que estaba esperando toda la jodida noche!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡Que me follaras como Dios manda!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            pt "¿Como Dios manda?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡Te ha tomado tu tiempo!"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "¡Pues espera a que te la meta entera dentro de nuevo y verás!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Eres un puto animal."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Y tú una jodida ninfómana."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils right02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Tssk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "¡Pues espera a que te la meta entera dentro y verás!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡No te flipes tampoco!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "¿Yo soy el flipado?"

        elif afternight04_Pussy_dick_med_Speed_3_Done == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "¡A esta velocidad me vas a dejar sin coño!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "Pero si apenas te he metido la mitad de mi polla."

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Sólo estoy calentando para volvértela a meter entera de nuevo..."

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "¡¿Para volverme a reventar el coño?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡Ni se te ocurra!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils down05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Espera a que te la meta entera y entonces verás..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¡No me seas cenizo!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils down01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "¡¿No ves que apenas me cabe así?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "Tú espera..."


        elif afternight04_Pussy_dick_med_Speed_3_Done == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "¡Hostia puta!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¡No pares jodido cabrón!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "Me alagas tanto cuando me dices cosas tan tiernas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Deja de farfullar y sigue follándome!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Como la perra en celo que eres."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡Tssk!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Bien que lo estás disfrutando tú también imbécil."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            pt "No se lo puedo negar..."

            pt "Si sigo así no tardaré mucho en correrme..."

        elif afternight04_Pussy_dick_med_Speed_3_Done == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Me cago en la hostia!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "¿Siempre tienes que estar diciendo palabrotas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Fóllame hijo de puta y cállate!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Si te va tanto lo duro,"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Al final te la voy a volver a meter hasta el fondo,"

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "hasta que vuelvas a chillar de dolor."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Ni se te ocurra..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "hasta que vuelvas a chillar de placer."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Tssk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "Al final te la voy a meter hasta el fondo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Mmmfhmm..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                pt "No me ha dicho que no..."

                pt "cada vez está más caliente..."

        elif afternight04_Pussy_dick_med_Speed_3_Done == 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "¡COÑO!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡NO PARES JODER!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "Te gusta,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "¿Verdad?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx08_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils up01_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡ME ENCANTA JODER!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_3_Done == 8:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils up01_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "¡HOSTIA PUTA!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡¿PERO POR QUÉ COÑO ME PONE TANTO ESTO?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "¡¿Acaso con polla no te gustaba tanto?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡JODER!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡NI LA MITAD!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "¿Va en serio?"

        elif afternight04_Pussy_dick_med_Speed_3_Done == 9:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils up00_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "¡SI!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils up01_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡JODER!"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils up04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                p "Al final pensaré que quieres que te la vuelva a meter entera..."

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Si eres capaz de ir con más cuidado..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "¿Y a qué coño esperas?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Al final pensaré que quieres que te la meta entera..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No hay huevos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            pt "¡¿Qué?!"


        elif afternight04_Pussy_dick_med_Speed_3_Done >= 10:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils up00_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            ############################################################
            ###########################################################
            
        call afternight04_Pussy_dick_med_Fail

            ############################################################
            ###########################################################

                # SLOW DOWN DICK: MED 3
            ############################################################
            ###########################################################

        call afternight04_Pussy_dick_general_slowdown

            ############################################################
            ###########################################################

####################
    ####################
        #################### MED 2

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 2): ##### MED 2
        $ debug ("Dick med speed 2 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_med_Speed_2_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_2_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_2_Success += 1

                #HER REACTION: PUSSY MED 2
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_2
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡COÑO!"

            elif randomnum_1to5 == 2:

                d "¡Pedazo de polla!"

            elif randomnum_1to5 == 3:

                d "¡Ese ritmo ya me gusta más!"

            elif randomnum_1to5 == 4:

                d "¡No pares!"

            elif randomnum_1to5 == 5:

                d "¡Pollón es poco!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_2
                #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡Uhhmm!"

            elif randomnum_1to5 == 2:

                d "¡Mmhn!"

            elif randomnum_1to5 == 3:

                d "¡AHhm!"

            elif randomnum_1to5 == 4:

                d "¡Sihh!"

            elif randomnum_1to5 == 5:

                d "¡Hunmm!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve


                # DESCRIPTION: PUSSY MED 2
            ############################################################
            ###########################################################

        if afternight04_condom_broken == False:

            if afternight04_Pussy_dick_med_Speed_2_Done == 1:

                n "No solo el ritmo en el que mueves tus caderas es ligeramente más veloz que al inicio,"

                n "sino que además sus paredes vaginales son cada vez más opresoras,"

                n "consiguiendo un mayor placer al tener gran parte de tu polla en su interior."

            elif afternight04_Pussy_dick_med_Speed_2_Done == 2:

                n "El tacto cálido y constante de sentir tu polla siendo tragada por su ardiente horno,"

                n "consigue dificultar la sensación de poder alejar el orgasmo lo máximo posible."

            elif afternight04_Pussy_dick_med_Speed_2_Done == 3:

                n "A pesar del condón, sus flujos vaginales consiguen humedecerte por completo tu entrepierna."

                n "Tu polla está aprisionada por sus fuertes y musculosas caderas"

                n "que aceptan de buen grado tu polla en cada embestida que le ofreces."

        else:

            call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY MED 2
            ############################################################
            ###########################################################

    ## Sexual REACTIONS #There´S NO FAIL in MED PUSSY sex.

        if afternight04_Pussy_dick_med_Speed_2_Done == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Seeeh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡Esto ya es otra cosa!"

            if mc_body.roll_success == False:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Con ese grito,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "pensaba que te estaba haciendo daño."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "¿Y quien te dice que no me lo esté haciendo?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Pero eres tú quien..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Ya lo sé idiota."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "..."

                pt "¿Se supone que puedo seguir entonces...?"

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "Con ese gemido,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "queda claro que no te disgusta."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                d "Hmm..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Es posible..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Ahora no pares capullo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                p "..."

        elif afternight04_Pussy_dick_med_Speed_2_Done == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Dioss..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Me voy a volver adicta a tu jodida polla..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_2_Done == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Ni se te ocurra parar!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Acaso quieres que te la meta más rápido o hasta el fondo?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "..."

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 07_a
                        show afternight04_sexbattle_d_pupils front07_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Es evidente que tus intentos para metérmela más al fondo han sido de todo menos delicados..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows surprisex01_a
                        with dissolve

                    p "Quizás es que aún no estás lo suficientemente caliente..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿Más aun?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "¡¿Te crees que soy un horno industrial?!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    pt "Está claro que no se trata realmente de ponerla más caliente,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                    pt "sino de volverla tan sumisa que sea capaz de ignorar el dolor."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No pares."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Metérmela entera tampoco es una idea tan terrible..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Al fin y al cabo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "en ocasiones eres capaz de metérmela sin reventarme del todo por dentro..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx01_a
                        with dissolve

            elif afternight04_Pussy_dick_med_Speed_3_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Puedes volver a aumentar el ritmo cuando te de la gana."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Lo que no sé,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "es que estás esperando a metérmela más rápidamente;"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "después del rato que hace que me estás follando..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            if afternight04_Pussy_dick_deep_Speed_0_Done < 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Pero estás tomando drogas alucinógenas,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "si crees que esa {i}\"Anaconda\"{/i} tuya va a caber aquí dentro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            p "..."

        elif afternight04_Pussy_dick_med_Speed_2_Done == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Me encanta cuando me follas así..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_2_Done == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "No sabes cuanto he estado esperando este jodido momento de las narices..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_2_Done == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Me cagüen todo!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "¡No tienes ni jodida idea de lo que se siente!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            pt "Espero que sea algo agradable al menos..."

        elif afternight04_Pussy_dick_med_Speed_2_Done == 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Si me sigues follando así,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "al final no sé si realmente querré recuperar mi polla de nuevo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "..."

            pt "¡¿Habla en serio?!"

        elif afternight04_Pussy_dick_med_Speed_2_Done == 8:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡Dios!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Tienes un pollón enorme [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Fóllame más rápido,"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "O métemela entera de nuevo."

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "¡Pero solo haces que quejarte del dolor que te provoco!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Me da igual..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    pt "Sí..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    pt "eso dices ahora."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Fóllame."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "Quiero sentir como chocas contra el fondo de mi coño de nuevo..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "o métemela dentro de una jodida vez..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Eres consciente del tamaño,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "¿Verdad?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "He dicho que me folles,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "trátame como una perra si eso te pone más caliente,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "pero hazlo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            pt "Me está empezando a dar miedo..."

        elif afternight04_Pussy_dick_med_Speed_2_Done == 9:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Quiero que me folles más duro [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Quiero que me la metas hasta el fondo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Pero..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Me da igual el dolor..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "Reviéntame..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            pt "Ya..."

            pt "eso lo dices ahora..."

            pt "Perra."

        elif afternight04_Pussy_dick_med_Speed_2_Done >= 10:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            ############################################################
            ###########################################################
            
        call afternight04_Pussy_dick_med_Fail

            ############################################################
            ###########################################################

####################
    ####################
        #################### MED 1

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 1): ##### MED 1
        $ debug ("Dick med speed 1 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_med_Speed_1_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_1_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_med_Speed_1_Success += 1


                #HER REACTION: PUSSY MED 1
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
            #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡Coño!"

            elif randomnum_1to5 == 2:

                d "¡Puto pollón!"

            elif randomnum_1to5 == 3:

                d "¡Y apenas te estás moviendo!"

            elif randomnum_1to5 == 4:

                d "¡Joder...!"

            elif randomnum_1to5 == 5:

                d "¡Ostias...!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                d "¡Uhhmm!"

            elif randomnum_1to5 == 2:

                d "¡Mmhn!"

            elif randomnum_1to5 == 3:

                d "¡AHhm!"

            elif randomnum_1to5 == 4:

                d "¡Sihh!"

            elif randomnum_1to5 == 5:

                d "¡Hunmm!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve


                # DESCRIPTION: PUSSY MED 1
            ############################################################
            ###########################################################

        if afternight04_condom_broken == False:

            if afternight04_Pussy_dick_med_Speed_1_Done == 1:

                n "Con suma precaución, empiezas a desplazar tu miembro en su interior,"

                n "apreciando cada centímetro de su estrecho y ardiente vagina."

            elif afternight04_Pussy_dick_med_Speed_1_Done == 2:

                n "Con suma lentitud, desplazas tu erecto polla, acariciando sus estrechas paredes vaginales"

                n "con el roce de la delgada capa de plástico que cubre tu enorme mástil."

            elif afternight04_Pussy_dick_med_Speed_1_Done == 3:

                n "Con parsimonia y cautela, transitas por su estrecha y ardiente cavidad."

        else:

            call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY MED 1
            ############################################################
            ###########################################################

    ## Sexual REACTIONS #There´S NO FAIL in MED PUSSY sex.

        if afternight04_Pussy_dick_med_Speed_1_Done == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Que pollón tienes cabronazo."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Y eso que apenas estás moviéndote..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            pt "Y no te he metido ni la mitad..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "pero me estás removiendo toda por dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Mmmhh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Y me encanta."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¡¿Será posible?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            p "¡¿Qué?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Cómo me puedes poner tan caliente a la mierda de velocidad a la que vas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "..."

        elif afternight04_Pussy_dick_med_Speed_1_Done == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils down02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Ya es la tercera vez que me vas a esta velocidad,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "pero no puedo creer lo perra que me está poniendo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "¿Podrías pasarte el día follándome así?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Aunque de tanto en cuanto también podrías ir subiendo un poco el ritmo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            p "..."

        elif afternight04_Pussy_dick_med_Speed_1_Done == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Me encanta sentir como mi coño se va arropando a lo largo y ancho de tu jodida {i}anaconda{/i}..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Me encanta sentir las palpitaciones de tu polla a través de mi estrecho coño..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "No me disgusta que me folles a esta velocidad,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "pero estaría mejor si subieras un poco el ritmo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 8:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils down01_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Me pone mogollón como me follas,"

            if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                if afternight04_Pussy_dick_deep_Speed_0_Success == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "y aunque no hayas sido nada delicado metiéndomela hasta el fondo,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx04_a
                        with dissolve

                    d "quiero que lo vuelvas a intentar..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    d "pero quiero volverla a sentir toda dentro de mi."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            else:

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                d "pero podrías subir un poco más ese ritmo..."

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            p "..."

            if afternight04_Pussy_dick_med_Speed_2_Done > 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Sígueme follando así de duro [protname]!"

            else:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Dame más duro [protname]."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done == 9:

            d "Te agradecería si pudieras aumentar el ritmo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_1_Done >= 10:

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            ############################################################
            ###########################################################

        call afternight04_Pussy_dick_med_Fail

            ############################################################
            ###########################################################


####################
    ####################
        #################### MED 0

    elif (mc_body.store["dick"] == "Pussy_dick_med" and mc_body.dick_speed == 0): ##### MED 0
        $ debug ("Dick med speed 0 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_med_Speed_0_Done += 1

        if mc_body.roll_success == False: 
            $ afternight04_Pussy_dick_med_Speed_0_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_med_Speed_0_Success += 1

                # DESCRIPTION: PUSSY MED 0
            ############################################################
            ###########################################################

        if (afternight04_Pussy_dick_med_Speed_0_Done == 1 and afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0):

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            n "Con el preservativo empapado por su abundante jugo,"

            n "desplazas tu miembro hasta el inicio de su ardiente cavidad."

            n "Con cierta presión y dificultad, consigues abrirte paso en su interior,"

            n "hasta detenerte en un punto en el que en su rostro ves reflejado el inicio de un dolor agonizante."


                # HER REACTION: PUSSY MED 0
            ############################################################
            ###########################################################

        if (afternight04_Pussy_dick_med_Speed_0_Done == 1 and afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0):

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_0
        
            if randomnum_1to5 == 1:

                d "¡Por fin...!"

            elif randomnum_1to5 == 2:

                d "¡Joder con el pollón!"

            elif randomnum_1to5 == 3:

                d "¡Ya era hora...!"

            elif randomnum_1to5 == 4:

                d "¡Consiguió entrar!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "¿Lo dudaba?"

            elif randomnum_1to5 == 5:

                d "¡Al fin ha entrado...!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

        if mc_body.roll_success == False: # REally necessary??

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_0
            
            if randomnum_1to5 == 1:

                d "¡Dios!"

            elif randomnum_1to5 == 2:

                d "¡Menudo rabo!"

            elif randomnum_1to5 == 3:

                d "¡Realmente lo tengo estrecho!"

            elif randomnum_1to5 == 4:

                d "Duele un poco,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 06_a
                    show afternight04_sexbattle_d_pupils front06_a
                    show afternight04_sexbattle_d_eyebrows sadx03_a
                    with dissolve

                d "pero me encanta..."

            elif randomnum_1to5 == 5:

                d "Lo que tienes entre piernas es un arma de destrucción masiva..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_0
            
            if randomnum_1to5 == 1:

                d "Seeh..."

            elif randomnum_1to5 == 2:

                d "Otra vez dentro..."

            elif randomnum_1to5 == 3:

                d "Así sí..."

            elif randomnum_1to5 == 4:

                d "Me encanta..."

            elif randomnum_1to5 == 5:

                d "Me encanta sentirlo dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                # DESCRIPTION: PUSSY MED 0
            ############################################################
            ###########################################################

        if afternight04_condom_broken == False:

            if afternight04_Pussy_dick_med_Speed_0_Done == 2:

                if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                    n "A pesar de que en realidad tu pene ha conseguido introducirse hasta el fondo,"

                    n "Su mueca de dolor sigue intacta en su rostro,"

                    n "por lo que por el momento decides no forzar la situación."

                else:

                    n "Siendo la segunda vez que te abres paso en su interior,"

                    n "sigue siendo una cavidad estrecha,"

                    n "así como su expresión facial sigue mostrando un dolor intenso cuando pretendes ir más lejos."

            elif afternight04_Pussy_dick_med_Speed_0_Done == 3:

                if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                    n "Aunque tu polla haya penetrado su interior hasta lo más hondo,"

                else:

                    n "Aunque no es la primera vez que la penetras hasta este punto,"

                n "sigue siendo un lugar angosto y hostil con tu tamaño."

                n "Muestra de ello es su clara mueca de dolor."

            elif afternight04_Pussy_dick_med_Speed_0_Done == 4:

                n "Su rostro sigue mostrando una gesto de aflicción cuando consigues meter hasta la mitad de tu miembro."

                n "Pero aparentemente se adapta mejor al dolor que siente,"

                n "y casi te da la sensación que hasta empieza a disfrutarlo."

            elif afternight04_Pussy_dick_med_Speed_0_Done == 4:

                n "Apenas una ligera muestra de dolor se dibuja en su rostro,"

                n "para luego devolverte una sonrisa entre inocente y perturbadora..."

            elif afternight04_Pussy_dick_med_Speed_0_Done == 5:

                n "A pesar de sus esfuerzos para disimularlo,"

                n "está claro que tu miembro sigue haciéndole efecto,"

                n "pero eso no quita que a pesar del dolor que estás convencido que sufre,"

                n "hay también un placer retorcido."

            elif afternight04_Pussy_dick_med_Speed_0_Done == 6:

                n "Su rostro ya no da muestras de un dolor evidente,"

                n "más bien algo que mezcla lo mórbido, con el deseo."

            elif afternight04_Pussy_dick_med_Speed_0_Done >= 7:

                d "..."

        else:

            call afternight04_Pussy_dick_condom_broken


                # HER DIALOGUES: PUSSY MED 0
            ############################################################
            ###########################################################

    ## Sexual REACTIONS #There´S NO FAIL in MED PUSSY sex.

        if afternight04_Pussy_dick_med_Speed_0_Done == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Joder..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            p "¿Qué pasa?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡Que tienes un pedazo pollón!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¡Joder!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "¿No es lo que me has estado pidiendo toda la jodida noche?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Que sí joder!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Pero eso no quita que tu {i}Anaconda{/i} es enorme..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "¿La quito?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Ni se te ocurra."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

        elif afternight04_Pussy_dick_med_Speed_0_Done == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils down01_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Tengo el coño que me hace chispa..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Uhhh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx07_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils down03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Que gusto..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils down04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "que maravilla..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx08_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Que pollón!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "¿Realmente tiene que recordarme a ese {a=https://www.youtube.com/watch?v=0eZ4pWP1H2o}personaje{/a}?"

        elif afternight04_Pussy_dick_med_Speed_0_Done == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Dios..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "No sé que tiene tu polla"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "que no haya podido conseguir con toda la mierda que me he comprado en la jodida sex-shop,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "pero desde luego se siente mucho mejor..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "A saber que se habrá comprado..."

        elif afternight04_Pussy_dick_med_Speed_0_Done == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Déjala un ratito ahí dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Me encanta sentir la rigidez,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "las palpitaciones,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "el calor..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx07_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Dios!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            d "¿Por qué coño me pone tan caliente tu polla?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Por que te has vuelto una jodida ninfómana de narices..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils left03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Tssk..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_0_Done == 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Ya era hora de que me la volvieras a meter dentro;"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "jodido cabrón..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_0_Done == 6:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Ni se te ocurra volver a sacarla..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_0_Done == 7:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Siiiih..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Ahora mueve un poco cabrón..."
            
            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "Fóllame."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_0_Done == 8:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "Quiero sentir esa verga tuya rasgándome toda por dentro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils down05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            pt "Eso es lo que dices ahora..."

        elif afternight04_Pussy_dick_med_Speed_0_Done == 9:

            d "Fóllame."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

        elif afternight04_Pussy_dick_med_Speed_0_Done >= 10:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx05_a
                with dissolve
            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx04_a
                with dissolve

            ############################################################
            ###########################################################
            
        call afternight04_Pussy_dick_med_Fail

            ############################################################
            ###########################################################

        ####################
        ####################
        ####################

        ####################      
        ####################
        #################### LOW

####################
    ####################
        #################### LOW 3

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 3): ##### LOW 3
        $ debug ("Dick low speed 3 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_low_Speed_3_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_3_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_3_Success += 1

                #HER REACTION: PUSSY LOW 3
            ############################################################
            ###########################################################

        if mc_body.roll_success == False: # REally necessary??

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_3
            
            if randomnum_1to5 == 1:

                d "Tssk..."

            elif randomnum_1to5 == 2:

                d "..."

            elif randomnum_1to5 == 3:

                d "Pff..."

            elif randomnum_1to5 == 4:

                d "Hmm..."

            elif randomnum_1to5 == 5:

                d "Aish..."

    ## Success Reactions

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_3
            
            if randomnum_1to5 == 1:

                d "Hm..."

            elif randomnum_1to5 == 2:

                d "Mm..."

            elif randomnum_1to5 == 3:

                d "Mnh..."

            elif randomnum_1to5 == 4:

                d "SiHh..."

            elif randomnum_1to5 == 5:

                d "Hum..."

                #HER DIALOGUES: PUSSY LOW 3
            ############################################################
            ###########################################################

    ## Sexual Description "Dick low speed 3 rape" #There´s no need for fail here.

        if afternight04_Pussy_dick_low_Speed_3_Done == 1:

            n "Aceleras el ritmo de tu manubrio con una fuerte presión sobre su cálida y abundantemente húmeda vagina,"

            n "consiguiendo que el placer aumente considerablemente."

        elif afternight04_Pussy_dick_low_Speed_3_Done == 2:

            n "Con esta contundente celeridad,"

            n "y la presión que ejerces con tu firme miembro contra sus suaves y voluptuosos labios,"

            n "da la sensación que quieras prender fuego en su entrepierna;"

            n "como si estuvieras frotando una madera entre hojas."

        elif afternight04_Pussy_dick_low_Speed_3_Done == 3:

            n "El calor que se desprende de su entrepierna, ya no solo depende del ardor de su interior,"

            n "sino también del contraste y el velo roce que sufre el preservativo que rodea tu miembro viril."

    ## FAIL

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_low_Speed_3_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "No digo que no esté bien que me frotes rápidamente la polla contra mi coño."

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Pero podrías volver a metérmela de una jodida vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "La prefiero dentro que fuera."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Pero ya sería hora de que me empotraras!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¡¿No crees?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_3_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "En serio..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Deja de jugar con mi puto coño"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "y métemela de una jodida vez."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_3_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Que estés frotándola rápidamente no hará que me corra más rápido."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Métemela de una puta vez!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_3_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Al final me voy a cabrear..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_3_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

    ##
    ##  SUCCESS

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_low_Speed_3_Success == 1: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Definitivamente mejor que antes..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_3_Success == 2: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "No negaré que se siente bien rico..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Pero podrías aumentar el ritmo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                pt "¡¿Más aún?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "o mejor aún..."

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "preferiría que volvieras a rellenarme por dentro..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "podrías empezar a pensar en rellenarme por dentro de una vez..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Eres un jodido ansias de las narices..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "Puede..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "pero me encanta sentir tu polla dentro de mi."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "No pienso rellenarte de semen por dentro,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                p "que quede claro..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿En que momento he dicho eso?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Ya,"

                extend " ya..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "eso lo dices ahora..."

                pt "¡Y NO!"

                pt "¡No pienso dejar preñado a mi amigo de la infancia"

                pt "porque una rara voz interior me lo ordene!"

                p "..."

                pt "Estoy fatal..."

            elif afternight04_Pussy_dick_low_Speed_3_Success == 3: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows serious_a
                    with dissolve

                d "La verdad es que la sensación es más agradable de lo que me había imaginado..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils down02_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Tu polla está dura como una roca y realmente caliente."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "¿Lo dice para ponerme más caliente?"

                pt "Por que el jodido lo está consiguiendo..."

            elif afternight04_Pussy_dick_low_Speed_3_Success == 4: # low_speed_3

                d "¿Qué tal si empiezas a plantearte la posibilidad de metérmela?"

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils down03_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Me gustaría volverla a sentir dentro de mi."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils down04_a
                        show afternight04_sexbattle_d_eyebrows sadx02_a
                        with dissolve

                    d "Me gustaría poderla sentir dentro de mi de una jodida vez."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."



            elif afternight04_Pussy_dick_low_Speed_3_Success == 5: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿A qué estás esperando para follarme?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿A que vuelen las vacas?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¡Fóllame de una vez!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_3_Success >= 6: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                # SLOW DOWN DICK: LOW 3
            ############################################################
            ###########################################################

        call afternight04_Pussy_dick_general_slowdown


####################
    ####################
        #################### LOW 2

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 2): ##### LOW 2
        $ debug ("Dick low speed 2 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_low_Speed_2_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_2_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_2_Success += 1

                #HER REACTION: PUSSY LOW 2
            ############################################################
            ###########################################################

        if mc_body.roll_success == False: # REally necessary??

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_3
            
            if randomnum_1to5 == 1:

                d "Tssk..."

            elif randomnum_1to5 == 2:

                d "..."

            elif randomnum_1to5 == 3:

                d "Pff..."

            elif randomnum_1to5 == 4:

                d "Hmm..."

            elif randomnum_1to5 == 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Aish..."

    ##

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_2
            
            if randomnum_1to5 == 1:

                d "Hm..."

            elif randomnum_1to5 == 2:

                d "Mm..."

            elif randomnum_1to5 == 3:

                d "Mnh..."

            elif randomnum_1to5 == 4:

                d "Hmn..."

            elif randomnum_1to5 == 5:

                d "Hum..."

                #HER DIALOGUES: PUSSY LOW 2
            ############################################################
            ###########################################################


    ## Sexual Description "Dick low speed 2 rape"

        if afternight04_Pussy_dick_low_Speed_2_Done == 1:

            n "No solo tus caderas se mueven ligeramente más aceleradas,"

            n "la presión que ejerces contra su carnoso y ardiente horno, es también mayor."

            n "La sensación de sentir sus carnes internas al tacto de tu polla,"

            n "incluso cubierta por la goma del preservativo, no te deja en absoluto indiferente."

        elif afternight04_Pussy_dick_low_Speed_2_Done == 2:

            n "La ardiente y húmeda carne de sus labios menores doblándose y frotándose contra tu erecto miembro,"

            n "hace que tu sangre fluya con más celeridad por tu cuerpo."

        elif afternight04_Pussy_dick_low_Speed_2_Done == 3:

            n "Empiezas a sentir cerca de tus testículos,"

            n "como su abundante flujo vaginal se está derramando más allá del preservativo,"

            n "debido a la constante fricción, empapando prácticamente todo tu instrumento viril."

    ##
    ##  FAILED

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_low_Speed_2_Failed == 1: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Algo mejor que antes,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Pero estoy segura que dentro se sentiría mucho mejor."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "He visto marsupiales en celo más pacientes que tú."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_2_Failed == 2: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Aunque solo sea un paso previo para acelerar el ritmo,"

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "si me la metieras de una jodida vez"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "Te lo agradecería más."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "me gustaría más que volvieras a empotrarme con tu enorme {i}anaconda{/i}."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Tú y el juego previo no sois muy amigos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Cuando te hayas metido por el culo todos los juguetes que me he comprado yo,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "me hablas de juego previo."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "¿Quieres?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx01_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows surprisex01_a
                    with dissolve

                p "¡¿Te los has metido todos por el culo?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡No!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡Pero tú no tienes coño!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡¿verdad?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                pt "Eso es verdad..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "{size=15}Al menos no todos...{/size}"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                pt "¡¿Qué?!"

            elif afternight04_Pussy_dick_low_Speed_2_Failed == 3: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Estás empezando a agotar mi paciencia [protname]..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_2_Failed >= 4: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

    ## SUCCESS

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_low_Speed_2_Success == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Esto ya es otra cosa..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_2_Success == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No es que me disguste..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Pero ya que estás en modo frotar,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "¿Has pensado en hacerlo algo más rápido...?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_2_Success == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "Sino la quieres meter,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "al menos podrías subir un poco más ese ritmo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_2_Success == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿Estás esperando a que surja algún genio?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "¿Qué?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Mi coño no es ninguna lámpara mágica..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Sabes?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_2_Success == 5:

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Cuándo piensas volver a metérmela?"

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Pero métemela de una jodida vez!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Al final me voy a cabrear..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_2_Success >= 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

####################
    ####################
        #################### LOW 1

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 1): ##### LOW 1
        $ debug ("Dick low speed 1 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_low_Speed_1_Done += 1

        if mc_body.roll_success == False: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_1_Failed += 1

        elif mc_body.roll_success == True: #Big pain.
            $ afternight04_Pussy_dick_low_Speed_1_Success += 1

                #HER REACTION: PUSSY LOW 1
            ############################################################
            ###########################################################

        if mc_body.roll_success == False: # REally necessary??

            if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_1
            
            if randomnum_1to5 == 1:

                d "Tssk..."

            elif randomnum_1to5 == 2:

                d "..."

            elif randomnum_1to5 == 3:

                d "Pff..."

            elif randomnum_1to5 == 4:

                d "Hmm..."

            elif randomnum_1to5 == 5:

                d "Aish..."

    ##

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_1
            
            if randomnum_1to5 == 1:

                d "Hm..."

            elif randomnum_1to5 == 2:

                d "Mm..."

            elif randomnum_1to5 == 3:

                d "Mnh..."

            elif randomnum_1to5 == 4:

                d "Hmn..."

            elif randomnum_1to5 == 5:

                d "Hum..."

                #HER DIALOGUES: PUSSY LOW 1
            ############################################################
            ###########################################################


    ##
    ## Sexual Description "Dick low speed 1"

        if afternight04_Pussy_dick_low_Speed_1_Done == 1:

            n "Perezosamente, desplazas tu miembro a lo largo de su abundantemente húmeda vagina,"

            n "mientras sientes el ardor que desprende."

        elif afternight04_Pussy_dick_low_Speed_1_Done == 2:

            n "Con suma lentitud, vuelves a deslizar tu erecto mástil por fogosa y reciente virtud."

        elif afternight04_Pussy_dick_low_Speed_1_Done == 3:

            n "Deslizas con suma calma tu enorme polla sobre su encendida concha."

    ##
    ## FAIL

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_low_Speed_1_Failed == 1:

                if afternight04_Pussy_dick_low_Speed_1_Success > 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Esperaba que a estas alturas pudieras metérmela dentro,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "en lugar de seguir frotándome el {i}chirri{/i}..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "En lugar de frotar,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "podrías metérmela dentro."

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Failed == 2:

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                d "La sensación es agradable,"

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                d "pero va siendo hora de que se meta dentro de una vez"

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Failed == 3:

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                d "Si lo único que vas a hacer es frotar,"

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                d "al final me voy a cansar..."

                if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                p "..."

            elif afternight04_Pussy_dick_low_Speed_1_Failed >= 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve
    ##
    ##  SUCCESS

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_low_Speed_1_Success == 1: # low_speed_1

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

                d "Sí..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Me encanta sentir tu enorme polla"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "y lo dura que te la pongo..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Success == 2: # low_speed_1

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils down04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Despacito,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "pero sin pausas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Success == 3: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Como me pone este pollón..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Success == 4: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "No te detengas..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Success == 5: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils down03_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "Me encanta,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Pero estoy segura que puedes darle mejor utilidad..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx01_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_1_Success >= 6: # low_speed_3

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

####################
    ####################
        #################### LOW 0

    elif (mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0): ##### LOW 0
        $ debug ("Dick low speed 0 VAGINAL SEX &/")
        $ afternight04_Pussy_dick_low_Speed_0_Done += 1

        if mc_body.roll_success == False: 
            $ afternight04_Pussy_dick_low_Speed_0_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_low_Speed_0_Success += 1

                #HER REACTION: PUSSY LOW 0
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_0
            
            if randomnum_1to5 == 1:
                
                d "Tssk..."

            elif randomnum_1to5 == 2:

                d "..."

            elif randomnum_1to5 == 3:

                d "Pff..."

            elif randomnum_1to5 == 4:

                d "Hmm..."

            elif randomnum_1to5 == 5:

                d "Aish..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

    ##

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans low_speed_1
            
            if randomnum_1to5 == 1:

                #if current_pose.id == "pose_1":

                    #images

                d "Hm..."

            elif randomnum_1to5 == 2:

                d "Mm..."

            elif randomnum_1to5 == 3:

                d "Mnh..."

            elif randomnum_1to5 == 4:

                d "Seh..."

            elif randomnum_1to5 == 5:

                d "Hum..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

                #HER DIALOGUES: PUSSY LOW 1
            ############################################################
            ###########################################################


    ##
    ## Sexual Description "Dick low speed 0"

        if afternight04_Pussy_dick_low_Speed_0_Done == 1:

            n "Acercas grácilmente tu erecto miembro cerca de su ardiente núcleo de calor."

            n "sintiendo el ardiente y suave tacto de sus labios al mismo tiempo que su abundante humedad brotando de su interior."

        elif afternight04_Pussy_dick_low_Speed_0_Done == 2:

            if current_pose.id == "pose_1":

                n "Vuelves a posar tu rígido mástil sobre su ardiente vagina,"

            else:

                n "Vuelves a posar tu rígido mástil entre sus piernas en busca de su ardiente vagina."

        elif afternight04_Pussy_dick_low_Speed_0_Done == 3:

            n "Vuelves a sentir el calor de su triangulo de las bermudas alrededor de tu pollón."

    ##
    ## FAIL

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_low_Speed_0_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Ya era hora de que te decidieras."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Ahora date prisa y métemela dentro."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Madre mía..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "Cálmate un poco."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "..."

            elif afternight04_Pussy_dick_low_Speed_0_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Venga,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "métemela ya."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¡No me hagas esperar más!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Se un buen chico y fóllame de una jodida vez."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Failed >= 5:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

    ##
    ##  SUCCESS

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_low_Speed_0_Success == 1: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Por fin tengo tu polla cerca..."

                if current_pose.id == "pose_1":

                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Ya era hora..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Success == 2: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Me gusta sentir tu enorme polla sobre mi cucurucha..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                pt "¿Cucu qué?"



            elif afternight04_Pussy_dick_low_Speed_0_Success == 3: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "Siento tus palpitaciones a través de pollón."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Success == 4: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

                d "No me hagas suplicar [protname],"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                d "Continua..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Success == 5: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "No pares ahora..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx02_a
                    with dissolve

            elif afternight04_Pussy_dick_low_Speed_0_Success >= 6: # low_speed_0

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils down05_a
                    show afternight04_sexbattle_d_eyebrows sadx04_a
                    with dissolve

                p "..."

        ####################
        ####################
        ####################

        ####################      
        ####################
        #################### OUT

####################
    ####################
        #################### OUT

    elif (mc_body.store["dick"] == "Pussy_dick_out"): ##### OUT
        $ debug ("Dick OUT speed 0 VAGINAL SEX &/")

        $ mc_body.dick_speed = 0
        $ afternight04_Pussy_dick_out_Done += 1

        if mc_body.roll_success == False: 
            $ afternight04_Pussy_dick_out_Failed += 1

        elif mc_body.roll_success == True:
            $ afternight04_Pussy_dick_out_Success += 1

                #HER REACTION: PUSSY OUT
            ############################################################
            ###########################################################

        if mc_body.roll_success == False:

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans OUT

            if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve
            
            if randomnum_1to5 == 1:

                d "¡¿Qué?!"

            elif randomnum_1to5 == 2:

                d "¡Oye!"

            elif randomnum_1to5 == 3:

                d "¡¿Pero qué?!"

            elif randomnum_1to5 == 4:

                d "¡¿Qué diablos?!"

            elif randomnum_1to5 == 5:

                d "¡¿En serio?!"

            if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

    ##

        elif mc_body.roll_success == True:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans OUT
            
            if randomnum_1to5 == 1:

                d "¡¿Euh?!"

            elif randomnum_1to5 == 2:

                d "¡¿Por?!"

            elif randomnum_1to5 == 3:

                d "¿Uh?"

            elif randomnum_1to5 == 4:

                d "No..."

            elif randomnum_1to5 == 5:

                d "La madre que te parió..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve


                #HER DIALOGUES: PUSSY LOW 1
            ############################################################
            ###########################################################


    ##
    ## Sexual Description "Dick OUT"

        if afternight04_Pussy_dick_out_Done == 1:

            n "Sin previo aviso, apartas tu polla de golpe."

        elif afternight04_Pussy_dick_out_Done == 2:

            n "Sin darle tiempo a penas a reaccionar, vuelves a retirar rápidamente tu miembro."

        elif afternight04_Pussy_dick_out_Done == 3:

            n "Coges a Dídac por sorpresa al volver a quitarla de golpe."

    ##
    ## FAIL

        if mc_body.roll_success == False:

            if afternight04_Pussy_dick_out_Failed == 1:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Por qué diablos la sacas?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Intento hacerte disfrutar,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 07_a
                    show afternight04_sexbattle_d_pupils front07_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "Ten un poco más de fe."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx005_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No soy muy creyente que digamos..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."


            elif afternight04_Pussy_dick_out_Failed == 2:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Otra vez la sacas?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "¡¿Por qué?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Es que te ibas a correr?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                #if (mc_body.orgasm == 0 and mc_body.pleasure in range (25, 34)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (50, 74)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (75, 110)):
                if (mc_body.orgasm == 0 and mc_body.pleasure in range (25, 34)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (50, 59)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (70, 79)):

                    pt "No está tan desencaminada..."

                #elif (mc_body.orgasm == 0 and mc_body.pleasure in range (35, 40)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (75, 89)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (111, 135)):
                elif (mc_body.orgasm == 0 and mc_body.pleasure in range (35, 40)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (60, 69)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (80, 89)):

                    pt "No es que me quede mucho,"

                    pt "la verdad..."

                #elif (mc_body.orgasm == 0 and mc_body.pleasure in range (41, 50)) or (mc_body.orgasm == 1 and mc_body.pleasure in range (90, 100)) or (mc_body.orgasm == 2 and mc_body.pleasure in range (136, 150)):
                elif (mc_body.orgasm == 0 and mc_body.pleasure > 41) or (mc_body.orgasm == 1 and mc_body.pleasure > 70) or (mc_body.orgasm == 2 and mc_body.pleasure > 100):

                    pt "En realidad estoy casi a punto..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx07_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "Aún tengo para rato."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Me alegra oír eso."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

            elif afternight04_Pussy_dick_out_Failed == 3:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No veo como me vas a poder follar si vas sacando la polla cada dos por tres..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Porque hay otra maneras de follar que no son el mete-saca habitual en los animales sin cerebro."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 02_a
                    show afternight04_sexbattle_d_pupils front02_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "No me agotes la paciencia [protname];"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "O al final acabaré cabalgándote hasta que salga el sol"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "y tu polla quede tan flácida que deban trasplantarla quirúrgicamente."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_out_Failed == 4:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡¿Para qué diablos vuelves a quitar la polla?!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡La idea es que me folles!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡No que vayas haciendo el gilipollas!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "¿Tú quieres que me corra pronto?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "¿o tarde?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "¡Ya te he dicho lo que quiero!"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "Pues si te sigo follando,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "y me corro antes de lo que tú quieres,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "te vas a quedar a cuatro velas."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "¿Es eso lo que quieres?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Tssk..."

            elif afternight04_Pussy_dick_out_Failed == 5: # Must be 5

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Como vuelvas a quitar la polla de ahí,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx09_a
                    show afternight04_sexbattle_d_eyes 00_a
                    show afternight04_sexbattle_d_pupils front00_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "te voy a violar tan fuerte que te vas a quedar sin huevos."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                pt "Una expresión algo perturbadora..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve


            elif afternight04_Pussy_dick_out_Failed >= 6:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

    ##
    ##  SUCCESS

        elif mc_body.roll_success == True:

            if afternight04_Pussy_dick_out_Success == 1: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                d "¿En qué demonios estás pensando al quitar la polla?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx03_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "En que voy a durar más y por lo tanto lo vas a disfrutar mejor."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils right04_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Pff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Eso espero."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                pt "Para hacerle más favores..."

            elif afternight04_Pussy_dick_out_Success == 2: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Vuelves a sacarla?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Espero que sepas lo que te haces."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx02_a
                    with dissolve

                p "Sé lo que me hago."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Pff..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "Eso espero."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx06_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

            elif afternight04_Pussy_dick_out_Success == 3: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "¿Otra vez?"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx032_a
                    with dissolve

                d "Que yo sepa,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                d "para follar es necesario que la polla esté dentro,"

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "no fuera."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx02_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Eres un pesado."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils right03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Tssk..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx04_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils right05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_out_Success == 4: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "Al final me voy a cansar de que la vayas quitando cada dos por tres..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx07_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows angryx03_a
                    with dissolve

                p "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx08_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

            elif afternight04_Pussy_dick_out_Success == 5: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                d "Al final te voy a violar."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx09_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

                p "..."

            elif afternight04_Pussy_dick_out_Success >= 6: # OUT

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx08_a
                    show afternight04_sexbattle_d_eyes 03_a
                    show afternight04_sexbattle_d_pupils front03_a
                    show afternight04_sexbattle_d_eyebrows angryx04_a
                    with dissolve

                d "..."

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Silentx10_a
                    show afternight04_sexbattle_d_eyes 05_a
                    show afternight04_sexbattle_d_pupils front05_a
                    show afternight04_sexbattle_d_eyebrows angryx05_a
                    with dissolve

####################
    ####################
        ####################

        ####################

    elif (mc_body.store["dick"] == ""): ##### OUT

        $ debug("Dick \"\", that means something is done wrong. 5848")

        $ debug ("Dick \"\", that means something is done wrong. 5848")

    else:
        
        $ debug("Dick what the fuck? This message should NOT appear 0846.")
        $ debug ("Dick what the fuck? This message should NOT appear 0846.")

####################
    ####################
        ####################

        ####################



############################################################
###########################################################

    ###########################
    ##########################

    ### RAPE OR NOT?

    $ debug ("Wannabe02")

    if ((afternight04_Pussy_dick_out_Success > 4) # Failed probably is not necessary.
    #or ((mc_body.store["dick"] == "Pussy_dick_low" and mc_body.dick_speed == 0) # Does not make sense this one...
        #and (afternight04_Pussy_dick_low_Speed_0_Failed > 4))
    or ((((afternight04__prehfix_Pussy_dick_low == True) and (mc_body.dick_speed > 0)) 
        and (((afternight04_Pussy_dick_low_Speed_1_Success > 7) or (afternight04_Pussy_dick_low_Speed_1_Failed > 4))
        or ((afternight04_Pussy_dick_low_Speed_2_Success > 7) or (afternight04_Pussy_dick_low_Speed_2_Failed > 4))
        or ((afternight04_Pussy_dick_low_Speed_3_Success > 7) or (afternight04_Pussy_dick_low_Speed_3_Failed > 4))))

    or ((((afternight04__prehfix_Pussy_dick_med == True) and (mc_body.dick_speed > 0)) 
        and (((afternight04_Pussy_dick_med_Speed_1_Success > 10) or (afternight04_Pussy_dick_med_Speed_1_Failed > 8))
        or ((afternight04_Pussy_dick_med_Speed_2_Success > 10) or (afternight04_Pussy_dick_med_Speed_2_Failed > 8))
        or ((afternight04_Pussy_dick_med_Speed_3_Success > 10) or (afternight04_Pussy_dick_med_Speed_3_Failed > 8))))

    or ((afternight04__prehfix_Pussy_dick_deep == True)
        and ((afternight04_Pussy_dick_deep_Speed_0_Failed > 4)
        or (afternight04_Pussy_dick_deep_Speed_1_Failed > 4)
        or (afternight04_Pussy_dick_deep_Speed_2_Failed > 4)
        or (afternight04_Pussy_dick_deep_Speed_3_Failed > 4)))))):

        $ debug ("Wannabe03")

        call afternight04_RapeOrNot

    # if (((afternight04__prehfix_Pussy_dick_low == True) and (mc_body.dick_speed > 0))
    #     and (((afternight04_Pussy_dick_low_Speed_1_Success > 7) or (afternight04_Pussy_dick_low_Speed_1_Failed > 4))
    #     or ((afternight04_Pussy_dick_low_Speed_2_Success > 7) or (afternight04_Pussy_dick_low_Speed_2_Failed > 4))
    #     or ((afternight04_Pussy_dick_low_Speed_3_Success > 7) or (afternight04_Pussy_dick_low_Speed_3_Failed > 4)))):

    #     $ debug ("Wannabe04")

    # if ((afternight04__prehfix_Pussy_dick_low == True) and (mc_body.dick_speed > 0)):

    #     $ debug ("Wannabe 05")

    # if mc_body.dick_speed > 0:

    #     $ debug ("Wannabe 06")

        

    ###########################
    ##########################

    return



    ###########################
    ##########################

    ###########################
    ##########################
    
    ###########################
    ##########################



label afternight04_Pussy_dick_general_pain:

    $ debug ("Here is where the dick was put down and stopped.")

    $ mc_body.store["dick"] = "Pussy_dick_med"

    $ mc_body.dick_speed = 0

    $ debug ("Now IMage.")

    call afternight04_Pussy_dick_general_image
    with vpunch

    $ debug ("Now is Off.")

    return


    ###########################
    ##########################

    ###########################
    ##########################

    ###########################
    ##########################

label afternight04_Pussy_dick_general_slowdown:

                # POINTS
            ############################################################
            ###########################################################

    $ afternight04_dick_general_Speed_3_Cond = True

            # SPEED 2
        ############################################################
        ###########################################################

    $ mc_body.dick_speed = 2
    call afternight04_Pussy_dick_general_image

            # IMAGE?
        ############################################################
        ###########################################################

    # Image is necessary?

            # DESCRIPTION
        ############################################################
        ###########################################################

## Description

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx03_a
        show afternight04_sexbattle_d_eyes 01_a
        show afternight04_sexbattle_d_pupils front01_a
        show afternight04_sexbattle_d_eyebrows serious_a
        with dissolve

    $ randomnum_1to5 = renpy.random.randint(1, 5) # SlowDown
    
    if randomnum_1to5 == 1:

        n "A pesar de tener un cuerpo atlético y de poseer una resistencia que muchos desearían, decides disminuir el ritmo."

    elif randomnum_1to5 == 2:

        n "Incluso siendo un deportista habitual, decides que lo más sabio es reducir la marcha."

    elif randomnum_1to5 == 3:

        n "Tomas la decisión de relajar un poco el compás para no agotarte antes de tiempo."

    elif randomnum_1to5 == 4:

        n "Reduces levemente la cadencia de tus caderas contra sus nalgas."

    elif randomnum_1to5 == 5:

        n "Deceleras el ritmo paulatinamente."

## Didac Reaction

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils front04_a
        show afternight04_sexbattle_d_eyebrows angryx03_a
        with dissolve

    if randomnum_1to5 == 1:

        d "Por mi no hace falta que bajes el ritmo..."

    elif randomnum_1to5 == 2:

        d "¡¿Por qué disminuyes?!"

    elif randomnum_1to5 == 3:

        d "¡Vuelve a meter ese ritmo!"

    elif randomnum_1to5 == 4:

        d "Espero que no estés parando porque sientes que te vas a correr pronto..."

    elif randomnum_1to5 == 5:

        d "¿Por qué diablos disminuyes la marcha?"

## Your thoughts

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx06_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx04_a
        with dissolve

    $ randomnum_1to5 = renpy.random.randint(1, 5) # SlowDown
    
    if randomnum_1to5 == 1:

        pt "Siempre estoy a tiempo de volver a subir el ritmo."

    elif randomnum_1to5 == 2:

        pt "Mantener este ritmo de forma indefinida no es la mejor decisión."

    elif randomnum_1to5 == 3:

        pt "Seguir a este ritmo sin límite de tiempo me agotaría antes de tiempo."

    elif randomnum_1to5 == 4:

        pt "Es bueno ir cambiando de ritmo para que note la diferencia."

    elif randomnum_1to5 == 5:

        pt "De este modo apreciará mejor cada vez que me mueva a esta velocidad."

    return


    ###########################
    ##########################

    ###########################
    ##########################
    
    ###########################
    ##########################

label afternight04_Pussy_dick_med_Fail:

    if (mc_body.store["dick"] == "Pussy_dick_med"): ##### MED 0

        if mc_body.roll_success == False:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5) # Moans med_speed_3
                #if current_pose.id == "pose_1":

            if randomnum_1to5 == 1:

                pt "Es curioso,"

                pt "hubiera jurado que le había hecho daño..."

            elif randomnum_1to5 == 2:

                pt "Pensaba que le habría hecho daño con ese grito..."

            elif randomnum_1to5 == 3:

                pt "Me da la sensación que aunque le haga daño,"

                pt "esto le encanta igual..."

            elif randomnum_1to5 == 4:

                pt "No parece que le haya hecho daño..."

            elif randomnum_1to5 == 5:

                pt "¿Entonces porque no ha gemido de placer?"

        #else:

            #p "..."

    return

    ###########################
    ##########################

    ###########################
    ##########################
    
    ###########################
    ##########################

label afternight04_Pussy_dick_condom_broken:

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
        show afternight04_sexbattle_d_eyes 06_a
        show afternight04_sexbattle_d_pupils front06_a
        show afternight04_sexbattle_d_eyebrows sadx04_a
        with dissolve

    $ randomnum_1to10 = renpy.random.randint(1, 10)
        #if current_pose.id == "pose_1":

    if randomnum_1to10 == 1:

        pt "¡¿Por qué diablos se siente tan rico ahora?!"

    elif randomnum_1to10 == 2:

        pt "¡La sensación ha mejorado un montón!"

    elif randomnum_1to10 == 3:

        pt "¡Este último condón es la hostia!"

    elif randomnum_1to10 == 4:

        pt "¡Siento como si no llevase condón!"

    elif randomnum_1to10 == 5:

        pt "¡Este último condón es una jodida pasada!"

    elif randomnum_1to10 == 6:

        pt "¿Soy yo o Dídac o el coño de Dídac se siente más rico ahora?"

    elif randomnum_1to10 == 7:

        pt "¡Joder con el último condón!"

    elif randomnum_1to10 == 8:

        pt "Será porque tengo la polla hecha mierda,"

        pt "¡pero la siento mucho más sensible!"

    elif randomnum_1to10 == 9:

        pt "¡Siento su coño mucho más a flor de piel!"

    elif randomnum_1to10 == 10:

        pt "¡¿De qué marca será este condón?!"

    return
