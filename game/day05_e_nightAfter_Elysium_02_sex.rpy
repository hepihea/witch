
default night05_elysium_cunnilingus_askStop = -1

default night05_elysium_NeusNaked = False
default night05_elysium_MCNaked = False

default night05_elysium_blowjobBeginning_Cond = ""

default night05_elysium_sexMast_Cond = False

default night05_elysium_1rstRoundYou_action_Cond = ""

default night05_elysium_unpleasant_Cond = ""

default night05_elysium_2ndRoundYou_pos_Cond = ""
default night05_elysium_2ndRoundYou_mood = ""

default night05_elysium_3rdRound_bigBodyOpinion = ""

default night05_elysium_1rstRound_MCDom_stopTimes = 0

default night05_elysium_1rstRound_MCDom_pose = ""

default night05_elysium_MCCumshots = 0

default night05_elysium_SmackAss = 0

default night05_elysium_3rdRoundYou_wood = ""
default night05_elysium_NeusBody = "small"

default night05_elysium_1rstRound_cunnilingusDone = False

##########################################################################################
##########################################################################################
##########################################################################################


##########################################################################################

##########################################################################################

##########################################################################################
##########################################################################################
##########################################################################################


label night05_elysium_acceptNeus:

    $pl.ch_pts("np",2)

    if ntlong > 0:

        $ ntlong = 0

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with fade

        pause 0.2


    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "De acuerdo Neus,"

    extend " como quieras."

    show neus_exp_mouth happybiting_Silentx03
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    # gensex_ILoveYouNeus # Do you tell her that you love her?

    #    MOR CHOICES, NOT_FINISHED.

    menu:

        pt "¿Y ahora qué le digo?"

        "Si no hay otro modo, supongo que tendremos que hacerlo." if not gensex_ILoveYouNeus:
            $pl.ch_pts("np",-4)
            call p_Help

            $ gensex_INotLoveYouNeus = True

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows normal
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx04
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Tampoco hace falta que lo expreses de esa manera."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "Pero es la verdad,"

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "¿no?"

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows angryx04
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx10
            show neus_exp_eyebrows angryx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            n "Percibes una notable humedad en sus ojos."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows angryx04
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Sí..."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx06
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

        "Aunque no me creas, realmente te amo." if not gensex_INotLoveYouNeus:
            call p_Help

            $ gensex_ILoveYouNeus = True

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows sadx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if night05_elysium_whyAmISoSpecial_Cond:

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows sadx01
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Incluso sabiendo que soy tu hermana?"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Eso no cambia lo que siento por ti."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx03
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Yo..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿De verdad?"

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¿Qué tengo que hacer para que me creas?"

            show neus_exp_mouth happybiting_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            show neus_exp_mouth happy_Talkingx04
            show neus_exp_eyebrows sadx03
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Bésame."

            show neus_exp_mouth happybiting_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            scene day05
            with fade

            n "Te acercas a ella y le das un cálido y dulce beso."

        "Aunque no te lo creas, también he estado esperando este momento toda la noche." if not gensex_INotLoveYouNeus:
            call p_Help

            $ gensex_INotLoveYouNeus = False
            $ gensex_YoureAMonster = False

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmm..."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            show neus_exp_mouth happy_Talkingx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Yo hace demasiadas noches que anhelaba este momento contigo..."

            show neus_exp_mouth happybiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmmm..."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows suspiciousx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

    jump night05_elysium_NeusPushesToBed

label night05_elysium_NeusPushesToBed:

    pause 0.2

    scene black
    with vpunch
    p "¡Ugh!"

    n "Con un rápido gesto te lanza sobre la cama."

    scene day05
    with fade

    p "¡Neus!"

    ne "Por favor,"

    extend " simplemente,"

    ne "relájate."

    ne "Déjame a mí."

    p "¿Y si quiero tomar yo el control?"

    ne "..."

    ne "Aquí,"

    extend " ¿quien tiene más experiencia?"
    
    if night05_elysium_AllWasALie_Cond:

        p "¿No decías que la madurez no es una cuestión de edad?"

        ne "Pero la experiencia sí lo suele ser."

        p "Hmm..."

    else:

        menu:

            pt "¿Más experiencia?"

            "¿Y qué te hace pensar que tienes más que yo?":
                call p_Help

                ne "..."

                ne "Créeme,"

                ne "tengo bastante más que tú."

            "...":
                call p_Help
                pass

    ne "Además,"

    extend " primero tengo que animar esto un poquito..."

    p "¿Y tú no necesitas preliminares?"

    ne "¿Euh...?"

    ne "..."

    ne "Preferiría que no..."

    p "¿Y eso por qué?"

    ne "..."

    ne "Quiero disfrutar de esta experiencia tanto como tú,"

    ne "pero hay algo que debes saber."

    jump night05_elysium_NeusInfoOrgasm

label night05_elysium_NeusInfoOrgasm:

    ne "No puedo tener ningún orgasmo."

    p "¿Cómo?"

    p "¡¿Por qué?!"

    ne "Si llegara al clímax,"

    ne "no solo Padre sabría perfectamente dónde estamos"

    ne "sino que además sería capaz de poseer mi cuerpo,"

    ne "y entonces todo habría terminado."

    p "..."

    ne "Aunque nos escondiéramos en una cueva en el otro rincón del mundo"

    ne "sería capaz de encontrarme en ese estado."

    p "¿Nunca podrás tener un orgasmo?"

    ne "..."

    ne "En principio no."

    ne "Tengo la esperanza de que en un futuro no muy lejano"

    ne "encuentre algún modo de burlar su radar,"

    ne "pero por ahora sería una sentencia de muerte."

    p "..."

    ne "No pasa nada,"

    extend " de verdad."

    ne "No necesito un orgasmo para volverme loca con tu compañía,"

    ne "y por supuesto,"

    extend " con tu pollón."

    if not gensex_INotLoveYouNeus:

        p "Pero me gustaría que también llegaras al {a=https://es.wikipedia.org/wiki/Nirvana_(espiritualidad)}nirvana{/a}..."

        ne "Te aseguro que a mi modo ya lo consigo."

    ne "No he tenido demasiados momentos de pura felicidad a lo largo de mi vida,"

    ne "pero ahora mismo lo estoy teniendo."

    if gensex_INotLoveYouNeus:

        ne "A pesar de que tú no sientas lo mismo por mí..."

    if not night05_elysium_AllWasALie_Cond:

        pt "Lo dice como si fuera una anciana..."

    menu:

        pt "Pura felicidad..."

        "Podría lamerte la entrepierna, aunque fuera un poquito." if not gensex_INotLoveYouNeus:
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_elysium_1rstRoundYou_action_Cond = "Cunnilingus"

            jump night05_elysium_ICouldLickYou

        "<Dejar que ella decida>":
            call p_Help

            $ night05_elysium_1rstRoundYou_action_Cond = "sheControl"

            p "Como prefieras."

            jump night05_elysium_sheDecides

        "Preferiría ser yo quien lleve el control.":

            ne "No creo que sea buena idea."

            p "¿Por qué no?"

            $ night05_elysium_1rstRoundYou_action_Cond = "youControl"

            jump night05_elysium_ICouldLickYou
                # ne "Además del peligro que supone que pueda llegar al orgasmo,"
                # ne "mi cuerpo se comportar d eun modo extraño cuando pierdo el control"

label night05_elysium_ICouldLickYou:

    if night05_elysium_1rstRoundYou_action_Cond == "Cunnilingus":

        ne "..."

        ne "¿Con tu lengua?"

        p "¿Con qué entonces?"

        ne "Hmmm..."

        ne "Preferiría que no."

    ne "Además del peligro que supone que pueda llegar al orgasmo,"

    ne "mi cuerpo se comporta de un modo extraño cuando pierdo el control..."

    ne "Y temo que lo que encuentres no vaya a ser de tu agrado."

    menu:

        pt "¿Lo que encuentre?"

        "No me importa si lo tienes peludo.":
            call p_Help

            if night03_NeusFall_NotPanties:

                ne "Primero,"

                ne "creo que ya me lo viste cuando me caí de bruces delante de la puerta de la Pedrera."

                pt "Pensaba que no se acordaría con lo bebida que estaba..."

            else:

                ne "Primero,"

                extend " no lo tengo peludo."

            ne "Y segundo,"

            extend " no me refiero a eso."

        "...":
            call p_Help

            pass


    p "¿Tienes monstruos ahí abajo?"

    ne "No..."

    ne "No exactamente..."

    p "¿A qué te refieres con \"exactamente\"?"

    ne "Mis labios vaginales cobran vida propia cuando voy caliente..."

    p "..."

    p "¡¿Me vas a devorar a través de tu vagina?!"

    ne "¡¿Qué?!"

    ne "¡¿De qué demonios estás hablando?!"

    p "¿Nunca has oído hablar del \"Vaginal {a=https://es.wikipedia.org/wiki/Vorarefilia}Vore{/a}\"?"

    ne "En serio..."

    ne "¡¿Qué tipo de mangas lees?!"

    p "Se llama {a=https://es.wikipedia.org/wiki/Hentai}hentai{/a}..."

    ne "Sé cómo se llama."

    ne "¡Te recuerdo que dibujo {a=https://es.wikipedia.org/wiki/Yaoi}yaoi{/a}!"

    p "..."

    ne "Aishh..."

    ne "Tonto."

    ne "No te voy a devorar."

    ne "Bueno,"

    ne "no de manera literal,"

    extend " al menos."

    p "..."

    ne "No te preocupes,"

    ne "en realidad es muchos más placentero de lo que puedas imaginarte,"

    ne "verás cómo lo disfrutarás cuando la tengas dentro."

    ne "Pero preferiría que no tuvieras que verlo,"

    ne "no estoy segura que te vaya a gustar a la vista."

    menu:

        pt "A la vista..."

        "<Tomar el control y usar tu lengua en su entrepierna>":
            call p_Help
            $pl.ch_pts("np",1)

            $ night05_elysium_1rstRoundYou_action_Cond = "Cunnilingus"

            jump night05_elysium_cunnilingus01

        "<Tomar el control>" if night05_elysium_1rstRoundYou_action_Cond == "youControl":
            call p_Help

            p "Prefiero ser yo quien tome la iniciativa."

            jump night05_elysium_1rstRound_youControlBeginning

        "<Aceptar las condiciones de Neus>":
            call p_Help

            $ night05_elysium_1rstRoundYou_action_Cond = "sheControl"

            p "Como prefieras."

            jump night05_elysium_sheDecides
 

label night05_elysium_1rstRound_youControlBeginning:

    # $ night05_elysium_1rstRoundYou_action_Cond = "youControl"

    ne "Hmm..."

    ne "Solo si me prometes que pararás cuando te diga que pares."

    p "..."

    menu:

        pt "\"Parar\" cuando ella me lo diga."

        "Te lo prometo.":
            call p_Help

            jump night05_elysium_1rstRound_youControlPromise

        "No te puedo prometer eso.":
            call p_Help

            ne "Si no me lo puedes prometer,"

            ne "entonces tengo que ser yo quien tome el control."

            menu:

                pt "Si no se lo puedo prometer..."

                "Si no hay más remedio..." if gensex_INotLoveYouNeus:
                    call p_Help

                    ne "..."

                    ne "Tampoco hace falta que te lo tomes así..."

                "Ya te he dicho que no pienso prometértelo." if gensex_INotLoveYouNeus:
                    call p_Help

                    $pl.ch_pts("np",-2)

                    ne "..." # Angry

                    ne "Mira que eres obtuso cuando quieres..."

                    jump night05_elysium_sheDecides

            ####

                "Vale, te lo prometo." if not gensex_INotLoveYouNeus:
                    call p_Help

                    jump night05_elysium_1rstRound_youControlPromise

                "Lo siento, pero no te lo puedo prometer." if not gensex_INotLoveYouNeus:
                    call p_Help
                    $pl.ch_pts("np",-1)

                    jump night05_elysium_sheDecides

                

label night05_elysium_1rstRound_youControlPromise:

    if gensex_INotLoveYouNeus:

        n "Una ligera sonrisa se dibuja en sus labios."

    ne "De-"

    extend " deberías desvestirte."

    p "¿y tú?"

    # She takes off her clothes.

    $ night05_elysium_NeusNaked = True

    call afternight05_Pedrera_NeusNaked

    scene day05
    with fade

    ne "..."

    ne "Sigues vestido."

    pt "Tiene razón."

    n "Cuando te dispones a desabrocharte el cinturón"

    n "sientes sus manos acariciándote los abdominales por encima de la ropa."

    p "..."

    ne "¿Me permites ayudarte a desabrocharte los botones de la camisa?"

    p "¿Solo eso?"

    ne "Bueno,"

    ne "no te haré nada que luego no tenga ganas de seguir haciendo."

    menu:

        pt "¿Quiere desvestirme o...?"

        "Prefiero hacerlo solo.":
            call p_Help
            $pl.ch_pts("np",-1)

            ne "..."

            ne "Como prefieras..."

            jump night05_elysium_1rstRound_MCDressOffYouDo

        "Si haces que valga la pena...":
            call p_Help

            ne "..."

            ne "Exigente el chico..."

            jump night05_elysium_1rstRound_MCDressOffSheDoes

        "Por supuesto.":
            call p_Help

            ne "Así me gusta..."

            jump night05_elysium_1rstRound_MCDressOffSheDoes

label night05_elysium_1rstRound_MCDressOffYouDo:

    n "Uno a uno vas desabrochándote los botones de la camisa"

    n "mientras te mira con un rostro lascivo y mordiéndose el labio."

    n "Una vez te deshaces de la camisa te bajas la cremallera del pantalón."

    ono "ZIIIIP"

    n "Para luego quitártelos dejando a la vista tu visible -principio de- erección a través del bóxer."

    ne "Realmente la tienes enorme."

    if night04_pedrera_blowjob_DONE or night05_Park_Bathroom_Sweet_Cond:

        pt "Como si no lo supiera..."

    n "Al quitarte la última pieza de ropa que cubría tu parte púdica:"

    ne "¿Y bien?"

    ne "¿Qué quieres hacerme ahora?"

    jump night05_elysium_1rstRound_MCDom_Start
        # n "La agarras por las caderas"
        # with vpunch
        # ne "¡Ugh!"
        # n "y la lanzas encima de la cama."
        # ne "Vaya,"

label night05_elysium_1rstRound_MCDressOffSheDoes:

    n "Con un rostro juguetón y lascivo empieza desabrochándote el botón que tienes más cerca del paquete."

    n "Acerca su rostro a tus pectorales y sientes a través de la tela su cálida respiración."

    n "A medida que va desprendiéndose de ellos uno a uno"

    n "percibes la fría piel de sus dedos acariciándote la piel."

    n "Cuando al fin pone al descubierto tu pecho, acerca sus labios besándote juguetonamente tu desnuda piel."

    menu:

        pt "Me la imagino trabajando en una tienda de ropa..."

        "Pensaba que solo querías desabrocharme los botones.":
            call p_Help

            ne "¿Yo he dicho eso?"

        "...":
            call p_Help
            pass

    n "Aparta la camisa hasta que tú mismo terminas desprendiéndote de la misma."

    n "Sigue besando tu desnudo busto mientras acaricia con sus -ya no tan frías- manos tus duros pezones."

    n "Diriges otra vez tus manos al botón del pantalón."

    n "Te detiene suavemente con sus manos."

    ne "No..."

    ne "Permíteme a mí."

    n "Apartas tus manos mientras te sonríe de forma pícara."

    n "Se pone de rodillas y sin dificultad te desabrocha el botón mientras desliza la cremallera."

    ono "ZIIIIIP"

    ne "Realmente se ve enorme."

    if night04_pedrera_blowjob_DONE:

        p "Lo dices como si ayer no la hubieras tenido en tu garganta."

    elif night05_Park_Bathroom_Sweet_Cond:

        p "Lo dices como si no me la hubieras tocado en el cuarto de baño."

    if night04_pedrera_blowjob_DONE or night05_Park_Bathroom_Sweet_Cond:

        ne "Bueno,"

    if night04_pedrera_blowjob_DONE:

        ne "pero ahora la veo con más luz."

    elif night05_Park_Bathroom_Sweet_Cond:

        ne "pero ahora la tengo de frente."

    n "Acaricia tu miembro a través de la delgada tela del bóxer."

    ne "Me alegra ver que ya estás algo excitado."

    pt "Creo que no hacía falta bajarme los pantalones para comprobar eso."

    n "Ubica la palma de sus manos en cada pierna"

    n "y las asciende pasándolas por debajo de tu ropa interior."

    p "La idea es que me lo quites, no que me toquetees por debajo."

    ne "¿Dónde está tu espíritu juguetón?"

    menu:

        pt "Espíritu juguetón..."

        "¿No decías que no teníamos toda la noche?":
            call p_Help

            ne "Grhhmm..."

            n "Aparta sus manos del interior de tu bóxer."

            ne "Tienes razón."

            n "Con un veloz movimiento termina sacándote esa ropa interior."

            n "Y poniéndose de pie."

            ne "¿Y bien?"

            jump night05_elysium_1rstRound_MCDom_Before
                # ne "Quieres follarme en plan misionero o a cuatro patas?"

        "Supongo que tampoco hay tanta prisa.":
            call p_Help

            ne "..."

            ne "En realidad sí la hay,"

            ne "pero,"

            ne "no sabes cuánto hace que deseo disfrutar de..."

            ne "esto."

            pt "No estoy muy seguro de a qué se refiere con \"esto\"."

        "...":
            call p_Help

            pass

    n "Mientras te acaricia los testículos a flor de piel"

    n "posa sus labios sobre tu miembro a través de la tela"

    n "para besártela con dulzura."

    n "En pequeñas contracciones, tu polla sigue aumentando de tamaño"

    n "hasta que la punta emerge del bóxer por encima de tu ombligo."

    n "Alza el rostro para darte un beso en esa rosada y sensible carne."

    p "Creía que habíamos quedado que yo tomaría el control."

    ne "¿Es que no te apetece que te la chupe un poco?"

    menu:

        pt "¿Qué entenderá por \"un poco\"?"

        "¿Quién manda aquí?":
            call p_Help

            ne "..."

        "Quizás no es tan mala idea.":
            call p_Help

            ne "Así me gusta."

            $ night05_elysium_blowjobBeginning_Cond = "knees"

            jump night05_elysium_blowjobBeginning
                # $ night05_elysium_blowjobBeginning_Cond = True
                # n "Acerca sus labios a la base de tu miembro -y mientras sientes el calor de su aliento-"
                # n "besa sugerentemente la sensible piel de tus testículos."
                # n "Desliza sutilmente y sin prisas sus suaves dedos por tus piernas a la altura de la pantorrilla,"

        "Preferiría que no.":
            call p_Help
            pass


    ne "Como quieras..."

label night05_elysium_1rstRound_MCDom_Before:

    if night05_elysium_1rstRound_MCDom_pose in ["doggy", "missionary"]:

        ne "El problema es que sigo sin estar lo suficientemente dilatada para..."

        ne "Bueno,"

        extend " para tu tamaño."

        jump night05_elysium_1rsRoundCumShot # Not sure if I can really use this one.
            # n "A pesar de haberse detenido,"
            # n "la cálida piel de su estómago y su húmeda entrepierna"
            # n "siguen pegadas a tu erecto miembro."
            # ne "La verdad es que me pasaría la noche entera devorándola."

        ##jump night05_elysium_2ndRoundBeginnig
            # menu:
            #     pt "¿Y ahora?"
            #     "Me gustaría seguir teniendo el control" if night05_elysium_1rstRoundYou_action_Cond == "youControl":
            #         call p_Help
            #         jump night05_elysium_2ndRoundYou
            #     "Me gustaría poder tomar un poco el control ahora." if night05_elysium_1rstRoundYou_action_Cond != "youControl":


    else:

        ne "Quieres follarme en plan misionero o a cuatro patas?"

        menu night05_elysium_1rstRound_MCDom_choicePose:

            pt "En qué postura..."

            "¿En qué postura preferirías tú?" if not gensex_INotLoveYouNeus and night05_elysium_1rstRound_MCDom_pose == "":
                call p_Help
                $pl.ch_pts("np",1)

                $ night05_elysium_1rstRound_MCDom_pose = "YouAsk"

                ne "..."

                ne "Euhh..."

                ne "Yo..."

                ne "La verdad es que me gustaría verte de cara mientras me haces el amor."

                ne "Pero confieso que me pone muy perra que me folles a cuatro patas."

                p "..."

                jump night05_elysium_1rstRound_MCDom_choicePose

            "Creía que lo que querías es que te hiciera el amor." if gensex_ILoveYouNeus and night05_elysium_1rstRound_MCDom_pose == "":
                call p_Help
                $pl.ch_pts("np",1)

                $ night05_elysium_1rstRound_MCDom_pose = "love"

                ne "..."

                ne "Sí..."

                ne "Eso es verdad."

                ne "Entonces..."

                ne "¿Prefieres ponerme a cuatro patas o en plan misionero?"

            "Prefiero verte la cara mientras te hago el amor." if night05_elysium_1rstRound_MCDom_pose == "love":
                call p_Help

                $ night05_elysium_1rstRound_MCDom_pose = "missionary"

                ne "..."

                ne "Que cursi eres cuando quieres."

                p "¿Cursi?"

                jump night05_elysium_1rstRound_MCDom_choicePose

            "Prefiero tenerte de cara.":
                call p_Help

                $ night05_elysium_1rstRound_MCDom_pose = "missionary"

            "Prefiero tenerte a cuatro patas.":
                call p_Help

                $ night05_elysium_1rstRound_MCDom_pose = "doggy"


    jump night05_elysium_1rstRound_MCDom_Start

