
label am05_DSex_horny:

    $ pdaytime = "05_afternoon"
    call ac_sex_defining

    #call ac_sex_prev
    call ac_sex_aft

#########

    pause 0.12

    $ df_eye = "down04"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "Ves que sus ojos se fijan de nuevo en tu entrepierna."

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Parece que se te ha bajado un poco."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Es que hablar de responsabilidades y de partos"

    $ df_eye = "right02"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "no es algo que me ponga precisamente muy cachondo."

    progcheck "[protname] is [af5_p.closeOrgasmTotal] close to orgasm."

    if afternight04__MMouth_dick_Success > 0:

        $ df_eye = "down05"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        pause 0.2

        scene day05
        with fade

        # $ af5_d.sexAction("dickLick")
        # $ af5_p.pleasure += 2
        #call ## afterSexCheck
        
        n "Desciende su rostro hasta tu entrepierna y con sutil perrería"

        n "empieza a relamer la suave carne de tu miembro."

        p "Pensé que habías dicho que eso de chupármela era de maricones."

        d "Ahora es lo que somos,"

        d "¿no?"

        p "..."

        menu:

            pt "¿Es lo que somos?"

            "En el fondo quizás tienes razón.":
                call p_Help
                $pl.ch_pts("dp",1)

                d "Hmmm..."

            "¿Por qué no confiesas que en realidad te encanta chupármela?":
                call p_Help
                $pl.ch_pts("dp",1)

                d "..."

                p "Antes has dicho que tenías mini-orgasmos al hacerlo."

                d "No debería haberte dicho eso."

                p "Un poco tarde."

                d "Tssk..."

            "Habla por ti.":
                call p_Help

                p "Por muy musculosa que seas,"

                p "para mí,"

                p "ahora eres una mujer."

                d "Hmmm..."

                d "Ayer te la terminé chupando,"

                if afternight04__MMouth_dick_Deep_Success:

                    d "llegué a tragármela casi entera y todo..."

                d "¿no es así?"

                if afternight04__MMouth_dick_Deep_Success > 0:

                    pt "En realidad fui yo quien te la metí en la garganta..."

                else:

                    pt "En realidad fui yo quien te la metí en la boca..."

                d "Además,"

                d "sabiendo lo que sabes ahora"

                d "y que dependo de tus jodidas ganas de follar,"

                d "tendré que aprender a convencerte mejor en futuras ocasiones"

                d "para que me folles como un buen semental."

                menu:
                    pt "Como un buen semental..."

                    "¿Por qué lo llamas follar? Si en el fondo sabes que estás empezando a sentir algo por mí.":
                        call p_Help

                        d "..."

                        if pl.dp > 80:
                            $pl.ch_pts("dp",1)

                            d "No-"

                            extend "no me seas idiota..."

                        else:

                            d "Tampoco te flipes tú ahora..."

                    "Pues tendrás que mejorar bastante más la técnica si pretendes convencerme con eso.":
                        call p_Help

                        $pl.ch_pts("dp",-1)

                        d "..."

                        d "Serás imbécil..."

                    "...":
                        call p_Help
                        pass

                p "..."


                if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

                    if afternight04_CumInThroat > 0:

                        d "¡Pero ni se te ocurra volver a correrte en mi garganta!"

                    elif afternight04_CumInMouth > 0:

                        d "¡Pero ni se te ocurra volver a correrte en mi boca!"

                    d "¡¿Queda claro?!"

                    menu:
                        pt "¿Le gusta o no le gusta?"

                        "Lo dices como si antes no me hubieras dicho lo muy perra que te pone mi esperma...":
                            call p_Help
                            $pl.ch_pts("dp",1)

                            d "..."

                            d "A veces hablo demasiado..."

                            p "Pues sí."

                            d "Tssk..."

                        "Vale, vale... no lo volveré a hacer.":
                            call p_Help
                            $pl.ch_pts("dp",1)

                            d "Más te vale."

                        "...":
                            call p_Help

                            d "..."

        d "Bueno,"

        d "creo que ya está lo suficientemente dura."

    else:

            # n "Ves que sus ojos se fijan de nuevo en tu entrepierna."
            # d "Parece que se te ha bajado un poco."
            # p "Es que hablar de responsabilidades y de partos"
            # p "no es algo que me ponga precisamente muy cachondo."

        # NOT_FINISHED

        call WIP

        

        # your dick is not hard, but she doesn't want to suck it.

    jump am05_DSex_DidacWantsStart

label am05_DSex_DidacWantsStart:

    scene day05
    with fade

    n "Vuelve a ponerse de pie"

    n "acercando su entrepierna a la punta de tu erecto miembro."

    p "¡El condón!"

    if DidacPregnant:

        d "¡Pero si te acabo de explicar que no hace falta!"

        p "¡Me da igual!"

        p "Aún cabe la posibilidad de que no estés embarazada."

        p "¡Y esta vez me pondré yo el condón!"

        d "..."

        d "Mira que eres imbécil cuando quieres..."

    else:

        d "..."

        d "Tssk..."

    n "Se aparta de ti y se dirige al cajón de la mesita de noche"

    n "de dónde saca un condón que termina arrojándotelo encima."

    d "Toma."

    menu:

        pt "Que soy imbécil dice..."

        "<Ponerte el condón>":

            n "Sacas el preservativo del embalaje"

            n "y apenas has logrado ponértelo"

            n "cuando los cálidos labios vaginales de Dídac acarician tu polla."

            jump am05_DSex_start
                # n "Desciende sus caderas metiéndose casi la mitad de tu miembro en su cálido y estrecho interior."
                # d "Joder..."
                # n "Desciende su cuerpo acercándose a tu rostro."
                # d "Realmente la tienes bien dura..."

        "<Decirle que te lo ponga ella con su boca>":

            jump am05_DSex_mouthCondom


