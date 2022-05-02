


label day06_didacAlone_fuckHer_begin:

    $ day06_didacAlone_sex_order_begin_Cond = False
    $ day06_didacAlone_fuckHer_beforeAnal_Cond = False
    
    #$ day06_morning_Didac_orgasms = 0

    # SHE IS ON DOGGYSTYLE. mOVING her ass.

    menu:

        pt "¿Por dónde?"

        "<Sexo vaginal>":
            call p_Help

            $ day06_didacAlone_sex_vag = True

        "<Sexo anal>":
            call p_Help

            $ day06_didacAlone_sex_vag = False

    n "Acercas tu rojizo y sensible miembro a su empapada y fogosa entrepierna"

    n "mientras con tus manos agarras con fuerza sus nalgas."

    d "Hmm..."

    d "Fóllame..."

    if not day06_didacAlone_sex_vag:

        pt "Aún no se ha dado cuenta en qué agujero estoy apuntando..."

    menu:

        "<Penetrarla>":
            call p_Help

            jump day06_didacAlone_fuckHer_sex

        "<Hacerla sufrir un poco>":
            call p_Help

            jump day06_didacAlone_fuckHer_foreplay

label day06_didacAlone_fuckHer_foreplay:

    n "Ignorando su orden,"

    if day06_didacAlone_sex_vag:

        n "deslizas tu miembro a lo largo y ancho de sus cálidos labios vaginales"

        n "mientras intentas acariciar su clítoris con tu rosado glande."

        d "Hmmmfhmm..."

        d "Dejáte de hostias y fóllame de una vez..."

    else:

        n "deslizas tu miembro juguetonamente por la superficie de su orificio anal."

        d "Un momento..."

        call day06_didacAlone_fuckHer_beforeAnal_label

        d "Ghmmm..."

        d "Si vas a follarme el culo,"

        d "por lo menos ten la decencia de hacerlo de una jodida vez."

    pt "Realmente está cachonda."

label day06_didacAlone_fuckHer_beforeAnal_label:

    $pl.ch_pts("dp",-3)

    $ day06_didacAlone_fuckHer_beforeAnal_Cond = True
    #$ day06_didacAlone_fuckHer_beforeAnal_Str = "asked"

    d "¡¿Es que me estás tomando el pelo?!"

    p "¿Por qué lo dices?"

    if p_didac.anal_received > 3:
    
        d "¡¿Va en serio que quieres volverme a follar el culo?!"

        if p_didac.vaginalDeep_received > 2:

            p "Ayer te la metí hasta el fondo"

            p "y no pareció disgustarte tanto."

            $pl.ch_pts("dp",1)

            d "..."

        else:

            p "Ayer no pareció disgustarte tanto."

            d "¡Joder!"

        d "¡Vale!"

        d "¡No me disgustó!"

        d "¡¿Estás más contento si te digo esto?!"

        p "..."

    else:

        if p_didac.anal_received == 0:

            d "¡Pero si ayer ni siquiera me la metiste por ahí!"

            if afternight04__Anal_dick_med_Success > 1:

                p "Pero sin embargo, antes de ayer sí logré metértela más de una vez..."

                d "..."

                d "Si de verdad te gustase tanto,"

                d "me lo habrías hecho ayer también."

                p "..."

            else:

                p "Es posible..."

        else:

            d "¡Pero si ayer solo me la metiste por ahí [p_didac.anal_received] veces!"

            p "Quizás por eso quiero repetir."

        d "¡Simplemente lo haces para tocarme las narices!"

        d "¿Por qué no puedes follarme como una persona normal?"

        p "Dirás como a una mujer enfermizamente cachonda como tú."

        d "..."

        d "Serás imbécil..."

        p "¿Qué has dicho?"

        d "¡Nada!"

    d "¡Ahora fóllame el coño y déjate de mariconadas!"

    $ day06_didacAlone_fuckHer_beforeAnal_Str = "asked"

    menu:

        pt "Que me deje de mariconadas, dice..."

        "Suplícamelo y quizás me lo plantee.":
            call p_Help
            pass

        "<Hacerle caso y follarle el coño>":
            call p_Help
            $pl.ch_pts("dp",2)
            $ day06_didacAlone_sex_vag = True
            jump day06_didacAlone_fuckHer_sex

        "<Ignorar sus palabras y follarla analmente>":
            call p_Help
            $ day06_didacAlone_sex_vag = False
            jump day06_didacAlone_fuckHer_sex