label night05_elysium_1rstRound_MCDom_Start:

    n "La agarras por las caderas"

    with vpunch
    ne "¡Ugh!"

    n "y la lanzas encima de la alcoba."

    ne "Vaya,"

    ne "si al final resultarás ser un tigre en la cama y todo."

    p "Ya verás lo que puedo llegar a ser."

    n "Te acercas a ella a cuatro patas sobre la sábana colocándote encima de ella"

    n "teniendo tu miembro en erección colgando entre tus piernas."

    if night05_elysium_1rstRound_MCDom_pose == "missionary":

        n "Mirándote con cara de circunstancias y con una voz temblorosa."

    else:

        n "Ella misma te da la espalda y levanta sus caderas reposando sus rodillas sobre el suave colchón."

        n "Con una voz temblorosa y mirándote con cara de circunstancias."

    ne "La"

    extend "-la tienes bien gorda."

    menu:

        pt "Miss obviedad."

        "Como si no lo supieras." if night04_pedrera_blowjob_DONE or night05_Park_Bathroom_Sweet_Cond:
            call p_Help

            ne "Hmmm..."

            if night04_pedrera_blowjob_DONE:

                ne "Es solo que con mi garganta tengo algo más de práctica,"

                ne "pero mi entrepierna..."

                p "¿Es que no quieres que te la meta?"

                ne "Solo te pido que vayas con cuidado."

                menu:

                    pt "Con cuidado..."

                    "Lo dices como si me importara tu opinión." if gensex_INotLoveYouNeus:
                        call p_Help
                        $pl.ch_pts("np",-2)

                        ne "..."

                        ne "¿Por qué eres así?..."

                        pt "¿De verdad se merece que la trate así?"

                    "Te prometo que intentaré ir con cuidado."if not gensex_YoureAMonster:
                        $pl.ch_pts("np",1)

                        ne "..."

                        ne "Una sonrisa se dibuja en sus labios."

                    "...":
                        call p_Help

                        pass

        "¿Crees que te cabrá?":
            call p_Help

            ne "Supongo que lo sabremos cuando lo intentes."

            p "..."

        "...":
            call p_Help

            pass


    if night05_elysium_1rstRound_MCDom_pose == "missionary" and gensex_ILoveYouNeus:

        n "Te acaricia las mejillas con sus manos."

    elif night05_elysium_1rstRound_MCDom_pose == "doggy" and gensex_ILoveYouNeus:

        n "Con las mejillas sonrojadas:"

    ne "[protname];"

    if night05_elysium_1rstRound_MCDom_pose == "missionary" and gensex_ILoveYouNeus:

        n "Alargando su cuello y forzándote a bajar la cabeza te da un dulce beso en los labios."

    else:

        p "¿Hmm...?"

    if night05_elysium_1rstRound_MCDom_pose == "doggy":

        n "Posando su busto sobre la almohada y abriéndose más de piernas:"

    ne "Soy toda tuya."

    if night05_elysium_1rstRound_MCDom_pose == "missionary":

        n "Usando sus manos se abre aún más de piernas."

    else:

        n "Agita ligeramente sus nalgas para intentar acariciar tu miembro en suspensión."

    n "Agarras tu polla con tu mano derecha para acercar la rosada punta a su entrepierna."

    if night05_elysium_1rstRound_MCDom_pose == "missionary":

        n "Debido a su altura, su cabeza está a la altura de tus pectorales,"

        n "pero aún así te parece ver en su rostro una expresión entre el deseo y la preocupación."

    else:

        n "Debido a la postura, no tienes una visión clara de su rostro,"

        n "pero aún así te parece ver en ella una expresión de deseo y preocupación."

    n "A pesar de que tu polla está bien dura,"

    n "te resulta complicado introducir tu grueso glande en su tierna y estrecha vagina."

    ne "No te preocupes."

    n "Neus te dirige una dulce mirada con una forzada sonrisa."

    ne "Es solo la punta,"

    ne "tiene que entrar sí o sí."

    if not gensex_INotLoveYouNeus:

        p "Quizás no estás lo suficientemente húmeda."

        ne "Te aseguro que estoy mojada desde el primer momento en que te vi llegar a lo lejos"

        ne "antes de empezar nuestra cita."

    

    call night05_elysium_1rstRound_MCDom_stopQuestion

    n "Con cierto esfuerzo logras introducir parte del glande en su estrecha cavidad."

    ne "¡Ughhh...!"

    menu:

        pt "No parece estar disfrutándolo."

        "Es obvio que te estoy haciendo daño.":
            call p_Help

            $pl.ch_pts("np",1)

            ne "Quizás un poco..."

            ne "Pe-"

            extend "pero puedo aguantar..."

            p "..."

        "<Seguir sin decir nada>":
            call p_Help

            pass

    n "Al presionar con más energía logras enterrar el glande entero."

    with hpunch
    ne "¡Aghh...!"

    n "El tono de su gemido no parece de placer."

    n "Su coño es cálido pero intensamente estrecho y hostil al enorme tamaño de tu polla."

    n "Sigue agarrándose con fuerza a la sábana con el rostro agonizante y al borde de las lágrimas."

    n "Aumentas la presión, perforando su interior"

    n "como si la estuvieras intentado meter entre los dedos de un enorme puño enérgicamente cerrado."

    ne "¡Uughh...!"

    n "Intenta mantener sus piernas abiertas a pesar de sus gruñidos"

    n "y de tener todo su cuerpo temblando y en constante movimiento."

    n "Cada vez te resulta más difícil seguir enterrando tu miembro en su sexo"

    n "como si hubiera un muro que te impidiera avanzar."

    ne "Uuugh..."

    ne "Quizás no ha sido tan buena idea..."

    call night05_elysium_1rstRound_MCDom_stopQuestion

    n "Sigues presionando con ímpetu e intentas perforar esa pared carnosa."

    with hpunch
    ne "¡Aaaaghh!"

    if night05_elysium_1rstRound_MCDom_pose == "missionary":

        n "Aparta sus manos de sus piernas y las posa sobre tu cuerpo."

    else:

        n "Se reincorpora levantando su busto de la cama mirándote con cara de preocupación."

    ne "Por favor..."

    ne "Para unos segundos."

    call night05_elysium_1rstRound_MCDom_stopQuestion

    $pl.ch_pts("np",-3)

    n "Sigues imponiendo fuerza contra ese muro de carne."

    if night05_elysium_1rstRound_MCDom_pose == "missionary":

        n "Sus brillantes ojos te dejan paralizado."

    else:

        n "Contornea su cuerpo para mirarte con sus brillantes ojos."

    ne "¡[protname]!"

    n "Eres incapaz de mover un músculo."

    ne "¡Te he dicho que pares!"

    p "Me dijiste que parase si te acerbas al orgasmo."

    ne "..."

    p "¿Es que acaso estabas punto de tener uno?"

    ne "No."

    ne "Pero también te dije que te detuvieras cuando te lo pidiera."

    p "..."

    ne "Lo siento."

    ne "Supongo que con este cuerpo tan diminuto y tu enorme polla"

    ne "necesito algo más de tiempo para excitarme."

    p "No habías dicho que ya estabas lo suficientemente cachonda al verme."

    ne "Dije que estaba húmeda;"

    ne "y eso es verdad."

    ne "Pero no es lo mismo estar cachonda que estar dilatada."

    p "..."

    if gensex_ILoveYouNeus:

        #$ gensex_ILoveYouNeus = False

        $pl.ch_pts("np",-1)

        ne "Realmente pensé que me amabas."

        menu:

            "Y te amo.":

                ne "¿Y por qué sigues haciéndome daño cuando te pido que pares?"

                p "..."

            "Te dije lo que querías escuchar.":
                $pl.ch_pts("np",-5)

                $ gensex_ILoveYouNeus = False
                $ gensex_INotLoveYouNeus = True

                ne "..."

                ne "Yo..."

                n "Una gruesa lágrima se escurre por su mejilla."

                ne "Supongo que he sido una idiota al creerte."

                p "Supongo."

                ne "..."

            "...":

                $ gensex_ILoveYouNeus = False

                $pl.ch_pts("np",-1)

    ne "Estírate en la cama."

    p "Preferiría tener yo el control."

    n "Sus ojos vuelven a brillar con intensidad"

    ne "No era una sugerencia."

    n "y -en contra de voluntad- tu cuerpo termina obedeciendo sus palabras."

    ne "Es obvio que no sabes acatar una simple instrucción."

    ne "Así que no me das otra opción."

    jump night05_elysium_sheRidesYou
        # # EMPIEZA SENTADA SOBRE TUS HUEVOS
        # n "Se reincorpora para sentarse sobre tus muslos posando tu miembro encima de su estómago"
        # n "y asomándose entre sus modestos pechos.."

label night05_elysium_1rstRound_MCDom_stopQuestion:

    $ night05_elysium_1rstRound_MCDom_stopTimes += 1

    menu:

        pt "Puede que esté algo mojada, pero no parece que esté lo suficientemente dilatada."

        "<Seguir>":
            call p_Help

            pass

        "¿Y entonces qué propones?" if night05_elysium_1rstRound_MCDom_stopTimes == 4:

            ne "No-"

            extend "no lo sé..."

            ne "Podría intentar chupártela un poco..."

            if night05_elysium_WhatNow_After_BlowjobDisgusting:
                
                ne "Aunque antes ya me has dejado claro lo mucho que te disgusta mi lengua..."

                p "..."

            p "¿Y eso hará que te dilates más?"

            ne "Es posible."

            jump night05_elysium_1rstRound_MCDom_stopQuestion

        "<Dejar que te la chupe>" if night05_elysium_1rstRound_MCDom_stopTimes == 5:
            call p_Help
            $pl.ch_pts("np",1)

            p "De acuerdo,"

            p "si crees que puede funcionar..."

            if night05_elysium_WhatNow_After_BlowjobDisgusting:

                $ night05_elysium_WhatNow_After_BlowjobDisgusting02 = True

                ne "Me alegra que hayas cambiado de idea."

                menu:

                    pt "Cambiado de idea..."

                    "Tampoco es que me des muchas opciones.":
                        call p_Help
                        $pl.ch_pts("np",-2)

                        ne "..."

                        ne "También podrías haber usado tú la lengua."

                        p "¿No has dicho que no puedes llegar al orgasmo?"

                        ne "¡Se pueden hacer preliminares sin tener que llegar a eso!"

                        p "..."

                        ne "No importa."

                    "...":
                        call p_Help

                        ne "..."

                        p "¿Ocurre algo?"

                        ne "No."

                ne "Es solo que me gustaría hacértelo"

                ne "sin pensar que te está disgustando tanto..."

            else:

                ne "Espero que sí."

            n "Se reincorpora de rodillas sobre la cama."

            ne "Por favor,"

            ne "ponte cómodo."

            n "Obedeces sus palabras y te estiras encima de la sábana."

            jump night05_elysium_blowjobBeginning
                # n "Acerca sus labios a la base de tu miembro -y mientras sientes el calor de su aliento-"
                # n "besa sugerentemente la sensible piel de tus testículos."
                # n "Desliza sutilmente y sin prisas sus suaves dedos por tus piernas a la altura de la pantorrilla,"

        "<Obedecer y esperarte unos segundos>" if night05_elysium_1rstRound_MCDom_stopTimes == 3:
            $pl.ch_pts("np",1)

            p "..."

            ne "Hmm..."

            n "Mantienes la pequeña porción de tu erecta y palpitante polla en su asfixiante sexo."

            n "A pesar de sus palabras, su rostro sigue siendo de dolor y de preocupación."

            p "¿Estás segura que tendrás suficiente con unos segundos?"

            ne "No..."

            ne "No lo sé."

            ne "Quizás no ha sido una buena idea empezar tan en frío..."

            ne "Lo siento."

            jump night05_elysium_1rstRound_MCDom_stopQuestion

        "<Detenerte y hacerle un cunnilingus>":
            call p_Help

            $pl.ch_pts("np",2)

            with hpunch
            ne "¡Ugh!"

            n "La tiras sobre la cama y posas tu cabeza entre sus piernas."

            jump night05_elysium_cunnilingus02
                # ne "¿Qué-"
                # ne "qué estás haciendo...?"
                # p "Ayer me lo hiciste tú."
                # p "Hoy es mi turno."
                # ne "[protname],"
                # ne "no tenemos toda la noche..."
                # 
    return


label night05_elysium_sheDecides:

    $pl.ch_pts("np",1)

    #p "Como prefieras."

    ne "Entonces desnúdate y ponte cómodo sobre la cama."

    p "¿Y tú no te desnudas?" 

    ne "..."

    ne "Euhh..."

    ne "Supongo que sí..."

    call night05_elysium_NeusClothes

    jump night05_elysium_blowjobBefore


label night05_elysium_NeusClothes:

    menu:

        pt "¿Es que quiere hacerlo vestida?"

        "Se supone que si vamos a follar...":
            call p_Help

            ne "..."

            ne "¡Eso ya lo sé!"

            p "¿Entonces?"

        "No quiero presionarte.":
            call p_Help
            $pl.ch_pts("np",1)

            ne "..."

            ne "Te lo agradezco."

        "También me gustaría poder verte desnuda.":
            call p_Help
            $pl.ch_pts("np",1)

            if gensex_INotLoveYouNeus:

                ne "Pensaba que habías dicho que no me amabas."

                p "Eso no significa que no quiera verte desnuda."

                ne "..."

                if gensex_NotLoveSister:

                    ne "¿Aunque sea tu hermana?"

                    p "..."

                ne "De todos modos,"

                ne "tampoco es que te pierdas gran cosa..."

            else:

                ne "No estoy muy segura de ello..."

            menu:

                pt "La inseguridad de esta mujer es más alta que el Everest."

                "Pero si ya casi te lo he visto todo.":
                    call p_Help

                    ne "..."

                    if night03_NeusFall_NotPanties or night03_MidnightProblem04_GoUp_Boolean:

                        if night03_NeusFall_NotPanties and night03_MidnightProblem04_GoUp_Boolean:

                            ne "Supongo que tienes razón..."

                        ne "Aunque siempre me has visto un poco a oscuras..."

                        pt "Un poco dice..."

                    else:

                        ne "Hmm..."

                        aj "¿Can you get to this point without seeing any of her naked body? Please, report if you did. 65964 xD"

                "No seas tonta.":
                    call p_Help

                    if gensex_INotLoveYouNeus:
                        $pl.ch_pts("np",-1)

                        ne "¡No soy ninguna tonta!"

                        p "Pues a ver si lo demuestras."

                        ne "..."

                    else:

                        ne "*Gnnnn*" # Te saca la lengua de forma infantil.

                "...":
                    call p_Help

                    ne "..."

    ne "Supongo que es necesario..."

    n "Ves que voltea la cabeza para mirar alrededor de la habitación como si buscara algo."

    p "¿Qué ocurre?"

    ne "¿Por que nunca hay lámparas cuando las necesitas?"

    menu:

        pt "¿Tiene algún problema con la luz?"

        "¿Es que no hay suficiente luz?":
            call p_Help

            ne "El problema es que hay demasiada..."

        "Preferiría no tener que hacerlo a oscuras como ayer." if night04_pedrera_blowjob_DONE:
            call p_Help

            ne "..."

            ne "¿Y no crees que tengo razones para preocuparme después de lo que viste ayer?"

            menu:

                pt "Aparte de sus brillantes ojos, tampoco es que \"viera\" demasiado..."

                "¿Por qué asumes que me disgustó tanto?":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    ne "..."

                    if gensex_INotLoveYouNeus:

                        ne "¿Lo estás diciendo en serio?"

                        p "Claro."

                        if gensex_NotLoveSister:

                            ne "¿Es que ya no te importa que sea tu hermana?"

                            p "¿Qué tiene que ver una cosa con la otra?"

                            ne "..."

                    p "¿Acaso no terminé corriéndome?"

                    ne "Sí,"

                    ne "Pero..."

                    menu:

                        pt "Siempre hay un pero."

                        "Pues entonces deja de ser tan estúpida.":
                            call p_Help

                            if gensex_INotLoveYouNeus:
                                $pl.ch_pts("np",-1)

                                ne "¡No soy estúpida!"

                            else:

                                ne "..."

                                ne "No soy estúpida."

                            menu:

                                pt "¿Qué se supone que le tengo que decir ahora?"

                                "En realidad, lo eres bastante.":
                                    call p_Help
                                    $pl.ch_pts("np",-1)

                                    ne "¡Vale!"

                                    ne "¡Ya me ha quedado claro que soy tonta!"

                                    ne "..."

                                    ne "Aunque lo único que consigues diciéndome esto"

                                    ne "es darme la razón..."

                                "Lo eres, porque sigues sin entender lo mucho que me gustas." if not gensex_INotLoveYouNeus:
                                    call p_Help
                                    $pl.ch_pts("np",2)

                                    $ gensex_ILoveYouNeus = True

                                    ne "..."

                                    ne "¿De-"

                                    extend "de verdad?..."

                                    p "¿Por qué te cuesta tanto creerme?"

                                    ne "..."

                                    n "Una tímida sonrisa se dibuja en su rostro."

                                "...":
                                    call p_Help

                                    ne "..."

                        "Pues entonces no tengas tantas dudas y déjame ver lo hermosa que eres.":
                            call p_Help
                            $pl.ch_pts("np",1)

                            ne "..."

                            if gensex_INotLoveYouNeus:

                                ne "Pe-"

                                extend "pensé que no te gustaba."

                                menu:

                                    "Me gustas, pero el hecho de que seas mi hermana..." if gensex_NotLoveSister:

                                        $ gensex_LikeYou = True

                                        ne "..."

                                        ne "Ya..."

                                        ne "Lo siento."

                                    "Me gustas físicamente.":

                                        ne "..."

                                        ne "Hmmm..."

                                        ne "Supongo que algo es algo."

                                    "...":

                                        ne "..."

                            else:

                                ne "Mira que eres tonto..."

                                p "Mira quien habla."

                                ne "*Gnnn* -Gañota sacándose la lengua-"

                                n "Una dulce sonrisa se dibuja en su rostro."

                        "¿Acaso no me crees cuando te digo que te amo?" if gensex_ILoveYouNeus: ## Is there the option done here yet?
                            call p_Help
                            $pl.ch_pts("np",1)

                            ne "..."

                            ne "Supongo que me cuesta de creer..."

                            p "Pues créetelo."

                            ne "..."

                            n "Una dulce sonrisa se dibuja en su rostro."

                        "...":
                            call p_Help

                            ne "..."

                "...":
                    call p_Help

                    ne "..."


        "Hay la luz perfecta para poder ver lo bella que eres." if not gensex_INotLoveYouNeus:
            call p_Help
            $pl.ch_pts("np",1)

            ne "..."

            ne "Que cursi eres cuando quieres."

            pt "Quizás un poco..."

            ne "Gracias [protname]."

    ###

    # She takes off her clothes.

    $ night05_elysium_NeusNaked = True

    call afternight05_Pedrera_NeusNaked
        # ne "..."
        # n "Vuelve a ponerse de puntillas para acercarse a tus labios y darte un dulce beso,"
        # n "mientras desabrocha el lazo frontal que sujeta su reducido corsé,"
        # n "exhibiendo así sus modestos pechos con sus pezones duros y rosados."

    ## 

    if not night05_elysium_MCNaked:

        #call afternight05_Elysium_Sex_previous

        $ night05_elysium_MCNaked = True

        if gensex_INotLoveYouNeus:
            $ nteye = "front05"
            show n_closefromup_eyebrows sadx04
            show n_closefromup_mouth sad_Talkingx02
            call n_closefromup_tears_tears
        else:
            $ nteye = "front05"
            show n_closefromup_eyebrows sadx01
            show n_closefromup_mouth happy_Talkingx03
            call n_closefromup_tears_tears
        with dissolve
        
        # $ nteye = "front08"
        # show neus_exp_mouth sad_Talkingx02
        # show neus_exp_eyebrows sadx04
        # call gensex_oral_n_frontHead_exp_tears_tears
        # with dissolve

        ne "Ahora es tu turno."

        if gensex_INotLoveYouNeus:
            $ nteye = "front08"
            show n_closefromup_eyebrows sadx05
            show n_closefromup_mouth sadbiting_Silentx04
            call n_closefromup_tears_tears
        else:
            $ nteye = "front06"
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth happy_Silentx04
            call n_closefromup_tears_tears
        with dissolve

        p "..."

        scene day05
        with fade

        n "Sin rechistar, obedeces su orden desprendiéndote de tu ropa."

    return


label night05_elysium_cunnilingus01:

    p "Al final te voy a tener que dar la razón."

    ne "¿Euh...?"

    p "Eres bastante estúpida."

    ne "¡Oye!"

    n "La agarras por los hombros,"

    n "la tiras sobre la cama y te pones encima de ella."

    jump night05_elysium_cunnilingus02