label am05_DSex_mouthCondom:

    p "¿Por qué no me la pones con tu boca?"

    d "..."

    d "¿Hablas en serio?"

    p "Por supuesto."

    d "¡Pero si me acabas de decir que a partir de ahora el condón te lo ponías tú solo!"

    p "¿No decías que me querías cachondo?"

    d "¡Ya la tienes dura!"

    p "Quizás se me afloje viendo lo negativa que te pones..."

    ## If she sucked your dick she accepts.

    if afternight04__MMouth_dick_Success > 0 and pl.dp > 80:
        pass

    else:

        d "..."

        n "Se vuelve a poner de rodillas, acerca su rostro a tu entrepierna"

        with hpunch

        p "¡Auch!"

        n "y le da un hostión a tu polla."

        d "¡Ya la tienes suficientemente dura, joder!"

        p "..."

        n "Con sus dientes abre el embalaje del preservativo."

        p "Dídac..."

        d "No me vengas con gilipolleces,"

        if afternight04__MMouth_dick_Success > 0:

            d "que te la chupara ayer,"

            d "no significa que tenga que volver a hacerlo."

        else:

            d "tienes tantas ganas como yo."

        p "..."

        n "Sin demasiada delicadez te cubre el miembro con ese viscoso plástico."

        jump am05_DSex_start
                # n "Desciende sus caderas metiéndose casi la mitad de tu miembro en su cálido y estrecho interior."
                # d "Joder..."
                # n "Desciende su cuerpo acercándose a tu rostro."
                # d "Realmente la tienes bien dura..."

    d "..."

    d "La madre que te..."

    n "Se vuelve a poner de rodillas, acerca su rostro a tu entrepierna"

    n "y te hace el gesto de abrir la mano con cara de pocos amigos."

    d "¿Me lo das, o no?"

    p "Ni se te ocurra cortarlo."

    d "..."

    d "Tssk..."

    n "Finalmente le entregas el preservativo"

    n "y con sus dientes rompe el embalaje."

    p "¡Ey!"

    d "¿Qué coño pasa ahora?"

    p "¡No lo abras con tus dientes!"

    d "¡¿Y por qué no?!"

    p "¡Por que lo podrías romper!"

    d "¡¿Y cómo coño quieres que lo abra?!"

    p "¡Pues con las manos joder!"

    d "..."

    d "¿Se puede hacer con las manos?"

    p "..."

    p "¿Estás seguro que no tienes ningún hijo por ahí?"

    d "..."

    d "No que yo sepa..."

    d "Además, si lo tuviera,"

    d "ahora tampoco podrían colgarme el muerto a mí."

    pt "¿El muerto?"

    d "Alguna ventaja tenía que ser mujer."

    p "Sí..."

    p "Que ahora son los tíos los que te pueden dejar a ti embarazada."

    d "..."

    if pl.dp >80:

        d "No si tú lo haces primero..."
    else:

        d "Mira que eres aguafiestas cuando quieres."

    p "..."

    d "Primero se pone en la boca, ¿no?"

    n "Coloca el condón en sus labios."

    p "¿Es que no te lo han hecho nunca?"

    d "¡Glarog gue me lo han hegcho!"

    d "Pego una cgosa es veglo"

    d "y la ota haceglo..."

    n "Desciende su rostro a la altura del glande,"

    n "acariciando la punta con el cálido y viscoso plástico."

    n "Sigue empujando con sus labios"

    n "intentando extenderlo a lo largo de tu miembro."

    d "..."

    d "Desliza sus labios a lo largo del rollo"

    n "pero apenas logra llegar al limite del glande"

    n "cuando sigue bajando dejando el condón atrás."

    d "¡Joder!"

    d " Esto es más complicado de lo que parece..."

    n "Acerca sus manos dispuesto a seguir bajando el condón con sus dedos."

    menu:

        pt "¿Ya se rinde?"

        "<Decirle que no use las manos>":
            call p_Help

            # enslavement + 1
            pass

        "...":
            call p_Help

            n "Sin demasiada delicadeza sigue desenrollando el viscoso plástico"

            n "hasta que casi cubre tu enorme falo."

            n "Sin apenas darte tiempo a reaccionar se pone de pie sobre la cama"

            n "y acerca su cálida vagina a la cima de tu polla."

            jump am05_DSex_start
                # n "Desciende sus caderas metiéndose casi la mitad de tu miembro en su cálido y estrecho interior."
                # d "Joder..."
                # n "Desciende su cuerpo acercándose a tu rostro."
                # d "Realmente la tienes bien dura..."

    p "¡Ey!"

    p "¿Qué te he dicho?"

    d "¡No me seas tocapelotas!"

    d "Estoy cachonda,"

    d "¡¿vale?!"

    p "Pues entonces no tengas prisa y asegúrate de hacerlo bien."

    d "..."

    d "Tssk..."

    n "Acerca de nuevo sus labios dónde el condón apenas cubre tu glande"

    n "y deslizando sus labios retoma el camino logrando sobrepasarlo."

    n "Esta vez sus labios te presionan el miembro con más solidez"

    n "y se lo toma con más calma."

    n "Consigue llegar casi a la mitad"

    n "aún desenroscando el preservativo a lo largo del mismo."

    with hpunch

    d "¡Cough!{w=0.25}{nw}"

    extend "-¡cough!"

    d "Dios..."

    d "Que pollón tienes, joder."

    p "No has terminado."

    d "..."

    menu:

        pt "No sé si es buena idea insistir tanto..."

        "<Obligarla a seguir>":
            call p_Help
            $pl.ch_pts("dp",-1)

            # enslavement 2

            d "..."

            d "Me estás empezando a tocar las pelotas..."

            p "Algo que ya no tienes."

            d "..."

            d "Si no fuera porque la necesito bien dura,"

            d "¡ahora mismo te daría de hostias en los huevos!"

            p "Pero el caso es que la necesitas."

            d "..."

            d "Tsssk..."

            n "Vuelve acercar sus labios a tu polla e introduciéndosela en su boca."

            n "sigue deslizando el condón hacia abajo"

            n "hasta desenroscándolo casi por completo cuando:"

            with vpunch
            d "¡Cough! ¡Cough!"

            d "¡Joder!"

            d "¡Que no puedo, coño!"

            p "..."

            n "Con tus propias manos deslizas lo que falta del condón"

            n "al mismo tiempo que Dídac se levanta"

            n "y acerca su entrepierna a la punta de tu miembro."

        "Vale, supongo que es suficiente.":

            n "Vuelve a ponerse de pie"

            n "y casi sin darte tiempo a responder"

            n "se introduce la punta en su interior."

    p "¡Espera,"

    extend " espera!"

    d "¡¿Qué coño quieres ahora?!"

    p "¡Déjame ponerlo bien del todo!"

    d "¡Ya se irá poniendo bien, joder!"

    n "Sigue deslizándose hacia abajo"

    n "introduciéndose tu miembro más allá del glande."

    p "Hmmm..."

    d "Dios..."

    jump am05_DSex_beginning

###

label am05_DSex_beginning:

    n "Desciende sus caderas metiéndose casi la mitad de tu miembro"

    n "en su cálido y estrecho interior."

    d "Joder..."

    n "Desciende su cuerpo acercándose a tu rostro."

    d "Realmente la tienes bien dura..."

    jump am05_DSex_start


# You're both in living room. Didac French kisses you by surprise.

    # Didac Pregnant-She falls in love with you-Wants to live with you forever. Wants to fuck you raw, she will tell you that she took cut off the condom and... she is pretty sure she is already pregant, since she felt all your sperm floding inside of her. That doesn't mean anything! but still, you cum inside of her, so there are high chances that she is already pregnant and she asks you to fuck her again, she really wants to become a woman. Why? Because she fucking loves it! she never had such great pleasure in all her life, not even once was that pleasurable.



    # Bueeeeeno.... aquí qué coño hago?

    ##  A veer... 


    ## Distitnos finales que tengo ganas de llegar.
        # Dídac Pregnant:
            # She falls in love with you and begs you to stay with her for eternity.
            # She is mad horny with you and asks for you in eternity.
            # Despite being pregnant, doesn't like you, but can't live without you.
        # Dídac NOT pregnant:
            # She falls in love with you, (really high points) and asks you to breed her. 
            # She is mad horny with you and you discover she cutted a condom to get pregnant.
            # Despite not liking you, she still wants to be fucked by you, she needs it more than can she even accept it.

            # You can love her and get her pregnant.
            # You can accept her and get her pregnant.

            # You can have sex with her and after that leave to Neus date.

            # You can accept her love, but not get her pregnant but not going to the date with Neus, if she becomes a woman, then be it. (She becomes a man once again, but even then He still gets chills with you and you can have sex with him being a man.)




        # p "Si esas tenemos."
        # n "Agarras a Dídac, y con un rápido gesto"
        # n "te pones encima de ella sobre tu cama."
        # d "Uhhmmm..."
        # d "Me gusta cuando te pones así."
        # p "Eres una zorra."
        # d "Quizás..."
        # d "Fóllame [protname]."


