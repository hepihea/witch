
default ped_vel_number = 0

default ped_D_NoSex_times = 0

default ped_sex_blow_MChand = "off"
default ped_sex_general_zoom_Cond = ""
default ped_sex_general_expression_Cond = "talk"
default ped_sex_general_action_Cond = "talk" ## vdcum01 Didac Cum while having your dick in Vagina. #vcum = MC Vaginal Cum
default ped_sex_general_action_b_Cond = "" #sdcum01 =  Self Didac Cum 01

default ped_sex_general_69_cover = "over"
default ped_sex_num = 1
default ped_sex_b_num = 1

default p_characters_action = ""

#default p_didac_cunnilingus_done_to_p_didac = 0
#default p_didac_cunnilingus_received_from_p_prot_at_69 = 0

default p_txell_cunnilingus_received_from_p_didac_at_missionary_TRY = False
default p_txell_cunnilingus_received_from_p_didac_at_missionary = 0

#default p_prot_anilingus_done_to_p_didac = 0 # "Protagonista haciéndole un anilingus a Dídac."

#default p_didac_buttocks_pain_received_from_p_prot = 0

default p_prot_blowjobDeep_received_TRY_withDidac = 0

default p_prot_kiss_p_didac_FAIL = 0

default p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond = False

default p_prot_anal_fingered_received_from_p_txell = 0

default p_didac_blowjob_done_ACCEPTED = False


default p_didac_butSlap_rec_R = 0
default p_d_butS_R = 0
default p_d_butS_L = 0

default takeDickOut_Cond = 0
default takeDickOut_d_Total = 0
default takeDickOut_m_Total = 0
default takeDickOut_n_Total = 0


default p_didac_vaginal_pain_received_relax_times = 0
default p_didac_anal_pain_received_relax_times = 0

default p_didac_takeDickOut_attempt = 0
default p_didac_takeDickOut_againIn = 0