##

    d "..."

    d "Estas de coña,"

    d "¿verdad?"

    p "No."

    d "..."

    d "Tssk..."

    d "Por favor..."

    d "¿podrías follarme como un hombre...?"

    d "¿¡y dejarte de mariconadas!?"

    $ day06_didacAlone_fuckHer_beforeAnal_Str = "likeMan"

    menu:

        pt "Pesadita con las mariconadas..."

        "<Hacerle caso y follarle el coño>":
            call p_Help
            $pl.ch_pts("dp",2)
            $ day06_didacAlone_sex_vag = True
            jump day06_didacAlone_fuckHer_sex

        "He visto perros que lo piden mejor que tú.":
            call p_Help
            #$pl.ch_pts("dp",-1)

            d "¡¿Me estás comparando con un perro?!"

            p "Más bien con una perra en celo."

            d "¡La madre que te...!"

            p "¿Qué le pasa a mi madre?"

        "¿Este es tu modo de pedir algo?":
            call p_Help
            pass

        "<Azotarle una nalga>":
            call p_Help

            $ day06_morning_Didac_buttockSlaps += 1

            with hpunch
            d "¡Auch!"

            p "Lo único que estás consiguiendo"

            p "es que tenga más ganas de follarte el trasero."

        "<Ignorar sus palabras y follarla analmente>":
            call p_Help

            $ day06_didacAlone_sex_vag = False
            jump day06_didacAlone_fuckHer_sex

    d "..."

    d "Por favor [protname],"

    d "te lo pido de verdad..."

    d "fóllame el coño."

    $ day06_didacAlone_fuckHer_beforeAnal_Str = "please"

    menu:

        pt "¿Puedo tomarme eso cómo una súplica?."

        "<Follarle el coño>":
            call p_Help
            $pl.ch_pts("dp",2)
            $ day06_didacAlone_sex_vag = True
            jump day06_didacAlone_fuckHer_sex

        "Creo que te falta decir algo más.":
            call p_Help
            pass

        "<Ignorar sus palabras y follarla analmente>":
            call p_Help
            $ day06_didacAlone_sex_vag = False
            jump day06_didacAlone_fuckHer_sex


    d "..."

    d "Te lo suplico..."

    p "Hmmm..."

    $ day06_didacAlone_fuckHer_beforeAnal_Str = "beg"

    menu:

        pt "Realmente quiere sentirla en su vagina..."

        "Es posible que esto suene algo mejor.":
            call p_Help

            d "Idiota..."

            p "¿Qué has dicho?"

            d "Nada,"

            extend " nada..."

        "Sigue siendo una súplica bastante lamentable.":
            call p_Help
            $pl.ch_pts("dp",-1)

            d "¡Vete a...!"

            p "¿Sí?"

            d "..."

            p "¿Que me vaya dónde?"

            d "..."

            d "Por favor..."

            d "Te lo suplico."

            p "..."

        "...":
            call p_Help
            pass

    menu:

        pt "¿Por dónde...?"

        "<Follarle el coño>":
            call p_Help
            $pl.ch_pts("dp",2)
            $ day06_didacAlone_sex_vag = True
            jump day06_didacAlone_fuckHer_sex

        "<Ignorar sus palabras y follarla analmente>":
            call p_Help
            $ day06_didacAlone_sex_vag = False
            jump day06_didacAlone_fuckHer_sex

    return