label night05_elysium_cunnilingus02:

    $ night05_elysium_1rstRound_cunnilingusDone = True

    ne "¿Qué-"

    ne "qué estás haciendo...?"

    p "Ayer me lo hiciste tú."

    p "Hoy es mi turno."

    ne "[protname],"

    ne "no tenemos toda la noche..."

    p "No seas tan aguafiestas."

    p "Aún falta mucho para que amanezca,"

    extend " déjame complacerte un poco."

    if gensex_NotLoveSister:

        ne "No hace falta que lo hagas si no quieres hacerlo."

        p "Es obvio que necesitas unos preliminares."

    ne "..."

    ne "Tengo miedo de que te disguste..."

    if not gensex_INotLoveYouNeus:

        p "Tonta."

        ne "..."

        ne "Eso lo dices ahora,"

        extend " pero..."

    ne "¡Hhhmmff...!"

    n "Acaricias su labia exterior con la lengua"

    n "a la par que le apartas ambas piernas."

    n "Con tu mano derecha separas sus labios superiores"

    n "y centras la atención de tu lengua en su pequeño pero terso clítoris"

    n "que asoma en la cima de su sensible parte."

    ne "Hmmm..."

    n "Liberas sus labios mayores para introducir dos dedos en su húmedo y cálido interior."

    ne "Ahhmm..."

    n "Desplazas tu lengua hasta tus dedos en movimiento"

    n "y vuelves a subir relamiendo toda su rosada carne."

    ne "Para..."

    $ night05_elysium_cunnilingus_askStop = 0

    call night05_elysium_cunnilingus_question

    n "Apartas tus dedos -dibujando un hilo espeso y caliente en el transcurso- e introduces tu lengua en su interior."

    ne "[protname]..."

    n "Con esos dedos empapados en su jugo, acaricias su cada vez más abultado y rosado clítoris."

    ne "No sigas..."

    call night05_elysium_cunnilingus_question

    n "Extendiendo aún más tu mandíbula,"

    n "logras ahondar en su interior mientras pellizcas con fuerza la ovalada cima."

    ne "AAAHhmmm..."

    n "Deslizas -como un pez que se fuga de su presa- tu lengua en su interior"

    n "al mismo tiempo que mueves con celeridad tus dedos en su sensible parte."

    ne "¡Para!"

    call night05_elysium_cunnilingus_question

    n "Acercas tu mano libre y le introduces tres dedos alrededor de tu juguetona y ágil lengua."

    ne "{size=50}¡[protname]!{/size}"

    $pl.ch_pts("np",-1)

    with vpunch
    n "Te da una patada tan fuerte que sales disparado contra el suelo."

    n "Cuando alzas la vista te la encuentras exhalando denso vapor con una expresión de lujuria y deseo"

    n "pero al mismo tiempo con un rostro nada amigable y sus ojos brillando con intensidad."

    ne "¡Si te digo que pares, para!"

    ne "Casi haces que tenga un orgasmo."

    p "Pero te estaba gustando."

    ne "¡Claro que me estaba gustando!"

    ne "¡E ahí el problema, idiota!"

    p "..."

    ne "*Profundo suspiro*"

    ne "Estírate sobre la cama."

    p "Puedo ir más despacio si quie..."

    n "Sin ser capaz de terminar la frase,"

    n "te mira de nuevo con sus brillantes ojos."

    n "Incapaz de hacer nada al respecto,"

    n "obedeces sus ordenes y terminas estirándote sobre la sábana."

    ne "No me obligues a tener que recurrir a esto [protname],"

    ne "te lo pido por favor..."

    p "..."

    if not night05_elysium_MCNaked:

        ne "Ahora desnúdate."

        n "Tu cuerpo se mueve por inercia propia."

        n "Pieza a pieza,"

        n "te desprendes de tu ropaje."

        $ night05_elysium_MCNaked = True

    if not night05_elysium_NeusNaked:

        call night05_elysium_NeusStrip

    jump night05_elysium_blowjobBefore


label night05_elysium_cunnilingus_question:

    menu:

        pt "¿Debería parar?"

        "<Detenerte>":
            call p_Help

            if night05_elysium_cunnilingus_askStop >= 3:

                ne "Aaaahhh-aaAHAHH-Aahhh..."

                ne "Te-"

                extend "te había dicho que parases..."

                ne "¡Casi tengo un orgasmo!"

                ne "¡¿Acaso no entiendes el peligro que eso supone?!"

            elif night05_elysium_cunnilingus_askStop == 2:

                ne "Aaah-ahh..."

                p "¿Estás bien?"

                ne "Si te digo que pares, para."

                p "Es lo que he hecho."

                ne "..."

            elif night05_elysium_cunnilingus_askStop == 1:

                ne "Ahh..."

                ne "Gracias por parar cuando te lo he pedido."

            else:

                ne "..."

            p "..."

            menu:

                pt "¿Y ahora?"

                "Me gustaría poder seguir haciéndote lo mismo después.":

                    ne "..."

                    if night05_elysium_cunnilingus_askStop >= 3:
                        $pl.ch_pts("np",-3)

                        ne "¡¿Estás de broma?!"

                        ne "¡¿Después de que casi tenga un orgasmo?!"

                        ne "¡¿Es que acaso hablo en Chino?!"

                        ne "Ni te me acerques a la entrepierna,"

                        ne "o tomaré medidas drásticas."

                        ne "¡¿Me explico?!"

                        p "..."

                    elif night05_elysium_cunnilingus_askStop == 2:
                        $pl.ch_pts("np",-1)

                        ne "No."

                        ne "Mejor que no."

                        ne "Especialmente cuando te digo que pares"

                        ne "y no lo entiendes a la primera."

                        p "..."

                    elif night05_elysium_cunnilingus_askStop == 1:
                        #$pl.ch_pts("np",-2)

                        ne "Mejor no."

                        ne "No creo que sea una buena idea."

                        ne "Aunque te agradezco el gesto."

                        ne "De verdad."

                "<No decir nada>":
                    call p_Help

                    pass


        #########

            if not night05_elysium_MCNaked:

                ne "Por favor,"

                ne "quítate la ropa y ponte cómodo en la cama."

                if not night05_elysium_NeusNaked:

                    call night05_elysium_NeusStrip

                $ night05_elysium_MCNaked = True

        "<Seguir>":
            call p_Help

            $ night05_elysium_cunnilingus_askStop += 1

            return

    jump night05_elysium_blowjobBefore


label night05_elysium_NeusStrip:

    p "¿Y tú?"

    ne "¿Euh...?"

    p "¿No te la quitas?"

    $ night05_elysium_NeusNaked = True

    call afternight05_Pedrera_NeusNaked
        # ne "..."
        # n "Vuelve a ponerse de puntillas para acercarse a tus labios y darte un dulce beso,"
        # n "mientras desabrocha el lazo frontal que sujeta su reducido corsé,"
        # n "exhibiendo así sus modestos pechos con sus pezones duros y rosados."

    scene day05
    with fade

    return

label night05_elysium_blowjobBefore:

    n "Yendo a gatas sobre el suave colchón,"

    if night05_elysium_MCNaked and night05_elysium_NeusNaked:

        n "se acerca como si fuera una felina en celo hasta tu desnuda entrepierna."

    else:

        if not night05_elysium_MCNaked:

            progcheck "You're still not naked."

        if not night05_elysium_NeusNaked:

            progcheck "She's still not naked."

#####

    ne "Hmm..."

    p "Creo que ya está bastante dura."

    ne "¿Eso es que no quieres que te la chupe?"

    menu:

        pt "Que me la chupe..."

        "Claro que me gustaría.":
            call p_Help

            ne "Me alegra oír eso."

        "Me parece injusto si yo no puedo hacerte lo mismo.":

            ne "..."

            ne "¿Cómo tengo que explicártelo para que lo entiendas?"

            p "..."

            ne "¿No quieres que lo haga?"

            menu:

                pt "Recibir su mamada..."

                "Preferiría que no.":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    ne "..."

                    ne "Como quieras..."

                    if night05_elysium_1rstRoundYou_action_Cond == "youControl":
                        jump night05_elysium_1rstRound_MCDom_Before
                    else:
                        jump night05_elysium_sheRidesYou

                "No he dicho eso.":
                    call p_Help

                    ne "Hmmm..."

                    ne "Así me gusta."

        "Preferiría que no.":
            call p_Help
            $pl.ch_pts("np",-2)

            ne "..."

            ne "Como quieras..."

            if night05_elysium_1rstRoundYou_action_Cond == "youControl":
                jump night05_elysium_1rstRound_MCDom_Before
            else:
                jump night05_elysium_sheRidesYou

        "...":
            call p_Help

            ne "..."

            ne "Tomaré eso como un sí."

    jump night05_elysium_blowjobBeginning

####



label night05_elysium_blowjobBeginning:

    if night05_elysium_blowjobBeginning_Cond == "":

        $ night05_elysium_blowjobBeginning_Cond = "bed"
    # else:
    #     $ night05_elysium_blowjobBeginning_Cond = "knees" - Revise if the text works ON KNEES position

    n "Acerca sus labios a la base de tu miembro -y mientras sientes el calor de su aliento-"

    n "besa sugerentemente la sensible piel de tus testículos."

    n "Corretea sutilmente y sin prisas sus suaves dedos por tus piernas a la altura de la pantorrilla,"

    n "pasando por tus rodillas"

    n "-y con sutileza- las acerca a tu ingle,"

    n "dónde también percibes su cálida lengua acariciar la piel que une tu miembro con tu bolsa escrotal."

    n "Desliza juguetonamente su lengua por la parte trasera a lo largo y ancho de tu miembro"

    n "hasta alcanzar el inicio del glande."

    n "Le dedica unos segundos para besarlo y lamerlo cuidadosamente."

    n "Sus manos acarician tus sensibles y húmedos testículos."

    n "Sigue mimándotela con su lengua hasta alcanzar la cima."

    n "A modo juguetón relame la parte superficial hasta acariciar el orificio del glande."

    n "Desplaza una de sus manos para masajear suavemente el erecto mástil."

    n "Sientes su cálido aliento mientras sus labios te rodean la rosada cima."

    n "Con suavidad, desciende su rostro cubriendo la punta de tu miembro con sus labios"

    n "mientras juguetonamente sigue mimando la parte trasera del glande con su cálida lengua."

    n "Al fijarte en su rostro, ves la expresión de una chica golosa y traviesa."

    if not gensex_INotLoveYouNeus:

        p "¡Auch!"

        n "Sientes un fuerte pellizco en tus pelotas."

        ne "No te quejes tanto..."

    n "Acto seguido desciende su rostro hasta casi meterse la mitad de tu miembro en su garganta."

    n "Su lengua juguetea con tu mástil a medida que asciende de nuevo."

    n "Al sumergirse lo hace volteando la cabeza, dando rodeos en el vaivén."

    n "Acerca la mano que no usa para masajear tus testículos a tu mástil"

    n "-a la altura dónde sus labios no logran descender más-"

    n "y desde ahí hasta el nacimiento des tus testículos masturba con el mismo ritmo el resto de tu miembro."

    n "Aumenta el compás de sus cabezadas al mismo tiempo que incrementa el calor que emerge del interior de su boca."

    p "Ugh..."

    n "Rápidamente se aparta de tu falo."

    ne "No,{w=0.2}{nw}"

    extend " no,{w=0.2}{nw}"

    extend " no,{w=0.2}{nw}"

    extend " no..."

    ne "Por mucho que me muera de ganas de saborearla,"

    ne "necesito sacar todo el jugo de tu esperma,"

    ne "y la mejor manera de lograr eso"

    ne "es que termines dentro de mí."

    p "..."

    jump night05_elysium_sheRidesYou

####

    # She Rides you.

label night05_elysium_sheRidesYou:

    # EMPIEZA SENTADA SOBRE TUS HUEVOS

    if night05_elysium_blowjobBeginning_Cond == "knees":

        n "Te lanza sobre la cama."

        p "¡Ugh!"

        n "Se acerca como si fuera  una gata en celo hasta que sus labios acarician tu miembro."

    n "Se reincorpora para sentarse sobre tus muslos posando tu miembro encima de su estómago"

    n "y asomándose entre sus modestos pechos:"

    ne "Realmente la tienes bien dura..."

    if night05_elysium_blowjobBeginning_Cond != "":

        pt "No sé por qué será..."

    n "Con sus cálidas manos acaricia tu erecto mástil sin quitarle el ojo de encima."

    n "Una longeva lengua emerge de sus labios y acaricia sutilmente la punta."

    if not night04_pedrera_blowjob_DONE:

        pt "¡Joder!"

        pt "¡Sí que la tiene larga!"

    ne "Me encanta su sabor..."

    if gensex_INotLoveYouNeus and night05_elysium_blowjobBeginning_Cond == "":

        p "¿Es necesario que hagas esto?"

        ne "..."

        ne "Necesito lubricártela un poco..."

    n "Asciende sus delicados dedos palpando la parte de tu glande"

    n "mientras su lengua se desliza por la sensible zona posterior de tu rosada cima."

    if night05_elysium_blowjobBeginning_Cond != "":

        pt "Suerte que ha parado de chupármela porque estaba a punto de correrme..."

    n "Asciende su cuerpo rozando su barriga por tu mástil hasta que su entrepierna logra acariciar tu glande,"

    n "para luego descender de nuevo restregando"

    n "no solo su cálida piel,"

    n "sino también sus húmedos y cálidos labios vaginales"

    n "por tu erecto miembro."

    n "Con lentitud pero firmeza repite ese mismo movimiento sin quitarte los ojos de encima"

    n "con una expresión que no te tranquiliza en absoluto."

    if afternight04_Pussy_dick_med_Speed_0_Done == 0 or FuckM_Start_Cond or FuckH_Start_Cond:

        # how to check if you tasted a pussy or not?

        pt "¿Tiene el coño más caliente de lo normal,"

        pt "o es que hace mucho tiempo que no follo?"

    n "En el vaivén, no solo percibes que aumenta el ritmo y que su labia externa es más ardiente,"

    n "sino que además tienes la sensación de que su carne rosada"

    n "se arrastra pegándose de una forma extraña en la delgada y sensible piel de tu miembro viril."

    p "Ughh..."

    ne "¿En serio?"

    ne "¿Tan pronto?"

    if night05_elysium_WhatNow_After_BlowjobDisgusting02:

        ne "Pensaba que me habías dicho que mi mamada te resultaba algo horrible."

        ne "Especialmente después de lo que viste ahí fuera."

    elif gensex_INotLoveYouNeus:

        ne "Creía que me habías dicho que se te habían pasado las ganas"

        ne "después de lo que viste ahí fuera."

    else:

        ne "Pensaba que después de todo lo que has visto ahí fuera perderías las ganas..."

    menu:

        pt "Lo que escuché tampoco se queda atrás..."

        "¿No habías dicho que no teníamos toda la noche?":
            call p_Help

            ne "Hmm..."

            ne "Eso es verdad."

            ne "Pero es que,"

            ne "se ve tan sabrosa..."

        "¿Es que a ti te pone cachonda lo que pasa ahí fuera?":
            call p_Help

            ne "¡Por supuesto que no!"

            ne "..."

            ne "Claro que no..."

            p "..."

            ne "¿Crees que soy un monstruo por estar tan caliente contigo"

            ne "a pesar de lo que hay ahí fuera?"

            menu:

                pt "Lo que hay ahí fuera..."

                "No creo que seas un monstruo, pero desde luego, preferiría estar en otro lugar.":
                    call p_Help

                    ne "¡¿Y te crees que yo no?!"

                    menu:

                        pt "..."

                        "Lo siento.":
                            call p_Help

                            ne "No pasa nada..."

                        "Por lo visto no lo parece.":
                            # $pl.ch_pts("np",-1)

                            call night05_elysium_sheRidesYou_excitment

                        "...":
                            call p_Help

                            $pl.ch_pts("np",-1)

                            ne "..."

                "Es un poco extraño, no te lo voy a negar.":
                    call p_Help

                    # $pl.ch_pts("np",-1)

                    call night05_elysium_sheRidesYou_excitment
                    
                "Después de lo que has vivido, soy incapaz de juzgarte.":
                    call p_Help

                    ne "..."

                    ne "Gracias por entenderlo, [protname]."

                    ne "Pero no quiero que lo hagas conmigo por pena."

                    p "Bueno, en realidad lo estamos haciendo por una cuestión de vida o muerte..."

                    ne "..."

                    pt "¿He dicho eso en voz alta?"

                    ne "Desde luego eso suena mucho más romántico."

                    p "..."

                    ne "*suspiro*"

                    ne "Si realmente tienes tan pocas ganas de hacerlo conmigo en este lugar..."

                    ne "No sé..."

                    ne "Podrías probar de masturbarte y cuando estés a punto me avisas"

                    ne "e intentaré meterme aunque sea la punta para que puedas correrte dentro de mí."

                    p "..."

                    ne "¿Quieres hacerlo de este modo?"

                    menu night05_elysium_unpleasant_question02:

                        pt "Masturbarme y luego meterle le punta..."

                        "Quizás sería lo mejor.":
                            call p_Help

                            $ night05_elysium_unpleasant_Cond = "probablyBest"

                            ne "..."

                            ne "Comprendo..."

                            $ night05_elysium_sexMast_Cond = True

                            jump night05_elysium_sexMast_label

                        "La verdad es que, aunque sea en este horrible lugar, preferiría poder hacerte el amor." if gensex_INotLoveYouNeus == False:
                            call p_Help

                            $ gensex_ILoveYouNeus = True

                            ne "¿El amor?"

                            p "Cuando dos personas que se aman practican el sexo, se le suele llamar así."

                            ne "..."

                            ne "¿Me amas?"

                            p "¿Por qué crees que he huido contigo si no?"

                            ne "..."

                            p "No te pongas a llorar ahora..."

                            ne "Idiota..."

                        "..." if night05_elysium_unpleasant_Cond == "":
                            call p_Help

                            $ night05_elysium_unpleasant_Cond = "silence"

                            ne "Necesito una respuesta."

                            p "..."

                            jump night05_elysium_unpleasant_question02

        "...":
            call p_Help

            ne "Por lo que veo,"

            ne "no ha sido así."

            ne "Me alegro que pueda causarte este efecto."

    jump night05_elysium_1rsRoundCumShot


