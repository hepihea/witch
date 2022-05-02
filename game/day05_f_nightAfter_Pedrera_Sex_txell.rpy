
# default p_txell_cunnilingus_done_to_p_txell = 0


# default p_txell_cunnilingus_received_from_p_txell_at_missionary_TRY = False
# default p_txell_cunnilingus_received_from_p_txell_at_missionary = 0

# default p_txell_anilingus_done_to_p_txell = 0 # "Protagonista haciéndole un anilingus a Meritxell."

# default p_txell_buttocks_pain_received_from_p_prot = 0

# default p_prot_blowjobDeep_received_TRY_withDidac = 0

# default p_prot_kiss_p_txell_FAIL = 0

#default p_prot_masturbate_infrontof_txell_ONLYNEUS_Cond = False # You said you would be Faithful to Neus.

# default p_prot_anal_fingered_received_from_p_txell = 0

#default p_txell_cunnilingus_received_from_p_prot_at_69 = 0

default p_txell_blowjobDeep_done_ACCEPTED = False
default p_txell_blowjob_done_ACCEPTED = False
default p_txell_titwank_ACCEPTED = False

default p_txell_doggy_TRY = 0
default p_txell_missionary_TRY = 0

default p_txell_blowjobDeep_done_kneels = 0

default ped_sheTakesDickOut_txell = 0

#default p_txell.titwank_TRY = 0

label afternight05_Pedrera_Sex_p_txell_oral:

    $ ped_sex_general_expression_Cond = "talk"
    call pedrera_sex_p_general_talk

    $ debug ("Oral Sex with Txell.")

    if p_prot.action == "masturbate":

        $ debug ("Protagonist masturbate")

        $ p_prot.masturbate += 1

        if p_prot.masturbate == 1:

            show gensex_oral_m_frontHead_exp_eyes 02
            show gensex_oral_m_frontHead_exp_iris down02
            show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
            with dissolve

            n "Acaricias tu erecto miembro con tu mano a escasos centímetros del rostro de Meritxell."

            if p_prot_NotJustMasturbate_with_p_txell or p_prot_NotJustMasturbate_with_p_didac:

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                with dissolve

                tx "¿Ahora te masturbas?"

                if p_txell.blowjobDeep_done > 0:

                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                    tx "¿Después de haberla tenido entera dentro de mi esófago?"

                elif p_txell.blowjob_done > 0:

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "¿Después de habérmela metido en la boca?"

                elif p_txell.blowjob_done_TRY > 0:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "Después de haber querido metérmela en la boca?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                elif p_prot_NotJustMasturbate_with_p_didac:

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    tx "¿Después de lo que has llegado a hacer con Dídac?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                    tx "¿Y ahora conmigo vas de puritano?"

                    show gensex_oral_m_frontHead_exp_eyes 00
                    show gensex_oral_m_frontHead_exp_iris front00
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "¿No has pensado que quizás no me interesas tanto como Dídac?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris right04
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    tx "Gente con mal gusto hay en todos lados..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris right05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                else:

                    if p_txell_NoSex_Confirmed:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Después de intentar follarme,"

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows serious
                        with dissolve

                        tx "cuando sabes que no tengo ningún interés en ti..."

                    if p_txell.vaginal_received_TRY > 0:

                        if p_txell.vaginalDeep_received_TRY > 0:

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                            show gensex_oral_m_frontHead_exp_eyebrows angryx01
                            with dissolve

                            if p_txell.vaginalDeep_received > 0:

                                tx "Después de habérmela metido hasta el fondo..."

                            else:

                                tx "Después de haber intentado metérmela hasta el fondo..."

                        else:

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            if p_txell.vaginal_received > 0:

                                tx "Después de haber tenido sexo sin condón conmigo..."

                            else:

                                tx "Después de haber intentado hacerlo conmigo..."

                    elif p_txell.anal_received_TRY > 0:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        if p_txell.analDeep_received_TRY > 0:

                            if p_txell.analDeep_received > 0:

                                tx "Después de habérmela metido hasta el fondo por detrás..."

                            else:

                                tx "Después de haber intentado metérmela hasta el fondo por detrás..."

                        else:

                            if p_txell.anal_received > 0:

                                tx "Después de habérmela metido por detrás..."

                            else:

                                tx "Después de haber intentado metérmela por detrás..."

                    elif p_txell.blowjob_done_TRY > 0:

                        show gensex_oral_m_frontHead_exp_eyes 03
                        show gensex_oral_m_frontHead_exp_iris front03
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                        with dissolve
                
                        if p_txell.blowjobDeep_received_TRY > 0:

                            if p_txell.blowjobDeep_received_:

                                tx "Después de haber penetrado mi garganta con tu pollón..."

                        else:

                            if p_txell.blowjob_done > 0:

                                tx "Después de haber sentido mi lengua en tu pollón..."

                            else:

                                tx "Después de haber intentado meterme tu pollón en mi boca..."


                    elif p_txell.titwank_received_TRY > 0:

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows serious
                        with dissolve

                        if p_txell.titwank_received > 0:

                            tx "Después de haberte masturbado este pollón tuyo con mis pechos..."

                        else:

                            tx "Después de intentar que te masturbe con mis hermosos pechos..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    tx "Por lo menos ahora lo entiendes."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris left04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    with dissolve

                    tx "Aunque dudo que Neus esté contenta..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris left05
                    show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    with dissolve

                if p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                    tx "Desde luego lo que le dijiste a Neus de que solo te interesaba hacerlo con ella,"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    tx "ha sido una mentira de las gordas..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    tx "Pero viniendo de un hombre como tú,"

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "tampoco debería sorprenderle..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    pt "¡¿Un hombre como yo?!"

                    pt "¡¿A qué coño se refiere esta furcia?!"

            else:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                tx "Hmm..."

                if p_prot.restTurns > 1:

                    if p_prot.restTurns > 3:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows angryx01
                        with dissolve

                        tx "Lo que te ha costado..."

                    else:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "Te ha costado tiempo..."

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "pero al final parece que lo has conseguido entender."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                else:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "Intentando ser fiel a Neus,"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "eso no me lo esperaba de ti."

                if afternight05_Pedrera_Sex_SaidJustWithNeus:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris right05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "Quizás sí es verdad que quieres hacerlo solo con ella..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                else:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "¿Acaso será lo único que harás conmigo?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                    with dissolve

                    menu:

                        "Es posible, ya veremos.":
                            call p_Help

                            $pl.ch_pts("np",-1)

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Hmmm..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                            with dissolve

                            tx "Algo así me imaginaba..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                            with dissolve

                        "Como ya le he dicho a Dídac antes, esta noche solo quiero hacerlo con Neus." if p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond == True and p_prot.vaginal_done == 0 and p_prot.anal_done == 0:

                            $ p_prot_masturbate_infrontof_txell_ONLYNEUS_Cond = True

                            $pl.ch_pts("dp",1)
                            $pl.ch_pts("np",3)
                            $pl.ch_pts("mp",1)

                            show gensex_oral_m_frontHead_exp_eyes 02
                            show gensex_oral_m_frontHead_exp_iris front02
                            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris right01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            d "Pse..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris right04
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows serious
                            with dissolve

                            d "¿Te pensabas que no te rechazaría a ti también?"

                            call onlyWantNeus_with_p_txell

                        "Sí, esta noche solo quiero hacerlo con Neus." if p_prot_masturbate_infrontof_didac_ONLYNEUS_Cond == False and p_prot.vaginal_done == 0 and p_prot.anal_done == 0:
                            call p_Help

                            $ p_prot_masturbate_infrontof_txell_ONLYNEUS_Cond = True

                            $pl.ch_pts("np",3)
                            $pl.ch_pts("mp",1)

                            call onlyWantNeus_with_p_txell


        elif p_prot.masturbate > 1:

            $ ped_check_1_10("ped_masturbate_txell_list")

            if ped_check_list_result == 1:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                tx "Si sigues así,"

                extend " no tendrás tiempo de hacerme nada más."

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "¿Estás seguro de eso?"

                if p_prot_NotJustMasturbate_with_p_txell == False:

                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "Completamente."

                else:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                if p_txell.vaginal_received > 0:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "¿No te gustaría volver a metérmela...?"

                elif p_txell.anal_received > 0:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "¿No te ha gustado metérmela por detrás...?"

                if p_txell.blowjob_done > 0:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    tx "¿Acaso no te ha gustado lo que te he hecho con mi garganta...?"

                if p_prot_NotJustMasturbate_with_p_txell == False:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "Hmm..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "Buen chico."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

            elif ped_check_list_result == 2:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                show gensex_oral_m_frontHead_exp_eyebrows sadx02
                with dissolve

                tx "¿No te pone caliente ver lo húmeda que estoy?"

                if p_txell.vaginal_received > 0:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    with dissolve

                    tx "Estoy segura que la sentirías mucho mejor teniéndola de nuevo en mi interior..."

                else:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    with dissolve


                    tx "Creo que estoy lo suficientemente dilatada como para que pudiera entrar entera..."

                if p_txell.vaginal_received > 0:

                    pass # FOR_FUTURE

                else:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    with dissolve

                    p "..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "Tranquilo,"

                    extend " solo estoy bromeando..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    pt "¿En verdad quiere que me corra pronto"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx07
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    pt "o simplemente le gusta cachondearse de mi?"

            elif ped_check_list_result == 3:

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris down05
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                tx "Realmente pensaba que al verme desnuda te apetecería hacer otras cosas..."

                show gensex_oral_m_frontHead_exp_eyes 02
                show gensex_oral_m_frontHead_exp_iris front02
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "Lo siento."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx08
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                with dissolve

                tx "No,"

                extend " para nada..."

                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                with dissolve

                tx "de hecho me sorprende gratamente."

                if p_prot_NotJustMasturbate_with_p_txell:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    tx "Aunque es una lástima que hayas tenido que cagarla"

                    if p_txell.blowjob_done_TRY > 0:

                        tx "al pedirme que me la metiera en la boca."

                    elif p_txell_missionary_TRY > 0:

                        tx "al pedirme que me pusiera a cuatro patas."

                    elif p_txell_doggy_TRY > 0:

                        tx "al pedirme que me abriera de piernas ante ti."

                    else:

                        aj "ERROR 6484153"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx07
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                else:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    with dissolve


            elif ped_check_list_result == 4:

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "¿Me creerías si te digo que no me está disgustando la idea de que te me corras en la boca?"

                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                p "¿Me dices esto para que me corra más pronto?"

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                tx "Es posible..."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                show gensex_oral_m_frontHead_exp_eyebrows serious
                with dissolve

            elif ped_check_list_result == 5:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                tx "Para serte sincera,"

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris down04
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                tx "es de las pollas más grandes que he visto."

                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                show gensex_oral_m_frontHead_exp_eyebrows sadx03
                with dissolve

                tx "Y te aseguro que he visto bastantes."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                pt "La lesbiana de los huevos..."

            elif ped_check_list_result == 6:

                if p_prot_NotJustMasturbate_with_p_txell == False:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                    with dissolve

                    tx "Realmente me sorprende que no hayas intentado hacer nada más conmigo."

                    if p_prot.cunnilingus_done > 0:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris down04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "Aparte de lamerme el coño,"

                        extend " claro..."

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Pero supongo que eso no cuenta como acto egoísta por tu parte..."

                    if p_didac.seal == "sealed":

                        if p_prot_NotJustMasturbate_with_p_didac == True:

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx01
                            with dissolve

                            tx "Aunque con Dídac no has sido capaz de ser tan casto..."

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx08
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            tx "¿No será que ya te atraía de antemano tu compañero de piso?"

                        else:

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Quizás me equivoqué al juzgarte."

                    else:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows serious
                        with dissolve

                        tx "Aunque habrá que ver qué harás con Dídac..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    menu:

                        pt "Desde luego, amor propio no le falta..."

                        "No has pensado que quizás es que realmente no me atraes.":
                            call p_Help

                            $pl.ch_pts("mp", -2)

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Pssst..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                            with dissolve

                            tx "Quizás eres tú quien tiene mal gusto."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                            with dissolve

                            tx "Desde luego Neus no tenía tantos problemas cuando me las toqueteaba..."

                            show gensex_oral_m_frontHead_exp_eyes 00
                            show gensex_oral_m_frontHead_exp_iris right00
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with hpunch

                            ne "¡Txell!"

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris left04
                            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows sadx03
                            with dissolve

                            menu:

                                "Eso solo demuestra lo poco profesional que eres en tu trabajo, nada más.":
                                    call p_Help

                                    $pl.ch_pts("mp", -1)
                                    $pl.ch_pts("np", -1)

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris front04
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                    with dissolve

                                    tx "..."

                                    show gensex_oral_m_frontHead_exp_eyes 03
                                    show gensex_oral_m_frontHead_exp_iris right03
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                                    with dissolve

                                    ne "¡Dejad esta estupidez!"

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris right04
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                    show gensex_oral_m_frontHead_exp_eyebrows serious
                                    with dissolve

                                    ne "No es momento para actuar como niños."

                                    show gensex_oral_m_frontHead_exp_eyes 05
                                    show gensex_oral_m_frontHead_exp_iris left05
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_m_frontHead_exp_eyebrows sadx04
                                    with dissolve

                                    pt "Pero si ha empezado ella..."

                                "...":
                                    call p_Help


                        "Ya te he dicho que quien realmente me importa es Neus.":
                            call p_Help

                            if p_didac.seal == "sealed":

                                if p_prot_NotJustMasturbate_with_p_didac == False:

                                    $pl.ch_pts("mp", -1)
                                    $pl.ch_pts("dp", -1)
                                    $pl.ch_pts("np", 2)

                                    show gensex_oral_m_frontHead_exp_eyes 00
                                    show gensex_oral_m_frontHead_exp_iris front00
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                    with dissolve

                                    tx "..."

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris left04
                                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                                    with dissolve

                                    tx "Psst..."

                                    show gensex_oral_m_frontHead_exp_eyes 08
                                    show gensex_oral_m_frontHead_exp_iris front08
                                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                    with dissolve

                                    tx "Supongo que es normal que opines así,"

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris front04
                                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                                    with dissolve

                                    tx "si no sabes lo que te estás perdiendo..."

                                    show gensex_oral_m_frontHead_exp_eyes 05
                                    show gensex_oral_m_frontHead_exp_iris front05
                                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                                    with dissolve


                                    pt "Como si me hubiera de todos modos me hubiera dado muchas opciones,"

                                    pt "la bollera esta..."

                                else:

                                    $pl.ch_pts("mp", -1)
                                    $pl.ch_pts("dp", -1)
                                    $pl.ch_pts("np", 2)

                                    show gensex_oral_m_frontHead_exp_eyes 08
                                    show gensex_oral_m_frontHead_exp_iris front08
                                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                    with dissolve

                                    tx "No te interesará tanto Neus,"

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris front04
                                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                    with dissolve

                                    tx "si has hecho lo que sabes que has hecho con tu querido compañero de piso..."

                                    show gensex_oral_m_frontHead_exp_eyes 05
                                    show gensex_oral_m_frontHead_exp_iris front05
                                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                    with dissolve

                                    p "..."

                                    show gensex_oral_m_frontHead_exp_eyes 08
                                    show gensex_oral_m_frontHead_exp_iris front08
                                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                    with dissolve

                                    tx "Que antes tuviera rabo entre las piernas,"

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris front04
                                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                    with dissolve

                                    tx "no creo que te sirva demasiado de excusa..."

                                    show gensex_oral_m_frontHead_exp_eyes 03
                                    show gensex_oral_m_frontHead_exp_iris left03
                                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                    with dissolve

                                    tx "En realidad,"

                                    extend " más bien explica muchas cosas..."

                                    show gensex_oral_m_frontHead_exp_eyes 05
                                    show gensex_oral_m_frontHead_exp_iris front05
                                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                    with dissolve

                                    pt "Maldita ramera..."

                            else: # Not Didac Done yet.

                                $pl.ch_pts("mp", -1)
                                $pl.ch_pts("dp", -1)
                                $pl.ch_pts("np", 2)

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                tx "Hmmm..."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                tx "Eso ya lo veremos cuando le toque el turno a la ninfómana de tu compañera de piso."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris left04
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows normal
                                with dissolve

                                d "¡¿Perdona?!"

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris right01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with hpunch

                                ne "¡Tengamos la fiesta en paz!"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris left04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                with dissolve

                                d "¡Pero si ha empezado la cerda esta!"

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris right02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                ne "¡Ya basta!"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris right04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows sadx04
                                with dissolve

                                ne "Lo digo por ti también, Txell."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris right05
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows sadx05
                                with dissolve

                                ne "Ya sé que te gusta picar,"

                                extend " pero no es el momento."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                                show gensex_oral_m_frontHead_exp_eyebrows sadx04
                                with dissolve

                                tx "Vale, vale..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                                show gensex_oral_m_frontHead_exp_eyebrows sadx05
                                with dissolve

                                tx "Intentaré controlarme..."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                pt "No te lo crees ni tú."


                        "Creo que te valoras demasiado a ti misma.":
                            call p_Help

                            $pl.ch_pts("dp", -1)

                            show gensex_oral_m_frontHead_exp_eyes 02
                            show gensex_oral_m_frontHead_exp_iris front02
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                            with dissolve

                            tx "Eso es porque no sabes de lo que soy capaz."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx07
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve


                            pt "La madre que la parió..."

                        "...":
                            call p_Help

                else:

                    if p_girl_active.blowjob_done_TRY == 0 and p_girl_active.vaginal_received_TRY  == 0 and p_girl_active.anal_received_TRY  == 0:

                        aj "ERROR what you did?"

                    if p_girl_active.vaginal_received_TRY  > 0 and p_girl_active.anal_received_TRY  > 0 and p_girl_active.blowjob_done_TRY  > 0:

                        pass # FOR_FUTURE

                    elif p_girl_active.vaginal_received_TRY  > 0 or p_girl_active.anal_received_TRY  > 0:

                        pass # FOR_FUTURE

                    elif p_girl_active.blowjob_done_TRY  > 0:

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Me sorprende que te estés masturbando después de haber experimentado mi habilidosa lengua..."

                        p "Tan habilidosa no será,"

                        extend " si prefiero masturbarme..."

                        tx "Quizás tienes miedo de enamorarte demasiado de ella."

                        pt "Desde luego,"

                        extend " esta mujer no tiene techo en su narcisismo..."

                    else:

                        aj "ERROR 3598"



            elif ped_check_list_result == 7:

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows serious
                with dissolve

                tx "Quizás si movieras esa mano un poco más rápido terminarías antes."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

            elif ped_check_list_result == 8:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                with dissolve

                tx "Pensaba que al tener mis pechos enfrente de ti,"

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                tx "te correrías más deprisa..."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows serious
                with dissolve

                menu:

                    pt "Al tener sus pechos enfrente..."

                    "¿No te han dicho nunca que eres una presuntuosa de mierda?":
                        call p_Help

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve


                        tx "¿Acaso no te gustan mis pechos?"

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth happy_Silentx03
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                        with dissolve

                        menu:

                            pt "¿Si me gustan sus monstruosos pechos?"

                            "Prefiero los de Neus.":
                                call p_Help

                                $pl.ch_pts("mp", -1)
                                $pl.ch_pts("dp", -1)
                                $pl.ch_pts("np", 2)

                                show gensex_oral_m_frontHead_exp_eyes 00
                                show gensex_oral_m_frontHead_exp_iris front00
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris right02
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                pause 0.2

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                tx "Quizás te interesen más porque te has encariñado de ella,"

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris front03
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                with dissolve

                                tx "pero seguramente ni te hubieras fijado en ella"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                with dissolve

                                tx "si no te hubiera chantajeado para que lo hicieras."

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris right02
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with hpunch

                                ne "¡Txell!"

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris right03
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                with dissolve

                                tx "Tú misma lo dijiste."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris right05
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows sadx03
                                with dissolve

                                ne "..."

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris front01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                p "Eso no tiene nada que ver."

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                p "Simplemente me atrae más un cuerpo femenino de proporciones más modestas."

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris front03
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                p "Tus pechos son exageradamente desproporcionados en comparación con tu cuerpo."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows serious
                                with dissolve

                                p "Si no había salido con Neus antes,"

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                p "es porque tampoco me lo había pedido."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                                with dissolve

                                tx "Ya..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                tx "Si prefieres creerte esa mentira,"

                                extend " allá tú."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris left04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows normal
                                with dissolve

                                pt "¡¿Será posible la zorra esta?!"

                            "Prefiero los de Dídac.":
                                call p_Help

                                $pl.ch_pts("mp", -1)
                                $pl.ch_pts("dp", 2)
                                $pl.ch_pts("np", -2)

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris front01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris left02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                d "¿En serio...?"

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris front03
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                p "A ver..."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                                with dissolve

                                p "No son tan monstruosos como las tuyas,"

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris front01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                p "ni tampoco son como los de Neus."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                pause 0.2

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris right04
                                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                                with Dissolve(0.3)

                                pause 0.2

                                $ Pedrera_char_Cond = "NeusClose_show"
                                call Pedrera_char_lab

                                show neus_exp_mouth sadbiting_Silentx04
                                show neus_exp_iris front01
                                $ nteye = 1
                                call neus_exp_tears_tears
                                show neus_exp_eyebrows surprisex01
                                with fade_short

                                ne "..."

                                if ntlong in range (0,6):
                                    if ntlong < 5:
                                        $ ntlong += 1

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_iris right05
                                $ nteye = 5
                                call neus_exp_tears_tears
                                show neus_exp_eyebrows sadx04
                                with Dissolve(0.5)

                                p "Creo que es un punto medio acertado."

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with fade_short

                                tx "Todo un experto en agasajar a las mujeres,"

                                extend " ¿verdad?"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows angryx01
                                with dissolve

                                p "Solo intento ser sincero."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "Claro,"

                                extend " claro..."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                with dissolve

                                pt "¿Soy yo?"

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris right05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                pt "¿O me está provocando para decir algo que decepcione a Neus?"

                            "No me gustan tan grandes.":
                                call p_Help

                                $pl.ch_pts("mp", -1)
                                $pl.ch_pts("dp", 1)
                                $pl.ch_pts("np", 2)

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris front01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                tx "Pues serás de los pocos hombres que opinen así..."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                with dissolve

                                tx "la gran mayoría tiene un parecer algo distinto."

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris front01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx01
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                p "Quizás sea porque solo has conocido a quinceañeros vírgenes"

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                with dissolve

                                p "que apenas han tocado alguna vez un pecho,"

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx04
                                with dissolve

                                if KnowTxellwasEscort_Cond:

                                    tx "Eso es lo que tú te..."

                                    show gensex_oral_m_frontHead_exp_eyes 00
                                    show gensex_oral_m_frontHead_exp_iris front00
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx01
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex03
                                    with dissolve

                                    p "o quizás es la clase de clientes con los que has tratado"

                                    show gensex_oral_m_frontHead_exp_eyes 03
                                    show gensex_oral_m_frontHead_exp_iris front03
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx09
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx04
                                    with dissolve

                                    p "que aceptan cualquier cosa que tengan delante."

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris left04
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx04
                                    with dissolve

                                    tx "..."

                                    show gensex_oral_m_frontHead_exp_eyes 03
                                    show gensex_oral_m_frontHead_exp_iris front03
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                    with dissolve

                                    p "Pero al menos,"

                                else:

                                    tx "Eso es lo que tú te piensas..."

                                    show gensex_oral_m_frontHead_exp_eyes 04
                                    show gensex_oral_m_frontHead_exp_iris front04
                                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                    with dissolve

                                    p "Al menos,"

                                extend " a título personal,"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                                with dissolve

                                p "y siendo partícipe de ciertas conversaciones entre amigos algo picantonas,"

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                                with dissolve

                                p "por normal general,"

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                p "se prefiere un tamaño con el que se pueda agarrar bien con una mano"

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris front03
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                p "y si me apuras mucho,"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                                with dissolve

                                p "un tamaño que permita una buena cubana."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                p "Lo tuyo sin embargo,"

                                show gensex_oral_m_frontHead_exp_eyes 00
                                show gensex_oral_m_frontHead_exp_iris front00
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                p "creo que se podría definir casi como zoomórfico."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx09
                                show gensex_oral_m_frontHead_exp_eyebrows angryx05
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris left01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                d "Seremos unos pervertidos..."

                                $ Pedrera_char_Cond = "DidacClose_show"
                                call Pedrera_char_lab

                                show didacf_mouth happy_Talkingx05
                                $ dteye = 2
                                call didac_exp_tears_tears
                                show didacf_pupils front02
                                show didacf_eyebrows angryx03
                                with fade_short

                                d "pero en general tampoco somos muy exigentes con este tipo de cosas..."

                                show didacf_mouth sad_Talkingx004
                                $ dteye = 3
                                call didac_exp_tears_tears
                                show didacf_pupils front03
                                show didacf_eyebrows surprisex01
                                with dissolve

                                d "Aunque creo que de las tres,"

                                show didacf_mouth happy_Talkingx06
                                $ dteye = 2
                                call didac_exp_tears_tears
                                show didacf_pupils down02
                                show didacf_eyebrows angryx01
                                with dissolve

                                d "creo que soy la que tengo el mejor tamaño."

                                show didacf_mouth happy_Talkingx04
                                $ dteye = 4
                                call didac_exp_tears_tears
                                show didacf_pupils front04
                                show didacf_eyebrows angryx02
                                with dissolve

                                d "¿No crees?"

                                show didacf_mouth happy_Silentx05
                                $ dteye = 5
                                call didac_exp_tears_tears
                                show didacf_pupils front05
                                show didacf_eyebrows angryx03
                                with dissolve

                                pause 0.2

                                $ Pedrera_char_Cond = "p_nobody"
                                call Pedrera_char_lab

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris left05
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx04
                                with fade_short

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx005
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                tx "Con Neus tampoco podrías hacerte muchas cubanas,"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                with dissolve

                                tx "¿No crees?"

                                show gensex_oral_m_frontHead_exp_eyes 00
                                show gensex_oral_m_frontHead_exp_iris right00
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with vpunch

                                ne "¡Meritxell!"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris left04
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows sadx04
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                                show gensex_oral_m_frontHead_exp_eyebrows sadx03
                                with dissolve

                                tx "Vale,"

                                extend " vale..."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris left04
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                tx "ya me callo."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris left05
                                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows sadx03
                                with dissolve

                                pt "¿Qué demonios pretende provocándome?"

                            "Eso no te lo puedo negar...":
                                call p_Help

                                $pl.ch_pts("mp", 1)
                                $pl.ch_pts("dp", -1)
                                $pl.ch_pts("np", -2)

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "..."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                tx "Al menos eres sincero."

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows sadx03
                                with dissolve

                                tx "No me esperaba eso de ti."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris right05
                                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                                show gensex_oral_m_frontHead_exp_eyebrows angryx01
                                with dissolve

                                p "..."

                            "Eso no tiene nada que ver.":
                                call p_Help

                                $pl.ch_pts("mp", 1)

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "¿Que algo te ayude a provocarte el orgasmo más pronto no tiene nada que ver?"

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve


                                tx "¿O quizás en lugar de tener a una mujer hecha y derecha como yo,"

                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris left03
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                                show gensex_oral_m_frontHead_exp_eyebrows normal
                                with dissolve

                                tx "prefirieras tener a un hombre musculado y desnudo con un miembro al par con el tuyo"

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                                show gensex_oral_m_frontHead_exp_eyebrows sadx02
                                with dissolve

                                tx "en frente de ti?"

                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris front04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                                with dissolve

                                p "Estás enferma."

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                                with dissolve

                                tx "No soy yo quien tiene la polla dura."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx07
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                                with dissolve

                                p "..."

                            "...":
                                call p_Help

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx005
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                                with dissolve

                                tx "¿Se te ha comido la lengua el gato?"

                                show gensex_oral_m_frontHead_exp_eyes 08
                                show gensex_oral_m_frontHead_exp_iris front08
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                                with dissolve

                                tx "Tranquilo,"

                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris front02
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                                with dissolve

                                tx "suelo causar esa impresión en los hombres."

                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris front05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows angryx01
                                with dissolve

                                p "..."

                    "...":
                        call p_Help

            elif ped_check_list_result == 9:

                if p_didac.seal == "sealed":

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris right01
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    d "Conmigo no tardaste tanto..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris right04
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "Es normal que tarde más si es su segunda corrida."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris right05
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    d "Seguro..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    tx "..."

                else:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "¿Con Dídac también tardarás tanto en correrte?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris right04
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve


            elif ped_check_list_result == 10:

                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                tx "Te correrías antes si empiezo a tocarme los pechos?"

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows sadx02
                with dissolve

                tx "O con tu imaginación ya tienes suficiente?"

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                with dissolve

                p "..."

            else:

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "..."


    elif p_prot.action in ["rest", "takeDickOut", "takeTongueOut"] or p_prot.b_action in ["takeDickOut"]:

        if p_prot.b_action in ["takeDickOut"] or p_prot.action in ["takeDickOut", "takeTongueOut"]:

            call p_txell_notReceiveBlowjob

        else:

            ## 69 rest here is IMPOSSIBLE

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

                if FuckM_Start_Cond:

                    $ debug("Txell wanting to have oral with you?")

                    call WIP

                else:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "Supongo que de todos modos,"

                    extend " al final,"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "tienes que terminar en mi boca igualmente..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris right05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

            elif p_prot.pos_oral_rest >= 1: #or p_prot.pos_69_rest > 1:

                $ ped_check_1_10("ped_oral_rest_txell_list")

                if ped_check_list_result in range(1,11):

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                if ped_check_list_result == 1:

                    if p_prot.masturbate == 0:

                        tx "Puedes empezar a masturbarte."

                    else:

                        tx "Puedes continuar con tu masturbación."

                    if FuckM_Start_Cond == False and p_txell_blowjob_done_ACCEPTED == False:

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "Tampoco te voy a hacer nada más..."

                    elif p_txell_blowjob_done_ACCEPTED:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris right04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "¿O prefieres que vuelva a metérmela en la boca?"

                elif ped_check_list_result == 2:

                    if FuckM_Start_Cond == False:

                        tx "Sabes que no te haré nada,"

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris right05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                        with dissolve

                        tx "así que será mejor que empieces a darle brillo a ese manubrio tuyo."

                    elif p_txell_blowjob_done_ACCEPTED:

                        tx "Si no quieres que te la chupe,"

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        tx "me parece muy bien,"

                        extend " pero será mejor que hagas algo."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "No puedes estar toda la noche ahí quieto sin hacer nada."

                elif ped_check_list_result == 3:

                    tx "Podemos estar así toooooda la noche..."

                elif ped_check_list_result == 4:

                    tx "¿Tanto te han impresionado mis pechos que te has quedado patidifuso ante mi?"

                elif ped_check_list_result == 5:

                    tx "¿Te intimida tener a una mujer de mi calibre tan cerca,"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "y por eso eres incapaz de hacer nada?"

                elif ped_check_list_result == 6:

                    tx "No eres capaz ni de articular palabra."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    tx "A veces causo ese efecto en los hombres."

                elif ped_check_list_result == 7:

                    tx "¿Estás esperando que salga el sol?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "No te creas que tengo yo muchas ganas de hacer algo contigo..."

                elif ped_check_list_result == 8:

                    tx "¿Tanto disfrutas de lo que ves,"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "que no eres capaz ni de moverte?"

                elif ped_check_list_result == 9:

                    tx "Son bonitas,"

                    extend " ¿verdad?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Pues empieza a masturbarte,"

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    tx "o no saldremos hoy de aquí."

                elif ped_check_list_result == 10:

                    tx "¿Te crees que esto es una broma?"

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    tx "Sino me fuera la vida,"

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    tx "no estaría aquí desnuda de rodillas ante ti."

                else:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "..."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris right05
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve
            
            call afternight05_Pedrera_Neus_Warning


    ###############