label day06_didacAlone_fuckHer_sex:

    if day06_didacAlone_sex_vag:

        n "Con cierta facilidad, logras penetrar la punta de tu miembro en su angosto y cálido interior."

        d "Seehh..."

        if day06_didacAlone_fuckHer_beforeAnal_Cond:

            d "¿Ves cómo tampoco era tan mala idea?"

            p "Será mejor que te calles antes de que cambie de opinión."

            d "..."

    else:

        if day06_didacAlone_fuckHer_beforeAnal_Cond:

            n "Enfocando la punta de tu miembro en su agujero anal, empujas tus caderas"

            with vpunch
            d "¡Ugh!"

            n "logrando así penetrar su estrecho orificio."

            if day06_didacAlone_fuckHer_beforeAnal_Str in ["beg", "please"]:
                $pl.ch_pts("dp",-9)

                d "¡HIJO DE PUTA!"

                if day06_didacAlone_fuckHer_beforeAnal_Str == "beg":

                    d "¡HASTA TE LO HE PUTO SUPLICADO!"

                elif day06_didacAlone_fuckHer_beforeAnal_Str == "please":

                    d "¡Hasta te he pedido por favor, joder!"

                p "Pero al fin y al cabo es mi decisión."

                d "..."

                d "Con que esas tenemos..."

                jump day06_didacAlone_sex_order_begin
                    # n "Ves que se aparta de ti y se vuelve a poner a cuatro patas sobre la cama."
                    # pt "No estará haciendo lo que creo que está..."

            elif day06_didacAlone_fuckHer_beforeAnal_Str == "likeMan":

                d "¡La madre que te parió!"

                p "Me has dicho que te folle como un hombre,"

                p "¿no?"

                d "¡¿Y entonces por qué coño me follas el culo?!"

                p "Porque así es como follan los hombres entre sí."

                d "¡Serás imbé...!"

                d "¡Ugh!"

                d "..."

                d "Idiota..."

            else:

                #$ day06_didacAlone_fuckHer_beforeAnal_Str = "asked"

                d "¡Serás capullo!"

                d "¡Te he pedido que no me folles por ahí!"

                menu:

                    "¿A eso lo llamas pedir?":
                        call p_Help

                        p "La próxima vez inténtalo hacer mejor."

                        d "..."

                        d "Tsskk..."

                        d "Con que esas tenemos..."

                        jump day06_didacAlone_sex_order_begin
                            # n "Ves que se aparta de ti y se vuelve a poner a cuatro patas sobre la cama."
                            # pt "No estará haciendo lo que creo que está..."

                    "Haré lo que me de la gana.":
                        call p_Help
                        $pl.ch_pts("dp",-2)

                        d "..."

                        d "¿En serio?"

                        d "¿Es así cómo vamos a jugar?"

                        p "Eso parece."

                        d "Hmm..."

                        jump day06_didacAlone_sex_order_begin
                            # n "Ves que se aparta de ti y se vuelve a poner a cuatro patas sobre la cama."
                            # pt "No estará haciendo lo que creo que está..."

                    "Me gusta follarte el trasero.":
                        call p_Help

                        d "..."

                        d "Lo que tú digas..."

                    "...":
                        call p_Help

            p "¿Quieres que la saque?"

            d "Tsskk..."

            d "¡Haz lo que te salga de los cojones!"

            pt "Esa es la idea..."

        else:

            n "Con cierta gracilidad, presionas con la punta de tu polla su orificio anal"

            n "con la intención de penetrar en su interior."

            d "¡¿Euh...?!"

            d "¡Un momento!"

            d "¡¿Qué coño estás haciendo?!"

            p "¿No es obvio?"

            call day06_didacAlone_fuckHer_beforeAnal_label
                # d "¡¿Es que me estás tomando el pelo?!"
                # p "¿Por qué lo dices?"
                # d "¡¿Va en serio que quieres volver a follarme el culo?!"

    n "Deslizas tu miembro hasta hundir la mitad del mismo en su interior."

    d "Coño..."

    d "Que pollón tienes, joder..."

    n "Sin prisas, empiezas a desplazar tu miembro en horizontal en su ahogado y carnoso interior."

    d "¿A eso lo llamas follar?"

    d "¡Dame más duro, coño!"

    if not day06_didacAlone_sex_vag:

        p "Suerte que no te gusta el anal."

        d "..."

    menu:

        pt "La verdad es que tiene un buen culo..."

        "<Azotarle las nalgas mientras te la follas>":
            $ day06_morning_Didac_buttockSlaps += 1

        "<Seguir sin azotarle las nalgas>":
            $ day06_morning_Didac_buttockSlaps = 0

    if day06_morning_Didac_buttockSlaps > 0:

        with hpunch
        d "¡Auch!"

        d "¡Te he dicho que me folles más duro,"

        d "no que me azotes las nalgas!"

        if p_didac.buttockSlaps_received > 2:

            p "Ayer también te quejaste,"

            p "pero luego bien que te gustó..."

            d "..."

            d "Idiota..."

        else:

            p "No te quejes tanto,"

            p "que en el fondo sabes que te encanta."

            d "Tssk..."

    n "Emprendes la marcha y empiezas a follar con más dureza"

    if day06_didacAlone_sex_vag:

        n "el estrecho coño de tu ex-compañero de piso."

        d "Seeehh..."

    else:

        n "el estrecho ano de tu ex-compañero de piso."

        d "Hmmm..."

    p "Ughh..."

    n "A pesar del cosquilleo y gozo que sientes"

    if day06_didacAlone_sex_vag:

        n "al follar ese estrecho y caliente coño,"

    else:

        n "al follar ese estrecho y caliente ano,"

    n "sientes un dolor punzante en tu polla."

    d "¡Dame más duro!"

    if day06_morning_Didac_buttockSlaps > 0:

        $ day06_morning_Didac_buttockSlaps += 1

        with hpunch
        d "¡Auch!"

        d "Cabrón..."

    n "Sigues embistiendo con dureza su caluroso interior"

    if day06_didacAlone_sex_vag:

        n "a media que percibes su coño cada vez más hostil"

    else:

        n "a medida que percibes su cuerpo temblar con más intensidad"

    n "y sus gemidos aumentan de volumen."

    pt "¿Qué diablos?"

    d "AAaahhhhmm...."

    $ day06_morning_Didac_orgasms += 1

    n "Un considerable chorro de líquido ligeramente espeso"

    if day06_didacAlone_sex_vag:

        n "logra expulsar tu polla de su interior"

        n "mientras esta se derrama a lo largo de tu miembro, tus testículos y tus piernas."

    else:

        n "se derrama a lo largo de tus piernas salpicando ligeramente tus testículos."

    d "Diiooos...."

    d "Joder..."

    d "Cuánto necesitaba esto..."

    pt "A veces tiene unos orgasmos bastante aparatosos."

    d "No pares ahora..."

    if day06_didacAlone_sex_vag:

        n "Vuelves a introducir tu miembro en su interior -que sigue estando igual de húmedo y caliente-,"

        n "y sin más dilación prosigues con la misma marcha que antes."

    else:

        n "Sin más dilación prosigues con la misma marcha que antes."

    if day06_morning_Didac_buttockSlaps > 0:

        $ day06_morning_Didac_buttockSlaps += 1

        with hpunch
        d "¡Auch!"

        d "¡¿Es que no te vas a cansar de azotarme?!"

        p "Mientras sigas gimiendo de esta manera,"

        p "no lo creo."

        d "Tssk..."

        d "Mientras me folles de esta manera..."

    if (day06_didacAlone_sex_vag and p_didac.vaginal_received > 2 and afternight04_Pussy_dick_med_Speed_0_Success > 2) or (day06_didacAlone_sex_vag == False and p_didac.anal_received > 2 and afternight04__Anal_dick_med_Success > 2):

        pt "Por qué coño se siente tan estrecho"

        pt "si ya llevo dos días follándomela?"

    else:

        if day06_didacAlone_sex_vag:

            pt "Realmente tiene un coño muy estrecho..."

        else:

            pt "Realmente tiene este agujero muy estrecho..."

    n "Sientes un familiar cosquilleo que recorre tu entrepierna."

    pt "Mierda..."

    #Coinditional

    $ day06_didacAlone_sex_WarnHer = ""

    menu:

        pt "No creo que vaya pueda aguantar mucho más..."

        "<Avisarla de que te vas a correr>":

            $ day06_didacAlone_sex_WarnHer = "True"

            p "Dídac..."

            p "No creo que pueda aguantar mucho más."

            d "¡Estás de coña!,"

            d "¡¿verdad?!"

            if day06_morning_Didac_orgasms > 1:

                d "¡Pero si solo he tenido [day06_morning_Didac_orgasms] orgasmos!"

            elif day06_morning_Didac_orgasms == 1:

                d "¡Pero si solo he tenido un orgasmo!"

            else:

                aj "She had at least one orgasm... Isn't it?! 6897"

            ###

            if p_didac.orgasm > 4:

                p "¡Ayer ya te di bastantes!"

                d "¡Pero eso fue ayer!"

            elif p_didac.orgasm == 3:

                p "¡Ayer ya te di tres!"

                d "¡¿Y eso te parece mucho?!"

            elif p_didac.orgasm == 2:

                p "¡Ayer ya te di dos!"

                d "¡Joder!"

                d "¡Dos míseros orgasmos!"

                d "¡¿Se supone que tengo que darte las gracias por semejante hazaña?!"

            elif p_didac.orgasm == 1:

                p "¡Ayer ya te di uno!"

                d "..."

                d "¡¿Te estás cachondeando de mí?!"

                d "¡¿SE SUPONE QUE TENGO QUE DARTE LAS GRACIAS POR UN PUTO ORGASMO DE MIERDA?!"

                p "Es mejor que nada..."

                d "..."

                d "Tsssk..."

            else:

                if afternight04_didac_orgasms > 4:

                    p "Pero por lo menos antes de ayer ya te di bastantes."

                    d "¡¿Y AYER QUÉ?!"

                    d "¡Ayer no me diste ni uno!"

                elif afternight04_didac_orgasms > 1:

                    p "Pero por lo menos antes de ayer ya te di [afternight04_didac_orgasms] orgasmos."

                    d "¡¿Y eso te parecen muchos?!"

                    d "¡Por no hablar de que ayer...!"

                    d "¡NO ME DISTE NI UNO SOLO!"

                elif afternight04_didac_orgasms == 1:

                    p "Pero por lo menos antes de ayer ya te di un orgasmo."

                    d "..."

                    d "¡¿TE ESTÁS PUTO CACHONDEANDO DE MÍ?!"

                elif afternight04_didac_orgasms == 0:

                    p "..."

                    d "¡Ni ayer ni antes de ayer me diste..."

                    d "UN PUTO ORGASMO DE MIERDA!"

                    d "¡Espero que hoy aguantes un poco más!"

                else:

                    aj "It shouldn't be readable 98667"

                p "..."

        "...":
            call p_Help

            $ day06_didacAlone_sex_WarnHer = "False"

            pass



    p "Ughh..."

    if day06_didacAlone_sex_WarnHer == "True":

        d "Tsskk..."

        d "Al menos asegúrate de correrte dentro,"

        d "o la morenita nos matará a los dos."

    else:

        d "¡¿Qué...?!"

        d "¿Qué mierdas estás haciendo?"

    n "Sientes el espeso líquido deslizándose por tu entrepierna acercándose a tu rojizo y palpitante miembro."

    if day06_didacAlone_sex_WarnHer == "True":

        d "Hmmmmmfhm..."

        p "Uuuughhh..."

        d "¡No pares!"

    else:

        d "¡No"

        extend " no"

        extend " no...!"

        d "¡¡NO!!"

        d "¡Ni se te ocurra correrte aún!"

        d "¡Y MENOS SIN HABERME AVISADO!"

    $ day06_morning_MC_orgasms += 1

    n "Hasta que finalmente explosionas con viveza derramando tu esperma en su angosto y cálido interior."

    if day06_didacAlone_sex_WarnHer == "True":

        d "¡Dioos!"

    else:

        d "Tssk..."

        d "¡La madre que te parió!"

    if day06_didacAlone_sex_WarnHer == "True":

        $ day06_morning_Didac_orgasms += 1

        n "Otro enorme chorro de líquido vaginal vuelve a empaparte de ombligo para abajo."

        n "Dídac cae rendida en la cama mientras sus piernas siguen temblando descontroladamente"

        n "y su rostro muestra una expresión de placer absoluto."

        d "Jodeer..."

        d "Por qué estoy tan enamorada de tu pollón?"

        d "Puto [protname]..."

    else:

        pass
        # She doesn't had an orgasm, and is really pissed at you.

    p "¡Ugh...!"

    n "Ese punzante dolor, lo sientes ahora con más rudeza,"

    n "al mismo tiempo que percibes tus piernas tambaleando sin control."

    if day06_didacAlone_sex_WarnHer == "True":

        n "Observas a Dídac recobrando la compostura,"

        n "adoptando de nuevo la postura de perrita en celo."

    else:

        d "¡¿Y yo qué?!"

        d "¡Podrías haberme avisado!"

        n "Vuelve adoptar la postura de perrita en celo."

        d "¡Ni se te ocurra descansar ahora!"

        d "¡¿Me has oído?!"

    jump day06_didacAlone_sex_Stop
        # d "No pares..."
        # d "¡FÓLLAME!"
        # p "..."
        # d "¿Por qué coño no sigues?"
        # p "Parece que ya no tengo por que obedecer tus órdenes."