label night05_elysium_sheRidesYou_excitment:

    ne "..."

    ne "No soy yo quien tiene la polla más dura que una piedra."

    p "¡Mi polla va a otro rollo!"

    ne "¿Y te crees que tú y tu polla no me provocáis?"

    menu:

        pt "¿\"Yo\" y \"mi polla\"?"

        "Quizás yo no puedo controlar mi erección, pero al menos no soy esclavo de mis deseos.":
            call p_Help

            ne "..."

            ne "Yo..."

            ne "No te haces una idea de lo que adictivo que me resultas."

            ne "De las ganas que tenía de estar a tu lado."

            p "¿De mí,"

            p "o de mi polla?"

            ne "..."

            ne "No seas idiota."

            ne "Es cierto que tu esperma me resulta enfermizamente adictivo y necesario para sobrevivir..."

            ne "Pero si no fueras la persona que eres,"

            ne "si resultases ser, aunque fuera mínimamente como Padre,"

            ne "no estaría aquí ahora contigo."

            ne "No arriesgaría nuestras vidas por alguien que no valiera la pena."

            if night05_Interrogation_YourFatherPower_Cond:

                pt "¡Menos mal que no me parezco a un proxeneta incestuoso sociópata!"

            else:

                pt "Su padre debe de ser alguien terrible..."

            ne "Y te prometo que has superado con creces mis expectativas."

            if gensex_INotLoveYouNeus:

                ne "Aunque me hayas dejado claro que no sientes nada por mí."

                p "..."

            ne "No soy tan superficial como crees."

            menu:

                pt "No es tan superficial..."

                "No se nota.":
                    call p_Help

                    ne "¡¿Acaso no entiendes que lo de ahora es una cuestión de vida o muerte?!"

                    menu:

                        pt "Cuestión de vida o muerte..."

                        "¿Entonces por qué no me masturbas y terminamos con esto cuanto antes?":
                            call p_Help

                            ne "..."

                            ne "¿Tan...?"

                            ne "¿Tan desagradable te resulto?"

                            menu night05_elysium_unpleasant_question01:

                                pt "Desagradable..."

                                "No, por supuesto que no.":
                                    call p_Help
                                    $pl.ch_pts("np",2)

                                    $ night05_elysium_unpleasant_Cond = "ofCourseNot"

                                    ne "¡¿Entonces a qué viene esto?!"

                                    p "Pues que cuanto antes salgamos de aquí"

                                    p "más seguros estaremos."

                                    p "Ya habrá otras noches para poder disfrutarlo,"

                                    p "pero no creo que ahora sea el momento."

                                    p "¡Simplemente estoy diciendo esto!"

                                    ne "..."

                                    ne "Ahmm..."

                                    ne "Ya..."

                                    p "¿Entonces?"

                                    ne "Bueno,"

                                    extend " supongo que tienes razón..."

                                    ne "Pero al ser nuestra primera vez,"

                                    ne "yo..."

                                    p "..."

                                    ne "*suspiro*"

                                "Bastante.":
                                    call p_Help
                                    $pl.ch_pts("np",-6)

                                    $ night05_elysium_unpleasant_Cond = "quite"

                                    $ night05_elysium_sexMast_Cond = True

                                    ne "..."

                                    n "Una lágrima empieza a desprenderse de su mejilla."

                                    ne "Yo..."

                                    if gensex_ILoveYouNeus:

                                        ne "Pensaba que habías dicho que me amabas..."

                                    else:

                                        ne "Pensaba que..."

                                    ne "..."

                                    ne "Supongo que estaba equivocada."

                                    p "..."

                                    ne "¿Por qué me has seguido hasta aquí si me odias tanto?"

                                    p "Dijiste que era una cuestión de vida o muerte."

                                    ne "..."

                                    ne "Y lo es."

                                    p "Entonces entenderás que no quiero morir."

                                    ne "..."

                                    ne "Ya veo..."

                                    $ gensex_ILoveYouNeus = False
                                    $ gensex_INotLoveYouNeus = True
                                    $ gensex_YoureAMonster = True

                                "..." if night05_elysium_unpleasant_Cond == "":
                                    call p_Help

                                    $ night05_elysium_unpleasant_Cond = "silence"

                                    ne "¡Al menos di algo!"

                                    p "..."

                                    jump night05_elysium_unpleasant_question01

                        "Quizás, pero al menos no finjas lo que no es.":
                            call p_Help

                            ne "¡¿El qué?!"

                            ne "¡Que necesito tu esperma para sobrevivir;"

                            ne "que si volviera con Padre me torturaría durante décadas"

                            ne "en una asfixiante y dolorosa espiral de dolor, sufrimiento y agonía;"

                            ne "que aunque no fueras una persona tan maravillosa"

                            ne "quizás preferiría estar contigo que con él?"

                            ne "¡¿Es eso lo que quieres saber?!"

                            ne "¿Disfrutas restregándome por la cara que no tengo muchas opciones?"

                            $ night05_elysium_sheRidesYou_honesty_Cond = False

                            menu:

                                pt "No tiene muchas opciones..."

                                "¿Entonces admites que no estás conmigo por amor, sino porque soy tu única opción?":
                                    call p_Help

                                    $pl.ch_pts("np",-3)

                                    ne "..."

                                "Por supuesto que no.":

                                    call night05_elysium_sheRidesYou_honesty

                                "Por supuesto que no, ya te he dicho que te amo."if gensex_ILoveYouNeus:

                                    call night05_elysium_sheRidesYou_honesty

                                "...":
                                    call p_Help

                                    $pl.ch_pts("np",-1)

                            if not night05_elysium_sheRidesYou_honesty_Cond:

                                ne "Quizás en el fondo no eres tan distinto a él..."

                "...":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    ne "..."


            p "..."

            if night05_elysium_sexMast_Cond:

                jump night05_elysium_sexMast_label

            else:

                ne "¿Quieres que siga?"

                ne "¿O prefieres masturbarte y correrte dentro de mí cuando estés a punto...?"

        "Tienes razón Neus, lamento lo que te he dicho.":
            call p_Help

            $pl.ch_pts("np",1)

            ne "..."

            ne "No..."

            ne "Soy yo quien lamenta actuar de este modo."

            ne "No te imaginas las ganas que tenía de tenerte así..."

            ne "Aunque,"

            n "Una lágrima se desprende de su mejilla."

            ne "lamento que sea en estas condiciones..."

            menu:

                pt "¿Lamenta estar cachonda?"

                "No te preocupes, Neus.":
                    call p_Help

                    ne "Perdona..."

                    ne "No debería estar llorando en estos momentos."

                    ne "No cuando tengo esto delante a punto de estallar."
                    
                "<Abrazarla>" if not gensex_INotLoveYouNeus:
                    call p_Help

                    $pl.ch_pts("np", 1)
                    
                    ne "..."

                    n "Sientes su desnudo y cálido cuerpo al contacto con el tuyo"

                    n "mientras sigue sentada sobre tus piernas"

                    n "y tu polla está prisionera entre vuestras barrigas."

                    n "Te agarra con más fuerza al mismo tiempo que humedece tu pecho con sus lágrimas."

                    pt "Me va a quedar la polla hecha mierda..."

                    ne "[protname];"

                    p "¿Hmm...?"

                    ne "Gracias."

                    n "Se aparta dulcemente para luego darte un suave beso en los labios."

                "...":
                    call p_Help

                    $pl.ch_pts("np", -1)
                    
                    ne "Soy así de tonta..."

                    n "Rápidamente se seca la lágrima de su mejilla."

        "...":
            call p_Help

            ne "No soy de piedra, ¿sabes?"

            p "..."
    return

label night05_elysium_sheRidesYou_honesty:

    $ night05_elysium_sheRidesYou_honesty_Cond = True

    ne "¿Entonces por qué me dices estas cosas?"

    if gensex_ILoveYouNeus:

        p "Porque en el amor me gusta la sinceridad por delante de todo."

    else:

        p "Porque me gusta la sinceridad por delante de todo."

    ne "..."

    ne "Su..."

    ne "Supongo que tienes razón."

    return


label night05_elysium_1rsRoundCumShot:

    n "A pesar de haberse detenido,"

    n "la cálida piel de su estómago y su húmeda entrepierna"

    n "siguen pegadas a tu erecto miembro."

    ne "La verdad es que me pasaría la noche entera devorándola."

    with vpunch

    p "Hhmm..."

    n "Tu falo convulsiona al borde de la explosión."

    ne "No,{w=0.2}{nw}"

    extend " no,{w=0.2}{nw}"

    extend " no,{w=0.2}{nw}"

    extend " no..."

    n "Rápidamente, se pone de pie sobre la cama"

    ne "¡Espera!"

    n "y se mete a toda prisa la punta de tu miembro en su interior."

    n "Apenas lo consigue cuando..."

    $ night05_elysium_MCCumshots += 1

    with vpunch
    with vpunch
    p "¡Uughh...!"

    n "Lentamente, desciende hasta que casi una cuarta parte de tu polla desaparece en su interior."

    ne "Hmmm..."

    ne "Ibas bastante cargadito."

    n "Sin quitársela de su sexo,"

    n "te agarra por los hombros y voltea vuestros cuerpos"

    n "hasta que su espalda reposa sobre la sábana"

    n "y tú terminas encima de su desnudo cuerpo aún descargando en su interior."

    n "Cruza sus piernas sobre tus nalgas empujándote hacia ella"

    n "mientras desliza su entrepierna en círculos con el fin de intentar metérsela más adentro."

    n "Te acaricia por el cuello a la par que te mira desde la altura de tu pecho."

    if not gensex_INotLoveYouNeus:

        n "Debido a su baja estatura no logra llegar a tus labios."

        n "Agarrándote por la nuca, te empuja para forzarte a ello."

        n "Su beso es apasionado pero también caluroso y su lengua no te deja casi ni respirar."

        n "Cuando se aparta de tus labios, prosigue por tu mejilla, el cuello,"

        n "hasta que finalmente reposa su mejilla contra tus pectorales y deposita sus manos por tu espalda"

        n "tomándote en un suave abrazo."

    ne "Déjala ahí unos segundos."

    p "¿Uh...?"

    ne "Solo unos segundos..."

    n "Sientes su cálida respiración sobre tu pecho."

    n "La carne de su coño parece cobrar vida propia moviéndose en espasmos,"

    n "como si absorbiera los restos de esperma que queda alrededor de tu miembro."

    n "Sus caderas desaceleran."

    if gensex_ILoveYouNeus:

        n "Percibes sus labios besándote la piel de tus pectorales sin prisas, con suavidad y dulzura."

    jump night05_elysium_2ndRoundBeginnig


#########
label night05_elysium_2ndRoundBeginnig:

    menu:

        pt "¿Y ahora?"

        "Me gustaría seguir teniendo el control" if night05_elysium_1rstRoundYou_action_Cond == "youControl":
            call p_Help

            jump night05_elysium_2ndRoundYou
                # ne "Hmmmm..."
                # if night05_elysium_1rstRoundYou_action_Cond == "youControl":
                #     ne "Prométeme que seguirás deteniéndote cuando te lo pida."

        "Me gustaría poder tomar un poco el control ahora." if night05_elysium_1rstRoundYou_action_Cond != "youControl":
            call p_Help

            if night05_elysium_cunnilingus_askStop >= 3:

                ne "..."

                ne "Estás de broma, ¿verdad?"

                p "¿Por?"

                ne "¿Después de que te pidiera que te parases más de [night05_elysium_cunnilingus_askStop] veces?"

                ne "¡Y aún así seguiste hasta que tuve que detenerte a la fuerza!"

                ne "Lo siento,"

                ne "pero es demasiado arriesgado."

                jump night05_elysium_2ndRoundHer

            else:

                jump night05_elysium_2ndRoundYou

        "...":
            call p_Help

            jump night05_elysium_2ndRoundHer

    
label night05_elysium_2ndRoundHer:

    $ night05_elysium_2ndRoundYou_pos_Cond = "NeusRides"

    ne "Hmmm..."

    ne "Vaya..."

    ne "Parece que se está volviendo fofa."

    p "Por si no lo has notado,"

    p "he tenido un orgasmo."

    ne "*risilla inocente*"

    ne "Ya lo sé, tontín."

    pt "Encima..."

    ne "Tranquilo,"

    ne "ya me encargo de reanimártelo."

    n "Con suavidad y dulzura lo sustrae de su interior y se aparta de ti"

    n "para luego darte la vuelta, haciendo que reposes tu desnuda espalda en la cómoda alcoba."

    if gensex_ILoveYouNeus:

        n "Se acerca sugerentemente a tu rostro y te da un apasionado beso con lengua."

    else:

        n "Se acerca sugerentemente a tu mejilla y te da un dulce beso."

    n "Desciende sus labios por tu cuello, tu pecho, tus abdominales, tu ombligo"

    n "y finalmente alcanza tu flácido miembro."

    n "A modo juguetón desliza su lengua por su alrededor,"

    n "relamiendo el escaso esperma que permanece por tu sensible piel"

    n "mientras acaricia con habilidad y soltura tus testículos."

    n "Desliza su lengua a lo largo del manubrio hasta alcanzar el glande"

    n "dónde le dedica un cariño extra combinando sus labios y su lengua."

    n "Sientes su cálido aliento al mismo tiempo que el masaje de sus manos en tu parte baja."

    n "Introduce el glande en su boca mientras lo relame en círculos con su lengua."

    n "Sin demasiado esfuerzo logra tragárselo entero en su garganta."

    n "Sientes en espasmos el flujo sanguíneo volviendo a tu polla."

    n "Sufres ligeros espasmos en su estrecho, húmedo y ardiente interior,"

    n "como si la carne de su conducto digestivo tuviera vida propia"

    n "y estrujara con más fuerza tu lastimado falo,"

    n "al mismo tiempo, su lengua relame la parte externa hasta alcanzar la piel de tus testículos"

    n "logrando que vayas recuperando la virilidad."

    n "Percibes sus labios cada vez más lejos de tus testículos"

    n "a medida que tu miembro va creciendo en tamaño"

    n "hasta el punto que ni siquiera le cabe la mitad del mismo en sus fauces."

    n "Finalmente se aparta de él."

    ne "AAAhh-ahhh..." # Gemidos recuperando el aliento.

    n "Con una mirada de deseo y con un tinte de preocupación"

    ne "Parece que ya se está recuperando."

    ne "Es una lástima que no me quepa entera en la garganta..."

    n "Se reincorpora poniéndose de pie y acercando su cálido sexo en la cima de tu miembro."

    n "Con dulzura desciende sus caderas engullendo tu glande entero en su interior."

    ne "Hmmm..."

    n "Sigue bajando sus entrepierna hasta que casi logra enterrar la mitad de tu polla en su sexo."

    ne "Realmente es enorme."

    n "Manteniéndola en la misma profundidad,"

    n "se pone de rodillas y desciende su busto contra tu pecho besándote por el cuello."

    if gensex_ILoveYouNeus:

        n "Sigue ascendiendo hasta alcanzar tus labios para besarte con lengua de nuevo."

        ne "Me pasaría el día besándote."

    n "Vuelve a descender desplazando sutilmente sus caderas a lo largo del mismo"

    n "haciendo que percibas el calor de su sexo a través de él."

    ne "Hmmm..."

    p "¿Qué ocurre?"

    if gensex_ILoveYouNeus:

        ne "Así no alcanzo a besarte."

    else:

        ne "Así no alcanzo ni a mirarte a los ojos."

    menu:

        "Eres demasiado bajita.":
            call p_Help

            if not gensex_INotLoveYouNeus:

                ne "*GGnnn*"

                ne "Quizás es que tú eres demasiado alto."

            else:

                $pl.ch_pts("np",-1)

                ne "..."

                ne "Tampoco hace falta que me lo recuerdes."

                if gensex_YoureAMonster:

                    p "Si no te haces más grande es porque no quieres."

                    ne "..."

        "Lo lamento.":
            call p_Help

            if not gensex_INotLoveYouNeus:

                ne "No..."

                ne "No pasa nada."

            else:

                $pl.ch_pts("np",1)

                ne "..."

                ne "Gracias [protname]."

        "...":
            call p_Help

    ne "Hmm..."

    ne "Supongo que no hay otro modo."

    p "¿Qué?"

    n "A medida que sus caderas se desplazan arriba y abajo, sientes que el interior de sus exo va aumentando de temperatura, pero no solo eso, todo su cuerpo parece incrementar de temperatura, su modesto busto, sus manos que siguen acariciando tu pecho, sus labios y su aliento."

    n "Sientes las manos que acarician tu pecho no solo aumentar en temperatura, sino que te da la sensación que son ligeramente más grandes, su pecho que está en contacto directo con tu pecho desnudo, te da la sensación de que no solo es más caliente, si no que su modestos pechos parecen ligeramente más voluminosos."

    

    n "Sientes la carne de su sexo no solo más caliente, sino que te da la sensación que su carne cobra via propia removiendo tu miembro en su interior."

    n "Al fijarte en la cabeza de Neus, tienes la sensación de que cada vez la tienes más cerca y sus ojos recuperan ligeramente ese brillo en sus ojos."

    n "Sientes sus labios subiendo por tu pecho,"

    p "Auch!"

    p "¿Por qué te gusta tanto morderme?"

    ne "Pero si en el fondo te gusta."

    n "Sientes su lengua recorrer tu clavícula, para luego deslizarse por tu cuello, besar tu mejilla y finalmente tus labios para introducir su lengua y besarte con pasión y lujuria."

    p "¿Cómo?"

    n "A pesar de haber subido hasta tus labios, sientes que tu polla está cada vez más enterrada en su sexo."

    n "Sientes su busto bastante más voluminoso que antes y te fijas en que todo su cuerpo ha aumentado de tamaño consdierablemente."

    n "AL fijarte en su rostro, ves un rostro mucho más estilizado y maduro en su rostro, y sus ojos ligeramente brillantes con un rostro de lujuria y deseo."

    ne "Te amo tanto."

    n "Vuelve a besarte con hambre y deseo introduciéndote tanto la lengua que apenas eres capaz de respirar."

    n "Sientes que acelera el movimiento de sus caderas."

    n "En cada nueva embestida sientes que cada vez logra enterrar más tu miembro en su sexo."

    n "Hasta el punto que sientes su nalgas acariciar tu ingle."

    pt "¡¿Se la ha metido entera?!"

    n "Sientes el calor de su carne moviéndose con vida propia a medida que sus caderas se desplazan."

    p "Ughh..."

    n "Empiezas el particular cosquilleo recorrer tus piernas."

    pt "No aguanto una mierda..."

    n "Sus caderas se detienen en seco al mismo tiempo que ves una expresión de angustia y preocupación en su rostro."

    n "Apartando sus labios de los tuyos."

    ne "Mierda..."
    
    n "Al fijarte en sus ojos, ves que brillan con una enorme intensidad."

    ne "Dios..."

    menu:

        pt "¿Ahora se para?"

        "<Darle más caña>":
            call p_Help

            jump night05_elysium_NeusOrgasm

        "Estás a punto de tener un orgasmo, ¿verdad?":
            call p_Help

            ne "Sí..."

            jump night05_elysium_2ndRoundHerSheStops

        "...":
            call p_Help

            jump night05_elysium_2ndRoundHerSheStops

label night05_elysium_2ndRoundHerSheStops:

    ## Still it's ## if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides"

    call night05_elysium_2ndRoundYou_stopContinue
        # ne "Solo..."
        # ne "Dame unos segundos..."
        # n "Ves que su expresión es tensa y su respiración agitada."
        # p "¿Estás bien?"
        # ne "Ahora no [protname]."
        # (...)
        # ne "Estás a punto de correrte,"
        # ne "¿verdad?"
        # p "Sí..."

    ne "Hmmm..."

    n "Un largo suspiro surge de sus pulmones"

    ne "Así me gusta."

    n "mientras te muestra una expresión aparentemente forzada de serenidad."

    ne "Quiero que me des todo el esperma que puedas."

    n "Su tono de voz no contiene ni una pizca de broma,"

    n "sino más bien tintes de anhelo y un voraz apetito."

    # Solo tiene la punta en su interior, solo el glande.

    n "Desciende sus caderas con lentitud"

    n "hasta casi tragarse la mitad de tu miembro."

    ne "Ughhn..."

    # Parece que le duele.

    menu:

        pt "Parece que le duele."

        "¿Estás bien?":
            call p_Help
            $pl.ch_pts("np",1)

            if gensex_INotLoveYouNeus:

                ne "..."

                ne "Pensaba que no te preocupabas por mí."

                if gensex_YoureAMonster:

                    p "Tampoco soy un monstruo como tú."

                    ne "..."

                    ne "Tampoco hace falta que me digas estas cosas..."

                else:

                    p "Tampoco soy un monstruo."

                    ne "..."

            else:

                ne "Sí."

                ne "Estoy bien."

            if not gensex_YoureAMonster:

                p "¿Estás segura que puedes continuar?"

            ne "Hmm..."

        "...":
            call p_Help

            pass

    ne "Supongo que no hay otro modo."

    n "Percibes su vagina mucho más cálida."

    ne "Aaaahh--ahhmm..." # painful-pleasure moanings.

    n "Su tono de voz aumenta en decibelios."

    p "¡Ugh!"

    p "Neus..."

    n "Percibes sus pechos aumentando de volumen,"

    n "sus caderas más pesadas"

    n "descendiendo por tu falo hasta terminar tragándoselo por completo en su interior"

    n "y su rostro cada vez más cerca del tuyo"

    n "con esa expresión mucho más madura y estilizada."

    ne "Da-"

    n "Agarrándote con tanta fuerza de tus pectorales"

    n "que sientes sus uñas clavándose en tu carne."

    ne "Dámelo"

    n "Sientes sus nalgas acariciando la carne de tu pelvis"

    n "al mismo tiempo que tu polla sufre un infierno"

    n "en esa inquieta y ardiente carne de su sexo."

    n "Dámelo todo."

    n "Con vehemencia y entusiasmo te besa de nuevo con su fogosa lengua."

    n "Sus caderas empiezan a deslizarse a lo largo de tu miembro."

    n "A pesar de que apenas te da tiempo a respirar,"

    n "y de que sus enormes senos te aplastan el pecho,"

    n "eres capaz de ver en su mirada esos brillantes ojos recuperando su esplendor."

    n "Sus nalgas te embisten a mayor celeridad y dureza en cada nueva acometida."

    n "Toda su piel está abrasándote, pero en especial,"

    n "percibes su vagina como si tuvieras tu polla metida en cera ardiente."

    p "Ugh..."

    n "La alcoba entera está temblando."

    n "Sus nalgas impactan con tanta energía sobre tu ingle"

    n "que te da la sensación de que te está dando cachetadas con la carne de sus nalgas"

    n "y empiezas a sentir el hueso de sus caderas clavándose en tu piel."

    n "Oyes el crujir de la madera y el chirrido que hacen las patas de la cama al desplazarse."

    pt "¡Encima de dejarme sin caderas acabará por romper la cama!"

    ne "¡Córrete!"

###

    n "Se aparta de tus labios para ponerse de pie sobre la cama."

    n "Agarrándote de las piernas levanta tu trasero para luego enterrar su miembro entero en su interior."

    p "Ugh..."

    n "En esa posición amazónica empieza a embestirte de con nuevo con solidez y rudeza"

    n "Te sujetas a la sábana cómo puedes para soportar el peso y brusquedad de sus acometidas,"

    n "follándote como si fueras su esclavo sexual."

    n "Vuelves a sentir el particular cosquilleo en tu entrepierna."

    n "Cada vez que se traga tu falo al completo,"

    n "sientes esas extrañas lenguas en lo profundo de su sexo"

    n "intentando pegarse al glande como si fueran los tentáculos de un pulpo en busca de su presa."

    n "Una expresión alocada y hambrienta se dibuja en su rostro"

    n "al mismo tiempo que ves sus ojos brillar con intensidad."

    n "[protname]..."

    n "Sus mejillas están al rojo vivo,"

    ne "¡Co-!"

    n "su respiración es agitada,"

    ne "¡Corre-!"

    n "sus gemidos aumentan en cantidad y volumen."

    ne "{size=70}¡CÓRRETE!{/size}"

    $ night05_elysium_MCCumshots += 1

    ## if night05_elysium_2ndRoundYou_pos_Cond == "missionary":
    with vpunch
    with vpunch
    p "¡Uuuhhg!"

    n "En su última acometida se lo entierra por completo"

    n "haciendo que descargues en su infernal y angosto interior."

    n "A medida que vas descargando, te presiona la ingle con tanto vigor"

    n "que sientes que acabará quebrándote algún hueso."

    n "Manteniéndola entera en su calcinante interior,"

    n "empieza a dar círculos con sus caderas para intentar ordeñar aún más tu maltrecha polla."

    n "Percibes ese montón de lenguas en lo profundo de su sexo"

    n "acariciando y succionando tu miembro sin compasión."

    ne "Aahhh..."

    n "Un agudo gemido surge de sus labios mientras sus ojos brillan con intensidad."

    n "Sientes que su cuerpo empieza enfriarse a medida que su coño se va volviendo más estrecho."

    n "Sus hasta enormes y voluminosos pechos va encogiéndose."

    n "Entre gemidos de placer y de tenue dolor,"

    n "va apartándose de ella al mismo tiempo que su cuerpo disminuye de tamaño"

    n "hasta que algo menos de una cuarta parte persiste en su interior."

    n "Tus parpados poco a poco se van cerrando."

    n "Sientes que su cuerpo termina cayendo extenuado sobre tu desnudo pecho."

    n "Y teniendo aún tu glande relativamente enterrado en su cálido sexo"

    n "tus ojos terminan por cerrarse."

    jump night05_elysium_3rdRoundBeginning
        # p "Uh..."
        # n "Sientes su respiración por tu pecho"
        # n "mientras sus labios buscan besarte por toda la piel que encuentra delante."
        # p "¿Neus?"
        # n "Posa sus manos sobre ambos pectorales y con una fuerza sorprendente separa suavemente vuestros cuerpos."
        # n "Aparta su cadera de tu polla -que seguía hundida en su interior-"
        # n "para luego tumbarte y posar tu espalda sobre la sábana y ponerse ella encima de ti."