###############

    elif p_prot.action in ["titwank_received_TRY", "titwank_received"]:

        $ p_txell.titwank_received_TRY += 1

        if p_txell.titwank_received_TRY == 1:

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with fade_short

            n "Lentamente te acercas a la cama y reposas tu espalda sobre ella"

            show m_exp_eyes 04
            show m_exp_piris down04
            show m_exp_mouth sad_Silentx05
            show m_exp_eyebrows surprisex001
            with dissolve

            n "invitando a Meritxell a cercarse."

            tx "..."

            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "¿En serio...?"

            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_mouth sad_Silentx02
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Sabes que sí."

            show m_exp_eyes 04
            show m_exp_piris down04
            show m_exp_mouth sad_Silentx05
            show m_exp_eyebrows serious
            with dissolve

            p "Tampoco te estoy pidiendo que te la metas en la boca,"

            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_mouth sad_Silentx04
            show m_exp_eyebrows normal
            with dissolve

            extend " ¿no?"

            if p_txell.blowjob_done > 0:

                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_mouth sad_Talkingx05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                tx "Como si no lo hubieras hecho ya..."

            else:

                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_mouth sad_Talkingx05
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Por ahora..."

            show m_exp_eyes 03
            show m_exp_piris down03
            show m_exp_mouth sad_Silentx04
            show m_exp_eyebrows suspiciousx03
            with dissolve

            n "Sutilmente, sigues insistiendo con tu movimiento de caderas."

    ##

        if p_txell.orgasm > p_didac_cunnilingus_p_txell_orgasm and p_txell.orgasm > 0:

            $ debug("Txell should let you do a boobjob.")

            $ p_txell_titwank_ACCEPTED = True


        if p_txell_titwank_ACCEPTED == False:

            $ debug("You TRY to receive a TIT wank from Txell.")

            $ Pedrera_char_Cond = "TxellClose_b_show"
            call Pedrera_char_lab

            if p_txell.titwank_received_TRY == 1:

                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_mouth sad_Talkingx04
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Puedes empeñarte tanto cómo quieras,"

                extend " no lo voy a hacer."

                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_mouth sad_Talkingx05
                show m_exp_eyebrows serious
                with dissolve

                tx "Y mucho menos sin haber tenido aún ni siquiera un orgasmo..."

                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_mouth sad_Talkingx004
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Sin mencionar,"

                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_mouth sad_Talkingx03
                show m_exp_eyebrows normal
                with dissolve

                if p_txell.cunnilingus_received == 0:

                    tx "que ni siquiera has pasado una sola vez tu lengua entre mis piernas..."

                elif p_txell.cunnilingus_received == 1:

                    tx "que apenas has pasado tu lengua entre mis piernas una sola vez."

                else:

                    tx "que tan solo has pasado tu lengua entre mis piernas unas [p_txell.cunnilingus_received] veces..."

                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_mouth sad_Talkingx04
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "No sé con qué clase de mujeres habrás estado,"

                extend " pero me apiado de ellas..."

                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_mouth sad_Silentx02
                show m_exp_eyebrows surprisex02
                with dissolve

                p "La idea es que me corra para salvarte la vida."

                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_mouth sad_Talkingx07
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Pues estás tardando en masturbarte."

                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_mouth happy_Silentx03
                show m_exp_eyebrows angryx01
                with dissolve

                pt "Será hija de..."

            elif p_txell.titwank_received_TRY == 2:

                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_mouth sad_Silentx04
                show m_exp_eyebrows suspiciousx02
                with dissolve

                tx "..."

                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_mouth sad_Talkingx07
                show m_exp_eyebrows angryx02
                with dissolve

                tx "¿Acaso no has escuchado lo que he dicho antes?"

                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_mouth sad_Silentx06
                show m_exp_eyebrows surprisex02
                with dissolve

                p "No soy sordo."

                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_mouth sad_Talkingx07
                show m_exp_eyebrows angryx03
                with dissolve

                tx "Lo parece."

                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_mouth sad_Silentx05
                show m_exp_eyebrows angryx01
                with dissolve

            else:

                $ ped_check_1_10("ped_titwank_txell_list")

                if ped_check_list_result == 1:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "No has usado ni una sola vez tu lengua en mi entrepierna..."

                elif ped_check_list_result == 2:

                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "Te recuerdo que aún no he tenido ni un sólo orgasmo..."

                elif ped_check_list_result == 3:

                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyebrows sadx02
                    with dissolve

                    tx "Sigue soñando..."

                elif ped_check_list_result == 4:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "¿porqué debería complacer tus caprichos?"

                elif ped_check_list_result == 5:

                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyebrows sadx03
                    with dissolve

                    tx "Te gustaría..."

                    extend " ¿Verdad?"

                elif ped_check_list_result == 6:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Eres pesadito..."

                elif ped_check_list_result == 7:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "¿Así es como tratas a las mujeres con las que estás?"

                elif ped_check_list_result == 8:

                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    tx "Muchos hombres desearían estar en tu lugar..."

                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyebrows normal
                    with dissolve

                    tx "así que no pidas más."

                elif ped_check_list_result == 9:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "¿Tanto te cuesta darme un orgasmo?"

                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyebrows sadx02
                    with dissolve

                    tx "Que desilusión..."

                elif ped_check_list_result == 10:

                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Tu poder de persuasión es conmovedor..."

                else:

                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "..."

                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_mouth sad_Silentx04
                show m_exp_eyebrows surprisex002
                with dissolve

            $ p_prot.action = "rest"

            call afternight05_Pedrera_Neus_Warning

            $ Pedrera_char_Cond = "p_nobody"
            call Pedrera_char_lab

            $ ped_sex_general_expression_Cond = "indifferent"
            $ ped_sex_general_action_Cond = "o00_00"
            call pedrera_sex_p_general_talk

        elif p_txell_titwank_ACCEPTED == True:

            if p_txell.titwank_done == 0:

                $ Pedrera_char_Cond = "TxellClose_b_show"
                call Pedrera_char_lab

                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyebrows suspiciousx03
                with dissolve

                tx "..."

                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_mouth sad_Talkingx03
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Supongo que te lo has ganado..."

                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_mouth sad_Talkingx003
                show m_exp_eyebrows surprisex002
                with dissolve

                tx "Al fin y al cabo no esperaba que me dieras ningún orgasmo."

                show m_exp_eyes 05
                show m_exp_piris down05
                show m_exp_mouth sadbiting_Silentx03
                show m_exp_eyebrows suspiciousx02
                with dissolve

                pause 0.2

            $ debug ("You receive a Tit Wank from Txell.")

            $ p_txell.action = "titwank_done"
            $ p_prot.action = "titwank_received"
            $ p_txell.titwank_done += 1
            $ p_prot.titwank_received += 1

            if p_txell.titwank_done == 1:

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "ob00_00"
                call pedrera_sex_p_general_talk

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris down04
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                with fade_short

                n "Sin demasiado entusiasmo,"

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                pause 0.2

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "ob00_00b"
                call pedrera_sex_p_general_talk

                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with Dissolve(0.5)

                n "se acerca hasta ti poniendo tu erecto miembro entre sus pechos."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris down05
                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                tx "Hmmm..."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "Debo reconocer que es bastante grande,"

                extend " para que sobresalga..."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                p "No me negarás que algo,"

                show gensex_oral_m_frontHead_exp_eyes 01
                show gensex_oral_m_frontHead_exp_iris front01
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                with dissolve

                p "te pone."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve

                tx "Que esté sorprendida,"

                extend " no significa que esté cachonda."

                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris down05
                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "..."

                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                with dissolve

                tx "Supongo que es mejor esto que usar mi lengua..."

                if p_txell.blowjob_done > 0:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    p "Como si te hubiera disgustado tanto..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris right05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "No voy a opinar sobre ello."

                $ ped_sex_general_expression_Cond = "indifferent"
                $ ped_sex_general_action_Cond = "ob01_01"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                n "Con cierta frialdad empieza a desplazar sus pechos sobre tu miembro."

                p "Hmmm..."

            if p_txell.titwank_done > 1:

                if p_txell.titwank_done > 5:
                    $ ped_sex_general_action_Cond = "ob01_05"
                if p_txell.titwank_done > 4:
                    $ ped_sex_general_action_Cond = "ob01_04"
                elif p_txell.titwank_done > 3:
                    $ ped_sex_general_action_Cond = "ob01_03"
                elif p_txell.titwank_done > 2:
                    $ ped_sex_general_action_Cond = "ob01_02"
                elif p_txell.titwank_done > 1:
                    $ ped_sex_general_action_Cond = "ob01_01"
                else:
                    $ ped_sex_general_action_Cond = "ob00_05"

                if p_txell.titwank_done > 3:
                    $ ped_sex_general_expression_Cond = "lustSmile"
                else:
                    $ ped_sex_general_expression_Cond = "indifferent"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                if p_txell.titwank_done > 3:

                    if randomnum_1to5 == 1:
                        pt "Joder..."
                    elif randomnum_1to5 == 2:
                        p "Dios..."
                    elif randomnum_1to5 == 3:
                        p "Uhhmm..."
                    elif randomnum_1to5 == 4:
                        p "Ggghnn..."
                    elif randomnum_1to5 == 5:
                        tx "..."

                else:

                    if randomnum_1to5 == 1:
                        p "Pff..."
                    elif randomnum_1to5 == 2:
                        p "Huhhmm..."
                    elif randomnum_1to5 == 3:
                        p "Grrghnt..."
                    elif randomnum_1to5 == 4:
                        pt "Que par tiene la muy..."
                    elif randomnum_1to5 == 5:
                        tx "..."

            if p_txell.titwank_done > 1:

                $ ped_sex_general_expression_Cond = "talk"
                $ ped_sex_general_action_Cond = "ob00_00b"
                call pedrera_sex_p_general_talk

                $ ped_check_1_10("ped_titwank_done_txell_list")

                if ped_check_list_result == 1:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                    with dissolve

                    tx "Espero que así no tardes mucho en correrte."

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris front01
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "Eso dependerá de tu habilidad."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    tx "..."

                elif ped_check_list_result == 2:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with Dissolve(0.5)

                    tx "No parece disgustarte."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "Tampoco suelo recibir quejas,"

                    extend " no te preocupes."

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris front01
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "¿Has masturbado con tus pechos a muchos tíos?"

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris left03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "Más de los que soy capaz de recordar."

                    if KnowTxellwasEscort_Cond:

                        show gensex_oral_m_frontHead_exp_eyes 02
                        show gensex_oral_m_frontHead_exp_iris front02
                        show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        p "Me imagino que la mayoría deberían de ser cuando trabajabas de..."

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                        show gensex_oral_m_frontHead_exp_eyebrows normal
                        with dissolve

                        tx "En su gran mayoría."

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris left05
                        show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                        show gensex_oral_m_frontHead_exp_eyebrows sadx01
                        with dissolve

                        pt "¿Eso es que también lo hizo con hombres sin cobrar?"

                elif ped_check_list_result == 3:

                    if p_txell.blowjob_done == 0:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                        with dissolve

                        tx "Te gustaría metérmela en la boca,"

                        extend " ¿verdad?"

                        show gensex_oral_m_frontHead_exp_eyes 02
                        show gensex_oral_m_frontHead_exp_iris front02
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        p "Sinceramente, tus pechos se sienten realmente bien."

                        show gensex_oral_m_frontHead_exp_eyes 03
                        show gensex_oral_m_frontHead_exp_iris front03
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows serious
                        with dissolve

                        tx "Ni te imaginas la de cosas que puedo hacer con mi lengua..."

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                        show gensex_oral_m_frontHead_exp_eyebrows angryx01
                        with dissolve

                        pt "¿Me está provocando para que se la meta en la boca"

                        pt "o intenta excitarme para que me corra antes?"

                    else:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Te gustaría volver a metérmela en la boca,"

                        extend "¿Verdad?"

                        show gensex_oral_m_frontHead_exp_eyes 02
                        show gensex_oral_m_frontHead_exp_iris front02
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        p "Si te he pedido tus pechos,"

                        extend " es porque por ahora los prefiero."

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                        with dissolve

                        tx "..."

                        show gensex_oral_m_frontHead_exp_eyes 01
                        show gensex_oral_m_frontHead_exp_iris front01
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        p "¿Preferirías que te la metiera en la boca?"

                        show gensex_oral_m_frontHead_exp_eyes 03
                        show gensex_oral_m_frontHead_exp_iris front03
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "¿Terminarías antes si te dijera que sí?..."

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        pt "Será zorra..."


                elif ped_check_list_result == 4:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "No estoy segura si estás disfrutando más con tu polla entre mis pechos"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "o con tu pervertida mirada fijada en ellos..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    menu:

                        "No se puede negar que tienes unos pechos espectaculares.":
                            call p_Help

                            $pl.ch_pts("mp",1)

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                            with dissolve

                            tx "Dime algo que no sepa."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris left04
                            show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows serious
                            with dissolve

                            pt "Será..."

                        "Es difícil no disfrutar de unos pechos que me arropan la polla entera.":
                            call p_Help

                            $pl.ch_pts("mp",1)

                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris front01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                            with dissolve

                            p "No es algo que me pase a menudo..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris down04
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Hmmm..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                            show gensex_oral_m_frontHead_exp_eyebrows sadx02
                            with dissolve

                            tx "Supongo que no."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris left04
                            show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows serious
                            with dissolve

                        "Son un poco demasiado fofos para mi gusto, los prefiero más como Dídac, tersos y firmes.":
                            call p_Help

                            $pl.ch_pts("dp",2)
                            $pl.ch_pts("mp",-3)

                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris front01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                            with dissolve

                            tx "*Pseh...*"

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris right04
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            tx "Supongo que son gustos..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris left05
                            show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows sadx01
                            with dissolve

                        "...":
                            call p_Help

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                            with dissolve

                elif ped_check_list_result == 5:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "Está claro que te gustan..."

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris front01
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "No voy a negar una evidencia."

                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    tx "Dime,"

                    extend " ¿te gustan más que los de Dídac?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                    menu:

                        pt "¿Si me gustan más sus pechos que los de Dídac?"

                        "Desde luego, tus pechos son mucho más grandes y esponjosos.":
                            call p_Help

                            $pl.ch_pts("dp",-2)
                            $pl.ch_pts("np",-1)
                            $pl.ch_pts("mp",3)

                            show gensex_oral_m_frontHead_exp_eyes 02
                            show gensex_oral_m_frontHead_exp_iris front02
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            tx "Hmmm..."

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows sadx01
                            with dissolve

                            tx "No esperaba que fueras tan sincero..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Pero agradezco ese detalle."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris right04
                            show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows sadx01
                            with dissolve

                        "La verdad es que son mucho más blandos, pero también abarcan mucho más; ambas tenéis unos pechos increíbles.":
                            call p_Help

                            $pl.ch_pts("dp",1)
                            $pl.ch_pts("mp",1)

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "La respuesta neutral sin elegir favoritas,"

                            extend " muy listo el chico..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                            with dissolve

                        "Lamento decirte que los de Dídac son mucho más tersos y firmes que los tuyos.":
                            call p_Help

                            $pl.ch_pts("dp",2)
                            $pl.ch_pts("mp",-1)

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows serious
                            with dissolve

                            tx "Hmmm..."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                            with dissolve

                            tx "Bueno..."

                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris right03
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            tx "eso no te lo puedo negar..."

                            show gensex_oral_m_frontHead_exp_eyes 02
                            show gensex_oral_m_frontHead_exp_iris front02
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                            with dissolve

                            p "Has sido tú quien me ha preguntado."

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Lo sé,"

                            extend " lo sé..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris right05
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                            with dissolve

                elif ped_check_list_result == 6:

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    if p_txell.blowjob_done > 0:

                        tx "Al final pensaré que prefieres mis pechos a mi garganta..."

                    else:

                        tx "Al final pensaré que prefieres esto a que me la meta en la boca..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris left05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    pause 0.2

                elif ped_check_list_result == 7:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris down04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "La verdad es que masturbar una polla tan grande"

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris down03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "y sin ser de plástico,"

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                    with dissolve

                    tx "es algo..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "digamos que interesante..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                elif ped_check_list_result == 8:

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    with dissolve

                    tx "No se puede negar que te encantan mis pechos..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris left05
                    show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                elif ped_check_list_result == 9:

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    tx "¿Te habían hecho una cubana así alguna vez en tu vida?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    menu:

                        "Tampoco te creas tan especial.":
                            call p_Help

                            $pl.ch_pts("mp",-1)

                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris front01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris right04
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                            with dissolve

                        "Los preferiría más grandes":
                            call p_Help

                            $pl.ch_pts("np",-3)
                            $pl.ch_pts("dp",-2)
                            $pl.ch_pts("mp",-2)

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                            with dissolve

                            tx "Salió exigente el chico..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris left04
                            show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "NeusClose_show"
                            call Pedrera_char_lab

                            show neus_exp_mouth sad_Silentx02
                            $ nteye = 1
                            call neus_exp_tears_tears
                            show neus_exp_iris front01
                            show neus_exp_eyebrows surprisex01
                            with fade_short

                            pause 0.2

                            show neus_exp_mouth sadbiting_Silentx04
                            $ nteye = 5
                            call neus_exp_tears_tears
                            show neus_exp_iris left05
                            show neus_exp_eyebrows sadx02
                            with dissolve

                            ne "..."

                            $ Pedrera_char_Cond = "DidacClose_show"
                            call Pedrera_char_lab

                            show didacf_mouth sad_Talkingx06
                            $ dteye = 2
                            call didac_exp_tears_tears
                            show didacf_pupils front02
                            show didacf_eyebrows angryx03
                            with fade_short

                            d "¡¿Es que te los hizo una vaca o qué?!"

                            show didacf_mouth sad_Silentx05
                            $ dteye = 4
                            call didac_exp_tears_tears
                            show didacf_pupils front04
                            show didacf_eyebrows angryx04
                            with dissolve

                            tx "Déjale mentir..."

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                            show gensex_oral_m_frontHead_exp_eyebrows sadx03
                            with fade_short

                            tx "Si es feliz así."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            p "No estoy mintiendo."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_m_frontHead_exp_eyebrows sadx02
                            with dissolve

                            tx "Lo que tú digas, guapo."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris left05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows angryx01
                            with dissolve

                        "Son demasiado grandes para mi gusto.":
                            call p_Help

                            $pl.ch_pts("np",1)
                            $pl.ch_pts("dp",1)
                            $pl.ch_pts("mp",-1)

                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris front01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            tx "..."

                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            tx "Pero seguro que no lo disfrutarías del mismo modo."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                            with dissolve

                            pt "Engreída de mierda..."

                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris left05
                            show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows sadx01
                            with dissolve

                elif ped_check_list_result == 10:

                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows sadx01
                    with dissolve

                    tx "Siento que tampoco tardarás mucho en correrte..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx02
                    with dissolve

                    tx "¿Me equivoco?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    p "..."

                else:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve

                    tx "..."

            #if p_txell.titwank_done > 1: # not necessary.

                if p_txell.titwank_done > 5:
                    $ ped_sex_general_action_Cond = "ob01_05"
                if p_txell.titwank_done > 4:
                    $ ped_sex_general_action_Cond = "ob01_04"
                elif p_txell.titwank_done > 3:
                    $ ped_sex_general_action_Cond = "ob01_03"
                elif p_txell.titwank_done > 2:
                    $ ped_sex_general_action_Cond = "ob01_02"
                elif p_txell.titwank_done > 1:
                    $ ped_sex_general_action_Cond = "ob01_01"
                else:
                    $ ped_sex_general_action_Cond = "ob00_04"

                if p_txell.titwank_done > 3:
                    $ ped_sex_general_expression_Cond = "lustSmile"
                else:
                    $ ped_sex_general_expression_Cond = "indifferent"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

        
    ###############