################################################################################################
# ########################################################################
################################################################################################
################################################################################################
# ########################################################################
################################################################################################

################################################################################################
# ########################################################################
################################################################################################################################################################################################
# ########################################################################
################################################################################################

label morning06_Df_Sex:

    $ pdaytime = "06_morning"

    call ac_sex_aft

    if p_prot_analgesic == "accepted":
        jump morning06_DfS_Cuf_start
#################

    jump m6_DSex_start



################################################################################################
# ########################################################################
################################################################################################
################################################################################################
# ########################################################################
################################################################################################

################################################################################################
# ########################################################################
################################################################################################################################################################################################
# ########################################################################
################################################################################################


label morning06_DfS_Cuf_start:
        # p "¿Vas a ser así todos los días?"
        # d "Es posible..."
        # p "..."
        # n "Dejas ir un profundo suspiro."

    d "Hmmm..."

    n "Prosigue el movimiento de sus caderas."

    n "Pero hay algo que te llama la atención."

    p "Dídac..."

    d "¿Sí...?"

    p "Llevo un condón puesto,"

    extend " me imagino."

    d "..."

    d "Pues sigue imaginando eso."

    p "¡Dídac!"

    if DidacPregnant:

        d "¡¿Qué?!"

        d "¡Joder!"

        d "Ya te dije ayer que de todos modos es probable que ya esté embarazada."

        d "¿Qué más da que lo hagamos con,"

        extend " o sin él?!"

        p "¡Pues porque aún no es seguro!"

        d "¡Pues para mí lo es, y punto!"

        d "Además,"

        d "tampoco es que ahora puedas hacer nada para impedírmelo..."

        menu:

            "<Decirle que se ponga el condón>":
                call p_Help

                jump morning06_DfS_Cuf_condomRequest

            "...":
                call p_Help

                d "..."

                pt "¡¿En serio?!"

                pt "¡Que es Dídac joder!"

                pt "¡¿Y si realmente no está embarazada?!"

                menu:

                    pt "¡¿Quién coño está decidiendo por mí?!"

                    "<Decirle que se ponga el condón>":
                        call p_Help

                        jump morning06_DfS_Cuf_condomRequest

                    "...":
                        call p_Help

                        jump morning06_DfS_Cuf_condomNo

label morning06_DfS_Cuf_condomNo:

    d "..."

    n "Dídac sigue removiendo sus caderas"

    n "sintiendo tu desnuda polla en su húmeda y cálida vagina."

    if pl.dp > 80:

        d "Pensaba que me sería más complicado convencerte..."

        p "..."

    else:

        d "Así me gusta..."

label morning06_DfS_Cuf_condomRequest:

    p "Dídac..."

    d "..."

    if pl.dp > 80:

        d "Tsssk..."

        d "Vale..."

        d "Si eso te hace más feliz..."

        n "Con un rápido gesto se acerca a la mesita de noche que compartís"

        n "y del cajón saca un preservativo."

        n "Abre el envoltorio con sus dientes."

        p "¿Qué te dije ayer?"

        d "Déjame en paz."

        $ m6_p.condom = True

        n "Con celeridad te cubre el miembro con ese viscoso plástico"

        n "para luego metérsela de nuevo y sin previo aviso"

        n "hasta casi la mitad."

    else:

        d "¿Qué te hace pensar que podrás convencerme?"

        n "Percibes que sigue moviendo sus caderas."

        p "¡Dídac!"

        d "Me gusta cuando te pones gruñón..."

        n "Intentas mover tu cuerpo,"

        n "forcejeando tus brazos para intentar deshacerte de las cadenas que te sujetan"

        n "mientras te retuerces violentamente"

        n "moviendo el torso y la piernas bajo el pesado cuerpo de Dídac"

        n "que te sujeta con maestría y con una sorprendente fuerza."

        n "Pero lo único que consigues es penetrarla aún más."

        p "¡¿Es que se te ha ido completamente la cabeza?!"

        d "Quizás es que me pones muy cachonda..."

        p "..."

label morning06_DfS_Cuf_DidacFirstOrg:

    d "Hmmm..."

    n "Sientes su coño incluso más estrecho que antes,"

    n "como si su carne interina estuviera palpitando."

    d "Dioss...."

    p "¿Qué...?"

    $ m6_d.orgasm += 1

    d "¡Aahhhm...!"

    n "Sus piernas empiezan a temblar y ves su cuerpo en tensión."

    p "Pero si te la acabas de meter..."

    if m6_p.condom:

        pt "Sin mencionar el condón..."

    d "I-"

    extend "imbécil."

    if afternight04__MMouth_Tongue_Success > 0:

        n "Te coge por las mejillas y acerca sus labios hasta ti."

        d "Si no fuera porque me pones tan cachonda..."

        n "Te arranca un beso con lengua"

        n "mientras sigue deslizando sus caderas encima de la tuya."

        menu:

            "¿Soy yo o cada vez te gusta más besarme?":
                call p_Help
                $pl.ch_pts("dp",1)

                d "..."

                $ m6_d.faceSlapGiven += 1
                with hpunch
                ono "SLAP"

                p "¡Joder!"

                p "¿Y este bofetón a que ha venido?"

                d "Para que te calles de una vez."

            "...":
                call p_Help


    n "Sujetándose en tus pectorales intenta aumentar el ritmo de sus caderas."

    d "Aahh-ahhh..."

    n "Percibes sus gemidos a flor de piel"

    n "a medida que intenta tragarse algo más de tu miembro en su estrecha vagina"

    n "en cada nueva acometida."

    p "Ughmm..."

    d "Parece que tienes la polla algo más activa que antes..."

    n "Percibes tu polla palpitando en su cálido interior."

    d "¿No será que estás a punto de...?"

    p "¿Cuánto tiempo llevas follándome?"

    d "Quizás un poco."

    p "Ughh..."

    pt "No puedo más..."

    d "Córrete [protname]."

    if m6_p.condom:

        d "Revienta el condón."

    else:

        d "Explota dentro de mí."

    d "Pero ni se te ocurra pensar que la cosa va a terminar así..."

    p "¡GGhhh..!"