label night05_elysium_2ndRoundYou:

    ne "Hmmmm..."

    if night05_elysium_1rstRoundYou_action_Cond == "youControl":

        ne "Prométeme que seguirás deteniéndote cuando te lo pida."

    else:

        ne "Solo si me prometes que pararás cuando te diga que pares."

    $ night05_elysium_2ndRoundYou_question_Cond = False

    menu night05_elysium_2ndRoundYou_question:

        pt "Parar cuando me lo pida."

        "No puedo prometerte eso.":

            ne "..."

            ne "Entonces no."

            ne "Lo siento, pero es demasiado arriesgado."

            jump night05_elysium_2ndRoundHer

        "Te lo prometo.":

            jump night05_elysium_2ndRoundYou_promise

        "..." if night05_elysium_2ndRoundYou_question_Cond == False:

            $ night05_elysium_2ndRoundYou_question_Cond = True

            ne "Necesito una respuesta."

            jump night05_elysium_2ndRoundYou_question


label night05_elysium_2ndRoundYou_promise:

    if night05_elysium_cunnilingus_askStop == 2:

        ne "No hagas que te lo repita más de una vez."

        ne "¿De acuerdo?"

        p "De acuerdo."

    elif night05_elysium_cunnilingus_askStop == 1:

        ne "Hmmm..."

    else:

        pass

    n "Una dulce sonrisa se dibuja en su rostro."

    if night05_elysium_1rstRound_MCDom_pose == "missionary":
        ne "¿Me quieres volver a follar de frente"
    else:
        ne "¿Me quieres follar de frente"

    if night05_elysium_1rstRound_MCDom_pose == "doggy":
        ne "o prefieres que me vuelva a poner a cuatro patas?"
    else:
        ne "o a lo perrito?"

    $ night05_elysium_2ndRoundYou_pos_Cond = ""

    menu night05_elysium_2ndRoundYou_position_Question:

        pt "¿En qué posición?"

        "Prefiero tenerte a cuatro patas":
            call p_Help

            if night05_elysium_1rstRound_MCDom_pose == "missionary":

                ne "Ahora no podré mirarte a la cara."

            elif night05_elysium_1rstRound_MCDom_pose == "doggy":

                ne "Veo que te gusta tenerme así..."

            $ night05_elysium_2ndRoundYou_pos_Cond = "doggy"

            jump night05_elysium_2ndRoundYou_SexBeginning

        "Prefiero tenerte de frente.":
            call p_Help

            if night05_elysium_1rstRound_MCDom_pose == "missionary":

                ne "Así que igual que antes..."

            elif night05_elysium_1rstRound_MCDom_pose == "doggy":

                ne "Así que ahora quieres cambiar..."

            $ night05_elysium_2ndRoundYou_pos_Cond = "missionary"

            jump night05_elysium_2ndRoundYou_SexBeginning

        "Quiero hacerte el amor." if not gensex_INotLoveYouNeus and night05_elysium_2ndRoundYou_pos_Cond != "love":
            call p_Help

            $ night05_elysium_2ndRoundYou_pos_Cond = "love"

            ne "..."

            if not gensex_ILoveYouNeus:
                # Did you made her Love the first time? then you said you love her, so this options should be Ok.
                $pl.ch_pts("np",3)

                $ gensex_ILoveYouNeus = True

                ne "¿El amor?"

                ne "¿Lo dices en serio?"

                p "No bromearía con algo así."

                ne "¿Realmente me amas?"

                p "Sí."

                ne "..."

                if gensex_NotLoveSister:

                    ne "¿Aunque sea tu hermana?"

                    p "A pesar de ello."

                n "Te agarra del cuello y te empuja hacia ella para darte un dulce beso."

                ne "Te amo tanto..."

                p "..."

                ne "Quie-"

                extend "quieres..."

            else:

                $pl.ch_pts("np",1)

                ne "Euhh..."

                ne "He..."

                ne "Vale..."

            if gensex_ILoveYouNeus:

                ne "¿Quieres hacerme el amor de frente"

                ne "o mientras estoy a cuatro patas?"

            else:

                ne "¿Quieres hacérmelo de cara"

                ne "o a cuatro patas?"

            jump night05_elysium_2ndRoundYou_position_Question

        "¿Cuál prefieres?" if night05_elysium_2ndRoundYou_pos_Cond == "love":
            call p_Help

            ne "..."

            ne "Me gusta mirarte a la cara,"

            ne "pero confieso que me pone muy perra estar a cuatro patas..."

            menu:

                pt "¿Entonces cuál prefiere?"

                "A mí también me gustaría poder verte la cara mientras gimes de placer.":
                    call p_Help
                    $ night05_elysium_2ndRoundYou_pos_Cond = "missionary"

                    ne "..."

                    ne "Ey..."

                    ne "No seas malo."

                    ne "O al final no podré ni mirarte."

                "A mí también me gusta poder verte a los ojos mientras hacemos el amor.":
                    call p_Help
                    $ night05_elysium_2ndRoundYou_pos_Cond = "missionary"

                    ne "..."

                    ne "No me seas tan cursi protname..."

                    ne "HA-"

                    extend "haces que me cueste hasta respirar..."

                    pt "Y luego el cursi soy yo."

                "Entonces te voy a hacer el amor como si fueras una perrita.":

                    $ night05_elysium_2ndRoundYou_pos_Cond = "doggy"

                    ne "..."

                    ne "Tampoco hace falta ser tan literal..."

                "La verdad es que también me pone muy caliente poder tenerte a cuatro patas.":

                    $ night05_elysium_2ndRoundYou_pos_Cond = "doggy"

                    ne "..."

                    ne "¿De verdad?"

                    p "Sí."

                    n "Alarga su cuello para darte un beso."

                    ne "Entonces dame amor por detrás."

                    menu:

                        pt "¿Por detrás?"

                        "¿Por el ano?":

                            ne "..."

                            ne "No."

                            ne "No es que odie la idea,"

                            ne "pero..."

                            ne "Es mejor que no nos arriesguemos"

                            ne "y acabes corriéndote en el agujero equivocado."

                            $ night05_elysium_2ndRoundYou_promise_anal_Cond = ""

                            menu night05_elysium_2ndRoundYou_promise_anal_question:

                                pt "Agujero equivocado..."

                                "Tengo mayor control después de la primera corrida." if night05_elysium_2ndRoundYou_promise_anal_Cond == "":
                                    call p_Help

                                    $ night05_elysium_2ndRoundYou_promise_anal_Cond = "control"

                                    ne "Y te creo."

                                    ne "Pero es mejor no arriesgarnos."

                                    jump night05_elysium_2ndRoundYou_promise_anal_question

                                "¿No será eso una excusa por miedo a que no te quepa por ahí?":
                                    call p_Help

                                    ne "..."

                                    ne "No te negaré que el tamaño de tu polla es algo intimidante."

                                    ne "Pero en realidad,"

                                    ne "es más bien porque no gozamos del tiempo suficiente."

                                    n "Te da un suave beso en la barbilla."

                                    ne "Hazlo por mí,"

                                    ne "por favor."

                                    p "*suspiro*"

                                    p "Como quieras."

                                    n "Una dulce sonrisa se dibuja en sus labios."

                                "...":
                                    call p_Help
                                    pass


                        "...":
                            call p_Help
                            pass

            jump night05_elysium_2ndRoundYou_SexBeginning

        "..." if night05_elysium_2ndRoundYou_pos_Cond == "":

            $ night05_elysium_2ndRoundYou_pos_Cond = "silence"

            ne "Tienes que elegir."

            jump night05_elysium_2ndRoundYou_position_Question


label night05_elysium_2ndRoundYou_SexBeginning:

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        if gensex_ILoveYouNeus:

            n "Acercas tus labios a los suyos y le regresas un dulce beso."

            n "Te agarra por el cuello y te lo acompaña profundizando aún más en él"

            n "mientras mueve sus caderas para sentir tu polla -algo más flácida- en sus adentros."

        else:

            n "Mientras mueve sus caderas para sentir tu polla -algo más flácida- en sus adentros."

        ne "Me alegra ver que incluso después de una corrida"

        ne "no has perdido del todo la erección."

        p "Eso es por que tu coño está haciéndole cosas raras."

        ne "Hmmm..."

        ne "Es posible."

        pt "Es posible dice..."

    elif night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        ne "Hmm..."

        n "Te mira la entrepierna con una expresión de deseo y cierto temor."

        ne "No está muy dura,"

        n "Sientes sus cálidas manos acariciándotela."

        ne "pero me imagino que bastará."

        n "Estando de rodillas sobre la cama,"

        n "a modo seductor y sin prisas, te da la espalda"

        n "para luego reposar sus manos sobre la sábana."

        n "Levanta su trasero tanto como puede para intentar acariciar tu miembro"

        n "balanceándolo en círculos de un modo provocativo y sugerente." #Bailar, agasajador, invitación, ... ni zorra.

        n "Agarrándote el instrumento, lo posas en medio de sus pequeñas nalgas,"

        n "ejerciendo con tus manos cierta presión en ellas"

        n "intentas apretujarlas para masturbar tu manubrio entre ellas."

        ne "Hmmm..."

        n "A pesar de lo esponjosas y suaves que son"

        n "no son lo suficientemente carnosas y voluminosas"

        n "para cubrir ni una pequeña parte de tu enorme falo."

        n "Aún así, tu mástil consigue ir recobrando poco a poco su rigidez."

        n "Con una mano acaricias su entrepierna."

        n "Percibes su abundante humedad, pero también lo ceñida y estrecha que está su cavidad vaginal."

    else:

        aj "¿What? ERROR 198+3+"

    ne "[protname]."

    p "¿Sí?"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Rotando su rostro para mirarte con una mirada sugerente y casi de animal en celo..."

    else:

        n "Dedicándote una mirada sugerente y casi de animal en celo."

        if gensex_ILoveYouNeus:
            $ night05_elysium_2ndRoundYou_mood = "romantic"

    if gensex_ILoveYouNeus:

        ne "Hazme el amor."

    else:

        ne "Fóllame."

    if gensex_ILoveYouNeus:

        if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

            menu:

                pt "¿A cuatro patas?"

                "Lo que tú digas, cariño.":
                    $pl.ch_pts("np",1)

                    $ night05_elysium_2ndRoundYou_mood = "romantic"

                    ne "Hmmm..."

                "No sé yo si es muy romántico hacerlo así...":

                    $ night05_elysium_2ndRoundYou_mood = "wild"

                    ne "*Gnnn*"

                    ne "No seas tonto,"

                    ne "claro que es romántico,"

                    ne "si lo haces con amor."

                    p "..."

                    ne "Me ha quedado demasiado cursi,"

                    ne "¿verdad?"

                    menu:

                        pt "Euhmm..."

                        "Un poco...":
                            call p_Help

                            ne "Bueno,"

                            extend " me da igual."

                        "Prefiero no responder a eso.":
                            call p_Help

                            ne "Hmmm..."

                        "Por supuesto que no.":
                            call p_Help

                            ne "La verdad es que sí."

                            ne "Pero me da igual."

                    n "Ves que amolda su rostro sobre la sábana"

                    n "mientras alza aún más sus nalgas a modo de invitación."

                    ne "Fóllame bien duro,"

                    ne "si es lo que prefieres que te diga."

                "...":

                    ne "..."


label night05_elysium_2ndRoundYou_SexMoving:

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        if gensex_ILoveYouNeus:

            n "Vuelves a besarla tiernamente mientras desplazas tus caderas penetrando su interior."

            ne "Hmmm..."

            n "La besas por el cuello mientras masajeas dulcemente sus pechos."

            n "Abrazándose a ti, te acaricia la espalda con cariño."

            n "Cuando te apartas de su rostro descubres en sus ojos un brillo tenue,"

            n "una mirada de deseo y una sumisión absoluta."

            n "Acerca una de sus manos hasta tu mejilla y alarga su cuello para besarte de nuevo."

        else:

            # Do you have your dick inside of her? Yes, barely.

            n "Desplazas tus caderas intentando profundizar aún más en su sexo."

            ne "Ughh..."

            n "No solo es extremadamente estrecho y angosto, sino que además está algo más caliente que antes."

            n "Te da la sensación que su carne interina está moviéndose como si tuviera vida propia"

            n "acariciando tu polla en pequeños y rítmicos espasmos en ese ardiente interior."

            pt "¿Qué narices?"

        ## Continue:
            ## ne "Fóllame más duro..."

        
    else:

        # if night05_elysium_2ndRoundYou_mood == "romantic":
        #     #Your fuck her romantically
        # else:
        #     # you fuck her wildly.

        n "Apartas tu miembro de sus nalgas mientras sigue balanceando su trasero a modo de invitación."

        n "Acercas la punta de tu miembro a su cálido sexo y lentamente se la vas introduciendo."

        n "Al lograr embutir tu glande entero en su vagina,"

        n "descubres que su carne interina es ligeramente más caliente que antes."

        ne "Uhhmm..."

        n "El tono de su gemido no te parece exactamente de puro placer."

        menu:

            pt "Es obvio que le estoy haciendo algo de daño."

            "¿Te duele?":
                call p_Help

                if gensex_INotLoveYouNeus:
                    $pl.ch_pts("np",2)

                    ne "Hmmm..."

                    ne "Me alegro de que te preocupes por mí."

                    p "..."

                else:
                    $pl.ch_pts("np",1)

                ne "Solo un poco."

                if night05_elysium_2ndRoundYou_mood == "wild":

                        p "Pensaba que querías que te follara bien duro."

                        ne "..."

                        ne "Y es lo que me gustaría,"

                        ne "pero..."

                        ne "Supongo que tendrá que ser un poco más tarde."

                ne "Realmente la tienes enorme,"

                ne "pero no te preocupes."

            "...":
                call p_Help

                pass

        # Nonlove Variation?

        n "Decides no profundizar más y desplazarte horizontalmente"

        n "en ese pequeño rango de su estrecho sexo."

        ne "Hmmm..." # Femenine pleasure moan with shades of pain.

        #pt "Parece que esto no le disgusta tanto."

        n "A medida que sientes tu polla volviéndose dura en cada nueva incursión"

        if night05_elysium_2ndRoundYou_mood != "wild":

            n "Por sus gemidos deduces que ya no le duele tanto."

        else:

            n "decides agarrar sus nalgas con fuerza."

            ne "¿Hmmm...?"

            p "Tienes un trasero pequeño pero respingón."

            ne "Espero que sea un elogio."

            menu:

                pt "Un elogio..."

                "Por supuesto que es un elogio.":
                    call p_Help
                    $pl.ch_pts("np",1)

                    ne "Me alegra saber eso."

                "<Azotarle la nalga>":
                    call p_Help

                    $ night05_elysium_SmackAss += 1

                    with hpunch
                    ne "¡Auh!" # Ass slapped.

                    ne "¿Y eso a qué ha venido?" # Not angry, but curious and horny.

                    n "Su tono de voz es más de curiosidad que de enfado."

                    menu:

                        pt "No parece molesta..."

                        "<Azotarle la otra nalga>":
                            $pl.ch_pts("np",2)

                            $ night05_elysium_SmackAss += 1

                            with hpunch
                            ne "¡Auch...!"

                            p "¿Responde eso a tu pregunta?"

                            ne "Hmm..."

                            ne "Confieso que no me disgusta esa parte dominante de ti..."

                        "Lo es, porque me encanta.":
                            call p_Help

                            $pl.ch_pts("np",1)

                            ne "Me alegra oír eso."

                        "...":
                            call p_Help

                            ne "..."

                            ne "Al menos podrías decir algo."
 

                "Es solo una observación.":
                    call p_Help

                    ne "..."

                    ne "No sé cómo tomarme eso."

                "...":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    ne "..."

                    ne "Supongo que no..."

        n "A medida que te vas desplazando en su interior,"

        n "percibes su sexo cada vez menos hostil"

        n "y logras profundizar un poco más en cada nueva acometida."

        ne "Hmmm..."

        pt "Me está dejando la polla empapada..."

        n "No solo su coño se va volviendo más cálido,"

        n "sino que su sexo es capaz de engullir casi hasta una cuarta parte de tu enorme miembro."

        pt "Es obvio que cada vez está más dilatada."


#######

    ne "Fóllame más duro..."

    if gensex_ILoveYouNeus:

        p "¿No has dicho que te hiciera el amor?"

        if night05_elysium_2ndRoundYou_mood == "wild" and night05_elysium_2ndRoundYou_pos_Cond == "doggy":

            ne "Has sido tú el que me ha dicho que a cuatro patas no es hacer el amor."

            p "..."

        else:

            ne "*Gnnnn* -Te saca la lengua-"

        ne "Solo un poco más."

    menu:

        pt "¿Lo dice en serio?"

        "¿No te haré daño?":
            call p_Help

            if gensex_INotLoveYouNeus:

                ne "No..."

            ne "No te preocupes por eso."

            ne "Soy más resistente de lo que parezco."

            if night05_elysium_1rstRound_MCDom_stopTimes > 3:

                p "Antes no me has dicho lo mismo."

                ne "Eso es porque me estabas follando en frío."

                ne "No es lo mismo..."

            if gensex_INotLoveYouNeus:
                $pl.ch_pts("np",1)

                ne "Aunque me alegro de que te preocupes tanto por mí."

                p "..."

            p "Como quieras."

        "<Obedecerla>":
            call p_Help
            pass

    n "Profundizas aún más en su interior."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Su mirada muestra una mueca de dolor cuando percibes que"

    else:

        n "Notas un tono de dolor en su voz cuando percibes que"

    n "-a pesar de no haber logrado meter ni la mitad- tocas fondo."

    if not gensex_INotLoveYouNeus:

        p "¿Estás bien?"

    ne "No pares..."

    if gensex_INotLoveYouNeus:

        p "No tenía ninguna intención de hacerlo."

        ne "..."

## 

    n "Presionando con más fuerza tus caderas,"

    n "logras hundirla hasta la mitad."

    ne "Joder..."

    n "Su voz es entrecortada y con clara señal de dolor,"

    ne "Menudo pollón tienes..."

    n "aunque lo intenta disimular."

    if gensex_ILoveYouNeus:

        p "Si te hago daño debería..."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        if gensex_ILoveYouNeus:

            n "Vuelve a besarte mientras sientes que mueve sus caderas para acompañarte en el vaivén."

        else:

            n "Sientes que desplaza sus caderas para acompañarte en el vaivén."

    else:

        n "Sientes sus nalgas desplazándose para acompañarte en el vaivén."

    if not gensex_INotLoveYouNeus:

        ne "No pares..."

###

    if gensex_ILoveYouNeus:

        n "Con suavidad, decides aumentar el ritmo."

    else:

        n "Decides aumentar el ritmo."

    n "Sientes que en lo profundo de su carne, no solo está más caliente,"

    n "sino que además aparecen como pequeñas lenguas"

    n "que acarician tu miembro cada vez que logras chocar contra el muro de su sexo."

    pt "¿Qué demonios...?"

    n "Sientes el cosquilleo particular que te advierte de una corrida."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Neus cruza de nuevo las piernas sobre tus nalgas empujándote hacia ella."

    else:

        n "Yendo a gatas arrastra tu cuerpo hacia atrás"

        with hpunch
        p "Ugh..."

        n "hasta que tu espalda choca contra la dura y fría pared"

        n "y tus nalgas se clavan contra la madera de la cabecera de la cama"

        n "impidiendo que puedas apartarte de ella."

    ne "Dámelo todo..."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Aumentas las embestidas contra su pelvis"

        n "mientras ella sigue agarrándote con fiereza la espalda"

        n "y besándote el pecho con hambre y lujuria."

    else:

        pt "La madre que la..."

        if night05_elysium_SmackAss > 0:

            menu:

                pt "Antes no parece que le haya disgustado..."

                "<Azotarle la nalga>":
                    $ night05_elysium_SmackAss += 1

                    with hpunch
                    ne "¡Auch!"

                    ne "Hmmm..."

                    n "Te mira de reojo con sus brillantes ojos."

                    ne "Me alegra saber que mi trasero te gusta tanto."


                "...":
                    call p_Help


        n "Aumentas el ritmo de tus embestidas contra sus nalgas"

        n "mientras ella sigue agarrándose a la tela de la sábana soportando el peso de tus acometidas."