###############

    #elif p_prot.action == "blowjob_received_TRY":
    elif p_prot.action in ["blowjob_received_TRY", "blowjob_received"]: ## pos.ORAL (not 69)

        ##

        $ debug ("ORAL TEST")

        $ p_txell.blowjob_done_TRY += 1

        if p_txell.blowjob_done_TRY > 5:
            $ ped_sex_general_action_Cond = "o00_05"
        elif p_txell.blowjob_done_TRY > 4:
            $ ped_sex_general_action_Cond = "o00_04"
        elif p_txell.blowjob_done_TRY > 3:
            $ ped_sex_general_action_Cond = "o00_03"
        elif p_txell.blowjob_done_TRY > 2:
            $ ped_sex_general_action_Cond = "o00_02"
        elif p_txell.blowjob_done_TRY > 1:
            $ ped_sex_general_action_Cond = "o00_01"
        else:
            $ ped_sex_general_action_Cond = "o00_02"

        if p_txell.orgasm > p_didac_cunnilingus_p_txell_orgasm and p_txell.orgasm > 0:

            $ p_txell_blowjob_done_ACCEPTED = True

        if p_txell_blowjob_done_ACCEPTED == False:

            $ p_txell.blowjob_done_TRY += 1

            if p_txell.blowjob_done_TRY > 2:
                $ ped_sex_general_expression_Cond = "lustSmile"
            else:
                $ ped_sex_general_expression_Cond = "angry"
            call pedrera_sex_p_general_talk
            with Dissolve(0.5)

            if FuckM_Start_Cond == False:

                $ p_txell.action = "rest"
                $ p_txell.b_action = "rest"
                $ p_prot.action = "rest"
                $ p_prot.b_action = "rest"

                tx "..."

                if p_txell.blowjob_done_TRY == 1:
                    n "Sutilmente, acaricias con tu miembro su mejilla para indicarle que empiece."

                elif p_txell.blowjob_done_TRY == 2:
                    n "Vuelves a acariciarle la mejilla para intentarlo de nuevo."

                elif p_txell.blowjob_done_TRY == 3:
                    n "Lo vuelves a intentar."

                $ ped_sex_general_action_Cond = "o00_00"
                $ ped_sex_general_expression_Cond = "talk"
                call pedrera_sex_p_general_talk


                if p_txell.blowjob_done_TRY == 1:

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Si crees que me la voy a meter en la boca, es que estás peor de lo que pensaba."

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris front01
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    p "Igualmente tendré que correrme en la boca,"

                    extend " ¿no?"

                    p "Así que,"

                    extend " ¿qué más da?"

                    tx "..."

                    tx "Una cosa es que termines en mi boca,"

                    tx "y la otra muy distinta es que te ayude a llegar."

                    p "No seas así..."

                    tx "Da gracias que puedas correrte en mi boca,"

                    tx "pero no pidas más."

                    pt "Será perra..."

                elif p_txell.blowjob_done_TRY == 2:

                    show gensex_oral_m_frontHead_exp_eyes 03
                    show gensex_oral_m_frontHead_exp_iris front03
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx08
                    show gensex_oral_m_frontHead_exp_eyebrows angryx03
                    with vpunch

                    tx "¿Acaso no me expresado con claridad?"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    p "Pero quizás cambies de opinión."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                    with dissolve

                    tx "¿Y esta es tu manera de intentar convencerme?"

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    p "..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows sadx03
                    with dissolve

                    tx "Hombre tenías que ser..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                    with dissolve

                    pt "Pero será..."

                if p_txell.blowjob_done_TRY > 2:

                    $ ped_check_1_10("ped_oralTRY_txell_list")

                    if ped_check_list_result == 1:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "Puedes insistir tantas veces como quieras,"

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows sadx03
                        with dissolve

                        tx "pero no es más que una pérdida de tiempo."

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "Y no creo que estemos en una situación para malgastarlo de esta manera."

                    elif ped_check_list_result == 2:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Ni los primates son tan obtusos para entender algo tan básico."

                    elif ped_check_list_result == 3:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Al final pensaré realmente que necesitas un tratamiento para tu retraso mental."

                    elif ped_check_list_result == 4:

                        show gensex_oral_m_frontHead_exp_eyes 02
                        show gensex_oral_m_frontHead_exp_iris front02
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        p "Si te la pusieras en la boca,"

                        extend " es probable que terminase antes..."

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Cuanto más tardes en masturbarte,"

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "más tardarás en terminar."

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        p "..."

                    elif ped_check_list_result == 5:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "Puedes insistir tantas veces como quieras,"

                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris front05
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                        with dissolve

                        tx "no va a servir de nada."

                    elif ped_check_list_result == 6:

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Otra cosa no sé,"

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                        with dissolve

                        tx "pero tozudo,"

                        extend " lo eres un rato."

                    elif ped_check_list_result == 7:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                        with dissolve

                        tx "¿No entiendes un no por respuesta?"

                    elif ped_check_list_result == 8:

                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_m_frontHead_exp_eyebrows angryx03
                        with dissolve

                        tx "De verdad,"

                        extend " que pesadito eres..."

                    elif ped_check_list_result == 9:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                        with dissolve

                        tx "¿De verdad te funciona este método de seducción con otras mujeres?"

                    else:

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                    with dissolve

                if p_txell_blowjob_done_ACCEPTED:

                    call p_txell_blowjobDeep_done_kneels_label

                else:

                    call afternight05_Pedrera_Neus_Warning

            if FuckM_Start_Cond == True:

                aj "ERROR This is still in development."

        else: # p_txell_blowjob_done_ACCEPTED == True:

            $ debug ("Txell want to do Oral to you.")

            $ p_txell_blowjobDeep_done_kneels += 1

            if p_txell_blowjobDeep_done_kneels == 1:

                call p_txell_blowjobDeep_done_kneels_label

            else:

                if takeDickOut_m_Total < 1:

                    $ takeDickOut_m_Total == 2

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "¿Ahora quieres volver a metérmela?"

                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    p "Sabes que me la he quitado para aguantar un poco más."

                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris left05
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris right01
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                    with dissolve

                    d "¡En el fondo te está tirando un piropo y lo sabes!"

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris right04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    with dissolve

                    tx "..."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris down04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Hmmm..."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                    with dissolve

                    tx "Supongo que sí."

                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris right04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                    tx "Acabemos con esto de una vez."

                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows serious
                    with dissolve

                elif takeDickOut_m_Total >= 1:

                    $ ped_check_1_5("ped_oral_again_txell_list_01")

                    if ped_check_list_result in range(1,6):
                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris front04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                        show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    else:
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_m_frontHead_exp_eyebrows angryx03

                    with dissolve

                    if ped_check_list_result == 1:

                        tx "¿Otra vez?"

                    elif ped_check_list_result == 2:

                        tx "¿A qué estás jugando?"

                    elif ped_check_list_result == 3:

                        tx "¿Y si no me da la gana ahora?"

                    elif ped_check_list_result == 4:

                        tx "Tienes una actitud bastante infantil."

                    elif ped_check_list_result == 5:

                        tx "¿Ahora te apetece?"

                    else:

                        tx "..."

                    $ ped_check_1_5("ped_oral_again_txell_list_02")

                    if ped_check_list_result in range(1,6):
                        show gensex_oral_m_frontHead_exp_eyes 03
                        show gensex_oral_m_frontHead_exp_iris front03
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
                        show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
                    else:
                        show gensex_oral_m_frontHead_exp_eyes 08
                        show gensex_oral_m_frontHead_exp_iris front08
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                        show gensex_oral_m_frontHead_exp_eyebrows angryx04

                    if ped_check_list_result == 1:

                        p "Sabes que lo he hecho para durar más."

                    elif ped_check_list_result == 2:

                        p "Sabes de sobra por qué lo he hecho."

                    elif ped_check_list_result == 3:

                        p "Como si no supieras la razón por la que lo he quitado antes."

                    elif ped_check_list_result == 4:

                        p "No creo que tenga que explicarte el por qué lo he hecho."

                    elif ped_check_list_result == 5:

                        p "Eres perfectamente consciente del por qué lo he hecho."

                    else:

                        p "..."

                    $ ped_check_1_5("ped_oral_again_txell_list_03")

                    if ped_check_list_result in range(1,6):

                        show gensex_oral_m_frontHead_exp_eyes 04
                        show gensex_oral_m_frontHead_exp_iris right04
                        show gensex_oral_m_frontHead_exp_mouth sad_Talkingx07
                        show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    else:
                        show gensex_oral_m_frontHead_exp_eyes 05
                        show gensex_oral_m_frontHead_exp_iris right05
                        show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                        show gensex_oral_m_frontHead_exp_eyebrows angryx03

                    if ped_check_list_result == 1:

                        tx "Bah..."

                        tx "¿Qué más da?"

                    elif ped_check_list_result == 2:

                        tx "Si eso te hace terminar antes..."

                    elif ped_check_list_result == 3:

                        tx "Al menos eres sincero."

                    elif ped_check_list_result == 4:

                        tx "Al menos me alegra escucharte admitir lo buena que soy."

                    elif ped_check_list_result == 5:

                        tx "Espero que termines pronto al menos."

                    else:

                        tx "..."

                else:

                    aj "ERROR 59455156"


                call p_txell_blowjobDeep_done_label

            

    ###############