## MC ORGASM 1
    $ m6_p.orgasm += 1

    n "Con todo el cuerpo en tensión y estando esposado por las muñecas"

    n "sientes el particular cosquilleo en tu entrepierna"

    n "con el que terminas explosionando entre la cálida y estrecha carne de Dídac."

    d "Hmmm..."

    d "Joder..."

    n "Con sutileza, se aparta de ti y extendiendo sus rodillas se levanta"

    n "extrayendo tu polla de su cálido interior."

    if not m6_p.condom:

        n "Un chorro blanco y espeso empieza a derramarse por sus labios vaginales"

        n "el cual, poco después, termina cayendo sobre tu erecto y aún palpitante miembro."

    else:

        n "En la cima de tu miembro"

        n "un espeso líquido blanco empapa tu glande casi por completo"

        n "como si fuera el gorro de un pitufo."

    d "Ibas cargadito..."

    d "Me alegra ver que el descanso te haya servido para recargar tus pelotas."

    n "Sientes su cálida entrepierna deslizándose"

    if not m6_p.condom:

        n "por tu empapado miembro."

    else:
        
        n "por el viscoso plástico a lo largo de tu miembro."

    d "Hmfmm..."

    n "Acerca ahí su mano para abrir sus labios menores"

    n "con la clara intención de volver a metérsela dentro."

    $ morning06_DfS_Cuf_condomThrowMouth_Cond = False

    if m6_p.condom:

        p "No seas guarro y cambia el preservativo al menos."

        d "..."

        d "No nos quedan muchos."

        p "Pero hay los suficientes,"

        p "al menos por ahora."

        d "..."

        d "Vale."

        n "Se acerca al cajón de la mesita de noche"

        n "extrae uno del paquete"

        n "y te lo lanza encima de ti."

        d "Toma."

        p "..."

        d "..."

        d "Mierda..."

        n "Se pone de cuclillas ante ti."

        d "Supongo que no hay más remedio."

        n "Acerca sus manos a tu -aún bastante erecto- miembro"

        n "cubierto por ese plástico viscoso"

        n "y con la punta rellena de tu -cada vez más frío- esperma."

        d "Ughh..."

        n "Sin demasiada gracia termina retirándote el preservativo."

        menu:

            "¿Por que no pruebas echártelo por la boca?":
                call p_Help

                $ morning06_DfS_Cuf_condomThrowMouth_Cond = True

                d "..."

                if pl.dp > 80:

                    d "No digas gilipolleces."

                else:

                    d "¿Por qué no te doy una hostia?"

                if afternight04_CumInMouth > 0 or afternight04_CumInThroat > 0:

                    p "Antes de ayer no te dio tanto asco."

                    if afternight04_CumInMouth > 0:

                        d "Agarrándome por la cabeza,"

                        d "tampoco es que me dieras muchas opciones."

                    else:

                        d "¡Te me corriste directamente en el estómago!"

                    # FOR_FUTURE

                    # p "¿Y qué me dices de ayer?"

                    # d "..."

                    d "No es lo mismo que te me corras directamente a la boca"

                    d "que sacarlo de un condón ya frío."

                    d "O sea..."

                    d "¡No me jodas!"

                p "..."

            "Hazle un nudo.":
                call p_Help

                d "Ya lo sé,"

                extend " ya lo sé..."

            "...":
                call p_Help

                d "¿Qué?"

                p "No he dicho nada."

                d "Hmm..."

        n "Con el mismo rostro termina haciéndole el nudo al preservativo"

        n "y lo tira por ahí sin mirar dónde."

        n "Usando sus dientes se deshace del embalaje."

    p "¿No lo vas a limpiar primero?"

    d "¿Limpiar?"

    d "No tengo ningún trapo a mano precisamente."

    p "Me refiero con tu lengua."

    d "..."

    if morning06_DfS_Cuf_condomThrowMouth_Cond:

        d "¿Otra vez con eso?"

    else:

        d "¿Por qué iba a hacer eso?"

    if afternight04_CumInMouth > 0 or afternight04_CumInThroat > 0:

        p "No parece que te disgustase tanto la última vez."

        d "..."

    p "Además,"

    p "quieres que se mantenga bien dura,"

    p "¿no?"

    d "..."

    n "Sientes que vuelve a metérsela dentro."

    d "No parece que necesite de mi lengua"

    d "para que se mantenga cómo dices."

    p "..."

    if not m6_p.condom:

        d "Además,"

        d "así parece que entra mejor..."

    n "Sin prisas, y posando sus manos sobre tu pecho,"

    n "desciende sus caderas hasta hundir casi la mitad del mismo en cálido interior."

    n "Acerca su cuerpo al tuyo hasta sentir sus pechos contra tu piel"

    n "y su respiración a escasos centímetros de tus labios."

    d "No sé si es porque estoy cachonda"

    d "o por que tu polla me vuelve loca,"

    d "pero viéndote de cerca"

    d "tampoco eres tan feo."

    p "..."

    n "Sus caderas vuelven a recobrar el ritmo."

    d "Hmmm..."

    n "Sientes sus uñas clavándose en tu piel."

    p "Dídac..."

    d "Ahahh..."

    p "¡Dídac!"

    d "¡AAAhhh!"

    pt "¡La madre que lo parió!"

    $ m6_d.orgasm += 1 # Didac 2nd Orgasm

    n "Detiene el vaivén de sus caderas."

    n "Su carne interina ahoga con más ímpetu tu erecto miembro."

    n "Sus piernas tiemblan con más intensidad"

    n "al mismo tiempo que la parte superior de su cuerpo"

    n "desciende hasta que su cabeza termina reposando sobre tu cuello."

    n "Manteniendo la presión para mantener tu polla en su interior,"

    n "sus caderas siguen temblando sin control"

    n "mientras percibes su cálida respiración y sus agudos gemidos cerca de tu oreja."

    d "Dios..."

    n "No estás seguro si su respiración es tan agitada que mueve sus labios sin control"

    n "o si realmente está besándote por el cuello."

    d "Realmente me pones muy cachonda."

    n "Su respiración a flor de piel te causa cierto cosquilleo."

    $ morning06_DfS_Cuf_rideBack_Cond = False

    menu:

        "Nunca te hubiera imaginado tan romántica.":
            call p_Help
            if pl.dp > 80:
                $pl.ch_pts("dp", 2)

            $ morning06_DfS_Cuf_rideBack_Cond = True

        "Me alegra oír eso.":
            call p_Help
            $pl.ch_pts("dp", 1)

            d "Hmmm..."

        "...":
            call p_Help
            pass

    jump morning06_DfS_Cuf_rideYou