####

    p "Ughh..."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Siendo incapaz de apartar tus caderas"

        n "por la vigorosa sujeción de sus piernas contra tus nalgas"

    else:

        n "Cuando intentas apartarte ligeramente de ella"

        n "percibes que su coño te absorbe con tanta garra"

        n "que tienes la sensación que sería capaz de arrancártelo de cuajo."

        n "Incapaz de apartarte de ella por el muro que tienes detrás y su inhumanamente absorbente sexo"

    n "percibes esas lenguas interinas no solo aumentando en tamaño y número,"

    n "sino que además empiezan a succionártela como si tuvieran pequeños tentáculos,"

    n "tan sagaces como los de un pulpo"

    n "y ardientes como cera ardiente."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Todo ello sin detener sus piernas y caderas"

        n "para seguir golpeando tu dolorida pelvis contra su ingle."

    else:

        n "Todo ello sin detener sus nalgadas, que siguen impactando contra tu dolorida pelvis"

        n  "mientras la carne de tu trasero está siendo atormentado por la dura y puntiaguda madera de la cabecera."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "En su rostro se dibuja una expresión entre el placer y el dolor"

    else:

        n "En su rostro, te parece ver una expresión entre el placer y el dolor"

    n "a medida que sus ojos brillan con más intensidad."


###
    with hpunch
    with hpunch
    ne "¡Para!"

    n "Esos tentáculos se apartan y sus caderas se detienen en seco."

    p "¿Qué?"

    ne "¡PARA,{w=0.2}{nw}"

    extend " PARA,{w=0.2}{nw}"

    extend " PARA!"

    ne "¡No te muevas!"

    menu:

        pt "¿Ahora me dice que pare?"

        "<Detenerte>":
            call p_Help

            jump night05_elysium_2ndRoundYou_stopBeginning


        "<Desobedecerla y darle caña>":
            call p_Help

            jump night05_elysium_NeusOrgasm

label night05_elysium_2ndRoundYou_stopBeginning:

    n "Detienes tus caderas."

    p "¿Qué ocurre?"

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Sus ojos brillan con intensidad."

    else:

        n "Por el brillo que ves reflejado en la sábana,"

        n "deduces que sus ojos brillan con intensidad."

    n "Su respiración es agitada y su cuerpo tiembla en cortos pero intensos espasmos."

    p "¿Estás a punto de tener un orgasmo?"

    ne "Sí..."

    jump night05_elysium_2ndRoundYou_stopContinue

label night05_elysium_2ndRoundYou_stopContinue:

    ne "Solo..."

    ne "Dame unos segundos..."

    n "Ves que su expresión es tensa y su respiración turbulenta."

    if not gensex_INotLoveYouNeus:

        p "¿Estás bien?"

    else:

        p "Cualquier diría que estás a punto de tener un ataque de ansiedad."

    ne "Ahora no, [protname]."

    ne "Por favor,"

    ne "Ssshh..."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        p "¿Quieres que la saque?"

        ne "¡Ni se te ocurra moverte!"

    n "Decides obedecer y esperar un tiempo prudencial."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        pt "Por lo menos podría apartarse un poco..."

        pt "Esta maldita madera me está dejando el culo hecho mierda."

    n "Tu polla sigue palpitando en su interior"

    n "aunque ya no percibes esas extrañas lenguas en lo profundo de su sexo."

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        n "El ardor de su piel va apaciguándose."

        n "Sus pechos, que hasta ahora apenas te dejaban respirar, disminuyen de tamaño,"

        n "a la par que percibes sus caderas menos pesadas y voluminosas."

        n "Al mismo tiempo que todo su cuerpo se va encogiendo,"

        n "padeces tu polla siendo aplastada por el encogimiento de su sexo."

        n "Entre gruñidos de dolor y agarrándose a tus hombros"

        n "se la va desenterrando hasta que apenas queda solo la punta."

        n "Su rostro, que vuelve a ser el de antes, se va serenando"

        n "mientras el brillo en sus ojos se va apaciguando."

    else:

        if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

            n "Su rostro se va serenando y el brillo de sus ojos se va apaciguando."

        else:

            n "Gracias al reflejo de la sábana, descubres que el brillo de sus ojos se va apaciguando."

    ne "Dios..."

    ne "Esto es más difícil de lo que me imaginaba."

    ne "Tu polla me vuelve loca."

    p "¿Quieres cambiar de posición?"

    ne "No..."

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        if gensex_ILoveYouNeus:

            ne "Me encanta poder abrazarte mientras te hago el amor."

            n "Acariciándote la mejilla para que mires hacia ella,"

            n "recibes un dulce beso en tus labios."

        else:

            n "Me gusta poder mirarte a la cara mientras salto encima de ti."

    elif night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        if gensex_ILoveYouNeus:

            ne "Me encanta poder abrazarte mientras me haces el amor."

            n "Forzándote a bajar el cuello, recibes un dulce beso en tus labios."

        else:

            ne "Me gusta poder mirarte a la cara mientras me follas."

    else:

        if gensex_ILoveYouNeus:

            ne "Aunque me gustaría verte la cara y poder besarte,"

        else:

            ne "Aunque me gustaría poder verte la cara mientras me follas,"

        ne "En esta postura no me duele tanto."

        ne "Además,"

        ne "así no tienes que ver las extrañas muecas que hago."

        menu: 

            pt "¿Extrañas muecas?"

            "En realidad, sería interesante poder verte la cara.":

                ne "No sé cómo tomarme eso."

                p "Tómatelo cómo prefieras."

                ne "Hmm..."

            "En realidad me encantaría poder verlas.":
                call p_Help

                $pl.ch_pts("np",1)

                ne "..."

                if gensex_ILoveYouNeus:

                    ne "No-"

                    extend "no me digas estas cosas..."

                    pt "¿Tanto le molesta?"

                else:

                    ne "Me alegra oírte decir eso."

            "Sí, debe de ser horrible verte así." if gensex_INotLoveYouNeus:

                $pl.ch_pts("np",-2)

                ne "..."

                ne "Tampoco hace falta que seas de esta manera..."

            "Sí, debe de ser horrible verte así. (Con tono de broma)" if not gensex_INotLoveYouNeus:
                call p_Help

                $pl.ch_pts("np",2)

                ne "¡Oye!"

                p "No seas tonta,"

                p "ya sabes que me encantaría."

                ne "*Gnnn*"

                n "Te parece ver una dulce sonrisa en su rostro."

                ne "Tontín."

                p "Encima..."

                ne "En realidad,"

                ne "me encanta que seas de este modo."

                p "..."

                ne "¿Ves?"

                ne "Ahora eres tú quien está sonrojándose."

                p "Psst..."

                ne "*risilla inocente*"

            "...":
                call p_Help
                pass

    ne "Estás a punto de correrte,"

    ne "¿verdad?"

    p "Sí..."

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        return

    ne "Entonces dame bien duro."

    if gensex_ILoveYouNeus:

        p "¿Estás segura?"

        if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

            p "No parece que lo estés disfrutando demasiado."

            ne "Ohh..."

            ne "Te aseguro que lo estoy gozando más de lo que te imaginas."

        else:

            ne "Sí."

            if  night05_elysium_2ndRoundYou_mood != "wild":

                ne "Me encanta que me hagas el amor a cuatro patas"

            else:

                ne "Me encanta que me folles a cuatro patas"

            ne "y necesito sentirla dentro de mí."

        p "Pero tengo la sensación que te estoy haciendo daño."

        ne "Sí..."

        ne "Quizás un poco."

        ne "Pero por favor,"

        ne "no te retengas."

        p "..."

        ne "Confía en mí."

        p "..."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Apartas tus caderas hasta casi sacarla y vuelves a metérsela de golpe."

    else:

        n "Dejándote algo más de espacio, logras apartar ligeramente tus caderas"

        n "para luego volver a metérsela de golpe."

    with hpunch
    ne "¡NNGhnnn...!"

    if gensex_ILoveYouNeus:

        p "¿Neus?"

        ne "No..."

        ne "¡No pares!"

    if night05_elysium_SmackAss > 0:

        with hpunch
        ne "¡Auch!"

        n "Vuelves a azotarle las nalgas."

        p "En el fondo sé que te encanta."

        ne "Hmm..."

        ne "Es posible."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Aumentas el ritmo de tus embestidas con intención de chocar contra su pelvis"

    else:

        n "Aumentas el ritmo de tus embestidas con intención de chocar contra sus nalgas"

    n "aunque apenas logras hundir la mitad en su interior."

    if gensex_ILoveYouNeus:

        pt "Tengo que estar haciéndole daño..."

    n "Vuelves a sentir ese cosquilleo en tus piernas."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Los pies de Neus vuelven a cruzarse sobre tus nalgas."

    else:

        n "Percibes que desplaza sus caderas para intentar metérsela más adentro."

    ne "¡Más duro!"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy" and night05_elysium_2ndRoundYou_mood == "wild":    

        p "Al final te voy a reventar."

        ne "¡A ver si es verdad!"

    if night05_elysium_SmackAss > 0:

        with hpunch
        ne "¡Hmmm...!"

        ne "¡No pares!"

    n "En cada nueva embestida logras llevar algo más lejos tu miembro,"

    n "pero eso no evita que oigas un tenue tono de dolor en sus gemidos."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Ves que empieza a emerger el brillo en sus ojos."

    else:

        n "Descubres por el reflejo de la sábana que empieza a emerger el brillo en sus ojos."

    n "Percibes ese montón de lenguas en lo profundo de su sexo"

    n "acariciando y succionando tu miembro sin compasión."

    $ night05_elysium_MCCumshots += 1

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":
        with vpunch
        with vpunch
    else:
        with hpunch
        with hpunch
    p "¡Uuuhhg!"

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "Te abraza con extremo vigor."

        n "Sufres sus uñas clavándose en tu espalda y su mejilla sobre tu pecho"

        n "mientras con sus -inhumanamente sólidas- piernas te sujeta las nalgas"

        n "para presionar tus caderas contra su pelvis"

    elif night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Agarrándose con fuerza a la sábanas empuja sus caderas hacia atrás"

        n "forzándote a retroceder y clavarte de nuevo esa maldita madera en tus nalgas"

        n "al mismo tiempo que sientes de nuevo la fría pared en tu espalda"

        n "mientras sigue empujando hacia atrás con energía"

        n "con la intención de sumergir unos centímetros más tu enorme y bombeante miembro"

        n "sin que puedas hacer nada para evitarlo"

    else: # If She Rides you /// in doggyStyle Is that a thing?

        n "Posando sus pies y manos sobre la almohada -como si estuviera poseída-"

        n "te empuja hacia atrás -sin quitarse la polla- con tanta fuerza"

        n "que logra desplazar tu cuerpo entero hacia atrás hasta que tu espalda choca contra el muro"

        n "que está en contacto con el cabecero de la cama"

        n "desplazando sus nalgas para seguir bombeándote"

        n "sin que puedas hacer nada para evitarlo"

    n "al mismo tiempo que sientes el interior de su sexo removiendo tu polla."

    p "Uuuuhh..."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "A pesar de que que casi te rompe la espalda"

    else: #doggy and sheRidesYou

        n "A pesar de que casi te rompe la cadera"

    n "y de que tienes la sensación de que tus pelotas están más vacías que un aseo de pago en el barrio de  {a=https://es.wikipedia.org/wiki/La_Mina}la mina{/a},"

    n "su sexo te succiona con un impulso tan atroz"

    n "que de seguir así estás convencido de que te arrancará la polla de cuajo."

    n "Sus caderas desaceleran al igual que su coño baja de temperatura"

    n "hasta que finalmente apenas percibes alguna que otra de esas extrañas lenguas"

    n "acariciando el orificio de tu glande para arañar una última gota."

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "La fuerza con la que te arañaba la espalda se suaviza y te agarra con un dulce abrazo."

    else:

        n "Sin quitarse tu polla de su interior y poniéndose de pie sobre la alcoba,"

        n "reposa su cálida y húmeda espalda en tus abdominales y su cabeza contra tu pecho."

    n "Te relajas tanto,"

    scene black
    with fade

    if night05_elysium_2ndRoundYou_pos_Cond == "missionary":

        n "que terminas dejándote caer sobre su desnudo cuerpo como un peso muerto."

    else:

        n "que terminas reposando tu desnuda espalda contra la fría pared."

    pause

    jump night05_elysium_3rdRoundBeginning

###    ###    ###   ###

label night05_elysium_3rdRoundBeginning:

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        jump night05_elysium_3rdRoundBeginning_doggy

    else:
        jump night05_elysium_3rdRoundBeginning_missionary

        ## Also included if you rided her. 

########################################################################
################################################
########################################################################

label night05_elysium_3rdRoundBeginning_doggy:

    with vpunch
    ono "pug{w=0.1}{nw}"

    p "Uhh..."

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "Sientes tu cuerpo algo más pesado y cansado."

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "Te da la sensación que te has quedado medio dormido estando de pie sobre la cama"

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "y reposando la espalda contra el muro."

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "Paulatinamente, sigue moviendo sus caderas"

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "manteniendo casi la mitad de tu fofa folla en su interior"

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "como si intentara reanimarla con el movimiento de sus caderas."

    scene day05
    with fade

    n "Mirándote de espaldas con una sonrisa pícara."

    ne "Veo que has regresado al mundo de los vivos."

    p "¿Es que no has tenido suficiente con dos?"

    ne "Por supuesto que no."

    ne "Estoy segura que aún puedes darme otra abundante y rica corrida."

    n "El trasero te duele tanto por las concavidades de la madera de la cama"

    n "que apenas tienes sensibilidad en él."

    n "Intentas reincorporarte,"

    with vpunch
    ono "pug{w=0.1}{nw}"

    n "pero el férreo agarre de su sexo en tu polla te lo impide."

    n "Tienes la sensación de que tienes la piel de tu polla en carne viva"

    n "y cada vez que sus caderas se alejan puedes comprobar lo rojiza que está."

    n "Intentas mover tus caderas para acompañarla en el vaivén."

    ne "Sí..."

    ne "Fóllame, [protname]."

    pt "Dios..."

    n "Te presiona con tanta fuerza contra el muro que apenas puedes moverte."

    n "Intentas agarrarla de los hombros para tirarla sobre la cama"

    n "pero su fuerza inhumana te lo impide."

    ne "Antes me has follado como una perra,"

    ne "ahora es mi turno."

    menu:

        pt "¿Su turno?"

        "¿Podríamos hacerlo contra otra superficie? El culo me está doliendo una barbaridad.":

            if night05_elysium_2ndRoundYou_mood == "wild":

                ne "Antes me has dicho que no querías hacerlo de modo romántico."

                p "¡Una cosa es hacerlo de forma cursi y la otra es que me rompas los huesos de la cadera!"

            ne "..."

            ne "Supongo que tienes razón."

            $ night05_elysium_3rdRoundYou_wood = "out"

            call night05_elysium_3rdRoundYou_woodLabel

        "¿Acaso me vas a violar?" if gensex_INotLoveYouNeus:
            call p_Help

            $pl.ch_pts("np",-1)

            ne "..."

            ne "Estoy demasiado cachonda para tomarme en serio la estupidez que acabas de decirme."

            p "Yo no opino que sea una estupidez."

            ne "¿Acaso no lo has gozado tanto que has terminado corriéndote follándome a cuatro patas?"

            menu:

                "Eso es porque no te tenía que mirar a la cara.":
                    $pl.ch_pts("np",-3)

                    ne "..."

        "¿Es que piensas meterme algo por detrás?":
            call p_Help

            if gensex_INotLoveYouNeus:

                ne "¡Por supuesto que no!"

            else:

                ne "Claro que no."

        "Antes has dicho que yo tenía el control":
            call p_Help

            ne "Y ya lo has tenido..."

            ne "Pero ahora me apetece tenerlo yo."

            if gensex_INotLoveYouNeus:

                $pl.ch_pts("np",-1)

                p "Ya veo lo que te importa mi opinión."

                ne "..."

        "Podrías ser algo más romántica." if not gensex_INotLoveYouNeus:

            ne "..."

            if night05_elysium_2ndRoundYou_mood == "wild":

                ne "No es lo que me has pedido antes..."

                p "Pero tampoco te he pedido esto."

                ne "Hmm..."

            ne "Después de haberte corrido follándome a cuatro patas,"

            ne "estoy demasiado cachonda para eso..."

        "Fóllame como si fuera tu juguete sexual." if not gensex_INotLoveYouNeus:

            ne "..."

            ne "Con que esas tenemos..."

            ne "Espero que no te arrepientas de tus palabras."

            p "..."

    jump night05_elysium_3rdRoundAgainstWall

label night05_elysium_3rdRoundYou_woodLabel:

    # She can be big or small... First option she is small.

    ## $ night05_elysium_3rdRoundYou_wood = "OutSmall"
    ## $ night05_elysium_NeusBody = "small"

    n "Se aparta sugerentemente de tu espalda"

    n "mientras sustrae paulatinamente tu erecto y palpitante miembro de su interior."

    ne "La tienes bien dura..."

    pt "¡Y rojiza!"

    with vpunch
    p "¿Uh?"

    n "Sujetándote de la espalda y las piernas como si fueras una doncella en peligro"

    n "te lleva hasta la pared más próxima y te arroja a ella sin demasiada suavidad."

    with hpunch
    p "¡Ugh!"

    n "Percibes el frío de esa nueva pared en tu espalda y trasero."

    n "Sin darte tiempo a reaccionar, vuelve a meterse tu miembro."

    return

label night05_elysium_3rdRoundAgainstWall:

    ne "Como veo que te gusta tanto mi trasero,"

    ne "te follaré de espaldas."

    n "Percibes su cálida vagina aumentar de temperatura."

    pt "¿Qué narices...?"

    n "Te da la sensación de que su cabeza,"

    n "que hasta ahora estaba a la altura de tu pecho,"

    n "la tienes cada vez más cerca de tu rostro."

    n "El volumen de sus nalgas aumentan de tamaño,"

    n "su cuerpo se va alargando hasta el punto que ya no necesita estar de puntillas"

    n "para seguir embistiéndote con sus caderas."

    pt "¡¿Está creciendo?!"

    $ night05_elysium_NeusBody = "big"

    n "Contornea su cabeza para darte un profundo beso con lengua, mucho más ardiente que antes."

    n "Al fijarte en ella ves que su rostro es más estilizado y maduro."

    p "¡Auch!"

    p "¿Me hags mogdido la lengua?"

    ne "Solo un poquito."

    n "Percibes el sabor de tu propia sangre en dónde le ha hincado el diente."

    p "¿No me has dicho que no podía sangrar?"

    ne "No fuera de esta habitación"

    ne "y mucho menos sin que yo no sepa dónde."

    p "Pero..."

    n "Vuelve a besarte con fervor y pasión"

    n "absorbiendo el resto de tu saliva y sangre"

    n "al mismo tiempo que relame esa herida en tu lengua."

    n "Al apartarse te mirarte con esos ojazos -ligeramente brillantes- de gata en celo."

    ne "Ya no te duele,"

    ne "¿verdad?"

    n "Pasas tu lengua por tus dientes para comprobar dónde está la herida,"

    n "pero tienes la sensación que ha desaparecido por completo."

    ne "No te preocupes [protname],"

    ne "sé lo que me hago."

    n "Sientes sus caderas desplazándose a mayor ritmo mientras te vuelve a besar con intensidad."

    n "En cada nueva acometida su coño logra tragarse unos centímetros más de tu miembro"

    ne "Hmmm..."

    n "hasta que finalmente sientes sus esponjosas nalgas acariciando la sensible piel de tu ingle."

    p "¡Dios!"

    n "Sus gemidos son cada vez más agudos e intensos."

    n "No solo consigue enterrar toda tu polla en su interior"

    n "sino que además termina aplastando sus nalgas contra tu pelvis"

    n "asegurándose en cada embestida tenerla lo más al fondo posible."

    p "Fóllame, [protname]"

    n "Paulatinamente, desplaza a mayor velocidad sus caderas en tu rojizo y palpitante pollón"

    if night05_elysium_3rdRoundYou_wood != "out":

        n "a la par que tus nalgas están siendo martirizadas por la dura madera de la cama."

    else:

        n "a la par que tus nalgas impactan contra esa dura pared."

    menu:

        pt "¿Que la folle?"

        "¡Pero si eres tú quien me está follando!":
            call p_Help

            ne "Hmmm..."

            ne "Es posible."

            n "Una dulce y maliciosa sonrisa se dibuja en sus labios."

            if gensex_INotLoveYouNeus:

                p "A mi no me hace gracia."

                ne "Entonces sonríe un poco más."

            pt "La madre que la..."

        "...":
            call p_Help

            pass

    n "Su ritmo es tan acelerado y feroz que ya ni siquiera te mantienes de de pi por ti mismo"

    n "y apenas te sientes las piernas."

    menu:

        pt "Mi culo..."

        "El trasero me está doliendo un montón..." if night05_elysium_3rdRoundYou_wood != "out":
            call p_Help

            ne "Oh..."

            ne "Estoy segura que un hombretón como tú podrá aguantar un poco más."

            menu:

                pt "¿Se piensa que soy de goma?"

                "Te lo digo en serio.":

                    ne "..."

                    ne "¿Y por qué no me lo has dicho antes?"

                    p "Porque no quería arruinar el momento,"

                    p "pero de verdad que me está doliendo."

                    ne "..."

                    $ night05_elysium_3rdRoundYou_wood = "out"

                    call night05_elysium_3rdRoundYou_woodLabel

                "<No decir nada>":
                    call p_Help
                    pass

        "<No decir nada>":
            call p_Help
            pass

    n "Ves en su mirada -de gata en celo- esos brillantes ojos."

    n "Vuelve a besarte con pasión a la vez que sigue aumentando el ritmo de sus acometidas."

    n "Te embiste con tanta brutalidad"

    if night05_elysium_3rdRoundYou_wood != "out":

        n "que tienes la sensación de que la madera con la que impactas con tu lastimado trasero"

        n "no tardará en desquebrajarse."

    else:

        n "que tienes la sensación que perforarás el muro contra el que impactas con tu trasero."

    n "Tu ingle está quedándose completamente rojiza por las hostias que recibes de sus nalgas"

    if night05_elysium_3rdRoundYou_wood != "out":

        n "y toda la cama tiembla de tal modo que sientes que pronto terminará partiéndose en dos."

    else:

        n "y a pesar de que tu culo ya no se clava en ninguna madera,"

        n "sigues siendo aplastado salvajemente contra esa dura pared."

    n "Aparta rápidamente sus labios."

    ne "Aaahh-aaaahh... ahhhhh... *Agudos gemidos*"

    pause

    jump night05_elysium_3rdRoundStop
        # n "Se detiene de golpe reposando sus ardientes nalgas sobre tu cadera"
        # n "-aunque tu culo sigue sin tocar la sábana- con la mirada cabizbaja."
        # ne "*Largo suspiros* Aaahh... Ahhh..."