###############
    
    elif p_txell.action == "blowjobDeep_done":

        $ debug ("Txell Deep_done.")

        call p_txell_blowjobDeep_done_label

        
    #jump afternight05_Pedrera_Sex_action
    return
    #call afternight05_Pedrera_Sex


###########################################################################
###########################################################################  DOGGY - MISSIONARY


label afternight05_Pedrera_Sex_p_txell_doggy:

    if p_prot.pos == "doggy":

        $ debug("Doggystyle Sex with Txell.")

        $ debug ("Doggystyle Sex with Txell.")

        $ p_txell_doggy_TRY += 1

    if p_prot.pos == "missionary":

        $ debug("Missionary Sex with Txell 02.")

        $ debug ("Missionary Sex with Txell 02.")

        $ p_txell_missionary_TRY += 1

################################################################################
############################################################ BUTTOCKS SLAP

    if p_prot.b_action == "buttocks_slap":

        if p_neus.buttocks_pain > 5:

            $ p_txell.buttocks_pain_received += 1

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            with hpunch

            if randomnum_1to5 == 1:

                tx "{size=35}¡¡AUUH!!{/size}"

            elif randomnum_1to5 == 2:

                tx "{size=35}¡¡AUUCH!!{/size}"

            elif randomnum_1to5 == 3:

                tx "{size=35}¡¡OUUCH!!{/size}"

            elif randomnum_1to5 == 4:

                tx "{size=35}¡¡AAIIH!!{/size}"

            elif randomnum_1to5 == 5:

                tx "{size=35}¡¡AAAUUUH!!{/size}"

            

            ###

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                tx "¡ESO ME HA DOLIDO!"

            elif randomnum_1to5 == 2:

                tx "¡QUE PARES YA!"

            elif randomnum_1to5 == 3:

                tx "¡DÉJAME EL CULO EN PAZ, HOMBRE!"

            elif randomnum_1to5 == 4:

                tx "¡AL FINAL ME VOY A ENFADAR DE VERDAD!"

            elif randomnum_1to5 == 5:

                tx "¡ME ESTÁ SUBIENDO LA MOSCA!"

            ###

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if buttocks_pain_received == 1:

                d "¡¿NO VES QUE ME LO ESTÁS DEJANDO ROJO?!"

            elif buttocks_pain_received == 2:

                d "¡DUELE!"

            elif buttocks_pain_received == 3:

                d "¡¿QUÉ ES LO QUE NO ENTIENDES?!"

            elif buttocks_pain_received == 4:

                d "¡ME ESTÁS DEJANDO EL CULO ROJO!"

            elif buttocks_pain_received == 5:

                d "¡SI TE TUBIERA EN MI CELDA AHORA MISMO...!"


        else:  # NO PAIN ON THE BUTTOCKS

            $ p_txell_buttocks_pain_received_from_p_prot += 1

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            with hpunch

            ono "splash{nw}{w=0.2}"

            if randomnum_1to5 == 1:

                d "¡Au...!"

            elif randomnum_1to5 == 2:

                d "¡Aiimm...!"

            elif randomnum_1to5 == 3:

                d "¡Auch...!"

            elif randomnum_1to5 == 4:

                d "¡Iaahmmm...!"

            elif randomnum_1to5 == 5:

                d "¡Auhmmm...!"

            
            ###

            if p_txell_buttocks_pain_received_from_p_prot == 1:

                tx "[protname]..."

                tx "No sabía yo que te pusiera cachondo azotar las nalgas de una mujer..."

                p "Supongo que no tanto como a ti."

                tx "Hmmm..."

                tx "Es posible que no."

            elif p_txell_buttocks_pain_received_from_p_prot > 1:

                $ randomnum_1to10 = renpy.random.randint(1, 10)

                if randomnum_1to10 == 1:

                    tx "Eres un cabronazo con suerte..."

                elif randomnum_1to10 == 2:

                    tx "¿Eso te la pone dura?..."

                elif randomnum_1to10 == 3:

                    tx "Te gusta azotarme, ¿verdad?"

                elif randomnum_1to10 == 4:

                    tx "Eres un..."

                elif randomnum_1to10 == 5:

                    tx "Hmmm..."

                elif randomnum_1to10 == 6:

                    tx "No te pases demasiado..."

                elif randomnum_1to10 == 7:

                    tx "Dame más fuerte..."

                elif randomnum_1to10 == 8:

                    tx "Esa ha dolido..."

                elif randomnum_1to10 == 9:

                    tx "Hmmm..."

                elif randomnum_1to10 == 10:

                    tx "Joder..."


                if p_txell.b_action in ["vaginal_received", "vaginalDeep_received"]:

                    if randomnum_1to5 == 1:

                        tx "Azótame lo que quieras,"

                        tx "Pero sigue dándole duro..."

                    elif randomnum_1to5 == 2:

                        tx "Hmmm..."

                        p "Te gusta,"

                        extend " ¿Verdad?"

                        tx "No voy a negar una evidencia."

                        p "Hmm..."

                    elif randomnum_1to5 == 3:

                        tx "¿Me quieres dejar las nalgas rojas?"

                        p "Me gusta oírte gemir así."

                        tx "Vas aprendiendo..."

                        p "¿Quien está aprendiendo aquí?"

                        tx "Hmmm..."

                    elif randomnum_1to5 == 4:

                        tx "Hmmm..."

                    elif randomnum_1to5 == 5:

                        p "Reconoce que te gusta."

                        tx "¿Cuando te he dicho lo contrario?"

                else:

                    if randomnum_1to5 == 1:

                        tx "Si me quieres azotar,"

                        extend " hazlo..."

                        tx "Pero no dejes de jugar con tu entrepierna,"

                        tx "recuerda que estamos a contra-reloj."

                    elif randomnum_1to5 == 2:

                        if p_txell.vaginal_received > 0:

                            tx "¿Volverás a follarme?,"

                            extend " semental..."

                            if p_txell.action in ["anal_received", "analDeep_received"]:

                                p "Pero si es lo que estoy haciendo."

                                tx "Ya sabes a por dónde me refiero..."

                                p "..."

                        else:

                            tx "Creo que se te está poniendo más dura,"

                            extend " no crees?"

                    elif randomnum_1to5 == 3:

                        tx "¿Disfrutas más azotándome o follándome?"

                        p "Quizás ambas."

                        tx "Pues no lo estoy notando..."

                        pt "Será zorra..."

                    elif randomnum_1to5 == 4:

                        tx "Mañana no me podré sentar por tu culpa."

                        p "Seguro que tampoco sueles parar cuando te dicen esto a ti, ¿Verdad?"

                        tx "..."

                        tx "Hmm..."

                    elif randomnum_1to5 == 5:

                        tx "Hmmm..."

                    ##

                    if p_txell.action in ["anal_received", "analDeep_received"]:

                        if randomnum_1to5 == 1:

                            p "¿No te gusta que te dé por detrás?"

                            tx "¿He mencionado en algún momento que me disguste?"

                        elif randomnum_1to5 == 2:

                            tx "Estás hecho un cerdo, [protname]..."

                            pt "Como si tú no estuvieras disfrutando..."

                            tx "Hmmm..."

                        elif randomnum_1to5 == 3:

                            if p_txell.action == "anal_received":

                                if p_txell.anal_pain_received == 0:

                                    tx "Podrías intentar metérmela más adentro..."

                                    pt "¿No se me va a quejar?"

                                else:

                                    tx "Así se siente bien..."

                                    tx "pero intenta no volver a metérmela entera tan bruscamente..."

                            elif p_txell.action == "analDeep_received":

                                tx "HMMMm..."

                                pt "Es increíble que siendo lesbiana le quepa entera por detrás."

                                pt "A saber con qué tipo de juguetes jugara esta zorra en su... \"celda\"..."

                        elif randomnum_1to5 == 4:

                            tx "¿Te gusta mi trasero,"

                            extend " ¿verdad?"

                        elif randomnum_1to5 == 5:

                            tx "Sigue así..."


                p "..."

        $ p_prot.b_action = "rest"


################################################################################
############################################################ KISS


    if p_prot.b_action == "kiss_TRY":

        $ debug ("Kiss with TXELL??")

        $ p_prot.b_action = "rest"


################################################################################
############################################################ REST

    if p_txell.action == "rest" and p_txell.b_action == "rest":

        pass

        $ debug ("ERROR? 154985")

    #call p_prot_previousSex

    return


label afternight05_Pedrera_Sex_p_txell_missionary:

    $ debug ("Missionary Sex with Txell.")

    call afternight05_Pedrera_Sex_p_txell_doggy

    return

label afternight05_Pedrera_Sex_p_txell_69:

    # If she didn't sucked you cock on minigame, she has repairs here to suck yours.

    $ p_txell.pos_69 += 1
    $ p_prot.pos_69 += 1

    if p_txell.pos_69 == 1:

        scene bg dark_a_blurry_02:
            truecenter

        show gensex_69_R_pussy_full_d:
            subpixel True
            truecenter
            zoom 0.5
            ypos 1.2
            easein_quad 10.0 ypos 0.5

    else:
        if p_prot.action == "rest" and p_txell.action == "rest":
            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            $ ped_sex_general_action_Cond = "69_00_00"
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk
            with Dissolve(0.3)

    $ debug ("69 Sex with Txell.")

    if p_txell_blowjob_done_ACCEPTED == True and p_prot.action == "cunnilingus_done" and p_prot.b_action not in ["blowjobDeep_received_TRY", "blowjobDeep_received", "takeDickOut"]:

        # Did you take off your dick from her mouth. NOT FINISHED

        # You're licking her pussy.

        if p_txell.throat_pain > 0:

            ## pass because, she doesn't have problems with that.

            pass

        else:

            # "It goes through here first, why?" # Because This goes first.

            #call p_txell_oral_done_label # wtf ... not sure if it needs to go here... necessary? at all?

            $ p_txell.blowjobDeep_received_FAILED_temp = 0

            $ debug ("Txell can suck your cock.")

######## ########

            if p_prot.b_action == "blowjob_received_TRY":

                $ ped_sex_general_expression_Cond = "talk"
                if p_txell.blowjob_done_TRY == 1:
                    $ ped_sex_general_action_b_Cond = "69b_00_01"
                elif p_txell.blowjob_done_TRY == 2:
                    $ ped_sex_general_action_b_Cond = "69b_00_02"
                elif p_txell.blowjob_done_TRY == 3:
                    $ ped_sex_general_action_b_Cond = "69b_00_03"
                elif p_txell.blowjob_done_TRY == 4:
                    $ ped_sex_general_action_b_Cond = "69b_00_04"
                else:
                    $ ped_sex_general_action_b_Cond = "69b_00_05"

                call pedrera_sex_p_general_talk

                progcheck "You're trying to put your dick in her mouth."

                if p_prot.b_action == "blowjob_received_TRY" and takeDickOut_Cond > 0:

                    $ p_txell.takeDickOutTimes += 1

                    #$ takeDickOut_TxellTimes += 1

                    $ takeDickOut_Cond = 0

                    if p_prot.pos == "69":
                        show gensex_69_L_d_mouth sadbiting_Silentx02
                        with dissolve

                    tx "Hmmm..."

                    if p_prot.pos == "69":

                        $ ped_check_1_5("ped_69_blowjob_receivedAgain_txell_01_list")

                        if ped_check_list_result == 1:

                            show gensex_69_L_d_mouth sad_Talkingx03
                            with dissolve

                            tx "Será mejor que te decidas..."

                            show gensex_69_L_d_mouth happy_Talkingx03
                            with dissolve

                            tx "¿O es que quieres que tenga otro orgasmo con tu lengua antes de que tú termines?"

                            show gensex_69_L_d_mouth happybiting_Silentx03
                            with dissolve

                        elif ped_check_list_result == 2:

                            tx "¿Ahora quieres que te la chupe de nuevo?"

                        elif ped_check_list_result == 3:

                            tx "Sabes lo bien que la chupo y por eso intentas evitar mi lengua..."
                            
                        elif ped_check_list_result == 4:

                            tx "¿Intentas que tenga otro orgasmo?"
                            
                        elif ped_check_list_result == 5:

                            tx "No quieres hacer enfadar a Neus, ¿verdad?"
                            
                        else:

                            tx "..."

                $ p_prot.b_action = "blowjob_received_PROCESS"