label morning06_DfS_Cuf_rideYou:

    if morning06_DfS_Cuf_rideBack_Cond:
    
        d "¿Romántica...?"

    n "Vuelve a ponerse de pie sacándosela de su interior."

    p "¿Qué haces?"

    if morning06_DfS_Cuf_rideBack_Cond:

        if af5_d.assSmacks > 2 or afternight04__Buttock_Slap_Both_Done > 2:

            if af5_d.assSmacks > 2 or afternight04__Buttock_Slap_Both_Done > 2:

                d "Tanto ayer como antes de ayer me diste bastantes nalgadas,"

            elif af5_d.assSmacks > 2:

                d "Ayer me diste bastantes nalgadas,"

            elif afternight04__Buttock_Slap_Both_Done > 2:

                d "Antes de ayer me diste bastantes nalgadas,"

            d "así que me imagino que te gusta bastante mi trasero."

    else:

        d "Nada..."

        d "Simplemente me gusta verla,"

        d "antes de volver a metérmela dentro."

    if morning06_DfS_Cuf_rideBack_Cond:

        n "Dándote la espalda y sujetándotela con suavidad -y un toque de malicia-,"

    else:

        n "Con suavidad,"

    n "empieza acariciar sus cálidos labios vaginales con tu erecto miembro."

    n "Finalmente la envuelve de nuevo con su cálida carne"

    n "y sin apenas darte tiempo a reaccionar"

    if morning06_DfS_Cuf_rideBack_Cond:

        n "y sin verle el rostro,"

        n "sus nalgas empiezan a descender a lo largo de tu miembro"

    else:

        n "sus caderas empiezan a descender a lo largo de tu miembro"

    n "hasta que casi la mitad del mismo termina enterrándose en su estrecha vagina."

    d "Joder..."

    n "Arqueando su espalda y estando de rodillas"

    n "empieza a balancear el peso de su cuerpo contra tu pelvis"

    n "oyendo sus gemidos en cada nueva acometida."

    n "Percibes el angosto espacio de su coño"

    n "que intenta tragarse más tu miembro cada vez que desciende sus caderas."

    n "En sus gemidos te parece oír algún tondo de dolor pero aún así su marcha no desacelera."

    n "Vuelves a sentir el particular cosquilleo en tu entrepierna."

    if morning06_DfS_Cuf_rideBack_Cond:

        n "Mirándote de reojo te lanza una sonrisa pícara."

    else:

        n "Mirándote desde la cima te lanza una sonrisa pícara."

    n "Con sus músculos internos intenta ahogarte aún más tu miembro"

    n "aferrándose a él con más ímpetu."

    n "Apenas eres capaz de ver la carne de tu miembro cuando desciende sus caderas."

    p "Ughh..."

    n "Sus piernas empiezan a temblar y su ritmo desacelera."

    d "Ahhhmmm..."

    n "Teniéndola casi por completo enterrada en su interior"

    n "remueve sus caderas en círculos"

    n "mientras sientes tu polla convulsionar en su estrecha y cálida carne."

    pt "No puedo más..."

    n "Su coño se expande y se contrae mientras tu polla palpita incontroladamente"

    n "hasta que finalmente:"

    with vpunch
    p "¡Uughhh!"

    d "¡¡Jodeeer!!"

    $ m6_p.orgasm += 1
    $ m6_d.orgasm += 1

    n "Percibes el líquido blanco emerger de tu palpitante miembro"

    if m6_p.condom:

        n "rellenando el viscoso plástico que te envuelve"

    else:

        n "rellenando su interior con tu semilla"

    n "al mismo tiempo que su cálida carne sigue aferrándose a ti"

    n "como si fuera un pulpo agarrando a su presa."

    n "Sus piernas siguen temblando a medida que tu miembro sigue escupiendo tu líquido blanco"

    n "meneando sus caderas casi como si quisiera exprimirte hasta la última gota."

    d "Aahhh-ahhh..."

    n "Su respiración se va normalizando"

    n "y sus piernas cesan paulatinamente en su tembleque involuntario."

    n "Un longevo suspiro emerge de entre sus labios."

    d "Jodeer..."

    d "Dios."

    d "Me podría pasar el día así."

label morning06_DfS_Cuf_3dRoundStart:


### Más de 3/4 de tu polla han llegado a entrar en este punto.

    # 3a corrida de ella es ella follándote en plan amazónico

    if morning06_DfS_Cuf_rideBack_Cond:

        n "Sujetándose con más solidez de tus pies,"

    else:

        n "Sujetándose con más solidez de tu pectoral,"

    n "recupera la posición flexionando sus piernas"

    n "hasta que consigue desprenderse de tu aún palpitante miembro viril."

    ono "flop"

    if not m6_p.condom:

        n "Completamente empapado en tu propio esperma y sus jugos."

        n "Sus labios vaginales están bañados en una burbujeante y espesa espuma blanca"

        n "de dónde surge tu -más reciente- líquido blanco"

        n "que termina cayendo de nuevo sobre tu miembro."

        d "Está claro que si no me has dejado preñada con la corrida anterior,"

        d "lo habrás hecho con esta."

    else:

        n "No solo el condón está empapado en sus jugos,"

        n "sino que toda tu ingle, testículos y hasta -debido a las salpicaduras en sus orgasmos-"

        n "parte de tu ombligo, están embadurnados"

        n "por su cálido, blanquecino y algo espeso líquido vaginal."

        n "Tu glande está bañado en tu esperma dentro del globo adulto"

        n "con la punta de este otra vez en forma de gorro de pitufo."

    if morning06_DfS_Cuf_rideBack_Cond:

        n "Dídac se da la vuelta mostrándote una sonrisa pícara y maliciosa."

        d "¿Tanto te ha gustado mi trasero?"

        d "¿O es que te ha molado que te estrujara los huevos?"

    else:

        n "Dídac te dedica una sonrisa pícara y maliciosa."

        d "Parece que mi cuerpo desnudo no te disgusta tanto."

        d "¿O es que te mola lo estrecha que soy ahí abajo?"

    if (afternight04_Pussy_dick_deep_Speed_0_Success > 0 
        or afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0):

        if afternight04_Pussy_dick_deep_Speed_0_Success > 0:
            d "Aún no he logrado que entre por completo"

        elif afternight04_Pussy_dick_deep_Speed_0_Rape_Done > 0:

            d "Aún no he logrado que entre por completo"

        d "como hice antes de ayer,"

        d "pero dame tiempo."


    elif (afternight04_Pussy_dick_med_Speed_0_Success > 0 or
        afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0):

        d "¿Soy yo"

        if afternight04_Pussy_dick_med_Speed_0_Rape_Done:

            d "o ya ha entrado más de lo que llegué a metérmela antes de ayer?"

        elif afternight04_Pussy_dick_med_Speed_0_Success:

            d "o ya ha entrado más de lo que tú llegaste a metérmela antes de ayer?"

    p "..."

    n "Ves que vuelve a descender sus caderas dispuesta a metérsela de nuevo."

    d "Ey,{w=0.25}{nw}"

    extend " ey,{w=0.25}{nw}"

    extend " ey..."

    d "¡¿Por qué coño se está aflojando?!"

    p "Ya llevo dos corridas..."

    d "¡Pero puedes aguantar hasta tres corridas!"

    d "¡¿No?!"

    p "Sí,"

    extend " pero no está igual de dura en la primera"

    p "que en la tercera..."

    d "..."

    d "Está toda pringosa..."

    p "No es solo mi esperma lo que hay ahí."

    d "Ya lo sé."

    d "Aún así..."

    n "Una expresión entre la incertidumbre y el deseo se dibuja en su rostro."

    menu:

        "¿Por qué no le das un repaso con tu lengua?":
            call p_Help
            pass

        "...":
            call p_Help

            jump morning06_DfS_Cuf_3dHandJob
                # d "Hmmm..."
                # n "Se aleja de ti en dirección al cajón de la mesita de noche."
                # d "¿Dónde coño está?"
                # p "¿Qué estás buscando?"
                # d "Esto."
                # n "De ahí saca un pañuelo."


    d "¿Qué?"

    d "Estás de coña."

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        # What about yesterday? af5_p.cum? not sure.

        p "Ya lo hiciste antes de ayer..."

        if afternight04_CumInThroat > 0:

            d "¡Te me corriste directamente al estómago!"

        elif afternight04_CumInMouth > 0:

            d "¡Tampoco es que me dieras muchas opciones!"

    p "Dale una oportunidad."

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        p "Quizás te gusta más de lo que eres capaz de confesar."

    else:

        p "Quizás te guste más de lo que te imaginas."

    d "..."

    n "Desciende su rostro mientras agarra tu polla"

    n "notablemente más flácida."

    if afternight04__MMouth_dick_Success > 0 and pl.dp > 80:
        pass

    else:
        jump morning06_DfS_Cuf_3dHandJob
            # d "Hmmm..."
            # n "Se aleja de ti en dirección al cajón de la mesita de noche."
            # d "¿Dónde coño está?"
            # p "¿Qué estás buscando?"
            # d "Esto."
            # n "De ahí saca un pañuelo."


    d "Tssk...."

    if m6_p.condom:

        n "Sin demasiada dulzura,"

        n "agarra el empapado condón que sigue vistiendo tu miembro"

        with vpunch
        n "y te lo arranca casi de golpe."

        p "¡Joder!"

        p "¡Se un poco más delicada!"

        d "..."

    n "Acerca su nariz a tu miembro."

    d "..."

    p "¿Qué pasa?"

    d "Huele..."

    p "¿Huele mal?"

    d "..."

    d "No particularmente..."

    p "¿Entonces?"

    d "..."

    n "Desliza su lengua tímidamente por la mitad de tu -cada vez más flácido- miembro."

    d "Hmmm..."

    p "¿Y bien?"

    d "¿Y bien qué?"

    p "¿Qué tal sabe?"

    d "..."

    d "Déjame en paz."

    n "Acerca su mano a la base de tu miembro"

    n "acariciando con sus dedos el espeso y blanquecino líquido que la rodea."

    n "Aparta esa empapada mano para acercársela a sus labios."

    d "Hmmm..."

    p "No parece que te disguste."

    d "..."

    d "¿Te quieres callar?"

    n "Vuelve acariciarla con esa misma mano sin quitarle ojo de encima."

    p "Quizás es que también saboreas tu propio jugo..."

    with hpunch
    p "¡Oouuch...!"

    n "Te agarra la polla con tanta autoridad"

    n "que te da la sensación que te la arrancará en cualquier momento."

    d "¡¿Es que hablo jodido chino?!"

    p "Va-"

    extend "vale..."

    n "Te libera de ese agarrón."

    p "Aahh...."

    n "Para luego seguir deslizándola a lo largo de tu mástil"

    n "embadurnándose con los restos de su jugos y tu fría semilla."

    $ m6_d.sexActions.append("blowjob")

    n "Acerca sus labios."

    n "Con su lengua saborea la sensible piel de la cima."

    n "A medida que desliza sus embadurnados dedos a lo largo de tu miembro"

    n "sientes sus labios moviéndose alrededor del glande junto a su lengua."

    n "Cuando su mano alcanza esa cumbre,"

    n "usa su lengua para relamer sus empapados dedos"

    n "sin abandonar sus mimos a tu sensitiva piel."

    n "Cerrando los ojos y con un rostro sereno"

    n "relame esa parte como si estuviera degustando un exquisito elixir."

    n "Expande sus labios alrededor de tu glande."

    n "Sientes el calor de su boca abrazándote el capullo por completo"

    n "jugueteando con tu sensible y cada vez más rojiza superficie"

    n "mientras sus dedos acarician la piel cercana a sus labios y tu glande."

    n "Parece inducida, ignorándote por completo;"

    n "casi como si en la habitación solo estuviera ella y tu polla."

    n "Sus labios descienden más allá del glande,"

    n "relamiendo y succionando lo que encuentra en su camino."

    n "Sin apartar sus labios de esa sensible carne"

    n "te libera de su cálido interior,"

    n "descendiendo a lo largo de tu miembro"

    n "relamiendo y succionando cada tramo con esmero y deseo."

    n "Termina llegando a la base del mismo relamiendo ese pequeño charco"

    n "con todo el líquido que se ha desprendido debido a la gravedad."

    ono "slurp"

    n "Para proseguir su camino hasta tus testículos,"

    n "cubiertos por su -ya fría y no tan espesa- corrida vaginal"

    n "junto con algún resto de tu propio esperma"

    n "Dedicando esmero y tiempo hasta que solo su cálida saliva"

    n "impregna la piel de tu bolsa escrotal."

    p "Ughh..."

    n "Te los succiona con tanta energía"

    n "que tienes la sensación de que te acabará sacando un huevo de ahí."

    n "Pensaba que habías dicho que hacer esto te daba asco."

    d "..."

    n "Con tu mástil -cada vez más duro y erecto- por en medio,"

    n "y sin apenas dejar de usar su lengua"

    n "te dirige una mirada entre el deseo y la indiferencia."

    d "Cállate."

    n "Abandonando tu bolsa escrotal regresa,"

    n "repasando cada tramo con su lengua hasta la misma base"

    n "para luego seguir deslizándose por tu piel"

    n "hasta llegar a tu ombligo,"

    n "dónde termina por limpiar los últimos restos -algo ya más resecos- de tu esperma"

    n "que habían terminado cayendo en esa parte."

    p "Ni duchándome quedaría tan limpio."

    d "..."

    n "Su rostro muestra una mueca entre la rabia y la decepción."

    p "¿Ocurre algo?"

    d "..."

    n "Sin mediar palabra regresa a la cima de tu -ya bastante más- erecto miembro"

    n "y se lo vuelve a introducir en sus fauces."

    n "Sin pizca de vergüenza, desciende su rostro"

    n "tragándose hasta casi la mitad sin pudor ni pero con un cierto esfuerzo"

    n "intentando juguetear internamente con su lengua sobre tu piel,"

    n "especialmente cuando tiene espacio para hacerlo,"

    n "empapándotela con su propia saliva."

    n "Relamiéndotela cuando está en la cima"

    n "para luego darte cabezadas más bruscas y aceleradas"

    n "usando una mano para acariciarte los testículos"

    n "y la otra para masturbarte la base"

    n "mientras sigue llegando más y más lejos en cada nueva acometida"

    n "con sus ojos cerrados, casi como si ni siquiera estuvieras delante de ella."

    pt "Joder..."

    n "Hace un esfuerzo mayúsculo para intentar llegar más lejos"

    n "topándote con la carne de su garganta como muro"

    n "en todas y cada uno de sus acometidas."

    n "No solo has recuperado la erección,"

    n "si no que empieza a palpitar con energía"

    n "entre su áspera y juguetona lengua y el calor de su boca."

    pt "¿Es que no lo está notando?"

    n "Sigue dándote cabezadas como si estuviera disfrutando de un elixir imposible de abandonar."

    p "Ughhh..."

    menu:

        "<Avisarla de que te vas a correr>":
            call p_Help
            $pl.ch_pts("dp",1)

            jump morning06_DfS_Cuf_3dWarning

        "...":
            call p_Help

            jump morning06_DfS_Cuf_3dMouthCum

            