########################################################################
################################################
########################################################################


label night05_elysium_3rdRoundBeginning_missionary:

    p "Uh..."

    n "Sientes su respiración por tu pecho,"

    n "tu polla algo más flácida aún en su cálido interior,"

    n "y sus labios besándote dulcemente por toda la piel que encuentra delante."

    p "¿Neus?"

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        pass

    else:

        n "Posa sus manos en tus pectorales y con una sorprendente fuerza te aparta suavemente."

    n "Aleja su cadera de tu entrepierna, liberándote de su estrecho y cálido sexo"

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        n "para ascender por tu sudoroso cuerpo hasta alcanzar a mirarte directamente a los ojos"

        n "con su rostro no tan maduro y estilizado."

    else:

        n "para luego tumbarte, posar tu espalda sobre la sábana y ponerse ella encima de ti."

    if gensex_ILoveYouNeus:

        n "Acerca sus labios a los tuyos para robarte un apasionado y longevo beso."

    else:

        n "Sientes sus labios besándote con dulzura."

    n "Su lengua corretea por tu mejilla, tu cuello, tus pechos, tus abdominales"

    n "y sin demasiada demora alcanza tu ingle dónde reposa tu polla,"

    n "bastante más flácida y rojiza."

    n "Sientes su respiración cerca de tus testículos."

    n "Al fijarte en ella ves que sus ojos siguen estando ligeramente iluminados."

    n "Sus labios siguen acariciando tu piel, pero esta vez"

    n "sientes que te succiona tu bolsa escrotal al mismo tiempo que..."

    p "¡Auh!"

    n "Sin decirte nada, te dedica una mirada maliciosa y juguetona."

    p "¿Por qué te gusta tanto morder?"

    ne "Quizás es que tengo algo de vampiresa..."

    p "..."

    ne "*risilla aparentemente inocente*"

    n "Desliza sus labios y su lengua por tu flácido y rojizo miembro"

    n "hasta alcanzar la cima, a la cual le dedica un cariño extra."

    n "Con una mano te acaricia tus testículos."

    n "y con la otra te sujeta con firmeza la base de tu enorme -pero fofa y blanda- polla."

    n "Sin prisas, acerca de nuevo su lengua a la cima de tu polla"

    n "para sostenerla solamente con sus labios,"

    n "y acto seguido la entierra en su garganta."

    p "Uuughh..."

    ne "Hmm..."

    p "Neus..."

    ne "¿Zig...?"

    n "Te responde sin quitársela de la boca"

    p "Ya llevo dos..."

    n "Se la desentierra para luego darle un ardiente lametón en la punta."

    ne "Pero estoy segura que aún puedes aguantar una tercera."

    ne "A pesar de lo rojiza que está,"

    ne "parece que vuelve a animarse..."

    ne "¿No es así?"

    ne "Hombretón."

    p "Me has dejado la polla bastante hecha mierda."

    ne "Exagerado..."

    n "Sin mediar palabra, vuelve a metérsela en su ardiente boca."

    n "A pesar de que no logra tragarse más de la mitad,"

    n "su longeva lengua desciende por tu sensible piel posterior hasta alcanzar tu bolsa escrotal"

    n "dónde acaricia te acaricia con su húmeda y ardiente superficie"

    n "sin que sus cabezadas se detengan en ningún momento."

    n "Ves su rostro hundiéndose cada vez a más velocidad"

    n "mientras notas que tu riego sanguíneo vuelve a tu entrepierna."

    n "Se detiene para luego desenterrarla sugerentemente de su boca"

    n "mientras te dedica una mirada maliciosa y juguetona."

    ne "¿Lo ves?"

    n "Sin dejar de usar su lengua a lo largo de tu sensible miembro."

    p "Hmm..."

    n "Haces el gesto para reincorporarte y ponerte de rodillas..."

    n "Su mano te empuja y te tumba de nuevo sobre la cama."

    ne "No,"

    extend " no..."

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        ne "Antes de me has dado el control,"

        ne "así que asume la consecuencia de tus decisiones."

    else:

        ne "Ahora es mi turno."

    p "Pero..."

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        if gensex_ILoveYouNeus:

            ne "Me ha encantado hacerte el amor."

        else:

            ne "Me ha encantado tenerte bajo mi control."

            ne "Así que seguiré igual."

    else:

        if gensex_ILoveYouNeus:

            ne "Me ha encantado cómo me has hecho el amor,"

        else:

            ne "Me ha encantado que me follaras cara a cara,"

        ne "pero creo que ha sido algo peligroso..."

        ne "Otra vez he estado a punto de tener un orgasmo."

        if not gensex_INotLoveYouNeus:

            pt "¡Pero si al final es ella la que se estaba moviendo!"

        else:

            p "¡Pero si eres tú quien se estaba moviendo al final!"

            ne "..."

            ne "Es posible,"

            ne "pero eso no quita que sigue siendo peligroso."

            ne "Al fin y al cabo,"

            ne "soy yo quien conoce mejor mi cuerpo"

            ne "y las consecuencias de lo que puede ocurrir si..."

            ne "..."

            n "Un largo suspiro surge de sus labios."

    ne "Por favor,"

    if night05_elysium_2ndRoundYou_pos_Cond == "NeusRides":

        ne "descansa y déjame a mí de nuevo."

    else:

        ne "descansa y déjame a mí ahora."

    if gensex_ILoveYouNeus:

        n "Se acerca a tus labios y te da un dulce y apasionado beso con lengua."

    else:

        n "Se acerca a tus labios y te da un dulce beso."

    ne "Me pasaría el día besándote."

    if gensex_INotLoveYouNeus:

        p "Y haciendo lo que te da la gana en general, por lo que estoy viendo."

        ne "..." # Face of few friends

    n "Usa sus muslos para juguetear con tu húmedo y caliente miembro"

    n "mientras prosigue besándote dulcemente por la mejilla, luego el cuello, el pecho,"

    n "hasta que su entrepierna alcanza tu manubrio"

    n "y arrimando sus labios vaginales a esa sensible y rojiza piel,"

    n "vuelve a ascender despegando su busto de tu pecho hasta alcanzar la cima rosada."

    n "Descendiendo ligeramente sus caderas,"

    n "vuelve a engullir el glande con su estrecho y ardiente sexo."

    ne "Hmmm..."

    n "Sigue descendiendo sus caderas hasta lograr enterrar la mitad de tu miembro en su interior."

    ne "Me encanta..."

    n "Una vez de rodillas, vuelve acercar su modesto pecho contra tu desnudo cuerpo."

    p "Auh..."

    p "¿Por qué te gusta tanto pellizcarme?"

    ne "*risilla inocente*"

    n "No solo su interior se vuelve más abrasador,"

    ne "Tampoco te pellizco tan fuerte."

    n "percibes todo su cuerpo más caliente."

    n "Tienes la sensación que sus manos -que están masajeando tus pechos-"

    n "son algo más grandes que hace apenas unos segundos."

    n "Sientes su labios besándote por el pecho, luego por el cuello, y finalmente en los labios"

    n "sin haberse apartado su sexo de tu polla."

    p "¿Cómo...?"

    n "Al fijarte en ella, descubres un rostro más estilizado, como si fuera más maduro y adulto."

    n "En su cráneo te parece ver dos extrañas protuberancias."

    p "Neus..."

    n "Percibes su coño bastante más ardiente que antes."

    p "¿Qué...?"


    if gensex_ILoveYouNeus:

        n "Silencia tus palabras con un profundo beso de torniquete."

        n "Su lengua, más calcinante que antes, se remueve alrededor de la tuya."

    else:

        n "Posa el dedo índice en tus labios."

        ne "Shhh..."

        n "Para luego acercar sus labios a tu mejilla derecha."

    n "Sientes el calor de sus pechos sobre tu busto,"

    n "algo más calientes que antes, pero sobretodo mucho más voluminosos."

    n "Sus caderas -las cuales percibes mucho más pesadas-"

    n "empiezan a desplazarse para intentar tragarse aún más tu sensible -pero erecto- miembro."

    if gensex_ILoveYouNeus:

        n "Sin apartarse de tu boca,"

    else:

        n "Sin apartar su rostro,"

    n "te agarra una mano y se la acerca a uno de sus pechos."

    n "Tan enorme que simplemente no te cabe en la mano."

    if afternoon04_MACBA_TxellName_Know:

        pt "¡Pero si son casi tan grande como los de Meritxell!"

    else:

        pt "¡Pero si son casi tan grande como los de la rubia tetuda!"

    if gensex_ILoveYouNeus:

        n "Finalmente te permite respirar y al apartarse,"

    else:

        n "Finalmente aparta sus labios de tu mejilla y al hacerlo,"

    n "no solo ves ese rostro más estilizado,"

    n "sino también ese intenso brillo en sus ojos."

    if gensex_ILoveYouNeus:

        ne "Te amo tanto..."

    else:

        ne "Te deseo tanto..."

    if gensex_INotLoveYouNeus:

        p "Habla por ti."

        ne "..."

    n "Te agarra de los tobillos y con un rápido movimiento te levanta las piernas"

    n "mientras se pone de rodillas ante ti con su nueva estatura -mayor incluso que la tuya-."

    n "Su cuerpo es más voluminoso, sus pechos prominentes y su rostro bastante más adulto."

    n "Agarra tu polla con su enorme mano y flexionando ligeramente sus rodillas se la vuelve a introducir."

    n "Sin que tu trasero logre tocar la sábana,"

    n "sientes el calor y el peso de sus nalgas sobre la parte anterior de tus piernas a medida que va descendiendo."

    n "hasta lograr enterrarlo por completo en su interior sin excesiva dificultad"

    n "mientras tus piernas están tan apretujadas contra tu pecho que apenas te permite respirar."

    n "Recuperando un poco el aire cuando asciende"

    n "pero sin apenas darte tiempo, vuelve a descender dejándote a media respiración."

    if gensex_INotLoveYouNeus:

        p "¡Si tenemos que hacerlo preferiría tener yo el control!"

        n "Desciende su cuerpo hasta tener su rostro ante el tuyo."

        ne "Hmmm..."

        ne "Estás más guapo calladito."

    n "Agarrándote a la sábana como puedes resistes las duras embestidas que te da cada vez que desciende su cuerpo,"

    n "como si fueras un columpio al que tuviera que saltar encima."

    n "Sientes sus uñas clavándose en tus tobillos, su sexo ardiendo,"

    n "esas extrañas lenguas surgiendo de nuevo en lo profundo de su interior pegándose a tu miembro,"

    n "y en su rostro una expresión de lujuria absoluta"

    n "dónde sus brillantes ojos solo se fijan en tu polla"

    n "que sigue desapareciendo a velocidad de flashes de discoteca en su interior."

    n "Sus embestidas son tan duras y rápidas que apenas eres capaz de hacer nada."

    n "Su brillo ocular es cada vez más intenso."

    n "A la par que te está dejando la polla hecha mierda y sus gritos de placer te están dejando sordo,"

    n "percibes el cosquilleo que precede al orgasmo."

label night05_elysium_3rdRoundStop:

    n "Se detiene de golpe reposando sus ardientes nalgas sobre tu cadera"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy": # She's riding you.

        n "-aunque tus pies apenas logran tocar la sábana- con la mirada cabizbaja."

    elif night05_elysium_3rdRoundYou_wood == "out": # You're against the wall.

        n "-aunque tus pies apenas logran tocar el suelo- con la mirada cabizbaja."

    else: # You're against the wall with your feet on the bed.

        n "-aunque tu culo sigue sin tocar la sábana- con la mirada cabizbaja."

    ne "*Largo suspiros* Aaahh... Ahhh..."

    with vpunch
    ne "¡JODER!"

    p "..."

    ne "Joder..."

    n "El ardor de su cuerpo y sexo bajan ligeramente de temperatura."

    ne "Lo siento..."

    n "El tamaño de su cuerpo va reduciéndose."

    ne "Necesito..."

    n "El brillo en sus ojos es algo más leve."

    n "No puedo..."

    n "Una forzada sonrisa se dibuja en sus labios."

    ne "Se siente demasiado bien..."

    if night05_elysium_3rdRoundYou_wood == "out":

        n "Finalmente logras reposar tus pies sobre el frío suelo"

    elif night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Finalmente logras reposar tus pies sobre la almohada"

    else:

        n "Suelta tus piernas, las cuales caen por su propio peso sobre la almohada"

    n "y sin quitársela de su interior"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "apoya su más reducida desnuda espalda sobre tu torso."

    else:

        n "apoya su más reducido desnudo cuerpo sobre el tuyo."

    ne "Lo lamento..."

    p "¿Por qué?"

    ne "He malgastado energía usando ese cuerpo"

    ne "y ni siquiera he logrado que tuvieras otro orgasmo..."

    ne "Soy una inútil."

    menu:

        pt "Malgastado su energía..."

        "Eso no es verdad.":
            call p_Help

            ne "Hmm..."

        "No creo que sea buena idea que malgastes la energía de esa manera.":
            call p_Help

            ne "..."

            ne "Tienes razón."

        "Quizás algo inútil sí eres." if not gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np",-2)

            ne "..."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Te parece ver una lágrima deslizándose por su mejilla."

    else:

        n "Sientes la humedad de una lágrima en la mejilla que está en contacto con la piel de tu pecho."


    menu:
        pt "¿Qué le digo ahora?"

        "¿Podríamos darnos algo más de prisa?" if not gensex_ILoveYouNeus:
            call p_Help

            $pl.ch_pts("np",-2)

            $ night05_elysium_3rdRound_bigBodyOpinion = "dontCare"

            ne "..."

            ne "Sí..."

            ne "Tienes razón."

        "La verdad es que se te veía preciosa con esa figura tan adulta.":
            call p_Help

            $ night05_elysium_3rdRound_bigBodyOpinion = "like"

            ne "..."

            ne "Gracias."

            ne "Supongo..."

        "La verdad es que te prefiero con esa figura tan adulta.":
            call p_Help

            $ night05_elysium_3rdRound_bigBodyOpinion = "favorite"

            $pl.ch_pts("np",-1)

            ne "..."

            ne "Ya,"

            ne "me lo imagino..."

        "Me gustas más cuando tienes esta estatura tan pequeña.":

            $ night05_elysium_3rdRound_bigBodyOpinion = "smallBetter"

            ne "..."

            if night05_Plaza_NeusLooking_Body_MiniSkirt_loliLike:

                ne "Por lo que me dijiste al principio de esta cita,"

                ne "quizás te pondría más si vistiera de colegiala,"

                ne "¿no?"

                p "..."

            ne "Al final pensaré que tienes un problema..."

        "Te amo en todas y cada una de tus formas, Neus." if gensex_ILoveYouNeus:
            call p_Help

            $ night05_elysium_3rdRound_bigBodyOpinion = "loveAnyway"

            $pl.ch_pts("np",1)

            ne "..."

            p "No tengas duda de ello."

            n "Con su mirada algo más apagada, te observa con sus húmedos ojos y una sonrisa algo forzada."

            ne "¿Por qué eres tan dulce conmigo?"

        "...":
            call p_Help
            $pl.ch_pts("np",-1)

            $ night05_elysium_3rdRound_bigBodyOpinion = "silence"

            ne "..."

    if night05_elysium_3rdRound_bigBodyOpinion in ["like", "smallBetter", "loveAnyway"]:

        n "Retirando la polla de su interior se pone de puntillas te obliga a bajar la cabeza"

        n "y te da un dulce beso en los labios."

        if night05_elysium_3rdRound_bigBodyOpinion == "loveAnyway":

            ne "No te merezco."

            p "No digas tonterías."

            ne "*Gnnn*"

        else:

            ne "Aunque no te lo creas,"

            ne "agradezco tus palabras."

    p "..."

    ne "Uhhmm..."

    ne "Creo que ya estoy algo más relajada..."

    n "Percibes su cálida mano acariciando tu erecto miembro."

    ne "Realmente es hermosa."

    p "Y está bien dura."

    ne "Sí,"

    extend " eso también."

    menu:

        pt "No tengo muy claro si me prefiere a mí o a mi polla..."

        "Para que luego digas que no me gustas tal y cómo estás." if night05_elysium_3rdRound_bigBodyOpinion in ["smallBetter", "loveAnyway"]:
            call p_Help
            $pl.ch_pts("np",1)

            ne "..."

        "Me pregunto por qué está así de dura si ni siquiera te estás moviendo.":
            call p_Help

            ne "Bueno..."

        "Seguro que es por algún sucio truco." if not gensex_ILoveYouNeus:
            $pl.ch_pts("np",-2)

            $ night05_elysium_3rdRound_bigBodyOpinion = "dirtyTrick"

            $ gensex_YoureAMonster = True

            ne "..."

            ne "¡No es ningún sucio truco!"
    
    ne "En realidad eso es debido a mis jugos vaginales,"

    ne "que actúan como afrodisíaco para que tu cuerpo esté más caliente"

    ne "y tu sangre más activa de lo normal."

    if night05_elysium_3rdRound_bigBodyOpinion == "dirtyTrick":

        p "Lo que decía."

        ne "..."

        ne "Lo que tú digas."

    elif night05_elysium_3rdRound_bigBodyOpinion in ["smallBetter", "loveAnyway"]:

        ne "No creo que tenga nada que ver con lo atractiva que te parezca..."

        p "Te aseguro que estaría igual dura aunque no fuera por eso, y lo sabes."

        if night05_elysium_MCCumshots == 2:

            ne "¿Después de que ya te hayas corrido dos veces?"

        else:

            aj "¿How many cums did you got? ERROR 69896"

        p "¡Y hasta tres!"

        ne "Viendo cómo la tienes ahora,"

        ne "me gustará comprobar cómo esta después de tu tercera corrida."

        menu:

            pt "Mi límite suelen ser tres..."

            "Quizás la tengo así de mal porque estás tan caliente que me la estás quemando.":
                call p_Help

                ne "Sí..."

                ne "Eso también es cierto."

                pt "Y encima se ríe."

            "...":
                call p_Help

        ne "Aunque sé que no es verdad,"

        ne "agradezco tus palabras, tontín."

        pt "Y ahora me insulta..."

    if gensex_ILoveYouNeus:

        if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

            n "Se pone de puntillas para luego sujetarte de las mejillas y darte un dulce beso."

        else:

            n "Se acerca para darte otro dulce beso."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Vuelve a darte la espalda para luego posar tu enorme falo sobre sus nalgas."

        n "Con un movimiento sutil las desliza para intentar masturbarte con ellas."

        ne "Hmmm..."

        n "Tu polla vuelve a erigirse con fuerza y palpita con energía."

        ne "Es tan enorme..."

        n "Aleja sus nalgas de tu pelvis y acerca el orificio de su sexo a la punta de tu miembro."

    else:

        n "Desciende de nuevo y usando la cálida carne de su entrepierna acaricia tu miembro"

        n "volviendo a subir sus caderas hasta llegar a la cima dónde vuelve a metérsela dentro."

    n "Percibes el calor de su interior mientras su cuerpo vuelve aumentar de tamaño."

    menu:

        pt "¿Vuelve a transformarse?"

        "No hace falta que cambies tu cuerpo." if night05_elysium_3rdRound_bigBodyOpinion not in ["dirtyTrick", "dontCare"]:
            call p_Help
            $pl.ch_pts("np",1)

            if night05_elysium_3rdRound_bigBodyOpinion == "loveAnyway":

                p "Para mi ya eres perfecta."

                ne "Gracias [protname]."

            elif night05_elysium_3rdRound_bigBodyOpinion == "smallBetter":

                p "De hecho, te prefiero así."

                ne "Ya..."

            elif night05_elysium_3rdRound_bigBodyOpinion == "like":

                ne "¿No decías que me preferías con esta forma más adulta?"

                p "No si como dices, el precio a pagar es tan alto."

                ne "..."

                ne "Eres un amor."

            elif night05_elysium_3rdRound_bigBodyOpinion == "silence":

                ne "Vaya..."

                ne "Me alegra saber que te importa."

        "¿Es realmente necesario?":
            call p_Help

            ne "..."

            ne "Supongo que no..."

        "¿Otra vez malgastando tu poder?" if not gensex_ILoveYouNeus:
            call p_Help

            $pl.ch_pts("np",-2)

            ne "..."

            ne "¿Quieres dejarme a mí esa preocupación?"

            ne "Al fin y al cabo tampoco es que tú seas un experto en el tema,"

            ne "¿no te parece?"

            p "Tampoco da la sensación que tú lo seas demasiado por lo que veo."

            ne "..."

            ne "¿Por qué eres así conmigo?"

            p "..."

            ne "Puede que parezca que lo hago para intentar gustarte más..."

        "...":
            call p_Help

            if night05_elysium_3rdRound_bigBodyOpinion == "smallBetter":

                ne "Ya sé que aparentemente te gusto más con este cuerpo diminuto..."

            else:

                ne "No lo hago simplemente para gustarte más."

                ne "Quizás ayude..."


    ne "Pero en realidad con este cuerpo no me duele tanto"

    ne "y puedo tenerla toda dentro."

    ne "Además..."

    if gensex_ILoveYouNeus:

        ne "me gusta hacerte el amor de esta manera."

        pt "¿A esto lo llama hacer el amor?"

    else:

        ne "me gusta follarte de esta manera."

        if gensex_YoureAMonster:

            p "Más bien te gusta violarme."

            ne "..."

            ne "Si salvarte la vida lo llamas violarte,"

            ne "entonces llámalo como quieras."

            pt "No, si encima le tendré que dar las gracias..."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        # She can have you against the wall or against the bed wood.

        # Already the dick in the pussy.

        n "Percibes el calor de su espalda contra tu pecho"

        n "al mismo tiempo que su cadera se acerca a tu ingle"

        n "tragándose centímetro a centímetro tu enorme y palpitante miembro."

        ne "Hmm..."

        n "Hasta que sientes el calor de sus nalgas aplastándote la ingle."

        n "Teniéndolo por completo en su interior,"

        n "empieza a danzar sus caderas en movimientos circulares."

        n "Al mismo tiempo, percibes su ardiente carne vaginal masajeando la sensible piel de tu polla"

        n "como si tuviera vida propia."

        n "Acerca su mano a tu mejilla y volteando su rostro te roba un apasionado beso."

        if gensex_INotLoveYouNeus:

            pt "¡¡Qué narices?!"

        n "Sientes que aparta sus caderas liberándote ligeramente de esa enorme presión"

        n "y sin dejar de besarte apasionadamente,"

        n "regresa con sus caderas hasta tragarse tu lastimada polla al completo de nuevo."

        if gensex_INotLoveYouNeus:

            n "Apartándose unos segundos de tus labios:"

            ne "Ya sé que no te gusta que te bese,"

            ne "pero estoy demasiado cachonda..."

            # (what continues:)
            # n "Con una vigorosidad sobrehumana"
            # n "empieza a embestirte como si fuera ella la que te estuviera perforando;"
            # n "metiéndose la polla entera hasta el fondo a toda velocidad"

    else:

        n "Agarra tus piernas doblándolas de nuevo contra tus abdominales"

        n "mientras desciende sus caderas para enterrar tu polla entera en su interior."

        n "Sin embargo, esta vez no te sujeta de los tobillos"

        n "ni tampoco reposa sus nalgas sobre tus caderas,"

        n "sino que te agarra por los mulos y posa sus rodillas sobre la sábana."

        ne "En esta posición parece que sea yo la que te esté penetrando a ti,"

        ne "¿no crees?"

        n "Una cándida sonrisa se dibuja en sus labios."

        ne "Además, quizás hasta puedas respirar mejor."

        if gensex_ILoveYouNeus:

            n "Doblando su cuerpo posando sus voluminosos pechos sobre tu desnudo cuerpo"

            n "acerca sus labios dándote un tierno beso."

            ne "Mi dulce caballero,"

            ne "te amo."

    n "Con una vigorosidad sobrehumana"

    n "empieza a embestirte como si fuera ella la que te estuviera perforando;"

    n "metiéndose la polla entera hasta el fondo a toda velocidad"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        p "¡Ugh!"

        n "hasta que sus nalgas impactan con tanta rapidez sobre tu ingle"

        n "que parece que te esté dando de hostias con ellas."

        if night05_elysium_3rdRoundYou_wood == "out":

            pt "¡Si sigue a este ritmo me dejará el culo hecho una mierda!"

        else:
            pt "¡A este ritmo romperé esta maldita madera con mi trasero!"

    else:

        n "hasta que tu entrepierna empieza a sufrir el hueso de sus caderas clavándose en tus nalgas."

    n "A pesar de que el ardor de su sexo vuelve a calcinarte la polla,"

    n "el particular cosquilleo regresa a tu ingle."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Descubres que sus ojos brillan de nuevo con intensidad,"

    else:

        n "Sus ojos brillan con intensidad,"

    n "esas protuberancias reaparecen en su cráneo,"

    n "las extrañas lenguas regresan en el abismo de su sexo,"

    n "tu polla tiembla con más intensidad,"

    n "hasta que..."

    $ night05_elysium_MCCumshots += 1

    with vpunch
    p "¡UUuughh...!"

    n "Derramas tu corrida en lo profundo de su ardiente sexo."

    n "En lugar de detenerse, aumenta el ritmo."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Te agarras cómo puedes a la pared"

    else:

        n "Te agarras cómo puedes a la sábana"

    n "mientras sigue embistiéndote salvajemente"

    n "y decenas de lenguas tentaculosas calcinan y succionan tu polla por todas partes,"

    n "poniendo especial atención al glande que sigue regurgitando el líquido blanco."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Retuerce su cuello de nuevo y sin darte tiempo a tomar aire"

        n "te besa ímpetu metiéndote la lengua hasta el fondo"

        n "mientras sigue agitando sus nalgas contra tu ingle."

    else:

        n "Desciende su rostro para besarte con ímpetu"

        n "al mismo tiempo que usa sus manos para sujetarte por el cuello."

        n "Introduce su longeva y ardiente lengua hasta la garganta para besarte con apetito y lascivia."

    ne "¡AAaaahh...!"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Abandona tu boca liberándote de su asfixiante beso."

        n "Sientes su carne vaginal calcinando y ahogando tu lamentable polla que sigue bombeando en su interior."

        n "Detiene en seco su movimiento irguiendo su ardiente espalda contra tu pecho"

        if night05_elysium_3rdRoundYou_wood == "out": 

            n "y sus -no menos calcinantes- nalgas aplastándote la pelvis contra esa maldita madera."
        else:

            n "y sus -no menos calcinantes- nalgas aplastándote la pelvis contra el muro."

    else:

        n "Abrazándote con firmeza y aún manteniendo tu polla en su interior"

        n "detiene en seco su movimiento."

    n "El atroz ardor de su sexo se apacigua"

    n "al mismo tiempo que el calor de su cuerpo disminuye."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Ves su cabeza alejarse,"

    else:

        n "Ves su rostro alejarse,"

    n "así como todo su cuerpo empieza a recuperar su reducido tamaño."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Percibes su cálida y sudorosa espalda reposando sobre tu torso."

    else:

        n "Percibes sus manos y su mejilla reposando sobre tu pecho."

    n "Esas lenguas interinas se van alejando y apenas tienes medio pollón enterrado en su interior."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Descubres que esas protuberancias en su cráneo han desaparecido"

        n "y tienes la sensación de que sus ojos se han apagado."

    else:

        n "Al mirarle a los ojos, descubres que ya no brillan con tanta intensidad."

    n "El cansancio se apodera de ti"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "siendo incapaz de apartarte de ella, terminas reposando tu espalda sobre la -ya no tan fría- pared"

    scene black
    with fade

    n "y gradualmente vas cerrando los párpados."


