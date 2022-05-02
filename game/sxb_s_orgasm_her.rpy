#################################################################################
################################################################################
###############################################################################
###################################################################### HER ORGASM
default afternight04_didac_orgasms = 0 # Pose a, b and c
default afternight04_didac_orgasms_b = 0 # Pose b and c
    
label afternight04_mostly_her_orgasm:

    $ debug ("Her Orgasm 01")

    if current_pose.id == "pose_1":

        show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
        show afternight04_sexbattle_d_eyes 03_a
        show afternight04_sexbattle_d_pupils up03_a
        show afternight04_sexbattle_d_eyebrows sadx03_a
        with dissolve

    d "Ughh..."

    if current_pose.id == "pose_1":

        show afternight04_sexbattle_mc_handL empty
        
        show afternight04_sexbattle_mc_handR empty
        show afternight04_sexbattle_mc_handR_penetrate_pussy empty
        show afternight04_sexbattle_mc_handR_penetrate_anal empty
        
        show afternight04_sexbattle_mc_tongue_clitoris empty
        show afternight04_sexbattle_mc_tongue_pussy empty
        #####

        $ mc_body.dick_speed = 0

        #####

        if afternight04_condom_broken == False:

            if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

                $ mc_body.store["dick"] = "Pussy_dick_out"

                call afternight04_sexbattle_mc_dick_pussy_pose01_scene #Dick Pussy for a.

            elif (mc_body.store["right_hand"] == "Anal_Fingers" or mc_body.store["tongue"] == "Anal_tongue" or mc_body.store["dick"] == "Anal_dick_low" or mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

                $ mc_body.store["dick"] = "Anal_dick_out"

                call afternight04_sexbattle_mc_dick_anal_pose01_scene #Dick Anal for a

            if (mc_body.store["right_hand"] == "Pussy_Fingers" or mc_body.store["tongue"] == "Pussy_Tongue"):

                $ debug ("PUSSSY OUT!")

                show afternight04_sexbattle_d_legs_base wet_00_a :
                    afternight04_sexbattle_empty_NOposition

                show afternight04_sexbattle_mc_dick_pussy condom_wet_00_a:
                    afternight04_sexbattle_d_pussy_dick_out_stop_action

                # HIDING

                show afternight04_sexbattle_d_legs_pussy 02_wet_00_a:
                        afternight04_sexbattle_d_pubicpart_pos

                show afternight04_sexbattle_d_legs_over_pussy empty:
                    afternight04_sexbattle_empty_NOposition

                show afternight04_sexbattle_d_legs_stomach_pussy empty:
                    afternight04_sexbattle_empty_NOposition

                show afternight04_sexbattle_d_legs_top_pussy empty:
                        afternight04_sexbattle_d_pubicpart_pos

        if (mc_body.store["right_hand"] == "Anal_Fingers" or mc_body.store["tongue"] == "Anal_Tongue"):

            $ debug ("ANAAL OUT!")

            # HIDING

            show afternight04_sexbattle_d_legs_over_anal empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_stomach_anal empty:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_base wet_00_a:
                afternight04_sexbattle_empty_NOposition

            show afternight04_sexbattle_d_legs_top_anal empty:
                    afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_d_legs_anal 01_wet_00_a:
                    afternight04_sexbattle_d_pubicpart_pos

            show afternight04_sexbattle_mc_dick_anal condom_wet_00_a:
                #afternight04_sexbattle_empty_position # puts xanchor and yanchor to 0
                afternight04_sexbattle_d_anal_dick_out_stop_action

        $ mc_body.store["left_hand"] = ""
        $ mc_body.store["right_hand"] = ""
        $ mc_body.store["tongue"] = ""

        $ debug ("DICK AND EVERYTHING IS OUT. MADAFAKA!!")

        if afternight04_condom_broken == False:

            $ mc_body.store["dick"] = ""

    else:

        $ mc_body.dick_speed = 0

        #####
        if (mc_body.store["dick"] == "Pussy_dick_low" or mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):

            $ mc_body.store["dick"] = "Pussy_dick_out"

            call afternight04_sexbattle_mc_dick_Pussy_general_doggystyle_scene #Dick Pussy for b-c.

        elif (mc_body.store["right_hand"] == "Anal_Fingers" or mc_body.store["tongue"] == "Anal_tongue" or mc_body.store["dick"] == "Anal_dick_low" or mc_body.store["dick"] == "Anal_dick_med" or mc_body.store["dick"] == "Anal_dick_deep"):

            $ mc_body.store["dick"] = "Anal_dick_out"

            call afternight04_sexbattle_mc_dick_Anal_general_doggystyle_scene #Dick Anal for b-c.

        #####


        $ debug ("Orgasm Pose 02-03")



#####################################################################
####################################################################
################################################################### SQUIRT


    if current_pose.id == "pose_1":

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            $ debug ("001")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 001_a
                with vpunch

        elif randomnum_1to10 == 2:

            $ debug ("002")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 002_a
                with vpunch

        elif randomnum_1to10 == 3:

            $ debug ("003")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 003_a
                with vpunch

        elif randomnum_1to10 == 4:

            $ debug ("004")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 004_a
                with vpunch

        elif randomnum_1to10 == 5:

            $ debug ("005")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 005_a
                with vpunch

        elif randomnum_1to10 == 6:

            $ debug ("006")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 006_a
                with vpunch

        elif randomnum_1to10 == 7:

            $ debug ("007")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 007_a
                with vpunch

        elif randomnum_1to10 == 8:

            $ debug ("008")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 008_a
                with vpunch

        elif randomnum_1to10 == 9:

            $ debug ("009")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 009_a
                with vpunch

        elif randomnum_1to10 == 10:

            $ debug ("010")

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_didac_squirt 010_a
                with vpunch

    else:

        #if current_girl.orgasm == 1:
        if afternight04_didac_orgasms_b == 0: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 001_b
            show afternight04_sexbattle_didac_squirt_bed appearing_001_b
            with vpunch

        if afternight04_didac_orgasms_b == 1: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 002_b
            show afternight04_sexbattle_didac_squirt_bed appearing_002_b
            with vpunch

        if afternight04_didac_orgasms_b == 2: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 003_b
            show afternight04_sexbattle_didac_squirt_bed appearing_003_b
            with vpunch

        if afternight04_didac_orgasms_b == 3: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 004_b
            show afternight04_sexbattle_didac_squirt_bed appearing_004_b
            with vpunch

        if afternight04_didac_orgasms_b == 4: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 005_b
            show afternight04_sexbattle_didac_squirt_bed appearing_005_b
            with vpunch

        if afternight04_didac_orgasms_b >= 5: #Orgasms done in Pose B or C.

            show afternight04_sexbattle_didac_squirt 001_b
            show afternight04_sexbattle_didac_squirt_bed appearing_001_b
            with vpunch

#####################################################################
####################################################################
###################################################################
        

#######################

    $ randomnum_1to5 = renpy.random.randint(1, 5)

    if randomnum_1to5 == 1:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx004_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils up05_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

        d "*Gemido agudo* ¡¡AAAAmmmhhh...!!"

    elif randomnum_1to5 == 2:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows angryx01_a
            with dissolve

        d "*Gemido agudo* ¡¡AmMMMmmmmhh...!!"

    elif randomnum_1to5 == 3:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 05_a
            show afternight04_sexbattle_d_pupils up05_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

        d "*Gemido agudo* ¡¡AAaaammm...!!"

    elif randomnum_1to5 == 4:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth sad_Talkingx002_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows sadx03_a
            with dissolve

        d "*Gemido agudo* ¡¡UuuUHHH...!!"

    elif randomnum_1to5 == 5:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happy_Talkingx06_a
            show afternight04_sexbattle_d_eyes 04_a
            show afternight04_sexbattle_d_pupils up04_a
            show afternight04_sexbattle_d_eyebrows surprisex01_a
            with dissolve

        d "*Gemido agudo* ¡¡SSSSIIhhh...!!"

#####################################################################
####################################################################
################################################################### SQUIRT

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_didac_squirt 000_a

#####################################################################
####################################################################
################################################################### DICK HIDE

    $ mc_body.dick_speed = 0
    if afternight04_condom_broken == False:
        if (mc_body.store["dick"] == "Pussy_dick_med" or mc_body.store["dick"] == "Pussy_dick_deep"):
            $ mc_body.store["dick"] = "Pussy_dick_low"
        else:
            $ mc_body.store["dick"] = "Pussy_dick_out"
    #show afternight04_sexbattle_mc_dick_pussy general

    $ debug ("ALUMA")
    #if current_pose.id == "pose_1":
    call afternight04_sexbattle_mc_dick_pussy_pose01_scene #Dick Penetration for a.
    $ debug ("KALUMA")
    with dissolve

#####################################################################
####################################################################
###################################################################

    if mc_body.orgasm == 0:

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡Joder!"

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "Seeehh..."

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "¡¿Otra vez?!"

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "¡¿OTRA VEZ?!"

    if mc_body.orgasm == 1:

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡Al fin!"

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "¡Así sí!"

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡No pares!"

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡¿Otra vez?!"

    if mc_body.orgasm == 2:

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils up02_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "¡POR FIN!"

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils up03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "¡Ya tocaba!"

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils up04_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡Así me gusta!"

        elif current_girl.orgasm >= 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡No pares!"

    ######
    ##### Orgasmo de ella.

    $ debug ("Her Cum Scene")


    if mc_body.orgasm == 0:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth sad_Talkingx003_a
            show afternight04_sexbattle_d_eyes 06_a
            show afternight04_sexbattle_d_pupils front06_a
            show afternight04_sexbattle_d_eyebrows sadx04_a
            with dissolve

        d "*Suspiros* AAAaaahh... aaaahh..."

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Parece que no te ha disgustado..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "No sabes cuanto estaba esperando esto..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve
            
            

            if afternight04_Pussy_dick_med_Speed_0_Done == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                    show afternight04_sexbattle_d_eyes 04_a
                    show afternight04_sexbattle_d_pupils front04_a
                    show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                    with dissolve

                p "Y ni siquiera te la he metido dentro aún..."

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "Vas a necesitar mucho más que preliminares si quieres que me corra de nuevo."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    p "..."

                    pt "El agradecimiento no ha sido nunca su punto fuerte..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Por qué he sido yo quien se la ha metido dentro imbécil!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."



        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            p "Por lo visto ya llevas dos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "Sí..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "tú aún ninguno,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "no está mal [protname],"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "no está nada mal..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            if afternight04_Pussy_dick_med_Speed_0_Done == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows normal_a
                    with dissolve

                p "Especialmente cuando aún no te la he metido dentro."


                if afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                        with dissolve

                    d "Te gusta regocijarte,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows serious_a
                        with dissolve

                    d "¿Verdad?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows normal_a
                        with dissolve

                    p "Sí."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Eso no quita que sigo queriendo tu polla dentro de mi."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¡Por qué he sido yo quien se la ha metido dentro imbécil!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    p "..."

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Mmmmhh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "Cabrón..."

            extend " ya llevo tres..."

            d "y tú ninguno..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "¿Cuándo piensas correrte?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "Parece que realmente sí tenías ganas de correrte..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "No pares ahora."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Cabrón."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            if afternight04_Pussy_dick_med_Speed_0_Done == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sad_Talkingx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Y aún no te la he metido dentro..."

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Joder..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "¿Pero a qué diablos esperas?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "A que reconozcas que soy el puto amo en la cama."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Te reconoceré que eres el puto amo en el masaje erótico idiota,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "pero no en la cama."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Fóllame de una jodida vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Silentx01_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    p "¿Quieres que deje el masaje erótico?"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sabiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sabiting_Silentx04_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    d "¡Por qué he sido yo quien me la he metido violándote!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                        show afternight04_sexbattle_d_eyes 01_a
                        show afternight04_sexbattle_d_pupils front01_a
                        show afternight04_sexbattle_d_eyebrows angryx05_a
                        with dissolve

                    d "¡imbécil!"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sabiting_Silentx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx04_a
                        with dissolve

                    p "..."

        elif current_girl.orgasm == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx004_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "Hijo de puta..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Ya llevo cuatro..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Eso parece..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows sadx02_a
                with dissolve

            d "Tú no llevas ninguno aún..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "¡¿Es que no piensas correrte nunca?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "¿Por qué?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Ahora te preocupas por mí?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Gilipollas..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils left03_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            d "Haz lo que te de la gana..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            if afternight04_Pussy_dick_med_Speed_0_Done == 0:

                if current_pose.id == "pose_1":
                    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_a
                    show afternight04_sexbattle_d_eyes 01_a
                    show afternight04_sexbattle_d_pupils front01_a
                    show afternight04_sexbattle_d_eyebrows angryx01_a
                    with dissolve

                p "Y eso que sigo sin haberla metido dentro..."

                if afternight04_Pussy_dick_med_Speed_0_Rape_Done == 0:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "¿Y quieres una medalla..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils right04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Hostias..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils right03_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "Fóllame de una vez..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 02_a
                        show afternight04_sexbattle_d_pupils front02_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Quiero sentir tu polla dentro de mi..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows sadx03_a
                        with dissolve

                    p "..."

                else:

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx01_a
                        with dissolve

                    d "No,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                        show afternight04_sexbattle_d_eyes 04_a
                        show afternight04_sexbattle_d_pupils front04_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "pero yo sí me la he metido dentro,"

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils front05_a
                        show afternight04_sexbattle_d_eyebrows angryx03_a
                        with dissolve

                    d "ya que tú no lo hacías..."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                        show afternight04_sexbattle_d_eyes 03_a
                        show afternight04_sexbattle_d_pupils front03_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    d "Idiota."

                    if current_pose.id == "pose_1":
                        show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                        show afternight04_sexbattle_d_eyes 05_a
                        show afternight04_sexbattle_d_pupils right05_a
                        show afternight04_sexbattle_d_eyebrows angryx02_a
                        with dissolve

                    p "..."

        elif current_girl.orgasm >= 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx001_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils up05_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            d "¡Caa-"

            extend "bróoon...!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

            d "*Mmmhh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx01_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Yaah..."

            extend " he perdidoo..."

            extend " la putaah cuentaah..."

            extend " de cuantoos llevoo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows sadx03_a
                with dissolve

            d "¡¿Cuandoo piensaas..."

            extend " correrte túu...?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx002_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Puutoo sementaal..."

            extend " de mierdaa..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx06_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx04_a
                with dissolve

    if mc_body.orgasm == 1:

        if current_pose.id == "pose_1":
            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows sadx04_a
            with dissolve

        d "Uff..."

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Parece que te has corrido..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "Ya era hora..."

            d "¿Siempre eres el primero en correrte cuando quedas con las fulanas que te ligas?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Yo no me voy a la cama con la primera borracha que pillo como tú..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Pensaba que eras mejor semental..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            p "Solo llevo uno."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "pero estás más cerca del segundo que yo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "Puto Dídac..."

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Tu segunda vez..."

            extend " y yo solo llevo uno,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            p "no te quejarás..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "Espero que aguantes algunas rondas más..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "No llevo esperando todo el puto día para que solo tener dos o tres orgasmos de pacotilla..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            pt "Jodido Dídac..."

        elif current_girl.orgasm == 3:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            p "Ya llevas tres..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "Y espero tener bastantes más..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "Puto Dídac..."

        elif current_girl.orgasm == 4:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "Tu cuarto orgasmo,"

            extend " no te quejarás..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "Y tú solo uno,"

            d "no está mal [protname],"

            extend " no está nada mal..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

        elif current_girl.orgasm >= 5:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "Joder..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Solo llevas una corrida y yo he perdido la cuenta de los que he tenido ya..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "Esto no ha hecho más que empezar..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "Esa es la actitud..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

    if mc_body.orgasm == 2:

        if current_pose.id == "pose_1":

            show afternight04_sexbattle_d_mouth happy_Talkingx01_a
            show afternight04_sexbattle_d_eyes 07_a
            show afternight04_sexbattle_d_pupils front07_a
            show afternight04_sexbattle_d_eyebrows sadx02_a
            with dissolve

        d "Ufff..."

        if current_girl.orgasm == 1:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Esto ya es otra cosa..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 00_a
                show afternight04_sexbattle_d_pupils front00_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "Veo que te has corrido..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 01_a
                show afternight04_sexbattle_d_pupils front01_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡¿YA ERA PUTA HORA NO CREES?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Que tú ya llevas dos y vas por el tercero!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡Espero que aguantes bastante más!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            pt "Mejor no le digo que seguramente esta será mi última corrida o me mata..."

        elif current_girl.orgasm == 2:

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 06_a
                show afternight04_sexbattle_d_pupils front06_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Mmmhh..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx02_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            p "Ya llevas dos..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Igual que tú."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Imbécil!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "No me vengas que te vas a correr ya,"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡O te la corto!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx06_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils right03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡Voy a necesitar mucho más que esto!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx07_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¡¿Queda claro?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            pt "Puto Dídac..."

        elif current_girl.orgasm == 3:

            p "Sino llevo mal la cuenta,"

            extend " ya llevas tres."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows suspiciousx02_a
                with dissolve

            d "¿Y qué...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¿Te sientes orgulloso?"

            d "¿Te doy una medalla?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx03_a
                with dissolve

            d "¿O qué?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            p "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿Tú te crees que me voy a conformar con tres míseros orgasmos?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx04_a
                show afternight04_sexbattle_d_eyes 02_a
                show afternight04_sexbattle_d_pupils front02_a
                show afternight04_sexbattle_d_eyebrows surprisex02_a
                with dissolve

            p "Ya llevas más que yo..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            d "Y luego el experto en tías eres tú..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Silentx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils right04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            p "¿Euh...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Ni se te ocurra terminar aún."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx04_a
                show afternight04_sexbattle_d_eyes 03_a
                show afternight04_sexbattle_d_pupils front03_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve


            d "¡Como no me corra como mínimo otra vez más te quedas sin polla!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx02_a
                with dissolve

            d "¡¿Me explico?!"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            pt "Que manía tiene en cortarme la polla..."

        elif current_girl.orgasm == 4:

            p "Ya me llevas el doble de ventaja..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sadbiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils right05_a
                show afternight04_sexbattle_d_eyebrows surprisex01_a
                with dissolve

            d "¿Y qué...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth sad_Talkingx003_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows suspiciousx01_a
                with dissolve

            d "¿Te vas a rendir ya...?"

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows angryx01_a
                with dissolve

            d "Te tenía por mejor semental [protname]..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx03_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

            pt "El muy hijo de mil padres sabe como provocarme..."

        elif current_girl.orgasm >= 5:

            p "Ya llevas otro..."

            p "Y yo aún no he terminado."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx04_a
                show afternight04_sexbattle_d_eyes 07_a
                show afternight04_sexbattle_d_pupils front07_a
                show afternight04_sexbattle_d_eyebrows sadx01_a
                with dissolve

            d "Je..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happy_Talkingx05_a
                show afternight04_sexbattle_d_eyes 04_a
                show afternight04_sexbattle_d_pupils front04_a
                show afternight04_sexbattle_d_eyebrows normal_a
                with dissolve

            d "Calla y no pares..."

            if current_pose.id == "pose_1":
                show afternight04_sexbattle_d_mouth happybiting_Silentx05_a
                show afternight04_sexbattle_d_eyes 05_a
                show afternight04_sexbattle_d_pupils front05_a
                show afternight04_sexbattle_d_eyebrows serious_a
                with dissolve

    # To know how many orgasms she had.
    $ afternight04_didac_orgasms += 1

    if not current_pose.id == "pose_1": #Orgasm in pose02

        $ afternight04_didac_orgasms_b += 1

    #He has no more orgasms... In theory...

    return