label morning06_DfS_Cuf_3dMouthCum:
    $ m6_d.sexActions.append("cumMouth") ##Is this really a sex action?

    n "Percibes el particular cosquilleo recorrer tu entrepierna"

    n "a la par que el muro de su garganta se va volviendo más blando"

    n "y tu polla sigue desapareciendo, tramo a tramo, en sus fauces."

    n "Empieza a palpitar con energía en el interior de su garganta"

    n "a medida que su mano sigue masajeandote la polla con agarro y velocidad."

    n "Percibes que estás a punto de estallar"

    n "sin que se detenga en absoluto."

    p "Ughh..."

    n "Tus piernas tiemblan y sientes tu esperma recorrer tu entrepierna"

    n "hasta que finalmente:"

    d "¡¿Uhg?!"

    n "Dídac se aparta instintivamente de tu polla"

    n "mientras embadurnas su rostro con tu espesa explosión."

    d "¡¿Pero qué cojones?!"

    d "¡[protname]!"

    n "Sigues expulsando esperma por tu polla"

    n "mientras su mano se va embadurnado de tu blanquecino líquido."

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        n "Sin mediar palabra regresa a tu polla hundiéndola en sus fauces más allá del capullo."

        n "Sientes tu corrida explosionando en su cálida boca"

        n "mientras su lengua revolotea por la parte sensible de tu miembro"

        n "A pesar del rostro colérico que te dedica"

        n "percibes como absorbe con ímpetu tu esperma llevándoselo hacia su estómago"

        n "como si realmente estuviera disfrutando de tu elixir blanco."

        n "Su mirada regresa al tema en cuestión"

        n "al mismo tiempo que sus manos, las cuales te masturban con brío,"

        n "como si quisiera arrebatarte las últimas gotas que apenas te quedan."

        p "Ugh..."

        n "Te succiona y te masturba con tanto arrojo"

        n "que tienes la sensación que te arrancará la polla de cuajo."

        n "Con un rostro entre abducido y colérico se aparta de él."

    else:

        n "Te agarra la polla con tanta fuerza"

        n "que te impide expulsar más líquido blanco."

        d "¡Te hecho una pregunta!"

        p "Guuuhh..."

        d "¡¿Qué cojones haces corriéndote en mi boca sin avisarme?!"

        n "Su voz es colérica y su expresión de ira absoluta."

        p "Mi po-"

        extend "polla..."

        n "Cuando tu polla empieza a tomar un tono azulado"

        n "y con una expresión de pocos amigos"

        n "abandona paulatinamente el enérgico agarrón"

        n "hasta que terminas soltando un nuevo chorro  que empapa de nuevo su rostro"

        n "obstaculizándole la visión de un ojo."

        d "..."

        n "Tu polla sigue palpitando en el aire pero apenas saca alguna que otra gota."

    n "Dídac se la queda mirando con un rostro indefinido entre la ira y el deseo."

    d "No..."

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        n "Sus manos te masturban a mayor velocidad."

    else:

        n "Sientes su mano que te la agarra con vigor"

        n "mientras la desliza verticalmente con vehemencia y celeridad."

    d "No."

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        n "A estas alturas sientes casi más dolor que placer."

    else:

        n "Usa ambas para masturbarte el miembro"

    d "NO"

    if afternight04_CumInThroat > 0 or afternight04_CumInMouth > 0:

        n "A pesar de sus esfuerzos"

    else:

        n "pero a pesar de su esfuerzo"

    d "¡NO!"

    n "al paso de los segundos se va volviendo más flácida entre sus dedos."

    d "¡¡NOOO!!"

    n "Hasta que termina doblándose perdiendo por completo su erección."

    d "¡¿Por qué coño se te está volviendo flácida?!"

    p "Eughh..."

    n "Como te suele ocurrir después de tu tercera corrida"

    d "¡[protname]!"

    n "Vas perdiendo poco a poco las facultades del habla."

    d "¡Te estoy hablando!"

    n "Hasta que terminas cerrando los párpados"

    d "¡¡Ni se te ocurra sobarte, hijo de puta!!"

    n "Y solo ves oscuridad."

    jump morning06_Df_afterSex
        # ono "Riiiiiing"
        # P "Uhhmm..."
        # d "¿Aún estás en la cama?"
        # n "Ves a Dídac de pie con una toalla"
        # n "y con el pelo mojado"
        # n "como si se hubiera terminado de duchar."
        # p "¿Cómo es que tienes tanta energía?"


label morning06_DfS_Cuf_3dWarning:

    p "Dídac..."

    n "Sin sacarse la polla de su boca se detiene por un instante."

    d "¿Hmmm...?"

    p "Si sigues así..."

    n "Rápidamente se la aparta de la boca."

    d "¡¿Qué?!"

    menu:

        "Pero si quieres seguir...":
            call p_Help

            d "¡No-"

            extend "no hagas bromas sobre esto!"

            n "Su expresión aparentemente es de enfado,"

            n "pero sus ruborizadas mejillas parecen darte otro mensaje."


        "...":
            call p_Help

            pass

    jump morning06_DfS_Cuf_3dFucking
    

label morning06_DfS_Cuf_3dHandJob:

    d "Hmmm..."

    n "Se aleja de ti en dirección al cajón de la mesita de noche."

    d "¿Dónde coño está?"

    p "¿Qué estás buscando?"

    d "Esto."

    n "De ahí saca un pañuelo."

    n "Vuelve hacia ti y sin demasiada delicadeza"

    if m6.condom:

        with vpunch
        n "te quita el condón de cuajo."

        p "¡No seas tan bruta!"

        d "Mira que eres quejica cuando quieres..."

        n "Para luego limpiártela con esmero"

    else:

        n "empieza a limpiártela"

    n "dejando ese trozo de papel hecho un desastre."

    d "Te has corrido un montón."

    p "Mira quien habla..."

    d "Hmmm..."

    n "Tira ese pringoso pañuelo por el suelo."

    p "No seas tan guarra, joder."

    d "Ya lo limpiaré luego."

    n "Con sus algo más frías manos te sujeta el miembro,"

    n "el cual ha perdido casi la mitad de su volumen"

    n "y apenas se mantiene firme."

    n "Se pone de pie acercando tu flácido miembro a su entrepierna."

    if m6.condom:

        p "¡Ey!"

        p "¡¿Y el condón?!"

        d "Ya te pondré luego el condón, pesado."

        d "Solo quiero comprobar una cosa."

    n "Roza tu polla por sus cálidos labios vaginales"

    n "con la clara intención de introducírsela,"

    n "pero debido a su flacidez"

    n "lo único que consigue es doblarla cada vez que lo intenta."

    d "¡Joder!"

    n "Se vuelve a poner de rodillas"

    n "y con una expresión de pocos amigos"

    n "te agarra la polla enérgicamente y sin demasiada delicadez intenta masturbarte."

    d "No quiero oír ni una palabra."

    menu:

        pt "Como si nunca se hubiera masturbado su propia polla..."

        "¿Por qué te da más corte masturbarme que follarme?":
            call p_Help

            d "¡¿Qué coño te acabo de decir?!"

            p "..."

        "...":
            call p_Help

            pass

    n "Acerca una de sus manos a tus testículos"

    n "y ejerciendo una fuerza innecesaria"

    n "y falta absoluta de tacto hace un \"intento\" de acariciarlos."

    p "Dídac..."

    d "¿Qué coño quieres ahora?"

    p "No seas tan bruta..."

    d "..."

    d "Tsssk..."

    n "Obedeciendo a regañadientes tus palabras"

    n "suaviza su agarre y ralentiza sus movimientos"

    n "arrimándose con suavidad a tus testículos"

    n "y deslizando su mano a lo largo de tu miembro."

    n "Palpa con dulzura la piel que separa el glande del resto del miembro."

    n "Masajeandote el miembro entero con el resto de sus dedos,"

    n "usa el pulgar para juguetear con la abertura de tu polla"

    n "deslizándose por la parte sensible inferior del glande,"

    n "descendiendo hasta la piel que te une con los testículos."

    d "Está algo rojiza..."

    p "Llevo unos días un tanto peculiares."

    d "..."

    n "Su actitud se va suavizando y su masaje se mantiene sosegado pero comedido."

    d "Hmmm..."

    n "A medida que tu riego sanguíneo regresa a tu polla"

    n "Dídac parece darse cuenta de ello y empieza aumentar ligeramente el ritmo."

    pt "Ughh..."

    n "A medida que desliza su mano alrededor de tu miembro"

    n "tienes la sensación que no solo se limita a subir y bajar"

    n "sino que sus dedos juguetean con tu miembro"

    n "como si supiera qué botones presionar"

    n "para que el masaje ofrezca mejores resultados y consiga dar su fruto."

    pt "¿Será que me lo está haciendo como a él le gustaría que se lo hicieran?"

    p "Parece que no se te da tan mal..."

    n "Te lanza una mirada que no estás muy seguro si es de orgullo o de odio contenido."

    n "A pesar de que ha recuperado su tensión casi por completo,"

    n "sus ojos siguen fijándose en ella como si estuviera en trance,"

    n "mordiéndose el labio fijándose en el glande"

    n "y en la gota preseminal que surge e ella."

    n "No solo aumenta progresivamente el ritmo,"

    n "sino que parece darle más variedad, cariño y atención"

    n "como si ella misma estuviera sintiendo placer"

    n "con el simple hecho de hacerte semejante paja."

    n "Toda su expresión es de deseo absoluto y sus ojos están tan centrados en ella"

    n "que tienes la impresión de que ignora por completo tu presencia,"

    n "como si estuviera sola en la habitación"

    n "con tu polla ajena a tu cuerpo flotando en sus manos."

    p "Hmm..."

    n "Su hasta ahora calmado y sosegado masaje"

    n "se va volviendo cada vez más intenso y salvaje."

    n "Tu polla empieza a palpitar con intensidad en sus manos."

    p "Ughh..."

    d "¡¿Euh?!"

    n "Se detiene en seco."

    d "¡Ni se te ocurra correrte así!"

    d "¡¿Me oyes?!"

    p "Ya hace rato que ves que está bien dura,"

    p "y aún así no has parado en ningún momento."

    d "..."

    d "¡Serás imbécil!"

    $ m6_d.sexActions.append("handjob")

    # She needs to clean your dick with a tissue or something, masturbate it a bit... a lot probably... while she bites her lips but refuses to even lick it... and finally she grabs it and fucks you.

    jump morning06_DfS_Cuf_3dFucking