######## #################### #################### ############


label night05_elysium_4rthRoundBeginning:

    window hide dissolve

    pause

    n "slurp"

    extend "slurp"

    p "Euhh..."

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        n "Notas la suave y esponjosa superficie del colchón en tu espalda"

        n "mientras una cálida lengua relame tu agotado, dolorido y flácido miembro."

    else:

        n "Una cálida lengua relame tu agotado, dolorido y flácido miembro."

    p "¿Neus...?"

    scene day05
    with fade

    ne "¿Y quién si no?"

    if night05_elysium_2ndRoundYou_pos_Cond == "doggy":

        p "¿Sigo en la misma habitación?"

        if gensex_ILoveYouNeus:

            ne "Tontín..."

        ne "Has perdido la conciencia durante unos segundos"

        ne "y lo he aprovechado para ponerte más cómodo sobre la cama."

        menu:
            pt "Más cómodo..."

            "¿A esto lo llamas descansar?":
                call p_Help

                n "Te lanza una mirada fría con sus brillantes ojos"

                n "para luego devolverte una maliciosa sonrisa."

            "La verdad es que es algo más cómodo.":
                call p_Help

                ne "Me alegro que sea así."

            "...":
                call p_Help
                pass

    p "¿No dijiste que con tres tenías suficiente?"

    ne "¿Eso dije?"

    p "Hmmm..."

    n "Con mayor facilidad, logra metérsela entera en la boca."

    n "Al estar tan flácida sientes su lengua de modo distinto,"

    n "jugueteando con la sensible piel de tu miembro y moviendo el falo en círculos a voluntad."

    p "Hmmm..."

    n "Sufres una mezcla de placer y dolor,"

    n "el constante ardor al que ha sido sometida te la ha dejado bastante..."

    p "Neus..."

    p "Tres es mi límite,"

    p "no creo que..."

    ne "Shhh..."

    ne "Déjame a mí..."

    with vpunch
    p "¡AUCH!"

    p "¡¿Qué?!"

    ne "Tú descansa..."

    p "¿Me has mordido?"

    ne "Solo un poquitín..."

    if gensex_INotLoveYouNeus:

        p "¡Pero si me ha dolido un cojón!"

        ne "No te quejes tanto."

        if gensex_YoureAMonster:

            p "Eres un monstruo."

            ne "¿Y entonces qué eres tú si te pones cachondo conmigo?"

            p "Dudo que se me vuelva a poner dura."

            ne "¿Eso crees?"

    else:

        pt "¡Pero si me ha dolido un cojón!"

        pt "¿Qué entenderá esta mujer por descanso?"

    n "Percibes su lengua deslizándose alrededor de tu dolorido glande"

    n "mientras desplaza su rostro en distintas direcciones."

    n "La calidez de su boca, lo longeva y ardiente que tiene la lengua,"

    n "el meneo que te da al mover tanto su cabeza, lo sensible que la tienes..."

    p "Euhh.."

    n "Al mirar abajo descubres con algo de sorpresa que tu polla recupera la erección."

    p "¿Qué...?"

    ne "Ya te dije que no te preocuparas."

    ne "Tengo mis artimañas para lograr ponértela bien dura."

    ne "En el fondo también tengo mis encantos,"

    ne "¿no crees?"

    if gensex_YoureAMonster:

        p "No hace falta que me recuerdes lo bruja que eres."

        ne "..."

    with vpunch

    p "Ughh..."

    n "Se la vuelve a meter casi hasta la mitad en la garganta."

    n "Sientes que sube y baja a una mayor velocidad."

    p "Eughh..."

    n "Entre un placer enorme y un dolor punzante."

    p "Neus..."

    n "Sin escuchar tus palabras sus cabezadas aceleran hasta tal punto"

    n "que prácticamente eres incapaz de ver sus facciones con semejante movimiento en el vaivén."

    n "Con una mano te agarra sin sutileza ambos testículos,"

    n "removiéndolos como si quisiera hacer salsa con ellos"

    n "mientras un dedo juguetón acaricia la parte que une tus testículos con el ano."

    n "Sientes el cosquilleo en tu entrepierna."

    menu:

        pt "No puedo más..."

        "<Avisarla de que te vas a correr>":
            call p_Help

            $pl.ch_pts("np",1)

            p "Neus..."

            ne "¿Hmmm...?"

            n "Se la saca de la boca."

            ne "Ohh..."

            ne "¿Ya?"

            ne "¿No has dicho que tres era tu límite?"

            p "Euhh..."

            ne "*Risilla inocente*"

            ne "En realidad, es más bien por mi culpa..."

            p "¿Cómo...?"

            ne "Sigo con hambre..."

            n "Se muerde el labio de un modo que no sabrías definir si es sugerente o preocupante."

            if gensex_ILoveYouNeus:

                ne "Te amo tanto..."


        "...":
            call p_Help

            $pl.ch_pts("np",-1)

            ne "Hmm..."

            ne "Detiene sus cabezadas apartándose de tu palpitante polla."

            ne "Eres un chico malo."

            ne "Aunque me encantaría que me reventaras la garganta con tu corrida,"

            ne "sabes muy bien que es mejor que lo hagas otra vez dentro de mí."


    n "Asciende sugerentemente por tu desnudo y sudoroso cuerpo"

    n "besándote a lo largo del recorrido,"

    n "sintiendo el hormigueo de sus lametones por el ombligo, el pecho, el cuello, la mejilla"

    n "y finalmente haciendo lo mismo en tus labios superiores para terminar besándote con dulzor y ardor"

    n "con su rostro más estilizado y sintiendo su cuerpo más voluminoso."

    n "Te agarra la base de tu polla con su enorme mano"

    n "y sin apenas darte tiempo a reaccionar, se la vuelve a introducir en su sexo."

    n "Con el pectoral aplastado por sus enorme busto y sin apenas darte tiempo a tomar oxígeno"

    n "sigue besándote con vehemencia junto a esa longeva lengua."

    n "En lo profundo de su sexo vuelves a percibir esas extrañas lenguas"

    n "jugueteando con tu erecto pero sensible y torturado miembro."

    n "Intentas reaccionar de algún modo cuando te percatas de que levanta sus caderas librándote de ese ardor,"

    n "para acto seguido volver a zambullir de nuevo tu polla en su interior sin piedad."

    p "Ughh.."

    n "A duras penas eres capaz de levantar levemente el brazo y mover los dedos."

    pt "¿Qué me pasa?"

    n "Con su enorme cuerpo eleva sus caderas sin necesidad de ni siquiera levantar tus piernas."

    n "Sufres el impacto de su ingle chocando contra tu dolorida pelvis una y otra vez."

    ne "Córrete [protname]."

    n "Percibes que sus caderas descienden cada vez con más frecuencia y violencia."

    pt "¡¿Por qué no puedo ni moverme?!"

    n "Tienes la sensación que de seguir así no solo te romperá la cadera,"

    n "sino que la cama entera terminará partiéndose en dos."

    pt "Dios..."

    n "Sientes el cosquilleo emergiendo de tus entrañas."

    ne "Ves en su estilizado y adulto rostro sus ojos brillar con intensidad y deseo."

    ne "¡Dámelo todo!"

    $ night05_elysium_MCCumshots += 1

    p "¡¡Uughhh..!!"

    n "Descargas en su ardiente interior"

    n "al mismo tiempo que te acaricia la mejilla y te besa apasionadamente."

    n "Padeces esas decenas de pequeñas lenguas en lo profundo de su sexo devorando tu polla sin piedad,"

    n "succionando tu esperma directamente del orificio del glande"

    n "mientras te ahogan el mástil deslizándose de la base hasta la punta"

    n "manipulando tu polla como si se tratara de un tubo de pasta de dientes que ya no da más de si."

    n "Sus caderas siguen moviéndose en círculos como si fuera un desbocado tornado,"

    n "hasta el punto que padeces tanto dolor que tus caderas apenas perciben otra cosa"

    n "que no sea el impacto de los huesos de sus caderas contra tu ingle."

    p "Neus..."

    n "Silencia tus palabras con otro beso con lengua"

    n "a medida que se desliza a menos velocidad"

    n "y esas extrañas lenguas interinas empiezan a descender en número e intensidad."

    n "Tus párpados se van cerrando."

    scene black
    with fade

    n "y el cansancio se apodera de ti."

####

label night05_elysium_5thRoundBeginning:

    ono "slurp"

    extend " slurp"

    p "No..."

    n "Percibes su lengua casi como si fuera papel de lija rozando tu rojiza y dolorida polla"

    n "la cual por alguna razón, sigue estando en erección, palpitando y temblando."

    scene day05
    with fade

    p "Otra vez no..."

    n "Incapaz de hacer otra cosa,"

    ne "Hmmm..."

    n "percibes que vuelve a metérsela en su ardiente e infernal boca."

    n "Incapaz de hacer otra cosa,"

    scene black
    with fade

    n "tus párpados se cierran de nuevo."

    $ night05_elysium_MCCumshots += 1

    jump night05_elysium_AfterSex


    # She sucks your dick. Just to get it harder, even if it's already a bit hard.

## 1rst Round

    # Once is pretty wet and hard, she climbs over it and start introducing it in her pussy.

    # You can grab her and fuck her missionary or let her do her thing.

    ## If she fucks you, she gets so close to orgams that she must STOP. (You can make her Cum)

    ## If you fuck her, you can get her to the orgasm. (Can you make her Cum?)

            # If you make her cum. Daddy-O appears.

    # A) She Rides you. (You can make her cum.)

    # B) You fuck her. (Missionary or Doggystyle) Grab her against a wall - Rise Her legs and fuck her violently. (You can cum outside of her Pussy)
        # Doggy
            # If you're hard with her, she can drags you back and rides you backwards.
            # If you bring her up, you can fuck her against the wall.
        # Missionary
            # If you're hard with her you can rise her legs and fuck harder.
            # If you're lovely with her she will increase a bit her body in order to be able to kiss you while you fuck lovely with her.


## 2nd Round

    # She realizes it was too dangerous and is better now if she controls the whole thing.

    # A) If she rided you before, now she can ride you backwards while you see her ass. Rise your legs and Fucks you in Amazonic way.

    # B) She Rides you in a lovely pace.

    # If you were hard  with her, she will be hard with you, otherwise she will be lovely.


## 3rd Round

    # She puts herself over you and she orders to relax,

    # she kisses around all your body and move her lips while kissing your body.

    # She wishes she could fuck you while she kisses you, a duras penas logra besar tu barbilla. (She's short.)

    # She grows her body in order to make love with you. You can tell her she doesn't need to grow her body in order to love you.

    # After being lovely.


## After 3rd Round

    ## She grabs you in order to fuck in Amazonic way (She being big).

    # You lose your senses, but she keeps licking and sucking your dick.



    #####
    #########


############
######
######
######
######




    

##### You start licking her pussy, but later on she makes you stop, and start licking your dick.

### ONce is pretty wet, she climbs over it and start introducing it in her pussy.

### You can decide to grab her and fuck her missionary while you kiss each other.

## Basically you make love.

### She asks you to stop, she can't have an orgasm. Or father will posses her, even in this place and that's gonna be the end of both of us.

## You can ignore her and drive her to the orgasm and that's a bad ending.

# You can obey her, and then she starts sucking your cock once again, you asks her to make a nintysix position, she tells you it's not a good idea, but you tell her tha tyou will stop when she asks you... shen thens accepts. Before you can start licking her pussy you start to feel you're gonna cum.

#She stops and climbs over you, telling you that you must cum inside of her in order to pregnant her, it's the only way.

# Once you cum, you feel she doesn't stop.

# She tells you, with a single shot we can't be sure, we must try for another... you have stamina for another shot, don't you?

# She begins licking your dick once a gain, and now she asks you to fuck her in doggystyle. You can fuck her in the ass, but you must end in her pussy. You accept and star fucking her ass. YOu can slap her ass several times, she asks you to do it harder. You see she's starting to cry, you ask if you're hurting her, no... it's just I'm so happy.. Are you sure is not too big for your little ass? Well probably a bit, but I can endure I promise you.

# When you're about to cum, she asks you to change the hole fast. You obey and you finally cum twice in her pussy.

# Your eyes start to close, when you feel her tongue once again on your shaft. You ask... is two not good enough... And she tells you that your dick is getting hard once again, and 3 is better than 2. Here eyes are more glommy and her lust is bigger, you can feel her lust, her desire. she climbs you once again you feel her body weights more, looks like she has two horns on her head, her pussy feels different, looks like her breasts is bigger than before, and her teeth is sharper.

#You feel how she jumps over you is stronger and you dick is feeling more pain, but she doesn't stop, actually she goes faster and deeper, her body is definitely bigger. In a moment when you feel you're about to cum, she also stops abruptly, when you asks she tells you she's about to cum... You can decide to keep fucking her "bad end".

# She stops and lies over your naked body, her body gets once again reduced and you feel her pussy getting tighter.

# Your sweaty body against her, you feel her lips over your stomach, chest, nipples, biting one of them, (she takes your dick out of her)your neck your lips, and once again over your face kissing you lovely, she asks you if you really love her.

# If you keep like this I'm gonna cum anway. She asks you if you really love her. Of course I love you, dummy.

#####

## ONce you cum inside of her she keeps jumping over you, until you feel she about to cum, and then she stops and directly puts your dick in her mouth doing a fast deepthroat that makes you feel pleasure and pain in same ways until you fade out.



label night05_elysium_sexMast_label:

    $ night05_elysium_sexMast_Cond = True

    n "Te acerca el rostro a tu cara mientras te sujeta suavemente con sus cálidas manos."

    p "¿Qué...?"

    ne "Tranquilo,"

    ne "para ti solo será un momento."

    p "¿Para mí?"

    n "Sus ojos brillan con intensidad,"

    scene black
    with fade

    n "y todo se vuelve oscuro."

    pause

    jump night05_elysium_AfterSex


label night05_elysium_NeusOrgasm:

    aj "Here is where Neus is having an orgasm."

    # Here is where Neus is having an orgasm.

    # NOT_FINISHED

    call WIP

    jump gameover