label afternight05_Pedrera_Sex_p_didac_oral:

    $ ped_sex_general_expression_Cond = "talk"

    call pedrera_sex_p_general_talk

    $ debug ("Oral Sex with Didac.")

    if p_prot.action == "masturbate":

        $ debug ("Protagonist masturbate")

        $ p_prot.masturbate += 1

        if p_prot.masturbate == 1:

            show gensex_oral_d_frontHead_exp_blush 02
            show gensex_oral_d_frontHead_exp_eyes 03
            show gensex_oral_d_frontHead_exp_iris down03
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with Dissolve(0.5)

            n "Acaricias tu erecto miembro con tu mano a escasos centímetros del rostro de Dídac."

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "..."

            if p_prot_NotJustMasturbate_with_p_didac:

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¿Ahora te da por masturbarte?"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx01
                with dissolve

                d "¿Después de lo que ya me has hecho?"

            else:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                d "¿En serio?"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                with dissolve

                d "¿No se te ocurre otra manera de pasar un buen rato?"

                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "Ya hablas como una fulana barata..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "..."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                d "Serás capullo..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris right05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

        elif p_prot.masturbate == 2:

            if p_didac.vaginal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡¿Para eso la has sacado?!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡¿Para ponerte a masturbarte?!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

            else:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¡¿En serio te vas a pasar todo el rato así?!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 08
            show gensex_oral_d_frontHead_exp_iris front08
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
            show gensex_oral_d_frontHead_exp_eyebrows angryx05
            with dissolve

            d "Puto [protname]..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris right05
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

        elif p_prot.masturbate == 3:

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "Si sigues así,"

            extend " no tendrás tiempo de hacerme nada más."

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris front01
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows surprisex01
            with dissolve

            p "Esa es la idea."

            if p_didac.vaginal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡Pero si ya me la has metido por el coño!"

            elif p_didac.anal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡Pero si ya me la has metido por el culo!"

            if p_didac.blowjob_done > 0:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡¿Para eso me la has hecho chupar antes?!"

            if p_prot_NotJustMasturbate_with_p_didac == False:

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "Gilipollas..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris right05
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

        elif p_prot.masturbate == 4:

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            d "¿Acaso no ves lo húmeda que estoy?"

            if p_didac.vaginal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx006
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¿Por qué no me la vuelves a meter?"

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris right05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

        elif p_prot.masturbate == 5:

            if p_didac.vaginal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx03
                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                with dissolve

                d "La quiero volver a sentir dentro..."

                if p_didac.blowjob_done > 0:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡Pero no de mi boca!"

            if p_prot_NotJustMasturbate_with_p_didac == False:

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "..."

        elif p_prot.masturbate >= 6:

            $ ped_check_1_10("ped_masturbate_didac_list")

            if ped_check_list_result == 1:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "¿Tan asexual eres que prefieres masturbarte a follar?"

            elif ped_check_list_result == 2:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "Que te guste más tu estúpida mano,"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                with dissolve

                d "que un coño húmedo,"

                extend " caliente,"

                extend " y jugoso..."

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡Dice mucho de lo jodidamente mal que estás!"

            elif ped_check_list_result == 3:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

                d "Y sigues dándole a la manivela..."

            elif ped_check_list_result == 4:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "¡¿Eres gay o algo?!"

            elif ped_check_list_result == 5:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx006
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "Casi preferiría que me follaras el culo antes que esto..."

            elif ped_check_list_result == 6:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                d "¿De pequeño te caíste en una ermita,"

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "o qué puto problema tienes?"

            elif ped_check_list_result == 7:

                if DidacPregnant:

                    if DidacMCPregnant:

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx02
                        with dissolve

                        d "Ya me has dejado preñada..."

                    else:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows sadx02
                        with dissolve

                        d "De todos modos ya estoy preñada..."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    if p_didac.vaginal_received == 0:

                        if afternight04_Pussy_dick_med_Speed_0_Success > 0:

                            d "¡¿Qué mas da que me la vuelvas a meter ahora?!"

                            show gensex_oral_d_frontHead_exp_eyes 04
                            show gensex_oral_d_frontHead_exp_iris front04
                            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                            show gensex_oral_d_frontHead_exp_eyebrows angryx05
                            with dissolve

                            d "¡Si ya me la metiste ayer por la noche!"

                        else:

                            d "¡¿Qué más da si me la metes ahora?!"

                    else:

                        d "¡¿Qué más da si me la vuelves a meter de nuevo?!"

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    p "..."

                if DidacSex_Vaginal:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "¿Qué te cuesta volver a metérmela?"

                else:

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows sadx04
                    with dissolve

                    d "Me gustaría sentirla dentro..."

            elif ped_check_list_result == 8:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Hay que ser cutre para estar masturbándose enfrente de una tía que te pide sexo."

            elif ped_check_list_result == 9:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "Tssk..."

            elif ped_check_list_result == 10:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris down04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                with dissolve

                d "..."

            else:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris down04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                with dissolve

                d "..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris right05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

    #elif p_prot.action == "rest":
    elif p_prot.action in ["rest", "takeDickOut"]:

        if p_prot.b_action in ["takeDickOut"] or p_prot.action in ["takeDickOut", "takeTongueOut"]:
            call p_didac_notReceiveBlowjob
        else:

            ## 69 res here is IMPOSSIBLE.

            # if p_prot.pos == "oral":
            #     if p_prot.pos_oral_rest == 0:
            #         $ p_prot.pos_oral_rest += 1
            # elif p_prot.pos == "69":
            #     if p_prot.pos_69_rest == 0:
            #         $ p_prot.pos_69_rest += 1

            if p_prot.pos in ["oral", "69"]:
                $ ped_sex_general_expression_Cond = "talk"
                if p_prot.pos == "oral":
                    $ ped_sex_general_action_Cond = "o00_00"
                # elif p_prot.pos == "69":
                #     $ ped_sex_general_action_Cond = "o00_00" # Is this the correct one?
                call pedrera_sex_p_general_talk

            if p_prot.pos_oral_rest == 0:

                call afternight05_Pedrera_Sex_NakeYou

                if afternight04__MMouth_dick_Success > 0 or p_didac.blowjob_done > 0:

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris down03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    d "Pero,"

                    extend " en serio..."

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "¿Tengo que volver a metérmela en la boca?"

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    if p_didac.blowjob_done > 0:

                        d "¡¿No te la he chupado suficiente ya?!"

                    elif aftermorning05_Deepsea_Blowjob_Cond:

                        d "¡¿No has tenido suficiente esta mañana?!"

                    elif afternight04__MMouth_dick_Success > 0:

                        d "¡¿No tuviste suficiente ayer por la noche?!"


                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                p "Es evidente que no."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡¿De verdad no prefieres follarme?!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                menu:

                    pt "¿Qué prefiero?"

                    "Si quedo satisfecho, quizás lo haga después.":
                        call p_Help

                        $pl.ch_pts("dp", -1)

                        show gensex_oral_d_frontHead_exp_eyes 01
                        show gensex_oral_d_frontHead_exp_iris front01
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        d "¡¿Si quedas satisfecho?"

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                        d "¡¿Qué mierda de respuesta es esta?!"

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    "Ya he dicho que solo quiero hacerlo con [neusname]." if afternight05_Pedrera_Sex_SaidJustWithNeus:
                        call p_Help

                        $ afternight05_Pedrera_Sex_SaidJustWithNeusx02 = True

                        $pl.ch_pts("dp",-1)
                        $pl.ch_pts("np",1)

                        show gensex_oral_d_frontHead_exp_eyes 00
                        show gensex_oral_d_frontHead_exp_iris front00
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        d "..."

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                        show gensex_oral_d_frontHead_exp_eyebrows angryx03
                        with dissolve

                        d "¡¿En serio?!"

                        #if p_didac.vaginal_received > 0 or p_didac.anal_received > 0 or p_didac.cunnilingus_received > 0 or p_didac.anilingus_received > 0:
                        if p_prot_NotJustMasturbate_with_p_didac == True:

                            show gensex_oral_d_frontHead_exp_eyes 01
                            show gensex_oral_d_frontHead_exp_iris front01
                            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                            show gensex_oral_d_frontHead_exp_eyebrows angryx04
                            with dissolve

                            if p_didac.vaginal_received > 0:

                                d "¡Pero si ya me has follado!"

                                if p_didac.vaginal_received > 1:

                                    show gensex_oral_d_frontHead_exp_eyes 03
                                    show gensex_oral_d_frontHead_exp_iris front03
                                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                                    with dissolve

                                    d "¡Hasta [p_didac.vaginal_received] veces me la has metido!"

                            elif p_didac.anal_received > 0:

                                d "¡Pero si me la has metido por el culo!"

                            elif p_didac.cunnilingus_received > 0:

                                d "¡Pero si me has comido el coño!"

                            elif p_didac.anilingus_received > 0:

                                d "¡Pero si me has comido el culo!"

                            show gensex_oral_d_frontHead_exp_eyes 04
                            show gensex_oral_d_frontHead_exp_iris front04
                            show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                            show gensex_oral_d_frontHead_exp_eyebrows angryx04
                            with dissolve

                            p "..."

                        elif p_prot_NotJustMasturbate_with_p_txell:

                            if p_txell.blowjobDeep_done > 0:

                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris front04
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                                with dissolve

                                d "¡Pero si a la rubia esta se la has metido en la garganta entera!"

                                show gensex_oral_d_frontHead_exp_eyes 05
                                show gensex_oral_d_frontHead_exp_iris front05
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                                with dissolve

                                p "..."

                                show gensex_oral_d_frontHead_exp_eyes 01
                                show gensex_oral_d_frontHead_exp_iris front01
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_d_frontHead_exp_eyebrows serious
                                with dissolve

                                tx "Por favor..."

                                show gensex_oral_d_frontHead_exp_eyes 02
                                show gensex_oral_d_frontHead_exp_iris right02
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "No quieras compararte conmigo, {a=https://es.wikipedia.org/wiki/Pueblo_troglodita}troglodita{/a};"

                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris right04
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                                with dissolve

                                d "¡¿A quien llamas troglodita?!"

                                show gensex_oral_d_frontHead_exp_eyes 05
                                show gensex_oral_d_frontHead_exp_iris right05
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx13
                                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                                show m_exp_mouth sad_Talkingx04
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows surprisex01
                                with fade_short

                                tx "Nunca he considerado que ser femenina sea un requisito indispensable para ser una mujer,"

                                show m_exp_mouth sad_Talkingx05
                                show m_exp_eyes 02
                                show m_exp_piris front02
                                show m_exp_eyebrows sadx02
                                with dissolve

                                tx "pero es que en tu caso..."

                                show m_exp_mouth happy_Talkingx07
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                show m_exp_eyebrows sadx03
                                with dissolve

                                tx "Es tan obvio que sigues pensando más en tu pajarito inexistente,"

                                extend " que con otra cosa."

                                show m_exp_mouth happy_Silentx07
                                show m_exp_eyes 05
                                show m_exp_piris front05
                                show m_exp_eyebrows sadx04
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_d_frontHead_exp_eyes 02
                                show gensex_oral_d_frontHead_exp_iris right02
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                                with fade_short

                                d "¡¿Pajarito inexistente?!"

                                show gensex_oral_d_frontHead_exp_eyes 03
                                show gensex_oral_d_frontHead_exp_iris right03
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                                with dissolve

                                d "¡¿De qué coño estás hablando pija de mierda?!"

                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris right04
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx14
                                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                                show m_exp_mouth sad_Talkingx04
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows surprisex01
                                with fade_short

                                tx "Pues de esto,"

                                extend " precisamente;"

                                show m_exp_mouth sad_Talkingx03
                                show m_exp_eyes 02
                                show m_exp_piris front02
                                show m_exp_eyebrows serious
                                with dissolve

                                tx "Aunque hayas perdido ese aspecto de armario con músculos,"

                                show m_exp_mouth happy_Talkingx08
                                show m_exp_eyes 03
                                show m_exp_piris front03
                                show m_exp_eyebrows sadx03
                                with dissolve

                                tx "{a=https://es.wikipedia.org/wiki/Homer_Simpson}Homer Simpson{/a} sigue resultando más seductor que tú."

                                show m_exp_mouth happy_Silentx07
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                show m_exp_eyebrows angryx01
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_d_frontHead_exp_eyes 02
                                show gensex_oral_d_frontHead_exp_iris right02
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                                with fade_short

                                d "¡Atrévete a decírmelo a la cara, maldita zorra!"

                                show gensex_oral_d_frontHead_exp_eyes 01
                                show gensex_oral_d_frontHead_exp_iris right01
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                                with dissolve

                                tx "Ahora mismo, la zorra que tiene algo delante de la cara,"

                                extend " no soy yo..."

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris down00
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                                with dissolve

                                d "..."

                                show gensex_oral_d_frontHead_exp_eyes 01
                                show gensex_oral_d_frontHead_exp_iris right01
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                                with dissolve

                                d "¡TE VOY A...!"

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris right00
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                                with hpunch

                                d "¡Ugh...!"

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris down00
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                d "¿Uh...?"

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris left00
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                                with dissolve

                                ne "¡BASTA!"

                                $ Pedrera_char_Cond = "NeusClose_show"
                                call Pedrera_char_lab

                                show neus_exp_mouth sadbiting_Silentx04
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris front04
                                show neus_exp_eyebrows angryx04
                                with fade_short

                                pt "[neusname]..."

                                show neus_exp_mouth sad_Talkingx09
                                $ nteye = 1
                                call neus_exp_tears_tears
                                show neus_exp_iris front01
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                ne "¡Os recuerdo que esto no es ninguna broma y que la noche tiene las horas contadas!"

                                show neus_exp_mouth sad_Talkingx08
                                $ nteye = 2
                                call neus_exp_tears_tears
                                show neus_exp_iris front02
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                ne "¡Así que no voy a tolerar ninguna estupidez más!"

                                show neus_exp_mouth sad_Silentx11
                                $ nteye = 8
                                call neus_exp_tears_tears
                                show neus_exp_iris front08
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                d "¡Pero si...!"

                                show neus_exp_mouth sad_Talkingx11
                                $ nteye = 0
                                call neus_exp_tears_tears
                                show neus_exp_iris front00_bright
                                show neus_exp_eyebrows angryx05
                                with vpunch

                                ne "¡SILENCIO!"

                                show neus_exp_mouth sad_Silentx10
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris front04_bright
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_d_frontHead_exp_eyes 07
                                show gensex_oral_d_frontHead_exp_iris front07
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                                with fade_short

                                d "¡Ughh...!"

                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris down04
                                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                                show gensex_oral_d_frontHead_exp_eyebrows sadx05
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "NeusClose_show"
                                call Pedrera_char_lab

                                show neus_exp_mouth sad_Talkingx06
                                $ nteye = 3
                                call neus_exp_tears_tears
                                show neus_exp_iris right03_bright
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                ne "Txell."

                                show neus_exp_mouth sad_Silentx05
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris right04_bright
                                show neus_exp_eyebrows angryx05
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "TxellClose_b_show"
                                call Pedrera_char_lab

                                show m_exp_mouth sad_Talkingx004
                                show m_exp_eyes 00
                                show m_exp_piris left00
                                show m_exp_eyebrows surprisex01
                                with fade_short

                                tx "¡¿Sí?!"

                                show m_exp_mouth sadbiting_Silentx02
                                show m_exp_eyes 01
                                show m_exp_piris left01
                                show m_exp_eyebrows sadx02
                                with dissolve

                                ne "No le provoques más."

                                show m_exp_mouth sadbiting_Silentx04
                                show m_exp_eyes 04
                                show m_exp_piris left04
                                show m_exp_eyebrows sadx03
                                with dissolve

                                tx "..."

                                show m_exp_mouth sad_Talkingx05
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows sadx04
                                with dissolve

                                tx "Lo siento..."

                                show m_exp_mouth sadbiting_Silentx07
                                show m_exp_eyes 06
                                show m_exp_piris front06
                                show m_exp_eyebrows sadx05
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris up00
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx007
                                show gensex_oral_d_frontHead_exp_eyebrows sadx02
                                with fade_short

                                d "Ahhh..."

                                show gensex_oral_d_frontHead_exp_eyes 07
                                show gensex_oral_d_frontHead_exp_iris front07
                                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                                with dissolve

                                d "¡Casi me quedo sin respiración!"

                                show gensex_oral_d_frontHead_exp_eyes 00
                                show gensex_oral_d_frontHead_exp_iris left00
                                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                                with dissolve

                                ne "Pues asegúrate de que no se repita."

                                show gensex_oral_d_frontHead_exp_eyes 04
                                show gensex_oral_d_frontHead_exp_iris left04
                                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                                with dissolve

                                d "..."

                                show gensex_oral_d_frontHead_exp_eyes 05
                                show gensex_oral_d_frontHead_exp_iris right05
                                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_d_frontHead_exp_eyebrows sadx05
                                with dissolve

                                pt "Desde luego,"

                                extend " cuando se cabrea..."

                                pt "da un poco de {a=https://es.wikipedia.org/wiki/Yuyu_(magia)}yuyu{/a}..."

                            elif p_txell.blowjob_done > 0:

                                aj "Does this one exist? ERROR 4983"

                            else:

                                ## FOR_FUTURE

                                aj "ERROR 29894 What does here?"

                        show gensex_oral_d_frontHead_exp_eyes 03
                        show gensex_oral_d_frontHead_exp_iris front03
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                    "...":
                        call p_Help

                p "No te quejes tanto."

                if afternight05_Pedrera_Sex_SaidJustWithNeusx02 == False:

                    if p_didac.vaginal_received == 0:

                        show gensex_oral_d_frontHead_exp_eyes 00
                        show gensex_oral_d_frontHead_exp_iris front00
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        p "De este modo quizás te vayas calentando para que luego estés bien dilatada ahí abajo."

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx03
                        with dissolve

                        d "¡¿Te crees que no voy suficientemente mojada?!"

                        call ped_D_NoSex

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx03
                        with dissolve

                        p "Venga..."

                    if afternight04__MMouth_dick_Success > 0:

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        p "Cualquiera diría que te disgustó tanto ayer,"

                        show gensex_oral_d_frontHead_exp_blush 04

                        show gensex_oral_d_frontHead_exp_eyes 00
                        show gensex_oral_d_frontHead_exp_iris front00
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        if afternight04__MMouth_dick_Deep_Success > 0:

                            p "Si hasta te la metí entera por la garganta sin que te me quejaras..."

                        elif aftermorning05_Deepsea_Blowjob_Cond:

                            p "si hoy en la playa me la has vuelto a comer entera."

                        show gensex_oral_d_frontHead_exp_blush 05

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Tssk..."

                if afternight05_Pedrera_Sex_SaidJustWithNeusx02:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "No quiero que te corras en mi boca."

                else:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "Por lo menos no te corras."

                    if afternight04_CumInMouth > 0 or afternight04_CumInThroat > 0:

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                        d "No quiero volver a saborear tu maldito esperma."

                        if afternight04_CumInThroat > 0 and afternight04_CumInMouth == 0:

                            show gensex_oral_d_frontHead_exp_eyes 05
                            show gensex_oral_d_frontHead_exp_iris right05
                            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                            show gensex_oral_d_frontHead_exp_eyebrows angryx04
                            with dissolve

                            pt "¿Llegó a saborearlo?"

                            pt "Después de todo me corrí directamente en su garganta..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                d "Además,"

                extend " me gusta más sentirlo calentito dentro de mi;"

                if afternight04_Anal_dick_med_Speed_1_Success > 0:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris right04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    d "aunque sea por detrás..."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx01
                with dissolve


            elif p_prot.pos_oral_rest == 1:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                p "¿A qué estás esperando?"

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "Si te crees que me la voy a meter en la boca yo misma,"

                extend " puedes esperar sentado."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

            elif p_prot.pos_oral_rest == 2:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "Si no quieres que te la chupe,"

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                if afternight04_Anal_dick_med_Speed_1_Success > 0:

                    d "estaría encantada de metérmela en otro sitio."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "Pero decídete."

                else:

                    d "ya sabes dónde me la tienes que meter..."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris left04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                d "Aparentemente,"

                extend " tampoco tenemos toda la noche."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

            elif p_prot.pos_oral_rest >= 3: #or p_prot.pos_69_rest > 1: # 69 here is not possible

                $ ped_check_1_10("ped_oral_rest_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    d "Que estés ahí delante sin hacer nada,"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "¡me está poniendo de los nervios!"

                elif ped_check_list_result == 2:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "¿¡Vas a estar toda la noche así?!"

                elif ped_check_list_result == 3:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_d_frontHead_exp_eyebrows sadx01
                    with dissolve

                    d "¿Tan poco te atrae mi coño?"

                elif ped_check_list_result == 4:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "¡Casi preferiría hacer un sesenta y nueve si vas a estar todo el rato así!"

                elif ped_check_list_result == 5:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Si no me vas a follar,"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "al menos mastúrbate,"

                    extend " imbécil."

                elif ped_check_list_result == 6:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Te juro que si tuviera mi cuerpo de hace tres días,"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "ahora mismo te estaría metiendo de hostias..."

                elif ped_check_list_result == 7:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡Fóllame de una vez!"

                elif ped_check_list_result == 8:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "Me estás poniendo de mala leche..."

                elif ped_check_list_result == 9:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Tssk..."

                elif ped_check_list_result == 10:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    d "..."

                else:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    d "..."

            if p_prot.pos_oral_rest > 0:

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve
            
            call afternight05_Pedrera_Neus_Warning

    elif p_prot.action == "masturbate":

        $ p_prot.masturbate += 1

        $ p_prot.pleasure += 4
        $ p_prot.pleasure += 6

        $ debug ("You masturbate in front of Didac.")

        $ p_prot_masturbate_infrontof_didac += 1

        if p_prot_masturbate_infrontof_didac == 1:

            d "..."

            n "Con tu mano derecha acaricias tu longevo miembro."

            d "¿Se puede saber qué coño haces?"

            p "¿No es obvio?"

            d "..."

            p "¿O prefieres metértela en la boca?"

            d "¡No digas gilipolleces!"

            d "¡¿Es que piensas correrte así?!"

            d "¿¡Masturbándote?!"

            menu:

                "Es posible, ya veremos.":
                    call p_Help

                    $pl.ch_pts("dp",-1)

                    d "..."

                "Como ya le he dicho a Txell antes, esta noche solo quiero hacerlo con Neus." if p_prot_masturbate_infrontof_txell_ONLYNEUS_Cond == True and p_prot.vaginal_done == 0 and p_prot.anal_done == 0:
                    
                    call p_Help

                    $ p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond = True

                    $pl.ch_pts("dp",-3)
                    $pl.ch_pts("np",4)
                    $pl.ch_pts("mp",2)

                    call onlyWantNeus_with_p_didac
                        # d "..."
                        # ne "¿Euh...?"
                        # ne "[protname]..."
                        # ne "¿E-"
                        # extend "estás seguro?..."

                "Sí, esta noche solo quiero hacerlo con Neus." if p_prot_masturbate_infrontof_txell_ONLYNEUS_Cond == False and p_prot.vaginal_done == 0 and p_prot.anal_done == 0:
                    call p_Help

                    $ p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond = True

                    $pl.ch_pts("dp",-3)
                    $pl.ch_pts("np",3)
                    $pl.ch_pts("mp",1)

                    call onlyWantNeus_with_p_didac
                        # d "..."
                        # ne "¿Euh...?"
                        # ne "[protname]..."
                        # ne "¿E-"
                        # extend "estás seguro?..."

                d "Tsssk..."

        elif p_prot_masturbate_infrontof_didac == 2:

            d "..."

            d "¿Te piensas pasar todo el rato masturbándote?"

            if p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond:

                p "¿No te lo he dejado claro antes?"

                if p_prot_NotJustMasturbate_with_p_didac:

                    if p_didac.blowjob_done > 0:

                        d "¡Pero si igualmente ya me la has metido por la boca!"

                    else:

                        aj "This message shouldn't appear 49738748"

            else:

                p "Ya te he dicho que depende..."

                d "¡¿Depende de qué?!"

                p "De como me pique."

            d "..."

        elif p_prot_masturbate_infrontof_didac == 3:

            if p_prot.vaginal_done == 0:

                d "No me la vas a meter,"

            else:

                d "No me la vas a volver a meter,"

            extend " ¿Verdad?"

        elif p_prot_masturbate_infrontof_didac == 4:

            d "¿Significa esto que te me vas a correr en la boca?"

            d "¡¿En serio?!"

            if DidacPregnant:

                if p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond:

                    p "Sí."

                else:

                    p "Es posible."

            else:

                p "Mejor eso que una broma de nueve meses que te deje como mujer permanentemente,"

                extend " ¿No crees?"

            d "..."

        elif p_prot_masturbate_infrontof_didac == 5:

            d "Eres un capullo..."

            p "Y tú una cachonda mental."

            d "..."

        elif p_prot_masturbate_infrontof_didac >= 6:

            d "..."

    ###############
###############

    elif p_prot.action in ["titwank_received_TRY", "titwank_received"]:

        #$ debug ("You receive a Tit Wank from Didac.")

        $ p_didac.action = "titwank_done"
        $ p_prot.action = "titwank_received"
        $ p_didac.titwank_done += 1
        $ p_prot.titwank_received += 1

        if p_didac.titwank_done > 1:

            if p_didac.titwank_done > 5:
                $ ped_sex_general_action_Cond = "ob01_01"
            if p_didac.titwank_done > 4:
                $ ped_sex_general_action_Cond = "ob01_02"
            elif p_didac.titwank_done > 3:
                $ ped_sex_general_action_Cond = "ob01_02"
            elif p_didac.titwank_done > 2:
                $ ped_sex_general_action_Cond = "ob01_03"
            elif p_didac.titwank_done > 1:
                $ ped_sex_general_action_Cond = "ob01_04"
            else:
                $ ped_sex_general_action_Cond = "ob00_00"

            if p_didac.titwank_done > 3:
                $ ped_sex_general_expression_Cond = "lustAngry"
            else:
                $ ped_sex_general_expression_Cond = "veryAngry"
            call pedrera_sex_p_general_talk
            with dissolve

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if p_didac.titwank_done > 3:

                if randomnum_1to5 == 1:
                    d "Hmmm..."
                elif randomnum_1to5 == 2:
                    d "Mmmn..."
                elif randomnum_1to5 == 3:
                    d "Uhhmm..."
                elif randomnum_1to5 == 4:
                    d "Ggghnn..."
                elif randomnum_1to5 == 5:
                    d "..."

            else:

                if randomnum_1to5 == 1:
                    d "Pff..."
                elif randomnum_1to5 == 2:
                    d "Tssk..."
                elif randomnum_1to5 == 3:
                    d "Grrghnt..."
                elif randomnum_1to5 == 4:
                    d "Humm..."
                elif randomnum_1to5 == 5:
                    d "..."

            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "ob00_00b"
            call pedrera_sex_p_general_talk

        if p_didac.titwank_done == 1:

            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "ob00_00"
            call pedrera_sex_p_general_talk

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils down02
            show didacf_eyebrows surprisex02
            with fade

            n "Lentamente te acercas a la cama y reposas tu espalda sobre ella"

            show didacf_mouth sadbiting_Silentx05
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils front04
            show didacf_eyebrows suspiciousx02
            with dissolve

            n "invitando a Dídac a cercarse."

            show didacf_mouth sad_Talkingx07
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows angryx03
            with dissolve

            d "¿Qué demonios haces?"

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex01
            with dissolve

            p "Acércate."

            show didacf_mouth sadbiting_Silentx03
            $ dteye = 8
            call didac_exp_tears_tears
            show didacf_pupils front08
            show didacf_eyebrows angryx03
            with dissolve

            pause 0.2

            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "ob00_00" # CORRECT ONE
            call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris down05
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with fade

            n "Con cierta duda, se acerca hasta ti."

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            n "Sugerentemente, le acercas tu miembro a sus pechos"

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris down02
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx02
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            n "mientras los acaricias suavemente con tus manos."

            show gensex_oral_d_frontHead_exp_eyes 03
            show gensex_oral_d_frontHead_exp_iris front03
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "¿Qué demonios estás haciendo?"

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows surprisex01
            with dissolve

            p "Me apetece probar algo distinto con estos recientes pechos tuyos."

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris down04
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 08
            show gensex_oral_d_frontHead_exp_iris front08
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

            d "¡¿Quieres que te haga una {a=https://es.wikipedia.org/wiki/Masturbación_con_las_mamas}cubana{/a}?!"

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris front01
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            p "Chica lista."

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "¡¿Por qué demonios no prefieres follarme?!"

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris front01
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            d "¡¿Acaso te caíste de pequeño o algo?!"

            if p_didac.vaginal_received > 0 or p_didac.anal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "Pero si ya te la he metido."

                if p_didac.vaginal_received > 0:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡No lo suficiente!"

                elif p_didac.anal_received > 0:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡Por detrás!"

            call ped_D_NoSex ##########################################

            show gensex_oral_d_frontHead_exp_eyes 00
            show gensex_oral_d_frontHead_exp_iris front00
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            p "¿Nunca te han hecho una cubana?"

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "Sí..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
            with dissolve

            d "¡¿Pero eso qué tiene que ver?!"

            show gensex_oral_d_frontHead_exp_eyes 00
            show gensex_oral_d_frontHead_exp_iris front00
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            p "Pues que me apetece probar el suave tacto de tus pechos sobre sobre mi polla."

            show gensex_oral_d_frontHead_exp_blush 03
            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris down01
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "¡Pero si ya la tienes dura!"

            show gensex_oral_d_frontHead_exp_blush 04
            show gensex_oral_d_frontHead_exp_eyes 00
            show gensex_oral_d_frontHead_exp_iris front00
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            p "¿Acaso a ti te la hacían sin que estuviera dura?"

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris right02
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 08
            show gensex_oral_d_frontHead_exp_iris front08
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

            d "Tssk..."

            show gensex_oral_d_frontHead_exp_blush 03
            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

            d "De acuerdo..."

            if p_didac.vaginal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¡Pero luego me vuelves a follar!"

            else:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡Pero luego me follas!"

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            d "Y ni si te ocurra correrte en mi cara,"

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris front01
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            d "¡¿me explico?!"

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
            show gensex_oral_d_frontHead_exp_eyebrows angryx03
            with dissolve

            # pause 0.2

            # $ ped_sex_general_expression_Cond = "lustAngry"
            # $ ped_sex_general_action_Cond = "o02"
            # call pedrera_sex_p_general_talk

            # window hide dissolve
            # pause

        elif p_didac.titwank_done == 2:

            # $ ped_sex_general_expression_Cond = "talk"
            # $ ped_sex_general_action_Cond = "talk"
            # call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
            show gensex_oral_d_frontHead_exp_eyebrows angryx02
            with dissolve

            d "Hmmm..."

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "¿Te lo estás pasando bien?"

            show gensex_oral_d_frontHead_exp_eyes 01
            show gensex_oral_d_frontHead_exp_iris front01
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
            show gensex_oral_d_frontHead_exp_eyebrows surprisex01
            with dissolve

            p "La verdad es que tienes unos pechos bastante tersos y esponjosos..."

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris right04
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            with dissolve

            d "..."

            show gensex_oral_d_frontHead_exp_eyes 08
            show gensex_oral_d_frontHead_exp_iris front08
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
            with dissolve

            d "Tsskk..."

            show gensex_oral_d_frontHead_exp_eyes 08
            show gensex_oral_d_frontHead_exp_iris front08
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
            show gensex_oral_d_frontHead_exp_eyebrows angryx06
            with dissolve

            d "Vete a tomar por el culo."

            # $ ped_sex_general_expression_Cond = "lustAngry"
            # $ ped_sex_general_action_Cond = "o02"
            # call pedrera_sex_p_general_talk
            # with dissolve

        elif p_didac.titwank_done == 3:

            # $ ped_sex_general_expression_Cond = "talk"
            # $ ped_sex_general_action_Cond = "talk"
            # call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            d "Me alegra que te gusten tanto mis pechos,"

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

            if p_didac.vaginal_received > 0:

                d "¡¿pero no crees que ya sería hora de que me la volvieras a meter dentro?!"

            else:

                d "¡¿pero no crees que ya sería hora de que me la metieras de una vez?!"

            call ped_D_NoSex ##########################################

            if p_didac.anal_received > 0:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡Y no me refiero por el culo!"

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

        elif p_didac.titwank_done == 4:

            # $ ped_sex_general_expression_Cond = "talk"
            # $ ped_sex_general_action_Cond = "talk"
            # call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
            with Dissolve(0.5)

            d "Al final te vas a correr y te voy a meter una hostia..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows angryx04
            with dissolve

        elif p_didac.titwank_done == 5:

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris front02
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
            with Dissolve(0.5)

            d "¡¿Es que no me explico?!"

            show gensex_oral_d_frontHead_exp_eyes 04
            show gensex_oral_d_frontHead_exp_iris front04
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows angryx06
            with dissolve

        elif p_didac.titwank_done == 6:

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
            show gensex_oral_d_frontHead_exp_eyebrows angryx05
            with Dissolve(0.5)

            d "Ni se te ocurra correrte..."

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
            show gensex_oral_d_frontHead_exp_eyebrows angryx06
            with dissolve

        elif p_didac.titwank_done >= 7:

            $ ped_check_1_10("ped_titwank_didac_list")

            #$ randomnum_1to10 = renpy.random.randint(1, 10)

            if ped_check_list_result == 1:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡Preferiría usar otra cosa que no fueran mis melones!"

            elif ped_check_list_result == 2:

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

                d "¡Me van a quedar rojos con tanto roce!"

            elif ped_check_list_result == 3:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡Está polla tendría que estar dentro de mi!"

            elif ped_check_list_result == 4:

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡Te juro que como te corras así, te voy a meter de hostias!"

            elif ped_check_list_result == 5:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

                d "A mi también me gustaban las tetas,"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡pero no decía no a buen coño, joder!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

            elif ped_check_list_result == 6:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                with dissolve

                d "¡Métemela de una vez, joder!"

                call ped_D_NoSex ##########################################

            elif ped_check_list_result == 7:

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris down03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                with dissolve

                d "La tienes enorme,"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "eso no se puede negar..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

            elif ped_check_list_result == 8:

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                with dissolve

                d "La quiero dentro..."

                call ped_D_NoSex ##########################################

            elif ped_check_list_result == 9:

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                with dissolve

                d "No me hagas suplicarte..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows sadx05
                with dissolve

            elif ped_check_list_result == 10:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Eres un hijo de puta..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

            else:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "..."

        if p_didac.titwank_done > 0:

            if p_didac.titwank_done > 5:
                $ ped_sex_general_action_Cond = "ob01_01"
            elif p_didac.titwank_done > 4:
                $ ped_sex_general_action_Cond = "ob01_02"
            elif p_didac.titwank_done > 3:
                $ ped_sex_general_action_Cond = "ob01_03"
            elif p_didac.titwank_done > 2:
                $ ped_sex_general_action_Cond = "ob01_04"
            else:
                $ ped_sex_general_action_Cond = "ob01_05"

            $ ped_sex_general_expression_Cond = "lustAngry"
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            pause 0.2

        

    ###############
###############

    elif p_prot.action in ["blowjob_received_TRY", "blowjob_received"]: # ORAL, not 69

        ##

        # $ ped_form_string = "o00l_02"
        # $ ped_vel_number = 2
        
        # $ ped_sex_general_expression_Cond = "veryAngry"
        # $ ped_sex_general_action_Cond = "o03_03" #
        # #$ ped_sex_general_action_Cond = "{}{}".format(ped_form_string, ped_vel_number) #
        # call pedrera_sex_p_general_talk

        $ debug ("ORAL TEST")

        if afternight04__MMouth_dick_Success > 0:

            $ p_prot.action = "blowjob_received"
            $ p_didac.action = "blowjob_done"

            $ p_prot.blowjob_received += 1
            $ p_didac.blowjob_done += 1

            $ p_didac.throat_dilatation += 1

            if p_didac.blowjob_done > 5:
                $ ped_sex_general_action_Cond = "o03_01"
            elif p_didac.blowjob_done > 4:
                $ ped_sex_general_action_Cond = "o03_02"
            elif p_didac.blowjob_done > 3:
                $ ped_sex_general_action_Cond = "o03_03"
            elif p_didac.blowjob_done > 2:
                $ ped_sex_general_action_Cond = "o03_04"
            elif p_didac.blowjob_done > 1:
                $ ped_sex_general_action_Cond = "o02_04"
            else:
                $ ped_sex_general_action_Cond = "o02_03"

            if p_didac.blowjob_done == 1:
                
                $ p_didac.blowjob_done = 0 # For Image Purposes.

                $ ped_sex_general_expression_Cond = "veryAngry"
                $ ped_sex_general_action_Cond = "o00_01" # tease
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Sutilmente, acaricias con tu miembro su mejilla para indicarle que empiece."

                n "A pesar del gruñido descolorido inicial,"

                $ ped_sex_general_expression_Cond = "lust"
                $ ped_sex_general_action_Cond = "o00l_01" # tease # it was o00_01 what does 00_01 ?
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "empieza acariciando suavemente la punta del glande con su cálida lengua."

                $ ped_sex_general_expression_Cond = "lust"
                $ ped_sex_general_action_Cond = "o00l_02" # tease
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                p "..."

                $ p_didac.blowjob_done = 1 # For images purposes. # Still necessary?

                $ ped_sex_general_expression_Cond = "closed"
                $ ped_sex_general_action_Cond = "o01_01" # Blowjob Glans Tip
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Sin demasiada demora, empieza a introducirla en su boca sin dejar de saborearla con su lengua."

                pt "Suerte que no le gusta..."

                $ ped_sex_general_expression_Cond = "closed"
                $ ped_sex_general_action_Cond = "o02_01" # Blowjob Glans Tip
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Deslizando su cabeza, consigue introducirse el glande por completo."

                $ ped_sex_general_expression_Cond = "angryFront"
                $ ped_sex_general_action_Cond = "o02_02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with vpunch

                p "Ughh..."

                # $ p_prot.action = "rest"
                # $ p_didac.action = "rest"

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with Dissolve(0.5)

                d "No te me vayas a correr aún,"

                extend " eh."

                if p_prot.orgasm == 0:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    p "La primera corrida suele ser más rápida que las demás."

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡Joder!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡Pues entonces me hubieras podido elegir segunda!"

                else:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    p "..."

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¿En serio quieres que siga chupándotela?"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                d "Ya estoy bastante húmeda ahí abajo..."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth   sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                # $ p_prot.action = "blowjob_received"
                # $ p_didac.action = "blowjob_done"

                # $ p_characters_action = "rest"

                # $ ped_sex_general_expression_Cond = "closed"
                # $ ped_sex_general_action_Cond = "o02" # blowbjob slow
                # call pedrera_sex_p_general_talk
                # with Dissolve(0.5)

            elif p_didac.blowjob_done == 2:

                $ ped_sex_blow_MChand = "on"
                $ ped_sex_general_expression_Cond = "angryFront"
                $ ped_sex_general_action_Cond = "o02_03" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Posando tu mano sobre su cabeza, le indicas que no se detenga"

                n "Aún y a regañadientes,"

                $ ped_sex_general_expression_Cond = "closed"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "prosigue su movimiento horizontal acariciando cada tramo de tu falo con sus labios y su ardiente lengua,"

                n "al mismo tiempo que sientes el cálido aliento que exhala,"

                n "y su mano acariciando la base de tu manubrio."

                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_expression_Cond = "angryFront"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                p "No se te da nada mal..."

                p "Se nota que has estado practicando."

                # $ p_prot.action = "rest"
                # $ p_didac.action = "rest"

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with Dissolve(0.5)

                d "Como sigas así de gilipollas,"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "al final te la voy a morder."

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "Siempre y cuando no sea demasiado fuerte..."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Tskk..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

                pause 0.2

                # $ p_prot.action = "blowjob_received"
                # $ p_didac.action = "blowjob_done"

                # $ ped_sex_general_expression_Cond = "closed"
                # $ ped_sex_general_action_Cond = "o02" # blowbjob slow
                # call pedrera_sex_p_general_talk
                # with Dissolve(0.5)

            elif p_didac.blowjob_done == 3:

                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_expression_Cond = "angryFront"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Sin otra instrucción que tu mirada, prosigue en su labor."

                $ ped_sex_general_expression_Cond = "closed"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

            elif p_didac.blowjob_done > 3:

                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_expression_Cond = "angryFront"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                d "..."

                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00" # blowbjob slow
                call pedrera_sex_p_general_talk

                $ ped_check_1_10("ped_oral_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Como te me corras en la boca,"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "te voy a reventar los huevos."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris down05
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                elif ped_check_list_result == 2:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Ni se te ocurra terminar en mi boca."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                elif ped_check_list_result == 3:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx02
                    with dissolve

                    d "Ya va siendo hora de que me folles..."

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡¿No crees?!"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                elif ped_check_list_result == 4:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "¿Hasta cuando quieres que esté haciendo esta mariconada?"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                elif ped_check_list_result == 5:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Te recuerdo que no la quiero en mi boca..."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                elif ped_check_list_result == 6:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_d_frontHead_exp_eyebrows sadx04
                    with dissolve

                    d "¿Por qué te cuesta tanto follarme?"

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_d_frontHead_exp_eyebrows sadx04
                    with dissolve

                elif ped_check_list_result == 7:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Métemela de una jodida vez..."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows sadx05
                    with dissolve

                    call ped_D_NoSex ##########################################

                elif ped_check_list_result == 8:

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    d "¿Tanto te gusta que te la esté chupando?"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
                    show gensex_oral_d_frontHead_exp_eyebrows sadx05
                    with dissolve

                elif ped_check_list_result == 9:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Estoy segura que te lo pasarías mejor si me estuvieras follando..."

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows sadx05
                    with dissolve

                elif ped_check_list_result == 10:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "..."

                else:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "..."

                # pause 0.2

                # $ ped_sex_blow_MChand = "off"
                # $ ped_sex_general_expression_Cond = "angryFront"
                # #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                # call pedrera_sex_p_general_talk
                # with Dissolve(0.5)

            if p_didac.blowjob_done == 3:

                n "Teniendo tu atención centrada en el arte oral de Dídac,"

                n "apenas te percatas de la presencia que se impone detrás de ti."

                $ ped_sex_general_expression_Cond = "surpriseLeft"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                p "¡¿Txell?!"

                $ ped_sex_general_expression_Cond = "surpriseDown"
                #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                call pedrera_sex_p_general_talk
                with dissolve

                p "¿Qué estás haciendo?"

                $ Pedrera_char_Cond = "TxellSuperClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with fade_short

                tx "Viendo que te gusta tanto que te den un repaso por delante,"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows normal
                with dissolve

                tx "me pregunto si disfrutarías al mismo tiempo que jugase un poco con tu trasero."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx03
                with dissolve

                p "¿De qué estás...?"

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Tranquilo,"

                extend " tengo experiencia en esto..."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                pause 0.3

                show m_exp_mouth special_tongueOut
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows sadx01

                show m_armL fingerLicking
                with Dissolve(1.0)

                n "Sugerentemente, se introduce un dedo entre sus labios,"

                show m_exp_mouth sad_Talkingx001
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows sadx04

                show m_armL fingerSucking
                with Dissolve(0.5)

                n "lamiéndolo con un rostro lascivo y juguetón,"

                show m_exp_mouth sad_Talkingx001
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with dissolve

                pause 0.2

                scene ped_assf_comp01:
                    subpixel True
                    truecenter
                    zoom 0.75 xpos 0.5 ypos 0.5 # Center ass
                    ease 2.0 zoom 0.8 xpos 0.2 ypos 0.8 # Showing the hand on buttock.
                with fade

                n "mientras con la otra mano aparta una de tus nalgas,"

                show ped_assf_comp02:
                    subpixel True
                    truecenter
                    zoom 1.0 ypos -0.34 # Close Down
                    ease 5.0 zoom 1.0 ypos 0.5
                    ease 5.0 zoom 0.38 xpos 0.5 ypos 0.5 # Image General.
                with Dissolve(0.5)

                n "para luego acercar ese húmedo y cálido dedo a tu agujero anal."

                p "¿Se puede saber qué...?"

                window hide dissolve
                pause

                $ Pedrera_char_Cond = "TxellSuperClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows sadx01
                with fade_short

                tx "No te importa que le haga esto,"

                extend " ¿Verdad?"

                show m_exp_mouth sadbiting_Silentx03
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex01
                with dissolve

                p "¿Me lo preguntas en tercera persona?"

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Se lo estoy preguntando a Neus."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows serious
                with dissolve

                ne "¿Uh...?"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 01
                show m_exp_piris right01
                show m_exp_eyebrows normal
                with dissolve

                tx "No tendrás miedo que pierda su virilidad,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "si empieza a disfrutar en exceso de mi dedo en su trasero,"

                extend " ¿Verdad?"

                show m_exp_mouth happybiting_Silentx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx01
                show neus_exp_iris left00
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with fade_short

                ne "Uh-"

                extend "No."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Eso es cosa suya."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "TxellSuperClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with fade_short

                menu:

                    pt "¡¿Me quiere meter un dedo por el culo?!"

                    "<Detenerla>":
                        call p_Help

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 01
                        show m_exp_piris front01
                        show m_exp_eyebrows surprisex02
                        with dissolve

                        p "Siento decepcionarte,"

                        extend " pero no quiero que me metas el dedo por el culo."

                        if FuckM_Start_Cond:

                            pass

                            # CONDITIONAL depending of if you had sex PASIVE or ACTIVE with her. FOR FUTURE

                        else:

                            show m_exp_mouth sad_Talkingx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                            tx "¿Por qué?"

                            show m_exp_mouth sad_Talkingx08
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                            tx "¿Crees que vas a ser menos hombre si te meten algo por detrás?"

                            show m_exp_mouth sad_Talkingx06
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows surprisex001
                            with dissolve

                            tx "¿Aunque sea un simple dedo?"

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 01
                            show m_exp_piris front01
                            show m_exp_eyebrows surprisex02
                            with dissolve

                            p "¿Sabes aceptar un no?"

                            show m_exp_mouth sad_Silentx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx04
                            with dissolve

                            tx "..."

                            show m_exp_mouth sad_Talkingx05
                            show m_exp_eyes 03
                            show m_exp_piris right03
                            show m_exp_eyebrows angryx03
                            with dissolve

                            tx "Como quieras..."

                            show m_exp_mouth sad_Silentx06
                            show m_exp_eyes 05
                            show m_exp_piris right05
                            show m_exp_eyebrows angryx04
                            with dissolve

                            # pause 0.2

                            # $ ped_sex_general_expression_Cond = "angry"
                            # #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                            # call pedrera_sex_p_general_talk
                            # with fade


                    "<Dejarle que te meta el dedo en el culo>":
                        call p_Help

                        show m_exp_mouth happy_Silentx07
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx03
                        with dissolve

                        pause 0.2


                        $ p_txell.anal_fingered_done += 1
                        $ p_prot.anal_fingered_received += 1
                        $ p_prot.anal_dilatation += 1

                        $ p_prot.b_action = "anal_fingered_received"
                        $ p_txell.action = "anal_fingered_done"

                        $ p_prot_anal_fingered_received_from_p_txell += 1


                        scene ped_assf_comp04:
                            subpixel True
                            truecenter
                            zoom 1.0 ypos -0.34 # Close Down
                            ease 3.0 zoom 1.0 ypos 0.5
                            easein_quad 20.0 zoom 0.38 xpos 0.5 ypos 0.5 # Image General.

                            #zoom 0.38 xpos 0.5 ypos 0.5 # Image General.
                        with fade

                        pause 1.0

                        with vpunch

                        pt "La madre que la parió..."

                        tx "¿Ves como te gusta?"

                        p "No te he dicho tal cosa."

                        window hide dissolve
                        pause

                        $ Pedrera_char_Cond = "TxellSuperClose"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows suspiciousx02
                        with fade_short

                        tx "Hay reacciones corporales mucho más sinceras que las palabras."

                        show m_exp_mouth happy_Silentx08
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx03
                        with dissolve

                        pt "Será hija de..."

                        $ ped_sex_general_expression_Cond = "angryFront"
                        #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                        call pedrera_sex_p_general_talk
                        with hpunch

                        p "¡Ugh!..."

                        $ ped_sex_general_expression_Cond = "talk"
                        $ ped_sex_general_action_Cond = "o00_00"
                        call pedrera_sex_p_general_talk

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx02
                        with Dissolve(0.5)

                        d "Si quieres te dejo de chupar,"

                        show gensex_oral_d_frontHead_exp_eyes 03
                        show gensex_oral_d_frontHead_exp_iris down03
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_d_frontHead_exp_eyebrows angryx03
                        with dissolve

                        d "y que siga ella hurgándote el culo si tanto te gusta..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        #pause 0.2

                        $ Pedrera_char_Cond = "NeusClose"
                        call Pedrera_char_lab

                        show neus_exp_mouth sad_Talkingx08
                        show neus_exp_iris front04
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_eyebrows angryx04
                        with fade_short

                        ne "¡No perdamos el norte!"

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_iris front01
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_eyebrows angryx01
                        with dissolve

                        ne "¡Tiene que correrse dentro de ti!"

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_iris front04
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_eyebrows angryx03
                        with dissolve

                        ne "Sea dónde sea,"

                        show neus_exp_mouth sad_Talkingx09
                        show neus_exp_iris front03
                        $ nteye = 3
                        call neus_exp_tears_tears
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "pero no puedes desperdiciar ninguna gota."

                        show neus_exp_mouth sadbiting_Silentx04
                        show neus_exp_iris front05
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        d "..."

                        $ ped_sex_general_expression_Cond = "talk"
                        $ ped_sex_general_action_Cond = "o00_00"
                        call pedrera_sex_p_general_talk

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris right02
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with fade_short

                        d "¡Es él el que insiste en que se la chupe!"

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                        ne "..."

                        show gensex_oral_d_frontHead_exp_eyes 00
                        show gensex_oral_d_frontHead_exp_iris down00
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                        show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        tx "Eres tú quien necesita su esperma para sobrevivir."

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris down02
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                        show gensex_oral_d_frontHead_exp_eyebrows normal
                        with dissolve

                        tx "Además,"

                        extend " ni que te hubiera forzado a ello..."

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris down04
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                        tx "No te quejes tanto."

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        d "..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris right05
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                        d "Tssk..."

                        # $ ped_sex_general_expression_Cond = "closed"
                        # #$ ped_sex_general_action_Cond = "o02" # blowbjob slow
                        # call pedrera_sex_p_general_talk
                        # with Dissolve(0.5)

## END BLOWJOB

            pause 0.2

            if p_didac.blowjob_done > 6:
                $ ped_sex_general_action_Cond = "o00l_01"
            elif p_didac.blowjob_done > 5:
                $ ped_sex_general_action_Cond = "o00l_02"
            elif p_didac.blowjob_done > 4:
                $ ped_sex_general_action_Cond = "o00l_03"
            elif p_didac.blowjob_done > 3:
                $ ped_sex_general_action_Cond = "o00l_02"
            elif p_didac.blowjob_done > 2:
                $ ped_sex_general_action_Cond = "o01_04"
            elif p_didac.blowjob_done > 1:
                $ ped_sex_general_action_Cond = "o01_03"
            else:
                $ ped_sex_general_action_Cond = "o01_02"

            if p_didac.blowjob_done > 3:
                $ ped_sex_general_expression_Cond = "angryLick"
            elif p_didac.blowjob_done > 2:
                $ ped_sex_general_expression_Cond = "angry"
            else:
                $ ped_sex_general_expression_Cond = "veryAngry"

            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

        else:

            $ debug ("Didac doesn't want to do oral sex to you.")

            $ p_didac.blowjob_done_TRY += 1

            if p_didac.blowjob_done_TRY > 5:
                $ ped_sex_general_action_Cond = "o00_05"
            elif p_didac.blowjob_done_TRY > 4:
                $ ped_sex_general_action_Cond = "o00_04"
            elif p_didac.blowjob_done_TRY > 3:
                $ ped_sex_general_action_Cond = "o00_03"
            elif p_didac.blowjob_done_TRY > 2:
                $ ped_sex_general_action_Cond = "o00_02"
            elif p_didac.blowjob_done_TRY > 1:
                $ ped_sex_general_action_Cond = "o00_01"
            else:
                $ ped_sex_general_action_Cond = "o00_02"

            $ ped_sex_general_expression_Cond = "veryAngry"
            call pedrera_sex_p_general_talk

            if p_didac.blowjob_done_TRY == 1:

                $ ped_sex_general_expression_Cond = "veryAngry"
                #$ ped_sex_general_action_Cond = "o00_01" # tease
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Sutilmente, acaricias con tu miembro su mejilla para indicarle que empiece."

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00" # tease
                call pedrera_sex_p_general_talk

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with vpunch

                d "¡¿Qué cojones estás haciendo imbécil?!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                p "¿No es evidente?"

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                with dissolve

                d "Como sigas así,"

                extend " te voy a romper las pelotas."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                d "Eso sí que va a ser una..."

                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                with vpunch

                d "¡PUTA EVIDENCIA!"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

                d "¡Gilipollas!"

                if afternight04__MMouth_dick_Failed > 0:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "Ayer te dije que no te no tenía ninguna puta intención de metérmela en la boca!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¿¡Y aún sigues insistiendo?!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx11
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

                p "..."

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris down02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                with dissolve

                d "¡Aparta tu maldita polla de mi cara!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx13
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

            elif p_didac.blowjob_done_TRY > 1:

                $ ped_sex_general_expression_Cond = "veryAngry"
                #$ ped_sex_general_action_Cond = "o00_01" # tease
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                d "..."

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "o00_00"
                call pedrera_sex_p_general_talk

                if p_didac.blowjob_done_TRY == 2:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with Dissolve(0.5)

                    d "Si por alguna casualidad llegara a entrar en mi boca..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡TE LA ARRANCO DE UN MORDISCO!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                    d "¡¿ME EXPLICO?!"

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    p "..."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris right03
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx01
                    with dissolve

                    ne "Dídac..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris right01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡Es el capullo este que no lo entiende!"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    ne "..."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris left05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx11
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                elif p_didac.blowjob_done_TRY == 3:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "La madre que te parió..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡¿ES QUE NO ME EXPLICO?!"

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                    d "¡APARTA TU PUTA ASQUEROSA POLLA DE MI BOCA!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡Y FÓLLAME DE UNA JODIDA VEZ!"

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                elif p_didac.blowjob_done_TRY >= 4:

                    $ ped_check_1_10("ped_oralTRY_didac_list")

                    #$ randomnum_1to10 = renpy.random.randint(1, 10)

                    if ped_check_list_result == 1:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                        d "Tienes ganas de quedarte eunuco como ese gordo, calvo de {a=https://es.wikipedia.org/wiki/Juego_de_tronos}Juego de Tronos{/a},"

                        extend " ¿Verdad?"

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        pt "También me podría haber comparado con {a=https://es.wikipedia.org/wiki/Anexo:Personajes_de_Canción_de_hielo_y_fuego#Gusano_Gris}Gusano Gris{/a} en lugar de con {a=https://es.wikipedia.org/wiki/Varys}Varys{/a}..."

                    elif ped_check_list_result == 2:

                        show gensex_oral_d_frontHead_exp_eyes 02
                        show gensex_oral_d_frontHead_exp_iris front02
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                        d "¡¿Por qué coño insistes tanto en metérmela en la boca?!"

                        show gensex_oral_d_frontHead_exp_eyes 01
                        show gensex_oral_d_frontHead_exp_iris front01
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "¡Si lo que quiero es que me la metas por el coño, joder!"

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx13
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    elif ped_check_list_result == 3:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx07
                        with dissolve

                        d "Te la estás jugando maldito hijo de puta..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                    elif ped_check_list_result == 4:

                        show gensex_oral_d_frontHead_exp_eyes 00
                        show gensex_oral_d_frontHead_exp_iris front00
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "¡Fóllame de una puta vez y déjate de mariconadas!"

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    elif ped_check_list_result == 5:

                        show gensex_oral_d_frontHead_exp_eyes 04
                        show gensex_oral_d_frontHead_exp_iris front04
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows sadx03
                        with dissolve

                        d "¿Por qué coño insistes?"

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve
                        
                    elif ped_check_list_result == 6:

                        show gensex_oral_d_frontHead_exp_eyes 01
                        show gensex_oral_d_frontHead_exp_iris front01
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "¡¿Es que hablo chino?!"

                        show gensex_oral_d_frontHead_exp_eyes 03
                        show gensex_oral_d_frontHead_exp_iris left03
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                        d "Maldito imbécil..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris left05
                        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
                        show gensex_oral_d_frontHead_exp_eyebrows angryx04
                        with dissolve

                    elif ped_check_list_result == 7:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "Me estás agotando la paciencia..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    elif ped_check_list_result == 8:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "Al final te voy a meter tal hostia en los huevos..."

                        show gensex_oral_d_frontHead_exp_eyes 01
                        show gensex_oral_d_frontHead_exp_iris front01
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                        show gensex_oral_d_frontHead_exp_eyebrows angryx07
                        with dissolve

                        d "¡Que te van a salir por la boca!"

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    elif ped_check_list_result == 9:

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris front05
                        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                        d "Eres pesado de la hostia..."

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                    elif ped_check_list_result == 10:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris left05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    else:

                        show gensex_oral_d_frontHead_exp_eyes 08
                        show gensex_oral_d_frontHead_exp_iris front08
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx14
                        show gensex_oral_d_frontHead_exp_eyebrows angryx06
                        with dissolve

                        d "..."

                        show gensex_oral_d_frontHead_exp_eyes 05
                        show gensex_oral_d_frontHead_exp_iris left05
                        show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                        show gensex_oral_d_frontHead_exp_eyebrows angryx05
                        with dissolve

                    p "..."

            call afternight05_Pedrera_Neus_Warning

            $ p_prot.action = "rest"
            $ p_didac.action = "rest"


    ###############
###############
    
    #elif p_didac.action in ["blowjobDeep_done_TRY", "blowjobDeep_done"]:
    elif p_prot.action in ["blowjobDeep_received_TRY", "blowjobDeep_received"]:

        $ debug ("Se la metes entera en la garganta a Dídac")

        $ p_prot_blowjobDeep_received_TRY_withDidac += 1

        ##

        if p_didac.throat_dilatation >= 4:

        #if afternight04__MMouth_dick_Deep_Success > 0:

            $ ped_sex_blow_MChand = "on"
        
            if p_didac.blowjobDeep_done > 4:
                $ ped_sex_general_action_Cond = "o04_05"
            elif p_didac.blowjobDeep_done > 3:
                $ ped_sex_general_action_Cond = "o04_04"
            elif p_didac.blowjobDeep_done > 2:
                $ ped_sex_general_action_Cond = "o04_03"
            elif p_didac.blowjobDeep_done > 1:
                $ ped_sex_general_action_Cond = "o04_02"
            else:

                $ ped_sex_general_action_Cond = "o04_01"

            if p_didac.blowjobDeep_done > 4:
                $ ped_sex_general_expression_Cond = "closed"
            elif p_didac.blowjobDeep_done > 2:
                $ ped_sex_general_expression_Cond = "angry"
            else:
                $ ped_sex_general_expression_Cond = "veryAngry"

            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            $ debug ("Didac Throat Dilatation: [p_didac.throat_dilatation]\nThroat Pain Received times: [p_didac.throat_pain_received]")

            #if p_didac.throat_dilatation >= 3:

            $ debug ("Deepthroat Didac.")

            $ p_prot.blowjobDeep_received += 1
            $ p_didac.blowjobDeep_done += 1

            $ p_prot.action = "blowjobDeep_received"
            $ p_didac.action = "blowjobDeep_done"

            with vpunch

            if p_didac.blowjobDeep_done == 1:

                d "{size=55}¡UUGHHMM!{/size}"

            elif p_didac.blowjobDeep_done == 2:

                d "{size=50}¡UGH!{/size}"

            elif p_didac.blowjobDeep_done == 3:

                d "{size=45}¡HUHMMMmm!{/size}"

            elif p_didac.blowjobDeep_done == 4:

                d "{size=40}¡Hhhmm...!{/size}"

            elif p_didac.blowjobDeep_done > 4:

                d "{size=35}HMmmm...{/size}"

            if p_didac.blowjobDeep_done == 1:

                n "Con una expresión entre dolor, malestar y extraña lascivia,"

                n "Dídac recibe la presión que haces entre sus fauces,"

                n "consiguiendo penetrar más allá de su garganta;"

                n "Casi la totalidad de tu falo penetra a través de su esófago."

                ne "..."

                if p_prot_anal_fingered_received_from_p_txell > 0:

                    $ Pedrera_char_Cond = "TxellSuperClose"

                else:
                    $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with fade_short

                tx "Caray..."

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "No me imaginaba que le llegaría a caber entera sin que acabara sacando la cena..."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                pause 0.2

                $ ped_sex_general_expression_Cond = "lustAngry"
                call pedrera_sex_p_general_talk
                with fade_short

                n "Un gruñido gutural surge del interior de Dídac entre la sorna, el enojo y y la victoria,"

                $ ped_sex_general_expression_Cond = "angry"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "mientras sigue luchando para no desfallecer por la falta de oxígeno."

            if p_didac.blowjobDeep_done > 1:
                $ ped_sex_general_expression_Cond = "closed"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                if p_didac.blowjobDeep_done == 2:

                    n "A pesar de sus gruñidos y sus quejas,"

                    n "es evidente que no le disgusta tanto como vocea."

                    n "Sientes el calor de sus amígdalas al mismo tiempo que la carne de su esófago arropándolo por completo."

                elif p_didac.blowjobDeep_done == 3:

                    n "Su lengua te provoca cierto cosquilleo en tus testículos al conseguir meterse tu polla entera en su garganta."

                elif p_didac.blowjobDeep_done == 4:

                    n "La presión que sientes en el glande al llegar lo más profundo que te es posible,"

                    n "te resulta inquietamente doloroso y placentero."

                elif p_didac.blowjobDeep_done >= 5:

                    p "Uffh..."


            # $ p_prot.action = "rest"
            # $ p_didac.action = "rest"
            

            $ ped_sex_blow_MChand = "off"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "o00_00"
            call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 07
            show gensex_oral_d_frontHead_exp_iris front07
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
            show gensex_oral_d_frontHead_exp_eyebrows sadx04
            with vpunch
            
            if p_didac.blowjobDeep_done == 1:

                d "{size=55}¡AAhhh...!{/size}"

            elif p_didac.blowjobDeep_done == 2:

                d "{size=50}¡Aahhhm...!{/size}"

            elif p_didac.blowjobDeep_done == 3:

                d "{size=45}AAAhhh-Ahhh...{/size}"

            elif p_didac.blowjobDeep_done == 4:

                d "{size=40}AAAhhh...{/size}"

            elif p_didac.blowjobDeep_done > 4:

                d "{size=35}Aahh...{/size}"

            if p_didac.blowjobDeep_done == 1:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡DIOS...!"

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                d "¡¿Tenías que metérmela entera?!"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows normal
                with dissolve

                p "No te quejes tanto,"

                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "que en el fondo sabes que lo disfrutas."

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡Casi me quedo sin respirar!"

                show gensex_oral_d_frontHead_exp_eyes 01
                if p_prot.b_action == "anal_fingered_received":
                    show gensex_oral_d_frontHead_exp_iris down01
                else:
                    show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                tx "Pero sorprendentemente lo has logrado..."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris left04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "Hmm..."

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "No es la primera vez que se la meto entera,"

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                p "¿verdad que no?"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

                d "Tsssk..."

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¡Ya sabes dónde quiero que me la metas!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Pero por ahora te permito hacer el gilipollas,"

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx007
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

                d "porque sé que luego harás lo que te pido..."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                with dissolve

                d "¡¿Verdad?!"

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

            elif p_didac.blowjobDeep_done == 2:

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows sadx05
                with dissolve

                d "Ahhh..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "Joder..."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "¡¿Me quieres dejar sin respiración?!"

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx10
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                p "No te quejes tanto."

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "..."

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Como te corras sin habérmela metido,"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "me cabrearé de verdad."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

            elif p_didac.blowjobDeep_done == 3:

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx13
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡¿Cómo te puede poner más caliente una garganta que un coño?!"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows serious
                with dissolve

                p "Me dirás que no te gustaba a ti que te la metieran hasta el fondo de su garganta..."

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "..."

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows angryx01
                with dissolve

                p "Además,"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                p "se te da bastante bien..."

                show gensex_oral_d_frontHead_exp_blush 03
                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "¿Seguro que no habías practicado esto antes de convertirte en mujer?"

                show gensex_oral_d_frontHead_exp_blush 04
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

                d "¡SERÁS CAPULLO!"

                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "..."

                show gensex_oral_d_frontHead_exp_blush 03
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                with dissolve

            elif p_didac.blowjobDeep_done == 4:

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Como se te ocurra correrte mientras la tengas en mi garganta..."

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                d "¡Te la arranco de un mordisco!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                p "Si hicieras eso,"

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                with dissolve

                p "es probable que acabases muriendo ahogada..."

                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris down02
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                d "..."

                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve

                d "Gilipollas..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                with dissolve

            elif p_didac.blowjobDeep_done >= 5:

                $ ped_check_1_10("ped_blowjobDeep_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "Ni se te ocurra correrte en mi boca..."

                elif ped_check_list_result == 2:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows sadx01
                    with dissolve

                    d "Quieres que muera ahogada..."

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¿Verdad?"

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "No me seas tan {a=https://en.wiktionary.org/wiki/drama_queen}drama queen{/a}..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡¿QUE NO SEA QUÉ?!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    p "..."

                elif ped_check_list_result == 3:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "Ya me la he metido entera en la boca cómo querías..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡AHORA MÉTEMELA POR EL COÑO!"

                    call ped_D_NoSex ##########################################

                elif ped_check_list_result == 4:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¿Vas a estar mucho rato atragantándome con tu pollón?"

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    p "Como si no lo disfrutaras..."

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx18
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡¿QUIERES QUE TE META EL PUÑO POR EL CULO?!"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris right01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "¡Admite de una vez que te estás poniendo cachonda con su pollón!"

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx106
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡Tú cállate!"

                elif ped_check_list_result == 5:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx005
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "Coño..."

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx11
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡¿Ya está suficientemente mojado no crees?!"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    if p_didac.vaginal_received > 0:

                        d "¡MÉTEMELA DE NUEVO!"

                    else:

                        d "¡MÉTEMELA DE UNA VEZ!"

                    call ped_D_NoSex ##########################################

                elif ped_check_list_result == 6:

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx18
                    show gensex_oral_d_frontHead_exp_eyebrows sadx01
                    with dissolve

                    d "¡¿De verdad hace falta que me la metas entera en la garganta?!"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    p "¿Entonces no te molesta tenerla en la boca?"

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡VETE A LA MIERDA!"

                elif ped_check_list_result == 7:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_d_frontHead_exp_eyebrows sadx02
                    with dissolve

                    d "Quiero que me la metas hasta el fondo..."

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡PERO NO EN LA GARGANTA!"

                elif ped_check_list_result == 8:

                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    d "Eres pesadito..."

                elif ped_check_list_result == 9:

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡¿Qué tiene mi garganta que no tenga mi coño?!"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_d_frontHead_exp_eyebrows serious
                    with dissolve

                    p "Que me pone un montón verte así de cabreada."

                    show gensex_oral_d_frontHead_exp_blush 04
                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    d "..."

                    show gensex_oral_d_frontHead_exp_blush 05
                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx10
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "Serás capullo..."

                elif ped_check_list_result == 10:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "..."

                else:

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_d_frontHead_exp_eyebrows angryx03
                    with dissolve

                    d "..."

                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve

                pause 0.2

            if p_didac.blowjobDeep_done > 4:
                $ ped_sex_general_action_Cond = "o04_03"
            elif p_didac.blowjobDeep_done > 3:
                $ ped_sex_general_action_Cond = "o04_02"
            elif p_didac.blowjobDeep_done > 2:
                $ ped_sex_general_action_Cond = "o03_02"
            elif p_didac.blowjobDeep_done > 1:
                $ ped_sex_general_action_Cond = "o02_02"
            else:

                $ ped_sex_general_action_Cond = "o00l_02"

            if p_didac.blowjobDeep_done > 4:
                $ ped_sex_general_expression_Cond = "closed"
            elif p_didac.blowjobDeep_done > 2:
                $ ped_sex_general_expression_Cond = "angry"
            else:
                $ ped_sex_general_expression_Cond = "angryLick"

            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            #$ p_characters_action = "rest"


        #elif p_didac.throat_dilatation <= 4 or afternight04__MMouth_dick_Deep_Success == 0:
        else:

            $ ped_sex_blow_MChand = "on"
            $ ped_sex_general_expression_Cond = "angry"
            $ ped_sex_general_action_Cond = "o04_01" # Deepthroat
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            pause 1.5

            $ p_prot.action = "rest"
            $ p_didac.action = "rest"

            $ ped_sex_blow_MChand = "off"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "o00_00" # Deepthroat
            call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 07
            show gensex_oral_d_frontHead_exp_iris front07
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
            show gensex_oral_d_frontHead_exp_eyebrows angryx06

            with vpunch
            with vpunch

            $ p_didac.throat_pain_received += 1

            if p_prot_blowjobDeep_received_TRY_withDidac == 1:
                $ p_didac.throat_pain += 1
                $ p_didac.throat_dilatation -= 1

            elif p_prot_blowjobDeep_received_TRY_withDidac == 2:
                $ p_didac.throat_pain += 2
                $ p_didac.throat_dilatation -= 2

            elif p_prot_blowjobDeep_received_TRY_withDidac >= 3:
                $ p_didac.throat_pain += 3
                $ p_didac.throat_dilatation -= 3

            if p_didac.throat_pain_received == 1:

                d "¡KOF! ¡KOF!"

            elif p_didac.throat_pain_received == 2:

                d "{size=40}¡KOF! ¡KOF!{/size}"

            elif p_didac.throat_pain_received == 3:

                d "{size=45}¡KOF! ¡KOF!{/size}"

            elif p_didac.throat_pain_received == 4:

                d "{size=50}¡KOF! ¡KOF!{/size}"

            elif p_didac.throat_pain_received > 4:

                d "{size=55}¡KOF! ¡KOF!{/size}"

            if p_didac.throat_pain_received == 1:

                if afternight04__MMouth_dick_Deep_Success == 0:

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                    d "¡¿ES QUE ESTÁS IMBÉCIL O QUÉ TE PASA?!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡¿NO VES QUE NO CABE?!"

                else:

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡Joder!"

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡¿Es que no ves que no cabe?!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx11
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

            elif p_didac.throat_pain_received == 2:

                if afternight04__MMouth_dick_Deep_Success == 0:

                    show gensex_oral_d_frontHead_exp_eyes 00
                    show gensex_oral_d_frontHead_exp_iris front00
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve

                    d "¡ME CAGO EN TU JODIDA MADRE!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                    d "¡¿ES QUE ERES RETRASADO MENTAL O TE VOMITARON AL NACER?!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx18
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                    d "¡AL FINAL TE LA ARRANCARÉ DE UN BOCADO!"

                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve

                else:

                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    d "¡COÑO!"

                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with dissolve

                    d "¡¿Es que no me has escuchado antes?!"

                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_iris front04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows sadx02
                    with fade_short

                    ne "[protname]..."

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_iris front02
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Se más gentil."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_iris front04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    pause 0.2

                    $ ped_sex_blow_MChand = "off"
                    $ ped_sex_general_expression_Cond = "talk"
                    $ ped_sex_general_action_Cond = "o00_00" # Deepthroat
                    call pedrera_sex_p_general_talk

                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx04
                    with fade_short

                    d "..."

            elif p_didac.throat_pain_received == 3:

                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

                d "¡LA MADRE QUETE PARIÓ!"

                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris front00
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve

                d "¡¿QUÉ COÑO TE PASA POR LA CABEZA?!"

                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris front04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx07
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "[protname]..."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx05
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "TxellSuperClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx03
                with fade_short

                tx "Sabía que eras imbécil."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx02
                with dissolve

                tx "Pero no hasta este punto."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx03
                with dissolve

                pause 0.2

            elif p_didac.throat_pain_received >= 4:

                d "..."

                #call afternight05_Pedrera_Sex_NeusLastWarning

            $ p_characters_action = "rest"
            
            call afternight05_Pedrera_Neus_Warning

            $ ped_sex_blow_MChand = "off"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "o00_00" # Deepthroat
            call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 05
            show gensex_oral_d_frontHead_exp_iris front05
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
            show gensex_oral_d_frontHead_exp_eyebrows angryx06
            with fade_short

        # else: # She doesn't want to receive ORAL DEEP.

        #     $ p_didac.throat_pain_received += 1

        #     $ debug ("PAIN THROAT, you never did Deepthroat")

        #     d ""


    ###############
###############

    else:

        aj "ORAL DIDAC ERROR 158648798"

        # CHOICE.

        #p "Supongo que tienes razón."

        #d "Así me gusta."

    #jump afternight05_Pedrera_Sex_action
    return
    #call afternight05_Pedrera_Sex


###########################################################################
###########################################################################  DOGGY - MISSIONARY


label afternight05_Pedrera_Sex_p_didac_doggy:

    # if p_prot.pos == "doggy":
    #     # $ ped_sex_general_zoom_Cond = ""
    #     # call pedrera_sex_p_general_talk

    #     $ debug ("Doggystyle Sex with Didac.")


    # if p_prot.pos == "missionary":

    #     # $ ped_sex_blow_MChand = "off"
    #     # if p_didac.action == "cunnilingus_done_p_txell":
    #     #     $ ped_sex_general_expression_Cond = "closed"
    #     # else:
    #     #     $ ped_sex_general_expression_Cond = "talk"
    #     # #$ ped_sex_general_action_Cond = "o00_00"
    #     # call pedrera_sex_p_general_talk

    #     $ debug ("Missionary Sex with Didac.")



################################################################################
############################################################ REST

    #if p_didac.action != "rest" and p_didac.b_action != "rest":

    #call p_prot_previousSex

    if p_prot.action in ["rest", "takeDickOut", "takeTongueOut"] and p_prot.b_action in ["rest", "takeDickOut", "takeTongueOut"]:

        # $ p_prot.restTurns += 1 # How many sequential times you did nothing.

    ################################ REST Doggy

        if p_prot.pos == "doggy":

            if p_prot.pos_doggy_rest > 0:

                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "v00_01"
                call pedrera_sex_p_general_talk
                with fade
            else:
                $ ped_sex_blow_MChand = "off"
                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "v00_01"


            $ debug ("Doggystyle Sex with Didac.")

            # if p_prot.pos_doggy_rest == 0:
            #     $ p_prot.pos_doggy_rest += 1 # How many times you did nothing in doggystyle in TOTAL.

            if p_prot.pos_doggy_rest == 0:

                call afternight05_Pedrera_Sex_NakeYou

                d "Hmmm..."

                p "Te gusta que te folle como si fueras una perrita,"

                p "¿Verdad?"

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                with fade_short

                d "Tsk..."

                if p_didac.blowjob_done > 0:

                    d "Al menos así no me la tengo que volver a meter en la boca."

                elif p_didac.pos_missionary > 0:

                    d "Al menos así no tengo que mirarte a la cara."

            elif p_prot.pos_doggy_rest == 1:

                d "¿Te gusta mirarme el trasero?"

                p "Es posible."

                d "Bueno,"

                extend " pues también lo podrías estar mirando mientras me lo estás follando."

                p "No es lo mismo."

                d "Tssk..."

                d "Mira que eres toca-pelotas a veces..."

            elif p_prot.pos_doggy_rest == 2:

                d "¿Estás esperando a que se haga de día?"

                d "¡Métemela de una puta vez!"

                call ped_D_NoSex ##########################################

            elif p_prot.pos_doggy_rest == 3:

                d "¡Debería darte vergüenza tener a una tía a cuatro patas y no follártela!"

                p "Te recuerdo que hace apenas dos días..."

                d "¡No me vuelvas con eso!"

                d "¡Fóllame de una vez,"

                extend " joder!"

            elif p_prot.pos_doggy_rest >= 3:

                $ ped_check_1_10("ped_doggy_rest_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    d "Ya sé que te gusta mi culo,"

                    d "¡pero métemela de una vez!"

                elif ped_check_list_result == 2:

                    d "Te tenía por alguien de acción..."

                elif ped_check_list_result == 3:

                    d "Como tardes más,"

                    d "¡se me va a disecar el chumino!"

                elif ped_check_list_result == 4:

                    d "En serio..."

                    d "¡¿A qué coño esperas?!"

                elif ped_check_list_result == 5:

                    d "¿¡Para qué tienes un pollón tan enorme,"

                    d "si luego no lo usas?!"

                elif ped_check_list_result == 6:

                    d "¡Fóllame de una vez, joder!"

                elif ped_check_list_result == 7:

                    d "¡¿Me vas a hacer esperar toda la noche?!"

                elif ped_check_list_result == 8:

                    d "¿¡Acaso no te gusta mi coño?!"

                elif ped_check_list_result == 9:

                    d "Métemela de una vez..."

                elif ped_check_list_result == 10:

                    d "..."

                else:

                    d "..."


########################################################
########################################################
######################################################## ## REST Missionary

        if p_prot.pos == "missionary":

            $ ped_sex_general_action_Cond = "v00_00"

            $ ped_sex_blow_MChand = "off"
            if p_didac.action == "cunnilingus_done_p_txell":
                $ ped_sex_general_expression_Cond = "closed"
            else:
                $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_zoom_Cond = ""

            call pedrera_sex_p_general_talk

            #if p_prot.pos_missionary_rest == 0:
            # $ p_prot.pos_missionary_rest += 1 # How many times you did nothing in doggystyle in TOTAL.

            if p_prot.pos_missionary_rest == 0:

                call afternight05_Pedrera_Sex_NakeYou

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
                    with dissolve

                d "Hmmm..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx11
                    with dissolve

                d "¿Te gusta follarme mientras me miras la cara?"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                    with dissolve

                menu:

                    "Me gusta tenerte de cara para poder besarte.":
                        call p_Help

                        $pl.ch_pts("np",-1)
                        $pl.ch_pts("mp",1)

                        if afternight04__MMouth_Tongue_Success > 1:
                            $pl.ch_pts("dp",1)

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 04
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 06
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                                with dissolve

                            d "Euh..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils right01
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                                with dissolve

                            d "Serás capullo..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils right05
                                show gensex_missionary_d_head_exp_eyebrows sadx07
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                                with dissolve

                        else:
                            $pl.ch_pts("dp",-1)

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 03
                                show gensex_missionary_d_head_exp_eyes 00
                                show gensex_missionary_d_head_exp_pupils front00
                                show gensex_missionary_d_head_exp_eyebrows surprisex04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 02
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows angryx07
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "¡Serás imbécil!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx08
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                                with dissolve

                            d "¡No me vengas con mariconadas ahora!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx07
                                show gensex_missionary_d_head_exp_mouth sad_Silentx07
                                with dissolve

                    "Así puedo ver las muecas raras que haces cada vez que te corres.":
                        call p_Help

                        $pl.ch_pts("dp",1)

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_blush 03
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                        d "Tssk."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                        d "Serás imbécil..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_blush 04
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows sadx07
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                            with dissolve

                    "Me gusta tenerte de frente para ver lo hermosa que eres.":
                        call p_Help

                        $pl.ch_pts("np",-1)
                        $pl.ch_pts("mp",-1)

                        if afternight04__MMouth_Tongue_Success > 1:
                            $pl.ch_pts("dp",2)

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 04
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 06
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx01
                                with dissolve

                            d "¿Qué...?"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils front03
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                                with dissolve

                            d "¿De qué coño hablas tú ahora?"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 06
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils right03
                                show gensex_missionary_d_head_exp_eyebrows serious
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "No me vengas con mariconadas..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils right05
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                                with dissolve

                        else:
                            $pl.ch_pts("dp",-1)

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 04
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_blush 03
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx07
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "¡¿Pero qué clase de jodida mariconada acabas de soltar?!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows angryx08
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                                with dissolve

                            d "¡Déjate de hostias y fóllame de una vez!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx08
                                show gensex_missionary_d_head_exp_mouth sad_Silentx07
                                with dissolve


                    "Prefiero verte de cara que de culo.":
                        call p_Help

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sad_Silentx05
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with dissolve
                        
                        d "Mientras me des duro contra el muro..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils right03
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                            with dissolve

                        d "Bueno,"

                        extend " sobre la cama en este caso..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                        d "Me da un poco igual que postura prefieras."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows serious
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                if p_didac.anal_received > 0:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                        with dissolve

                    d "Espero que por lo menos,"

                    extend " no me la vuelvas a meter por el culo..."

                elif p_didac.blowjob_done > 0:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                        with dissolve

                    d "Por lo menos así no me la metes por la boca."

                if p_didac.pos_doggy > 0:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows surprisex04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                        with dissolve

                    d "Pensé que te estaba gustando más follarme a cuatro patas..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                        with dissolve

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Silentx03
                    with dissolve

            elif p_prot.pos_missionary_rest == 1:

                if p_didac.action == "cunnilingus_done_p_txell":

                    $ Pedrera_char_Cond = "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows surprisex01
                    with fade_short

                    tx "Me imagino que verme desnuda en frente de ti debe ponerte muy caliente..."

                    show m_exp_mouth sad_Talkingx02
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Pero estaría bien que hicieras algo con Dídac para que te corrieras."

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "En el fondo para eso estamos haciendo esto, ¿No?"

                    $ ped_sex_general_zoom_Cond = ""
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with vpunch

                    d "¡Gue me foglle de una vegz!"

                    $ Pedrera_char_Cond = "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 03
                    show m_exp_piris down03
                    show m_exp_eyebrows surprisex001
                    with fade_short

                    tx "Tú calla y sigue,"

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "que no veo que esa lengua se mueva."

                    show m_exp_mouth happybiting_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris down05
                    show m_exp_eyebrows sadx01
                    with dissolve

                    pause 0.2

                    $ ped_sex_general_zoom_Cond = ""
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with fade_short

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                        with dissolve

                    d "¿Te gusta verme con las piernas abiertas,"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                        with dissolve

                    d " o solo te fijas en mis tetas?"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows surprisex02
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                        with dissolve

                    p "Quizás ambas."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                        with dissolve

                    d "También podrías hacer eso mientras me follas,"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                        with dissolve

                    d "¿no crees?"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils right05
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                        with dissolve

            elif p_prot.pos_missionary_rest == 2:

                if p_didac.action == "cunnilingus_done_p_txell":

                    $ Pedrera_char_Cond = "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows surprisex001
                    with fade_short

                    tx "Tengo entendido que no tenemos toda la noche..."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    tx "así que sería buena idea que empezaras a usar esa anaconda tuya con tu amiguito."

                    show m_exp_mouth happybiting_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    d "¡Ghhhmm!"

                    $ ped_sex_general_zoom_Cond = ""
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with fade_short

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                        with dissolve

                    d "Se supone que me has abierto de piernas para hacer algo más que mirarme..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils front00
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx24
                        with dissolve

                    d "¡¿No?!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                        with dissolve

            elif p_prot.pos_missionary_rest >= 3:

                if p_didac.action == "cunnilingus_done_p_txell":

                    $ Pedrera_char_Cond = "TxellSuperClose_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with fade_short

                    $ ped_check_1_10("ped_missionary_rest_txellOver_didac_list")

                    #$ randomnum_1to10 = renpy.random.randint(1, 10)

                    if ped_check_list_result == 1:

                        tx "¿Vas a estar así toda la noche?"

                    elif ped_check_list_result == 2:

                        tx "Te recuerdo que no tenemos toda la noche."

                    elif ped_check_list_result == 3:

                        tx "Sería mejor que empezaras a hacer algo con esa anaconda tuya."

                    elif ped_check_list_result == 4:

                        tx "Dídac está haciendo su trabajo con su lengua,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "pero tú no estás haciendo el tuyo."

                    elif ped_check_list_result == 5:

                        tx "Te recuerdo que la idea es que tienes que correrte tú,"

                        extend " no yo."

                    elif ped_check_list_result == 6:

                        tx "¿Tanto te hipnotiza mi busto,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "que eres incapaz de hacer nada?"

                    elif ped_check_list_result == 7:

                        tx "Me alegro que te gusten tanto mis pechos,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "pero se supone que deberías estar haciendo algo tu miembro viril."

                    elif ped_check_list_result == 8:

                        tx "Como sigas así,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Neus se va a enfadar de verdad."

                    elif ped_check_list_result == 9:

                        tx "¿Tanto te estoy distrayendo que no eres capaz de moverte?"

                    elif ped_check_list_result == 10:

                        tx "Veo que te cuesta..."

                    else:

                        tx "..."

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    pause 0.2

                    $ ped_sex_general_zoom_Cond = "face"
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with vpunch

                    $ randomnum_1to5 = renpy.random.randint(1, 5)

                    if randomnum_1to5 == 1:

                        d "¡HHmmmghh!"

                    elif randomnum_1to5 == 2:

                        d "¡MMmmfghh!"

                    elif randomnum_1to5 == 3:

                        d "¡HUhhmmgh!"

                    elif randomnum_1to5 == 4:

                        d "¡Ghhhmm!"

                    elif randomnum_1to5 == 5:

                        d "¡Fghmmm!"

                    $ Pedrera_char_Cond = "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris down03
                    show m_exp_eyebrows angryx01
                    with fade_short

                    $ ped_check_1_10("ped_missionary_rest_txellOver_didac_02_list")

                    #$ randomnum_1to5 = renpy.random.randint(1, 5)

                    if ped_check_list_result == 1:

                        tx "Tú cállate,"

                        show m_exp_mouth sad_Talkingx03
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        tx "que deberías tener la lengua ocupada."

                    elif ped_check_list_result == 2:

                        tx "En lugar de hablar,"

                        show m_exp_mouth sad_Talkingx03
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        tx "deberías estar haciendo otra cosa con tu lengua."

                    elif ped_check_list_result == 3:

                        tx "Si tienes tiempo de hablar,"

                        show m_exp_mouth sad_Talkingx03
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        tx "eso que no estás haciendo lo que deberías."

                    elif ped_check_list_result == 4:

                        tx "No veo que muevas esa lengua, Dídac."

                    elif ped_check_list_result == 5:

                        tx "Tú cállate y sigue con tu lengua."

                    elif ped_check_list_result == 6:

                        tx "Tú,"

                        extend " ¿Te he dicho que pares?"

                    elif ped_check_list_result == 7:

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows sadx02
                        with dissolve

                        tx "¿Ya te has cansado ahí abajo?"

                        show m_exp_mouth happy_Talkingx07
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "¡Sigue hombre!"

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "Bueno..."

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows sadx02
                        with dissolve

                        tx "ya me entiendes."

                    elif ped_check_list_result == 8:

                        tx "He visto babosas más lentas."

                        show m_exp_mouth sad_Talkingx07
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "¡¿Quieres darle más ritmo a esa lengua tuya?!"

                    elif ped_check_list_result == 9:

                        tx "Espero que no dependas de tu lengua para conquistar a las mujeres,"

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows sadx02
                        with dissolve

                        tx "porque no lograrías convencer ni a mi abuela."

                    elif ped_check_list_result == 10:

                        tx "¡¿Con qué clase de mujeres has estado"

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows sadx02
                        with dissolve

                        tx "para que no tengas ni idea de comerte bien un coño?!"

                    else:

                        tx "Y tú no pares."

                    show m_exp_mouth happybiting_Silentx02
                    show m_exp_eyes 05
                    show m_exp_piris down05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    pause 0.2

                    $ ped_sex_general_zoom_Cond = ""
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with fade_short

                    pause 0.2

                else:

                    $ ped_check_1_10("ped_missionary_rest_didac_list")

                    #$ randomnum_1to10 = renpy.random.randint(1, 10)

                    if ped_check_list_result == 1:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_blush 03
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                        d "¿Vas a estar así toda la noche?..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                    elif ped_check_list_result == 2:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            with dissolve

                        d "Métemela de una vez."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                        call ped_D_NoSex ##########################################

                    elif ped_check_list_result == 3:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                        d "¿A qué estás esperando?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                    elif ped_check_list_result == 4:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                        d "Te tenía por un semental..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            with dissolve

                        d "pero ya veo que eres más vago que una vaca."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                    elif ped_check_list_result == 5:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx175
                            with dissolve

                        d "Me alegro que te guste lo que ves.."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx26
                            with dissolve

                        d "¡Pero úsala de una vez!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                    elif ped_check_list_result == 6:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            with dissolve

                        d "Me estás poniendo de los nervios ahí sin hacer nada..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Silentx13
                            with dissolve

                    elif ped_check_list_result == 7:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                            with dissolve

                        d "Tendría que darte vergüenza,"

                        extend " estar ahí quieto mirando,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx24
                            with dissolve

                        d "¡cuando puedes estar follándome!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                    elif ped_check_list_result == 8:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils down02
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                            with dissolve

                        d "Sino fuera porque la tienes dura como una piedra,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            with dissolve

                        d "pensaría que eres un jodido impotente."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Silentx16
                            with dissolve

                    elif ped_check_list_result == 9:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                            with dissolve

                        d "Tssk..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Silentx13
                            with dissolve

                    elif ped_check_list_result == 10:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Silentx13
                            with dissolve

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            show gensex_missionary_d_head_exp_mouth sad_Silentx13
                            with dissolve

        call afternight05_Pedrera_Neus_Warning

################################################################################
############################################################ BUTTOCKS SLAP

    elif p_prot.b_action == "buttocks_slap":

        $ p_didac.buttockSlaps_received += 1

        if p_didac.buttockSlaps_received in [1, 3, 5, 7, 9, 11]:
            if p_d_butS_R < 6:
                $ p_d_butS_R += 1
        if p_didac.buttockSlaps_received in [2, 4, 6, 8, 10, 12]:
            if p_d_butS_L < 6:
                $ p_d_butS_L += 1

        $ ped_sex_general_zoom_Cond = "butt"
        call pedrera_sex_p_general_talk

        if p_didac.buttockSlaps_received in [1, 3, 5, 7, 9, 11]:
            show smack 00:
                truecenter
                xpos 0.62 ypos 0.35
                pedrera_sex_buttSmack_base_pos
        elif p_didac.buttockSlaps_received in [2, 4, 6, 8, 10, 12]:
            show smack 00:
                truecenter
                xpos 0.38 ypos 0.35
                pedrera_sex_buttSmack_inverse_pos
        else:
            show smack 00:
                truecenter
                xpos 0.62 ypos 0.35
                pedrera_sex_buttSmack_base_pos

        with hpunch

        if p_didac.buttocks_pain > 5:

            $ p_didac.buttocks_pain_received += 1

            call pedrera_sex_p_general_talk
            with hpunch

            $ ped_check_1_5("ped_buttocks_pain_didac_list")

            #$ randomnum_1to5 = renpy.random.randint(1, 5)

            if ped_check_list_result == 1:

                d "{size=35}¡¡AUUH!!{/size}"

            elif ped_check_list_result == 2:

                d "{size=35}¡¡AUUCH!!{/size}"

            elif ped_check_list_result == 3:

                d "{size=35}¡¡OUUCH!!{/size}"

            elif ped_check_list_result == 4:

                d "{size=35}¡¡AAIIH!!{/size}"

            elif ped_check_list_result == 5:

                d "{size=35}¡¡AAAUUUH!!{/size}"

            else:

                d "{size=35}¡¡AAAUUUH!!{/size}"


            ###

            $ ped_check_1_5("ped_buttocks_pain_didac_list_02")

            #$ randomnum_1to5 = renpy.random.randint(1, 5)

            # show gensex_missionary_d_head_exp_eyes 03
            # show gensex_missionary_d_head_exp_pupils front03
            # show gensex_missionary_d_head_exp_eyebrows angryx08
            # show gensex_missionary_d_head_exp_mouth sad_Talkingx24
            # with dissolve

            if ped_check_list_result == 1:

                d "¡HIJO DE PUTA!"

            elif ped_check_list_result == 2:

                d "¡QUE PARES YA COÑO!"

            elif ped_check_list_result == 3:

                d "¡QUE ME DEJES EL CULO EN PAZ!"

            elif ped_check_list_result == 4:

                d "¡AL FINAL TE VOY A PARTIR LA CARA!"

            elif ped_check_list_result == 5:

                d "¡TE LA ESTÁS JUGANDO!"

            else:

                d "..."

            ###

            if p_didac.buttocks_pain_received == 1:

                d "¡QUE ME HACES DAÑO JODER!"

            elif p_didac.buttocks_pain_received == 2:

                d "¡TE HE DICHO QUE DUELE!"

            elif p_didac.buttocks_pain_received == 3:

                d "¡¿QUÉ ES LO QUE NO ENTIENDES?!"

            elif p_didac.buttocks_pain_received == 4:

                d "¡ME ESTÁS DEJANDO EL CULO ROJO!"

            elif p_didac.buttocks_pain_received == 5:

                d "¡ACABARÉ HACIÉNDOTE LO MISMO Y VERÁS!"


        else:  # NO PAIN ON THE BUTTOCKS

            #$ p_didac_buttocks_pain_received_from_p_prot += 1
            $ p_didac.buttockSlaps_well_received += 1

            $ ped_check_1_5("ped_buttocksSlap_didac_list")

            #$ randomnum_1to5 = renpy.random.randint(1, 5)

            #ono "splash{nw}{w=0.2}"

            if ped_check_list_result == 1:

                d "¡Au...!"

            elif ped_check_list_result == 2:

                d "¡Aii...!"

            elif ped_check_list_result == 3:

                d "¡Auch...!"

            elif ped_check_list_result == 4:

                d "¡Iaauh...!"

            elif ped_check_list_result == 5:

                d "¡AAh...!"

            else:

                d "Hmmm..."

            
            ###

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            if p_didac.buttockSlaps_well_received == 1:

                # show gensex_missionary_d_head_exp_eyes 02
                # show gensex_missionary_d_head_exp_pupils front02
                # show gensex_missionary_d_head_exp_eyebrows angryx07
                # show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                # with dissolve

                d "¡La madre que te parió!"

                d "¡¿Por qué demonios me das una hostia en la nalga ahora?!"

                p "Porque tienes unas nalgas bien ricas."

                d "..."

                if (afternight04__RButtock_Slap_Done > 2) and (afternight04__LButtock_Slap_Done > 2):

                    p "Como si ayer te hubieras quejado mucho de esto..."

                    p "Admite de una vez que te gusta ser tratada como a una perra en celo."

                    if (afternight04__RButtock_Slap_Success > afternight04__RButtock_Slap_Failed) and (afternight04__LButtock_Slap_Success > afternight04__LButtock_Slap_Failed):

                        d "..."

                        d "Tssk..."

                        d "Eres un imbécil."

                    else:

                        d "¡¿En serio?!"

                        d "¡¿Con el daño que me hiciste?!"

                        d "¿Aún tienes los santos cojones de decir eso?"

                        p "..."

                        d "Déjate de tonterías de una vez..."

                        d "y fóllame como es debido."

                        d "¡Coño!"

                else:

                    p "Dan ganas de apretarlas con fuerza y azotarlas."

                    d "..."

                    d "Mira que eres capullo..."

            elif p_didac.buttockSlaps_well_received > 1:

                $ ped_check_1_10("ped_buttocksSlaps_well_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    d "Hijo de puta..."

                elif ped_check_list_result == 2:

                    d "La madre que te parió..."

                elif ped_check_list_result == 3:

                    d "Serás cabronazo..."

                elif ped_check_list_result == 4:

                    d "Eres un..."

                elif ped_check_list_result == 5:

                    d "Me cago en tus muertos..."

                elif ped_check_list_result == 6:

                    d "Maldito cabrón..."

                elif ped_check_list_result == 7:

                    d "Cabronazo..."

                elif ped_check_list_result == 8:

                    d "Maldito seas..."

                elif ped_check_list_result == 9:

                    d "Tsskk..."

                elif ped_check_list_result == 10:

                    d "Joder..."

                else:

                    d "..."

                $ ped_sex_general_zoom_Cond = ""


                if p_didac.vaginal_received or p_didac.vaginalDeep_received:

                    $ ped_check_1_5("ped_buttocksSlaps_well_vaginalSex_didac_list")

                    if ped_check_list_result == 1:

                        d "Azótame si quieres..."

                        d "¡Pero no dejes de follarme, coño!"

                    elif ped_check_list_result == 2:

                        d "Hmmm..."

                        p "Te gusta,"

                        extend " ¿Verdad?"

                        d "¡Calla y sigue!"

                        p "¿Azotándote?"

                        d "Imbécil..."

                    elif ped_check_list_result == 3:

                        d "¿Me quieres dejar las nalgas rojas?"

                        p "Me gusta oírte gemir así."

                        d "Tssk..."

                        d "Serás capullo..."

                    elif ped_check_list_result == 4:

                        d "Tskk..."

                    elif ped_check_list_result == 5:

                        p "Reconoce que te gusta."

                        d "Vete a la mierda."

                else:

                    $ ped_check_1_5("ped_buttocksSlaps_well_vaginalSexNO_didac_list")

                    if ped_check_list_result == 1:

                        d "Si me quieres azotar,"

                        extend " hazlo..."

                        d "¡Pero por lo menos fóllame!"

                    elif ped_check_list_result == 2:

                        if p_didac.vaginal_received > 0:

                            d "¡¿Cuando piensas volver a follarme?!"

                        else:

                            d "¡¿Cuando piensas follarme?!"

                    elif ped_check_list_result == 3:

                        d "¡¿Disfrutas más azotándome que follándome?!"

                        p "..."

                        d "Imbécil..."

                    elif ped_check_list_result == 4:

                        d "¡En serio!"

                        d "¡Métemela de una vez!"

                        call ped_D_NoSex ##########################################

                    elif ped_check_list_result == 5:

                        d "¡Métemela joder!"

                    else:

                        d "Tsk..."

                    ##

                    if p_didac.anal_received or p_didac.analDeep_received:

                        $ ped_check_1_5("ped_buttocksSlaps_well_vaginalSexNO_didac_02_list")

                        if ped_check_list_result == 1:

                            p "Ya te estoy follando..."

                            d "¡POR EL CULO JODER!"

                            d "¡NO ES POR AHÍ DÓNDE QUIERO QUE ME LA METAS!"

                        elif ped_check_list_result == 2:

                            d "¡Y me refiero por el coño!"

                        elif ped_check_list_result == 3:

                            d "Y no me refiero por el culo!"

                        elif ped_check_list_result == 4:

                            d "¡Y sabes que prefiero el coño!"

                        elif ped_check_list_result == 5:

                            d "Y no me hagas repetirlo..."


                p "..."

        # $ ped_sex_general_zoom_Cond = ""
        # call pedrera_sex_p_general_talk
        # with fade_short

        call afternight05_Pedrera_Neus_Warning

        $ p_prot.b_action = "rest"

################################################################################
############################################################ KISS # AFTER REST, because you end up doing a Rest.


    elif p_prot.b_action in ["kiss_TRY", "kiss_done"]:

        # DOES SHE ALLOW IT?

        call pedrera_general_kiss

        show kiss_ n_d_01:
            truecenter
        with fade

        if afternight04__MMouth_Tongue_Success == 0:

            $ p_prot_kiss_p_didac_FAIL += 1

            if p_prot_kiss_p_didac_FAIL > 1:

                pause 0.2

                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk

            if p_prot_kiss_p_didac_FAIL == 1:

                n "Acercas sugerentemente tus labios a los suyos."

                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                #$ ped_sex_general_action_Cond = "talk"
                call pedrera_sex_p_general_talk

                #if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell": ## THIS IS NOT NECESSARY. (You can't kiss Didac otherwise.)
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows angryx08
                show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                with vpunch

                d "¡¿Qué coño haces?!"

                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils front04
                show gensex_missionary_d_head_exp_eyebrows angryx08
                show gensex_missionary_d_head_exp_mouth sad_Silentx08
                with dissolve

                p "¿Euh...?"

                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows angryx08
                show gensex_missionary_d_head_exp_mouth sad_Silentx10
                with dissolve

                p "Pues besarte."

                if aftermorning05_SunScreenMassage_FrontParts_Neck_Strangle_Cond:

                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                    with dissolve

                    p "Como me has besado esta mañana."

                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                with dissolve

                d "¡¿Estás de coña?!"

                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils front03
                show gensex_missionary_d_head_exp_eyebrows angryx07
                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                with dissolve

                d "¡Te he dicho cien veces que esto es una jodida mariconada!"

                if aftermorning05_SunScreenMassage_FrontParts_Neck_Strangle_Cond:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                    with dissolve

                    d "Lo de esta mañana ha sido simplemente para evitar problemas..."

                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx11
                    with dissolve

                    d "¡¿O es que querías que te metieran de hostias?!"

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Silentx09
                    with dissolve

                    p "..."

                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows angryx07
                show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                with dissolve

                if p_didac.b_action not in ["vaginal_received", "vaginalDeep_received"]:

                    d "¡Déjate de gilipolleces y fóllame de una puta vez!"

                else:

                    d "¡Déjate de gilipolleces y céntrate en follarme!"

                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx05
                show gensex_missionary_d_head_exp_mouth sad_Silentx07
                with dissolve

            elif p_prot_kiss_p_didac_FAIL == 2:

                d "¡Te recuerdo que hace dos días era un tío!"

                p "Pero bien que me pides que te folle..."

                d "¡Eso no tiene nada que ver!"

                p "..."

            elif p_prot_kiss_p_didac_FAIL == 3:

                d "¡¿Desde cuando te van estas mariconadas?!"

            elif p_prot_kiss_p_didac_FAIL >= 4:

                $ ped_check_1_10("ped_kiss_FAIL_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx11
                    with vpunch

                    d "¡¿Otra vez?!"

                elif ped_check_list_result == 2:

                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx14
                    with vpunch

                    d "¡¿Es que hablo otro idioma?!"

                elif ped_check_list_result == 3:

                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx12
                    with vpunch

                    d "¡Aparta tu cara de la mía!"

                elif ped_check_list_result == 4:

                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                    with vpunch

                    d "¡No pienso besarte!"

                elif ped_check_list_result == 5:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx11
                    with vpunch

                    d "¡¿Acaso no recuerdas que soy Dídac?!"

                elif ped_check_list_result == 6:

                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                    with vpunch

                    d "¡¿Qué es lo que no entiendes?!"

                elif ped_check_list_result == 7:

                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                    with vpunch

                    d "¡Te he dicho que no voy a besarte!"

                elif ped_check_list_result == 8:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows angryx07
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                    with dissolve

                    d "¡Paso de estas mariconadas!"

                elif ped_check_list_result == 9:

                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                    with vpunch

                    d "¡AL FINAL TE VOY A METER UNA HOSTIA!"

                elif ped_check_list_result == 10:

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                    with vpunch

                    d "¡Al final pensaré que el mariquita eres tú!"

                else:

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                    with vpunch

                    d "¡PARA YA!"

                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx07
                show gensex_missionary_d_head_exp_mouth sad_Silentx09
                with dissolve

            p "..."

        else:

            $ debug ("Character kisses Didac on her lips.")

            $ p_prot.kiss_p_didac += 1
            $ p_prot.kiss_done += 1
            $ p_didac.kiss_received += 1

            $ p_prot.b_action = "kiss_done"
            $ p_didac.b_action = "kiss_received"

            if p_prot.kiss_p_didac == 1:

                show kiss_ f_d_07:
                    truecenter
                with Dissolve(0.5)

                n "Acercas tus labios a los suyos"

                show kiss_ f_d_05
                with Dissolve(0.5)

                show kiss_ f_d_12
                with Dissolve(0.5)

                n "y sugerentemente os unís en un suave y profundo beso"

                show kiss_ f_d_03
                with Dissolve(0.5)

                show kiss_ f_d_11
                with Dissolve(0.5)

                n "entremezclando vuestras lenguas."

                show kiss_ f_d_10
                with Dissolve(0.5)

                show kiss_ f_d_02
                with Dissolve(0.5)

                #$ ped_sex_blow_MChand = "off"
                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                #$ ped_sex_general_action_Cond = "talk"
                call pedrera_sex_p_general_talk

                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx01
                with fade_long1s

                pause 0.5

                show gensex_missionary_d_head_exp_eyes 00
                show gensex_missionary_d_head_exp_pupils front00
                show gensex_missionary_d_head_exp_eyebrows surprisex04
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                with dissolve

                pause 0.2

                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows sadx06
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                with dissolve

                d "..."

                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows angryx08
                show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                with dissolve

                d "Espero que esto te sirva para ponerte más caliente,"

                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils front04
                show gensex_missionary_d_head_exp_eyebrows angryx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                with dissolve

                d "pero no para que te me corras más pronto..."

                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils right05
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                with dissolve

            if p_prot.kiss_p_didac > 1:

                show kiss_ f_d_10:
                    truecenter
                with Dissolve(0.5)

                show kiss_ f_d_02
                with Dissolve(0.5)

                $ ped_sex_general_zoom_Cond = "face"
                $ ped_sex_general_expression_Cond = "talk"
                #$ ped_sex_general_action_Cond = "talk"
                call pedrera_sex_p_general_talk

                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx01
                with fade_long1s

                if p_prot.kiss_p_didac == 2:

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils right04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                    with dissolve

                    d "¿Te pone cachondo besarme?"

                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows surprisex04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                    with dissolve

                    p "A ti más que a mi."

                    show gensex_missionary_d_head_exp_blush 04
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils right04
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                    with dissolve

                    d "Gilipollas..."

                    show gensex_missionary_d_head_exp_blush 06
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                    with dissolve

                elif p_prot.kiss_p_didac == 3:

                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows surprisex02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                    with dissolve

                    p "No me negarás que esto no te pone caliente..."

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                    with dissolve

                    d "Serás capullo..."

                    show gensex_missionary_d_head_exp_blush 04
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                    with dissolve

                elif p_prot.kiss_p_didac == 4:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                    with dissolve

                    d "No hace falta que hagas esto para ponerme más caliente..."

                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows surprisex04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                    with dissolve

                    p "¿Quien te dice que no lo disfruto yo también?"

                    show gensex_missionary_d_head_exp_blush 04
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                    with dissolve

                    d "..."

                    show gensex_missionary_d_head_exp_blush 06
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                    with dissolve

                elif p_prot.kiss_p_didac == 5:

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                    with dissolve

                    d "Cualquiera diría que te pone más caliente besarme que follarme."

                    if p_prot.action in ["vaginal_done", "vaginalDeep_done"]:

                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows surprisex02
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                        with dissolve

                        p "¿Quiere que pare?"

                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                        with dissolve

                        d "¡Ni se te ocurra!"

                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                        with dissolve

                    else:

                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                        with dissolve


                else:

                    if p_prot.action in ["vaginal_done", "vaginalDeep_done"]:

                        $ ped_check_1_10("ped_kiss_vaginal_didac_list")

                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils down04
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                            d "Mientras no pares ahí abajo..."

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils right04
                            show gensex_missionary_d_head_exp_eyebrows normal
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                            with dissolve

                            d "haz las mariconadas que quieras."

                            show gensex_missionary_d_head_exp_blush 04
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils right00
                            show gensex_missionary_d_head_exp_eyebrows surprisex04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                            p "¿Por eso te estremeces tanto cada vez que te beso?"

                            show gensex_missionary_d_head_exp_blush 06
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                            d "..."

                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils right03
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                            d "Tssk..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 2:

                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                            with dissolve

                            d "No pares..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 3:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                            d "Tampoco está tan mal si lo haces mientras me estás follando..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        elif ped_check_list_result == 4:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with dissolve

                            d "Me gusta sentirla dentro..."

                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                            p "¿Mi lengua o mi polla?"

                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils right01
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sabiting_Silentx04
                            with dissolve

                            d "..."

                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils left02
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx11
                            with dissolve

                            d "¿No pueden ser ambas?"

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx06
                            with dissolve

                        elif ped_check_list_result == 5:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                            d "Parece que sabes hacer hasta dos cosas a la vez y todo..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        elif ped_check_list_result == 6:

                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx07
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with dissolve

                            d "Al final me va a gustar y todo si sigues así..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
                            with dissolve

                        elif ped_check_list_result == 7:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                            d "Me estás poniendo bien cachonda, cabrón..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        elif ped_check_list_result == 8:

                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx06
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                            with dissolve

                            d "Dios..."

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx11
                            with dissolve

                            d "Al final resulta que saber ser un buen semental y todo..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        elif ped_check_list_result == 9:

                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx11
                            with dissolve

                            d "Sígueme dando duro mamón."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        elif ped_check_list_result == 10:

                            d "Hmmm..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        else:

                            d "Hmmm..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve


                    else:

                        $ ped_check_1_10("ped_kiss_vaginalNO_didac_list")

                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils down04
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "¡¿Cuánto vas a tardar en metérmela?!"

                            else:

                                d "¡¿Cuánto vas a tardar en volver a metérmela?!"

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 2:

                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            d "Bésame lo que quieras,"

                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "¡pero la quiero dentro!"

                            else:

                                d "¡pero la quiero otra vez dentro!"

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 3:

                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                            with dissolve

                            d "Muy besucón..."

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "pero sigo esperando que me la metas..."

                            else:

                                d "pero sigo esperando que me la vuelvas a meter..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 4:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "¿Vas a tardar en metérmela?"

                            else:

                                d "¿Vas a tardar mucho en volver a metérmela?"

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 5:

                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            d "[protname],"

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx07
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "fóllame..."

                            else:

                                d "fóllame otra vez..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx06
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 6:

                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            d "Cualquiera diría que te estás enamorando de mi besándome tanto..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 7:

                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            with dissolve

                            d "¿Qué tiene mi lengua que no tenga mi coño?"

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 8:

                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            d "Si no vas a usar tu polla,"

                            extend " por lo menos podrías poner tu lengua ahí abajo..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        elif ped_check_list_result == 9:

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                            with dissolve

                            d "¿Qué tengo que hacer para que me folles?"

                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth sad_Silentx11
                            with dissolve

                        elif ped_check_list_result == 10:

                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            with dissolve

                            d "Vale,"

                            extend " no me disgusta..."

                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                            if p_didac.vaginal_received == 0:

                                d "pero al menos me la podrías meter dentro..."

                            else:

                                d "pero al menos podrías volver a metérmela..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                        else:

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                            d "..."

                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                            with dissolve


        $ p_prot.b_action = "rest"
        $ p_didac.b_action = "rest"

############################################################################################################
################################################################################################
############################################################################################################
################################################################################################
############################################################################################################
################################################################################################
        #if p_prot.b_action not in ["kiss_TRY", "kiss_done"]:

        if p_prot.pos_missionary_rest == 0 or p_prot.pos_doggy_rest == 0:

            call afternight05_Pedrera_Sex_p_didac_common
                # d "¡Métemela de una vez!"
                # p "¿No preferirías un poco de preliminares antes?"
                # d "¡¿Más preliminares?!"
                # d "¡Estoy hasta los cojones de los preliminares!"
                # d "¡Fóllame de una vez!"

        call afternight05_Pedrera_Neus_Warning

        ## FOR DOGGYSTYLE AND MISSIONARY

################################################################################
############################################################ CUNNILINGUS


    elif p_prot.action == "cunnilingus_done": # Doggystyle or Missionary (not 69)

        $ p_prot.cunnilingus_done += 1
        $ p_didac.cunnilingus_received += 1
        $ p_didac.cunnilingus_missionary_received += 1

        #$ p_didac.b_action = "cunnilingus_received" # What about "cunnilingus_done_p_txell"???
        #$ p_prot.action ="cunnilingus_done"

        #$ p_didac_cunnilingus_done_to_p_didac += 1

        #$ ped_sex_blow_MChand = "off"
        $ ped_sex_general_zoom_Cond = "crotch"
        $ ped_sex_general_expression_Cond = "closed"
        if p_didac.cunnilingus_received >= 6:
            $ ped_sex_general_action_Cond = "vt02_05"
        elif p_didac.cunnilingus_received == 5:
            $ ped_sex_general_action_Cond = "vt02_03"
        elif p_didac.cunnilingus_received == 4:
            $ ped_sex_general_action_Cond = "vt02_01"
        elif p_didac.cunnilingus_received == 3:
            $ ped_sex_general_action_Cond = "vt01_04"
        elif p_didac.cunnilingus_received == 2:
            $ ped_sex_general_action_Cond = "vt01_02"
        elif p_didac.cunnilingus_received == 1:
            $ ped_sex_general_action_Cond = "vt00_01"
        else:
            aj "ERROR 5647984"
        call pedrera_sex_p_general_talk

        $ ped_check_1_10("ped_cunnilingus_moan_didac_list")

        #$ randomnum_1to10 = renpy.random.randint(1, 10)

        if ped_check_list_result == 1:

            d "Hmmm..."

        elif ped_check_list_result == 2:

            d "Mmnfh..."

        elif ped_check_list_result == 3:

            d "Ahmmn..."

        elif ped_check_list_result == 4:

            d "Uhmm..."

        elif ped_check_list_result == 5:

            d "Mmmnn..."

        elif ped_check_list_result == 6:

            d "Aaahmm..."

        elif ped_check_list_result == 7:

            d "Hgmmmn..."

        elif ped_check_list_result == 8:

            d "Hhghmm..."

        elif ped_check_list_result == 9:

            d "Dios..."

        elif ped_check_list_result == 10:

            d "Joder..."

        else:

            d "Hmmm..."

        #$ debug ("Protagonista haciéndole un cunnilingus a Dídac.")

        #if p_didac_cunnilingus_done_to_p_didac == 1:
        if p_didac.cunnilingus_missionary_received == 1:

            window hide dissolve
            pause

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk

            if p_didac.action == "cunnilingus_done_p_txell":
                $ ped_sex_general_expression_Cond = "closed"
            else:
                $ ped_sex_general_expression_Cond = "talk"

            call pedrera_sex_p_general_talk

            if p_didac.action == "cunnilingus_done_p_txell":

                tx "Usando tu lengua..."

                tx "Me alegra ver que no eres simple testosterona pura, [protname]."

                p "..."

            else:

                if p_didac.cunnilingus_received == 1:
                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx06
                        with dissolve

                    d "¿Qué-"

                    extend "qué estás ha...?"

                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils down00
                        show gensex_missionary_d_head_exp_eyebrows surprisex03
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                        with dissolve

                else:
                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows sadx02
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx05
                        with dissolve

                    d "No te diré que no..."

                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils down04
                        show gensex_missionary_d_head_exp_eyebrows sadx03
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx05
                        with dissolve

            pause 0.2

            $ ped_sex_general_zoom_Cond = "crotch"
            $ ped_sex_general_expression_Cond = "closed"
            $ ped_sex_general_action_Cond = "vt01_01"
            call pedrera_sex_p_general_talk
            with fade

            n "Sugerentemente te acercas a sus labios menores"

            n "y acaricias con tu lengua su tierna piel."


        $ ped_sex_general_zoom_Cond = "face"

        if p_didac.action == "cunnilingus_done_p_txell":
            $ ped_sex_general_expression_Cond = "closed"
        else:
            $ ped_sex_general_expression_Cond = "talk"

        call pedrera_sex_p_general_talk

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                with fade_short

            d "AAAHHmmm..."

        elif randomnum_1to5 == 2:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                with fade_short

            d "MMfhmm..."

        elif randomnum_1to5 == 3:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx05
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                with fade_short

            d "HHMmhm..."

        elif randomnum_1to5 == 4:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 07
                show gensex_missionary_d_head_exp_pupils front07
                show gensex_missionary_d_head_exp_eyebrows sadx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                with fade_short

            d "Ah-aahmm..."

        elif randomnum_1to5 == 5:

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx05
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx11
                with fade_short

            d "Mmmmhm..."


        if p_didac.action == "cunnilingus_done_p_txell":
            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab


        #if p_didac_cunnilingus_done_to_p_didac == 1:
        if p_didac.cunnilingus_received == 1:

            if p_didac.action == "cunnilingus_done_p_txell":
                
                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows sadx02
                with fade_short

                tx "¿Ahora te da para usar la lengua a ti también?"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Si tu intención es hacer un trenecito oral,"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows sadx01
                with dissolve

                tx "lo lamento mucho,"

                # FOR FUTURE # DIFFERENT OUTCOMES.

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx01
                with dissolve

                tx "pero no pienso pasar mi lengua por tus partes..."

                if p_txell.seal == "sealed":

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    p "Ya lo has hecho antes."

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "Y no pienso volver a hacerlo..."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                else:

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    p "¿Y por dónde vas a querer que me corra entonces?"

                    show m_exp_mouth sadbiting_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "..."

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    tx "Una cosa es que te corras en mi boca en el último instante mientras te estás masturbando."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx03
                    with dissolve

                    tx "Y la otra muy distinta es que yo haga que te corras en mi boca."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    p "..."

            else:

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                    with dissolve

                d "¿Qué-"

                extend "qué demonios se supone que estás haciendo?"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows surprisex02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    with dissolve

                p "¿No es obvio?"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                    with dissolve

                d "..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                    with dissolve

                pause 0.2

        #elif p_didac_cunnilingus_done_to_p_didac == 2:
        elif p_didac.cunnilingus_missionary_received == 2:

            if p_didac.action == "cunnilingus_done_p_txell":

                if p_txell.cunnilingus_received > 0: # Only for MC?

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows surprisex001
                    with fade_short

                    tx "Por lo visto no soy la única que he disfrutado de tu habilidosa lengua..."

                else:

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows surprisex001
                    with fade_short

                    tx "Por lo visto no se te da tan mal usar la lengua ahí abajo..."

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    p "Te sorprenderías..."

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Quizás puedas demostrármelo más tarde."

                    show m_exp_mouth sadbiting_Silentx04
                    show m_exp_eyes 00
                    show m_exp_piris front00
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    p "Quizás si me lo pides amablemente."

                    show m_exp_mouth sadbiting_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx03
                    with dissolve

                    tx "..."

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows angryx02
                    with dissolve

                    tx "Pff..."

                    show m_exp_mouth sadbiting_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows sadx01
                    with dissolve

            else:

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows sadx01
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                    with dissolve

                d "Joder..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx006
                    with dissolve

                d "Lo que quiero..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx04
                    with dissolve

                d "es que..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 06
                    show gensex_missionary_d_head_exp_pupils front06
                    show gensex_missionary_d_head_exp_eyebrows sadx06
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                    with dissolve

                d "Hhmmm..."

        #elif p_didac_cunnilingus_done_to_p_didac == 3:
        elif p_didac.cunnilingus_missionary_received == 3:

            if p_didac.action == "cunnilingus_done_p_txell":

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris down03
                show m_exp_eyebrows angryx02
                with fade_short

                tx "¡Tú!"

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris down02
                show m_exp_eyebrows angryx03
                with dissolve

                tx "¡Deja de gemir tanto y no detengas esa lengua tuya!"

                show m_exp_mouth happybiting_Silentx03
                show m_exp_eyes 04
                show m_exp_piris down04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                d "¡Hmmm!"

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Seh,"

                extend " seh..."

                show m_exp_mouth happy_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_eyebrows sadx02
                with dissolve

                tx "Grita lo que quieras,"

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 03
                show m_exp_piris down03
                show m_exp_eyebrows angryx02
                with dissolve

                tx "pero no pares."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_eyebrows angryx02
                with dissolve

            else:

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                    with dissolve

                d "Preferiría que me follaras..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows surprisex02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                    with dissolve

                p "¿Quieres que pare?"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils right04
                    show gensex_missionary_d_head_exp_eyebrows angryx02
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    with dissolve

                d "..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows sadx05
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                    with dissolve

        #elif p_didac_cunnilingus_done_to_p_didac == 4:
        elif p_didac.cunnilingus_missionary_received == 4:

            if p_didac.action == "cunnilingus_done_p_txell":

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_eyebrows angryx02
                with fade_short

                tx "¿Qué te he dicho antes?"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 03
                show m_exp_piris down03
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Aprende un poco de él..."

                if p_txell.cunnilingus_received > 0:

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "Que sinceramente,"

                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    tx "no lo hace tan mal..."

                else:

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "que seguro que lo hace mejor que tú."

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 03
                show m_exp_piris down03
                show m_exp_eyebrows angryx03
                with dissolve

                tx "¡Sigue moviendo esa lengua, gandul!"

                show m_exp_mouth happybiting_Silentx05
                show m_exp_eyes 04
                show m_exp_piris down04
                show m_exp_eyebrows sadx02
                with dissolve

            else:

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx03
                    with dissolve

                d "Me imagino que se te da bien usar la lengua"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                    with dissolve

                d "porque raramente se la podrás meter a ninguna pava"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils down03
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx05
                    with dissolve

                d "sin un poco de lubricación con el tamaño que calzas..."

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx01
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx03
                    with dissolve

                d "¿O me equivoco?"

                if p_prot.pos == "missionary":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx02
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx04
                    with dissolve

                p "..."

        else: # More than 4.

            if p_didac.action == "cunnilingus_done_p_txell":

                $ ped_check_1_10("ped_cunnilingus_to_p_txell_didac_list")

                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                $ Pedrera_char_Cond = "TxellSuperClose_show"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris down04
                show m_exp_eyebrows suspiciousx01
                with fade_short

                if ped_check_list_result == 1:

                    tx "Tan gallito en la escuela"

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows sadx03
                    with dissolve

                    tx "y te detienes cuando recibes un poco de placer..."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 03
                    show m_exp_piris down03
                    show m_exp_eyebrows sadx02
                    with dissolve

                    tx "Que machito más cutre eres..."

                elif ped_check_list_result == 2:

                    tx "¿Este es tu nivel?"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "¿No das para más?"

                elif ped_check_list_result == 3:

                    tx "Aprende un poco más de tu amigo..."

                elif ped_check_list_result == 4:

                    tx "Una pensando que el haberte convertido en mujer habrías aprendido algo,"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "y tu amigo lo hace mejor que tú."

                elif ped_check_list_result == 5:

                    tx "¡Pero no te detengas!"

                elif ped_check_list_result == 6:

                    tx "¡Aprende un poco más de tu amigo!"

                elif ped_check_list_result == 7:

                    tx "¡¿Por qué te detienes?!"

                elif ped_check_list_result == 8:

                    tx "¡¿Es que no sabes gemir y lamer al mismo tiempo?!"

                elif ped_check_list_result == 9:

                    tx "Y pensar que el haberte convertido en mujer"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "no te ha ayudado en nada para entender como se lame en condiciones un coño..."

                elif ped_check_list_result == 10:

                    tx "¿Te he dicho que pares?"

                else:

                    tx "¡No pares esa lengua!"

                show m_exp_mouth happybiting_Silentx04
                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_eyebrows angryx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab
                with fade_short

                call p_didac_insult_blockedmouth

            else:

                $ ped_check_1_10("ped_missionary_cunnilingus_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                    with dissolve

                    if p_didac.orgasm == 0:

                        d "Al final conseguirás que tenga un orgasmo si sigues así..."

                    else:

                        d "Al final conseguirás que tenga otro orgasmo si sigues así..."

                elif ped_check_list_result == 2:

                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils down02
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                    with dissolve

                    d "¿Me lo parece a mi o tienes una lengua bastante larga?"

                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
                    with dissolve

                    p "..."

                elif ped_check_list_result == 3:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                    with dissolve

                    d "Ya que no vas a usar tu polla,"

                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                    with dissolve

                    d "al menos no pares esa lengua tuya..."

                elif ped_check_list_result == 4:

                    show gensex_missionary_d_head_exp_eyes 07
                    show gensex_missionary_d_head_exp_pupils front07
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx05
                    with dissolve

                    d "Eres jodidamente bueno con esto,"

                    extend " hijo de puta..."

                elif ped_check_list_result == 5:

                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                    with dissolve

                    d "Se nota que no es tu primera vez,"

                    extend " cabronazo..."

                elif ped_check_list_result == 6:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows normal
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx002
                    with dissolve

                    d "Reconozco que no se te da tan mal..."

                elif ped_check_list_result == 7:

                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                    with dissolve

                    d "No pares..."

                elif ped_check_list_result == 8:

                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows sadx05
                    show gensex_missionary_d_head_exp_mouth happy_Talkingx03
                    with dissolve

                    d "¿Quien lo iba a decir que me estarías comiendo el coño hace sólo tres días?"

                elif ped_check_list_result == 9:

                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx04
                        with dissolve

                    d "Cabrón..."

                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                        with dissolve

                    d "Se te da bien..."

                    if p_prot.pos == "missionary":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx06
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx06
                        with dissolve

                elif ped_check_list_result == 10:

                    show gensex_missionary_d_head_exp_eyes 07
                    show gensex_missionary_d_head_exp_pupils front07
                    show gensex_missionary_d_head_exp_eyebrows sadx07
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                    with dissolve

                    d "..."

                else:

                    show gensex_missionary_d_head_exp_eyes 07
                    show gensex_missionary_d_head_exp_pupils front07
                    show gensex_missionary_d_head_exp_eyebrows sadx07
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                    with dissolve

                    d "..."

                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows sadx06
                show gensex_missionary_d_head_exp_mouth happybiting_Silentx06
                with dissolve

        # Image licking her pussy.

        call afternight05_Pedrera_Neus_Warning

        $ ped_sex_general_zoom_Cond = "crotch"
        $ ped_sex_general_expression_Cond = "closed"

        # NEW

        if p_didac.cunnilingus_received >= 6:
            $ ped_sex_general_action_Cond = "vt02_05"
        elif p_didac.cunnilingus_received == 5:
            $ ped_sex_general_action_Cond = "vt02_04"
        elif p_didac.cunnilingus_received == 4:
            $ ped_sex_general_action_Cond = "vt02_02"
        elif p_didac.cunnilingus_received == 3:
            $ ped_sex_general_action_Cond = "vt01_05"
        elif p_didac.cunnilingus_received == 2:
            $ ped_sex_general_action_Cond = "vt01_03"
        elif p_didac.cunnilingus_received == 1:
            $ ped_sex_general_action_Cond = "vt01_01"
        else:
            aj "ERROR 36854"
        call pedrera_sex_p_general_talk
        with fade

        p "..."

        

################################################################################
############################################################ ANILINGUS

    elif p_prot.action == "anilingus_done": # Only DoggyStyle if I'm not wrong.

        $ p_prot.anilingus_done += 1
        $ p_didac.anilingus_received += 1
        $ p_didac.anal_dilatation += 1

        #$ p_prot_anilingus_done_to_p_didac += 1

        $ ped_sex_general_zoom_Cond = "ass"

        if p_didac.anilingus_received == 1:
            $ ped_sex_general_action_Cond = "at00_00"
        elif p_didac.anilingus_received == 2:
            $ ped_sex_general_action_Cond = "at01_01"
        elif p_didac.anilingus_received == 3:
            $ ped_sex_general_action_Cond = "at01_02"
        elif p_didac.anilingus_received == 4:
            $ ped_sex_general_action_Cond = "at01_03"
        else:
            $ ped_sex_general_action_Cond = "at01_04"
        call pedrera_sex_p_general_talk
        with fade

        $ debug ("Protagonista haciéndole un anilingus a Dídac.")

        if p_didac.anilingus_received == 1:

            n "Acercas tu rostro a su trasero  mientras deslizas una lengua juguetona en la superficie anal."

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "AAAHHmmm..."

        elif randomnum_1to5 == 2:

            d "MMfhmm..."

        elif randomnum_1to5 == 3:

            d "HHMmhm..."

        elif randomnum_1to5 == 4:

            d "Ah-aahmm..."

        elif randomnum_1to5 == 5:

            d "Mmmmhm..."

        ###

        if p_didac.anilingus_received == 1:

            with vpunch

            d "¡Ey!"

            d "Hmmm..."

            p "¿Sí?"

            $ ped_sex_general_zoom_Cond = "ass"
            $ ped_sex_general_action_Cond = "at01_01"
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            n "Empiezas a deslizar tu lengua por su interior."

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            d "¡¿Qué coño haces?!"

            p "Sabges perfegtamente gué estoy hagciendo."

            if p_prot.pos == "doggy":

                d "¡Mi coño está más abajo!"

            else:

                d "¡Mi coño está más arriba!"

            p "Nog lo habíagh notagdo..."

        elif p_didac.anilingus_received == 2:

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            d "La madre que te parió..."

            d "¡¿En serio me tienes que meter la lengua por ahí?!"

            d "Lo que quiero es que..."

            $ ped_sex_general_zoom_Cond = "ass"
            call pedrera_sex_p_general_talk
            with vpunch

            d "Hmmm..."

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            d "¡Que me folles el coño!"

            d "¡No que me estés lamiendo el jodido culo!"

            p "¿Te disgusta?"

            d "..."

        elif p_didac.anilingus_received == 3:

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            d "Serás hijo de..."

            $ ped_sex_general_zoom_Cond = "ass"
            call pedrera_sex_p_general_talk
            with vpunch

            d "Hmmm..."

            p "Al fignal te va a gustagr mág por agui..."

        elif p_didac.anilingus_received >= 4:

            $ ped_check_1_10("ped_anilingus_didac_list")
            #$ randomnum_1to10 = renpy.random.randint(1, 10)

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            with fade_short

            if ped_check_list_result == 1:

                d "Al menos podrías estar lamiéndome el otro agujero..."

                p "¿Entongces confiegsas gue no te disgusta tanto mi lengua?"

            elif ped_check_list_result == 2:

                d "¿Tanto te gusta usar tu lengua?"

                p "No tangto como a tig recivigrla..."

            elif ped_check_list_result == 3:

                d "..."

                p "¿No digces nagda?"

                d "¿Serviría de algo?"

                p "Nop."

            elif ped_check_list_result == 4:

                d "Reconozco que no es te da tan mal pero..."

                d "Por mi coño también estaría bien."

                p "Pogo a pogo vas aceptangdo tu pegrrería..."

            elif ped_check_list_result == 5:

                d "Métemela de una vez..."

                p "¿Por egste agujegro?"

                d "¡Ya sabes por dónde me refiero!"

                p "Impaciengte..."

                call ped_D_NoSex ##########################################

            elif ped_check_list_result == 6:

                d "Eres un hijo de puta con una lengua muy hábil..."

                p "Y dú una zgorra insagciable..."

            elif ped_check_list_result == 7:

                d "¿Por qué coño me pone tanto esto?"

                p "¿Por gué segrá...?"

            elif ped_check_list_result == 8:

                d "Al menos así no te corres tan pronto..."

                p "Y gú vas aceptgando megjor gue te gugsta que te meta gosas por degtrás..."

            elif ped_check_list_result == 9:

                d "..."

                p "¿No digces nada?"

                d "¡Calla y sigue!"

                p "Gue mangdona..."

            elif ped_check_list_result == 10:

                d "Tssk..."

            else:

                d "..."

        $ ped_check_1_10("ped_anilingus_insult_didac_list")
        #$ randomnum_1to10 = renpy.random.randint(1, 10)

        if ped_sex_general_zoom_Cond != "ass":
            $ ped_sex_general_zoom_Cond = "ass"
            call pedrera_sex_p_general_talk
            with fade_short

        if ped_check_list_result == 1:

            d "Imbécil..."

        elif ped_check_list_result == 2:

            d "Idiota..."

        elif ped_check_list_result == 3:

            d "Capullo..."

        elif ped_check_list_result == 4:

            d "Gilipollas..."

        elif ped_check_list_result == 5:

            d "Subnormal..."

        elif ped_check_list_result == 6:

            d "Lameculos..."

        elif ped_check_list_result == 7:

            d "Mendrugo..."

        elif ped_check_list_result == 8:

            d "Tarugo..."

        elif ped_check_list_result == 9:

            d "Zopenco..."

        elif ped_check_list_result == 10:

            d "Comeflores..."
        else:

            d "Tssk..."

        call afternight05_Pedrera_Neus_Warning


################################################################################
############################################################ VAGINAL SEX

    elif p_prot.action in ["vaginal_done_TRY", "vaginal_done"]:

        # If Didac is not pregnant by you, Neus has repairs on letting you fuck her cunt.

        $ p_didac.vaginal_received_TRY += 1

        if DidacPregnant == False:

            $ p_didac.vaginal_received_FAILED += 1

            if p_didac.vaginal_received_FAILED == 1:
                $ ped_sex_general_action_Cond = "v00_00"
            elif p_didac.vaginal_received_FAILED == 2:
                $ ped_sex_general_action_Cond = "v00_02"
            elif p_didac.vaginal_received_FAILED == 3:
                $ ped_sex_general_action_Cond = "v00_03"
            elif p_didac.vaginal_received_FAILED == 4:
                $ ped_sex_general_action_Cond = "v00_04"
            elif p_didac.vaginal_received_FAILED >= 5:
                $ ped_sex_general_action_Cond = "v00_04"

            $ ped_sex_general_zoom_Cond = "crotch"
            call pedrera_sex_p_general_talk
            with dissolve

            pause 0.2

            $ debug ("You can't fuck Didac, she is not pregnant.")

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk
            # Not with Dissolve

            if p_didac.vaginal_received_FAILED == 1:

                call ped_D_NoSex

            elif p_didac.vaginal_received_FAILED == 2:

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx09
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "¡¿Qué es lo que he dicho?!"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_iris front00
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx01
                with dissolve

                d "¡Podría al menos meter la puntita!"

                show neus_exp_mouth sad_Talkingx10
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "¡¿Es que hablo chino?!"

                show neus_exp_mouth sad_Silentx07
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils right01
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                with fade_short

                d "..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                    with dissolve

                    pause 0.2

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "¡Ni se te ocurra metérsela ahí!"

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "O al final tendré que tomar medidas drásticas."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_iris right05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils left04
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                with fade_short

            elif p_didac.vaginal_received_FAILED == 3:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils down01
                    show gensex_missionary_d_head_exp_eyebrows normal
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                with fade_short

                p "¡Ugh..!"

                $pl.ch_pts("np",-2)

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    with dissolve

                p "No puedo moverme..."

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "No hagas que me repita, [protname]."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "Puedo entender que Dídac sea cabezota y tenga esa necesidad..."

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Pero de ti me esperaba algo más..."

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_iris front00
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with dissolve

                d "¡No seas tan aguafiestas!"

                show neus_exp_mouth sad_Silentx08
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx07
                show neus_exp_iris front00_bright
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with dissolve

                d "..."

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils right04
                    show gensex_missionary_d_head_exp_eyebrows sadx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx06

                with fade_short

                d "Vale,"

                extend " vale..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils left03
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                    with dissolve

                d "ya me callo..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils left05
                    show gensex_missionary_d_head_exp_eyebrows sadx03
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                    with dissolve

            elif p_didac.vaginal_received_FAILED == 4:

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03
                with fade_short

                ne "Es mi última advertencia."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx04
                with dissolve

                pause 0.2

                $pl.ch_pts("np",-3)

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils right02
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                with fade_short

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":

                    pause 0.2

                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx04
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    with dissolve

                p "..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils left04
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                    with dissolve

            elif p_didac.vaginal_received_FAILED == 5:

                $pl.ch_pts("np",-5)

                $ p_prot.restTurns = 5

                call afternight05_Pedrera_Neus_Warning_4Times

        else:

            $ p_prot.vaginal_done += 1
            $ p_didac.vaginal_received += 1
            $ p_didac.vaginal_dilatation += 1

            $ p_prot.action = "vaginal_done"
            $ p_didac.b_action = "vaginal_received"

            #$ ped_sex_general_zoom_Cond = ""

            if p_didac.action == "cunnilingus_done_p_txell":
                $ ped_sex_general_expression_Cond = "closed"
            else:
                $ ped_sex_general_expression_Cond = "talk"

            if p_didac.vaginal_received > 3:
                $ ped_sex_general_action_Cond = "v01_05"
            elif p_didac.vaginal_received > 2:
                $ ped_sex_general_action_Cond = "v01_04"
            elif p_didac.vaginal_received > 1:
                $ ped_sex_general_action_Cond = "v01_02"
            else:
                $ ped_sex_general_action_Cond = "v01_01"
            call pedrera_sex_p_general_talk

            $ debug ("Sex Prove Missionary-Doggy02.")

            #if p_didac.pos == "doggy":
            $ ped_sex_general_zoom_Cond = "crotch"
            call pedrera_sex_p_general_talk
            with dissolve

            $ ped_check_1_10("ped_missionary_vaginal_moan_didac_list")
            #$ randomnum_1to10 = renpy.random.randint(1, 10)

            if ped_check_list_result == 1:

                d "Hmmmm...."

            elif ped_check_list_result == 2:

                d "MMmnn..."

            elif ped_check_list_result == 3:

                d "Hmffnn..."

            elif ped_check_list_result == 4:

                d "Hnmm..."

            elif ped_check_list_result == 5:

                d "Aahmmm..."

            elif ped_check_list_result == 6:

                d "Mmmhnm..."

            elif ped_check_list_result == 7:

                d "Nngnn..."

            elif ped_check_list_result == 8:

                d "Uhhmmm..."

            elif ped_check_list_result == 9:

                d "Hmfmmn..."

            elif ped_check_list_result == 10:

                d "Hmmm..."

            else:

                d "Hmmm..."

        ##

            if p_didac.vaginal_pain_received > 0:

                $ p_didac_vaginal_pain_received_relax_times += 1

                if p_didac_vaginal_pain_received_relax_times == 1:

                #if p_txell_cunnilingus_received_from_p_didac_at_missionary == 1:

                    $ debug ("¿Is This message Repeated?")

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        tx "Mucho mejor así..."

                        tx "¿No crees?"

                        d "¡SEEeeeghh...!"

                        tx "Es que mira que hay que ser bestia,"

                        tx "para metérsela de golpe sin juguetear un poco con ella."

                        p "..."

                        if p_txell.seal != "sealed":

                            tx "¿Tienes pensado ser tan bruto conmigo?"

                            p "Euh..."

                            tx "Por que no te vas a acercar a mi coño si piensas actuar de esta manera."

                            menu:

                                "<Decirle que no tiene muchas más opciones si quiere tu esperma>":
                                    call p_Help

                                    $pl.ch_pts("dp",-1)
                                    $pl.ch_pts("np",-2)
                                    $pl.ch_pts("mp",-3)

                                    p "Tengo entendido que necesitas mi esperma,"

                                    p "sea por las buenas o por las malas."

                                    p "Así que tampoco creo que tengas muchas más opciones que aceptar lo que te diga."

                                    tx "..."

                                    ne "¡[protname]!"

                                    ne "No seas así."

                                    p "..."

                                "Contigo seré más cuidadoso":
                                    call p_Help

                                    $pl.ch_pts("dp",-3)

                                    d "¡¿Y por qué con ella sí y no conmigo?!"

                                    d "¡La madre que te parió!"

                                    ne "Un poco de razón tiene..."

                                "No prometo nada.":
                                    call p_Help

                                    $pl.ch_pts("np",-1)
                                    $pl.ch_pts("mp",-1)

                                    tx "Pues yo sí te lo prometo,"

                                    tx "como intentes hacer algo así,"

                                    tx "te vas a quedar {i}eunuco{/i}."

                                    ne "Txell,"

                                    extend " no."

                                    ne "Tengas argumentos de peso o no,"

                                    ne "ahora mismo tu vida depende de que pueda seguir produciendo esperma."

                                    tx "..."

                                    tx "Psst..."

                                "Lo siento, reconozco que me he animado demasiado pronto...":
                                    call p_Help

                                    $pl.ch_pts("np",1)
                                    $pl.ch_pts("mp",-1)

                                    tx "Hmm..."

                                    d "Demasiado pronto dice,"

                                    d "la madre que te parió..."

                        else: # you already had sex with Txell.

                            if p_txell.vaginal_pain_received == 0:

                                tx "Suerte que conmigo no has sido tan bruto..."

                                if p_txell.anal_pain_received == 0:

                                    tx "Aunque por detrás no hayas sido tan delicado..."

                            else:

                                tx "Aunque después de lo bruto que has sido conmigo,"

                                extend "tampoco me extraña..."

                                if p_txell.anal_pain_received > p_txell.vaginal_pain_received:

                                    tx "Especialmente por detrás..."

                    else:

                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx01
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with fade_short

                        d "Mucho mejor así..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sad_Silentx03
                            with dissolve

                        p "Creía que querías que te la metiera hasta el fondo."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                            with dissolve

                        d "¡Joder!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                            with dissolve

                        d "¡Sí!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                            with dissolve

                        d "Pero tampoco hay que ser tan bestia!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                            with dissolve

                        p "¿No decías que estabas tan mojada aquí abajo?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils left04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            with dissolve

                        d "¡Pero es que tienes un pollón enorme!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        p "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                        d "Si consigues hacerme correr al menos una vez,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx08
                            with dissolve

                        d "estoy segura que ya entrará mucho mejor..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx05
                            with dissolve


                else: ## p_didac_vaginal_pain_received_relax_times

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        $ ped_check_1_5("ped_vaginal_pain_received_relax_didac_withTxell_list")

                        if ped_check_list_result == 1:

                            tx "Apenas lo entiendo,"

                            tx "pero imagino que quiere decirte que no se la vuelvas a meter de golpe."

                        elif ped_check_list_result == 2:

                            tx "Por mucho que diga tu amigo,"

                            tx "tu pollón es demasiado enorme para él."

                        elif ped_check_list_result == 3:

                            tx "Creo que a esta profundidad lo disfrutará mucho más."

                        elif ped_check_list_result == 4:

                            tx "Ya es bastante sorprendente que le quepa la mitad de tu pollón,"

                            tx "no creo que se buena idea metérsela otra vez entera."

                        elif ped_check_list_result == 5:

                            tx "Sino quieres reventar a tu amigo por dentro,"

                            tx "sería mejor que no se la volvieras a meter entera."

                        else:

                            tx "Si se la vuelves a meter entera,"

                            tx "se cabreará de verdad..."

                    else:

                        $ ped_check_1_5("ped_vaginal_pain_received_relax_didac_list")

                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk

                        if ped_check_list_result == 1:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                                with dissolve

                            d "¡Soy la primera que quiere tu puta anaconda dentro,"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils front03
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "pero joder!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                                with dissolve

                            d "¡Dame un poco más de tiempo que la tienes enorme!"

                        elif ped_check_list_result == 2:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                                with dissolve

                            d "Aunque me encantaría tenerla toda dentro,"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows sadx02
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx05
                                with dissolve

                            d "por ahora así no está nada mal..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows sadx03
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx07
                                with dissolve

                            d "al menos no me duele tanto..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 06
                                show gensex_missionary_d_head_exp_pupils front06
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx10
                                with dissolve

                            d "¡Que vaya pollón gastas, cabrón!"

                        elif ped_check_list_result == 3:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                                with dissolve

                            d "¡Te pediría que fueras un poco más con cuidado la próxima vez!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                                with dissolve

                            d "¡Que no la tienes precisamente pequeña, mamón!"

                        elif ped_check_list_result == 4:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 06
                                show gensex_missionary_d_head_exp_pupils front06
                                show gensex_missionary_d_head_exp_eyebrows sadx07
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx10
                                with dissolve

                            d "Pollón gastas, joder..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 03
                                show gensex_missionary_d_head_exp_pupils front03
                                show gensex_missionary_d_head_exp_eyebrows angryx03
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                                with dissolve

                            d "¡No me la vuelvas a meter de golpe"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx006
                                with dissolve

                            d "o te arranco los huevos!"

                        elif ped_check_list_result == 5:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx09
                                with dissolve

                            d "¡Así mucho mejor, joder!"

                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front2
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx06
                                with dissolve

                            d "Ni se te ocurra volver a metérmela de golpe..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve


            ###

            else:

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":
                    with fade_short

                if p_didac.vaginal_received == 1:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_blush 04
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx14
                        with dissolve

                    d "¡¡SEeh!!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows sadx03
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx12
                        with dissolve

                    elif p_didac.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with dissolve

                    d "¡Ya era hora de sentirla dentro de nuevo!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_blush 05
                        show gensex_missionary_d_head_exp_eyes 07
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                        with dissolve

                    pt "Y eso que solo le he metido la mitad..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx06
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx11
                        with dissolve

                    elif p_didac.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "crotch"
                        call pedrera_sex_p_general_talk
                        with dissolve

                    n "Lentamente vas deslizando tu enorme manubrio,"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                        with dissolve

                    n "sintiendo en cada embestida el calor y la presión de su interior. "

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 07
                        show gensex_missionary_d_head_exp_pupils front07
                        show gensex_missionary_d_head_exp_eyebrows sadx07
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx13
                        with dissolve

                    elif p_didac.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with dissolve

                    d "¡MMMHHmm...!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_blush 04
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                        with dissolve

                elif p_didac.vaginal_received == 2:

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        d "¡HHMMFFHMM...!"

                        $ Pedrera_char_Cond = "TxellClose_b"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with fade_short

                        tx "Eso significa que le está gustando."

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 03
                        show m_exp_piris down03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "Pero no dejes de lamer,"

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows angryx03
                        with dissolve

                        tx "o voy a tener que pellizcarte los pezones de un modo que no te va a gustar."

                        show m_exp_mouth sadbiting_Silentx04
                        show m_exp_eyes 05
                        show m_exp_piris down05
                        show m_exp_eyebrows normal
                        with dissolve

                        d "¡Tambhgien te pogdria morgder yogh!"

                        show m_exp_mouth sad_Talkingx004
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex02
                        with dissolve

                        tx "¿Y quien te dice que eso no me gustaría?"

                        show m_exp_mouth happybiting_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris down05
                        show m_exp_eyebrows angryx02
                        with dissolve

                        d "..."

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 07
                            show gensex_missionary_d_head_exp_pupils front07
                            show gensex_missionary_d_head_exp_eyebrows sadx06
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                        d "¡MMMmmhmm...!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx14
                            with dissolve

                        elif p_didac.pos == "doggy":
                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with dissolve

                        d "Hijo de puta,"

                        extend " que pollón tienes..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx06
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                            with dissolve

                        d "No sabes cuanto echaba de menos tenerla dentro..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx06
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                            with dissolve

                    

                elif p_didac.vaginal_received == 3:

                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        d "¡HHMMmmghf...!"

                        tx "Sigue dándole duro a esta perra."

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 07
                            show gensex_missionary_d_head_exp_pupils front07
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx08
                            with dissolve

                        d "¡AAhmmmmffh...!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                            with dissolve

                        elif p_didac.pos == "doggy":
                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with dissolve

                        d "Me encanta tu polla..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx03
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                            with dissolve

                elif p_didac.vaginal_received > 3:
                    
                    if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                        $ ped_check_1_10("ped_missionary_vaginal_cunnilingusDoneTxell_moan_didac_list")
                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            d "¡HHMMmmghf...!"

                        elif ped_check_list_result == 2:

                            d "¡UGhhmmm...!"

                        elif ped_check_list_result == 3:

                            d "¡GUghhmm...!"

                        elif ped_check_list_result == 4:

                            d "¡Agghmm...!"

                        elif ped_check_list_result == 5:

                            d "¡HHMmm...!"

                        elif ped_check_list_result == 6:

                            d "¡Aughhmmm...!"

                        elif ped_check_list_result == 7:

                            d "¡Fuuchmmm...!"

                        elif ped_check_list_result == 8:

                            d "¡Hhmmmm...!"

                        elif ped_check_list_result == 9:

                            d "¡Zoograhh...!"

                        elif ped_check_list_result == 10:

                            d "¡Fuuchmmm...!"

                        else:

                            d "¡Hhmmm...!"

                        $ ped_check_1_10("ped_missionary_vaginal_cunnilingusDoneTxell_didac_list")
                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            tx "¡Que no se detenga esa lengua zorrilla!"

                        elif ped_check_list_result == 2:

                            tx "No te he dicho que pares Dídac."

                        elif ped_check_list_result == 3:

                            tx "¡Mueve más esa lengua!"

                        elif ped_check_list_result == 4:

                            tx "Por lo menos sirve para algo la lengua de tu amigo."

                        elif ped_check_list_result == 5:

                            tx "Mmm..."

                            tx "Sigue así zorrilla."

                        elif ped_check_list_result == 6:

                            tx "Al final conseguirá que me corra y todo..."

                        elif ped_check_list_result == 7:

                            if p_prot.action in ["vaginalDeep_done", "vaginal_done"]:

                                tx "Sigue dándole duro,"

                                extend " que le encanta."

                            else:

                                tx "Fóllate su coño de una vez hombre,"

                                tx "que te lo está suplicando."

                        elif ped_check_list_result == 8:

                            tx "¿Decías algo?"

                        elif ped_check_list_result == 9:

                            tx "Es de mala educación hablar con la boca ocupada."

                        elif ped_check_list_result == 10:

                            tx "Estás mejor calladita."

                        else:

                            tx "Hmmm..."

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_blush 04

                        $ ped_check_1_10("ped_missionary_vaginal_didac_moan_list")
                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                                with dissolve

                            d "HHmmmm..."

                        elif ped_check_list_result == 2:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                                with dissolve

                            d "Mmmmn..."

                        elif ped_check_list_result == 3:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happy_Talkingx07
                                with dissolve

                            d "Seehh..."

                        elif ped_check_list_result == 4:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx06
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx02
                                with dissolve

                            d "Ahhmm..."

                        elif ped_check_list_result == 5:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx05
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx002
                                with dissolve

                            d "Dios..."

                        elif ped_check_list_result == 6:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx03
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                                with dissolve

                            d "Mmmnnfhhh..."

                        elif ped_check_list_result == 7:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                                with dissolve

                            d "Hmmhnn..."

                        elif ped_check_list_result == 8:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx08
                                with dissolve

                            d "Uhhmmn..."

                        elif ped_check_list_result == 9:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx06
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx04
                                with dissolve

                            d "AAhhmmm..."

                        elif ped_check_list_result == 10:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
                                with dissolve

                            d "Mmffhmm..."

                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows sadx06
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx04
                                with dissolve

                            d "AAhhmmm..."


                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_blush 05
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx03
                            show gensex_missionary_d_head_exp_mouth happy_Talkingx08
                            with dissolve


                        $ ped_check_1_10("ped_missionary_vaginal_didac_list")
                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if p_didac.pos == "doggy":
                            $ ped_sex_general_zoom_Cond = "face"
                            call pedrera_sex_p_general_talk
                            with dissolve

                        if ped_check_list_result == 1:

                            d "Me encanta..."

                        elif ped_check_list_result == 2:

                            d "Que pollón tienes cabrón..."

                        elif ped_check_list_result == 3:

                            d "No pares..."

                        elif ped_check_list_result == 4:

                            d "Me estoy enamorando de tu polla..."

                        elif ped_check_list_result == 5:

                            d "¿Por qué me pone tanto tu pollón?"

                        elif ped_check_list_result == 6:

                            d "¡Ni se te ocurra parar!"

                        elif ped_check_list_result == 7:

                            d "Dame más duro..."

                        elif ped_check_list_result == 8:

                            d "Me encantaría sentirla entera dentro..."

                        elif ped_check_list_result == 9:

                            d "¿Quien iba a decir hace una semana que hoy me estarías follando?"

                        elif ped_check_list_result == 10:

                            d "No sabes cuanto hacía que estaba esperando esto..."

                        else:

                            d "Sigue así..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth happybiting_Silentx09
                            with dissolve

                        elif p_didac.pos == "doggy":
                            $ ped_sex_general_zoom_Cond = "crotch"
                            call pedrera_sex_p_general_talk
                            with dissolve

                #####

                if p_prot.pos == "missionary" and (p_didac.vaginal_pain_received == 0 and p_didac.vaginal_received > 2):

                    if p_txell_cunnilingus_received_from_p_didac_at_missionary_TRY == False:

                        $ p_txell_cunnilingus_received_from_p_didac_at_missionary_TRY = True

                        pause 0.2

                        $ p_didac.action = "cunnilingus_done_p_txell"

                        $ ped_sex_general_zoom_Cond = "face"
                        $ ped_sex_general_expression_Cond = "closed"
                        call pedrera_sex_p_general_talk

                        with hpunch

                        d "¡¿Qué coño ha...?!"

                        d "¡MMmmmfh!"

                        $ ped_sex_general_zoom_Cond = ""
                        $ ped_sex_general_expression_Cond = "closed"
                        call pedrera_sex_p_general_talk
                        with fade

                        n "Con sutil elegancia e innegable perrería,"

                        n "Meritxell se abre de piernas sobre el rostro de Dídac, posándose desnuda ante ti."

                        $ Pedrera_char_Cond = "TxellSuperClose"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris down02
                        show m_exp_eyebrows suspiciousx02
                        with fade_short

                        tx "Calladita estás más guapa."

                        show m_exp_mouth happybiting_Silentx07
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows angryx01
                        with dissolve

                        d "¡¿Queg se supoghne que estás hagciendo?!"

                        show m_exp_mouth sad_Talkingx01
                        show m_exp_eyes 05
                        show m_exp_piris down05
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "Shhh..."

                        show m_exp_mouth sad_Talkingx004
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "En clase te he escuchado muchas veces alardear"

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "de lo bueno que eres en el arte de {i}\"comerte coños\"{/i}."

                        show m_exp_mouth happy_Talkingx09
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "Pues ahora tienes la oportunidad de demostrármelo."

                        show m_exp_mouth happybiting_Silentx08
                        show m_exp_eyes 05
                        show m_exp_piris down05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        pause 0.2

                        $ ped_sex_general_zoom_Cond = "face"
                        $ ped_sex_general_expression_Cond = "closed"
                        call pedrera_sex_p_general_talk
                        with fade

                        d "..."

                        p "En clase suele decir muchas tonterías cuando está con otros gilipollas."

                        d "¡Yog no digoh tongterías!"

                        $ Pedrera_char_Cond = "TxellSuperClose"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows angryx02
                        with fade_short

                        tx "Pues entonces calla y demuéstramelo."

                        show m_exp_mouth happybiting_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris down05
                        show m_exp_eyebrows angryx03
                        with dissolve

                        pause 0.2

                        $ ped_sex_general_zoom_Cond = "face"
                        $ ped_sex_general_expression_Cond = "closed"
                        call pedrera_sex_p_general_talk
                        with fade

                        d "..."

                        $ Pedrera_char_Cond = "TxellSuperClose"
                        call Pedrera_char_lab

                        show m_exp_mouth sadbiting_Silentx04
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows surprisex01
                        with fade_short

                        p "Creí que no disfrutabas en absoluto de esto."

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "Me he puesto juguetona viéndoos follar,"

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "no lo voy a negar."

                        show m_exp_mouth sadbiting_Silentx02
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        p "Ya..."

                        show m_exp_mouth sad_Talkingx03
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows normal
                        with dissolve

                        tx "No te molesta tenerme desnuda ante ti, mientras follas a Dídac"

                        extend " ¿verdad?"

                        show m_exp_mouth happy_Talkingx04
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows sadx01
                        with dissolve

                        if p_prot.kiss_p_didac > 0:

                            tx "Tampoco la ibas a besar todo el rato."

                        else:

                            tx "Tampoco la ibas a besar justo ahora..."

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx01
                        with dissolve

                        p "..."

                        show m_exp_mouth sad_Talkingx005
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        tx "Pero recuerda,"

                        extend " ahora es el turno de Dídac,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                        tx "así que puedes mirar,"

                        extend " pero no tocar."

                        show m_exp_mouth happybiting_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        pt "Será zorra..."

                        menu:

                            pt "¿Dejar a Txell que se quede encima de Dídac sin poder tocarla?"

                            "Puede ser interesante.":

                                $ p_txell_cunnilingus_received_from_p_didac_at_missionary = 1 # It's FUCKIN NECESSARY.

                                $pl.ch_pts("dp",1)
                                $pl.ch_pts("mp",1)

                                call p_Help


                                $ p_didac.action = "cunnilingus_done_p_txell"

                                show m_exp_mouth happy_Silentx07
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                show m_exp_eyebrows suspiciousx02
                                with dissolve

                                p "No voy a ser yo quien se queje de tener estos melones enfrente de mi."

                                show m_exp_mouth happybiting_Silentx05
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows sadx01
                                with dissolve

                                tx "Hmm..."

                                show m_exp_mouth happy_Talkingx06
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                show m_exp_eyebrows angryx03
                                with dissolve

                                tx "Así me gusta."

                                show m_exp_mouth happybiting_Silentx07
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows sadx02
                                with dissolve

                                $ ped_sex_general_zoom_Cond = ""
                                $ ped_sex_general_expression_Cond = "closed"
                                call pedrera_sex_p_general_talk
                                with fade_long1s


                            "Prefiero hacerlo a solas con Dídac.":
                                call p_Help

                                $pl.ch_pts("dp",1)
                                $pl.ch_pts("mp",-3)

                                $ p_didac.action = "rest"

                                show m_exp_mouth sad_Silentx02
                                show m_exp_eyes 00
                                show m_exp_piris front00
                                show m_exp_eyebrows surprisex02
                                with dissolve

                                tx "..."

                                show m_exp_mouth sad_Silentx06
                                show m_exp_eyes 03
                                show m_exp_piris right03
                                show m_exp_eyebrows angryx02
                                with dissolve

                                pause 0.2

                                show m_exp_mouth sad_Talkingx08
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows angryx03
                                with dissolve

                                tx "Como quieras..."

                                show m_exp_mouth sad_Silentx08
                                show m_exp_eyes 05
                                show m_exp_piris right05
                                show m_exp_eyebrows angryx03
                                with dissolve

                                $ ped_sex_general_zoom_Cond = ""
                                $ ped_sex_general_expression_Cond = "talk"
                                call pedrera_sex_p_general_talk

                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils right01
                                show gensex_missionary_d_head_exp_eyebrows surprisex01
                                show gensex_missionary_d_head_exp_mouth sad_Silentx03
                                with fade_long1s

                                pause 0.2

                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows sadx03
                                show gensex_missionary_d_head_exp_mouth happybiting_Silentx05
                                with dissolve

                                $ ped_sex_general_expression_Cond = "lust"


                    if p_didac.action == "cunnilingus_done_p_txell" and p_txell_cunnilingus_received_from_p_didac_at_missionary > 0:

                        $ p_txell.pleasure += 6
                        $ p_txell.closeOrgasm += 4

                        #if p_txell_cunnilingus_received_from_p_didac_at_missionary == 1: # NOT NECESSARY.

                        if p_txell_cunnilingus_received_from_p_didac_at_missionary == 2:

                            tx "Y tú no pares ahí abajo,"

                            tx "que aparte de decir tonterías,"

                            tx "Parece que también sabes darle otros usos a tu lengua..."

                            d "¡Gue dhe foghllen!"

                        elif p_txell_cunnilingus_received_from_p_didac_at_missionary == 3:

                            tx "Ahí abajo,"

                            tx "sigue dándole a la lengua y no te despistes."

                            d "¡Al fignal dhe voy a dargh!"

                            tx "Calla y sigue."

                        elif p_txell_cunnilingus_received_from_p_didac_at_missionary >= 4:

                            tx "HMMmm..."

        # IMAGE AFTER

        $ ped_sex_general_zoom_Cond = ""
        if ped_sex_general_expression_Cond == "talk":
            $ ped_sex_general_expression_Cond = "closed"
        call pedrera_sex_p_general_talk
        with fade_short

################################################################################
############################################################ VAGINAL DEEP

    elif p_prot.action in ["vaginalDeep_done_TRY", "vaginalDeep_done"]:

        $ debug ("Deep Vaginal Sex with Didac.")

        $ ped_sex_general_zoom_Cond = ""

        if p_didac.action == "cunnilingus_done_p_txell":
            $ ped_sex_general_expression_Cond = "closed"
        else:
            $ ped_sex_general_expression_Cond = "talk"

        if p_didac.vaginalDeep_received > 3:
            $ ped_sex_general_action_Cond = "v02_03"
        elif p_didac.vaginalDeep_received > 1:
            $ ped_sex_general_action_Cond = "v02_02"
        else:
            $ ped_sex_general_action_Cond = "v02_01"
        call pedrera_sex_p_general_talk

        ##

        if p_didac.vaginal_dilatation < 3:
            $ p_didac.vaginal_pain += 2

        if p_didac.vaginal_pain > 0:

            $ p_didac.vaginal_pain_received += 1

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 07
                show gensex_missionary_d_head_exp_pupils front07
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx25
                with vpunch

            if p_didac.vaginal_pain_received == 1:

                d "{size=30}¡DIOS!{/size}"

            elif p_didac.vaginal_pain_received == 2:

                d "{size=35}¡JODER!{/size}"

            elif p_didac.vaginal_pain_received == 3:

                d "{size=40}¡ME CAGÜEN!{/size}"

            elif p_didac.vaginal_pain_received > 3:

                d "{size=45}¡COÑO!{/size}"

            # TAKING OUT THE DICK

            $ ped_sex_general_action_Cond = "v00_00"
            call pedrera_sex_p_general_talk

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx08
                show gensex_missionary_d_head_exp_mouth sad_Silentx21

            $ p_didac.action = "rest"
            $ p_prot.action = "rest"

            show hit 11
            pause 0.02
            show hit 12
            pause 0.02
            show hit 13
            pause 0.02
            show hit 14
            pause 0.02
            show hit 15
            pause 0.02
            show hit 16
            pause 0.02
            show hit 17
            pause 0.02
            show black
            with vpunch

            hide hit
            hide black
            with fade

            if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                $ p_didac.action = "rest"

                tx "¡Ey!"

                n "Con un fuerte empujón se quita de encima a Meritxell"

                n "mientras te dirige una mirada de pura ira."

            if p_didac.vaginal_pain_received == 1:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with dissolve

                d "¡Se un poco más delicado!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                    with dissolve

                d "¡COÑO!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx01
                    show gensex_missionary_d_head_exp_mouth sad_Silentx04
                    with dissolve

                p "¿No me estás diciendo que estás bien mojada aquí abajo"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                    with dissolve

                p "y que la quieres sentir toda dentro?"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front08
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                    with dissolve

                d "¡Sí joder!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx21
                    with dissolve

                d "¡PERO ES QUE LA TIENES ENORME!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx20
                    with dissolve

                d "Espérate un poquito para que se me acomode un poco,"

                extend " coño..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils right01
                    show gensex_missionary_d_head_exp_eyebrows serious
                    show gensex_missionary_d_head_exp_mouth sad_Silentx05
                    with dissolve

                tx "Desde luego,"

                extend " sois tal para cual."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils left04
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Silentx07
                    with dissolve

            elif p_didac.vaginal_pain_received == 2:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with dissolve

                d "¡¿QUÉ ES LO QUE NO HAS ENTENDIDO DE CON MÁS CUIDADO?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Silentx10
                    with dissolve

                #ne "Dídac tiene razón..."

            elif p_didac.vaginal_pain_received == 3:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with dissolve

                d "¡ME ESTÁS HACIENDO DAÑO JODER!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Silentx10
                    with dissolve

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx21
                    with dissolve

                d "¡¿ES QUE NO LO ENTIENDES?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Silentx10
                    with dissolve

                #ne "¡[protname]!"

                #ne "Si sigues así voy a tener que tomar cartas en el asunto."

            elif p_didac.vaginal_pain_received == 4:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                    with dissolve

                d "¡¿ES QUE DISFRUTAS HACIÉNDOME DAÑO?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils front01
                    show gensex_missionary_d_head_exp_eyebrows angryx07
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx24
                    with dissolve

                d "¡PARA YA!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Silentx15
                    with dissolve

                #ne "Es mi último aviso."

            elif p_didac.vaginal_pain_received > 4:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Silentx15
                    with dissolve

                d "..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Silentx14
                    with dissolve

            call afternight05_Pedrera_Neus_Warning

            #call afternight05_Pedrera_Sex_NeusLastWarning

            p "..."

        else:

            $ p_prot.vaginalDeep_done += 1
            $ p_didac.vaginalDeep_received += 1

            $ p_prot.action = "vaginalDeep_done"
            $ p_didac.b_action = "vaginalDeep_received"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 07
                show gensex_missionary_d_head_exp_pupils front07
                show gensex_missionary_d_head_exp_eyebrows sadx07
                show gensex_missionary_d_head_exp_mouth sad_Talkingx006
                with vpunch

            if p_prot.pos == "doggy":
                $ ped_sex_general_zoom_Cond = "crotch"
                call pedrera_sex_p_general_talk
                with fade_short

            if p_didac.vaginalDeep_received == 1:

                d "{size=50}¡COOÑOOO...!{/size}"

            if p_didac.vaginalDeep_received == 2:

                d "{size=45}¡JODEER...!{/size}"

            if p_didac.vaginalDeep_received == 3:

                d "{size=45}¡DIOOS...!{/size}"

            if p_didac.vaginalDeep_received == 4:

                d "{size=40}¡HOSTIAS...!{/size}"

            if p_didac.vaginalDeep_received > 4:

                d "{size=35}¡MMMFHMM...!{/size}"

            if p_prot.pos == "doggy":
                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                with fade_short

            ##

            if p_didac.vaginalDeep_received == 1:

                $ debug ("Deep Vaginal Successfully with Didac 01")

                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                    d "¡LA MAGDRE QUE TE PAGHRIO!"

                    tx "Creo que intenta elogiarte por el tamaño de tu falo."

                    if p_didac.vaginal_pain_received > 0:

                        tx "Al menos parece que por fin ya estás suficientemente mojada..."

                        tx "¿Habrá ayudado que estés disfrutando de mi entrepierna?"

                    d "¡JOGHDER!"

                    tx "¡Ey!"

                    tx "¡Sigue dándole a esa lengua!"

                    tx "No dejes que la polla de tu amigo te distraiga."

                    tx "Por enorme que sea..."

                    pt "Será zorra..."

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx12
                        with dissolve

                    d "¡LA MADRE QUE TE PARIÓ!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                        with dissolve

                    d "¡La tienes enorme!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils front00
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                        with dissolve

                    p "Y tú estás realmente estrecha..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                        with dissolve

                    p "Pensaba que decías que estabas bien mojada..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                        with dissolve

                    d "Ha entrado,"

                    extend " ¿No?"

                    if p_didac.vaginal_pain_received > 0:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        p "Sí,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows surprisex03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                            with dissolve

                        p "Pero bien que te me has quejado antes."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                            with dissolve

                        d "¡JODER!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            with dissolve

                        d "¡Por que antes me has hecho daño!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                            with dissolve

                        p "¿Y ahora no?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils right04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                            with dissolve

                        d "Ahora se siente algo mejor..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils right01
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        tx "Normal,"

                        extend " ahora está más dilatada."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils right03
                            show gensex_missionary_d_head_exp_eyebrows sadx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        tx  "Es que hay que ser {a=https://es.wikipedia.org/wiki/Homo_neanderthalensis}neandertal{/a} para meter ese pollón que tienes"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils right04
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                            with dissolve

                        tx "sin tener en cuenta ese principio tan básico."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx02
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx06
                        with dissolve

                    d "Ahora no pares..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows angryx02
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx13
                        with dissolve

                    pt "Si sigo así tampoco tardaré mucho en correrme..."

            elif p_didac.vaginalDeep_received == 2:

                $ debug ("Deep Vaginal Successfully with Didac 02")

                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                    d "¡ME CAHGO EN LAG HOGSTIAGHH!"

                    d "¡¿Por quegh coghjones se sientegh tang bieengh?!"

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 07
                        show gensex_missionary_d_head_exp_pupils front07
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                        with dissolve

                    d "¡ME CAGO EN LA HOSTIA!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx04
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx10
                        with dissolve


                    d "¡¿Por qué coño se siente tan bien?!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx06
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx12
                        with dissolve

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with fade_short

                ne "Bueno,"

                extend " es normal que sientas eso con la polla de [protname],"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "porque..."

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_iris right01
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with dissolve

                tx "Neus,"

                $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris left03
                show m_exp_eyebrows sadx02
                with fade_short

                tx "creo que su pregunta era más bien retórica."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris down04
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Dudo que tenga demasiada sangre en el cerebro para pensar ahora mismo,"

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx01
                with dissolve

                tx "y mucho menos tratándose de Dídac."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                d "¡HHmmmm!"

                call pedrera_sex_p_general_talk

                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                    with fade_short

                    d "¡MMMmmhhf!"

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils right03
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx14
                    with fade_short

                    d "¡Habla por ti!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils right04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                        with dissolve

                    d "¡Gili...!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 07
                        show gensex_missionary_d_head_exp_pupils front07
                        show gensex_missionary_d_head_exp_eyebrows sadx05
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                        with vpunch

                    d "¡HHMmmmnn!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows angryx02
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                        with dissolve

                p "Ughh..."


                pt "El dolor de cabeza lo suelo tener yo cuando se me pone así de dura..."

            elif p_didac.vaginalDeep_received == 3:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 06
                    show gensex_missionary_d_head_exp_pupils front06
                    show gensex_missionary_d_head_exp_eyebrows sadx06
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx14
                    with dissolve

                d "¡MMMMFFHMmmm.!"

                if p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell":

                    tx "Creo que intenta decirte que ni se te ocurra parar."

                    tx "Desde luego tienes un buen pollón."

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx14
                        with dissolve

                    d "¡Ni se te ocurra parar!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                        with dissolve

                    d "¡La madre que te parió!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 07
                        show gensex_missionary_d_head_exp_pupils front07
                        show gensex_missionary_d_head_exp_eyebrows sadx06
                        show gensex_missionary_d_head_exp_mouth happy_Talkingx16
                        with dissolve

                    d "¡Que pollón tienes cabrón!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows angryx03
                        show gensex_missionary_d_head_exp_mouth happybiting_Silentx13
                        with dissolve

            elif p_didac.vaginalDeep_received > 3:

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 06
                    show gensex_missionary_d_head_exp_pupils front06
                    show gensex_missionary_d_head_exp_eyebrows sadx06
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx14
                    with dissolve

                d "¡MMMMFHHMMM...!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 06
                    show gensex_missionary_d_head_exp_pupils front06
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx13
                    with dissolve

################################################################################
############################################################ ANAL SEX

    elif p_prot.action in ["anal_done_TRY", "anal_done"]:

        # Didac doesn't let you have anal sex if you didn't had it in minigame.

        if p_didac.anal_received == 0:

            if p_didac.anal_received_TRY >= 4:
                $ ped_sex_general_action_Cond = "a00_05"
            elif p_didac.anal_received_TRY == 3:
                $ ped_sex_general_action_Cond = "a00_04"
            elif p_didac.anal_received_TRY == 2:
                $ ped_sex_general_action_Cond = "a00_03"
            elif p_didac.anal_received_TRY == 1:
                $ ped_sex_general_action_Cond = "a00_02"
            elif p_didac.anal_received_TRY == 0:
                $ ped_sex_general_action_Cond = "a00_00"
            $ ped_sex_general_zoom_Cond = "crotch"
            call pedrera_sex_p_general_talk
            with fade_short

        if afternight04_Anal_dick_med_Speed_1_Success == 0:

            $ debug ("Didac doesn't let you fuck his ass.")

            $ p_didac.anal_received_FAILED += 1 # Becaues on Txell will be different.

            if p_didac.anal_received_FAILED == 1:

                #$ ped_sex_general_action_Cond = "a00_02"
                call pedrera_sex_p_general_talk
                with dissolve

                n "Sugerentemente acercas la punta de tu miembro por la superficie de su orificio anal."

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils down00
                    show gensex_missionary_d_head_exp_eyebrows surprisex01
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                with fade_short

                pause 0.2

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 01
                    show gensex_missionary_d_head_exp_pupils down01
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                    with dissolve

                d "¿Qué coño estás haciendo?"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows angryx01
                    show gensex_missionary_d_head_exp_mouth sad_Silentx04
                    with dissolve

                p "¿Acaso no es obvio?"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils front04
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx12
                    with dissolve

                d "¿Te crees que me va esta mariconada?"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                    with dissolve

                d "¡¿Es que no sabes distinguir un agujero del otro?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with dissolve

                d "¡Te estoy diciendo que me folles por el coño!"

                if DidacPregnant:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx02
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                        with dissolve

                    p "Dídac..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx004
                        with dissolve

                    d "No."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                        with dissolve

                    d "No me vas a follar por el culo."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx07
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                        with dissolve

                    d "Ni de coña vamos."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Silentx09
                        with dissolve

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils right01
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sad_Silentx04
                        with dissolve

                    ne "Dídac,"

                    $ Pedrera_char_Cond = "NeusClose_show"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx06
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx02
                    with fade_short

                    ne "es muy peligroso que te practique sexo vaginal,"

                    show neus_exp_mouth sad_Talkingx04
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    ne "si llegara a correrse dentro,"

                    extend " podrías quedarte embarazada,"

                    show neus_exp_mouth sad_Talkingx05
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris front02
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    ne "y no volver a ser un hombre nunca más."

                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils right01
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx18

                    with fade_short

                    d "¡Joder!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils right00
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx20
                        with dissolve

                    d "¡Ya lo sé!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                        with dissolve

                    d "¡Pero tampoco es tan imbécil!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils right03
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                        with dissolve

                    d "Creo que es capaz de distinguir cuando se va a correr y sacarla cuando es el momento,"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                        with dissolve

                    d "¡¿No?!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils right01
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Silentx13
                        with dissolve

                    ne "Es demasiado peligroso."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx14
                        with dissolve

                    d "No me vas a follar por el culo."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils right03
                        show gensex_missionary_d_head_exp_eyebrows angryx07
                        show gensex_missionary_d_head_exp_mouth sad_Silentx15
                        with dissolve

                    ne "Entonces tendrá que ser por la boca."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils left05
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Silentx09
                        with dissolve

                    d "Tssk..."

            elif p_didac.anal_received_FAILED > 1:

                $ ped_check_1_10("ped_analFAILED_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                        with dissolve

                    d "¡¿Qué coño es lo que no has entendido?!"

                elif ped_check_list_result == 2:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                        with dissolve

                    d "¡He dicho que por el culo no!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx20
                        with dissolve

                    d "¡¿Cuantas veces te lo tengo que repetir?!"

                elif ped_check_list_result == 3:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                        with dissolve

                    d "Mira que eres pesado..."

                elif ped_check_list_result == 4:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                        with dissolve

                    d "¡¿Qué coño te pasa a ti con mi culo?!"

                elif ped_check_list_result == 5:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 03
                        show gensex_missionary_d_head_exp_pupils front03
                        show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                        with dissolve

                    d "¡¿Tanto te mola mi culo?!"

                elif ped_check_list_result == 6:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx21
                        with dissolve

                    d "¡¿Es que acaso ya te molaba mi culo antes de que me volviera tía?!"

                elif ped_check_list_result == 7:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                        with dissolve

                    d "¡Deja mi puto culo en paz!"

                elif ped_check_list_result == 8:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                        with dissolve

                    d "No me vas a follar el culo..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                        with dissolve

                    d "¡¿Me explico?!"

                elif ped_check_list_result == 9:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows sadx01
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                        with dissolve

                    d "Con lo húmedo que tengo el coño..."

                    if DidacPregnant == True:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx06
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                            with dissolve

                        d "¡Y SIGUES INSISTIENDO EN METÉRMELO POR EL CULO!"

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils right01
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                        ne "¡Ejem!..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Silentx08
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                            with dissolve

                        d "¡Pues que se masturbe!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                            with dissolve

                        d "¡Pero por el culo no me la vas a meter!"

                elif ped_check_list_result == 10:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 02
                        show gensex_missionary_d_head_exp_pupils front02
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                        with dissolve

                    d "Eres retrasado de remate..."

                else:

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils front04
                        show gensex_missionary_d_head_exp_eyebrows angryx06
                        show gensex_missionary_d_head_exp_mouth sad_Silentx08
                        with dissolve

                    d "..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx07
                    show gensex_missionary_d_head_exp_mouth sad_Silentx15
                    with dissolve

                p "..."

            call afternight05_Pedrera_Neus_Warning

        else: # YOU CAN FUCK HER ASS.

            #if p_prot.pos == "doggy":

            if p_didac.anal_received == 0:
                $ ped_sex_general_action_Cond = "a00_00"
            elif p_didac.anal_received == 1:
                $ ped_sex_general_action_Cond = "a01_02"
            elif p_didac.anal_received == 2:
                $ ped_sex_general_action_Cond = "a01_02"
            elif p_didac.anal_received == 3:
                $ ped_sex_general_action_Cond = "a01_03"
            elif p_didac.anal_received == 4:
                $ ped_sex_general_action_Cond = "a01_04"
            elif p_didac.anal_received >= 5:
                $ ped_sex_general_action_Cond = "a01_05"

            $ ped_sex_general_zoom_Cond = "crotch"
            call pedrera_sex_p_general_talk
            if p_didac.anal_received > 0:
                with fade_short

            if p_didac.anal_pain > 0:

                $ p_didac_anal_pain_received_relax_times += 1

                if p_prot.pos == "doggy":
                    $ ped_sex_general_action_Cond = "00"
                    $ ped_sex_general_zoom_Cond = ""
                    call pedrera_sex_p_general_talk
                    with vpunch

                pause 0.2

                if p_prot.pos == "doggy":
                    $ ped_sex_general_zoom_Cond = "face"
                    call pedrera_sex_p_general_talk
                    with fade_short

                if p_didac_anal_pain_received_relax_times == 1:

                    $pl.ch_pts("dp",-1)

                    d "¡QUE ME HAS HECHO DAÑO JODER!"

                    d "¡Deja mi culo en paz y fóllame el coño de una vez!"

                else:

                    $pl.ch_pts("dp",-3)
                    $pl.ch_pts("np",-2)
                    $pl.ch_pts("mp",-1)

                    $ ped_check_1_10("ped_anal_pain_received_relax_didac_list")

                    if ped_check_list_result == 1:

                        d "¡Que me sigue doliendo el trasero!"

                    elif ped_check_list_result == 2:

                        d "¡¡¿Qué coño no entiendes?!!"

                    elif ped_check_list_result == 3:

                        d "¡QUE ME DUELE!"

                    elif ped_check_list_result == 4:

                        d "¡QUE PARES YA!"

                    elif ped_check_list_result == 5:

                        d "¡Al final te voy a romper la cara!"

                    elif ped_check_list_result == 6:

                        d "¡TE VOY A METER UNA HOSTIA!"

                    elif ped_check_list_result == 7:

                        d "¡TE VOY A REVENTAR LOS HUEVOS AL FINAL!"

                    elif ped_check_list_result == 8:

                        d "¡LA MADRE QUE TE PARIÓ!"

                    elif ped_check_list_result == 9:

                        d "¡TE VOY A METER EL PUÑO POR EL CULO!"

                    elif ped_check_list_result == 10:

                        d "¡TE VOY A METER UNA HOSTIA QUE VAS PERDER TODOS LOS DIENTES!"

                    else:

                        d "..."

                    call p_didac_insulting

                    
            else:
                
                $ p_prot.action = "anal_done"
                $ p_didac.b_action = "anal_received"

                $ p_prot.anal_done += 1
                $ p_didac.anal_received += 1
                $ p_didac.anal_dilatation += 1

                ##

                $ ped_sex_general_zoom_Cond = "crotch"

                if p_didac.action == "cunnilingus_done_p_txell":
                    $ ped_sex_general_expression_Cond = "closed"
                else:
                    $ ped_sex_general_expression_Cond = "talk"

                #$ ped_sex_general_action_Cond = "acum02" # TEST

                if p_didac.anal_received > 3:
                    $ ped_sex_general_action_Cond = "a01_05"
                elif p_didac.anal_received > 2:
                    $ ped_sex_general_action_Cond = "a01_04"
                elif p_didac.anal_received > 1:
                    $ ped_sex_general_action_Cond = "a01_02"
                else:
                    $ ped_sex_general_action_Cond = "a00_02"
                call pedrera_sex_p_general_talk

                # $ ped_sex_general_zoom_Cond = ""
                # call pedrera_sex_p_general_talk

                $ debug ("Sex Prove Missionary-Doggy01.")

                if p_didac.pos == "doggy":
                    $ ped_sex_general_zoom_Cond = "crotch"
                    call pedrera_sex_p_general_talk
                    with dissolve

                $ ped_check_1_10("ped_missionary_anal_moan_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    d "Ggnn...."

                elif ped_check_list_result == 2:

                    d "Ugghh..."

                elif ped_check_list_result == 3:

                    d "Hhmfmm..."

                elif ped_check_list_result == 4:

                    d "Txxx..."

                elif ped_check_list_result == 5:

                    d "A-aahmm..."

                elif ped_check_list_result == 6:

                    d "Hmmffmn..."

                elif ped_check_list_result == 7:

                    d "Nngnn..."

                elif ped_check_list_result == 8:

                    d "Ughhmmm..."

                elif ped_check_list_result == 9:

                    d "Ughh..."

                elif ped_check_list_result == 10:

                    d "Hmmm..."

                else:

                    d "Hmmm..."

                if p_prot.pos == "missionary":
                    $ ped_sex_general_zoom_Cond = ""
                    call pedrera_sex_p_general_talk

                if p_didac.anal_received == 1:

                    $ debug ("Anal with Didac 01")

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils down00
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                        with dissolve

                    n "Sugerentemente acercas la punta de tu miembro por la superficie de su orificio anal."

                    # if p_prot.pos == "doggy":
                    #     $ ped_sex_general_zoom_Cond = "crotch"
                    #     call pedrera_sex_p_general_talk
                    #     with fade_short

                    if p_didac.action == "cunnilingus_done_p_txell":

                        d "¿Queg cogño egstás haciengdo?"

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx23
                            with dissolve

                        d "¿Qué coño estás haciendo?"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 00
                        show gensex_missionary_d_head_exp_pupils front00
                        show gensex_missionary_d_head_exp_eyebrows normal
                        show gensex_missionary_d_head_exp_mouth sad_Silentx03
                        with dissolve

                    p "¿Acaso no es obvio?"

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with fade_short

                    if p_didac.action == "cunnilingus_done_p_txell":

                        d "¿Te creegs que me va egsta marigonada?"

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                            with dissolve

                        d "¿Te crees que me va esta mariconada?"

                    if afternight04_Anal_dick_med_Speed_1_Success > 0:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                            with dissolve

                        p "Ten los huevos de reconocer de una vez,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils right01
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                        p "que te encantó que te la metiera por detrás ayer por la noche."

                        if aftermorning05_Deepsea_Fuck_AnalRAW_Cond:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 00
                                show gensex_missionary_d_head_exp_pupils front00
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                                with dissolve

                            p "¡Joder!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                                with dissolve

                            p "¡Si lo has disfrutado esta mañana en la playa y todo!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                                with dissolve
                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Silentx10
                                with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Silentx09
                            with dissolve

                        d "Tsskk..."

                    if DidacPregnant == False:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                            show gensex_missionary_d_head_exp_mouth sad_Silentx04
                            with dissolve

                        p "Además,"

                        extend " por el culo no te voy a dejar preñada."

                        if p_didac.action == "cunnilingus_done_p_txell":

                            d "Lo digces gomo si no tuvgieras las neugronas sufgcientes"

                            d "como paga guitarla a tiempgo."

                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows angryx03
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx20
                                with dissolve

                            d "Lo dices como si no tuvieras las neuronas suficientes"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                                with dissolve

                            d "como para quitarla a tiempo."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows angryx02
                            show gensex_missionary_d_head_exp_mouth sad_Silentx10
                            with dissolve

                        p "Bueno,"

                        extend " para mantener esto duro,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            show gensex_missionary_d_head_exp_mouth sad_Silentx12
                            with dissolve

                        p "necesito mucha sangre ahí abajo y poca aquí arriba."

                        if p_didac.action == "cunnilingus_done_p_txell":

                            d "Gue exgusa tan magla..."

                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                                with dissolve

                            d "Que excusa tan mala..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Silentx15
                                with dissolve

                    # if afternight04_Anal_dick_med_Speed_1_Success > 0: # Not necessary.

                    if p_didac.action == "cunnilingus_done_p_txell":
                        $ Pedrera_char_Cond = "TxellSuperClose"

                    else:
                        $ Pedrera_char_Cond = "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    show m_exp_eyebrows suspiciousx01
                    with fade_short

                    tx "Déjate de pretextos y acepta que disfrutas del sexo anal."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 05
                    show m_exp_piris down05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "Se te nota que lo estás deseando,"

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    tx "pero por una gilipollez masculina te niegas a aceptarlo."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 05
                    show m_exp_piris down05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    if p_didac.action == "cunnilingus_done_p_txell":

                        n "Apartando levemente sus labios del coño de Txell."

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with fade_short

                    d "Que a una zorra como a ti le guste,"

                    extend " no significa que..."

                    #if p_prot.pos == "doggy":
                    $ ped_sex_general_zoom_Cond = "crotch"
                    $ ped_sex_general_action_Cond = "a01_01"
                    call pedrera_sex_p_general_talk

                    with fade_short
                    pause 0.5
                    with vpunch

                    d "¡AAAAHhhmmmmf...!"
                    
                    n "Sin esperar a que termine la frase, se la vas metiendo poco a poco."

                    # if p_prot.pos == "doggy":
                    #     $ ped_sex_general_zoom_Cond = ""
                    #     call pedrera_sex_p_general_talk
                    # with fade_short

                    if afternight04_Anal_dick_deep_Speed_1_Success > 1:

                        p "Pero si casi ha entrado sola..."

                        d "..."

                        if p_didac.action == "cunnilingus_done_p_txell":
                            $ Pedrera_char_Cond = "TxellSuperClose"

                        else:
                            $ Pedrera_char_Cond = "TxellClose_b"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 02
                        show m_exp_piris down02
                        show m_exp_eyebrows angryx01
                        with fade_short

                        tx "Es evidente que te dio bien duro ayer por la noche,"

                        show m_exp_mouth happy_Talkingx09
                        show m_exp_eyes 04
                        show m_exp_piris down04
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "¿Me equivoco?"

                        show m_exp_mouth happy_Silentx09
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx03
                        with dissolve

                        pause 0.2

                    else:

                        p "Tampoco ha sido tan difícil de que entrara..."

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk

                    else:

                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with vpunch

                    d "¡Gilipollas!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows sadx02
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx08
                        with dissolve

                    d "A-"

                    extend "aaavisa..."

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "crotch"
                        call pedrera_sex_p_general_talk
                        with fade_short

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx04
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                        with dissolve

                    d "¡MMhfhmm...!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils right04
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                        with dissolve

                    tx "Pero si con la cara que haces lo dices todo."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 06
                        show gensex_missionary_d_head_exp_pupils front06
                        show gensex_missionary_d_head_exp_eyebrows sadx06
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                        with dissolve

                    d "..."

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with fade_short

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx19
                        with dissolve

                    d "¡Pero me gusta más por el coño!"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 01
                        show gensex_missionary_d_head_exp_pupils front01
                        show gensex_missionary_d_head_exp_eyebrows surprisex01
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                        with dissolve

                    if DidacPregnant:

                        p "Si tanto te digusta,"

                        extend " ¿por qué estás gimiendo?"

                    else:

                        p "¿Y también quieres tener una broma de nueve meses?"

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 05
                        show gensex_missionary_d_head_exp_pupils front05
                        show gensex_missionary_d_head_exp_eyebrows angryx04
                        show gensex_missionary_d_head_exp_mouth sad_Silentx08
                        with dissolve

                    d "..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                        with dissolve

                    d "¡Tssk!..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 04
                        show gensex_missionary_d_head_exp_pupils right04
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                        with dissolve

                    d "Haz lo que quieras..."

                    if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                        show gensex_missionary_d_head_exp_eyes 08
                        show gensex_missionary_d_head_exp_pupils front08
                        show gensex_missionary_d_head_exp_eyebrows angryx05
                        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                        with dissolve

                elif p_didac.anal_received > 1:

                    $ ped_check_1_10("ped_missionary_anal_moan_didac_list")
                    #$ randomnum_1to10 = renpy.random.randint(1, 10)

                    if ped_check_list_result in range(1,6):

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                            with dissolve

                    else:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 06
                            show gensex_missionary_d_head_exp_pupils front06
                            show gensex_missionary_d_head_exp_eyebrows sadx05
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx02
                            with dissolve


                    if ped_check_list_result == 1:

                        d "¡HHhmmm...!"

                    elif ped_check_list_result == 2:

                        d "¡Hmffmm...!"

                    elif ped_check_list_result == 3:

                        d "¡Huhmmfmm...!"

                    elif ped_check_list_result == 4:

                        d "¡Huuhmmm...!"

                    elif ped_check_list_result == 5:

                        d "¡FFmmhmmm...!"

                    elif ped_check_list_result == 6:

                        d "¡Ahhhmm...!"

                    elif ped_check_list_result == 7:

                        d "¡AAah-ahmm...!"

                    elif ped_check_list_result == 8:

                        d "¡AAhhhmm...!"

                    elif ped_check_list_result == 9:

                        d "¡AAAaah...ahhmm...!"

                    elif ped_check_list_result == 10:

                        d "¡AA-aahmm...!"

                    else:

                        d "¡AA-aahmm...!"

                    ##

                    if p_prot.pos == "doggy":
                        $ ped_sex_general_zoom_Cond = "face"
                        call pedrera_sex_p_general_talk
                        with fade_short

                    if p_didac.anal_received == 2:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                            with dissolve

                        p "Parece que te guste..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx01
                            with dissolve

                        p "Quizás ya te gustaba esto antes de que fueras mujer..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Silentx12
                            with dissolve

                        p "¿No crees?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx06
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx23
                            with dissolve

                        d "¡Imbécil!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

                    elif p_didac.anal_received == 3:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows sadx03
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                        d "También me la podrías meter por el otro lado..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows serious
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                            with dissolve

                        if p_didac.action == "cunnilingus_done_p_txell":

                            p "¿Y perderme esos jadeos tuyos mientras aceptas tu homosexualidad?"

                        else:

                            p "¿Y perderme esa expresión tuya mientras aceptas tu homosexualidad?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx06
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                            with dissolve

                        d "¡Tú también me estás follando!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                        p "Pero al menos soy activo,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                        p "y tú tienes aspecto de mujer..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils right03
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                            show gensex_missionary_d_head_exp_mouth sad_Silentx09
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx06
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                            with dissolve

                        d "Serás capullo..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                    elif p_didac.anal_received == 4:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows serious
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                            with dissolve

                        p "¿Qué?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows surprisex02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                            with dissolve

                        p "¿Ya no te quejas?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx22
                            with dissolve

                        d "¡Idiota!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows surprisex01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                        p "Zorra."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Silentx09
                            with dissolve

                        d "Tssk..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                        tx "Sois como niños..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx02
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx15
                            with dissolve

                    elif p_didac.anal_received == 5:

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                            with dissolve

                        d "¿De verdad te gusta más follarme el culo que el coño?"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 03
                            show gensex_missionary_d_head_exp_pupils front03
                            show gensex_missionary_d_head_exp_eyebrows sadx01
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
                            with dissolve

                        p "Está más estrecho..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows serious
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                            with dissolve

                        p "Además,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 01
                            show gensex_missionary_d_head_exp_pupils front01
                            show gensex_missionary_d_head_exp_eyebrows normal
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                            with dissolve

                        p "verte disfrutar de esta parte que no quieres aceptar,"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 04
                            show gensex_missionary_d_head_exp_pupils front04
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Silentx07
                            with dissolve

                        p "me da un placer especial."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows angryx05
                            show gensex_missionary_d_head_exp_mouth sad_Silentx09
                            with dissolve

                        d "..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils right05
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            with dissolve

                        d "¡Serás imbécil!"

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx04
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                            with dissolve

                    elif p_didac.anal_received >= 6:

                        $ ped_check_1_10("ped_missionary_anal_didac_list")
                        #$ randomnum_1to10 = renpy.random.randint(1, 10)

                        if ped_check_list_result == 1:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                                with dissolve

                            d "¿Hace falta que vayas tan rápido?"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                            p "No parece que te moleste tanto,"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows serious
                                show gensex_missionary_d_head_exp_mouth sad_Silentx08
                                with dissolve

                            p "del modo en que gimes..."

                        elif ped_check_list_result == 2:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils front04
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                                with dissolve

                            d "La tienes muy gorda..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows sadx01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                                with dissolve

                            p "Y larga..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows normal
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                            if p_didac.analDeep_received > 0:

                                p "¿Quieres que te la vuelva a meter entera?"

                            elif afternight04__Anal_dick_deep_Success > 0:

                                p "¿Quieres que te la meta entera como ayer?"

                            else:

                                p "¿Quieres que te la meta entera?"

                        elif ped_check_list_result == 3:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 07
                                show gensex_missionary_d_head_exp_pupils front07
                                show gensex_missionary_d_head_exp_eyebrows angryx03
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx09
                                with dissolve

                            d "Serás hijo de perra..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 06
                                show gensex_missionary_d_head_exp_pupils front06
                                show gensex_missionary_d_head_exp_eyebrows sadx02
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                                with dissolve

                            d "No-"

                            extend "no es por aquí dónde tienes que meterla..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
                                with dissolve

                            p "Lo dices como si te disgustara tanto..."


                        elif ped_check_list_result == 4:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                                with dissolve

                            d "Maldito seas..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows angryx01
                                show gensex_missionary_d_head_exp_mouth sad_Silentx05
                                with dissolve

                            p "No te quejes tanto,"

                            extend " que sabes que te encanta."

                        elif ped_check_list_result == 5:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows normal
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx005
                                with dissolve

                            d "¿No será que ya le tenías ganas a mi culo antes de que me transformara en mujer?"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                                with dissolve

                            p "Es posible..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                            #d "..."

                        elif ped_check_list_result == 6:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils front02
                                show gensex_missionary_d_head_exp_eyebrows normal
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                                with dissolve

                            p "Realmente estás bien estrecha por aquí..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils right05
                                show gensex_missionary_d_head_exp_eyebrows sadx04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx08
                                with dissolve

                            #d "..."

                        elif ped_check_list_result == 7:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
                                with dissolve

                            p "Al final te va a gustar más por aquí que por delante..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils left05
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                                with dissolve

                            #d "..."

                        elif ped_check_list_result == 8:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 00
                                show gensex_missionary_d_head_exp_pupils right00
                                show gensex_missionary_d_head_exp_eyebrows surprisex02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                                with dissolve

                            tx "¡Acepta de una vez que te está encantando que te folle el trasero!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 02
                                show gensex_missionary_d_head_exp_pupils right02
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx15
                                with dissolve

                            d "¡Tú cállate!"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                            p "Sabes que tiene razón."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils left05
                                show gensex_missionary_d_head_exp_eyebrows sadx01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx07
                                with dissolve

                            #d "..."

                        elif ped_check_list_result == 9:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 08
                                show gensex_missionary_d_head_exp_pupils front08
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                                with dissolve

                            d "Al menos no te corras pronto..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 01
                                show gensex_missionary_d_head_exp_pupils front01
                                show gensex_missionary_d_head_exp_eyebrows surprisex01
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                                with dissolve

                            p "¿Tanto te gusta?"

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 04
                                show gensex_missionary_d_head_exp_pupils right04
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                                with dissolve

                            #d "..."

                        elif ped_check_list_result == 10:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils right05
                                show gensex_missionary_d_head_exp_eyebrows sadx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                                with dissolve

                        else:

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                                with dissolve

                            d "..."

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils right05
                                show gensex_missionary_d_head_exp_eyebrows sadx02
                                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx11
                                with dissolve

                        if ped_check_list_result in [5, 6, 7, 8, 9]:

                            d "..."

                        if ped_check_list_result in range(1,11):

                            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                show gensex_missionary_d_head_exp_eyes 05
                                show gensex_missionary_d_head_exp_pupils front05
                                show gensex_missionary_d_head_exp_eyebrows angryx04
                                show gensex_missionary_d_head_exp_mouth sad_Talkingx04
                                with dissolve


                            $ ped_check_1_10("ped_missionary_anal_didac_insult_list")
                            #$ randomnum_1to10 = renpy.random.randint(1, 10)

                            if ped_check_list_result == 1:

                                d "Mira que eres capullo..."

                            elif ped_check_list_result == 2:

                                d "Gilipollas..."

                            elif ped_check_list_result == 3:

                                d "Vete a tomar por el culo..."

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 00
                                    show gensex_missionary_d_head_exp_pupils front00
                                    show gensex_missionary_d_head_exp_eyebrows surprisex02
                                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                                    with dissolve

                                p "Algo así estoy haciéndote."

                                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                                    show gensex_missionary_d_head_exp_eyes 05
                                    show gensex_missionary_d_head_exp_pupils right05
                                    show gensex_missionary_d_head_exp_eyebrows angryx03
                                    show gensex_missionary_d_head_exp_mouth sad_Silentx09
                                    with dissolve

                                d "Tssk..."

                            elif ped_check_list_result == 4:

                                d "Eres un capullo..."

                            elif ped_check_list_result == 5:

                                d "Alcornoque..."

                            elif ped_check_list_result == 6:

                                d "Imbécil..."

                            elif ped_check_list_result == 7:

                                d "Gilipollas..."

                            elif ped_check_list_result == 8:

                                d "Serás zopenco..."

                            elif ped_check_list_result == 9:

                                d "Peinabombillas..."

                            elif ped_check_list_result == 10:

                                d "Pollopera..."

                            else:

                                d "Idiota..."

                        if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                            show gensex_missionary_d_head_exp_eyes 08
                            show gensex_missionary_d_head_exp_pupils front08
                            show gensex_missionary_d_head_exp_eyebrows sadx05
                            show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
                            with dissolve

################################################################################
############################################################ ANAL DEEP SEX

    elif p_prot.action in ["analDeep_done_TRY", "analDeep_done"]:

        # You can't put the dick in her ass if she feels pain, no reason to make deep pain instances.

        $ p_didac.analDeep_received_TRY  += 1

        #if p_prot.pos == "doggy":
        $ ped_sex_general_zoom_Cond = "crotch"

        if p_didac.analDeep_received >= 4:
            $ ped_sex_general_action_Cond = "a02_05"
        elif p_didac.analDeep_received == 3:
            $ ped_sex_general_action_Cond = "a02_04"
        elif p_didac.analDeep_received == 2:
            $ ped_sex_general_action_Cond = "a02_03"
        elif p_didac.analDeep_received == 1:
            $ ped_sex_general_action_Cond = "a02_02"
        elif p_didac.analDeep_received == 0:
            $ ped_sex_general_action_Cond = "a02_01"
        call pedrera_sex_p_general_talk
        with fade_short

        if p_didac.anal_dilatation < 4: # PAIN DEEP ANAL.

            $ p_didac.action = "rest"
            $ p_prot.action = "rest"
            $ ped_sex_general_action_Cond = "00"

            pause 2.1
            # $ ped_sex_general_action_Cond = "00"
            # call pedrera_sex_p_general_talk

            scene hit 15:
                truecenter
                zoom 1.5 rotate 90 ypos 0.25
            pause 0.05
            show hit 16
            pause 0.05
            show hit 17
            pause 0.05
            show hit 21
            pause 0.05
            show hit 22
            pause 0.05
            show hit 23
            pause 0.05
            play sound "audio/sfx/punch01.ogg"
            
            scene black
            with vpunch

            $ p_didac.analDeep_received_FAILED  += 1
            $ p_didac.anal_pain += 1

            if p_didac.analDeep_received_FAILED == 1:

                d "{size=40}¡¡JODEER!!{/size}"

            elif p_didac.analDeep_received_FAILED == 2:

                d "{size=45}¡¡ME CAGO EN TUS PUTOS MUERTOS PISOTEADOS!!{/size}"

            elif p_didac.analDeep_received_FAILED == 3:

                d "{size=50}¡¡LA PUTA MADRE QUE TE PARIÓ!!{/size}"

            elif p_didac.analDeep_received_FAILED == 4:

                d "{size=55}¡¡COOÑOOO!!{/size}"

            elif p_didac.analDeep_received_FAILED >= 5:

                $ ped_check_1_10("ped_analDeep_FAILED_insult_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:
                    d "{size=60}¡¡JODER!!{/size}"

                elif ped_check_list_result == 2:
                    d "{size=60}¡¡HIJO DE PUTA!!{/size}"

                elif ped_check_list_result == 3:
                    d "{size=60}¡¡MECAGÜENDIOS!!{/size}"

                elif ped_check_list_result == 4:
                    d "{size=60}¡¡HOSTIAS!!{/size}"

                elif ped_check_list_result == 5:
                    d "{size=60}¡¡COÑO!!{/size}"

                elif ped_check_list_result == 6:
                    d "{size=60}¡¡CULLONS!!{/size}"

                elif ped_check_list_result == 7:
                    d "{size=60}¡¡ME CAGO EN TU PUTA MADRE!!{/size}"

                elif ped_check_list_result == 8:
                    d "{size=60}¡¡ME CAGO EN TUS TRIPAS!!{/size}"

                elif ped_check_list_result == 9:
                    d "{size=60}¡¡HOSTIA PUTA!!{/size}"

                elif ped_check_list_result == 10:
                    d "{size=60}¡¡JODER!!{/size}"

                else:
                    d "{size=60}¡¡JODER!!{/size}"

            if p_didac.analDeep_received_FAILED == 1:

                n "De una fuerte patada,"

                n "sales disparado sintiendo un dolor considerable en tu trasero"

                n "cuando este impacta contra el suelo."

            else:

                n "De nuevo, recibes otra de sus patadas."

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            ###

            if p_didac.analDeep_received_FAILED == 1:

                show didacf_mouth sad_Talkingx09
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils front02
                show didacf_eyebrows angryx04
                with fade_short

                d "¡¿QUE PUTAS MIERDAS TE PASAN POR TU PUTA JODIDA CABEZA?!"

                show didacf_mouth sad_Talkingx08
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows angryx04
                with dissolve

                d "¡¿NO VES QUE NO CABE?!"

                show didacf_mouth sad_Talkingx09
                $ dteye = 1
                call didac_exp_tears_tears
                show didacf_pupils front01
                show didacf_eyebrows angryx04
                with dissolve

                d "¡JODER!"

                if afternight04_Anal_dick_deep_Speed_1_Success > 0:

                    show didacf_mouth sadbiting_Silentx04
                    $ dteye = 0
                    call didac_exp_tears_tears
                    show didacf_pupils front00
                    show didacf_eyebrows angryx01
                    with dissolve

                    p "Ayer te entró bastante bien..."

                    show didacf_mouth sad_Talkingx08
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils front04
                    show didacf_eyebrows angryx04
                    with dissolve

                    d "¡LA MADRE QUE TE PARIÓ!"

                    if afternight04_Anal_dick_deep_Speed_1_Success > afternight04_Anal_dick_deep_Speed_1_Failed:

                        show didacf_mouth sad_Talkingx07
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡¿ACASO NO TE ACUERDAS CUANTAS VECES ME HICISTE DAÑO"

                        show didacf_mouth sad_Talkingx08
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "ANTES DE QUE DEJARA DE QUEJARME?!"

                        show didacf_mouth sad_Silentx09
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils front04
                        show didacf_eyebrows angryx04
                        with dissolve

                        p "..."

                    else:

                        show didacf_mouth sad_Talkingx08
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡ME LA SOPLA QUE CUPIERA AYER!"

                show didacf_mouth sad_Talkingx09
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows angryx04
                with dissolve

                d "¡ME HAS HECHO DAÑO COÑO!"

                show didacf_mouth sad_Silentx08
                $ dteye = 3
                call didac_exp_tears_tears
                show didacf_pupils right03
                show didacf_eyebrows angryx03
                with dissolve

                tx "*Sigh*"

                if p_didac.action == "cunnilingus_done_p_txell":
                    $ Pedrera_char_Cond = "TxellSuperClose"

                else:
                    $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with fade_short

                tx "Desde luego..."

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows normal
                with dissolve

                tx "Con el tamaño de polla que tienes,"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows suspiciousx01
                with dissolve

                tx "una pensaría que entenderías mejor el término \"preliminares\""

                extend " y \"dilatación\","

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "pero supongo que eso es pedirte demasiado."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab

                show didacf_mouth sad_Silentx05
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                with fade_short

                p "..."

                show didacf_mouth sadbiting_Silentx02
                $ dteye = 3
                call didac_exp_tears_tears
                show didacf_pupils right03
                show didacf_eyebrows serious
                with dissolve

                tx "Aunque en el fondo,"

                show didacf_mouth sadbiting_Silentx02
                $ dteye = 0
                call didac_exp_tears_tears
                show didacf_pupils right00
                show didacf_eyebrows surprisex01
                with dissolve

                tx "ya le está bien empleado a Dídac."

                show didacf_mouth sad_Talkingx08
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils right04
                show didacf_eyebrows angryx03
                with dissolve

                d "¡¿Cómo dices?!"

                show didacf_mouth sad_Silentx01
                $ dteye = 0
                call didac_exp_tears_tears
                show didacf_pupils right00
                show didacf_eyebrows surprisex02
                with dissolve

                tx "¿Nunca se la has metido a ninguna por detrás sin que se quejara de lo mismo?"

                show didacf_mouth sadbiting_Silentx04
                $ dteye = 1
                call didac_exp_tears_tears
                show didacf_pupils front01
                show didacf_eyebrows suspiciousx01
                with dissolve

                d "..."

                show didacf_mouth sad_Talkingx004
                $ dteye = 8
                call didac_exp_tears_tears
                show didacf_pupils front08
                show didacf_eyebrows angryx03
                with dissolve

                d "No-"

                extend "No es lo mismo..."

                show didacf_mouth sadbiting_Silentx05
                $ dteye = 5
                call didac_exp_tears_tears
                show didacf_pupils right05
                show didacf_eyebrows angryx03
                with dissolve

                tx "¿Ah no?"

                $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 04
                show m_exp_piris left04
                show m_exp_eyebrows surprisex001
                with fade_short

                tx "¿Y qué diferencia hay?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris left05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab

                show didacf_mouth sadbiting_Silentx04
                $ dteye = 8
                call didac_exp_tears_tears
                show didacf_pupils front08
                show didacf_eyebrows angryx04
                with fade_short

                d "Tssk..."

                show didacf_mouth sad_Talkingx07
                $ dteye = 3
                call didac_exp_tears_tears
                show didacf_pupils front03
                show didacf_eyebrows angryx03
                with dissolve

                d "¡Solo ve con cuidado!"

                show didacf_mouth sad_Talkingx08
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils front02
                show didacf_eyebrows angryx04
                with dissolve

                d "¡¿Vale?!"

                show didacf_mouth sad_Talkingx05
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                with dissolve

                d "¡Y métemela un poco por el coño ahora!..."

                show didacf_mouth sad_Talkingx005
                $ dteye = 8
                call didac_exp_tears_tears
                show didacf_pupils front08
                show didacf_eyebrows angryx04
                with dissolve

                d "¡Que duele, joder!"

                call ped_D_NoSex ##########################################

                show didacf_mouth sad_Silentx05
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils right02
                show didacf_eyebrows suspiciousx01
                with dissolve

                tx "No has respondido a mi pregunta."

                show didacf_mouth sad_Talkingx08
                $ dteye = 8
                call didac_exp_tears_tears
                show didacf_pupils front08
                show didacf_eyebrows angryx04
                with dissolve

                d "Paso de ti."

                show didacf_mouth sad_Silentx05
                $ dteye = 5
                call didac_exp_tears_tears
                show didacf_pupils right05
                show didacf_eyebrows angryx03
                with dissolve

                tx "Ya..."

                show didacf_mouth sad_Silentx08
                $ dteye = 5
                call didac_exp_tears_tears
                show didacf_pupils left05
                show didacf_eyebrows angryx03
                with dissolve

                p "..."

            elif p_didac.analDeep_received_FAILED  > 1:

                $ ped_check_1_10("ped_analDeep_FAILED_didac_list")
                #$ randomnum_1to5 = renpy.random.randint(1, 5)

                show didacf_mouth sad_Talkingx09
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils front02
                show didacf_eyebrows angryx04
                with fade_short

                if ped_check_list_result == 1:

                    d "¡¿QUÉ COÑO ES LO QUE NO ENTIENDES?!"

                elif ped_check_list_result == 2:

                    d "¡ESTÁS JODIDAMENTE ENFERMO COÑO!"

                elif ped_check_list_result == 3:

                    d "¡AL FINAL TE VOY A METER UN PALO ENTERO POR EL CULO Y VERÁS!"

                elif ped_check_list_result == 4:

                    d "¡¿ES QUE ERES RETRASADO MENTAL?!"

                elif ped_check_list_result == 5:

                    d "¡¿ES QUE NO ME OYES?!"

                    show didacf_mouth sad_Talkingx08
                    $ dteye = 3
                    call didac_exp_tears_tears
                    show didacf_pupils front03
                    show didacf_eyebrows angryx04
                    with dissolve

                    d "¡¿O QUÉ COÑO PASA CONTIGO?!"

                elif ped_check_list_result == 6:

                    d "¡TE VOY A METER ORTIGAS POR EL CULO CON UN TUBO Y VAS A VER COMO ME VOY A REIR!"

                elif ped_check_list_result == 7:
                    
                    d "¡¿TE CREES QUE SOY UN PUTO JUGUETE?!"

                elif ped_check_list_result == 8:
                    
                    d "¡¿ES QUE QUIERES PARTIR EN DOS?!"

                elif ped_check_list_result == 9:
                    
                    d "¡ERES UN PUTO ENFERMO!"

                elif ped_check_list_result == 10:
                    
                    d "¡TE VOY A METER LA PIERNA ENTERA POR EL CULO!"

                else:
                    
                    d "¡LA MADRE QUE TE PARIÓ!"

                show didacf_mouth sad_Silentx09
                $ dteye = 5
                call didac_exp_tears_tears
                show didacf_pupils front05
                show didacf_eyebrows angryx04
                with dissolve

            elif p_didac.analDeep_received_FAILED  >= 4:

                call afternight05_Pedrera_Neus_Warning

        else:

            $ p_prot.analDeep_done += 1
            $ p_didac.analDeep_received += 1
            
            $ p_prot.action = "analDeep_done"
            $ p_didac.b_action = "analDeep_received"

            with vpunch

            if p_didac.analDeep_received == 1:

                d "{size=40}¡¡JODEER!!{/size}"

            elif p_didac.analDeep_received == 2:

                d "{size=40}¡¡COÑOO!!{/size}"

            elif p_didac.analDeep_received == 3:

                d "{size=35}¡DIOOS!{/size}"

            elif p_didac.analDeep_received == 4:

                d "{size=30}¡HOSTIAS...!{/size}"

            elif p_didac.analDeep_received > 4:

                d "{size=28}¡MMMFHMM...!{/size}"

            ####


            if p_didac.analDeep_received == 1:

                n "La sensación de asfixia que sufre tu polla en lo más profundo de su cavidad anal,"

                n "consigue estremecer todo tu cuerpo."

                pt "Desde luego,"

                extend " está bien prieta aquí..."

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 00
                    show gensex_missionary_d_head_exp_pupils front00
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx23

                with fade_short

                d "La madre que te parió..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 03
                    show gensex_missionary_d_head_exp_pupils front03
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx24
                    with dissolve

                d "¡¿Acaso no ves que la tienes enorme?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 06
                    show gensex_missionary_d_head_exp_pupils front06
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx18
                    with dissolve

                d "¡¿Hacía falta metérmela entera?!"

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 04
                    show gensex_missionary_d_head_exp_pupils right04
                    show gensex_missionary_d_head_exp_eyebrows angryx05
                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
                    with dissolve

                tx "No parece que te quejes tanto..."

                if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils left05
                    show gensex_missionary_d_head_exp_eyebrows angryx06
                    show gensex_missionary_d_head_exp_mouth sad_Silentx06
                    with dissolve

                pause 0.2

                $ ped_sex_general_zoom_Cond = "crotch"
                call pedrera_sex_p_general_talk
                with fade_short

                d "Tssk..."

            elif p_didac.analDeep_received == 2:

                d "Hostia..."

                $ ped_sex_general_zoom_Cond = "face"
                call pedrera_sex_p_general_talk
                with fade_short

                d "La madre que te parió..."

                $ Pedrera_char_Cond =  "TxellClose_b_show"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex001
                with fade

                tx "¿Es que no sabes decir nada más?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond =  "p_nobody"
                call Pedrera_char_lab

                with fade_short

                if p_txell.analDeep_received == 0:

                    d "Como se nota que no te la ha metido entera a ti por detrás..."

                    if FuckM_Start_Cond:

                        tx "Quizás aún no..."

                    else:

                        tx "Es posible."

                else:

                    d "Quizás a ti te molara más porque eres una jodida enferma."

                    tx "Mira quien habla..."

                d "Tsskk..."

            elif p_didac.analDeep_received == 3:

                d "Puto pollón que tienes cabrón..."

                d "Pero me gustaría más sentirla así en mi coño y no en mi puto culo!"

                if DidacPregnant:
                
                    pass

                else:

                    ne "..."

                    tx "Estoy segura que cuando vuelvas a ser hombre,"

                    tx "esto lo vas a echar de menos..."

                    d "..."

                d "¡Mañana no me podré ni sentar!"

                tx "En realidad,"

                extend " creo que tampoco te podrías sentar aunque te la metiera por delante,"

                tx "con este tamaño,"

                extend " da igual por que agujero te la meta..."

                if p_txell.analDeep_received > 0:

                    tx "A mi me ha dolido igual..."

                else:

                    p "tiene que doler igual..."

                $ debug ("Anal Deep received Successfully: [p_didac.analDeep_received]")


            elif p_didac.analDeep_received >= 4:

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if randomnum_1to5 == 1:

                    d "Dios..."

                elif randomnum_1to5 == 2:

                    d "Joder..."

                elif randomnum_1to5 == 3:

                    d "Hostias..."

                elif randomnum_1to5 == 4:

                    d "Coño..."

                elif randomnum_1to5 == 5:

                    d "Mierda..."

    # image AFTER

    # if p_prot.pos == "doggy":
    #     $ ped_sex_general_zoom_Cond = ""
    #     call pedrera_sex_p_general_talk
    #     with fade

    # elif p_prot.pos == "missionary":

    #     $ ped_sex_general_expression_Cond = "closed"
    #     $ ped_sex_general_zoom_Cond = ""
    #     call pedrera_sex_p_general_talk
    #     with fade

    return


label afternight05_Pedrera_Sex_p_didac_missionary:

    $ debug ("Missionary Sex with Didac Previs.")

    call afternight05_Pedrera_Sex_p_didac_doggy

    return

label afternight05_Pedrera_Sex_p_didac_69:

    $ p_didac.pos_69 += 1
    $ p_prot.pos_69 += 1

    # If she didn't sucked you cock on minigame, she has repairs here to suck yours.

    if p_didac.pos_69 == 1:

        scene bg dark_a_blurry_02:
            truecenter

        show gensex_69_R_pussy_full_d:
            subpixel True
            truecenter
            zoom 0.5
            ypos 1.2
            easein_quad 10.0 ypos 0.5

    else:
        if p_prot.action == "rest" and p_didac.action == "rest":
            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

    $ debug ("69 Sex with Didac.")


    if p_didac_blowjob_done_ACCEPTED == True and p_prot.action == "cunnilingus_done" and p_prot.b_action not in ["blowjobDeep_received_TRY", "blowjobDeep_received", "takeDickOut"]:

        # Did you take off your dick from her mouth? NOT FINISHED

        if p_didac.throat_pain > 0:

            $ p_didac.action = "rest"
            $ p_prot.b_action = "rest"

            $ p_didac.blowjobDeep_received_FAILED += 1
            $ p_didac.blowjobDeep_received_FAILED_temp += 1

            if p_didac.blowjobDeep_received_FAILED == 1:

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡Ni de coña!"

                show gensex_69_L_d_mouth sad_Talkingx11
                with dissolve

                d "¡Aún me duele la jodida garganta!"

            elif p_didac.blowjobDeep_received_FAILED == 2:

                show gensex_69_L_d_mouth sad_Talkingx11
                with dissolve

                d "¡Me sigue doliendo!"

            elif p_didac.blowjobDeep_received_FAILED > 2:

                $ ped_check_1_10("ped_blowjobDeep_FAILED_didac_list")

                show gensex_69_L_d_mouth sad_Talkingx11
                with dissolve

                #$ randomnum_1to5 = renpy.random.randint(1, 5)

                if ped_check_list_result == 1:

                    d "¡¿Es que no me explico?!"

                elif ped_check_list_result == 2:

                    d "¡¿Quieres que te meta un bate de béisbol por la tráquea?!"

                elif ped_check_list_result == 3:

                    d "¡Como lo vuelvas a intentar te dejo sin pelotas!"

                elif ped_check_list_result == 4:

                    d "¡Que dejes mi garganta en paz!"

                elif ped_check_list_result == 5:

                    d "¡Al final te voy a morder la polla!"

                elif ped_check_list_result == 6:

                    d "¡TE VOY A DEJAR SIN PELOTAS!"

                elif ped_check_list_result == 7:

                    d "¡AL FINAL TE TRAGARÁS MI PUÑO!"

                elif ped_check_list_result == 8:

                    d "¡VOY A METERTE TAL HOSTIA"

                    show gensex_69_L_d_mouth sad_Talkingx12
                    with dissolve

                    d "QUE TE VAN A SALIR LOS HUEVOS POR LA BOCA!"

                elif ped_check_list_result == 9:

                    d "¡¿ES QUE ME QUIERES AHOGAR?!"

                    show gensex_69_L_d_mouth sad_Talkingx12
                    with dissolve

                    d "¡¿O QUÉ COÑO TE PASA?!"

                elif ped_check_list_result == 10:

                    d "¡QUE NO CABE, JODER!"

                else:

                    d "¡Que hostia tienes!"

                show gensex_69_L_d_mouth sad_Silentx10
                with dissolve

            ####

            call p_character_throat_pain_common

            show gensex_69_L_d_mouth sad_Silentx09
            with dissolve

        elif takeDickOut_Cond > 1:

            $ p_didac.action = "rest"
            $ p_prot.b_action = "rest"

            $ takeDickOut_Cond -= 1
            $ p_didac_takeDickOut_attempt += 1

            show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

            if p_didac_takeDickOut_attempt == 1:

                d "Primero la quitas,"

                extend " y ahora la quieres volver a meter."

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡Pues ahora te aguantas!"

            elif p_didac_takeDickOut_attempt == 2:

                d "¡¿Otra vez?!"

                d "¡¿Te crees que soy un juguete?!"

            elif p_didac_takeDickOut_attempt >= 3:

                $ ped_check_1_5("ped_takeDickOut_attempt_didac_list")

                if ped_check_list_result == 1:

                    d "¡¿Me tomas por imbécil?!"

                elif ped_check_list_result == 2:

                    d "¡¿Te crees que soy idiota?!"

                elif ped_check_list_result == 2:

                    d "¿Ahora sí?"

                    d "¡Pues te aguantas!"

                elif ped_check_list_result == 2:

                    d "¡Te lo hubieras pensado antes!"

                elif ped_check_list_result == 2:

                    d "¡¿Te crees que puedes ir cambiando de opinión a tu antojo?!"

                else:

                    d "..."

            show gensex_69_L_d_mouth sad_Silentx07
            with dissolve

        else:

            $ p_didac.blowjobDeep_received_FAILED_temp = 0

            $ debug ("Didac is sucking your cock.")

            if takeDickOut_Cond == 1:

                $ takeDickOut_Cond = 0

                $ p_didac_takeDickOut_againIn += 1

                if p_didac_takeDickOut_againIn == 1:

                    d "Tskk..."

                    d "Decídete, capullo."

                else:

                    $ ped_check_1_5("ped_takeDickOut_againIn_didac_list")

                    if ped_check_list_result == 1:

                        d "¡Al final te daré un mordisco que te la partiré en dos!"

                    elif ped_check_list_result == 2:

                        d "¡Eres un cagadudas!"

                    elif ped_check_list_result == 2:

                        d "¡Será mejor que te decidas de una vez!"

                    elif ped_check_list_result == 2:

                        d "¡¿Haces lo mismo con todas las tías?!"

                    elif ped_check_list_result == 2:

                        d "¡No te recordaba tan tocapelotas!"

                    else:

                        d "..."

            $ p_didac.blowjob_done += 1
            $ p_prot.blowjob_received += 1
            $ p_didac.throat_dilatation += 1

            $ p_prot.cunnilingus_done += 1
            $ p_didac.cunnilingus_received += 1
            $ p_didac.cunnilingus_69_received += 1

            $ p_didac.vaginal_dilatation += 1

            $ p_didac.action = "blowjob_done"
            $ p_prot.b_action = "blowjob_received"

            call ped_sex_69_mc_lickpussy01
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                d "¡Ugh...!"

            elif randomnum_1to5 == 2:

                d "¡Humm...!"

            elif randomnum_1to5 == 3:

                d "¡Ahhm...!"

            elif randomnum_1to5 == 4:

                d "¡Uhm...!"

            elif randomnum_1to5 == 5:

                d "¡Mm...!"

            if p_didac.blowjob_done > 1:

                if p_prot.action == "cunnilingus_done":

                    $ debug("69 Oral done by Didac while your licking her pussy.")

                else:

                    $ debug("69 Oral done by Didac without you licking her pussy.")


            #$ ped_sex_general_69_cover = "dissolve"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_b_Cond = "69b_00_00b"
            call pedrera_sex_p_general_talk

            show gensex_69_L_d_mouth happybiting_Silentx04
            with Dissolve(0.5)

            pause 0.2

            if p_didac.cunnilingus_69_received == 1:

                if p_didac.cunnilingus_received == 1:

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    d "A ver cómo de bueno eres con esto..."

                    if afternight04__Pussy_Tongue_Success > 0:

                        show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                        p "Como si no te lo hubiera hecho ya..."

                        show gensex_69_L_d_mouth happy_Talkingx07
                        with dissolve

                        d "Calla y usa esa lengua tuya."

                        show gensex_69_L_d_mouth happybiting_Silentx04
                        with dissolve

                        p "..."

                else:

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    d "No te diré que no..."

            elif p_didac.cunnilingus_69_received >= 2:

                $ ped_check_1_10("ped_69_cunnilingus_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_69_L_d_mouth sad_Talkingx005
                    with dissolve

                    d "¡No pares con esa lengua!"

                elif ped_check_list_result == 2:

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    d "¡No se te da nada mal!"

                elif ped_check_list_result == 3:

                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve
                    
                    d "¡Tienes una lengua enorme, cabrón!"

                elif ped_check_list_result == 4:

                    show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve
                    
                    d "¡No pares!"

                elif ped_check_list_result == 5:

                    show gensex_69_L_d_mouth sad_Talkingx09
                    with dissolve
                    
                    d "¡Ni se te ocurra correrte en mi boca!"

                elif ped_check_list_result == 6:

                    show gensex_69_L_d_mouth sad_Talkingx005
                    with dissolve
                    
                    d "Si no paras con esa lengua tuya,"

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    d "tampoco me molesta tanto usar la mía..."

                elif ped_check_list_result == 7:

                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve
                    
                    d "¡¿Cómo es posible que tengas la lengua tan larga?!"

                elif ped_check_list_result == 8:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve
                    
                    d "Aparte de pollón..."

                    show gensex_69_L_d_mouth happy_Talkingx09
                    with dissolve

                    d "¡Pedazo lengua!"

                elif ped_check_list_result == 9:

                    show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve
                    
                    d "¡No te acostumbres a lo que te estoy haciendo!"

                elif ped_check_list_result == 10:

                    show gensex_69_L_d_mouth sadbiting_Talkingx06
                    with dissolve
                    
                    d "La madre que te parió.."

                else:

                    show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve
                    
                    d "Hmffmm..."

            $ ped_sex_general_expression_Cond = ""
            $ ped_sex_general_action_b_Cond = "69b_01_01"
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)


                #call p_didac_cunnilingus_received_label

    elif p_prot.b_action in ["blowjobDeep_received_TRY", "blowjobDeep_received"] and p_prot.action == "cunnilingus_done":

        $ debug("You try DEEPTHROAT her throat")

        if p_didac.throat_dilatation >= 5:

            $ debug("She has a good throat dilatation.")

            $ p_didac.blowjobDeep_received += 1
            $ p_prot.blowjobDeep_done += 1
            $ p_didac.throat_dilatation += 1

            $ p_prot.b_action = "blowjobDeep_received"
            $ p_didac.action = "blowjobDeep_done"

            $ ped_sex_general_expression_Cond = ""

            
            if p_didac.blowjobDeep_received >= 10:
                $ ped_sex_general_action_b_Cond = "69b_04_05"
            elif p_didac.blowjobDeep_received == 9:
                $ ped_sex_general_action_b_Cond = "69b_04_04"
            elif p_didac.blowjobDeep_received == 8:
                $ ped_sex_general_action_b_Cond = "69b_04_03"
            elif p_didac.blowjobDeep_received == 7:
                $ ped_sex_general_action_b_Cond = "69b_04_02"
            elif p_didac.blowjobDeep_received == 6:
                $ ped_sex_general_action_b_Cond = "69b_04_01"
            elif p_didac.blowjobDeep_received == 5:
                $ ped_sex_general_action_b_Cond = "69b_03_05"
            elif p_didac.blowjobDeep_received == 4:
                $ ped_sex_general_action_b_Cond = "69b_03_04"
            elif p_didac.blowjobDeep_received == 3:
                $ ped_sex_general_action_b_Cond = "69b_03_03"
            elif p_didac.blowjobDeep_received == 2:
                $ ped_sex_general_action_b_Cond = "69b_03_02"
            else:
                $ ped_sex_general_action_b_Cond = "69b_03_01"


            call pedrera_sex_p_general_talk

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if p_didac.blowjobDeep_received < 6:

                if randomnum_1to5 == 1:

                    d "¡Hgh!"

                elif randomnum_1to5 == 2:

                    d "¡Argh!"
                elif randomnum_1to5 == 3:

                    d "¡Uhgh!"

                elif randomnum_1to5 == 4:

                    d "¡Ggh!"

                elif randomnum_1to5 == 5:

                    d "¡Ugh!"

            else:

                if randomnum_1to5 == 1:

                    d "¡¡Uuuughh!!"

                elif randomnum_1to5 == 2:

                    d "¡¡Argghh!!"
                    
                elif randomnum_1to5 == 3:

                    d "¡¡GGGhhh!!"

                elif randomnum_1to5 == 4:

                    d "¡¡Gughhh!!"

                elif randomnum_1to5 == 5:

                    d "¡¡Unghhh!!"


            $ debug("You succeded doing a deepthroat to Didac: " + str(p_didac.blowjobDeep_received))

            if p_didac.blowjobDeep_received == 1: # Did he done it in oral?

                n "Con cierta suavidad,"

                n "consigues penetrar el interior de su garganta sin que ofrezca demasiada resistencia."

                tx "No está mal Dídac,"

                extend " no está mal..."

                d "Tgsshsk..."

            elif p_didac.blowjobDeep_received == 2:

                n "Con algo más de confianza,"

                n "logras aumentar ligeramente el ritmo sin que le den arcadas."

            elif p_didac.blowjobDeep_received == 6:

                n "Con cierta pericia,"

                n "logras metérsela completamente en su garganta."

                $ Pedrera_char_Cond = "TxellClose_b_show"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex01
                with fade_short

                tx "Caray..."

                show m_exp_mouth happy_Talkingx04
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows sadx01
                with dissolve

                tx "Sinceramente,"

                extend " no me esperaba que llegaras a metérsela entera..."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows surprisex01
                with dissolve

                ne "La verdad es que sí..."

                $ Pedrera_char_Cond = "NeusClose_show"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with fade_short

                ne "Es algo que hasta a mi me requiere tiempo y concentración..."

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris left00
                show neus_exp_eyebrows surprisex02
                with dissolve

                tx "Tampoco tanto..."

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows sadx01
                with dissolve

                tx "no exageres."

                show neus_exp_mouth happybiting_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "..."

                $ ped_sex_general_zoom_Cond = ""
                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab
                with vpunch

                d "¡GGGHHhh!"

                pt "Por lo visto a nadie le preocupa aquí que Dídac se quede sin aire..."

            

        else:

            $ debug("You failed on Deepthroating her.")

            $ ped_sex_general_expression_Cond = ""
            $ ped_sex_general_action_b_Cond = "69b_03_01"
            call pedrera_sex_p_general_talk
            with Dissolve(1.0)

            $ p_didac.throat_pain += 3
            $ p_didac.throat_dilatation -= 2
            $ p_didac.blowjobDeep_received_FAILED += 1

            pause 1.0

            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk

            $ ped_check_1_10("ped_blowjobDeep_FAILED_insult_didac_list")
            #$ randomnum_1to5 = renpy.random.randint(1, 5)

            show gensex_69_L_d_mouth sad_Talkingx10
            with vpunch

            if ped_check_list_result == 1:

                d "¡¡JODER!!"

            elif ped_check_list_result == 2:

                d "¡¡COÑO!!"

            elif ped_check_list_result == 3:

                d "¡¡HOSTIAS!!"

            elif ped_check_list_result == 4:

                d "¡¡ARRGHH!!"

            elif ped_check_list_result == 5:

                d "¡¿PERO QUÉ COÑO?!"

            elif ped_check_list_result == 6:

                d "¡¡ME CAGO EN TUS MUERTOS!!"

            elif ped_check_list_result == 7:

                d "¡¡LA CONCHA DE TU MADRE!!"

            elif ped_check_list_result == 8:

                d "¡¡SERÁS HIJO DE PUTA!!"

            elif ped_check_list_result == 9:

                d "¡¡LA MADRE QUE TE PARIÓ!!"

            elif ped_check_list_result == 10:

                d "¡¡HOSTIA PUTA!!"

            else:

                d "¡¡JODER!!"


        ###
            
            if p_didac.blowjobDeep_received_FAILED_temp == 1 and p_didac.blowjobDeep_received_FAILED > 1:

                # After she gets relaxed, you try it once again.

                $ ped_check_1_10("ped_blowjobDeep_received_Failed_Again_didac_01_list")

                if ped_check_list_result == 1:

                    d "¡¿VUELVES CON LO MISMO?!"

                elif ped_check_list_result == 2:

                    d "¡¿OTRA VEZ?!"

                elif ped_check_list_result == 3:

                    d "¡¿EN SERIO?!"

                elif ped_check_list_result == 4:

                    d "¡¿PERO DE QUÉ COÑO VAS?!"

                elif ped_check_list_result == 5:

                    d "¡¿OTRA PUTA VEZ?!"

                $ ped_check_1_10("ped_blowjobDeep_received_Failed_Again_didac_02_list")

                if ped_check_list_result == 1:

                    d "¡QUE LA TIENES ENORME JODER!"

                elif ped_check_list_result == 2:

                    d "¡ES UNA PUTA ANACONDA!"

                    d "¡¿ES QUE NO LO ENTIENDES?!"

                elif ped_check_list_result == 3:

                    d "¡¿ES QUE ERES RETRASADO?!"

                elif ped_check_list_result == 4:

                    d "¡¿TAN JODIDAMENTE ENFERMO ESTÁS QUE NO TE DAS CUENTA DE QUE NO CABE?!"

                elif ped_check_list_result == 5:

                    d "¡¡QUE NO CABE JODER!!"

                else:

                    d "¡¡JODER!!"

            elif p_didac.blowjobDeep_received_FAILED == 1:

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡LA MADRE QUE TE PARIÓ!"

                show gensex_69_L_d_mouth sad_Talkingx11
                with dissolve

                d "¡¿ES QUE NO VES QUE NO CABE?!"

                if afternight04__MMouth_dick_Deep_Success > 0:

                    show gensex_69_L_d_mouth sad_Silentx08
                    with dissolve

                    p "Bieng gue te la pudiste meter agyer por la nogche..."

                    show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                    d "..."

                    show gensex_69_L_d_mouth sad_Silentx09
                    with dissolve

                    tx "Quizás sea porque ayer te lo trabajaste mejor antes de metérsela en la boca."

                $ Pedrera_char_Cond = "TxellClose_b_show"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with fade_short

                tx "Con el tamaño que tienes,"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                tx "deberías saber que se necesita un poco de tiempo para preparar el terreno..."

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows sadx01
                with dissolve

                tx "Pero supongo que eso demasiado pedirte."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "p_nobody"
                call Pedrera_char_lab

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡ENCIMA DE QUE TE LA ESTABA CHUPANDO, IMBÉCIL!"

                show gensex_69_L_d_mouth sad_Silentx10
                with dissolve

            elif p_didac.blowjobDeep_received_FAILED == 2:

                show gensex_69_L_d_mouth sad_Silentx10
                with dissolve

                d "¡AL FINAL TE LA ARRANCARÉ DE UN MORDISCO!"

                show gensex_69_L_d_mouth sad_Silentx08
                with dissolve

                pt "Entonces sí que ya no serías capaz de respirar..."

            elif p_didac.blowjobDeep_received_FAILED == 3:

                show gensex_69_L_d_mouth sad_Talkingx11
                with dissolve

                d "¡¿ES QUE ERES RETRASADO O QUÉ COÑO TE PASA?!"

                show gensex_69_L_d_mouth sad_Silentx10
                with dissolve

            elif p_didac.blowjobDeep_received_FAILED >= 4:

                $ ped_check_1_10("ped_blowjobDeep_FAILED_insult02_didac_list")
                #$ randomnum_1to5 = renpy.random.randint(1, 5)

                if ped_check_list_result in range(1,11):
                    show gensex_69_L_d_mouth sad_Talkingx09
                else:
                    show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                if ped_check_list_result == 1:

                    d "¡TE VOY A ROMPER LOS HUEVOS!"

                elif ped_check_list_result == 2:

                    d "¡DÉJAME LA GARGANTA EN PAZ!"

                elif ped_check_list_result == 3:

                    d "¡ENCIMA DE QUE  TE LA ESTOY CHUPANDO!"

                elif ped_check_list_result == 4:

                    d "¡¿ES QUE QUIERES MATARME,"

                    show gensex_69_L_d_mouth sad_Talkingx10
                    with dissolve

                    d "O QUÉ COÑO QUIERES?!"

                elif ped_check_list_result == 5:

                    d "¡¿ES QUE ERES SORDO O RETRASADO?!"

                elif ped_check_list_result == 6:

                    d "¡¿ES QUE TU MADRE TE VOMITÓ EN LUGAR DE PARIRTE,"

                    show gensex_69_L_d_mouth sad_Talkingx10
                    with dissolve

                    d "O QUÉ COÑO TE PASA?!"

                elif ped_check_list_result == 7:

                    d "¡¿ES QUE ME QUIERES MATAR?!"

                elif ped_check_list_result == 8:

                    d "¡¿ES QUE ERES DEFICIENTE MENTAL?!"

                elif ped_check_list_result == 9:

                    d "¡¿ACASO NO LO ENTIENDES?!"

                elif ped_check_list_result == 10:

                    d "¡¡QUE NO CABE, JODER!!"

                else:

                    d "..."

                show gensex_69_L_d_mouth sad_Silentx11
                with dissolve

                call p_didac_insulting_02

                show gensex_69_L_d_mouth sad_Silentx09
                with dissolve


            

    elif p_prot.b_action == "blowjob_received_TRY" and p_prot.action != "takeTongueOut":
    #elif p_didac_blowjob_done_ACCEPTED == False and p_prot.pos_69_rest > 0:
    #elif p_prot.b_action == "blowjob_received_TRY" and p_didac.action != "blowjob_done": #Wich means your dick is still not inside her mouth, but you're trying.

        $ p_didac.blowjob_done_TRY +=1

        if p_didac_blowjob_done_ACCEPTED == False:

            #$ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_expression_Cond = "talk"
            if p_didac.blowjob_done_TRY == 1:
                $ ped_sex_general_action_b_Cond = "69b_00_01"
            elif p_didac.blowjob_done_TRY == 2:
                $ ped_sex_general_action_b_Cond = "69b_00_02"
            elif p_didac.blowjob_done_TRY == 3:
                $ ped_sex_general_action_b_Cond = "69b_00_03"
            elif p_didac.blowjob_done_TRY == 4:
                $ ped_sex_general_action_b_Cond = "69b_00_04"
            else:
                $ ped_sex_general_action_b_Cond = "69b_00_05"

        else:
            pass

        call pedrera_sex_p_general_talk
        

        if p_didac.blowjob_done_TRY == 1: # Not suck your dick yet, even if she did.

            show gensex_69_L_d_mouth sad_Silentx04

            with dissolve

            n "Sugerentemente,"

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

            n "mueves tus caderas para intentar acercar el glande de tu miembro"

            show gensex_69_L_d_mouth sad_Silentx06
            with dissolve

            n "a sus carnosos labios."

            show gensex_69_L_d_mouth sad_Talkingx09
            with dissolve

            d "¿Se puede saber qué coño estás haciendo?"

            show gensex_69_L_d_mouth sad_Talkingx08
            with dissolve

            d "¡¿No querías comerme el coño?!"

            if p_prot.action == "cunnilingus_done":

                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

                d "Pues sigue."

            else:

                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

                d "¡Porque no veo que uses tu lengua ahí abajo!"


            if p_didac.blowjob_done == 0:

                if afternight04__MMouth_dick_Success > 0:

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    if p_prot.action == "cunnilingus_done":

                        p "¿Por gue no intengtas hagcer lo mismo gue hicistge agyer?"

                    else:

                        p "¿Por qué no intentas hacer lo mismo que hiciste ayer?"

                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                    d "Estás de coña,"

                    extend " ¿Verdad?"

                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                    d "¡Te dije que lo de ayer fue una excepción"

                    show gensex_69_L_d_mouth sad_Talkingx09
                    with dissolve

                    d "que simplemente fue para que se te pusiera dura!"

                    show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                    d "Solo quería que me follaras en condiciones, joder!"

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    if p_prot.action == "cunnilingus_done":

                        p "Sabes perfegtamente gue estaba bien dugra,"

                    else:

                        p "Sabes perfectamente que estaba bien dura,"

                    show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

                    if p_prot.action == "cunnilingus_done":

                        p "y aúng así me la chupgaste."

                    else:

                        p "y aún así me la chupaste."

                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                    d "No pienso volver a metérmela en la boca."

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    if p_prot.action == "cunnilingus_done":

                        p "Sabes gue te gustó..."

                    else:

                        p "Sabes que te gustó..."

                    show gensex_69_L_d_mouth sad_Talkingx09
                    with dissolve

                    d "¡Vete a la mierda!"

                    show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "TxellClose_b"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows serious
                    with fade_short

                    tx "No seas tan orgulloso,"

                    extend " y acepta que te gustó."

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows sadx01
                    with dissolve

                    tx "Se te nota en la cara."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    pause 0.2

                    call pedrera_sex_p_general_talk
                    show gensex_69_L_d_mouth sad_Talkingx09
                    with fade_short

                    d "¡Tú cállate,"

                    extend " que esto no va contigo!"

                    show gensex_69_L_d_mouth sad_Silentx07
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Talkingx06
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx03
                    with fade_short

                    ne "Os recuerdo que no tenemos toda la noche."

                    show neus_exp_mouth sad_Silentx04
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    pause 0.2

                    call pedrera_sex_p_general_talk
                    show gensex_69_L_d_mouth sad_Silentx06
                    with fade_short

                    d "Tssk..."

                else:

                    show gensex_69_L_d_mouth sad_Silentx07
                    with dissolve

                    p "¿Por qué no lo intentas?"

                    show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                    d "¡Por que no!"

                    show gensex_69_L_d_mouth sad_Talkingx09
                    with dissolve

                    d "¡Y deja de insistir!"

                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                    d "¡Pesado!"

                    show gensex_69_L_d_mouth sad_Silentx07
                    with dissolve

                    p "..."

            else:

                show gensex_69_L_d_mouth sad_Silentx05
                with dissolve

                p "Bien que me la has estado chupando ahora..."

                show gensex_69_L_d_mouth sad_Talkingx08
                with dissolve

                d "Porque no tenía más remedio,"

                show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                d "no porque realmente quisiera."

                show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

                p "Lo dices como si te hubiera obligado..."

                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                d "..."

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                p "¿Prefieres comérmela mientras estás de rodillas"

                show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

                p "y no mientras te estoy dando un repaso en la entrepierna?"

                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

                d "¡Prefiero que me folles y te dejes de hostias!"

                if DidacPregnant == False:

                    show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                    p "¡¿Acaso no entiendes el peligro de dejarte embarazada?!"

                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                    d "¡¿En serio tienes tan poco auto-control?!"

                    show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                    p "¡Los accidentes ocurren!"

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    d "Confío en ti."

                    show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                    call ped_D_NoSex 

                    p "..."

                    show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

                    p "Lo que pasa es que vas tan cachondo que eres incapaz de entender el peligro."

                    show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                    d "Tsskk..." 

                show gensex_69_L_d_mouth sad_Silentx05
                with dissolve   

        elif p_didac.blowjob_done_TRY == 2:

            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

            d "Como tu polla siga sobándome la cara como hasta ahora,"

            show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

            d "al final no te la voy a chupar;"

            show gensex_69_L_d_mouth sad_Talkingx11
            with vpunch

            d "¡Sino a morder!"

            show gensex_69_L_d_mouth sad_Talkingx08
            with dissolve

            d "¡Cambiemos de postura de una vez!"

            show gensex_69_L_d_mouth sad_Talkingx09
            with dissolve

            d "¡Y no!"

            show gensex_69_L_d_mouth sad_Talkingx10
            with dissolve

            d "No me refiero a que me pongas de rodillas;"

            show gensex_69_L_d_mouth sad_Talkingx11
            with dissolve

            d "¡Sino a cuatro patas!"

            if p_prot.action == "blowjob_done":

                show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

                p "¿No te gusta lo que te estoy haciendo?"

                if afternight04__MMouth_dick_Success > 0:

                    show gensex_69_L_d_mouth sadbiting_Silentx07
                    with dissolve

                    d "..."

                    show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                    d "¡Eso no cambia nada!"

                    show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                    p "Ya..."

                else:

                    show gensex_69_L_d_mouth sad_Talkingx09
                    with dissolve

                    d "¡Lo haces por que te da la gana!"

                    show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

                    p "..."
            else:

                show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

        elif p_didac.blowjob_done_TRY == 3:

            show gensex_69_L_d_mouth sad_Silentx08
            with dissolve

            d "..."

            show gensex_69_L_d_mouth sad_Talkingx05
            with dissolve

            d "Mira que eres pesado..."

            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

            d "¡Que no me la voy a meter en la boca por mucho que te empeñes!"

            show gensex_69_L_d_mouth sad_Silentx04
            with dissolve

            p "¿Estás segura?..."

            if afternight04__MMouth_dick_Success > 0:

                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                d "..."

                show gensex_69_L_d_mouth sad_Silentx05
                with dissolve

                d "Tssk..."

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            else:

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡¿A ti que te parece?!"

                show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        elif p_didac.blowjob_done_TRY >= 4:

            show gensex_69_L_d_mouth sad_Silentx06
            with dissolve

            d "..."

            if p_prot.action == "blowjob_done" and afternight04__MMouth_dick_Success > 0:

                show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                d "La madre que te parió..."

                $ p_didac_blowjob_done_ACCEPTED = True

                $ p_didac.action == "blowjob_done"
                $ p_prot.b_action == "blowjob_received"

                $ p_didac.blowjob_done += 1
                $ p_prot.blowjob_received += 1

                #$ ped_sex_general_69_cover = "over"
                $ ped_sex_general_expression_Cond = ""
                #$ ped_sex_general_action_Cond = "69_00_00"
                $ ped_sex_general_action_b_Cond = "69b_01_01"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Un ligero cosquilleo te recorre la entrepierna al sentir sus labios"

                n "acariciando tu miembro."

                pt "¿Será posible?..."
                
                n "Lentamente, sientes sus labios rodeando tu glande,"

                n "y la punta de su lengua, jugueteando con el frenillo."

                p "Hmm..."

                d "Tssk..."

                n "Casi sin darte tiempo a reaccionar,"

                n "sus manos se posan sobre tus nalgas a modo de palanca"

                n "para así conseguir meterse casi la mitad de tu falo"

                n "en el interior de su garganta."

                p "¡Ugh!..."

                n "Te parece sentir, más que escuchar,"

                n "una sorna gutural de victoria"

                n "a través del cosquilleo causado por sus labios y su garganta."

            else:

                $ ped_check_1_10("ped_69_oralTRY_FAILED_didac_list")
                #$ randomnum_1to10 = renpy.random.randint(1, 10)

                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

                if ped_check_list_result == 1:

                    d "Podemos estar así todo el día..."

                elif ped_check_list_result == 2:

                    d "¿Estás esperando a que llueva?"

                elif ped_check_list_result == 3:

                    d "Podemos pasarnos la noche así."

                elif ped_check_list_result == 4:

                    d "Estás perdiendo el tiempo."

                elif ped_check_list_result == 5:

                    d "Sabes que no me la voy a meter en la boca."

                elif ped_check_list_result == 6:

                    d "¿Por qué insistes?"

                elif ped_check_list_result == 7:

                    d "¿Acaso eres imbécil?"

                elif ped_check_list_result == 8:

                    d "Quita tu polla de mi cara de una vez."

                elif ped_check_list_result == 9:

                    d "Te voy a meter una hostia en los huevos,"

                    d "que tendrás que comprarte una gallina para reponerlos."

                elif ped_check_list_result == 10:

                    d "Te estás jugando una buena hostia..."

                else:

                    d "Mira que eres pesado..."

                show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

        
        call afternight05_Pedrera_Neus_Warning

        $ p_prot.b_action = "rest"

    elif p_prot.action in ["rest"] or p_prot.b_action in ["takeTongueOut", "takeDickOut"]:

        if p_prot.b_action in ["takeTongueOut", "takeDickOut"]:
            call p_didac_notReceiveBlowjob

        #$ p_prot.restTurns += 1 # How many sequential times you did nothing.
        # $ p_prot.pos_69_rest += 1 # How many times you did nothing in doggystyle in TOTAL.

        elif p_prot.pos_69_rest == 0:

            #$ p_prot.restTurns += 1 # How many sequential times you did nothing.

            if p_didac.start == 1:

                call afternight05_Pedrera_Sex_NakeYou

            else:

                n "Acariciándole el hombro, le indicas que se ponga cómoda sobre la cama."

                n "A pesar de los claros indicios de sospecha en su rostro, obedece."

                n "Una vez desnuda sobre la cama, haces lo propio y te incorporas encima de ella"

            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk
            show gensex_69_L_d_mouth sad_Silentx04
            with Dissolve(0.5)

            pause 0.2

            show gensex_69_L_d_mouth sad_Talkingx05
            with dissolve

            d "¿Qué-"

            extend "qué haces?"

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

            p "He pensado que sería más interesante si hacemos lo mismo a la vez."

            show gensex_69_L_d_mouth sad_Talkingx04
            with dissolve

            d "¡¿Qué?!"

            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

            d "¡¿LO MISMO?!"

            show gensex_69_L_d_mouth sad_Talkingx08
            with dissolve

            d "¡Tú no tienes coño!"

            show gensex_69_L_d_mouth sad_Talkingx09
            with dissolve

            d "¡No es lo mismo ni de coña!"

            if p_didac.blowjob_done > 0:

                show gensex_69_L_d_mouth sad_Talkingx08
                with dissolve

                d "¡¿Para eso me has hecho cambiar de postura?!"

                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

                d "¡¿Para que en lugar de chupártela de rodillas,"

                extend " lo haga estirada?!"

                show gensex_69_L_d_mouth sad_Talkingx09
                with dissolve

                d "¡Vaya puta gilipollez!"

            show gensex_69_L_d_mouth sad_Talkingx11
            with dissolve

            d "¡Lo que quiero es que me folles joder!"

            show gensex_69_L_d_mouth sad_Talkingx12
            with dissolve

            d "¡¿Tan difícil es entenderlo?!"

            show gensex_69_L_d_mouth sad_Silentx07
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with fade_short

            tx "No te quejes tanto."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            d "¡¿Euh?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Ya de por si es bastante sorprendente que no se limite a follarte la boca mientras te deja con las ganas."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Al menos así cabe la posibilidad de que llegues a correrte y todo."

            if DidacPregnant == True:

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                tx "Y sin ningún peligro de dejarte preñada."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx03
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            show gensex_69_L_d_mouth sad_Talkingx09
            with fade_short

            d "¡Lo que necesito para correrme es su polla!"

            show gensex_69_L_d_mouth sad_Talkingx10
            with dissolve

            d "¡No su lengua!"

            show gensex_69_L_d_mouth sad_Silentx09
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with fade_short

            ne "En realidad,"

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "puede conseguir {i}casi{/i} el mismo efecto."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "No tiene la misma intensidad..."

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "pero sigue conteniendo sus fluidos corporales."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx03
            with dissolve

            d "..."

            pause 0.2

            call pedrera_sex_p_general_talk
            show gensex_69_L_d_mouth sad_Silentx06
            with fade_short

            d "Tssk..."

            call pedrera_sex_p_general_talk
            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

            d "¡Si me quieres lamer el coño,"

            extend " hazlo!"

            show gensex_69_L_d_mouth sad_Talkingx09
            with dissolve

            d "¡Pero no pienso volver a meterme tu polla en la boca!"

            show gensex_69_L_d_mouth sad_Silentx06
            with dissolve

            tx "¿Estás segura de ello?"

            show gensex_69_L_d_mouth sadbiting_Silentx05
            with dissolve

            d "..."

        elif p_prot.pos_69_rest == 1:

            show gensex_69_L_d_mouth sad_Silentx04
            with dissolve

            d "..."

            show gensex_69_L_d_mouth sad_Talkingx05
            with dissolve

            d "¿Estás esperando algo?"

            show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

            d "Porque estás soñando si crees que yo lo voy a hacer."

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

            p "..."

        elif p_prot.pos_69_rest == 2:

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

            d "..."

            show gensex_69_L_d_mouth sad_Talkingx04
            with dissolve

            d "En serio..."

            show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

            d "¿Para qué te me has puesto encima,"

            show gensex_69_L_d_mouth sad_Talkingx05
            with dissolve

            d "si te vas a quedar sin hacer nada?"

            show gensex_69_L_d_mouth sad_Talkingx04
            with dissolve

            d "Y sabes que no me la voy a meter en la boca."

            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

            d "¿Qué puto sentido tiene esto?"

            if afternight04__MMouth_dick_Success > 0:

                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                d "Si al menos usaras la lengua,"

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                d "quizás,"

                extend " solo quizás,"

                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                d "podrías convencerme..."

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

        elif p_prot.pos_69_rest == 3:

            show gensex_69_L_d_mouth sad_Talkingx04
            with dissolve

            d "No pienso hacer nada."

            show gensex_69_L_d_mouth sad_Talkingx06
            with dissolve

            d "Por mi,"

            extend " como si estamos así hasta que salga el sol."

            show gensex_69_L_d_mouth sad_Silentx05
            with dissolve

        elif p_prot.pos_69_rest == 4:

            show gensex_69_L_d_mouth sad_Silentx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond =  "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx02
            with fade_short

            tx "Esto empieza a ser hasta ridículo..."

            if p_didac.cunnilingus_received == 0:

                show m_exp_mouth sad_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows angryx02
                with dissolve

                tx "¡Si no les vas a comer el coño,"

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx03
                with dissolve

                tx "al menos cambia de postura!"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Cuando he visto que te ponías de cara a su entrepierna,"

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "pensaba que actuarías de un modo distinto a lo que imaginaba,"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "pero no,"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            tx "eres tan imbécil como él."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            d "¡Oye!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx03
            with dissolve

            d "¿Y ahora por qué coño me insultas?"

            show m_exp_mouth sad_Talkingx002
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex002
            with dissolve

            tx "Por que sois tal para cual."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            pause 0.2

            call pedrera_sex_p_general_talk
            show gensex_69_L_d_mouth sad_Silentx06
            with fade_short

            d "Tssk..."

        elif p_prot.pos_69_rest == 5:

            show gensex_69_L_d_mouth sad_Talkingx04
            with dissolve

            if p_didac.blowjob_done > 0:

                d "No pienso volver a meterme tu polla mientras no hagas tú lo mismo con mi panocha."

            else:

                d "No pienso meterme tu polla en mi boca;"

                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

                d "¡y mucho menos si ni tan solo eres capaz de usar tu lengua en mi jodida panocha!"

            show gensex_69_L_d_mouth sadbiting_Silentx06
            with dissolve

            p "¿Tienes que llamarlo de esta manera?"

            show gensex_69_L_d_mouth sad_Talkingx09
            with dissolve

            d "¡La llamo como me sale de los huevos!"

            show gensex_69_L_d_mouth sadbiting_Silentx05
            with dissolve

            pt "Desde luego,"

            extend " sigue siendo el de siempre..."

        elif p_prot.pos_69_rest >= 6:

            $ ped_check_1_10("ped_69_rest_didac_list")
            #$ randomnum_1to10 = renpy.random.randint(1, 10)

            if ped_check_list_result in range(1,11):
                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

            if ped_check_list_result == 1:

                d "¡¿Te vas a quedar mucho rato ahí quieto mirándome el coño?!"

            elif ped_check_list_result == 2:

                d "Ya que estás en esta postura,"

                show gensex_69_L_d_mouth sad_Talkingx08
                with dissolve

                if p_didac.cunnilingus_received > 0:

                    d "¡Al menos podrías usar un poco más tu lengua!"

                else:

                    d "¡Al menos podrías usar un poco tu lengua!"

            elif ped_check_list_result == 3:

                d "¡Deja de mirarme tanto el coño y haz algo!"

            elif ped_check_list_result == 4:

                d "¿Estás esperando que se haga de día?"

            elif ped_check_list_result == 5:

                d "¡¿Tanto te mola mi coño que tienes que estar mirándolo..."

                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

                d "¡SIN HACER NADA!"

            elif ped_check_list_result == 6:

                d "¡Estás flipando si crees que voy a meterme tu polla en la boca."

                show gensex_69_L_d_mouth sad_Talkingx10
                with dissolve

                d "¡Si ni siquiera eres capaz de meter tu lengua en mi chumino!"

                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                pt "¿Tanto le cuesta llamarlo coño...?"

            elif ped_check_list_result == 7:

                if p_didac.cunnilingus_received == 0:

                    d "¿Tanto te cuesta usar tu lengua?"

                else:

                    d "¿Tanto te cuesta usar tu lengua de nuevo?"

            elif ped_check_list_result == 8:

                d "¿Te gusta estar encima sin hacer nada?"

            elif ped_check_list_result == 9:

                d "Podrías hacer algo más que quedarte mirando sin hacer nada..."

            elif ped_check_list_result == 10:

                d "Si de todos modos no vas a hacer nada,"

                d "¿no preferirías estar sentado?"

            else:

                show gensex_69_L_d_mouth sad_Silentx05
                with dissolve

                d "..."

            show gensex_69_L_d_mouth sadbiting_Silentx06
            with dissolve

            #call afternight05_Pedrera_Sex_NeusLastWarning
        
        call afternight05_Pedrera_Neus_Warning

    #elif p_didac.action == "blowjob_done": ## Didac can decide to suck your cock or not.


    elif p_prot.action == "cunnilingus_done" and p_prot.b_action not in ["takeTongueOut"]: # 69

        $ debug("MC Licking pussy")

        $ p_prot.cunnilingus_done += 1
        $ p_didac.cunnilingus_received += 1
        $ p_didac.cunnilingus_69_received += 1

        $ p_didac.vaginal_dilatation += 1

        $ ped_sex_general_69_cover = "over"
        #$ ped_sex_general_expression_Cond = ""

        call ped_sex_69_mc_lickpussy01

        #$ ped_sex_general_action_b_Cond = "69b_01_01"
        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

        pause 3.0/ped_sex_num

        ##

        #$ p_didac_cunnilingus_received_from_p_prot_at_69 += 1

        $ ped_check_1_10("ped_69_cunnilingus_moan_didac_list")
        #$ randomnum_1to10 = renpy.random.randint(1, 10)

        if ped_sex_general_expression_Cond == "talk":

            if ped_check_list_result in range(1,4):
                show gensex_69_L_d_mouth happybiting_Silentx05

            if ped_check_list_result not in range(1,11):
                show gensex_69_L_d_mouth happybiting_Silentx05

            elif ped_check_list_result == 4:
                show gensex_69_L_d_mouth sad_Talkingx005
                
            else:
                show gensex_69_L_d_mouth sad_Talkingx04

            with vpunch


        if ped_check_list_result == 1:

            d "Hhmm..."

        elif ped_check_list_result == 2:

            d "Hhmfm..."

        elif ped_check_list_result == 3:

            d "Mfhhmm..."

        elif ped_check_list_result == 4:

            d "Oufhm..."

        elif ped_check_list_result == 5:

            d "Aahmm..."

        elif ped_check_list_result == 6:

            d "Aa-ahhm..."

        elif ped_check_list_result == 7:

            d "Ahhfmm..."

        elif ped_check_list_result == 8:

            d "Fhmmm..."

        elif ped_check_list_result == 9:

            d "Ca..."

        elif ped_check_list_result == 10:

            d "Hmm..."

        else:

            d "Mmmm..."

        if ped_sex_general_expression_Cond == "talk":
            show gensex_69_L_d_mouth sadbiting_Silentx06
            with dissolve

        ##

        if p_didac_blowjob_done_ACCEPTED == True:

            $ p_prot.b_action = "blowjob_received"

            $ debug ("You receive Didac blowjob while you're licking her pussy (MOUTH FULL BOTH).")

            call p_didac_cunnilingus_received_label

        else:

            if p_didac.cunnilingus_69_received == 1:

                show gensex_69_L_d_mouth sadbiting_Silentx03
                with dissolve

                n "Agarrándote con firmeza a sus nalgas,"

                n "desciendes la cabeza para acercar tu mandíbula a sus labios menores."

                show gensex_69_L_d_mouth sadbiting_Silentx09
                with dissolve

                d "Ughh..."

                show gensex_69_L_d_mouth sadbiting_Silentx07
                with dissolve

                n "Con suavidad,"

                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                n "deslizas superficialmente tu lengua a lo largo y ancho de la tierna piel"

                n "que cubre su cálida entrepierna."

                show gensex_69_L_d_mouth sadbiting_Silentx08
                with dissolve

                n "Inevitablemente,"

                n "empiezas a saborear el cálido y ligeramente viscoso jugo vaginal que emana de su interior."

                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

                d "Por mucho que te empeñes,"

                show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                d "por mucho que te esfuerces con tu lengua,"

                show gensex_69_L_d_mouth sad_Talkingx05
                with dissolve

                d "no voy a metérmela en la..."

                $ ped_sex_general_69_cover = "over"
                $ ped_sex_general_action_Cond = "69_01_01"
                call pedrera_sex_p_general_talk
                with Dissolve(1.0)

                show gensex_69_L_d_mouth sadbiting_Silentx08
                with vpunch

                n "Con cierta celeridad, introduces tu lengua entre sus labios menores,"

                $ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_01_01"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sadbiting_Silentx07
                with Dissolve(0.5)

                n "acariciando cada tramo carnoso que rodea su interior mientras penetras su abertura vaginal."

                show gensex_69_L_d_mouth sadbiting_Silentx09
                with vpunch

                d "¡UHhmmg...!"

                show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

                tx "No parece que lo estés pasando tan mal..."

                show gensex_69_L_d_mouth sad_Talkingx06
                with dissolve

                d "Ca-"

                extend "cállate..."

                show gensex_69_L_d_mouth sadbiting_Silentx07
                with dissolve

            elif p_didac.cunnilingus_69_received == 2:

                $ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_01_02"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                d "¡Uhhmmg...!"

                show gensex_69_L_d_mouth sad_Talkingx05
                with dissolve

                d "Puto [protname],"

                extend " se nota que tienes práctica..."

                if not p_txell.seal == "sealed":

                    show gensex_69_L_d_mouth sadbiting_Silentx06
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows suspiciousx01
                    with fade_short

                    tx "Hmmm..."

                    show m_exp_mouth sad_Talkingx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Me pregunto si cuando le toque hacerlo conmigo,"

                    show m_exp_mouth sad_Talkingx002
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    tx "le pondrá el mismo empeño."

                    show m_exp_mouth sadbiting_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    pause 0.2

                if not p_txell.seal == "sealed":
                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab

                show gensex_69_L_d_mouth sadbiting_Silentx05

                if not p_txell.seal == "sealed":
                    with fade_short
                else:
                    with dissolve

            elif p_didac.cunnilingus_69_received == 3:

                $ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_01_03"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sadbiting_Silentx06
                with Dissolve(0.5)

                d "Hmmm..."

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                d "Reconozco que no se te da tan mal..."

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                d "Aún así..."

                show gensex_69_L_d_mouth happybiting_Silentx06
                with vpunch

                d "¡HHHMMMmm...!"

                if DidacPregnant == True:

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    d "Quiero volver a sentir tu polla dentro..."

                    show gensex_69_L_d_mouth sadbiting_Silentx05
                    with dissolve

                else:

                    $ Pedrera_char_Cond =  "TxellClose_b_show"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with fade_short

                    tx "Aún así,"

                    extend " si te folla el coño te puede dejar preñada."

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "Vas tan cachonda que te da igual,"

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "pero luego quizás te arrepientas."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "p_nobody"
                    call Pedrera_char_lab
                    with fade_short

                    d "Tssk..."

            elif p_didac.cunnilingus_69_received == 4:

                $ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_01_05"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sad_Talkingx03
                with Dissolve(0.5)

                d "Mierda..."

                #$ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_02_01"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sad_Talkingx03
                with Dissolve(0.5)

                d "Aaa-"

                extend "aaaahhmmm..."

                show gensex_69_L_d_mouth sadbiting_Silentx07
                with dissolve

                n "Con cierta habilidad, penetras su interior con tu lengua,"

                show gensex_69_L_d_mouth sadbiting_Silentx09
                with dissolve

                n "deslizándola suavemente en su ardiente interior."

                if afternight04__MMouth_dick_Success > 0:

                    # if afternight04__MMouth_dick_Deep_Success > 0: # Necessary?

                    show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                    d "¡A tomar por el culo!"

                    $ p_didac_blowjob_done_ACCEPTED = True

                    $ p_didac.action = "blowjob_done"
                    $ p_prot.b_action = "blowjob_received"

                    $ p_didac.blowjob_done += 1
                    $ p_prot.blowjob_received += 1
                    $ p_didac.throat_dilatation += 1

                    #$ ped_sex_general_69_cover = "over"
                    $ ped_sex_general_expression_Cond = ""
                    #$ ped_sex_general_action_Cond = "69_00_00"
                    $ ped_sex_general_action_b_Cond = "69b_01_01"
                    call pedrera_sex_p_general_talk
                    with Dissolve(1.5)

                    n "Sin demasiada demora, sientes el agarrón de su mano a tu miembro que empuja tus caderas hacia abajo."

                    n "Sus cálidos labios envuelven tu hinchado y rosado glande,"

                    n "al mismo tiempo que sientes su lengua juguetear con esa parte tan sensible."

                    $ ped_sex_general_69_cover = "off"
                    $ ped_sex_general_action_b_Cond = "69b_02_01"
                    call pedrera_sex_p_general_talk
                    with Dissolve(1.5)

                    n "poco a poco se va deslizando hasta llegar casi a la mitad de tu miembro en erección."

                    tx "Suerte que habías dicho que no se la querías volver a chupar..."

                    d "¡Caahlagthe!"

            elif p_didac.cunnilingus_69_received >= 5:

                call p_didac_cunnilingus_received_label

        if p_didac_blowjob_done_ACCEPTED == False:

            # $ p_prot.restTurns += 1

            call afternight05_Pedrera_Neus_Warning

    return



############################################################################
############################################################################

############################################################################
############################################################################

label afternight05_Pedrera_Sex_p_didac_common:

    if p_didac.action == "rest":

        if (p_prot.pos == "missionary" and p_prot.pos_missionary_rest == 1) or (p_prot.pos == "doggy" and pos_doggy_rest == 1):

        #if (p_prot.pos_missionary_rest or p_prot.pos_doggy_rest) == 1:

            $ debug ("DIDAC COMMON 1.")

            d "¡Métemela de una vez!"

            p "¿No preferirías un poco de preliminares antes?"

            d "¡¿Más preliminares?!"

            d "¡Estoy hasta los cojones de los preliminares!"

            d "¡Fóllame de una vez!"

            call ped_D_NoSex ##########################################

        else:

            $ debug("Needs a description of how you take your clothes off.")

            aj "IS IT READABLE? 8668"

    return

label p_didac_insulting:

    $ ped_check_1_10("ped_insulting_didac_list")
    #$ randomnum_1to10 = renpy.random.randint(1, 10)


    if ped_check_list_result == 1:

        d "¡COÑO!"

    elif ped_check_list_result == 2:

        d "¡HOSTIAS!"

    elif ped_check_list_result == 3:

        d "¡JODER!"

    elif ped_check_list_result == 4:

        d "¡ME CAGO EN TUS MUERTOS!"

    elif ped_check_list_result == 5:

        d "¡ME CAGO EN LOS CLAVOS DE LAS TUMBAS DE TUS MUERTOS!"

    elif ped_check_list_result == 6:

        d "¡COJONES!"

    elif ped_check_list_result == 7:

        d "¡SUBNORMAL!"

    elif ped_check_list_result == 8:

        d "¡GILIPOLLAS!"

    elif ped_check_list_result == 8:

        d "¡LA HOSTIA!"

    elif ped_check_list_result == 8:

        d "¡IMBÉCIL!"

    return

label p_didac_insulting_02:

    $ ped_check_1_10("ped_insulting_02_didac_list")

    if ped_check_list_result == 1:

        d "¡SABATOT!"

    elif ped_check_list_result == 2:

        d "¡GAMARÚS!"

    elif ped_check_list_result == 3:

        d "¡CAPSIGRANY!"

    elif ped_check_list_result == 4:

        d "¡TORRACULLONS!"

    elif ped_check_list_result == 5:

        d "¡MITJA MERDA!"

    elif ped_check_list_result == 6:

        d "¡CAP DE PREPUCI!"

    elif ped_check_list_result == 7:

        d "¡TAP DE BASSA!"

    elif ped_check_list_result == 8:

        d "¡CURT DE GAMBALS!"

    elif ped_check_list_result == 9:

        d "¡DESVIRGA-GALLINES!"

    elif ped_check_list_result == 10:

        d "¡MITJA MERDA!"

    else:

        d "¡TROS DE QÜONIAM!"

    return

#####

label onlyWantNeus_with_p_didac:

    d "..."

    ne "¿Euh...?"

    ne "[protname]..."

    ne "¿E-"

    extend "estás seguro?..."

    p "Es lo que he dicho,"

    extend " ¿No?"

    d "¡¿En serio?!"

    d "¡¿Qué clase de gilipollez es esta?!"

    tx "Una llamada respeto y amor,"

    tx "algo que quizás no está ni en tu vocabulario."

    d "..."

    return


label p_didac_cunnilingus_received_label:

    if p_prot.b_action == "blowjob_received":

        call p_prot_oral_received_moans_label

    $ ped_check_1_10("ped_cunnlingus_received_01_didac_list")
    #$ randomnum_1to10 = renpy.random.randint(1, 10)

    if ped_check_list_result == 1:

        d "No pares hijo de puta..."

    elif ped_check_list_result == 2:

        d "Se te da mejor de lo que imaginaba..."

    elif ped_check_list_result == 3:

        d "A este paso no echaré de menos mi polla, joder..."

    elif ped_check_list_result == 4:

        d "No me extraña que quieran repetir contigo esas zorras..."

    elif ped_check_list_result == 5:

        d "Aunque prefiero tu polla,"

        extend " la verdad es que no se te da nada mal..."

    elif ped_check_list_result == 6:

        d "Que mamonazo eres..."

        d "¡Me encanta!"

    elif ped_check_list_result == 7:

        if p_didac.orgasm == 0:

            d "Si sigues así,"

            extend " al final voy a correrme..."

        else:

            d "Al final conseguirás que tenga otro orgasmo..."

    elif ped_check_list_result == 8:

        d "Por mi puedes follarte a Neus"

        extend " o a la rubia esta,"

        d "pero no quites tu lengua de aquí..."

    elif ped_check_list_result == 9:

        d "La lengua que tienes,"

        extend " hijo de puta..."

    elif ped_check_list_result == 10:

        d "¡¿Quien coño te enseñó a lamer tan bien un jodido chumino?!"

    else:

        d "¡Jodeeer...!"

    ####

    if p_prot.b_action == "blowjob_received":

        $ ped_check_1_10("ped_cunnlingus_received_blowjobRecieved_didac_list")
        #$ randomnum_1to10 = renpy.random.randint(1, 10)

        if ped_check_list_result == 1:

            pt "No se le da tan mal..."

        elif ped_check_list_result == 2:

            pt "Supongo que con el tiempo mejorará."

        elif ped_check_list_result == 3:

            pt "Para ser primeriza, no se le da tan mal..."

        elif ped_check_list_result == 4:

            pt "Supongo que el haber tenido polla, habrá ayudado a saber cómo chuparla mejor..."

        elif ped_check_list_result == 5:

            pt "Si la chupa así ahora, en un futuro..."

        elif ped_check_list_result == 6:

            if DidacPregnant == True:

                pt "A veces me pregunto si no he sido yo quien le ha empujado desde un principio a quedarse como mujer para siempre..."

            else:

                pt "A veces me pregunto si es buena idea que vuelva a ser hombre..."

        elif ped_check_list_result == 7:

            pt "Si sigue así, no creo que tarde mucho en correrme."

        elif ped_check_list_result == 8:

            pt "Casi prefiero su boca que su coño..."

        elif ped_check_list_result == 9:

            pt "Tiene un buen juego de lengua, eso no se puede negar..."

        elif ped_check_list_result == 10:

            pt "¿Soy yo?, ¿o me ha hecho un mordisquito?"

        else:

            pt "Mamona..."

    return



label ped_D_NoSex:

    if DidacPregnant == False:

        $ ped_D_NoSex_times += 1

        if ped_D_NoSex_times == 1:

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx01
            with fade_short

            ne "Ni se te ocurra."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_iris front03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "Podrías dejarla embarazada,"

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_iris front01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "y eso no lo voy a permitir."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            $ ped_sex_general_zoom_Cond = "face"
            $ ped_sex_general_expression_Cond = "talk"
            call pedrera_sex_p_general_talk

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils right03
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth sad_Talkingx18
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx08
            with fade_short

            d "¡No seas aguafiestas!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils right02
                show gensex_missionary_d_head_exp_eyebrows angryx02
                show gensex_missionary_d_head_exp_mouth sad_Talkingx19
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡La sacará a tiempo,"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth sad_Talkingx17
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx08
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "no es tan imbécil!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                show gensex_missionary_d_head_exp_mouth sad_Talkingx11
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx006
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡¿Verdad que no?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils front01
                show gensex_missionary_d_head_exp_eyebrows suspiciousx01
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris front01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx01
            with fade_short

            ne "Es demasiado arriesgado."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            $ ped_sex_general_zoom_Cond = "face"
            call pedrera_sex_p_general_talk

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows angryx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx20
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx17
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx09
            with fade_short

            d "¡Arriesgado, mis cojones!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils right02
                show gensex_missionary_d_head_exp_eyebrows angryx05
                show gensex_missionary_d_head_exp_mouth sad_Talkingx22
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx07
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡Fuiste tú quien me convirtió en mujer!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils right01
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx23
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx08
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve


            d "¡¿Y ahora me vas a quitar el placer de sentir su polla?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx25
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx11
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡¿Qué clase de sádica eres?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils right05
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Silentx15
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx09
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            ne "..."

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with fade_short

            tx "Dídac."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Dirás lo que quieras,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            tx "pero sabes que tiene razón."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            tx "Si termina corriéndose dentro de ti,"

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx02
            with dissolve

            tx "nunca más volverás a ser hombre."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 08
                show gensex_missionary_d_head_exp_pupils front08
                show gensex_missionary_d_head_exp_eyebrows suspiciousx04
                show gensex_missionary_d_head_exp_mouth sad_Silentx15
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx08
            with fade_short

            d "..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils left01
                show gensex_missionary_d_head_exp_eyebrows angryx04
                show gensex_missionary_d_head_exp_mouth sad_Talkingx21
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris left01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx11
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡¿Y qué?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth sad_Talkingx005
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx10
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡Tampoco sería el fin del mundo!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils left05
                show gensex_missionary_d_head_exp_eyebrows angryx02
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx09
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 00
            show m_exp_piris front00
            show m_exp_eyebrows surprisex02
            with fade_short

            tx "..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Lo estás diciendo en serio?"

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils right01
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth sad_Talkingx12
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx15
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx07
            with fade_short

            d "¡Puede!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx02
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx09
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx07
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils right02
                show gensex_missionary_d_head_exp_eyebrows surprisex01
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx03
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris right02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            ne "Quien habla aquí no es tu razón,"

            extend " sino tu enfermizo deseo,"

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx02
            with fade_short

            ne "sé lo que sientes,"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "y te prometo que a partir de mañana irá desapareciendo,"

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "poco a poco."

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_iris front00
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_eyebrows surprisex02
            with dissolve

            d "¡¿Y si no quiero que desaparezca?!"

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Entonces no me dejarás otra alternativa que forzarte a ello."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils right01
                show gensex_missionary_d_head_exp_eyebrows surprisex01
                show gensex_missionary_d_head_exp_mouth happy_Talkingx15
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_mouth happy_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx004
            with fade_short

            d "¡¿Tú?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils right03
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth happy_Talkingx17
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth happy_Talkingx11
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx09
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡¿Y cómo piensas obligarme?!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                show gensex_missionary_d_head_exp_mouth happy_Silentx12
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth happy_Silentx12
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx08
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx04
            with fade_short

            ne "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front00_bright
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with Dissolve(0.5)

            d "..."

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 00
                show gensex_missionary_d_head_exp_pupils right00
                show gensex_missionary_d_head_exp_eyebrows surprisex02
                show gensex_missionary_d_head_exp_mouth sad_Silentx12
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 00
                show gensex_oral_d_frontHead_exp_iris right00
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx12
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx002
            with fade_short

            d "Euhh..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils down01
                show gensex_missionary_d_head_exp_eyebrows sadx02
                show gensex_missionary_d_head_exp_mouth sad_Silentx15
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris down01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx10
                show gensex_oral_d_frontHead_exp_eyebrows sadx02
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx10
            with vpunch

            d "{size=60}¡Uhh...!{/size}"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 07
                show gensex_missionary_d_head_exp_pupils front07
                show gensex_missionary_d_head_exp_eyebrows sadx05
                show gensex_missionary_d_head_exp_mouth sad_Silentx19
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 07
                show gensex_oral_d_frontHead_exp_iris front07
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx13
                show gensex_oral_d_frontHead_exp_eyebrows sadx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx08
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows sadx01
            with fade_short

            tx "Creo que ha entendido el mensaje."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_iris front05_bright
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx03
            with fade_short

            ne "¿Tú crees?"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 06
                show gensex_missionary_d_head_exp_pupils front06
                show gensex_missionary_d_head_exp_eyebrows angryx05
                show gensex_missionary_d_head_exp_mouth sad_Talkingx18
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 06
                show gensex_oral_d_frontHead_exp_iris front06
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx16
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx10
            with vpunch

            d "¡Joder!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils right03
                show gensex_missionary_d_head_exp_eyebrows angryx06
                show gensex_missionary_d_head_exp_mouth sad_Talkingx22
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris right03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx12
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "¡Casi me quedo sin aire!"

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx05
                show gensex_missionary_d_head_exp_mouth sad_Silentx15
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with fade_short

            tx "Yo de ti no jugaría con ella,"

            extend " Dídac..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 01
                show gensex_missionary_d_head_exp_pupils right01
                show gensex_missionary_d_head_exp_eyebrows serious
                show gensex_missionary_d_head_exp_mouth sad_Silentx04
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 01
                show gensex_oral_d_frontHead_exp_iris right01
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows serious
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx05
            with fade_short

            d "..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils left05
                show gensex_missionary_d_head_exp_eyebrows sadx04
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx04
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx01
            with fade_short

            ne "[protname]."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_iris front03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "Ni se te ocurra volvérsela a meter ahí."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx09
            show neus_exp_iris front01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "¡¿Me has oído?!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            p "Sí,"

            extend " sí..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "Fui yo quien lo convirtió en mujer,"

            extend " es verdad."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_iris right04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Pero no permitiré que cometa este error."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_iris front03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "No mientras yo esté aquí."

            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_iris front08
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils left05
                show gensex_missionary_d_head_exp_eyebrows sadx03
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx06
            with fade_short

        elif ped_D_NoSex_times == 2:

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_iris front02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx03
            with fade_short

            ne "¡¿Es que no me has entendido?!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 04
                show gensex_missionary_d_head_exp_pupils right04
                show gensex_missionary_d_head_exp_eyebrows angryx01
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx05
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 04
                show gensex_oral_d_frontHead_exp_iris right04
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx01
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx05
            with fade_short

            d "..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 03
                show gensex_missionary_d_head_exp_pupils left03
                show gensex_missionary_d_head_exp_eyebrows angryx03
                show gensex_missionary_d_head_exp_mouth sad_Silentx09
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris left03
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx04
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

            d "Tssk..."

            if p_prot.pos == "missionary" and p_didac.action != "cunnilingus_done_p_txell":
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils left05
                show gensex_missionary_d_head_exp_eyebrows sadx03
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
            elif p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris left05
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
            elif p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx06
            if not (p_prot.pos == "missionary" and p_didac.action == "cunnilingus_done_p_txell") or p_prot.pos == "doggy":
                with dissolve

        elif ped_D_NoSex_times >= 3:

            $ ped_check_1_10("ped_D_NoSex_didac_list")
            #$ randomnum_1to10 = renpy.random.randint(1, 10)

            $ Pedrera_char_Cond = "NeusClose_show"
            call Pedrera_char_lab

            if ped_check_list_result in range(1,6):
                show neus_exp_mouth sad_Talkingx08
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx03

            elif ped_check_list_result in range(6,11):
                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03

            else:
                show neus_exp_mouth sad_Silentx04
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows angryx01

            $ debug ("ped_check_list_result = [ped_check_list_result]")

            with fade_short

            if ped_check_list_result == 1:

                ne "¡¿Es que hablo chino?!"

            elif ped_check_list_result == 2:

                ne "Eso no va a pasar mientras yo esté aquí."

            elif ped_check_list_result == 3:

                ne "¡¿Es que no lo entiendes?!"

            elif ped_check_list_result == 4:

                ne "Sabes muy bien que no."

            elif ped_check_list_result == 5:

                ne "No me lo pongas más difícil..."

            elif ped_check_list_result == 6:

                ne "Sabes que eso no va a ocurrir."

            elif ped_check_list_result == 7:

                ne "No insistas otra vez..."

            elif ped_check_list_result == 8:

                ne "Eso es algo que no va ocurrir."

            elif ped_check_list_result == 9:

                ne "No insistas,"

                extend " por favor..."

            elif ped_check_list_result == 10:

                ne "¿No lo entiendes...?"

            else:

                ne "..."

            
            show neus_exp_mouth sad_Silentx05
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows serious
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

    return

label p_didac_insult_blockedmouth:

    $ ped_check_1_10("ped_insult_blockedmouth_didac_list")
    #$ randomnum_1to10 = renpy.random.randint(1, 10)

    if ped_check_list_result == 1:

        d "¡Gue te fogllen!"

    elif ped_check_list_result == 2:

        d "¡Gue te den pog el gulo!"

    elif ped_check_list_result == 3:

        d "¡Gallate!"

    elif ped_check_list_result == 4:

        d "¡Me impogta una miegda!"

    elif ped_check_list_result == 5:

        d "¡Gue te den!"

    elif ped_check_list_result == 6:

        d "¡Segá tu opginion!"

    elif ped_check_list_result == 7:

        d "¡A veg si te voy a mogder!"

    elif ped_check_list_result == 8:

        d "¡Miga que pagro, eh!"

    elif ped_check_list_result == 9:

        d "¡La magde que te pagio!"

    elif ped_check_list_result == 10:

        d "¡Eges imbécil!"

    else:

        d "¡Gapullo!"

    return


label p_didac_notReceiveBlowjob:

    if p_prot.pos == "oral":

        $ ped_sex_general_expression_Cond = "talk"
        $ ped_sex_general_action_Cond = "o00_00"
        call pedrera_sex_p_general_talk

    # elif p_prot.pos == "69" and p_prot.action not in ["takeTongueOut"]:

    #     if ped_sex_general_action_Cond != "69_00_00":

    #         $ ped_sex_general_69_cover = "over"
    #         $ ped_sex_general_expression_Cond = "talk"
    #         $ ped_sex_general_action_Cond = "69_00_00"
    #         $ ped_sex_general_action_b_Cond = "69b_00_00"
    #         call pedrera_sex_p_general_talk


    if p_prot.pos == "69" and p_didac.action in ["blowjob_done", "blowjobDeep_done"] and p_prot.action == "takeTongueOut": # takeTongueOut

        $ ped_sex_general_69_cover = "over"
        $ ped_sex_general_expression_Cond = "talk"
        $ ped_sex_general_action_Cond = "69_00_00"
        #$ ped_sex_general_action_b_Cond = "69b_00_00"
        call pedrera_sex_p_general_talk

        $ p_prot.action = "rest" # Not really necessary this one.
        $ p_prot.b_action = "rest"
        $ p_didac.action = "rest"
        $ p_didac.b_action = "rest"

        # if p_prot.pos == "oral": # Not necessary
        #     show gensex_oral_d_frontHead_exp_eyes 08
        #     show gensex_oral_d_frontHead_exp_iris front08
        #     show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
        #     show gensex_oral_d_frontHead_exp_eyebrows angryx04
        show gensex_69_L_d_mouth sad_Silentx03
        with vpunch

        n "Rápidamente saca tu polla de su boca."

        show gensex_69_L_d_mouth sad_Talkingx02
        with dissolve

        d "Estás flipando si crees que me la voy a meter en la boca"

        show gensex_69_L_d_mouth sad_Talkingx002
        with dissolve

        d "sin que tú metas al menos la lengua ahí."

        show gensex_69_L_d_mouth sad_Silentx02
        with dissolve

        p "..."

    elif p_prot.action == "takeDickOut" or p_prot.b_action == "takeDickOut":

        $ debug("You take off your dick from her Mouth.")

        $ takeDickOut_Cond += 2
        $ takeDickOut_d_Total += 1

        if p_prot.pos == "oral":
            $ ped_sex_general_expression_Cond = "talk"
            if p_didac.action == "titwank_done":
                $ ped_sex_general_action_Cond = "ob00_00"
            else:
                $ ped_sex_general_action_Cond = "o00_00"
            call pedrera_sex_p_general_talk

            show gensex_oral_d_frontHead_exp_eyes 02
            show gensex_oral_d_frontHead_exp_iris down02
            show gensex_oral_d_frontHead_exp_mouth sad_Talkingx02
            show gensex_oral_d_frontHead_exp_eyebrows surprisex02

        elif p_prot.pos == "69":
            #$ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            #$ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk
            show gensex_69_L_d_mouth sad_Talkingx01

        with Dissolve(0.5)

        $ randomnum_1to5 = renpy.random.randint(1, 5)

        if randomnum_1to5 == 1:

            d "¿Uh?"

        elif randomnum_1to5 == 2:

            d "¿Euh?"

        elif randomnum_1to5 == 3:

            d "¿Uhmm?"

        elif randomnum_1to5 == 4:

            d "¿Qué?"

        elif randomnum_1to5 == 5:

            d "¿Que coño...?"

        if takeDickOut_d_Total == 1:

            # NOT FINISHED, it's not TXELL it must be DIDAC.

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 03
                show gensex_oral_d_frontHead_exp_iris front03
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx03
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

            d "¿Ahora decides sacarla?"  

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris front05
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

            if p_prot.pos == "69":
                d "¡¿Para qué coño te me has puesto encima si no es eso lo que querías?!"

            else:
                d "¿Para qué coño me la ha puesto en la boca entonces?"

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            p "No quiero terminar en tu boca aún..."

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve
            else:
                show gensex_69_L_d_mouth sadbiting_Silentx03
                with dissolve

            d "..."

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 05
                show gensex_oral_d_frontHead_exp_iris right05
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve

        elif takeDickOut_d_Total == 2:

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 02
                show gensex_oral_d_frontHead_exp_iris front02
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

            d "¡¿Otra puta vez?!"

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx08
                show gensex_oral_d_frontHead_exp_eyebrows angryx05
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

        if takeDickOut_d_Total > 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 in [1, 2]:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

                d "Tssk..."

            elif randomnum_1to5 in [3, 4]:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris front03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                d "¿Te estás cachondeando de mi...?"

            elif randomnum_1to5 == 5:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx05
                    with dissolve

                d "..."

            $ ped_check_1_10("ped_takeDickOut_didac_list")

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if ped_check_list_result == 1:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris front02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx07
                    with dissolve

                d "Eres bastante imbécil..."

            elif ped_check_list_result == 2:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 02
                    show gensex_oral_d_frontHead_exp_iris right02
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                d "Tú mismo..."

            elif ped_check_list_result == 3:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 03
                    show gensex_oral_d_frontHead_exp_iris rigth03
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx005
                    with dissolve

                d "Luego te vas quejando..."

            elif ped_check_list_result == 4:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx11
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                d "¡¿Te crees que soy tu puta muñeca?!"

            elif ped_check_list_result == 5:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                d "Al final te romperé las pelotas."

            elif ped_check_list_result == 6:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx12
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx10
                    with dissolve

                d "¡¿Acaso crees que soy una puta a sueldo?!"

            elif ped_check_list_result == 7:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                d "No seré yo quien se la vuelva a poner en la boca, imbécil."

            elif ped_check_list_result == 8:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 05
                    show gensex_oral_d_frontHead_exp_iris front05
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                d "No sabes ni lo que coño quieres."

            elif ped_check_list_result == 9:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 08
                    show gensex_oral_d_frontHead_exp_iris front08
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                    show gensex_oral_d_frontHead_exp_eyebrows angryx05
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx07
                    with dissolve

                d "Si no me la quieres meter en la boca,"

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                    show gensex_oral_d_frontHead_exp_eyebrows angryx07
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                d "de puta madre."

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 01
                    show gensex_oral_d_frontHead_exp_iris front01
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx09
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx08
                    with dissolve

                d "Sabes de sobra dónde prefiero que me la metas."

            elif ped_check_list_result == 10:

                if p_prot.pos == "oral":
                    show gensex_oral_d_frontHead_exp_eyes 04
                    show gensex_oral_d_frontHead_exp_iris front04
                    show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_d_frontHead_exp_eyebrows angryx06
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve

                d "Pareces un retrasado."

            else:

                pass

            if p_prot.pos == "oral":
                show gensex_oral_d_frontHead_exp_eyes 08
                show gensex_oral_d_frontHead_exp_iris front08
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx06
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx07
                with dissolve

    else:

        aj "takeDickOut or notReceivedBlowjob? ERROR 4878656"

    $ p_prot.action = "rest" # Not really necessary this one.
    $ p_prot.b_action = "rest"
    $ p_didac.action = "rest"
    $ p_didac.b_action = "rest"

    return


label p_prot_previousSex:

    if p_prot.action in ["vaginal_done_TRY", "vaginal_done", "vaginalDeep_done", "vaginalDeep_done_TRY", "anal_done", "anal_done_TRY", "analDeep_done", "anal_Deep_doneTRY", "blowjob_received", "blowjob_received_TRY", "blowjobDeep_received", "blowjobDeep_received_TRY", "titwank,received", "titwank_received_TRY", "masturbate"] or p_prot.b_action in ["blowjob_received", "blowjob_received_TRY", "blowjobDeep_received", "blowjobDeep_received_TRY"]:

        $ debug ("Your working with your dick.")

        if p_prot.restTurns > 2:
            $ p_prot.restTurns -= 1

    return