###

label morning06_DfS_Cuf_3dFucking:

    n "Vuelve a ponerse de pie acercando su entrepierna a la punta de tu miembro"

    n "que sigue palpitando por su notable limpieza de sable."

    if m6_p.condom:

        p "Dídac..."

        d "Ghnn..."

        n "Un ligero gruñido surge de sus labios"

        n "a medida que se acerca de nuevo al cajón de la mesita de noche"

        n "de dónde coge otro condón que vuelve a abrir con sus dientes"

        n "y que rápidamente te viste con él."

    d "Hmmm..."

    n "Desciende sus caderas tragándose casi la mitad de tu miembro"

    n "en su cálido y estrecho interior."

    n "Te agarra de las piernas y las eleva por encima de su ombligo."

    p "¿Qué?"

    n "Hunde tu polla al completo al sentarse sobre tu entre pierna."

    d "Hmmm..."

    n "Sujetándose con fuerza de tus extremidades,"

    n "desliza sus caderas sin que puedas hacer nada al respecto."

    d "Así parece que sea yo quién te esté follando."

    p "..."

    n "Posando sus pies sobre la alcoba"

    n "y alzando sus manos hasta agarrarte con fuerza de los tobillos"

    n "acelera el ritmo de sus acometidas"

    n "logrando enterrarlo por completo en su asfixiante vagina."

    d "Jodeer..."

    n "Acelera tanto sus acometidas que te está dejando la ingle rojiza y lastimada"

    n "por los duros impactos de sus nalgas."

    d "AAAhhh-aahahh..."

    n "Sus piernas vuelven a temblar incontroladamente"

    n "hasta el punto de detenerse cuando tiene toda tu polla enterrada en su interior."

    n "Dando pequeños y erráticos rodeos"

    n "sintiendo el calor de su carne aferrándose a la sensible piel de tu miembro."

    $ m6_d.orgasm += 1

    n "Un abundante chorro emerge de su interior"

    n "dejándote toda la entrepierna empapada en su espeso y cálido líquido vaginal."

    d "Dios..."

    n "Sus caderas se detienen, sus gemidos se apaciguan"

    n "y su respiración vuelve a la normalidad."

    d "¿Soy yo,"

    d "o tu polla está palpitando como si estuvieras a punto de correrte de nuevo?"

    if "blowjob" in m6_d.sexActions:
        ##$ m6_d.sexActions.append("blowjob")
        p "Después de la mamada que me has dado antes,"

        p "lo raro es que no me haya corrido ya."

        d "Hmmm..."
    else:

        p "..."

    n "Sin prisas, alza sus caderas"

    n "para luego descender sin piedad"

    with vpunch
    p "¡Ouch!"

    n "tragándose tu rojiza y sensible polla por completo."

    pt "La madre que la parió..."

    n "Sientes el particular cosquilleo en tu entrepierna."

    p "Ughh..."

    n "Tu sensible polla palpita en su interior."

    d "Hmmm..."

    n "Sin mediar otra palabra retoma el ritmo anterior,"

    d "Creo que yo también..."

    n "enterrándosela por completo"

    p "¡Uughh...!"

    n "aumentando en ritmo y salvajismo en cada nueva acometida."

## THIRD CUM Of prot and Didac Cum.

    $ m6_p.orgasm += 1

    n "Percibes tu esperma recorrer por tu entrepierna"

    if m6_p.condom:

        n "hasta que termina estallando en el estrecho preservativo"

        n "rodeado por su cálida y asfixiante carne."

    else:

        n "hasta que termina estallando en su estrecho interior."

    n "Detiene en seco su vaivén,"

    n "removiendo de nuevo sus caderas con tu polla completamente enterrada en su interior."

    d "¡Diooos...!"

    $ m6_d.orgasm += 1

    n "Sus piernas vuelven a temblar"

    n "mientras te agarra con más ímpetu de los tobillos"

    n "gritando entre gemidos y moviéndose en espasmos."

    n "A pesar de que tus huevos están vacíos"

    n "y tu polla empieza a sentir el dolor de la extenuación,"

    n "sigue removiendo sus caderas como si quisiera ordeñarte hasta la última gota."

    d "Hmmmm..."

    n "Te suelta las piernas que terminan cayendo sobre la alcoba"

    n "y con un sutil movimiento desciende su torso"

    if pl.dp > 80:

        n "hasta acercar sus labios a los tuyos para darte un dulce beso."
    else:

        n "hasta acercar sus labios en tu mejilla, dándote un dulce beso."

    n "Para luego terminar apoyando su desnudo cuerpo contra el tuyo"

    n "sintiendo sus pechos aplastándose contra tus pectorales"

    n "y su cabeza reposando en tu cuello"

    n "manteniendo tu polla aún enterrada en su interior."

    scene black
    with fade

    n "Tus párpados empiezan a cerrarse"

    n "mientras oyes sus ligeros gemidos del post-orgasmo"

    n "y su respiración a flor de piel cerca de tu oreja."

    jump morning06_Df_afterSex
        # ono "Riiiiiing"
        # P "Uhhmm..."
        # d "¿Aún estás en la cama?"
        # n "Ves a Dídac de pie con una toalla"
        # n "y con el pelo mojado"
        # n "como si se hubiera terminado de duchar."
        # p "¿Cómo es que tienes tanta energía?"


    # You can ask her or order her to release you.

    # YOU'RE cuffed on the bed, and she wants to fuck you all the three cums, either you were dominant with her or not.

    # In any case, write the goddam scene where you're fucked by her being cuffed.


    