######## ########

            if p_prot.b_action in ["blowjob_received", "blowjobDeep_received", "blowjob_received_PROCESS"]:

                if p_prot.b_action in ["blowjob_received", "blowjobDeep_received"]:

                    $ randomnum_1to5 = renpy.random.randint(1, 5)

                    if randomnum_1to5 == 1:

                        p "¡Ugh...!"

                    elif randomnum_1to5 == 2:

                        p "¡Humm...!"

                    elif randomnum_1to5 == 3:

                        p "¡Ahhm...!"

                    elif randomnum_1to5 == 4:

                        p "¡Uhm...!"

                    elif randomnum_1to5 == 5:

                        p "¡Mm...!"

                $ p_txell.blowjob_done += 1
                $ p_prot.blowjob_received += 1
                $ p_txell.throat_dilatation += 1

                
                $ p_prot.cunnilingus_done += 1
                $ p_txell.cunnilingus_received += 1
                $ p_txell.cunnilingus_missionary_received += 1

                $ p_txell.vaginal_dilatation += 1

                $ p_txell.action = "blowjob_done"
                $ p_prot.b_action = "blowjob_received"

                call ped_sex_69_mc_lickpussy01
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                

                if p_txell.blowjob_done == 2:

                    p "Pengsaba gue habías dicho gue eras toda una experta en la feglación magculina..."

                    tx "..."

                    #$ ped_sex_general_69_cover = "over"
                    $ ped_sex_general_expression_Cond = "talk"
                    #$ ped_sex_general_action_Cond = "69_00_00"
                    $ ped_sex_general_action_b_Cond = "69b_00_00"
                    call pedrera_sex_p_general_talk

                    show gensex_69_L_d_mouth happy_Talkingx02
                    with Dissolve(0.5)

                    tx "Así que esas tenemos..."

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Voy a abrir la boca,"

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "y veamos lo profundo que llegas,"

                    show gensex_69_L_d_mouth happy_Talkingx06
                    with dissolve

                    tx "¿de acuerdo?"

                    show gensex_69_L_d_mouth happy_Silentx05
                    with dissolve

                    p "Lo digces en..."

                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve

                    tx "¿No te atreves?"

                    show gensex_69_L_d_mouth happy_Silentx07
                    with dissolve

                    p "Luego no te me guejes."

                    show gensex_69_L_d_mouth happy_Talkingx06
                    with dissolve

                    tx "Desde luego que..."

                    $ p_txell_blowjobDeep_done_ACCEPTED = True

                    $ p_txell.blowjobDeep_received += 1
                    $ p_prot.blowjobDeep_done += 1
                    $ p_txell.throat_dilatation += 1

                    $ p_prot.b_action = "blowjobDeep_received"
                    $ p_txell.action = "blowjobDeep_done"

                    $ ped_sex_general_expression_Cond = ""

                    $ ped_sex_general_expression_Cond = ""
                    $ ped_sex_general_action_b_Cond = "69b_04_01"
                    call pedrera_sex_p_general_talk
                    with Dissolve(0.5)

                    pt "¡Dios!"

                else:

                    ##takeDickOut_Cond
                    ##takeDickOut_m_Total
                    if takeDickOut_Cond > 0:

                        $ ped_check_1_5("ped_oral_notreceived_txell_01_list")

                        
                        show gensex_69_L_d_mouth sadbiting_Silentx04
                        with dissolve

                        tx "Hmmmm..."

                        if ped_check_list_result in range(1,6):
                            show gensex_69_L_d_mouth sad_Talkingx04
                        else:
                            show gensex_69_L_d_mouth sad_Silentx03
                        with dissolve

                        if ped_check_list_result == 1:

                            tx "Si no la tengo en mi boca es por que no quieres,"

                            show gensex_69_L_d_mouth sad_Talkingx004
                            with dissolve

                            tx "que quede claro..."

                        elif ped_check_list_result == 2:

                            tx "Agradezco que me quieras pasar la lengua por ahí abajo,"

                            show gensex_69_L_d_mouth sad_Talkingx004
                            with dissolve

                            tx "pero te recuerdo que no tenemos toda la noche..."

                        elif ped_check_list_result == 3:

                            tx "Así que prefieres no correrte tan pronto..."

                        elif ped_check_list_result == 4:

                            tx "Si no quieres que te la chupe,"

                            show gensex_69_L_d_mouth sad_Talkingx004
                            with dissolve

                            tx "¿cuál es tu plan?"

                        elif ped_check_list_result == 5:

                            tx "Cualquiera diría que tienes miedo de correrte demasiado pronto..."

                        else:
                            tx "..."

                        show gensex_69_L_d_mouth sadbiting_Silentx02
                        with dissolve

                    else:

                        $ ped_check_1_5("ped_cunnilingus_blowjob_txell_list_01")

                        if ped_check_list_result == 1:

                            #$ ped_sex_general_69_cover = "over"
                            $ ped_sex_general_expression_Cond = "talk"
                            #$ ped_sex_general_action_Cond = "69_00_00"
                            $ ped_sex_general_action_b_Cond = "69b_00_00"
                            call pedrera_sex_p_general_talk

                            show gensex_69_L_d_mouth happy_Talkingx05
                            with Dissolve(0.5)

                            tx "Ahora sí."

                            show gensex_69_L_d_mouth happy_Silentx06
                            with dissolve

                            n "Sientes que te agarra de las nalgas y te empuja para que vuelvas a metérsela en la garganta."

                        $ p_txell.blowjobDeep_received += 1
                        $ p_prot.blowjobDeep_done += 1
                        $ p_txell.throat_dilatation += 1

                        $ p_prot.b_action = "blowjobDeep_received"
                        $ p_txell.action = "blowjobDeep_done"

                        $ ped_sex_general_expression_Cond = ""

                        $ ped_sex_general_expression_Cond = ""
                        $ ped_sex_general_action_b_Cond = "69b_04_01"
                        call pedrera_sex_p_general_talk
                        with Dissolve(0.5)

                        pt "¡Dios!"

                        n "Apenas sin resistencia logra metérsela por completo de nuevo."


            else:

                # She is not sucking your cock and you're trying to put your dick in her mouth // She HAD AN ORGASM at least.

                #progcheck "What the fuck is happening here?"

                # $ p_txell.blowjob_done += 1
                # $ p_prot.blowjob_received += 1
                # $ p_txell.throat_dilatation += 1

                
                $ p_prot.cunnilingus_done += 1
                $ p_txell.cunnilingus_received += 1
                $ p_txell.cunnilingus_missionary_received += 1

                $ p_txell.vaginal_dilatation += 1

                #$ p_prot.action = "cunnilingus_done" ## Not necessary.
                #$ p_txell.b_action = "cunnilingus_received" # Not necessary.

                call ped_sex_69_mc_lickpussy01
                $ ped_sex_general_69_cover = "dissolve"
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                $ randomnum_1to5 = renpy.random.randint(1, 5)

                show gensex_69_L_d_mouth happybiting_Silentx06
                with dissolve

                if randomnum_1to5 == 1:

                    tx "¡Hmmm...!"

                elif randomnum_1to5 == 2:

                    tx "¡Hmfh...!"

                elif randomnum_1to5 == 3:

                    tx "¡Uhgh...!"

                elif randomnum_1to5 == 4:

                    tx "¡Ghhm...!"

                elif randomnum_1to5 == 5:

                    tx "¡Ughm...!"

                if (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 1:

                    $ ped_times_1_5("ped_cunnilingus_AfOrg_Again_txell_list_01")

                    if ped_check_list_result in range(1,6):
                        show gensex_69_L_d_mouth happy_Talkingx03

                    else:
                        show gensex_69_L_d_mouth happybiting_Silentx04

                    with dissolve

                    if ped_check_list_result == 1:

                        tx "Ya veo..."

                        show gensex_69_L_d_mouth sad_Talkingx002
                        with dissolve

                        tx "Así que intentas darme otro orgasmo antes de que yo te haga terminar..."

                        show gensex_69_L_d_mouth happy_Talkingx04
                        with dissolve

                        tx "Agradezco tu interés,"

                        show gensex_69_L_d_mouth happy_Talkingx02
                        with dissolve

                        tx "pero me temo que no lo conseguirás."

                    elif ped_check_list_result == 2:

                        tx "Puedes esforzarte tanto cuanto quieras..."

                    elif ped_check_list_result == 3:

                        tx "Necesitas más años de experiencia para lograr que tenga otro orgasmo..."

                    elif ped_check_list_result == 4:

                        tx "Aprecio tu esfuerzo,"

                        show gensex_69_L_d_mouth happy_Talkingx02
                        with dissolve

                        tx "pero desgraciadamente será en vano."

                    elif ped_check_list_result == 5:

                        tx "El simple hecho de que no me la dejes chupar,"

                        show gensex_69_L_d_mouth happy_Talkingx04
                        with dissolve

                        tx "ya demuestra la poca confianza que tienes con tu habilidad con la lengua."

                    else:

                        pass

                elif (p_txell.orgasm - p_didac_cunnilingus_p_txell_orgasm) == 2:

                    $ ped_times_1_5("ped_cunnilingus_AfOrg_Again_txell_list_02")

                    if ped_check_list_result in range(1,6):
                        show gensex_69_L_d_mouth happy_Talkingx03

                    else:
                        show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                    if ped_check_list_result == 1:

                        tx "¿Intentas que tenga un tercer orgasmo?"

                    elif ped_check_list_result == 2:

                        tx "La verdad es que no esperaba que me dieras dos orgasmos..."

                    elif ped_check_list_result == 3:

                        tx "Al final tendré que cambiar mi opinión sobre ti..."

                    elif ped_check_list_result == 4:

                        tx "Admito que tienes una gran habilidad con tu lengua."

                    elif ped_check_list_result == 5:

                        tx "No pares..."

                    else:

                        pass

                else:

                    $ ped_times_1_5("ped_cunnilingus_AfOrg_Again_txell_list_03")

                    if ped_check_list_result in range(1,6):
                        show gensex_69_L_d_mouth happy_Talkingx10

                    else:
                        show gensex_69_L_d_mouth happybiting_Silentx08
                    with dissolve

                    if ped_check_list_result == 1:

                        tx "¡Dios!"

                    elif ped_check_list_result == 2:

                        tx "¿Cuántos orgasmos llevo ya?"

                    elif ped_check_list_result == 3:

                        tx "¡Al final conseguirás que tenga otro orgasmo!"

                    elif ped_check_list_result == 4:

                        tx "Reconozco que te he juzgado mal..."

                    elif ped_check_list_result == 5:

                        tx "Por lo que más quieras..."

                        show gensex_69_L_d_mouth happy_Talkingx08
                        with dissolve

                        tx "¡no pares!"

                    else:

                        tx "¡Hmmm...!"


                show gensex_69_L_d_mouth happybiting_Silentx04
                with dissolve

                #call afternight05_Pedrera_n_Neus_Warning # This is when Neus is fucking you.
                call afternight05_Pedrera_Neus_Warning


    elif p_prot.b_action in ["blowjobDeep_received_TRY", "blowjobDeep_received"] and p_prot.action == "cunnilingus_done":

        $ debug("You try DEEPTHROAT her throat IN 69")

        if p_txell.throat_dilatation >= 0:

            $ debug("She has a good throat dilatation.")

            $ p_txell.blowjobDeep_received += 1
            $ p_prot.blowjobDeep_done += 1
            $ p_txell.throat_dilatation += 1

            $ p_prot.b_action = "blowjobDeep_received"
            $ p_txell.action = "blowjobDeep_done"

            $ ped_sex_general_expression_Cond = ""

            if p_txell.blowjobDeep_received >= 5:
                $ ped_sex_general_action_b_Cond = "69b_04_05"
            elif p_txell.blowjobDeep_received == 4:
                $ ped_sex_general_action_b_Cond = "69b_04_04"
            elif p_txell.blowjobDeep_received == 3:
                $ ped_sex_general_action_b_Cond = "69b_04_03"
            elif p_txell.blowjobDeep_received == 2:
                $ ped_sex_general_action_b_Cond = "69b_04_02"
            else:
                $ ped_sex_general_action_b_Cond = "69b_04_01"


            call pedrera_sex_p_general_talk

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 == 1:

                p "¡Hmmm...!"

            elif randomnum_1to5 == 2:

                p "¡Hmfh...!"

            elif randomnum_1to5 == 3:

                p "¡Uhgh...!"

            elif randomnum_1to5 == 4:

                p "¡Ghhm...!"

            elif randomnum_1to5 == 5:

                p "¡Ughm...!"


            $ debug("You succeded doing a deepthroat to Didac: " + str(p_txell.blowjobDeep_received))

            if p_txell.blowjobDeep_received == 1: # Did he done it in oral?

                n "Con cierta suavidad,"

                n "consigue introducirse tu falo entero en el interior de su garganta."

            elif p_txell.blowjobDeep_received == 2:

                n "Sin apenas resistencia,"

                n "logra aumentar ligeramente el ritmo sin que le den arcadas."

            elif p_txell.blowjobDeep_received > 2:

                $ ped_check_1_10("ped_blowjobDeep_txell_list")

                if ped_check_list_result == 1:

                    pt "Como siga así,"

                    extend " no tardaré mucho en terminar..."

                elif ped_check_list_result == 2:

                    pt "Es impresionante que pueda seguir sin tener que parar para respirar..."

                elif ped_check_list_result == 3:

                    pt "Será la jodida reina de las engreídas,"

                    pt "¡pero no se puede negar que la tía es buena!"

                elif ped_check_list_result == 4:

                    pt "¡Parece una maldita aspiradora de la forma que me succiona!"

                elif ped_check_list_result == 5:

                    pt "¡¿Cuantas pollas habrá mamada para hacerlo así de bien?!"

                elif ped_check_list_result == 6:

                    pt "¡Que buena es la muy puta!"

                elif ped_check_list_result == 7:

                    if KnowTxellwasEscort_Cond:

                        pt "¡No me extraña que tuviera tantos clientes!"

                    else:

                        pt "¡¿Con qué clase de juguetes habrá jugado esta tía para tener esta experiencia siendo lesbiana?!"

                elif ped_check_list_result == 8:

                    pt "¡Esta tía tiene de lesbiana,"

                    extend " lo que tengo yo de {a=https://es.wikipedia.org/wiki/Eunuco}eunuco{/a}!"

                elif ped_check_list_result == 9:

                    pt "¡Como siga así,"

                    extend " me voy a quedar sin polla!"

                elif ped_check_list_result == 10:

                    pt "¡Como siga así,"

                    extend " Neus se va a quedar sin esperma!"

                else:

                    "¡Joder!"


    elif p_prot.b_action == "blowjob_received_TRY" and p_prot.action != "takeTongueOut":
    #elif p_txell_blowjob_done_ACCEPTED == False and p_prot.pos_69_rest > 0:
    #elif p_prot.b_action == "blowjob_received_TRY" and p_didac.action != "blowjob_done": #Wich means your dick is still not inside her mouth, but you're trying.

        $ p_txell.blowjob_done_TRY +=1

        $ p_prot.b_action = "rest"

        #if p_txell_blowjob_done_ACCEPTED == False: # I think this one is not really necessary, since is not gonna be called here.

        #$ ped_sex_general_action_Cond = "69_00_00"
        $ ped_sex_general_expression_Cond = "talk"
        if p_txell.blowjob_done_TRY == 1:
            $ ped_sex_general_action_b_Cond = "69b_00_01"
        elif p_txell.blowjob_done_TRY == 2:
            $ ped_sex_general_action_b_Cond = "69b_00_02"
        elif p_txell.blowjob_done_TRY == 3:
            $ ped_sex_general_action_b_Cond = "69b_00_03"
        elif p_txell.blowjob_done_TRY == 4:
            $ ped_sex_general_action_b_Cond = "69b_00_04"
        else:
            $ ped_sex_general_action_b_Cond = "69b_00_05"

        call pedrera_sex_p_general_talk

        if p_txell_blowjob_done_ACCEPTED == True:

            $ debug ("She will not suck your dick if you don't lick her pussy.")

            show gensex_69_L_d_mouth sad_Silentx02
            with dissolve

            tx "..."

            $ ped_check_1_10("ped_oral_notreceived_txell_01_list")

            if ped_check_list_result in range(1,11):
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

            if ped_check_list_result == 1:

                tx "Sigo sin sentir tu lengua en mi entrepierna."

            elif ped_check_list_result == 2:

                tx "Creo que he sido bastante clara."

            elif ped_check_list_result == 3:

                tx "Sin usar tu lengua..."

            elif ped_check_list_result == 4:

                tx "Sigo sin sentir nada en mi entrepierna..."

            elif ped_check_list_result == 5:

                tx "Y sigues sin usar tu lengua..."

            elif ped_check_list_result == 6:

                tx "¿Tanto te cuesta usar tu lengua antes de restregarme tu entrepierna por mi rostro?"

            elif ped_check_list_result == 7:

                tx "¿Es que se te ha cansado la lengua?"

            elif ped_check_list_result == 8:

                tx "¿Es que un gato se te ha comido la lengua?"

            elif ped_check_list_result == 9:

                tx "En lugar de hablar deberías estar haciendo algo más con tu lengua."

            elif ped_check_list_result == 10:

                tx "¿Tan poco aguantáis los hombres usando vuestra lengua?"

            if ped_check_list_result in range(1,11):
                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

            $ ped_check_1_10("ped_oral_notreceived_txell_02_list")

            if ped_check_list_result == 1:

                tx "Que lamentable."

            elif ped_check_list_result == 2:

                tx "Creo que he sido bastante clara."

            elif ped_check_list_result == 3:

                tx "Tu manera de intentar convencerme es es deplorable."

            elif ped_check_list_result == 4:

                tx "He visto perros que saben pedirlo mejor."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

                pt "¿Qué le pasa a esta con los perros?"

            elif ped_check_list_result == 5:

                tx "Eres lamentable."

            elif ped_check_list_result == 6:

                tx "Quizás es que ese es tu límite..."

            elif ped_check_list_result == 7:

                tx "Me apiado de las mujeres con las que has estado."

            elif ped_check_list_result == 8:

                tx "Eres tan básico..."

            elif ped_check_list_result == 9:

                tx "¿Acaso crees que así me vas a convencer?"

            elif ped_check_list_result == 10:

                tx "Y yo que pensaba que habrías aprendido algo..."

            else:

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                tx "..."

            show gensex_69_L_d_mouth sad_Silentx03
            $ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk
            with dissolve
            
            call afternight05_Pedrera_Neus_Warning

        else:

            if p_txell.orgasm > p_didac_cunnilingus_p_txell_orgasm and p_txell.orgasm > 0 and p_prot.action == "cunnilingus_done":

                if p_txell.blowjob_done_TRY == 1:

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    n "Sugerentemente,"

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    n "mueves tus caderas para intentar acercar el glande de tu miembro"

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    n "a sus carnosos labios."

                show gensex_69_L_d_mouth sadbiting_Silentx02
                with dissolve

                p "¿Acago no te gugta lo gue egtoy hagciendo gon la lengua."

                show gensex_69_L_d_mouth sadbiting_Silentx03
                with dissolve

                p "¿O digás gue no has disfgutado del oggasmo que hag tenido...?"

                if p_didac_cunnilingus_p_txell_orgasm > 0:

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Lo dices como si Dídac no te hubiera ayudado..."

                else:

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    tx "Hmmm..."

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Supongo que no eres inútil como pensaba..."

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "Aunque en verdad,"

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                tx "he estado con perros que lo hacen mucho mejor."

                show gensex_69_L_d_mouth happy_Silentx03
                with dissolve

                pt "¡¿Cómo dice?!"

                $ p_txell_blowjob_done_ACCEPTED = True

                call p_txell_oral_done_label
            

            elif p_txell.blowjob_done_TRY == 1: # Not suck your dick yet, even if she did.

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

                n "Sugerentemente,"

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

                n "mueves tus caderas para intentar acercar el glande de tu miembro"

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                n "a sus carnosos labios."

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "¿Puedo saber qué intentas hacer?"

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

                p "¿No es obvio?"

                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                tx "Demasiado."

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "¿No has elegido esta postura para lamerme la entrepierna?"

                if p_prot.action == "cunnilingus_done":

                    show gensex_69_L_d_mouth sad_Talkingx001
                    with dissolve

                    tx "Pues sigue."

                else:

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "Porque no siento que uses tu lengua."

                if p_txell.blowjob_done == 0:

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    p "¿Por qué no lo intentas?"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "¿Acaso crees que es por falta de experiencia?"

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    p "Creía que habías dicho que eras lesbiana."

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Mi \"ex\" era {a=https://es.wikipedia.org/wiki/Transexualidad}transexual{/a}."

                    show gensex_69_L_d_mouth sad_Silentx01
                    with dissolve

                    p "¿Y la tenía tan grande como la mía?"

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    tx "..."

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "He llegado a meterme en la garganta juguetes sexuales que simulan un falo equino."

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Así que no es por falta de aptitudes que no me quiera meter la tuya."

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    p "Me lo haces dudar."

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "Sabes perfectamente que es una cuestión de falta de interés,"

                    extend " nada más."

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    p "..."

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "Puedes insistir tanto como quieras,"

                    show gensex_69_L_d_mouth happy_Talkingx06
                    with dissolve

                    tx "solo conseguirás ponerte aún más en ridículo."

                    show gensex_69_L_d_mouth happy_Silentx04
                    with dissolve

                    pt "Maldita zorra..."

                else:

                    show gensex_69_L_d_mouth sad_Silentx035
                    with dissolve

                    p "Bien que me la has estado chupando hasta ahora..."

                    show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                    tx "..."

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Supongo que tienes algo de razón."

                    show gensex_69_L_d_mouth sad_Talkingx05
                    with dissolve

                    tx "Pero tendrás que esforzarte mucho más que esto,"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "si quieres convencerme."

                    if p_prot.action == "cunnilingus_done":

                        show gensex_69_L_d_mouth sad_Talkingx003
                        with dissolve

                        tx "Aunque vas con buen camino si la sigues usando correctamente..."

                    else:

                        show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                        tx "Especialmente si no usas tu lengua."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    p "..."

            elif p_txell.blowjob_done_TRY > 1:

                $ ped_check_1_10("ped_69_oralTRY_FAILED_txell_list")
                # $ randomnum_1to10 = renpy.random.randint(1, 10)

                if ped_check_list_result == 1:

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Que refriegues tu polla por mis mejillas"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "como si fueras un mono en celo,"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "no logrará convencerme."

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "Para tu desgracia,"

                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve

                    tx "estoy a un eslabón superior en la evolución."

                    show gensex_69_L_d_mouth happy_Silentx06
                    with dissolve

                elif ped_check_list_result == 2:

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Que no entiendas algo tan básico,"

                    show gensex_69_L_d_mouth sad_Talkingx01
                    with dissolve

                    tx "es algo que realmente ya ni me sorprende de ti."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 3:

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "No siento que tu lengua se mueva"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "y sin embargo me pides que yo haga lo propio contigo..."

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "Toda una demostración de la inteligencia masculina..."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 4:

                    show gensex_69_L_d_mouth happy_Talkingx03
                    with dissolve

                    tx "Cuantos hombres desearían tener mi entrepierna delante de sus narices"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "y tú ni siquiera eres capaz de mover un dedo..."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 5:

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Lo triste,"

                    extend " es que ni me extraña que seas tan básico"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "como para no entender la función que tiene la posición del sesenta y nueve."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 6:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Ni siquiera eres capaz de mover tu lengua,"

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "¿Y quieres que lo haga yo?"

                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve

                    tx "¿Por quien me tomas?"

                    show gensex_69_L_d_mouth happy_Silentx04
                    with dissolve

                elif ped_check_list_result == 7:

                    show gensex_69_L_d_mouth sad_Talkingx004
                    with dissolve

                    tx "¿Te ha parecido que tuviera un orgasmo?"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Porque si te lo ha parecido,"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "me compadezco de las mujeres con las que habrás estado..."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 8:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "No sé qué es lo que entenderás por orgasmo,"

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "pero te informo de que aún no he tenido ni uno."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                elif ped_check_list_result == 9:

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "Desde luego,"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "no envidio a Neus con su gusto para los hombres..."

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                elif ped_check_list_result == 10:

                    show gensex_69_L_d_mouth sad_Talkingx02
                    with dissolve

                    tx "Eres más inútil que un vibrador sin pilas."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                else:

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    tx "..."

            if p_txell_blowjob_done_ACCEPTED == False:

                call afternight05_Pedrera_Neus_Warning

                $ ped_sex_general_action_b_Cond = "69b_00_00"
                call pedrera_sex_p_general_talk
                with dissolve

                $ p_prot.b_action = "rest" # This is necessary if you failed, Neus Warning.

    elif p_prot.action in ["rest", "takeDickOut", "takeTongueOut"] or p_prot.b_action in ["takeDickOut", "takeTongueOut"]:

        if p_prot.b_action in ["takeDickOut", "takeTongueOut"] or p_prot.action in ["takeDickOut", "takeTongueOut"]:

            call p_txell_notReceiveBlowjob

        elif p_prot.pos_69_rest == 0:

            #$ p_prot.restTurns += 1 # How many sequential times you did nothing.

            if p_txell.start == 1:

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

            show gensex_69_L_d_mouth happy_Talkingx04
            with Dissolve(0.2)

            tx "Así que decides tener mi entrepierna delante de tu cara..."

            show gensex_69_L_d_mouth sad_Silentx03
            with dissolve

            p "¿Preferirías que te pusiera a cuatro patas?"

            if p_txell.cunnilingus_received > 0:

                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                tx "Sabes que no."

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

            else:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "De hecho,"

                extend " estaba pensando si sabrás usar esa lengua tuya..."

                show gensex_69_L_d_mouth happy_Silentx03
                with dissolve

                pt "Desde luego,"

                extend " es zorra como ella sola..."

        elif p_prot.pos_69_rest == 1:

            show gensex_69_L_d_mouth sad_Talkingx02
            with dissolve

            tx "¿Te gusta tener mi coño en frente?"

            show gensex_69_L_d_mouth sadbiting_Silentx01
            with dissolve

            p "Es posible."

            show gensex_69_L_d_mouth sad_Talkingx03
            with dissolve

            tx "No voy a discutir tus gustos,"

            show gensex_69_L_d_mouth sad_Talkingx02
            with dissolve

            tx "pero estaría bien que hicieras algo más que mirar..."

            if p_txell.action == "blowjob_done":

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                tx "Porque desde luego,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "no te la voy a seguir chupando"

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "si no recibo nada a cambio."

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

            else:

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

                p "Tú también podrías hacer algo..."

                show gensex_69_L_d_mouth sad_Talkingx002
                with dissolve

                tx "Estás soñando si crees que voy a hacerte algo así,"

                show gensex_69_L_d_mouth happy_Talkingx02
                with dissolve

                tx "por tu cara bonita..."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

        elif p_prot.pos_69_rest > 1:

            $ ped_check_1_10("ped_69_rest_txell_list")

            $ ped_sex_general_69_cover = "over"
            $ ped_sex_general_expression_Cond = "talk"
            #$ ped_sex_general_action_Cond = "69_00_00"
            #$ ped_sex_general_action_b_Cond = "69b_00_00"
            call pedrera_sex_p_general_talk

            if ped_check_list_result == 1:

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "¿Qué motivo hay para que me hayas puesto encima?"

                show gensex_69_L_d_mouth happy_Talkingx05
                with dissolve

                tx "Creía que ibas a querer hacer un {a=https://es.wikipedia.org/wiki/69_(postura)}{i}soixante-neuf{/i}{/a}..."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

                p "¡¿Un qué?!"

                show gensex_69_L_d_mouth happy_Talkingx05
                with dissolve

                tx "Su primera mención explícita en un libro data de 1888 en Francia,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "de ahí que también se le conozca con su pronunciación en francés."

                show gensex_69_L_d_mouth happy_Silentx02
                with dissolve

                p "..."

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Pero no te recomiendo esta postura,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "es difícil que logres darme el más mínimo placer"

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "si me metiera tu polla en mi boca..."

                show gensex_69_L_d_mouth happy_Talkingx05
                with dissolve

                tx "si realmente me pusiera en serio,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "no serías capaz ni de mover la lengua."

                show gensex_69_L_d_mouth happy_Silentx05
                with dissolve

                pt "Esta mujer no tiene abuela,"

                extend " eso está claro..."

            elif ped_check_list_result == 2:

                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

                tx "Si pretendes que te haga algo..."

                if p_txell.cunnilingus_received == 0:

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Será mejor que empieces a usar esa lengua tuya"

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "para algo más que hablar."

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Porque estás soñando si crees que voy a metérmela en la boca."

                    if p_txell.orgasm == 0:

                        show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                        tx "Y menos sin haber tenido ni un solo orgasmo."

                else:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Será mejor que vuelvas a poner tu lengua ahí."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

            elif ped_check_list_result == 3:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "¿Preferirías que tuviera una polla de plástico?"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "Quizás así te animarías más a usar tu lengua..."

                show gensex_69_L_d_mouth happy_Silentx03
                with dissolve

                pt "Será zorra..."

                show gensex_69_L_d_mouth happy_Silentx04
                with dissolve

            elif ped_check_list_result == 4:

                show gensex_69_L_d_mouth sad_Talkingx003
                with dissolve

                tx "Estoy segura que te gusta lo que ves..."

                if p_txell.orgasm == 0:

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "Lo que pasa es que tienes miedo de defraudarme."

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "Tranquilo,"

                    extend " es difícil que puedas decepcionarme,"

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "tampoco espero nada de ti."

                    show gensex_69_L_d_mouth happy_Silentx04
                    with dissolve

                elif p_txell.orgasm == 1:

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Después de todo,"

                    extend " has logrado que tenga un orgasmo..."

                    show gensex_69_L_d_mouth sad_Talkingx03
                    with dissolve

                    tx "No negaré que me ha sorprendido,"

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "al fin y la cabo tampoco me esperaba nada de ti..."

                    show gensex_69_L_d_mouth happy_Silentx03
                    with dissolve

                elif p_txell.orgasm >= 2:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Al fin y al cabo has logrado que tenga [p_txell.orgasm] orgasmos..."

                    if p_didac_cunnilingus_p_txell_orgasm > 0: # it must be changed.

                        show gensex_69_L_d_mouth happy_Talkingx04
                        with dissolve

                        tx "Aunque en realidad [p_didac_cunnilingus_p_txell_orgasm] de ellos me lo has otorgado Dídac,"

                        extend " y no tú..."

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "Es mucho más de lo que me esperaba."

                    show gensex_69_L_d_mouth happy_Silentx03
                    with dissolve

                if p_txell.orgasm < 2:

                    pt "Será hija de..."

            elif ped_check_list_result == 5:

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Soy consciente de que tengo una vagina hermosa,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "pero tampoco hace falta que te quedes patidifuso sin mover un músculo observándola."

                show gensex_69_L_d_mouth happy_Silentx03
                with dissolve

            elif ped_check_list_result == 6:

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Si tanto te fascina mi entrepierna,"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "luego puedes hacerle una foto y enmarcarla en tu habitación."

                show gensex_69_L_d_mouth happy_Talkingx06
                with dissolve

                tx "Al fin y al cabo no sería la primera vez que lo expongo artísticamente en una galería..."

                show gensex_69_L_d_mouth happy_Silentx05
                with dissolve

                pt "¿Por qué será que no me sorprende?"

            elif ped_check_list_result == 7:

                show gensex_69_L_d_mouth sad_Talkingx004
                with dissolve

                tx "Al final pensaré que tengo el mismo efecto que Medusa volviendo a los hombres en piedra,"

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                tx "aunque desde luego,"

                show gensex_69_L_d_mouth happy_Talkingx05
                with dissolve

                tx "lo que suele volverse de piedra primero"

                show gensex_69_L_d_mouth happy_Talkingx06
                with dissolve

                tx "suele ser su miembro viril..."

                show gensex_69_L_d_mouth happy_Silentx05
                with dissolve

                pt "Dirá lo que quiera..."

                pt "pero es una zorra como la copa de un pino."

            elif ped_check_list_result == 8:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "He aceptado tenerte encima porque creía que harías algo..."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

            elif ped_check_list_result == 9:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "La verdad es que no decepcionas."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

            elif ped_check_list_result == 10:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "¿Por qué será que os cuesta tanto a los hombres usar vuestra lengua?"

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Especialmente teniendo en cuenta cuanto os gusta que lo hagamos nosotras..."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

            else:

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                tx "..."

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

        $ p_txell.action = "rest"
        $ p_txell.b_action = "rest"
        
        call afternight05_Pedrera_Neus_Warning

    ##

    elif p_prot.action == "cunnilingus_done" and p_prot.b_action not in ["takeDickOut", "takeTongueOut"]: # 69

        $ debug("MC Licking TXELL pussy")

        $ p_prot.cunnilingus_done += 1
        $ p_txell.cunnilingus_received += 1
        $ p_txell.cunnilingus_69_received += 1
        #$ p_txell_cunnilingus_received_from_p_prot_at_69 += 1

        $ p_txell.vaginal_dilatation += 1

        $ ped_sex_general_69_cover = "over"
        #$ ped_sex_general_expression_Cond = ""

        call ped_sex_69_mc_lickpussy01

        #$ ped_sex_general_action_b_Cond = "69b_01_01"
        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

        pause 3.0/ped_sex_num

        ##

        $ ped_check_1_10("ped_69_cunnilingus_moan_txell_list")
        #$ randomnum_1to10 = renpy.random.randint(1, 10)

        if ped_sex_general_expression_Cond == "talk":

            if ped_check_list_result not in range(1,11):
                show gensex_69_L_d_mouth happybiting_Silentx05

            elif ped_check_list_result in range(1, 7):
                show gensex_69_L_d_mouth happybiting_Silentx05

            elif ped_check_list_result == 7:
                show gensex_69_L_d_mouth sad_Talkingx005
                
            else:
                show gensex_69_L_d_mouth sad_Talkingx04

            with Dissolve(0.3)


        if ped_check_list_result == 1:

            tx "Hhmm..."

        elif ped_check_list_result == 2:

            tx "Hfhm..."

        elif ped_check_list_result == 3:

            tx "Mhmm..."

        elif ped_check_list_result == 4:

            tx "Hfmm..."

        elif ped_check_list_result == 5:

            tx "Hfm..."

        elif ped_check_list_result == 6:

            tx "Hmm..."

        elif ped_check_list_result == 7:

            tx "Ouhm..."

        elif ped_check_list_result == 8:

            tx "Ahfhm..."

        elif ped_check_list_result == 9:

            tx "A-ahm..."

        elif ped_check_list_result == 10:

            tx "Ahfm..."

        else:

            tx "¡Hmmmm...!"

        if ped_sex_general_expression_Cond == "talk":
            show gensex_69_L_d_mouth sadbiting_Silentx06
            with dissolve

        ##

        # if p_txell_blowjob_done_ACCEPTED == True: # Txell sucking your cock.

        #     $ p_prot.b_action = "blowjob_received" # Is this one really necessary here?

        #     $ debug ("You receive Didac blowjob while you're licking her pussy (MOUTH FULL BOTH).")

        #     call p_txell_cunnilingus_received_label

        #     call WIP

        if p_txell_blowjob_done_ACCEPTED == False:

            $ debug ("You're licking her pussy.")

            if p_txell.cunnilingus_69_received == 1:

                show gensex_69_L_d_mouth sadbiting_Silentx02
                with dissolve

                n "Agarrándote con firmeza a sus nalgas,"

                n "desciendes la cabeza para acercar tu mandíbula a sus labios menores."

                show gensex_69_L_d_mouth sadbiting_Silentx05
                with dissolve

                tx "Ughh..."

                show gensex_69_L_d_mouth sadbiting_Silentx04
                with dissolve

                n "Con suavidad,"

                $ ped_sex_general_69_cover = "over"
                $ ped_sex_general_action_Cond = "69_01_01"
                call pedrera_sex_p_general_talk
                with Dissolve(1.0)

                show gensex_69_L_d_mouth sadbiting_Silentx03
                with dissolve

                n "deslizas superficialmente tu lengua a lo largo y ancho de la tierna piel"

                n "que cubre su cálida entrepierna."

                show gensex_69_L_d_mouth sadbiting_Silentx02
                with dissolve

                n "Inevitablemente,"

                n "empiezas a saborear el cálido y ligeramente viscoso jugo vaginal que emana de su interior."

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                if p_prot_NotJustMasturbate_with_p_txell:

                    tx "¿Intentas ser más persuasivo usando finalmente tu lengua?"

                else:

                    tx "¿Intentas ser más persuasivo usando tu lengua?"


                show gensex_69_L_d_mouth sadbiting_Silentx05

                $ ped_sex_general_69_cover = "dissolve"
                $ ped_sex_general_action_Cond = "69_01_01"
                call pedrera_sex_p_general_talk
                with vpunch

                tx "¡Mmm...!"

                show gensex_69_L_d_mouth happy_Silentx03
                with Dissolve(0.5)

                tx "Hmm..."

                show gensex_69_L_d_mouth happy_Talkingx05
                with dissolve

                tx "Tendrás que esforzarte bastante más"

                show gensex_69_L_d_mouth happy_Talkingx04
                with dissolve

                tx "si tu intención es que me ponga tu \"cosa\" en mi boca."

                show gensex_69_L_d_mouth happy_Silentx05
                with dissolve

                pt "Maldita ramera..."

            #elif p_txell_cunnilingus_received_from_p_prot_at_69 > 1:
            elif p_txell.cunnilingus_69_received > 1:

                $ debug ("+ Cunnilingus without Txell Blowjob.") # Is it really visible?

                call ped_sex_69_mc_lickpussy02
                call pedrera_sex_p_general_talk
                with Dissolve(0.5)

                $ ped_check_1_10("ped_69_cunnilingus_received_beforeOrgasm_txell_list")

                if ped_check_list_result == 1:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Bueno,"

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "tampoco eres tan principiante cómo pensaba,"

                    show gensex_69_L_d_mouth happy_Talkingx03
                    with dissolve

                    tx "pero tendrás que mejorar bastante si deseas impresionarme."

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    p "¿Quiéngh te ha dichogh gue guiera impresionargthe?"

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "Calla y sigue usando esa lengua para lo único que se te da bien."

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    pt "Al final la voy a morder..."

                    if p_txell.action == "blowjob_done": # Is it actually posible?

                        pt "Aunque teniendo mi polla en su boca,"

                        extend " no creo que sea la mejor idea..."

                elif ped_check_list_result == 2:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Supongo que es verdad que no se te da tan mal..."

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "Me pregunto con cuantas habrás estado"

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "antes de que empezaras a hacerlo mínimamente bien."

                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                    p "Supongho gue las mighmas gue tuh..."

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "No tienes vagina,"

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "no sabes lo que se siente."

                    show gensex_69_L_d_mouth sad_Silentx01
                    with dissolve

                    p "¿Eso es gue la chupaghs mal?"

                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    p "Porgue me paguerece que tugh tampogho tienes pollagh..."

                    extend " ¿verdad?"

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    tx "Hmm..."

                    show gensex_69_L_d_mouth happy_Talkingx02
                    with dissolve

                    tx "Buena respuesta."

                    show gensex_69_L_d_mouth happybiting_Silentx02
                    with dissolve

                elif ped_check_list_result == 3:

                    show gensex_69_L_d_mouth sad_Talkingx002
                    with dissolve

                    tx "Vale..."

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "reconozco que no se te da mal."

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "Pero tendrás que hacerlo mucho mejor si quieres me corra."

                    if p_girl_active.orgasm - p_didac_cunnilingus_p_txell_orgasm < p_didac_cunnilingus_p_txell_orgasm:

                        show gensex_69_L_d_mouth happy_Talkingx03
                        with dissolve

                        tx "Tu amigo ya lo consiguió..."

                    show gensex_69_L_d_mouth happy_Silentx03
                    with dissolve

                elif ped_check_list_result == 4:

                    show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    tx "Hmmm..."

                    show gensex_69_L_d_mouth sad_Silentx02
                    with dissolve

                    p "¿Gtienes alguna gueja?"

                    show gensex_69_L_d_mouth sad_Talkingx003
                    with dissolve

                    tx "¿Acaso me has oído quejarme?"

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Sigue y no hables."

                    show gensex_69_L_d_mouth happybiting_Silentx05
                    with dissolve

                    p "..."

                elif ped_check_list_result == 5:

                    show gensex_69_L_d_mouth happy_Talkingx05
                    with dissolve

                    tx "¿Quien lo iba a decir que alguien como tú sería capaz de hacerlo mínimamente bien?"

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    pt "¡¿Alguien como yo?!"

                    show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                    pt "¡¿A qué diablos se refiere?!"

                elif ped_check_list_result == 6:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Quizás lo logres y todo si sigues así..."

                    show gensex_69_L_d_mouth happybiting_Silentx05
                    with dissolve

                elif ped_check_list_result == 7:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Al final resulta que eres útil y todo..."

                    show gensex_69_L_d_mouth happybiting_Silentx05
                    with dissolve

                elif ped_check_list_result == 8:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "No hables y sigue usando esa lengua."

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    pt "¡Pero si no he dicho nada!"

                    show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                elif ped_check_list_result == 9:

                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                    tx "Quizás sea verdad y todo"

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "aquello que dicen que cuanto más habla uno,"

                    show gensex_69_L_d_mouth happy_Talkingx06
                    with dissolve

                    tx "más hábil es con la lengua."

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    pt "¡Pero si quien no calla eres tú!"

                    show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                elif ped_check_list_result == 10:

                    show gensex_69_L_d_mouth happy_Talkingx04
                    with dissolve

                    tx "¿Me lo parece a mí,"

                    show gensex_69_L_d_mouth happy_Talkingx06
                    with dissolve

                    tx "o realmente tienes una lengua realmente larga?"

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    p "Egpero gue no sea una gueja..."

                    show gensex_69_L_d_mouth happy_Talkingx07
                    with dissolve

                    tx "Cállate y sigue."

                    show gensex_69_L_d_mouth happybiting_Silentx04
                    with dissolve

                    pt "La madre que la parió..."

                    show gensex_69_L_d_mouth happybiting_Silentx06
                    with dissolve

                else:

                    show gensex_69_L_d_mouth sadbiting_Silentx04
                    with dissolve

                    tx "..."

                    show gensex_69_L_d_mouth happybiting_Silentx08
                    with dissolve

        if p_txell_blowjob_done_ACCEPTED == False:

            call afternight05_Pedrera_Neus_Warning

    return



############################################################################
############################################################################

############################################################################
############################################################################



############################################################################
############################################################################

# label afternight05_Pedrera_Sex_p_txell_common:

#     if p_txell.action == "rest":

#         if (p_prot.pos_missionary_rest or p_prot.pos_doggy_rest) == 0: 

#             d "¡Métemela de una vez!"

#             p "¿No preferirías un poco de preliminares antes?"

#             d "¡¿Más preliminares?!"

#             d "¡Estoy hasta los cojones de los preliminares!"

#             d "¡Fóllame de una vez!"

#         else:

#             $ debug("Needs a description of how you take your clothes off.")

#             $ debug ("Needs a description of how you take your clothes off.")

#     return

# label p_txell_insulting:

#     $ randomnum_1to10 = renpy.random.randint(1, 10)


#     if randomnum_1to10 == 1:

#         tx "¡COÑO!"

#     elif randomnum_1to10 == 2:

#         tx "¡HOSTIAS!"

#     elif randomnum_1to10 == 3:

#         tx "¡JODER!"

#     elif randomnum_1to10 == 4:

#         tx "¡ME CAGO EN TUS MUERTOS!"

#     elif randomnum_1to10 == 5:

#         tx "¡ME CAGO EN LOS CLAVOS DE LAS TUMBAS DE TUS MUERTOS!"

#     elif randomnum_1to10 == 6:

#         tx "¡COJONES!"

#     elif randomnum_1to10 == 7:

#         tx "¡SUBNORMAL!"

#     elif randomnum_1to10 == 8:

#         tx "¡GILIPOLLAS!"

#     elif randomnum_1to10 == 8:

#         tx "¡LA HOSTIA!"

#     elif randomnum_1to10 == 8:

#         tx "¡IMBÉCIL!"

#     return


label onlyWantNeus_with_p_txell:

    show gensex_oral_m_frontHead_exp_eyes 02
    show gensex_oral_m_frontHead_exp_iris front02
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
    with dissolve

    tx "..."

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris left04
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
    show gensex_oral_m_frontHead_exp_eyebrows serious
    with dissolve

    tx "Ya veo..."

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris right05
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
    show gensex_oral_m_frontHead_exp_eyebrows sadx01
    with dissolve

    return

label p_txell_oral_done_label: # 69 or oral.

    $ p_txell.action == "blowjob_done"
    $ p_prot.b_action == "blowjob_received"

    $ p_txell.blowjob_done += 1
    $ p_prot.blowjob_received += 1

    if p_txell.blowjob_done > 1: # She can suck your dick in 69 or frontal veiew.

        $ debug("Goes faster and deeper everytime she sucks your dick.")

        $ ped_sex_general_expression_Cond = ""

        if p_txell.blowjob_done == 2:
            $ ped_sex_general_action_b_Cond = "69b_03_01"

        elif p_txell.blowjob_done == 3:
            $ ped_sex_general_action_b_Cond = "69b_03_03"

        elif p_txell.blowjob_done == 4:
            $ ped_sex_general_action_b_Cond = "69b_04_03"

        elif p_txell.blowjob_done >= 5:
            $ ped_sex_general_action_b_Cond = "69b_04_05"

        call pedrera_sex_p_general_talk
        with Dissolve(1.5)

        p "¡Uhm...!"

    if p_txell.blowjob_done > 1: # Can be done more than once? Because she does Deepthroat Just After.

        $ ped_sex_general_expression_Cond = "talk"
        $ ped_sex_general_action_b_Cond = "69b_00_00b"
        call pedrera_sex_p_general_talk

        aj "IS IT READABLE? 65967"

        ###

        $ debug("Goes faster and deeper everytime she sucks your dick.")

        $ ped_sex_general_expression_Cond = ""

        if p_txell.blowjob_done == 2:
            $ ped_sex_general_action_b_Cond = "69b_03_02"

        elif p_txell.blowjob_done == 3:
            $ ped_sex_general_action_b_Cond = "69b_03_04"

        elif p_txell.blowjob_done == 4:
            $ ped_sex_general_action_b_Cond = "69b_04_04"

        elif p_txell.blowjob_done >= 5:
            $ ped_sex_general_action_b_Cond = "69b_04_05"

        call pedrera_sex_p_general_talk
        with Dissolve(1.5)

    elif p_txell.blowjob_done == 1:

        #$ ped_sex_general_69_cover = "over"
        $ ped_sex_general_expression_Cond = ""
        #$ ped_sex_general_action_Cond = "69_00_00"
        $ ped_sex_general_action_b_Cond = "69b_01_01"
        call pedrera_sex_p_general_talk
        with Dissolve(1.5)

        n "Un ligero cosquilleo te recorre la entrepierna al sentir sus labios acariciando tu miembro."

        pt "¿Será posible?..."
        
        n "Lentamente, sientes sus labios rodeando tu glande,"

        n "y la punta de su lengua, jugueteando con el frenillo."

        p "Hmm..."

        tx "Hmmm.."

        $ p_prot.b_action = "blowjob_received"
        $ p_txell.action = "blowjob_done"

        $ ped_sex_general_69_cover = "off"
        $ ped_sex_general_action_b_Cond = "69b_02_01"
        call pedrera_sex_p_general_talk
        with Dissolve(1.5)

        n "Casi sin darte tiempo a reaccionar,"

        n "sus manos se posan sobre tus nalgas a modo de palanca"

        n "para así conseguir meterse casi la mitad de tu falo"

        n "en el interior de su garganta."

        p "¡Ugh!..."

        n "Te parece sentir, más que escuchar,"

        n "una sorna gutural de victoria a través del cosquilleo causado por sus labios y su garganta."

        $ ped_sex_general_69_cover = "off"
        $ ped_sex_general_action_b_Cond = "69b_02_02"
        call pedrera_sex_p_general_talk
        with Dissolve(1.5)

        # $ ped_sex_general_expression_Cond = "talk"
        # $ ped_sex_general_action_b_Cond = "69b_00_00b"
        # call pedrera_sex_p_general_talk
        # with Dissolve(0.5)

    return

label p_txell_cunnilingus_received_label:

    if p_prot.b_action == "blowjob_received":

        call p_prot_moans_01_label

    $ randomnum_1to10 = renpy.random.randint(1, 10)

    if randomnum_1to10 == 1:

        tx "Sigue así..."

    elif randomnum_1to10 == 2:

        tx "No pares..."

    elif randomnum_1to10 == 3:

        tx "Quizás lo hagas mejor de lo que me imaginaba..."

    elif randomnum_1to10 == 4:

        tx "Reconozco que se te da bien..."

    elif randomnum_1to10 == 5:

        tx "Hacía tiempo que no me lo comían así..."

    elif randomnum_1to10 == 6:

        tx "Para ser un hombre, no se te da nada mal..."

    elif randomnum_1to10 == 7:

        if p_txell.orgasm == 0:

            tx "Al final conseguirás que tenga un orgasmo..."

        else:

            tx "Al final conseguirás que tenga otro orgasmo..."

    elif randomnum_1to10 == 8:

        tx "¿Ya se lo has comido a Neus?"

        tx "Estoy segura que no le disgustará..."

    elif randomnum_1to10 == 9:

        tx "Me pregunto si también se te da tan bien comer pollas..."

    elif randomnum_1to10 == 10:

        tx "Al final conseguirás que cambie mi opinión sobre ti..."

    if p_prot.b_action == "blowjob_received":

        $ randomnum_1to10 = renpy.random.randint(1, 10)

        if randomnum_1to10 == 1:

            pt "Tampoco se queda atrás con su jodida técnica..."

        elif randomnum_1to10 == 2:

            pt "La madre que la parió..."

        elif randomnum_1to10 == 3:

            pt "¡¿Cómo es que se le da tan bien?!"

        elif randomnum_1to10 == 4:

            pt "¡Es una jodida profesional!"

        elif randomnum_1to10 == 5:

            pt "¡Puta, que mamada!"

        elif randomnum_1to10 == 6:

            pt "Desde luego, se nota que ha sido puta..."

        elif randomnum_1to10 == 7:

            pt "Me cuesta reconocerlo, ¡pero es una jodida profesional!"

        elif randomnum_1to10 == 8:

            pt "¡Que mamada!"

        elif randomnum_1to10 == 9:

            pt "¡a madre que la pairó...!"

        elif randomnum_1to10 == 10:

            pt "¡Así no tardaré en correrme!"

    return



###


label p_txell_notReceiveBlowjob:

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

    if p_prot.pos == "69" and p_txell.action in ["blowjob_done", "blowjobDeep_done"] and p_prot.action == "takeTongueOut": # takeTongueOut

        $ ped_sex_general_69_cover = "over"
        $ ped_sex_general_action_Cond = "69_00_00"
        #$ ped_sex_general_action_b_Cond = "69b_00_00"
        call pedrera_sex_p_general_talk

        $ p_prot.action = "rest" # Not really necessary this one.
        $ p_prot.b_action = "rest"
        $ p_txell.action = "rest"
        $ p_txell.b_action = "rest"

        with Dissolve(0.5)
        
        tx "..."

        $ ped_sex_general_expression_Cond = "talk"
        $ ped_sex_general_action_b_Cond = "69b_00_00"
        call pedrera_sex_p_general_talk

        show gensex_69_L_d_mouth sad_Silentx03
        with vpunch

        n "Rápidamente te aparta con rudeza sacando la polla de su garganta."

        $ ped_sheTakesDickOut_txell += 1

        if ped_sheTakesDickOut_txell == 1:

            show gensex_69_L_d_mouth sad_Talkingx02
            with dissolve

            tx "Estás soñando si crees que voy a meterme tu miembro en mi boca,"

            show gensex_69_L_d_mouth sad_Talkingx002
            with dissolve

            tx "si tú no haces lo debido con mi entrepierna."

            show gensex_69_L_d_mouth sad_Silentx02
            with dissolve

        else:

            $ ped_check_1_5("ped_sheTakesDickOut_txell_list")

            if ped_check_list_result == 1:

                show gensex_69_L_d_mouth sad_Talkingx07
                with dissolve

                tx "¡¿Es que acaso no me explico?!"

                show gensex_69_L_d_mouth sad_Silentx06
                with dissolve

            elif ped_check_list_result == 2:

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Impresionante."

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "Eres peor de lo que me podría haber imaginado."

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

            elif ped_check_list_result == 3:

                show gensex_69_L_d_mouth sad_Talkingx05
                with dissolve

                tx "¿De verdad te cuesta tanto entenderlo?"

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            elif ped_check_list_result == 4:

                show gensex_69_L_d_mouth sad_Talkingx004
                with dissolve

                tx "¿Estás intentando provocarme?"

                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

                tx "Porque realmente eres lamentable."

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            elif ped_check_list_result == 5:

                show gensex_69_L_d_mouth sad_Talkingx03
                with dissolve

                tx "Mira que cuando te conocí pensaba que serías estúpido,"

                show gensex_69_L_d_mouth happy_Talkingx03
                with dissolve

                tx "pero desde luego,"

                show gensex_69_L_d_mouth happy_Talkingx06
                with dissolve

                tx "me quedaba corta."

                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            else:

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

                tx "..."

                show gensex_69_L_d_mouth sadbiting_Silentx04
                with dissolve

        p "..."

    elif p_prot.action == "takeDickOut" or p_prot.b_action == "takeDickOut": # NOT 69, Oral pos in theory.

        $ debug("You take off your dick from her Mouth.")

        if p_prot.action == "takeDickOut":
            $ p_prot.action = "rest"

        if p_prot.b_action == "takeDickOut":
            $ p_prot.b_action = "rest"

        $ takeDickOut_Cond += 2
        $ takeDickOut_m_Total += 1

        if p_prot.pos == "oral":
            $ ped_sex_general_expression_Cond = "talk"
            if p_txell.action == "titwank_done":
                $ ped_sex_general_action_Cond = "ob00_00"
            else:
                $ ped_sex_general_action_Cond = "o00_00"
            call pedrera_sex_p_general_talk

            show gensex_oral_m_frontHead_exp_eyes 02
            show gensex_oral_m_frontHead_exp_iris down02
            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx02
            show gensex_oral_m_frontHead_exp_eyebrows surprisex02

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

            tx "¿Uh?"

        elif randomnum_1to5 == 2:

            tx "¿Euh?"

        elif randomnum_1to5 == 3:

            tx "¿Uhmm?"

        elif randomnum_1to5 == 4:

            tx "¿Qué?"

        elif randomnum_1to5 == 5:

            tx "¿MMMmm...?"

        if takeDickOut_m_Total == 1:

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx02
                with dissolve

            tx "¿Ahora la sacas?"  

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

            if p_prot.pos == "69":
                tx "¿Para qué te me has puesto encima si no es eso lo que buscas?"

            else:
                tx "¿Para qué me la ha puesto en la boca entonces?"

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

            p "No quiero terminar en tu boca aún..."

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_m_frontHead_exp_eyebrows angryx04
                with dissolve
            else:
                show gensex_69_L_d_mouth sadbiting_Silentx03
                with dissolve

            tx "..."

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris right05
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                with dissolve

        elif takeDickOut_m_Total == 2:

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows angryx03
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Talkingx04
                with dissolve

            tx "¿Otra vez me la vuelves a quitar?"

        if takeDickOut_m_Total > 1:

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if randomnum_1to5 in [1, 2]:
                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx03
                    with dissolve

                tx "Hmmm..."

            elif randomnum_1to5 in [3, 4]:

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx04
                    with dissolve

                tx "¿En serio...?"

            elif randomnum_1to5 == 5:

                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 05
                    show gensex_oral_m_frontHead_exp_iris front05
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                tx "..."

            $ ped_check_1_10("ped_takeDickOut_txell_list")

            $ randomnum_1to5 = renpy.random.randint(1, 5)

            if ped_check_list_result in range(1,11):
                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx04
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Talkingx06
                    with dissolve
            else:
                if p_prot.pos == "oral":
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx05
                    with dissolve
                else:
                    show gensex_69_L_d_mouth sad_Silentx06
                    with dissolve

                    ## NOT FINISHED DIALOGUES
            if ped_check_list_result == 1:

                tx "Allá tú..."

            elif ped_check_list_result == 2:

                tx "Tú mismo..."

            elif ped_check_list_result == 3:

                tx "Luego no te me quejes..."

            elif ped_check_list_result == 4:

                tx "Ya me lo volverás a pedir de nuevo..."

            elif ped_check_list_result == 5:

                tx "Será mejor que te aclares..."

            elif ped_check_list_result == 6:

                tx "No tienes ni idea de lo que quieres."

            elif ped_check_list_result == 7:

                tx "No seré yo quien se la meta en la boca de nuevo."

            elif ped_check_list_result == 8:

                tx "No sabes ni lo que quieres."

            elif ped_check_list_result == 9:

                tx "Desde luego que..."

            elif ped_check_list_result == 10:

                tx "Mejor no digo nada..."

            else:

                tx "..."

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 05
                show gensex_oral_m_frontHead_exp_iris front05
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

    elif p_prot.action == "takeTongueOut": # She is not sucking your dick and you take your tongue of her.

        $ p_prot.action = "rest" 

        if (p_girl_active.orgasm + p_didac_cunnilingus_p_txell_orgasm) == p_didac_cunnilingus_p_txell_orgasm:

            #progcheck "You take your TONGUE out. You don't have your dick in her mouth. You didn't give her any ORGASM."

            if p_prot.pos == "69":

                $ ped_sex_general_69_cover = "over"
                $ ped_sex_general_action_Cond = "69_00_00"
                #$ ped_sex_general_action_b_Cond = "69b_00_00"
                call pedrera_sex_p_general_talk

                ## ped_times_1_5 If it were not random.
                $ ped_check_1_5("ped_cunnilingus_takeTongueOut_txell_list_01")

                ## NOT FINSIHED-EXPRESSIONS

                show gensex_69_L_d_mouth sad_Silentx04
                with Dissolve(0.5)

                tx "..."

                if ped_check_list_result in range(1,6):
                    show gensex_69_L_d_mouth sad_Talkingx003
                else:
                    show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                if ped_check_list_result == 1:

                    tx "Si esperas que me la meta en la boca porque dejas de usar tu lengua,"

                    show gensex_69_L_d_mouth sad_Talkingx004

                    tx "puedes esperar sentado..."

                elif ped_check_list_result == 2:

                    tx "¿Estás esperando que se haga de día?"

                elif ped_check_list_result == 3:

                    tx "Realmente no sé a qué estás esperando..."

                elif ped_check_list_result == 4:

                    tx "¿Es que te has cansado?"

                elif ped_check_list_result == 5:

                    tx "No me la voy a meter en tu boca porque pares."

                    tx "Eso tenlo por seguro."

                else:

                    tx "..."

                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

            else:

                progcheck "You take your TONGUE off... not in 69, from where?"

        else:

            # progcheck "You take your TONGUE OUT. You don't have your dick in her mouth. She had an orgasm with you."


            if p_prot.pos == "69":
                $ ped_sex_general_69_cover = "over"
                $ ped_sex_general_action_Cond = "69_00_00"
                #$ ped_sex_general_action_b_Cond = "69b_00_00"
                call pedrera_sex_p_general_talk

                show gensex_69_L_d_mouth sad_Silentx02
                with dissolve

                tx "..."

                $ ped_check_1_5("ped_cunnilingus_takeTongueOut_AfOrg_txell_list_01")

                if ped_check_list_result in range(1,6):
                    show gensex_69_L_d_mouth sad_Talkingx003
                else:
                    show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

                if ped_check_list_result == 1:

                    tx "¿Ahora has decidido parar?"

                elif ped_check_list_result == 2:

                    tx "¿Por qué te paras ahora?"

                elif ped_check_list_result == 3:

                    tx "¿En serio?"

                elif ped_check_list_result == 4:

                    tx "No hay quien te entienda..."

                elif ped_check_list_result == 5:

                    tx "Aclárate..."

                else:

                    tx "..."

                if p_txell.takeDickOutTimes > 0:

                    # $ takeDickOut_Cond ##This one is not necessary.

                    $ ped_check_1_5("ped_cunnilingus_takeTongueOut_AfOrg_DickComment_txell_list_01")

                    if ped_check_list_result in range(1,6):
                        show gensex_69_L_d_mouth sad_Talkingx04
                    else:
                        show gensex_69_L_d_mouth sad_Silentx04
                    with dissolve

                    if ped_check_list_result == 1:

                        tx "No quieres quieres que te la chupe,"
                        show gensex_69_L_d_mouth sad_Talkingx03
                        with dissolve

                        tx "ni quieres usar tu lengua..."
                        show gensex_69_L_d_mouth sad_Talkingx004
                        with dissolve

                        tx "¿Entonces qué quieres?"

                    elif ped_check_list_result == 2:

                        tx "Eres tú que ahora no quieres que te la chupe..."

                    elif ped_check_list_result == 3:

                        tx "Pensaba que me la habías quitado de la boca porque tenías miedo de correrte..."

                    elif ped_check_list_result == 4:

                        tx "Tienes una forma de hacer el 69 un tanto extraña..."

                    elif ped_check_list_result == 5:

                        tx "En realidad no sé qué pretendes..."

                    else:

                        tx "..."


                show gensex_69_L_d_mouth sad_Silentx03
                with dissolve

            else:

                progcheck "You take your TONGUE off, not in 69. She is NOT SUCKING and she had ONE ORGASM."

    else:

        aj "ERROR 2678814"

    # $ p_prot.action = "rest" # Not really necessary this one.
    $ p_prot.b_action = "rest"
    $ p_txell.action = "rest"
    $ p_txell.b_action = "rest"

    return


##

label p_txell_blowjobDeep_done_label:

    if takeDickOut_Cond > 0:

        $ takeDickOut_Cond = 0

        $ ped_check_1_5("ped_blowjobDeep_takeDickOut_txell_list_01")

        if ped_check_list_result in range(1,6):

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

        if ped_check_list_result == 1:

            tx "Ahora la quieres otra vez dentro, ¿verdad?"

        elif ped_check_list_result == 2:

            tx "Ahora sí, ¿no?"

        elif ped_check_list_result == 3:

            tx "¿Y si ahora no me apetece a mi?"

        elif ped_check_list_result == 4:

            tx "¿Ahora te vuelve apetecer?..."

        elif ped_check_list_result == 5:

            tx "Y yo pensando que querrías sorprenderme..."

        $ ped_check_1_5("ped_blowjobDeep_takeDickOut_txell_list_02")

        if ped_check_list_result in range(1,5):

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve
            else:
                show gensex_69_L_d_mouth sad_Silentx04
                with dissolve

        else:

            if p_prot.pos == "oral":
                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_m_frontHead_exp_eyebrows angryx01
                with dissolve
            else:
                show gensex_69_L_d_mouth sadbiting_Silentx04
                with dissolve

        if ped_check_list_result == 1:
            
            tx "Lo triste es que no me sorprenda."

        elif ped_check_list_result == 2:

            tx "Donde no hay..."

        elif ped_check_list_result == 3:

            tx "Hombre tenías que ser..."

        elif ped_check_list_result == 4:

            tx "Tampoco me esperaba otra cosa..."

        elif ped_check_list_result == 5:

            tx "Tss..."

        else:

            "Pft..."



    $ p_txell.blowjobDeep_done += 1
    $ p_prot.blowjobDeep_received += 1

    if p_prot.pos == "oral":
        $ p_prot.action = "blowjobDeep_received"
    elif p_prot.pos == "69":
        $ p_prot.b_action = "blowjobDeep_received"
    $ p_txell.action = "blowjobDeep_done"

    $ p_txell_blowjobDeep_done_kneels += 1

    if p_txell_blowjobDeep_done_kneels > 0:

        $ ped_sex_general_expression_Cond = "indifferent"

        if p_txell_blowjobDeep_done_kneels > 4:
            $ ped_sex_general_action_Cond = "o04_05"
        elif p_txell_blowjobDeep_done_kneels > 3:
            $ ped_sex_general_action_Cond = "o04_04"
        elif p_txell_blowjobDeep_done_kneels > 2:
            $ ped_sex_general_action_Cond = "o04_03"
        elif p_txell_blowjobDeep_done_kneels > 1:
            $ ped_sex_general_action_Cond = "o04_02"
        else:
            $ ped_sex_general_action_Cond = "o04_01"

        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

        pt "¡Dios...!"


        # ### TEST
        # progcheck "PRUEBA JOEEEER"
        # $ ped_sex_general_action_Cond = "o01_01"
        # call pedrera_sex_p_general_talk
        # progcheck "01"
        # $ ped_sex_general_action_Cond = "o02_01"
        # call pedrera_sex_p_general_talk
        # progcheck "02"
        # $ ped_sex_general_action_Cond = "o03_01"
        # call pedrera_sex_p_general_talk
        # progcheck "03"
        # $ ped_sex_general_action_Cond = "o04_01"
        # call pedrera_sex_p_general_talk
        # progcheck "04"
        # ## PRUEBA!!!!

        $ ped_sex_general_expression_Cond = "talk"
        $ ped_sex_general_action_Cond = "o00_00"
        call pedrera_sex_p_general_talk

        if p_prot.pos == "69":

            show gensex_69_L_d_mouth sad_Talkingx07
            with dissolve

        else:

            show gensex_oral_m_frontHead_exp_eyes 05
            show gensex_oral_m_frontHead_exp_iris front05
            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03

        with Dissolve(0.5)

        $ ped_check_1_10("ped_blowjobDeep_received_txell_list")

        if ped_check_list_result == 1:

            tx "No te vayas a correr ahora tan pronto,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                show gensex_oral_m_frontHead_exp_eyebrows surprisex001
            with dissolve

            tx "con lo que te ha costado que me la metiera en la boca..."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happybiting_Silentx04
            else:
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happybiting_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows serious
            with dissolve

            pt "Cualquiera diría que lo está disfrutando y todo..."

        elif ped_check_list_result == 2:

            tx "Tranquilo,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 08
                show gensex_oral_m_frontHead_exp_iris front08
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
            with dissolve

            tx "no hace falta que me elogies..."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Silentx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows suspiciousx01
            with dissolve

            pt "¿Quien te ha dicho que yo iba...?"

            pt "Bah..."

            extend " ¿Para qué molestarse...?"

        elif ped_check_list_result == 3:

            tx "No te faltará mucho para correrte,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 02
                show gensex_oral_m_frontHead_exp_iris front02
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
            with dissolve

            tx "¿Me equivoco?"

        elif ped_check_list_result == 4:

            tx "Disfrútalo mientras puedas..."

        elif ped_check_list_result == 5:

            tx "Dirás lo que quieras,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                show gensex_oral_m_frontHead_exp_eyebrows angryx03
            with dissolve

            tx "pero estoy segura que nunca te han hecho algo parecido."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Silentx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
            with dissolve

            pt "¿Se puede ser más engreída?"

        elif ped_check_list_result == 6:

            tx "Cualquiera diría que se te está poniendo más dura y todo"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 02
                show gensex_oral_m_frontHead_exp_iris front02
                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                show gensex_oral_m_frontHead_exp_eyebrows sadx01
            with dissolve

            tx "teniéndola entera dentro de mi garganta..."

        elif ped_check_list_result == 7:

            tx "¿Te gusta sentirla entera dentro de mi garganta?"

        elif ped_check_list_result == 8:

            tx "Realmente la tienes enorme..."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 02
                show gensex_oral_m_frontHead_exp_iris front02
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
            with dissolve

            tx "Pero nada que no pueda manejar."

        elif ped_check_list_result == 9:

            tx "Te gusta,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth happy_Talkingx06
            else:
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_m_frontHead_exp_eyebrows angryx02
            with dissolve

            tx "¿verdad?"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx02
            else:
                show gensex_oral_m_frontHead_exp_eyes 01
                show gensex_oral_m_frontHead_exp_iris front01
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows surprisex01
            with dissolve

            p "Mientras hablas,"

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sad_Silentx04
            else:
                show gensex_oral_m_frontHead_exp_eyes 03
                show gensex_oral_m_frontHead_exp_iris front03
                show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_m_frontHead_exp_eyebrows serious
            with dissolve

            p "no trabajas."

            if p_prot.pos == "69":
                show gensex_69_L_d_mouth sadbiting_Silentx04
            else:
                show gensex_oral_m_frontHead_exp_eyes 04
                show gensex_oral_m_frontHead_exp_iris front04
                show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_m_frontHead_exp_eyebrows angryx01
            with dissolve

            tx "Hmm..."

        elif ped_check_list_result == 10:

            if p_txell.blowjobDeep_done > 0:

                tx "Estoy convencida de que lo hago bastante mejor que tu compañero de piso."

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx03
                else:
                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris front02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                    show gensex_oral_m_frontHead_exp_eyebrows normal
                with dissolve

                p "¿Qué te hace pensar eso?"

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Talkingx06
                else:
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                with dissolve

                tx "Que tengo bastante más experiencia."

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx03
                else:
                    show gensex_oral_m_frontHead_exp_eyes 01
                    show gensex_oral_m_frontHead_exp_iris right01
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
                with dissolve

                d "¡Eso no se lo puedo negar!"

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx06
                else:
                    show gensex_oral_m_frontHead_exp_eyes 02
                    show gensex_oral_m_frontHead_exp_iris right02
                    show gensex_oral_m_frontHead_exp_mouth sad_Silentx07
                    show gensex_oral_m_frontHead_exp_eyebrows angryx02
                with dissolve

                d "¡Pero eso es por que eres mucho más ramera que yo!"

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth sad_Silentx05
                else:
                    show gensex_oral_m_frontHead_exp_eyes 08
                    show gensex_oral_m_frontHead_exp_iris front08
                    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                with dissolve

                tx "Pfft...."

            else:

                tx "¿Te habían hecho algo parecido alguna vez?"

                if p_prot.pos == "69":
                    show gensex_69_L_d_mouth happy_Silentx05
                else:
                    show gensex_oral_m_frontHead_exp_eyes 04
                    show gensex_oral_m_frontHead_exp_iris front04
                    show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                    show gensex_oral_m_frontHead_exp_eyebrows angryx01
                with dissolve

                menu:

                    "Desde luego que sí.":
                        call p_Help

                        $pl.ch_pts("np",-1)
                        $pl.ch_pts("mp",-2)

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx03
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "Hmm..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx004
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        tx "Más te gustaría..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                        with dissolve

                        pt "¡Será engreída la tía!"

                    "Ayer mismo lo hizo Dídac." if afternight04__MMouth_dick_Deep_Success > 0:
                        call p_Help

                        $pl.ch_pts("np",-1)
                        $pl.ch_pts("dp",2)
                        $pl.ch_pts("mp",-2)

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Silentx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 00
                            show gensex_oral_m_frontHead_exp_iris front00
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex03
                        with dissolve

                        tx "..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx005
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris right01
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx006
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        tx "¿Conseguiste metértela entera?"

                        $ Pedrera_char_Cond = "DidacClose_show"
                        call Pedrera_char_lab

                        show didacf_mouth sad_Talkingx07
                        $ dteye = 8
                        call didac_exp_tears_tears
                        show didacf_pupils front08
                        show didacf_eyebrows angryx03
                        with fade_short

                        d "¡No lo hice a gusto!"

                        show didacf_mouth sadbiting_Silentx02
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows angryx02

                        p "Lo dices como si te hubiera obligado..."

                        show didacf_mouth sadbiting_Silentx05
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils right05
                        show didacf_eyebrows angryx04

                        d "Tsssk..."

                        $ Pedrera_char_Cond = "p_nobody"
                        call Pedrera_char_lab

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sadbiting_Silentx03
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 01
                            show gensex_oral_m_frontHead_exp_iris right01
                            show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex03
                        with fade_short


                        tx "..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx002
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 02
                            show gensex_oral_m_frontHead_exp_iris right02
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx002
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                        with dissolve

                        tx "Desde luego,"

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Talkingx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris right03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                        with dissolve

                        tx "es algo que no me esperaba de ti,"

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Talkingx06
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris right04
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                        with dissolve

                        tx "Dídac..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 06
                            show gensex_oral_m_frontHead_exp_iris front06
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows sadx02
                        with dissolve

                        d "¡Vete a la mierda!"

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx03
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows sadx01
                        with dissolve

                    "Eso no te lo puedo negar.":
                        call p_Help

                        $pl.ch_pts("np",-1)
                        $pl.ch_pts("dp",-1)
                        $pl.ch_pts("mp",1)

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx06
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                        with dissolve

                        tx "Hmm..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Talkingx07
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx07
                            show gensex_oral_m_frontHead_exp_eyebrows angryx03
                        with dissolve

                        tx "Por supuesto que no."

                        if afternight04__MMouth_dick_Deep_Success > 0:

                            if p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx04
                            else:
                                show gensex_oral_m_frontHead_exp_eyes 01
                                show gensex_oral_m_frontHead_exp_iris right01
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
                                show gensex_oral_m_frontHead_exp_eyebrows surprisex02
                            with dissolve

                            d "¡¿Y lo que me hiciste ayer no cuenta?!"

                            if p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Silentx05
                            else:
                                show gensex_oral_m_frontHead_exp_eyes 04
                                show gensex_oral_m_frontHead_exp_iris right04
                                show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
                                show gensex_oral_m_frontHead_exp_eyebrows serious
                            with dissolve

                            tx "..."

                            if p_prot.pos == "69":
                                show gensex_69_L_d_mouth sad_Talkingx05
                            else:
                                show gensex_oral_m_frontHead_exp_eyes 03
                                show gensex_oral_m_frontHead_exp_iris right03
                                show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
                                show gensex_oral_m_frontHead_exp_eyebrows angryx02
                            with dissolve

                            tx "¿Acaso te entró entera en la garganta?"

                            $ Pedrera_char_Cond = "DidacClose_show"
                            call Pedrera_char_lab

                            show didacf_mouth sadbiting_Silentx04
                            $ dteye = 0
                            call didac_exp_tears_tears
                            show didacf_pupils front00
                            show didacf_eyebrows surprisex02
                            with fade_short

                            d "..."

                            show didacf_mouth sad_Talkingx07
                            $ dteye = 2
                            call didac_exp_tears_tears
                            show didacf_pupils right02
                            show didacf_eyebrows angryx03
                            with dissolve

                            d "¡No he dicho nada!"

                            show didacf_mouth sad_Silentx07
                            $ dteye = 5
                            call didac_exp_tears_tears
                            show didacf_pupils right05
                            show didacf_eyebrows angryx04
                            with dissolve

                            pause 0.2

                            $ Pedrera_char_Cond = "p_nobody"
                            call Pedrera_char_lab

                            if p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Talkingx06
                            else:
                                show gensex_oral_m_frontHead_exp_eyes 02
                                show gensex_oral_m_frontHead_exp_iris right02
                                show gensex_oral_m_frontHead_exp_mouth happy_Talkingx06
                                show gensex_oral_m_frontHead_exp_eyebrows sadx01
                            with dissolve

                            tx "Ya me lo imaginaba..."

                            if p_prot.pos == "69":
                                show gensex_69_L_d_mouth happy_Silentx07
                            else:
                                show gensex_oral_m_frontHead_exp_eyes 05
                                show gensex_oral_m_frontHead_exp_iris right05
                                show gensex_oral_m_frontHead_exp_mouth happy_Silentx07
                                show gensex_oral_m_frontHead_exp_eyebrows angryx01
                            with dissolve

                    "Es posible...":
                        call p_Help

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Es posible dice..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx003
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "¿Qué más quisieras..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx03
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx03
                            show gensex_oral_m_frontHead_exp_eyebrows serious
                        with dissolve

                    "No pienso responderte a eso.":
                        call p_Help

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Talkingx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 03
                            show gensex_oral_m_frontHead_exp_iris front03
                            show gensex_oral_m_frontHead_exp_mouth happy_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Ni falta que hace..."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx07
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
                            show gensex_oral_m_frontHead_exp_eyebrows angryx02
                        with dissolve

                        pt "¡¿Se puede ser más engreída?!"

                    "...":
                        call p_Help

                        $pl.ch_pts("mp",1)

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx004
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 04
                            show gensex_oral_m_frontHead_exp_iris front04
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex001
                        with dissolve

                        tx "¿Te he dejado sin habla?"

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth sad_Talkingx04
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 08
                            show gensex_oral_m_frontHead_exp_iris front08
                            show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
                            show gensex_oral_m_frontHead_exp_eyebrows surprisex002
                        with dissolve

                        tx "Tranquilo,"

                        extend " no eres el primero."

                        if p_prot.pos == "69":
                            show gensex_69_L_d_mouth happy_Silentx05
                        else:
                            show gensex_oral_m_frontHead_exp_eyes 05
                            show gensex_oral_m_frontHead_exp_iris front05
                            show gensex_oral_m_frontHead_exp_mouth happy_Silentx05
                            show gensex_oral_m_frontHead_exp_eyebrows angryx01
                        with dissolve

        else:

            tx "..."

        show gensex_oral_m_frontHead_exp_eyes 08
        show gensex_oral_m_frontHead_exp_iris front08
        show gensex_oral_m_frontHead_exp_mouth happy_Silentx06
        show gensex_oral_m_frontHead_exp_eyebrows angryx02
        with dissolve

        pause 0.2


        $ ped_sex_general_expression_Cond = "indifferent"

        if p_txell_blowjobDeep_done_kneels > 4:
            $ ped_sex_general_action_Cond = "o04_05"
        elif p_txell_blowjobDeep_done_kneels > 3:
            $ ped_sex_general_action_Cond = "o04_04"
        elif p_txell_blowjobDeep_done_kneels > 2:
            $ ped_sex_general_action_Cond = "o04_03"
        elif p_txell_blowjobDeep_done_kneels > 1:
            $ ped_sex_general_action_Cond = "o04_02"
        else:
            $ ped_sex_general_action_Cond = "o04_02"

        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

    return

label p_txell_blowjobDeep_done_kneels_label:

    $ ped_sex_general_expression_Cond = "veryAngry"
    #$ ped_sex_general_action_Cond = "o00_00"
    call pedrera_sex_p_general_talk
    with Dissolve(0.5)

    tx "..."

    $ ped_sex_general_expression_Cond = "talk"
    $ ped_sex_general_action_Cond = "o00_00"
    call pedrera_sex_p_general_talk

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris front04
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx06
    show gensex_oral_m_frontHead_exp_eyebrows angryx03
    with hpunch

    tx "¿Qué pretendes?"

    show gensex_oral_m_frontHead_exp_eyes 00
    show gensex_oral_m_frontHead_exp_iris front00
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
    with dissolve

    p "Me has dicho que si era capaz de que consigueras un orgasmo..."

    show gensex_oral_m_frontHead_exp_eyes 02
    show gensex_oral_m_frontHead_exp_iris front02
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx07
    show gensex_oral_m_frontHead_exp_eyebrows angryx02
    with dissolve

    tx "Mientras me lamías la entrepierna teniéndome de rodillas,"

    show gensex_oral_m_frontHead_exp_eyes 08
    show gensex_oral_m_frontHead_exp_iris front08
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx004
    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
    with dissolve

    tx "estando de pie,"

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris front05
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
    show gensex_oral_m_frontHead_exp_eyebrows surprisex002
    with dissolve

    tx "creo que te será difícil semejante hazaña."

    show gensex_oral_m_frontHead_exp_eyes 03
    show gensex_oral_m_frontHead_exp_iris front03
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx03
    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx02
    with dissolve

    p "¿Tanto miedo le tienes al tamaño de mi miembro?"

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris front05
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx02
    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show gensex_oral_m_frontHead_exp_eyes 08
    show gensex_oral_m_frontHead_exp_iris front08
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
    show gensex_oral_m_frontHead_exp_eyebrows angryx02
    with dissolve

    tx "Tus artimañas de salido de pueblo no te van a servir conmigo,"

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris front05
    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
    show gensex_oral_m_frontHead_exp_eyebrows angryx03
    with dissolve

    tx "palurdo."

    show gensex_oral_m_frontHead_exp_eyes 01
    show gensex_oral_m_frontHead_exp_iris right01
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
    with dissolve

    d "Yo también lo he escuchado."

    show gensex_oral_m_frontHead_exp_eyes 02
    show gensex_oral_m_frontHead_exp_iris right02
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx05
    show gensex_oral_m_frontHead_exp_eyebrows angryx02
    with dissolve

    tx "¿De qué hablas tú?"

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris right04
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx05
    show gensex_oral_m_frontHead_exp_eyebrows angryx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "DidacClose_show"
    call Pedrera_char_lab

    show didacf_mouth happy_Talkingx05
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    with fade_short

    d "Le dijiste que si era capaz de conseguirte un orgasmo,"

    show didacf_mouth happy_Talkingx06
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    with dissolve

    d "te la meterías entera en tu garganta."

    show didacf_mouth happy_Silentx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "p_nobody"
    call Pedrera_char_lab

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris right04
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx04
    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
    with fade_short

    tx "No sé que diablos has escuchado,"

    show gensex_oral_m_frontHead_exp_eyes 03
    show gensex_oral_m_frontHead_exp_iris right03
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
    with dissolve

    tx "pero desde luego tendrías hacértelo mirar."

    show gensex_oral_m_frontHead_exp_eyes 08
    show gensex_oral_m_frontHead_exp_iris front08
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx04
    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "DidacClose_show"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx002
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows normal
    with fade_short

    d "Neus,"

    show didacf_mouth sad_Talkingx03
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "¿Verdad?"

    show didacf_mouth happy_Silentx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose_show"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_iris right01
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_eyebrows surprisex01
    with fade_short

    ne "¿Euh...?"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_iris right00
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_eyebrows surprisex02
    with dissolve

    d "Tú también lo has escuchado,"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris right02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    d "¿o es que [protname] y yo estamos sordos?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_iris left04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Euhmm..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris left02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Algo así me ha parecido oír..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "p_nobody"
    call Pedrera_char_lab

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris left04
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
    show gensex_oral_m_frontHead_exp_eyebrows sadx03
    with fade_short

    tx "..."

    show gensex_oral_m_frontHead_exp_eyes 00
    show gensex_oral_m_frontHead_exp_iris right00
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx05
    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
    with dissolve

    d "Pero bueno,"

    extend " tampoco pasa nada,"

    $ Pedrera_char_Cond = "DidacClose_show"
    call Pedrera_char_lab

    show didacf_mouth happy_Talkingx07
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows normal
    with fade_short

    d "es normal que una zorra manipuladora como esta,"

    show didacf_mouth happy_Talkingx08
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    with dissolve

    d "no tenga palabra,"

    extend " ni dignidad."

    show didacf_mouth happy_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "p_nobody"
    call Pedrera_char_lab

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris right05
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
    show gensex_oral_m_frontHead_exp_eyebrows angryx04
    with fade_short

    tx "..."

    show gensex_oral_m_frontHead_exp_eyes 08
    show gensex_oral_m_frontHead_exp_iris front08
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx003
    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
    with dissolve

    tx "Bien jugado,"

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris right05
    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx03
    show gensex_oral_m_frontHead_exp_eyebrows surprisex001
    with dissolve

    tx "Zorra."

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris right04
    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
    show gensex_oral_m_frontHead_exp_eyebrows angryx01
    with dissolve

    tx "No me esperaba que alguien como tú me pudiera acorralar..."

    show gensex_oral_m_frontHead_exp_eyes 00
    show gensex_oral_m_frontHead_exp_iris front00
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx04
    show gensex_oral_m_frontHead_exp_eyebrows surprisex02
    with dissolve

    p "Me imagino que está aprendiendo de la mejor."

    show gensex_oral_m_frontHead_exp_eyes 05
    show gensex_oral_m_frontHead_exp_iris left05
    show gensex_oral_m_frontHead_exp_mouth sadbiting_Silentx02
    show gensex_oral_m_frontHead_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show gensex_oral_m_frontHead_exp_eyes 03
    show gensex_oral_m_frontHead_exp_iris front03
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx02
    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
    with dissolve

    p "¿Entonces...?"

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris front04
    show gensex_oral_m_frontHead_exp_mouth sad_Silentx03
    show gensex_oral_m_frontHead_exp_eyebrows normal
    with dissolve

    p "¿Lo harás?"

    show gensex_oral_m_frontHead_exp_eyes 02
    show gensex_oral_m_frontHead_exp_iris right02
    show gensex_oral_m_frontHead_exp_mouth sad_Talkingx03
    show gensex_oral_m_frontHead_exp_eyebrows surprisex01
    with dissolve

    tx "Dídac,"

    show gensex_oral_m_frontHead_exp_eyes 04
    show gensex_oral_m_frontHead_exp_iris right04
    show gensex_oral_m_frontHead_exp_mouth happy_Talkingx05
    show gensex_oral_m_frontHead_exp_eyebrows angryx03
    with dissolve

    tx "mira y aprende."

    # Deepthroat

    $ p_prot.blowjobDeep_received += 1
    $ p_txell.blowjobDeep_done += 1

    $ p_prot.action = "blowjobDeep_received"
    $ p_txell.action = "blowjobDeep_done"

    $ ped_sex_general_expression_Cond = "lust"
    $ ped_sex_general_action_Cond = "o04_01"
    call pedrera_sex_p_general_talk
    with Dissolve(0.5)

    pt "¡Joder!"

    # If Didac had done deepthroat completely.

    if p_didac.blowjobDeep_done > 0:

        $ ped_sex_general_expression_Cond = "surpriseRight"
        #$ ped_sex_general_action_Cond = "o04_01"
        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

        d "Psst..."

        d "Antes también me la he metido así hasta el fondo..."

        $ ped_sex_general_expression_Cond = "indifferent"
        #$ ped_sex_general_action_Cond = "o04_01"
        call pedrera_sex_p_general_talk
        with Dissolve(0.5)

    $ p_txell_blowjobDeep_done_ACCEPTED = True

    return