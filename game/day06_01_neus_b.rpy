
label p_neus_afterOrgasm:

    if config.version < "00.99.99": #For FUTURE
        call endupdatescript

    if (pl.np < 100 and gensex_YoureAMonster) or pl.np < 30 or p_ao_neusLastSecret:

        if not p_ao_neusLastSecret:
            $ renpy.notify("[p_neg] 100[hn]")

        $ day06_company = "atHome"

        jump day06_night_home

    scene black
    with fade

    p "Hhmm..."

    tx "¿Se encuentra bien?"

    ne "Sí,"

    extend " bueno..."

    ne "No está muerto,"

    ne "si es lo que preguntas."

    tx "..."

    d "Muerto no sé,"

    d "pero desde luego,"

    extend " está para el arrastre..."

    tx "El sol está despuntando."

    ne "Lo sé,"

    extend " lo sé..."

    ne "Dídac,"

    extend " ¿me ayudas?"

    tx "¿No será un poco sospechoso si llevamos a alguien inconsciente por la calle de este modo?"

    ne "He llamado a alguien de confianza que nos está esperando abajo,"

    ne "solo tenemos que evitar que alguien nos vea hasta llegar ahí;"

    ne "y en cualquier caso,"

    ne "tengo energía suficiente como para convencer a quien nos vea"

    ne "que estamos llevando a un amigo borracho a casa."

    tx "¿Y a dónde tienes pensado llevarnos?"

    ne "Ahora no,"

    ne "no es seguro que hablemos sobre esto hasta que lleguemos."

    tx "..."

    ne "¿Confías en mi?"

    tx "Sí."

    d "Yo no mucho..."

    tx "..."

    ne "Dídac,"

    extend " por favor..."

    d "Vale,"

    extend " vale..."

    d "Joder..."

    d "¿Soy yo?"

    d "¿o [protname] ha ganado peso?"

    tx "Quizás has olvidado que has perdido un poco de masa muscular..."

    if not DidacPregnant:

        d "Espero poderla recuperar a partir de mañana..."

        tx "¿Estás seguro que no has jugado a médicos y pacientes con nadie?"

        d "No soy una fulana como otras..."

        tx "¿A quien te refieres?"

        ne "¡Haya paz!"

        tx "Pssst..."

    else:

        d "Tssk..."

    tx "Trae,"

    tx "ya os ayudo."

    scene black
    with fade

    with hpunch
    ono "BBBRRRRRMMMMM..."

    pt "¿Estoy en un coche...?"

    tx "¿Seguro que está bien?"

    d "Después de todo el trote que llevamos,"

    d "el cabrón sigue durmiendo como una {a=https://es.wikipedia.org/wiki/Marmota}marmota{/a}."

    ne "Está muy cansado."

    ne "Succioné quizás más de lo que debía,"

    ne "pero prefiero tener de más,"

    extend " que de menos."

    ne "Lo mejor es que descanse,"

    if p_neus.cumReceived in ["vaginal", "anal", "oral", "pre-oral"]:

        ne "lo tiene bien merecido."

    else:

        ne "no es que se lo merezca,"

        ne "pero es lo que necesita."

        tx "¿A qué te refieres?"

        ne "Nada,"

        extend " no importa."

    d "¿No podemos saber aún a dónde coño vamos?"

    ne "No."

    ne "No es seguro."

    tx "Aparentemente, vamos hacia el norte."

    d "¡Hace horas que vamos al norte!"

    d "Hemos cambiado de coche como unas tres veces,"

    d "Con ese primer conductor,"

    d "que parecía el típico hombre de negro con gafas de sol..."

    d "Pero desde entonces hemos ido en taxi."

    d "¡Y en todos ellos has hecho lo mismo con los ojos!"

    d "¿Tan poco te fiabas del primer conductor?"

    d "¿Euh?"

    d "¿Otra vez?"

    tx "¡¿Será posible que seas tan estúpido?!"

    tx "¡¿Te piensas que el taxista es sordo,"

    tx "o qué demonios te pasa?!"

    d "Tssk..."

    ne "Haya paz."

    ne "No me hagáis el trabajo más difícil,"

    extend " por favor."

    ne "Tampoco me ha quitado mucha energía."

    ne "Pero aún así,"

    ne "sería mejor que nos mantuviéramos en silencio,"

    ne "tampoco es bueno que hurgue innecesariamente en la mente de alguien."

    d "¿Entonces por qué no nos hemos quedado con el primer conductor?"

    d "¿Es que no te fiabas de ese tipo oscuro con gafas?"

    ne "Le hubiera confiado mi vida."

    d "Pues no lo parece."

    tx "¿De verdad no lo entiendes?"

    d "¿El qué?"

    tx "La mejor manera de evitar que alguien interrogue al conductor que nos ha llevado,"

    tx "para averiguar a dónde hemos ido,"

    tx "es coger varios vehículos"

    tx "sin que el anterior conductor sepa ni siquiera en qué coche o dirección hemos ido después."

    d "Hmmm..."

    d "¡Eso demuestra que no se fiaba tanto del primer conductor!"

    ne "No."

    ne "Eso es porque sé de lo que es capaz mi padre."

    d "..."

    scene black
    with fade

    d "Podríamos tomarnos un descanso,"

    d "hace horas que salimos de {a=https://en.wikipedia.org/wiki/Barcelona}Barcelona{/a}."

    ne "No vamos a parar."

    d "¡Me estoy meando!"

    tx "¿Qué tienes,"

    extend " cinco años?"

    d "Tengo la vejiga pequeña, joder."

    ne "Si realmente tienes que hacerlo,"

    ne "hazlo en esta botella."

    d "¡¿Me estás tomando el pelo?!"

    d "¡¿Cómo coño quieres que apunte si no tengo polla?!"

    tx "Bienvenida al mundo, querida."

    d "¡Vete a la mierda!"

    if not DidacPregnant:

        d "¡¿Y por qué coño aún no he recuperado mi forma masculina?!"

        ne "No creo que tardes mucho en sufrir los síntomas."

        ne "Seguramente ya empieces a tener dolor de cabeza,"

        ne "¿no es así?"

        d "..."

        ne "En unas horas empezarás a hacer el cambio."

        d "¡¿Voy a volver a pasar por la misma mierda dentro de este coche?!"

        ne "Tranquilo,"

        ne "para entonces quizás ya habremos llegado y podrás hacerlo reposando en una cama."

        tx "No te quejarás..."

        d "Sigo teniendo ganas de mear."

    else:

        ne "¡¿Queréis tener la fiesta en paz?!"

    ne "No vamos a parar."

    ne "Usa esta botella si tienes que hacerlo,"

    ne "y si tienes ganas de hacer lo otro,"

    ne "hay una caja de plástico detrás que podéis usar."

    d "Si tengo que hacer lo otro,"

    d "vamos a morir todos aquí dentro."

    tx "Realmente has pensado en todo."

    ne "No es la primera vez hago esto."

    scene black
    with fade

    p "Hghhmm..."

    tx "Creo que empieza a reaccionar."

    d "¡No me jodas!"

    d "¡Le hemos llevado por todo el puto parking!"

    d "¡Ya podría ir andando de una jodida vez!"

    d "¡Hace medio siglo que está durmiendo!"

    ne "Ya te lo he dicho,"

    ne "le he quitado mucha energía."

    d "¡Llámalo por su jodido nombre,"

    d "esperma!"

    d "¡Ni que le hubieras hecho correr dos jodidas maratones seguidas!"

    d "¡¿Te tragaste su esperma o su vida?!"

    ne "Un poco de ambas..."

    d "¿Qué?"

    ne "Bueno,"

    ne "de todos modos ya estamos llegando."

    ne "Solo un poquito más."

    scene black
    with fade

    h01 "{i}Bonsoir Miss Elur{/i}."

    h01 "{i}Avez-vous besoin d'aide pour déplacer votre dîner ?{/i}"

    ne "{i}Non,"

    extend " merci{/i}."

    ne "{i}J'ai juste besoin des clés des chambres{/i}."

    h01 "{i}Bien sûr,"

    extend " les voici{/i}."

    tx "..."

    tx "¿Nos ha preguntado si queríamos asistencia para llevar nuestra cena?"

    ne "No preguntes y sigue andando."

    d "Estos gabachos están locos..."

    scene black
    with fade

    jump day06_night_label

#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################

## SEX WITH NEUS UNCUFFED

default day06_neusAlone_uncuff_cond = False

default day06_neusAlone_pasSex_pos_missionary = False

label day06_neusAlone_uncuff:

    $ renpy.notify("[p_pos] 230[hn]")

    call endtranslation

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ nteye = "right02"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "Euhmm.."

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Estás seguro?"

    $ nteye = "front04"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    p "Sí,"

    extend " lo estoy."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Quiero que me prometas una cosa."

    $ nteye = "front02"
    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    # CHOICE
    menu:

        "Lo que quieras.":
            call p_Help
            $pl.ch_pts("np", 1)

        "Dime.":
            call p_Help
            #$pl.ch_pts("np", 2)

        "¿Por qué será que esto me suena mal...?":
            call p_Help

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "No seas así..."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            p "..."

    $ nteye = "front00"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Por mucho que te pida un orgasmo,"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "no lo permitas."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Es posible que se me vaya la cabeza..."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Prométemelo."

    $ nteye = "front05"
    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    menu:

        "Te lo prometo.":
            call p_Help
            $pl.ch_pts("np", 2)

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve


        "No te lo puedo prometer.":
            call p_Help
            $pl.ch_pts("np", -1)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "Entonces tengo que esposarte."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            menu:

                "Vale, vale, te lo prometo.":
                    call p_Help
                    $pl.ch_pts("np", 1)

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    pause 0.2

                "Entonces hazlo.":
                    call p_Help

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Silentx06
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    pause 0.2

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_secondHand

    $ day06_neusAlone_uncuff_cond = True

    pause 0.2

    scene day06
    with fade

    call endillustrations

    ne "..."

    n "Alarga su brazo para acercarse a tu mano enmanillada."

    ono "clic"

    n "Sientes tu muñeca liberada."

    p "Ughh..."

    n "Aunque apenas eres capaz de moverla."

    ne "Te cuesta moverte, ¿verdad?"

    p "Me siento bastante débil."

    ne "Hay una manera de conseguir que tengas más energía,"

    ne "pero tiene un precio."

    p "¿A qué te refieres?"

    ne "Si te bebes mi sangre,"

    ne "tu cuerpo olvidará el el dolor y el cansancio que sufres."

    ne "Recuperarás tus fuerzas"

    if gensex_ILoveYouNeus:

        ne "y podrás hacerme el amor."

    else:

        ne "y podrás hacerme lo que quieras."

    p "¿Y cual es el precio a pagar?"

    ne "..."

    ne "Eso te permitirá correrte una,"

    ne "quizás dos veces."

    ne "Pero después de eso..."

    p "¿Sí...?"

    ne "Es posible que te pases una semana sin poder levantarte de la cama."

    p "..."

    p "¿Entonces por qué me estabas esposando?"

    ne "Si por casualidad recuperases las fuerzas"

    ne "y me cogieses en un momento de debilidad,"

    ne "yo..."

    ne "Existía el peligro de que acabara teniendo un orgasmo."

    p "..."

    ne "No pasa nada,"

    ne "puedes relajarte en la cama"

    if gensex_ILoveYouNeus:

        ne "mientras soy yo la que te hace el amor,"

    else:

        ne "mientras soy yo la que hace el trabajo,"

    ne "no hace falta que te espose si no quieres."

    # CHOICE

    $ day06_neusAlone_uncuff_bloodDecision = "False"

    menu day06_neusAlone_uncuff_bloodDecision:

        pt "¿Una semana en cama por beberme su sangre?"

        "Quiero arriesgarme..":
            call p_Help
            #$pl.ch_pts("np",1)

            ne "De acuerdo."

        "Prefiero no arriesgarme.":
            call p_Help
            #$pl.ch_pts("np",1)

            ne "Lo entiendo..."

            jump day06_neusAlone_uncuff_NeusFucksYou

        "¿Qué es lo que tú deseas?":
            call p_Help
            $pl.ch_pts("np",1)

            ne "..."

            ne "Lo que tu elijas,"
            
            ne "me estará bien."

            p "Eso no es una respuesta."

            ne "..."

            if gensex_ILoveYouNeus:

                ne "Quiero que me hagas el amor."

            else:

                ne "Quiero que me folles."

            p "..."

            ne "Ya sé que es un tanto egoísta por mi parte..."

            # CHOICE

            menu:

                "¿Quieres tenerme una semana sin poder moverme para aprovecharte de mi?":
                    call p_Help
                    $pl.ch_pts("np",1)

                    ne "..."

                    ne "Es posible..."

                    p "..."

                    ne "En realidad preferiría ponerme a cuatro patas"

                    ne "y que me dieras tan duro como pudieras;"

                    ne "pero ya sabes lo arriesgado que es para mi tener un orgasmo."

                    menu:

                        "¿Incluso después del solsticio?":
                            call p_Help

                            ne "Sí,"

                            extend " desgraciadamente,"

                            ne "seguirá siendo arriesgado."

                            p "..."

                            ne "Va..."

                        "...":
                            call p_Help

                    ne "Déjate de bromas y decídete."

                    menu:

                        "Dame tu sangre.":
                            call p_Help
                            $pl.ch_pts("np",1)

                            ne "Hmm..."

                        "Prefiero no arriesgarme.":
                            call p_Help

                            ne "Supongo que tienes razón."

                            jump day06_neusAlone_uncuff_NeusFucksYou

                "Entonces dame tu sangre.":
                    call p_Help
                    $pl.ch_pts("np",1)

                    ne "Hmm..."

                "Prefiero no arriesgarme.":
                    call p_Help

                    ne "Como quieras."

                    jump day06_neusAlone_uncuff_NeusFucksYou

        "..." if day06_neusAlone_uncuff_bloodDecision == "False":
            call p_Help

            $ day06_neusAlone_uncuff_bloodDecision = "doubt"

            ne "Tienes que tomar una decisión."

            jump day06_neusAlone_uncuff_bloodDecision

    $ day06_neusAlone_uncuff_bloodDecision = "True"

    call day06_bloodDrink
        # ne "Hubiera sido mejor preparar un frasco para esto,"
        # ne "pero supongo que no pasará nada."
        # pt "¿Qué debería pasar?"
        # 
        # p "Hasta que se me termine esta euforia,"
        # extend " supongo."
        # ne "Sí..."
        # p "Ya..."

    jump day06_neusAlone_uncuff_howYouWantIt



label day06_neusAlone_uncuff_howYouWantIt:

    ne "Dime..."

    if gensex_ILoveYouNeus:

        ne "¿Cómo quieres hacerme el amor?"

    else:

        ne "¿Cómo quieres follarme?"

    # CHOICE

    # Cunnilingus.

    $ day06_neusAlone_uncuff_you_Sex_Pos = "vaginal"

    menu:

        "<Empezar con un cunnilingus>":
            call p_Help
            $pl.ch_pts("np", 1)

            $ day06_neusAlone_uncuff_you_Sex_Pos = "cunnilingus"

            jump day06_neusAlone_uncuff_you_cunnilingus

        "<Vaginal>":
            call p_Help
            $pl.ch_pts("np", 3)

            $ day06_neusAlone_uncuff_you_Sex_Pos = "vaginal"

            jump day06_neusAlone_uncuff_sex
                # n "Te agarras la tersa y dura polla y la deslizas por sus más que cálidos labios vaginales."
                # ne "No me hagas sufrir..."
                # n "Sin demasiada demora la introduces en su estrecho y ardiente interior,"
                # n "dónde su carne se arropa como si fuera un enorme tentáculo a tu polla."

        "<Anal>":
            call p_Help
            $pl.ch_pts("np", 2)

            $ day06_neusAlone_uncuff_you_Sex_Pos = "anal"

            jump day06_neusAlone_uncuff_sex
                # n "Te agarras la tersa y dura polla y la deslizas por sus más que cálidos labios vaginales."
                # ne "No me hagas sufrir..."
                # n "Sin demasiada demora la introduces en su estrecho y ardiente interior,"
                # n "dónde su carne se arropa como si fuera un enorme tentáculo a tu polla."


label day06_neusAlone_uncuff_you_cunnilingus: 

    p "Reposa tu espalda sobre la cama."

    ne "Obedece tus órdenes y se acuesta sobre la sábana mirándote con excitación y nerviosismo."

    n "Acercas tu rostro a su entrepierna"

    n "y abriéndola de piernas, acaricias su sexo con tu lengua."

    ne "Hmmm..."

    ne "Te recuerdo que no puedo tener un orgasmo,"

    ne "eres tú quien..."

    p "Lo sé."

    p "Confía en mi."

    ne "..."

    ne "De acuerdo."

    n "Deslizas tu boca por sus labios exteriores dando pequeños y continuos besos en su suave piel."

    n "Acercas tu mano y con tu pulgar acaricias cariñosamente su rosado y abultado clítoris."

    ne "Hhhmm..."

    n "Desplazas tu lengua por su interior acariciando la más que cálida carne que la envuelve"

    n "mientras su cuerpo se agita levemente a medida que profundizas en su sexo."

    ne "Ahhmm..."

    $ day06_neusAlone_uncuff_you_cunnilingus_analFinger = False

    menu:

        "<Juguetear también con su orificio anal>":
            call p_Help
            $pl.ch_pts("np",2)

            $ day06_neusAlone_uncuff_you_cunnilingus_analFinger = True

        "<Seguir enfocándote solo en su vagina>":
            call p_Help

    if day06_neusAlone_uncuff_you_cunnilingus_analFinger:

        n "Acercas los dedos de tu mano libre a la parte sensible de su orificio anal."

        ne "¿Por ahí también?"

        p "¿No te gusta?"

        ne "Me encanta..."

        n "Sigues lamiendo su interior mientras jugueteas con penetrar tu dedo índice en su cavidad trasera."

        ne "Quizás si lo humedecieras un poco..."

        n "Desplazas esa mano por su vagina, remojando tus dedos en su jugo,"

        n "para después volver a su trasero"

        n "e introducir el dedo índice más fácilmente en su interior."

        ne "Hmmm..."

    else:

        n "Con tu mano libre,"

        n "acercas esos dedos bajo tu lengua, que sigue labrándose su camino en ardiente sexo"

        n "y junto a ella, profundizas aún más,"

        n "jugueteando contra esos muros carnosos y ardientes."

        ne "Hmmm..."

        n "Con más vigorosidad, agitas tu dedos en su clítoris, pellizcándolo y agitándolo."

        ne "Ughh..."

        n "Para luego sacar tu empapada lengua de su interior y acercarla a su perla rosada,"

        n "jugueteando con ella, sin detener el errático movimiento de tus manos."

        ne "[protname]..."

    p "Realmente estás empapada."

    ne "No sé de quien es la culpa..."

    if day06_neusAlone_uncuff_you_cunnilingus_analFinger:

        n "Sigues jugueteando con su clítoris con tu lengua y tus dedos,"

        n "mientras con la otra mano,"

        n "logras meter tus cuatro dedos hasta los nudillos en su interior"

        n "penetrando su sexo sin compasión."

    else:

        n "Sigues removiendo tu lengua, como si fuera un pequeño torbellino,"

        n "acariciando sus paredes vaginales"

        n "mientras profundizas aún más tu dedo en su trasero."

    ne "¡Ahhmm...!"

    ne "Para..."

    p "¿Por qué?"

    if gensex_ILoveYouNeus:

        ne "Quiero que me hagas el amor."

    else:

        ne "Quiero que me folles."

    ne "Quiero sentirte dentro de mi."

    p "..."

    # CHOICE

    $ day06_neusAlone_uncuff_you_previsSex_kiss = False

    menu day06_neusAlone_uncuff_you_previsSex_question:

        "<Besarla con tu boca empapada en sus jugos>" if day06_neusAlone_uncuff_you_previsSex_kiss == False:
            $pl.ch_pts("np",2)

            $ day06_neusAlone_uncuff_you_previsSex_kiss =  True

            n "Apartas tu rostro de su entrepierna"

            n "y con la boca y barbilla empapadas en sus jugos"

            n "te acercas a su rostro y te mezclas en un beso apasionando"

            n "entremezclando su flujo con vuestra saliva."

            if gensex_ILoveYouNeus:

                ne "Hazme el amor."

            else:

                ne "Fóllame."

            n "Sientes sus manos descendiendo por tus lumbares hasta llegar a tu trasero"

            n "dónde hace cierta presión para que te acercas a ella."

            ne "Hmmm..."

            jump day06_neusAlone_uncuff_you_previsSex_question

        "<Penetrarla vaginalmente>":

            $ day06_neusAlone_uncuff_you_Sex_Pos = "vaginal"

            jump day06_neusAlone_uncuff_sex

        "<Penetrarla analmente>":

            $ day06_neusAlone_uncuff_you_Sex_Pos = "anal"

            jump day06_neusAlone_uncuff_sex


label day06_neusAlone_uncuff_sex:

    n "Te agarras la tersa y dura polla"

    if day06_neusAlone_uncuff_you_Sex_Pos == "vaginal":

        n "y la deslizas por sus más que cálidos labios vaginales."

        if day06_neusAlone_sex != "vaginal":

            ne "Me alegro que por fin elijas terminar por aquí..."

            p "¿Alguna queja?"

            ne "En absoluto."

        else:

            ne "No me hagas sufrir..."

    else:

        n "y la deslizas por su cálido orificio anal."

        if p_neus.anal_received > 3: 

            ne "¿Otra vez por aquí?"

            p "¿Algún problema?"

            ne "No..."

            ne "para nada."

            if day06_neusAlone_sex == "vaginal":

                ne "Al fin y al cabo, ayer ya terminaste por el otro lado."

                p "..."

            else:

                ne "Es solo que me hubiera gustado que hubieras podido terminar por el otro lado esta vez."

    n "Sin demasiada demora la introduces en su estrecho y ardiente interior,"

    n "dónde su carne se arropa como si fuera un enorme tentáculo a tu polla."

    ne "Aaahhmm..."

    pt "¡¡DIOS!!"

    pt "¡Si apenas me he movido!"

    if day06_neusAlone_uncuff_you_Sex_Pos == "vaginal":

        pt "¡No sé si será su infernal coño"

    else:

        pt "¡No sé si será su infernal trasero"

    pt "o esta sangre que me ha dado,"

    pt "pero la tengo super sensible!"

    ne "[protname],"

    extend " por favor..."

    ne "córrete cuanto antes."

    ne "No te haces una idea lo que me está costando aguantar..."

    if day06_neusAlone_uncuff_you_Sex_Pos == "anal":

        p "¿Aunque sea por detrás?"

        ne "No me juzgues..."

    p "Ugh..."

    n "Sientes el particular cosquilleo recorriendo tu entrepierna"

    n "mientras tu polla palpita de forma alocada en su interior."

    pt "¡Si apenas le he metido la punta!"

    n "Intentas mover tus caderas pero justo en ese instante."

    ne "¿[protname]?"

    p "¡UGH...!"

    ne "¡Espera,"

    extend " aún no...!"

    ono "spuuurt"

    n "Debido a los espasmos de tu cuerpo,"

    n "cuando apenas habías logrado meter la punta de tu miembro en su interior,"

    n "tus temblorosas piernas y tu palpitante polla"

    n "hacen que te apartes unos centímetros de ella en el momento del orgasmo"

    n "y acabes derramando tu esperma por su barriga y rostro."

    ne "..."

    $ day06_neusAlone_uncuff_sex_FirstOrgasmApologie = False

    # CHOICE

    menu:

        "Lo siento...":
            call p_Help
            $pl.ch_pts("np",1)

            $ day06_neusAlone_uncuff_sex_FirstOrgasmApologie = True

            ne "No,"

            ne "por favor,"

            extend " no te disculpes."

            ne "Es mi culpa."

            ne "Debería haberte advertido de los efectos secundarios de mi sangre."

        "Creo que esto ha sido por culpa de los efectos de tu sangre.":
            call p_Help

            ne "Sí,"

            ne "eso parece."

        "...":
            call p_Help

            ne "Tranquilo,"

            ne "Es normal..."

    ne "Todo tu cuerpo está en ebullición,"

    ne "tu sangre está alterada,"

    ne "y tu polla está mucho más sensible."

    ne "Es normal que no hayas podido controlarlo y haya sido tan temprana."

    ne "Solo espero que para la próxima no te corras tan pronto"

    ne "y apuntes algo mejor..."

    if day06_neusAlone_uncuff_sex_FirstOrgasmApologie:

        p "Lo siento."

        ne "No te disculpes tontín."

    n "Desliza uno de sus dedos por su barriga agarrando parte de tu derramado esperma"

    n "y se lo lleva a su boca."

    ne "Hmmm..."

    ne "Sigue algo cálido y espeso..."

    menu:

        "<Esperar a ver qué hace>":
            call p_Help

            n "Pasa su lengua por la comisura de sus labios"

            n "disfrutando de cada gota derramada por su rostro."

            n "Para luego pasar sus manos por su piel"

            n "recogiendo cada uno de las gotas que has derramado en su cuerpo"

            n " hasta que no deja ni rastro."

            ne "Por favor..."

            ne "No te asustes por lo que voy a hacer ahora..."

            pt "¿Que no me asuste?"

            n "Alarga su lengua hasta el punto en que se vuelve inhumanamente longeva"

            n "y vuelve a pasar por dónde había usado sus dedos"

            n "para relamer los restos resecos en su piel."

            n "Hasta que finalmente regresa a su boca."

            ne "HMmm..."

            ne "Soy consciente que quizás no quedaba mucho,"

            ne "pero me gusta apurar hasta la última gota."

            ne "Al fin y al cabo no tienes corridas infinitas..."

            p "..."

            ne "¿Estás esperando que te lo pida?"

            if day06_neusAlone_uncuff_you_Sex_Pos == "vaginal":

                if p_neus.vaginalDeep_received > 1:

                    ne "Porque sabes de sobra que la quiero volver a sentir dentro de mi..."

                else:

                    ne "Porque sabes de sobra que la quiero sentir toda dentro de mi..."

            else:

                if p_neus.analDeep_received > 1:

                    ne "Porque sabes de sobra que puede entrar entera..."

                else:

                    ne "Veamos si puedes metérmela entera..."

                ne "La quiero sentir toda dentro de mi."

            jump day06_neusAlone_uncuff_sex_SecondRound

        "<Volver a metérsela>":
            call p_Help

            jump day06_neusAlone_uncuff_sex_SecondRound


label day06_neusAlone_uncuff_sex_SecondRound:

    n "Vuelves a acercarte a su entrepierna,"

    n "y esta vez, logras penetrar algo más que tu glande en su interior."

    ne "Hmm..."

    ne "No te quedes solo con la punta..."

    if gensex_ILoveYouNeus:

        ne "Atraviésame con tu lanza,"

        ne "mi querido {a=https://en.wikipedia.org/wiki/Lancelot}Lancelot{/a}."

    else:

        ne "Métemela toda,"

        ne "por favor..."
    
    n "En cada nueva embestida logras penetrar más en su interior,"

    if day06_neusAlone_uncuff_you_Sex_Pos == "vaginal":

        n "hasta que finalmente hundes por completo tu polla en su sexo."

    else:

        n "hasta que finalmente hundes por completo tu polla en su trasero."

    ne "HMmmm..."

    ne "Sí... "

    if day06_neusAlone_uncuff_you_Sex_Pos == "vaginal":

        if p_neus.vaginalDeep_received == 0:

            ne "Has conseguido meterla entera..."

    else:

        if p_neus.analDeep_received == 0:

            ne "No me puedo creer que haya entrado entera..."

    if ((day06_neusAlone_uncuff_you_Sex_Pos == "vaginal" and p_neus.vaginalDeep_received == 0) or
        (day06_neusAlone_uncuff_you_Sex_Pos == "anal" and p_neus.analDeep_received == 0)):

        p "¿Te duele?"

    ne "Me encanta..."

    ne "Pero ve despacio por favor..."

    if ((day06_neusAlone_uncuff_you_Sex_Pos == "vaginal" and p_neus.vaginalDeep_received > 0) or
        (day06_neusAlone_uncuff_you_Sex_Pos == "anal" and p_neus.analDeep_received > 0)):

        ne "no sé si lo notaste,"

        ne "pero ayer me dolió un poquito..."

    p "..."

    ne "Solo te pido que vayas despacio,"

    ne "realmente la tienes enorme..."

    ne "pero solo un ratito,"

    ne "también tengo ganas de que me folles como a una perra."

    p "¿Quieres que te trate como una princesa o como una perra?"

    ne "..."

    ne "Cuando me pones así de caliente,"

    ne "prefiero que me trataras más como..."

    ne "como si fuera..."

    menu:

        "Como si fueras una perra en celo.":
            call p_Help
            $pl.ch_pts("np",1)

            ne "Sí..."

            ne "algo parecido."

        "Como si fueras una puta de barrio que se vende el trasero por un dolar.":
            call p_Help
            $pl.ch_pts("np",-2)

            ne "..."

            ne "¿De verdad?"

            ne "¿No se te ha ocurrido nada mejor?"

            p "¿Llamarte perra es mejor?"

            ne "Que romántico eres cuando quieres..."

            pt "¡Como si lo que me está pidiendo fuera romanticismo!"

        "Haré lo que me pidas.":
            call p_Help
            $pl.ch_pts("np",-1)

            ne "..."

            ne "No hace falta que seas siempre tan servicial [protname]."

            ne "A veces me gusta que también puedas satisfacer tus deseos."

            p "..."

            ne "No pares..."

        "¿Cómo si fueras qué?":
            call p_Help
            $pl.ch_pts("np",2)

            p "¿Qué?"

            ne "No te disgusta que quiera que me trates así,"

            ne "¿verdad?"

            p "Dilo."

            ne "..."

            p "Di como quieres que te trate."

            ne "Como si fuera une perra en celo."

        "...":
            call p_Help
            #$pl.ch_pts("np",2)

            ne "No importa..."

            ne "Pero no pares,"

            ne "por favor..."

    n "Teniéndola de frente moviendo tu polla en su interior,"

    n "sientes sus manos acariciando tu espalda acercándose a tu cuello."

    n "Mirándote fijamente con los ojos semi-cerrados:"

    ne "[protname],"

    extend " bésame."

    n "Acercas tus labios a los suyos mientras te abraza con ímpetu"

    n "Sus piernas se agarran a tus nalgas y te presiona hacia ella"

    n "para que detengas el movimiento del vaivén"

    n "y tu polla permanezca completamente en su interior."

    n "Sientes el calor de su cuerpo desnudo contra el tuyo,"

    n "su beso apasionado,"

    n "su ardiente carne asfixiando tu palpitante polla."

    ne "¡Ugh!"

    n "Repentinamente se aleja de ti y libera tus nalgas."

    ne "¡¡Para,"

    extend " para!!"

    p "Si no estoy haciendo nada..."

    ne "No..."

    ne "¡Aparta aparta!"

    p "..."

    # CHOICE you can make her cum here and BAD ENDING. #It can be chosen later...

    menu:

        "<Obedecerla y apartarte>":
            call p_Help

            jump day06_neusAlone_uncuff_sex_SecondRound_stop

        "<Desobedecerla y aumentar el ritmo de tus embestidas>":
            call p_Help
            
            jump day06_neusAlone_uncuff_sex_SecondRound_continue

label day06_neusAlone_uncuff_sex_SecondRound_stop:

    n "Haces el intento de apartarte,"

    n "cuando sientes sus fuertes manos agarrándote de los brazos para impedírtelo."

    ne "Para,"

    extend " para..."

    p "¿En qué quedamos?"

    ne "Dios..."

    ne "No te muevas,"

    extend " por favor..."

    ne "Ha sido una mala idea..."

    ne "Maravillosa..."

    ne "pero terrible..."

    p "¿Estás a...?"

    ne "¡Síiii...!"

    ne "No te muevas por favor..."

    p "¿Quieres que la saque?"

    ne "No,"

    extend " no,"

    extend " no..."

    ne "es mejor que note muevas..."

    ne "¡Joder!"

    ne "¡¿Por qué demonios tu polla tiene que palpitar tanto?!"

    p "¿Qué hago?"

    ne "Shhh..."

    ne "Deja que me concentre..."

    n "Mantiene sus ojos cerrados con el ceño fruncido y mordiéndose el labio."

    $ day06_neusAlone_uncuff_sex_SecondRound_stop2_beauty = False
    $ day06_neusAlone_uncuff_sex_SecondRound_stop2_grin = False

    menu day06_neusAlone_uncuff_sex_SecondRound_stop2_question:

        "Eres preciosa." if not day06_neusAlone_uncuff_sex_SecondRound_stop2_beauty:
            call p_Help

            $ day06_neusAlone_uncuff_sex_SecondRound_stop2_beauty = True

            if day06_neusAlone_uncuff_sex_SecondRound_stop2_grin:

                ne "Que hace expresiones raras... ¿No?"

                p "Así es."

                ne "Idiota..."

                p "Lo digo en serio."

                ne "Ahora no..."

            else:

                ne "¡AHORA NO!"

                ne "¡SSSHHH....!"

            ne "Cállate unos segundos,"

            extend " por favor..."

            jump day06_neusAlone_uncuff_sex_SecondRound_stop2_question

        "Estás haciendo una mueca algo extraña.":
            call p_Help

            $ day06_neusAlone_uncuff_sex_SecondRound_stop2_grin = True

            if day06_neusAlone_uncuff_sex_SecondRound_stop2_beauty:

                ne "¡Pero si me acabas de decir que soy preciosa!"

                p "Una cosa no quita la otra."

                ne "..."

                ne "Serás tonto..."

            else:

                ne "..."

                ne "Tonto..."

        "<Obedecerla y quedarte quieto>":
            call p_Help

            jump day06_neusAlone_uncuff_sex_SecondRound_stop2_label

        "<Desobedecerla y aumentar el ritmo de tus embestidas>":
            call p_Help
            
            jump day06_neusAlone_uncuff_sex_SecondRound_continue

label day06_neusAlone_uncuff_sex_SecondRound_stop2_label:

    n "Obedeces su orden y permaneces quieto y en silencio."

    n "Permanece con los ojos cerrados y su cuerpo completamente inmóvil."

    ne "*Sniiiiff...*"

    n "Inhala aire vigorosamente,"

    ne "*Uuuufff...*"

    n "para finalmente exhalarlo."

    n "Repite varias veces esta acción mientras te mantienes a la espera."

    ne "Hmmm..."

    ne "Vale..."

    ne "Creo que ya me he tranquilizado."

    n "Cuando separa sus párpados,"

    n "aún ves algo de brillo en sus ojos."

    ne "Despacio,"

    ne "ve sacándola muy despacio."

    n "Obedeces, y lentamente,"

    n "vas sacando tu -aún erecta y palpitante- polla de su estrecho y ardiente interior."

    ne "Hmmm..."

    p "¿Voy bien?"

    ne "Sí..."

    extend " sí...."

    with vpunch
    ne "¡Espera espera!"

    p "..."

    ne "Jodeeer..."

    ne "¡¿Por qué coño la tienes tan grande?!"

    p "..."

    if day06_neusAlone_uncuff_sex_FirstOrgasmApologie:

        ne "Lo-"

        extend "lo siento..."

    else:

        p "La tengo así de nacimiento."

        ne "Ya..."

        ne "Ughmm..."

    ne "Te-"

    extend "te prometo que lo intento,"

    ne "pero es que..."

    extend " es jodidamente enorme..."

    menu:

        "Ya te pareces a Dídac hablando así.":
            call p_Help
            $pl.ch_pts("np",1)

            ne "..."

            n "Su expresión no es demasiado amigable."

            n "Luego se dirige su mirada hacia abajo."

            ne "Hmm..."

            ne "Compararme con Dídac,"

            ne "no ha sido tan mala idea."

        "...":
            call p_Help

    ne "Muévete,"

    ne "pero hazlo despacio..."

    p "No puedo ir más despacio."

    ne "Inténtalo..."

    n "Tratando de apartarte lo más lentamente que te resulta posible,"

    n "desplazas tus caderas hacia atrás"

    n "mientras ella sigue intentando mantener la respiración controlada a medida que te alejas,"

    n "hasta que finalmente."

    with hpunch
    ono "flop"

    ne "Aahhh..."

    n "De sus labios sale un longevo suspiro."

    p "¿Estás mejor?"

    ne "Un poco..."

    ne "Pensaba que no lo conseguiría."

    ne "Realmente logras volverme loca, [protname]."

    p "Gracias."

    ne "Me alegro que te lo tomes como un cumplido,"

    ne "pero ni se te ocurra tomártelo a broma."

    ne "Si hubiera llegado a tener ese orgasmo..."

    # CHOICE?

    menu:

        "Siempre podríamos escapar, como hicimos ayer.":
            call p_Help

            p "Siempre podemos escapar,"

            p "como hicimos ayer."

            ne "No."

        "Tu padre no me causa ningún temor.":
            call p_Help

            ne "Espero que lo digas en broma."

            p "No, lo digo muy en serio."

            p "Estoy seguro que podríamos derrotarlo si le plantásemos cara."

            n "Sientes su mano acariciando tu mejilla"

            n "y con un rostro serio y preocupado:"

            ne "Ni se te ocurra volver a repetir semejante tontería."

            p "¿Por qué le tienes tanto miedo?"

            ne "Solo en pensar en él, ya corro el riegos de que logre entrar en mi mente, especialmente hoy."

            p "Entonces le combatiríamos."

            ne "No sé si eres valiente,"

            extend " estúpido,"

            ne "o sencillamente no has entendido nada de lo que te he explicado sobre él."

            ne "Ni si quiera podríamos escapar de él si tuviera un orgasmo."

        "Entonces suerte que no has tenido ningún orgasmo.":
            call p_Help

            ne "Sí..."

            ne "Suerte..."

            call WIP
            # NOT FINISHED

            jump gameover

        "...":
            call p_Help

            call WIP
            # NOT FINISHED

            jump gameover


label day06_neusAlone_uncuff_sex_escape:

    p "¿Por qué no?"

    ne "Porque a estas horas todas mis hermanas estarán reunidas en un mismo lugar junto a Padre."

    ne "Porque hoy es el solsticio de verano."

    p "Pero tampoco creo que vaya a tener tanto poder..."

    ne "¿Crees que soy débil?"

    menu:

        "No, para nada.":
            call p_Help

            p "No,"

            extend " para nada."

            jump day06_neusAlone_uncuff_sex_solsticeExplanation

        "Quizás no eres tan poderosa como crees.":
            call p_Help
            #$pl.ch_pts("np",-1)

            n "Sus ojos brillan con intensidad de nuevo,"

            n "y sientes tu cuerpo completamente inmóvil."

            ne "¿De verdad?"

            ne "Si ahora cogiera un cuchillo y te degollara con él."

            n "Sientes que te va faltando el oxígeno."

            ne "¿Qué es lo que harías para evitarlo?"

            p "Ughhh..."

            n "Ni siquiera eres capaz de articular una palabra."

            p "AAAaahhh-aaahhh..."

            n "Finalmente te libera de la presión que sentías en tu garganta"

            n "y eres capaz de volver a mover tu cuerpo."

            ne "Lo siento."

            ne "Lamento haberte hecho pasar por esto."

            ne "Pero quiero que lo entiendas."

            ne "Apenas soy capaz de aguantar así unos segundos,"

            ne "pero cuando tenía los ojos rojos,"

            ne "cuando no me tenía que preocupar para ahorrar energía,"

            ne "cuando poseo todo mi potencial..."

            if p_ao_started:

                ne "Lo que viste ayer después de que me desobedecieras y me dieras ese orgasmo,"

                ne "es solo un mero espejismo de lo que soy capaz de hacer."

            else:

                ne "Puedo hacer cosas que apenas eres capaz de imaginar."

            p "..."

            ne "¿Sigues pensando que soy débil?"

            p "..."

            jump day06_neusAlone_uncuff_sex_solsticeExplanation

        "...":
            call p_Help

            jump day06_neusAlone_uncuff_sex_solsticeExplanation

label day06_neusAlone_uncuff_sex_solsticeExplanation:

    ne "Pues créeme cuando te digo que estoy en mi peor momento."

    p "¿Y qué...?"

    ne "Durante el solsticio de verano y de invierno,"

    ne "no solo es capaz de controlar mi poder y mi cuerpo a su antojo,"

    ne "si no el de todas nosotras,"

    ne "al mismo tiempo."

    p "..."

    ne "Hasta las criaturas más oscuras, siniestras y poderosas que he llegado a conocer,"

    ne "le tienen respeto a Padre estos dos días."

    p "¿A qué tipo de criaturas te refieres?"

    ne "..."

    ne "Las llamo criaturas,"

    ne "por no llamarlas deidades."

    menu:

        "¿Y si es tan poderoso, cómo estás tan segura que no nos encontrará?":
            call p_Help

            ne "Si no consiguió encontraros a mamá y a ti durante más de veinte años,"

            ne "es porque tampoco es {a=https://es.wikipedia.org/wiki/Omnipotencia}todopoderoso{/a}."

        "...":
            call p_Help

label day06_neusAlone_uncuff_sex_gettingDarker:

    n "Ves que se fija en la ventana."

    p "¿Qué ocurre?"

    ne "Ha oscurecido del todo."

    p "¿Y eso es malo?"

    ne "Sí,"

    extend " lo es..."

    ne "Necesito que te corras cuanto antes."


###
label day06_neusAlone_uncuff_sex_neusGetsOver:

    p "Ouch!"

    n "Sientes que te tira sobre la cama de un empujón."

    p "¡¿Y esto a qué ha venido?!"

    ne "Está claro que no es buena idea que me sigas follando,"

    ne "así que es mejor que te saque el esperma con mi lengua."

    p "No hace falta,"

    p "te prometo que esta vez iré con más cuidado."

    ne "¿Es que no lo entiendes?"

    ne "Soy yo la que no ha sabido controlarse."

    $ day06_neusAlone_uncuff_sex_neusFuckingYou = "blowjob"

    menu:

        "Dame otra oportunidad.":
            call p_Help

            p "Dame otra oportunidad."

            ne "Ni hablar."

            menu:

                "¿Y si me montas tú?":
                    call p_Help

                    ne "..."

                    p "Te prometo que no me moveré,"

                    p "como si estuviera esposado."

                    ne "..."

                    if day06_neusAlone_uncuff_you_Sex_Pos == "anal":

                        ne "Pero esta vez será por delante."

                        menu:

                            "Me parece bien.":
                                call p_Help
                                $pl.ch_pts("np",1)

                            "Preferiría por detrás.":
                                call p_Help
                                $pl.ch_pts("np",-1)

                                ne "Entonces yo prefiero usar mi boca."

                                menu:

                                    "¿Pero no llegarás al orgasmo antes por por delante que por detrás?":
                                        call p_Help

                                        ne "Tengo mayor control ahí que en mi {a=https://es.wikipedia.org/wiki/M%C3%BAsculo_esfínter_externo_del_ano}esfínter{/a}."

                                        ne "Es mi coño,"

                                        extend " o mi boca."

                                        ne "Elige."

                                        menu:

                                            "Lo que tú prefieras.":
                                                call p_Help
                                                $pl.ch_pts("np",1)

                                                ne "..."

                                            "Prefiero tu empapado coño.":
                                                call p_Help
                                                $pl.ch_pts("np",1)

                                                $ day06_neusAlone_uncuff_sex_neusFuckingYou = "ride"

                                                ne "..."

                                                ne "Tontín..."

                                            "Prefiero tu boca.":
                                                call p_Help

                                                ne "Te aseguro que no te arrepentirás."

                                    "Como quieras.":
                                        call p_Help

                                    "...":
                                        call p_Help

                                jump day06_neusAlone_uncuff_sex_herAction

                    ne "Solo si me prometes que no te reprimirás cuando tengas ganas de correrte."

                    menu:

                        "Te lo prometo.":
                            call p_Help
                            $pl.ch_pts("np",1)

                            $ day06_neusAlone_uncuff_sex_neusFuckingYou = "ride"

                            ne "De acuerdo..."

                        "Eso no te lo puedo prometer.":
                            call p_Help

                            $pl.ch_pts("np",-1)

                            ne "Entonces no me dejas alternativa."

                "Como quieras.":
                    call p_Help

        "Como quieras.":
            call p_Help

            ne "Gracias por entenderlo."

        "...":
            call p_Help

label day06_neusAlone_uncuff_sex_herAction:

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Con ternura, desciende por tu cuerpo dándote pequeños besos por tu desnuda piel,"

        n "lamiéndote el pezón, acariciando tus muslos,"

        n "hasta que sientes su aliento cerca de tu aún erecto miembro viril."

    else:

        n "Sientes la presión de su mano sobre tu pecho mientras se incorpora para ponerse de pie."

        n "Sus nalgas se posan sobre tus muslos"

        n "y acerca su ombligo a tu erecta, rojiza, y sensible polla."

    ne "Me alegro que siga estando bien dura..."

    p "..."

    ne "Antes estuviste a punto de correrte,"

    ne "¿verdad?"

    menu:

        "Es posible...":
            call p_Help

        "Sí.":
            call p_Help
            $pl.ch_pts("np",1)

            ne "Te agradezco la sinceridad."

            ne "Pero..."

        "No.":
            call p_Help
            $pl.ch_pts("np",-1)

            ne "Mentiroso."

            p "..."

    ne "Como no te corras esta vez,"

    ne "voy a tener que usar otro método que no te va a gustar."

    ne "Así que córrete,"

    ne "¿de acuerdo?"

    p "¿Otro método?"

    ne "No lo quieres saber."

    pt "A veces da cierto miedo..."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Usa su longeva y ardiente lengua para acariciar la parte interior de tu rosado glande"

        n "mientras te dedica una mirada pícara y lasciva."

    else:

        n "Vuelve a levantarse y posa su cálido sexo cerca de la cima de tu palpitante polla,"

        n "acariciando su carne contra la sensible piel de tu glande."


    # CHOICE?

    menu:

        "Pensaba que me la ibas a chupar, no a lamer." if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":
            call p_Help

            ne "Que impaciente eres cuando quieres..."

        "Pensaba que me ibas a follar, rozarla con tus labios vaginales." if day06_neusAlone_uncuff_sex_neusFuckingYou == "rides":
            call p_Help

            ne "¿Tienes prisa?"

            p "¡Eres tú la que ha dicho que ya está oscuro!"

            ne "Hmmm..."

        "Te gusta ser juguetona...":
            call p_Help

            ne "¿Es una pregunta?"

            p "No."

    ne "Me gusta ponerte cachondo,"

    ne "no te lo voy a negar."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Desciende su rostro introduciéndose la punta de tu miembro entre sus labios"

        n "mientras desliza su lengua alrededor del glande"

        n "Su boca está ardiendo y su lengua no es menos,"

        n "a pesar del ligero dolor que sufres, sigue resultándote bastante placentero."

    else:

        n "Desciende levemente sus caderas introduciéndose solo la punta."

        n "Su sexo está ardiendo y su carne se arropa a ella de un modo extraño, pero placentero."

    ne "Realmente es enorme..."

    p "Eso ya me lo has dicho."

    ne "Es que sigue pareciéndome maravillosa..."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Paulatinamente, sigue descendiendo"

        n "hasta que la mitad de tu polla desaparece en su ardiente interior."

        n "Su lengua se remueve a lo largo y ancho de tu falo"

        n "mientras sientes la carne de su garganta pulsando"

        n "a distinto ritmo que el de tu polla,"

        n "como si fuera el latido de un corazón."

    else:

        n "Paulatinamente, sigue descendiendo sus caderas"

        n "ahogando tu polla en su estrecha carne"

        n "hasta que la mitad de tu miembro desaparece en su ardiente interior."

    ne "Hmmm..."

    n "Te fijas en su rostro donde ves que vuelve aparecer -levemente-, ese brillo en sus ojos."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "¿Con solo chupármela se está poniendo así de cachonda?"

    n "Sin darte tiempo a responder, vuelve a ascender para luego volver a bajar."

    pt "Joder..."

    # GOING DEEPER than half.

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Sintiendo la presión de su tráquea a través del esófago"

        n "que se arropa con fervor y ardor a tu erecto miembro,"

        n "logra descender cada vez más en cada nuevo intento."

    else:

        n "Deslizando su ardiente carne por tu erecto miembro,"

        n "sintiendo el angustioso ardor de su sexo"

        n "que cada vez logra penetrar más profundamente."

    p "Ughh..."

    n "Tu polla vuelve a palpitar con la misma intensidad que hace escasos minutos."

    menu:

        "<Aguantar un poco más>":
            call p_Help

            jump day06_neusAlone_uncuff_sex_dontHoldBack

        "<Correrte>":
            call p_Help

            p "Uughh..."

            jump day06_neusAlone_uncuff_sex_closeCum
                # n "Acerca sus labios a tu oreja y te sussura:"
                # ne "Dámelo todo."


label day06_neusAlone_uncuff_sex_dontHoldBack:

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Detiene su movimiento bucal,"

        n "se aparte de tu polla,"

        n " y te mira con una expresión poco amistosa."

    else:

        n "Detiene el movimiento de sus caderas."

    ne "Ya te he dicho que no te aguantes."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Asciende por tu desnudo torso hasta acercarse a tu rostro"

    else:

        n "Inclina su cabeza acercando su rostro al tuyo"

    n "donde te besa suavemente en los labios."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        ne "Quiero tenerla entera en mi garganta,"

        ne "que mi nariz tope con tu ombligo,"

        ne "que derrames todo tu esperma directamente en mi estómago."

        n "Sugerentemente vuelve a descender por tu pecho, ombligo, entrepierna..."

        n "Hasta que sientes de nuevo tu polla arropada por su infernal y asfixiante garganta."

    else:

        ne "Quiero sentirla toda dentro de mi."

        n "Sientes la asfixiante carne de su sexo descender a lo largo de tu miembro."

    p "Hmmm..."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Hasta que sientes el ardor de sus labios cerca de tu ombligo."

        p "Uhhmm..."

        n "A pesar del dolor-placer que sufres, te fijas que en su rostro, su expresión no es precisamente de serenidad."

        n "Rápidamente aparta su rostro de tu entrepierna."

        ne "*¡Cough!{w=0.25}{nw}"

        extend " ¡Cough!{w=0.25}{nw}"

        extend " ¡Cough!*"

        menu:

            "¿Estás bien?":
                call p_Help

                if p_neus.blowjobDeep_done > 1:

                    ne "Ayer lo logré,"

                    ne "así que no dudes tanto de mi."

                else:

                    ne "Lo siento,"

                    ne "solo dame otra oportunidad."

            "...":
                call p_Help

    else:

        n "Hasta que sus nalgas topan contra tus muslos"

        n "y sus labios vaginales acarician la base de tu erecto y palpitante miembro."

        ne "Uhmmm..."

        p "Parece que te duele."

        if p_neus.vaginalDeep_received > 1:

            ne "Si entró ayer,"

            ne "también tenía que entrar hoy..."

        else:

            ne "Es solo cuestión de tiempo."

        n "Te acaricia la barbilla con sus suaves manos"

        n "y separa sus labios para juntarse con los tuyos en busca de tu lengua."

        n "Mueve sus caderas lentamente en círculos mientras sigue forzándose a bajar."

    ne "Ughhmm..."

    menu:

        "No hace falta que te esfuerces tanto.":
            call p_Help

            p "Tampoco pasa nada por que no entre entera."

            ne "Sí,"

            extend " sí hace falta..."

            ne "aunque me duela."

            if ((day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob" and p_neus.blowjobDeep_done > 1) or
                (day06_neusAlone_uncuff_sex_neusFuckingYou == "ride" and p_neus.vaginalDeep_received > 1)):

                ne "No te haces una idea de lo feliz que me sentí ayer"

                ne "al poder tenerla toda dentro de mi."

            else:

                ne "No te haces una idea de las veces que he soñado"

                ne "en poder sentirla toda dentro de mi."

                if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

                    if p_neus.vaginalDeep_received > 1:

                        ne "Y ahora le toca a mi garganta."

                    else:

                        ne "Aunque sea en mi garganta."

            p "..."

        "...":
            call p_Help

label day06_neusAlone_uncuff_sex_tryingDown:

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Vuelve a descender su rostro,"

        n "pero esta vez, ladeando su cabeza a medida que va profundizando en tu miembro"

        n "al mismo tiempo que desliza su lengua en círculos,"

        n "como si estuviera intentando imitar el movimiento de un torbellino,"

        n "subiendo y bajando lentamente."

    else:

        n "Sigue moviendo sus caderas en círculos,"

        n "pero esta vez intentando imitar más el movimiento de un torbellino,"

        n "subiendo y bajando lentamente."

    p "Hhhmm..."

    n "Tu polla sigue palpitando con ímpetu"

    n "y el familiar cosquilleo recorre de nuevo tu entrepierna."

    jump day06_neusAlone_uncuff_sex_closeCum


label day06_neusAlone_uncuff_sex_closeCum:

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Te mira con ojos de hembra en celo y sacándose la polla de nuevo:"

    else:

        n "Acerca sus labios a tu oreja y te sussura:"

    ne "Dámelo todo."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Sientes sus manos agarrándote con fuerza de las nalgas."

    else:

        n "Rápidamente se aparta de ti posando su mano sobre tu pecho y con sus pies sobre la sábana."

    p "¿Qué-"

    extend "qué estás...?"

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Introduce tu polla en su boca"

        n "y casi de una sentada,"

        n "la ves desaparecer en su interior"

        n "hasta que su nariz topa contra tu desnuda piel."

        pt "Jodeer..."

    else:

        n "Empieza a cabalgarte con rudeza introduciéndose todo tu miembro."

    pt "¡DIOS!"

    n "No estás seguro si su rostro es de dolor o de placer,"

    n "Pero eso no la detiene, más bien lo contrario,"

    n "tienes la sensación que aumenta el ritmo en cada nueva acometida."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Sientes tu miembro ahogado en medio de su abrasadora carne,"

        n "y experimentas algo extraño en lo profundo de su estómago,"

        n "como si fueran pequeñas lenguas que surgen de esas ardientes paredes digestivas"

        n "acariciando tu palpitante polla a lo largo del camino."

    else:

        n "Sientes tu miembro ahogado en medio de su abrasadora carne,"

        n "y experimentas algo extraño en lo profundo de su sexo,"

        n "como si fuera una lengua interina que busca lamer tu polla cada vez que llegas al fondo."

    n "Tus testículos vibran como nunca los habías sentido antes,"

    n "el flujo recorre tu entrepierna con tanta energía que te deja casi sin aliento"

    n "mientras tu polla palpita de tal modo que tienes la sensación de que literalmente van a explotar."

    with vpunch
    p "¡¡Uuughh!!"

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Estallas en su ardiente interior,"

        n "mientras esas extrañas lenguas interinas se agarran la sensible piel de tu miembro"

        n "acercándose a tu glande, relamiendo tu sensible piel,"

        n "cuando este explosiona todo su chorro directamente al vació de su sistema digestivo."

        n "En lo más profundo, experimentas que algo te succiona de un modo demencial,"

        n "como si su estómago quisiera,"

        n "no solo arrancarte las últimas gotas que pudieran quedar en tu miembro,"

        n "sino más bien, arrancártela de cuajo para que cayera en sus jugos gástricos."

    else:

        n "Estallas en su ardiente interior"

        n "mientras esa extraña lengua se arropa a tu glande relamiendo todo el chorro que derramas"

        n "como si fuera una aspiradora succionando todo cuanto sale de tu interior."

    p "Diooos..."

    if not day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Con un rápido movimiento,"

        n "desciende su rostro y te besa con pasión y desenfreno sin que seas capaz de hacer nada al respecto."

    n "Todos los músculos de tu cuerpo vibran con tanta intensidad que sientes que van a estallar."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Su rostro sigue ascendiendo y descendiendo sin compasión."

    else:

        n "Sus caderas siguen saltando sobre tu cuerpo sin compasión."

    n "Tu miembro sigue palpitando con energía,"

    n "aunque tienes la sensación de que ya no tienes más esperma en tus testículos."

    n "Te sientes pesado,"

    n "apenas eres capaz de mover las manos."

    n "Todo tu cuerpo está en ebullición"

    n "y tus músculos siguen palpitando descontroladamente."

    if day06_neusAlone_uncuff_sex_neusFuckingYou == "blowjob":

        n "Sus uñas se clavan en tus nalgas con tanta fuerza"

        n "que sientes el goteo de tu sangre empapando las sábanas."

        n "Su rostro engulle tu polla a una velocidad inhumana,"

        n "hasta el punto que su rostro se vuelve casi fantasmal."

        n "Su boca se vuelve ardiente como un horno a máxima potencia."

        n "A pesar de lo exhausta, destrozada y lamentable que tienes la polla,"

        n "y de que apenas sientes ya nada en ella, como si estuviera anestesiada"

        n "o como si ya no formara parte de tu cuerpo,"

        n "sigue dura como una piedra."

    else:

        n "Su ardiente torso sobre tu pecho y el apasionado beso que compartís,"

        n "te impiden respirar con normalidad."

        n "Sus caderas siguen embistiéndote sin cesar."

        n "En tu parte pélvica, apenas eres capaz de sentir nada,"

        n "y a pesar de que ella sigue cabalgándote salvajemente y sin compasión alguna,"

        n "tienes la sensación de que tu polla sigue estando dura como una piedra."

    n "Dolor."

    n "Es casi lo único que eres capaz de sentir."

    n "Tus ojos empiezan a ceder contra el cansancio."

    n "Hasta que al final solo ves oscuridad."

    jump day06_ending_NeusLove
        # p "Oye..."
        # p "¿Qué estás haciendo?"
        # ne "Se te está volviendo a poner dura..."
        # p "¿No puedes estarte quietecita unos minutos?"


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
## Pasive Sex - Neus Fucks you.


label day06_neusAlone_pasSex:

    $ day06_neusAlone_sex = "penetrated"

    call endtranslation

    ne "..."

    pt "¡¿Qué?!"

    ne "¿Te refieres a...?"

    p "Sí."

    ne "¿Tanto te gustó?"

    p "No te lo pediría si me hubiera disgustado."

    p "Aunque si puede ser,"

    p "preferiría que no fueras tan brusca..."

    pt "¡¿Me gustó?!"

    ne "¿Acaso no era tu primera vez?"

    p "Sí..."

    ne "..."

    ne "Bueno..."

    ne "Si es lo que te quieres,"

    ne "de acuerdo."

    pt "¡¿Quien está tomando decisiones por mi?!"

    ne "Aunque será mejor que no te acostumbres demasiado a ello."

    ne "Lamentablemente,"

    ne "para hacer surgir esto de mi entrepierna,"

    ne "necesito gran parte de tu esperma."

    ne "Y por desgracia no tienes corridas infinitas..."

#### Doggystyle or Missionary?

    n "Alarga sus brazos hasta una de tus esposadas muñecas."

    p "¿Qué haces?"

    ne "Tengo que cambiarte de postura."

    menu:

        "<Dejar que te folle a cuatro patas>":
            call p_Help

            jump day06_neusAlone_pasSex_start

        "<Pedirle que te folle cara a cara>":
            call p_Help

            $ day06_neusAlone_pasSex_pos_missionary = True

            p "¿No podrías hacerlo teniéndome de cara?"

            ne "..."

            ne "Supongo que sí..."

            jump day06_neusAlone_pasSex_start

label day06_neusAlone_pasSex_start:

    if not day06_neusAlone_pasSex_pos_missionary:

        ono "clic"

        n "Te libera la otra mano."

        n "A pesar de gozar de ese albedrío,"

        n "eres incapaz de moverte demasiado."

    n "Acerca su rostro al tuyo y te da un dulce, pero apasionado beso."

    n "desliza sus labios por tu mejilla,"

    n "para luego acercarse a tu cuello donde sientes su ardiente lengua."

    if day06_neusAlone_pasSex_pos_missionary:

        n "Sin prisas, se desplaza por tu clavícula hasta alcanzar tu pecho."

        n "Sufres el calor de su lengua en tu sensible pezón hasta que..."

        p "Auch."

        ne "No te quejes tanto..."

        n "Relame lo mordido mientras te mira con una mirada pícara y juguetona."

        n "Sin demorarse demasiado, sigue descendiendo por tus abdominales"

        n "besando cada uno de ellos con dulzura y tintes de lascivia."

        n "A la altura de la base de tu miembro, deja de descender,"

        n "pero sigue dándote besos en tu suave y delicada piel."

        n "Sientes pequeñas pulsaciones de sangre en tu entrepierna"

        n "que van levantando tu lastimado y rojizo miembro."

        n "Se acerca a él y le da un cariñoso beso en la punta."

        n "Desciende por él usando su lengua"

        n "mientras con su mano acaricia tus testículos."

    else:

        n "Sin prisas, se desplaza por tu clavícula hasta alcanzar tu hombro derecho."

        n "Sufres el calor de su lengua en tu sensible piel hasta que..."

        with hpunch
        p "¡Auch!"

        n "De un fuerte tirón voltea tu cuerpo y te encuentras mordiendo la almohada."

        n "Con sus manos te agarra de las caderas y levanta tu trasero al aire."

        n "Tus piernas tiemblan tanto que vuelves a caer sobre la sábana."

        ne "Hmmm..."

        ne "Parece que no tienes ni fuerzas para mantenerte a cuatro patas..."

        if p_neus.buttockSlaps_received > 1:

            ne "Hasta el culo lo tienes rojizo..."

            ne "¿Aún te duelen los azotes que te di ayer?"

            p "..."

            with vpunch
            p "¡Ouch!"

            ne "Unos cuantos más no te harán ningún daño."

        n "Sientes su aliento cerca de tus nalgas."

        p "¿Qué...?"

label day06_neusAlone_pasSex_cleanAss:

    n "Pasa sus labios por tu bolsa escrotal acariciándolos con dedicación."

    ne "Es delicioso poder hacer esto sin encontrarme pelos por en medio."

    ne "¿Sueles afeitártelos a menudo?"

    p "..."

    ne "jejeje"

    n "Una de sus manos se acerca al agujero que se esconde entre tus nalgas"

    n "y con cierta destreza, desliza uno de sus dedos por ese orificio carnoso."

    ne "Parece increíble que llegara a entrar por este agujerito tan pequeño,"

    ne "¿No te parece?"

    p "..."

    ne "Tendré que lubricártelo un poco."

    ne "Además,"

    ne "llevas todo el día sin ir al baño."

    p "Euh..."

    p "Espera,"

    extend " déjame..."

    p "Ughh..."

    ne "[protname],"

    extend " apenas eres capaz de mover un brazo,"

    ne "es obvio que no puedes ir al servicio."

    p "..."

    ne "Tranquilo,"

    extend " déjamelo a mi."

    n "Acerca sus labios a tu orificio trasero,"

    n "donde le da pequeños y tiernos besos"

    n "para luego sentir su lengua acariciando el carnoso anillo exterior."

    n "Paulatinamente, va introduciendo esa ardiente lengua en tu interior,"

    n "mientras una de sus manos se agarra a tu nalga derecha"

    n "y la otra sigue acariciándote los testículos con maestría."

    p "Hmm..."

    n "Su lengua se mueve en círculos mientras sigue hundiéndose lentamente en tu interior."

    n "Percibes que juguetea con la carne que envuelve tu cavidad anal,"

    n "haciéndote retorcer debido al cosquilleo y la incomodidad."

    n "Sientes su cálido aliento a través de tu sensible piel exterior"

    n "a medida que va profundizando en tu cavidad anal."

    p "Ughnmm..."

    n "Su lengua empieza a extenderse de forma inhumana,"

    n "hasta un punto en el que tu esfínter ha dejado de funcionar"

    n "y tienes la sensación de que vas a expulsar algo."

    p "[neusname]..."

    ne "Hhhghhmm..."

    n "Su tono de voz es sereno y calmado,"

    n "como si no le afectara demasiado lo que le has dicho,"

    n "sigue profundizando hasta el punto en que notas toda su lengua"

    n "penetrándote a la misma profundidad que ayer."

    n "La desliza serpentinamente removiéndote por dentro"

    n "en una sensación agridulce y extraña de placer y malestar"

    n "que no sabrías definir demasiado bien."

    p "Uuughhmm..."

    n "Hasta que finalmente percibes que vuelve del mismo modo"

    n "hasta regresar a su boca."

    p "Aahhhh..."

    ne "¿Mejor?"

    p "Euhh..."

    n "Sientes un vació en el estómago"

    n "junto a la perdida de necesidad de ir al baño."

    p "[neusname],"

    p "¿has hecho lo que creo que has...?"

    n "Oculta sus labios con su mano."

    ne "Dame un segundo,"

    extend " ahora vuelvo,"

    ne "espérame aquí."

    pt "Como si pudiera hacer otra cosa..."

    n "Se dirige a lo que parece ser el cuarto de baño de la habitación."

    p "..."

    ono "pum"

    n "Oyes que cierra la puerta y enciende el grifo."

    pt "¿Era necesario que lo volviera a hacer...?"

    if day06_neusAlone_pasSex_pos_missionary:

        n "Pocos minutos después reaparece con una sonrisa en sus labios."

    else:

        n "Girando incómodamente el cuello,"

        n "la ves de nuevo con una sonrisa en sus labios."

    ne "¿Me has echado de menos?"

    p "[neusname],"

    p "no hacía falta que hicieras esto..."

    ne "No queremos manchar las sábanas,"

    ne "¿verdad?"

    ne "Además,"

    ne "tenías mucho menos que ayer."

    p "..."

    n "Ves que te acerca su labios..."

    menu:

        "Supongo que te habrás lavado bien los dientes...":
            call p_Help
            $pl.ch_pts("np", -2)

            ne "..."

            ne  "¿Y qué crees que he ido a hacer?"

            ne "Pero tranquilo,"

            ne "si no quieres que te bese,"

            ne "no lo haré."

        "Si no te molesta, Preferiría que no me besaras ahora mismo.":
            call p_Help
            $pl.ch_pts("np", -1)

            ne "..."

            ne "Como quieras."

        "<Devolverle el beso>":
            call p_Help
            $pl.ch_pts("np", 1)

            n "Entremezcla su lengua con la tuya apasionadamente."

            n "A pesar del sabor fresco de la pasta de dientes,"

            n "hay algo que proviene de su aliento que huele algo distinto."

            ne "Hmmm..."

            ne "Me encanta como besas."

    p "..."

label day06_neusAlone_pasSex_afterClean:
    
    n "Vuelve acercar sus labios a tu orificio anal"

    n "dónde te ofrece un tierno beso en tu carnoso anillo."

    ne "Depiladito así, está delicioso."

    pt "Espero que esté hablando de mi trasero..."

    n "Vuelve a ponerse de rodillas ante ti"

    if day06_neusAlone_pasSex_pos_missionary:

        n "mientras te sigue sujetando las piernas al aire"

        n "y te observa con una expresión algo perversa"

        n "y ese intenso brillo en sus ojos."

    else:

        n "Vuelve a agarrarte de las caderas y te levanta de nuevo el trasero."

        n "Sin embargo esta vez, tus piernas no tiemblan tanto"

        n "ni tampoco cedes contra la gravedad."

        p "¿Euh...?"

        ne "Tranquilo,"

        ne "Mientras te estaba haciendo la limpieza,"

        ne "he aprovechado para darles un poquito de fuerza a tus piernas."

        ne "Al fin y al cabo, no solo tendrá que soportar el peso de tu cuerpo..."

        p "No..."

        p "No las puedo ni mover..."

        ne "Tampoco te hace falta."

        n "Sientes sus manos descender por tus piernas"

        n "y grácilmente te las separa aún más."

    p "¿Qué...?"

    n "Algo pequeño pero rígido acaricia tiernamente tu empapado orificio anal."

    ne "¿Estás listo?"

    pt "¡No!"

    pt "¡Por supuesto que no lo estoy!"

    pt "¡Ey!"

    pt "¿¡Por qué coño no estoy hablando?!"

    n "Sientes su diminuto objeto fálico penetrando con delicadeza tu -algo más dilatado- agujero anal"

    n "logrando entrar sin demasiada dificultad."

    n "Al introducírtelo por completo"

    n "percibes el ardor de sus caderas al tacto con tus nalgas y tus testículos."

    ne "He pensado que sería una buena idea empezar por algo pequeñín,"

    ne "a fin de cuentas, ayer no fue tan mala idea."

    p "Empezaste con algo pequeño,"

    p "pero..."

    ne "Sí,"

    extend " ya..."

    ne "quizás me pasé."

    ne "Cuando voy cachonda,"

    ne "pierdo un poco el control..."

    ne "Pero no puedes reprocharme de que no te lo advirtiera."

    p "..."

    if day06_neusAlone_pasSex_pos_missionary:

        n "Sientes que aparta ligeramente sus caderas"

    else:

        n "Sientes que se aparta ligeramente de tus nalgas"

    n "para luego volver a penetrarte con su diminuto miembro."

    n "A pesar de su reducido tamaño,"

    n "sigue tan ardiente como el resto de su cuerpo."

    n "Percibes que aumenta ligeramente el ritmo en cada nueva embestida."

    n "La ardiente y suave piel de su entrepierna"

    n "golpea cada vez con más dureza tus nalgas y testículos."

    ne "Hmmm..."

    if not day06_neusAlone_pasSex_pos_missionary:

        n "Tienes la sensación de que se aparta un poco y ladea la cabeza para mirarte la entrepierna."

    ne "Te iba a preguntar si te está gustando,"

    ne "pero,"

    ne "viendo la reacción que está teniendo tu polla,"

    ne "supongo que no hace falta."

    if day06_neusAlone_pasSex_pos_missionary:

        n "Al bajar tu mirada,"

    else:

        n "Al mirar entre tus piernas,"

    n "descubres con cierta sorpresa,"

    n "que tu polla está recuperando su erección en pequeños cañonazos."

    pt "¡¿Pero qué cojones?!"

    p "Auch..."

    ne "Lo siento,"

    ne "¿estoy siendo demasiado brusca?"

    menu:

        pt "Demasiado brusca..."

        "Desde luego, no tanto como ayer.":
            call p_Help

            ne "Ya te he pedido disculpas por eso,"

            ne "¿no?"

            menu:

                "Lo siento.":
                    call p_Help

                    $pl.ch_pts("np", 2)

                    ne "..."

                    ne "No..."

                    ne "Perdona."

                    ne "No debería habértelo dicho así..."

                    ne "Te prometo que intentaré ir más despacio."

                    jump day06_neusAlone_pasSex_slower

                "...":
                    call p_Help

        "No, tranquila, sigue cómo creas oportuno.":
            call p_Help
            $pl.ch_pts("np", 1)

            ne "..."

            ne "Gracias,"

            ne "Pero creo que debería controlarme un poco más."

            jump day06_neusAlone_pasSex_slower

        "Un poco sí.":
            call p_Help

            ne "..."

        "¡¿A ti que te parece?!":
            call p_Help
            $pl.ch_pts("np", -1)

            ne "¡Perdona!"

            ne "Pensaba que querías que te tratara como un perro."

            ne "Quizás me equivoqué..."

            p "..."

    ne "Perdona,"

    ne "intentaré ir más despacio."

label day06_neusAlone_pasSex_slower:

    n "Con tranquilidad, vuelve a mover sus caderas."

    n "Su extraño miembro viril sigue aumentando de tamaño."

    p "[neusname]..."

    ne "He dicho que empezaría con algo pequeño,"

    ne "pero no que me quedaría con ese tamaño."

    menu:

        pt "¿La volverá a tener tan grande como ayer?"

        "¿Es realmente necesario?":
            call p_Help

            ne "Me temo que sí..."

        "Creo que este tamaño ya es suficiente.":
            call p_Help

            ne "Me temo que no."

            ne "¿Acaso no lo entiendes?"

        "Fóllame.":
            call p_Help

            $pl.ch_pts("np", 2)

            ne "Hmm..."

            ne "Tus deseos son órdenes."

            jump day06_neusAlone_pasSex_gettingBigger

        "Hazme el amor." if gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", 1)

            ne "Sinceramente,"

            ne "me había imaginado la situación de otra manera,"

            ne "pero tampoco puedo decir que me disguste del todo."

            jump day06_neusAlone_pasSex_gettingBigger

    ne "Necesito que te corras,"

    ne "no que simplemente se te ponga dura."

label day06_neusAlone_pasSex_gettingBigger:

    if day06_neusAlone_pasSex_pos_missionary:

        n "Se acerca a tu mejilla y con un tono dulce te susurra al oído:"

    else:

        n "Sientes su barriga al tacto con tus nalgas y su cabeza acercándose a tu espalda"

        n "mientras te susurra:"

    ne "Te prometo que esta vez intentaré no hacerte tanto daño;"

    ne "a menos que me lo pidas,"

    ne "claro..."

    if day06_neusAlone_pasSex_pos_missionary:

        n "Agarrándote con fuerza de los tobillos"

    else:

        n "Reincorporándose y agarrándote con firmeza de las nalgas"

    n "acelera ligeramente el ritmo de sus embestidas."

    p "Ughhh..."

    if not day06_neusAlone_pasSex_pos_missionary:

        with hpunch
        p "¡Auch!"

        p "¿Hace falta?"

        if p_neus.buttockSlaps_received > 1:

            ne "Lo mismo te podría haber preguntado ayer..."

        else:

            ne "Con estas nalgas tan perfectas que tienes,"

            ne "no puedo evitarlo."

    p "Suerte que vas con cuidado..."

    if not day06_neusAlone_pasSex_pos_missionary:

        with hpunch
        p "¡Ouch!"

    ne "Dices que te hago daño,"

    ne "pero fíjate en cómo la tienes."

    n "Vuelves a fijarte ahí abajo y descubres, sin demasiada sorpresa,"

    n "que está tan dura y rojiza que hasta observas y percibes el ímpetu con el que palpita."

    ne "Cuanto más brusca soy,"

    ne "más dura se te pone."

    p "..."

    if not day06_neusAlone_pasSex_pos_missionary:

        with hpunch
        p "¡Auch!"

        ne "¿Lo ves?"

    ne "Al final pensaré que te gusta más recibir,"

    ne "que dar..."

    n "Su extraño miembro sigue creciendo."

    p "[neusname]..."

    ne "Sigue siendo más pequeña que la tuya."

    ne "Además,"

    ne "te está encantando,"

    ne "salta a la vista."

    $ day06_neusAlone_pasSex_faster_cond = False

####

    menu:

        "No te retengas y dame más duro.":
            call p_Help

            $ day06_neusAlone_pasSex_faster_cond = True

        "Ve con cuidado, por favor...":
            call p_Help

label day06_neusAlone_pasSex_goingOn:

    if day06_neusAlone_pasSex_faster_cond:

        ne "¿Estás seguro?"

        pt "¡¿Qué?!"

        ne "Como quieras."

        pt "¡¿Cuando he decidido esto?!"

        ne "Pero luego no me quejes..."

        ne "Aunque tampoco creo que te falte mucho para terminar..."

    else:

        ne "Por supuesto,"

        ne "tranquilo..."

        ne "De todos modos,"

        ne "no creo que te falte mucho para terminar."

    if day06_neusAlone_pasSex_faster_cond:

        pt "¡YO NO HE DECIDIDO ESTO!"

        ne "Como quieras..."

        if day06_neusAlone_pasSex_pos_missionary:

            n "Vuelves a ver ese brillo en sus ojos."

            p "¿Qué...?"

            n "Con rudeza,"

            n "no solo lleva tus piernas más arriba,"

            n "sino que con ello, eleva tu trasero y tu espalda de las sábanas"

            n "poniéndose de pie ante ti."

        else:

            n "Retira la polla de tu interior"

            n "y sientes sus manos no solo mucho más ardientes que antes,"

            n "sino que además, tienes la sensación de que están aumentando de tamaño."

            p "¿Qué...?"

            with vpunch
            p "¡Auch!"

            n "Te agarra tan fuerte de las nalgas"

            n "que sufres sus uñas clavándose en tu piel"

            n "mientras acerca de nuevo su extraño miembro;"

            n "algo más ardiente y sobre todo más grande."

            ne "Es hora de ponerse serios..."

            pt "Espera..."

            extend " ¡¿Qué?!"

    else:

        if day06_neusAlone_pasSex_pos_missionary:
            call WIP
            # NOT FINISHED

        else: ## Doggystyle SOFT
            call WIP
            # NOT FINISHED

    p "Ugh..."

    if day06_neusAlone_pasSex_faster_cond:

        if day06_neusAlone_pasSex_pos_missionary:

            n "Con tu cabeza soportando el peso de tu cuerpo y el de sus caderas contra ti"

            n "sumándole al cuello siendo asfixiado por tus pectorales,"

            n "te resulta difícil respirar con normalidad."

            ne "Espero que no te arrepientas..."

            n "Con su polla aún en tu interior, te dedica una sonrisa maliciosa"

            n "antes de volver a mover sus caderas usando la gravedad a su favor."

        else: ## Doggystyle Hard

            n "Sin prisas pero sin compasión, te mete la polla de golpe."

            with vpunch
            p "¡Uugh!"

            n "Sus caderas impactan con tanta rudeza en tus nalgas"

            n "que apenas eres capaz de articular palabra alguna."

            ne "Espero que no te arrepientas."

            with hpunch
            p "¡AUCH!"

            n "Te azota con tanta fuerza en la nalga,"

            n "que la sientes cómo si estuviera en carne viva."

            ne "Te gusta que te azote,"

            ne "¿Verdad?"

            with hpunch
            p "¡Ouch!"

            n "Vuelve a embestirte con vigor metiéndotela entera de nuevo,"

            n "sufriendo el hueso de sus caderas clavándose en tus nalgas."

            pt "Dios..."

            ne "Dime,"

            ne "¿Quién es mi dulce perrito?"

            with hpunch
            ono "SLAP"

    else:

        if day06_neusAlone_pasSex_pos_missionary:
            call WIP
            # NOT FINISHED

        else: ## Doggystyle SOFT
            call WIP
            # NOT FINISHED

    n "Sientes su polla crecer en tu interior."

    if day06_neusAlone_pasSex_faster_cond:


        n "Con salvajismo,"

        n "vuelve a embestirte con rudeza"

        n "mientras te agarras cómo puedes -y con apenas fuerza- en las sábanas,"

        n "soportando cada nueva arremetida"

        n "mientras recibes el enorme y ardiente pollón"

        n "que sigue creciendo en tu cavidad anal."

        # if day06_neusAlone_pasSex_pos_missionary: # NOT NECESSARY
        # else: ## Doggystyle Hard

    else:

        if day06_neusAlone_pasSex_pos_missionary:
            call WIP
            # NOT FINISHED

        else: ## Doggystyle Hard
            call WIP
            # NOT FINISHED

    pt "No..."

    n "Sientes tu polla palpitar con energía y un cosquilleo recorre tu entrepierna."

    p "Ugh..."

    if day06_neusAlone_pasSex_faster_cond:

        ne "¿Te gusta que te trate así?"

        if day06_neusAlone_pasSex_pos_missionary:

            n "Como si fueras mi objeto sexual..."

        else: ## Doggystyle Hard

            n "Como si fueras mi perrita en celo..."

    else: # SLOW

        if day06_neusAlone_pasSex_pos_missionary:
            call WIP
            # NOT FINISHED

        else: ## Doggystyle SOFT
            call WIP
            # NOT FINISHED

    p "Ughhhm..."

    n "Tus testículos se remueven y sientes el flujo que recorre tu entrepierna."

    ne "¡No!"

    extend " ¡No!"

    ne "¡Espera!"

    ne "¡No te corras aún!"

    if not day06_neusAlone_pasSex_pos_missionary:

        n "Alarga rápidamente su mano entre tus piernas posando sus dedos sobre la punta de tu polla."

    elif not day06_neusAlone_pasSex_faster_cond and day06_neusAlone_pasSex_pos_missionary:

        n "Inclina rápidamente su cabeza introduciendo la punta de tu miembro en ardiente boca."

    ono "spuuurtt"

    if day06_neusAlone_pasSex_faster_cond and day06_neusAlone_pasSex_pos_missionary:

        n "Un enorme chorro de esperma fluye directamente hasta tu cara y tu pecho"

        n "empapándote a ti mismo con tu propio líquido blanco."

        ne "Mierda..."

    elif not day06_neusAlone_pasSex_pos_missionary:

        n "Un enorme chorro de esperma fluye directamente sobre su mano empapándola por completo"

        n "mientras algunas gotas se deslizan por su brazo hasta terminar cayendo sobre la sábana."

    else:

        n "Un enorme chorro de esperma fluye directamente en el interior de su ardiente boca."


label day06_neusAlone_pasSex_after:

    with vpunch
    p "¡Ugh!"

    if day06_neusAlone_pasSex_faster_cond and day06_neusAlone_pasSex_pos_missionary:

        n "Al liberarte las piernas, tu cuerpo se desploma sobre la cama."

        n "Sientes su desnudo y cálido pecho sobre el tuyo"

        n "mientras una ardiente, húmeda, y áspera lengua se desliza por una de tus mejillas."

        menu:

            "<Lamer tu propio esperma>":
                call p_Help

                n "Desplazas tu lengua por tus labios saboreando tu propia -y aún algo cálida- semilla."

                n "Su lengua se detiene."

                n "Se aparta y te mira con una mirada algo confusa."

                ne "..."

                pt "¡¿Pero qué cojones acabo de hacer?!"

                ne "[protname]..."

                ne "¿Has hecho lo que me ha parecido que has hecho?"

                pt "¡Eso me pregunto yo!"

                n "Sin mediar otra palabra,"

                n "se acerca a tus labios besándote apasionadamente"

                n "mientras su ardiente y áspera lengua hurga minuciosamente en la tuya"

                n "tanto por encima como por debajo"

                n "para luego desplazarla hacia dentro,"

                n "más allá de la amígdala."

                p "Uuughhhh..."

                n "Por momentos, sientes que te falta el aire."

                n "Finalmente la retira."

                ne "Si lo que querías es que te besara,"

                n "solo tenías que pedírmelo."

                ne "Pero si en realidad lo que deseas es degustar el sabor de una corrida masculina,"

                ne "hay otras maneras de hacerlo."

                if not DidacPregnant:

                    ne "Podríamos pedirle a Dídac, una vez se recupere,"

                    ne "que participara con nosotros"

                    ne "y que te follara ese trasero tuyo que tanto te gusta que sodomice"

                    ne "para luego pedirle que se te corra en la boca."

                    ne "O incluso otro día podría seducir a un hombre por la calle"

                    ne "o en algún lugar de ambiente"

                else:

                    ne "Algún día podría salir por la noche y seducir un hombre por la calle,"

                    ne "o en algún lugar de ambiente,"

                ne "para traerlo a casa y veas como me folla como a una perra ante tus narices"

                ne "y finalmente pedirle que se te corra en la boca."

                ne "Si te portas bien podría incluso convencerle para que que te folle a ti también,"

                ne "ya que veo que te gusta tanto..."

                pt "¡¿Pero qué está diciendo?!"

                ne "No me importa,"

                ne "de verdad."

                ne "En realidad es algo que me pondría bastante cachonda,"

                ne "no voy a negártelo..."

                if gensex_ILoveYouNeus:

                    ne "Sé que me amas"

                    ne "y para mi eso es suficiente."

                elif gensex_YoureAMonster:

                    ne "Sé que piensas que soy un monstruo,"

                    ne "pero está claro que esto te pone tan caliente como a mi."

                else:

                    ne "Mientras lo disfrutes,"

                    ne "yo lo disfrutaré aún más."

                ne "Pero hay algo que quiero dejarte bien claro."

                n "Su tono de voz se enfría y su rostro abandona todo atisbo de sonrisa."

                ne "Ni se te ocurra volver a hacer esto,"

                ne "NUNCA MÁS."

                ne "Tu esperma es para mi,"

                extend " y SOLAMENTE para mi."

                ne "¿Me has entendido?"

                p "..."

                if p_neus.cumReceived in ["buttocks", "stomach"]:

                    menu:

                        pt "Ni una sola gota..."

                        "¿Entonces por qué ayer no tuviste reparos en que te limpiara el trasero?" if p_neus.cumReceived == "buttocks":
                            call p_Help

                            call day06_neusAlone_pasSex_after_cumSwallow

                        "¿Entonces por qué ayer no tuviste reparos en que te limpiara la barriga?" if p_neus.cumReceived == "stomach":
                            call p_Help

                            call day06_neusAlone_pasSex_after_cumSwallow

                        "...":
                            call p_Help

                pt "A veces da un poco de miedo..."

                ne "Por favor,"

                extend " entiéndelo."

                ne "Tu semen es demasiado valioso para desperdiciarlo de esta manera."

                n "Con una expresión algo apenada,"

                n "regresa a la misma mejilla que estaba embadurnándote con su lengua."

            "<No hacer nada>":
                call p_Help

                n "Esa misma lengua recorre tus labios -untados de esperma- impidiéndote articular palabra."

        n "Cuando te fijas en su rostro, ves en ella una expresión extraña,"

        n "como si fuera una bestia famélica que actúa por puro instinto."

        p "Ughh..."

        n "Con el afán de no descuidar ni una sola gota,"

        n "la desliza por tus párpados y cejas."

        n "Su saliva es tan ardiente y pegajosa"

        n "que apenas eres capaz de mantener los párpados separados."

        n "La desplaza incluso por dónde careces de pelo."

        n "Desciende de nuevo por tu otra mejilla,"

        n "deslizándola cariñosamente mientras sigues con la vista borrosa."

        n "Bajando hasta la barbilla, para luego dirigirse al cuello,"

        n "dónde no solo se limita a lamerte,"

        n "sino también a escurrir sus labios e incluso mordisquearte en ciertos momentos."

        n "Cuando llega a tu clavícula se detiene especialmente en el hoyo"

        n "dónde el esperma empieza a volverse más fluido."

        n "Finalmente sigue descendiendo hasta llegar a tu zona pectoral"

        n "dónde termina de relamer las últimas gotas que te habías derramado encima."

    elif not day06_neusAlone_pasSex_pos_missionary:

        ne "Hmm..."

        n "Con su mano y sus dedos empapados con tu esperma"

        n "sigue acariciándote dulcemente la polla."

        ne "Has tenido una buena corrida."

        ne "Parece que te gusta bastante que te de por el culo..."

        p "..."

        ne "Al final tendré que llamarte \"mi zorrita\"."

        n "Una aparentemente dulce risilla surge de sus labios."

        n "Sientes su mano a lo largo y ancho de tu polla embadurnándote con tu propio esperma,"

        n "mientras acerca la otra a tus lastimados testículos para acariciarlos afablemente."

        p "¿Qué haces?"

        ne "Shhh..."

        ne "Tranquilo."

        ne "Sé lo que me hago."

        n "Dirige sus empapados dedos cerca de tus testículos"

        n "donde su otra mano empieza presionarte enérgicamente tu bolsa escrotal"

        n "y con el índice y el pulgar a modo de anillo ahoga con viveza la base de tu mástil,"

        n "y con esa fuerte presión"

        n "empieza a ascender."

        p "Uughh..."

        n "Hasta alcanzar la punta del glande,"

        n "dónde logra sacar unas últimas gotas."

        n "Deshaciendo la forma de anillo, usa uno de esos dedos para acariciar esas gotas"

        n "logrando embadurnarte aún más la parte del glande."

        n "Oyes un ruido extraño que surge de sus labios"

        n "como si estuviera..."

        n "salivando."

        with hpunch
        p "¡Ouch!"

        n "Con un fuerte empujón voltea tu cuerpo haciendo que reposes tu espalda de nuevo sobre la sábana"

        n "unos centímetros alejado de dónde estabas."

        p "¿Qué...?"

        ne "Mucho mejor..."

        n "Con una mirada lasciva y famélica,"

        n "desciende su rostro hasta el trozo de tela dónde habían caído esas cuatro gotas"

        n "mientras mantiene el brazo empapado de esperma en el aire,"

        n "sorbiendo con fuerza con sus labios esa lastimosa tela."

        p "..."

        p "¿Hace falta?"

        n "Elevando su rostro, acerca su lengua al codo del empapado brazo"

        n "y mientras no te quita los ojos de encima:"

        ne "No hay ni una sola gota que se pueda considerar innecesaria."

        n "Desliza su longeva y áspera lengua a lo largo de su brazo hasta la muñeca,"

        n "sin dejar rastro de tu esperma en el recorrido que ha hecho por su piel."

        n "Regresa de nuevo al codo donde sigue el mismo movimiento varias veces"

        n "hasta que no deja ni el vestigio de tu semilla."

        n "Desliza su lengua por la palma de su mano"

        n "hasta alcanzar su dedo pulgar,"

        n "el cual se lo introduce en la boca,"

        n "lamiéndolo y chupando,"

        n "sin quitarte los ojos de encima,"

        n "con esa mirada lasciva y juguetona,"

        n "como si te lo estuviera haciendo a ti."

        n "Después de estar lamiéndolo por un tiempo longevamente innecesario,"

        n "se mueve al índice,"

        n "repitiendo exactamente el mismo proceso,"

        n "así sucesivamente hasta que termina limpiando todos y cada uno de sus dedos."

        n "Termina pasando su lengua por el dorso de su mano"

        n "como si fuera una gata en celo acicalándose."

        n "Se vuelve a poner a cuatro patas sobre tu entrepierna"

        n "sintiendo su aliento cerca de tus testículos"

        n "dónde tu frío esperma empieza a volverse mucho más líquido."

        n "Con su ardiente lengua, relame tus huevos uno por uno"

        n "asegurándose de que no termine cayendo ni una gota de nuevo sobre la sábana."

        n "Sin prisas, asciende por tu aún rojizo, sensible y erecto mástil,"

        n "sin apartarte esa felina mirada."

        pt "¡¿Cómo es posible que siga estando dura?!"

        n "Con devoción, asciende desde la base con su áspera lengua"

        n "usando además sus labios para sorber"

        n "y no abandonar ni un solo centímetro al descuido."

        n "Hasta que alcanza la cima dónde le dedica un tiempo especial"

        n "besándotela y sorbiéndola como si fuera un gustoso y dulce helado."

        n "Con la misma mano de antes,"

        n "vuelve a hacer el mismo procedimiento"

        n "uniendo su dedo índice y pulgar,"

        n "desde la punta hasta la cima."

        p "Uuughh..."

        n "La tienes tan sensible"

        n "que este procedimiento te resulta más doloroso que antes."

        n "Cuando finalmente llega a la punta,"

        n "ves en su rostro una expresión de decepción"

        n "al descubrir que apenas ha logrado sacar una mísera gota,"

        n "que no desperdicia y lame con interés."

        p "¡Ugh!"

        n "Con un movimiento brusco, hunde su rostro,"

        n "escondiendo la mitad de tu polla en su interior."

        p "[neusname]..."

        n "Finalmente se retira paulatinamente sin apartarte la mirada."

    else:

        # not finished revision ## YOU came at missionar in her mouth.

        n "Sientes sus labios acariciar tu sensible glande,"

        n "mientras su lengua acaricia la parte inferior de tu glande"

        n "al mismo tiempo que succiona con placer el líquido blanco que surge de tu interior."

        n "Su lengua se mueve frenéticamente en esa base"

        n "obsequiándote con un cosquilleo que logra sonsacar más esperma de tu interior,"

        n "el cual se desliza libremente por el interior de su garganta"

        n "en una sensación entre el dolor y un placer difícil de describir."

        n "Sigue desplazando su rostro verticalmente junto a sus labios y su lengua"

        n "en un carente esfuerzo por intentar lograr sacar más esperma."

        p "[neusname]..."

        n "Sin sacar el mástil de su boca,"

        n "separa sus labios y ves su lengua alargarse más de lo que es humanamente posible"

        n "acercándose a la base de tu polla."

        p "Ouch..."

        n "Con su dedo índice y pulgar formando un círculo te ahoga con fuerza la base de tu polla."

        n "Con esa misma presión, asciende lentamente a lo largo de tu mástil"

        n "hasta alcanzar el glande dónde sientes que logra sacar unas pocas gotas más."

        n "Con una expresión perturbadora y con ese brillo en sus ojos"

        n "lame esas últimas gotas como si fuera el mejor elixir que haya tomado en su vida."

        n "Vuelve a hundir su rostro, tragándose casi la mitad de tu miembro en su interior"

        n "succionándote aún con más energía para intentar socavar alguna otra gota."

        p "Uuughh..."

        n "Apenas eres capaz de mantener los ojos abiertos debido al dolor."

        n "Finalmente se aparta sin dejar de mirar con interés tu aún tensa y tersa polla."

    ne "Hmmmm...."

    n "Con un gemido ahogado,"

    n "regresa su lengua al interior de su boca"

    n "mientras se dibuja una expresión de gozo y satisfacción en su rostro."

##

    p "¿Estás bien?"

    ne "Mejor que nunca..."

    ne "No sabes lo mucho que adoro tu esperma."

    p "Me hago una idea..."

    ne "No."

    ne "Te aseguro que no te haces ni la más mínima idea..."

    n "Al fijarte en su entrepierna,"

    n "descubres que su polla ha desaparecido por completo."

    ne "Hmm..."

    ne "Lo siento,"

    ne "pero ya te he dicho que solo podía tenerla así por un tiempo limitado."

    ne "Ahora tendrás que conformarte con mi boca."

    p "¿Ahora?"

    p "¡¿Es que no me he corrido?!"

    ne "Sí,"

    extend " pero..."

    n "Vuelves tu vista hacia abajo y la descubres tan dura como antes."

    p "¡¿Qué?!"

    p "¡¿Cómo es posible?!"

    ne "{a=https://es.wikipedia.org/wiki/Mea_culpa_(expresión)}Mea culpa{/a}."

    ne "Digamos que he aprovechado el tiempo para..."

    ne "Intentar que pueda seguir dando un poco más de guerra."

    p "¿Por?"

    ne "Porque necesito tu esperma para Dídac,"

    extend " para Meritxell,"

    ne "y para mi."

    ne "Con una sola corrida no es suficiente."

    p "No creo que pueda aguantar tanto..."

    n "Te acerca los labios y te da un beso apasionado"

    n "en el que aún puedes percibir un extraño sabor."

    ne "Te sorprenderías..."

    p "..."
    
    n "Su rostro desciende y sientes sus labios en tu pecho,"

    n "bajando sutilmente por tus abdominales,"

    n "tu ombligo,"

    n "hasta alcanzar tu erecto miembro."

    n "Donde una lengua ardiente y juguetona"

    n "decide juguetear con tu rojizo y sensible miembro."

    p "Ughhm..."

    menu:

        "En lugar de tu boca, ¿por qué no me dejas hacerte el amor?" if gensex_ILoveYouNeus:
            call p_Help

            jump day06_neusAlone_pasSex_beforeBlowjob

        "En lugar de tu boca, ¿por qué no probamos por otro sitio?" if not gensex_ILoveYouNeus:
            call p_Help

            jump day06_neusAlone_pasSex_beforeBlowjob

        "Me encanta sentirla dentro de tu boca.":
            call p_Help

            ne "Me alegra decirte eso."

            ne "Aunque..."

            jump day06_neusAlone_pasSex_blowjob

        "...":
            call p_Help

            jump day06_neusAlone_pasSex_blowjob

label day06_neusAlone_pasSex_beforeBlowjob:

    ne "Sabes que me encantaría."

    ne "Pero he agotado demasiada energía para esto."

    ne "Si llegara a acercarme demasiado al orgasmo,"

    ne "sin poder usar mis poderes..."

    ne "El riesgo de que no fuera capaz de detenerme,"

    ne "es demasiado arriesgado."

    $ day06_neusAlone_pasSex_beforeBlowjob_power_cond = False

    menu day06_neusAlone_pasSex_beforeBlowjob_question:

        "¿De verdad necesitas de tus poderes para detenerte a ti misma?" if day06_neusAlone_pasSex_beforeBlowjob_power_cond == False:
            call p_Help

            $ day06_neusAlone_pasSex_beforeBlowjob_power_cond = True

            ne "No te haces una idea del placer que siento cuando llego al orgasmo."

            ne "Y mucho menos de lo loca que me vuelve tu polla..."

            ne "Así que no me juzgues tan a la ligera."

            jump day06_neusAlone_pasSex_beforeBlowjob_question

        "Vamos, no seas así, inténtalo.":
            call p_Help
            $pl.ch_pts("np", -1)

            ne "¿De verdad te crees que no me gustaría también?"

            ne "¿Acaso no entiendes el riesgo que supone que tenga un orgasmo?"

            ne "No te haces una idea de lo poderoso que puede llegar a ser Padre estos dos días al año."

        "Te ordeno que lo intentes.":
            call p_Help

            ne "..."

            ne "¿Me lo ordenas?"

            ne "Te acabo de follar el trasero sacrificando parte de mi energía porque me lo has pedido"

            ne "y ahora te me pones así?"

            menu:

                "Lo que llamas energía es mi esperma.":
                    call p_Help
                    $pl.ch_pts("np", -2)

                    ne "Y por lo visto,"

                    ne "sigues sin entender que no tienes corridas infinitas."

                    p "..."

                    ne "Entiéndelo,"

                    ne "es demasiado arriesgado."

                "Perdón, pensaba que te gustaría que me pusiera en plan dominante.":
                    call p_Help
                    $pl.ch_pts("np", 1)

                    ne "Después de haber sido tan pasivo conmigo,"

                    ne "el plan dominante no te pega tanto..."

                "Lo siento.":
                    call p_Help
                    $pl.ch_pts("np", 2)

                    ne "Hmm..."

                    ne "No pasa nada."

                "...":
                    call p_Help
                    $pl.ch_pts("np", -1)

        "¿Podrías intentarlo, por favor?":
            call p_Help

            ne "Me encantaría,"

            ne "te lo aseguro,"

            ne "pero como ya te he dicho,"

            ne "es demasiado arriesgado."

        "Es una lástima, pero lo entiendo.":
            call p_Help
            $pl.ch_pts("np", 1)

            ne "Gracias por comprenderlo."

        "...":
            call p_Help

    p "..."

    jump day06_neusAlone_pasSex_blowjob

label day06_neusAlone_pasSex_blowjob:

    n "Sus ojos se fijan en tu erecto pero venoso y rojizo miembro."

    ne "Me imagino que debe empezar a dolerte,"

    ne "mantenerla así de dura tiene su precio,"

    ne "especialmente después de que me hiciste hacer ayer."

    p "Lo dices como si te hubiese obligado..."

    ne "Te dije que si me llevabas al orgasmo,"

    ne "tendría sus consecuencias."

    p "¿Dejarme el culo hecho mierda no fue suficiente?"

    ne "Por lo que estoy viendo,"

    ne "ni siquiera te lo tomaste como un castigo."

    p "Pero..."

    n "Sin darte tiempo a responder,"

    n "hunde su rostro tragándose la mitad de tu polla en su ardiente interior."

    p "Dios..."

    n "Dando pequeños círculos,"

    n "asciende y desciende grácilmente con su lengua a lo largo de tu castigada polla."

    p "Tienes una boca infernal."

    ne "Me lo tomaré como un cumplido."

    n "Su lengua juguetea con la parte inferior de tu glande mientras te observa maliciosamente."

    n "Sus ojos brillan con leve intensidad,"

    n "pero los susurros que te envuelven aumentan en número y en volumen."

    n "Sus manos se acercan a tus testículos y de modo desenfadado empieza a acariciarlos suavemente."

    n "Sin meterse la polla en tu boca,"

    n "desciende sus labios mimándola con pequeños besos"

    n "hasta llegar cerca de tus testículos."

    n "Allí se detiene"

    n "y vuelve a usar su lengua para relamer la base de tu miembro viril"

    n "sin dejar de mirarte a los ojos."

    ne "¿Aún te duele?"

    p "No sabría decirte..."

    ne "Eso no es malo."

    p "Pero tu lengua está ardiendo."

    ne "Eso no puedo evitarlo."

    n "Vuelve a besarte la base de la polla"

    n "y sin ninguna prisa vuelve a subir con esos pequeños besos a lo largo del manubrio"

    n "de forma cariñosa y algo traviesa."

    n "Abriendo sus labios vuelve arroparte el glande."

    n "Te succiona con sutileza a la par que acaricia el orificio del glande con su ardiente lengua."

    n "Su rostro es sonriente y casi parecería inocente."

    n "Desciende de nuevo dando círculos y volteando su cabeza"

    n "como si estuviera devorando un helado famélicamente."

    n "Percibes que en cada nueva embestida no solo va aumentando más el ritmo,"

    n "sino que también intenta descender cada vez más."

    p "Ughh..."

    n "Desacelera mientras te mira con ojos curiosos."

    n "Un pequeño ruido gutural surge de su interior,"

    n "como si intentara sonreír con la boca llena."

    n "Vuelve a cerrar sus párpados y prosigue con su movimiento bucal,"

    n "aumentando paulatinamente el ritmo y acercando su aliento peligrosamente la base de tu miembro."

    n "A pesar del dolor, que prácticamente se está volviendo una tortura insoportable,"

    n "sientes el particular cosquilleo recorriendo tu entrepierna."

    p "Ughh..."

    n "Tu polla palpita con energía"

    n "a la par que percibes tu liquido blanco recorrer su camino con rudeza"

    n "hasta estallar en el interior de su garganta."

    n "En ese instante,"

    n "te agarra firmemente de las nalgas y hunde su rostro tragándose tu polla al completo,"

    n "impidiéndole seguir expulsando con normalidad,"

    n "dejándote en una sensación agonizante"

    n "junto con el dolor que ya padeces debido a lo sensible que la tienes."

    p "[neusname]...."

    n "Finalmente, se va apartando, sin prisas."

    n "A medida que tu polla recupera espacio"

    n "es capaz de seguir derramando esperma en su interior."

    pt "Dios..."

    pt "¡¿Qué narices...?!"

    n "Percibes pequeñas protuberancias tan húmedas y ardientes como la carne que te rodea"

    n "que parecen moverse por voluntad propia,"

    n "como si fueran diminutas lenguas que se encuentran a lo largo de su esófago,"

    n "acariciando y mimando tu sensible polla."

    n "A pesar de que el espasmo de tu corrida ha cesado y que ya no tienes nada más que ofrecer,"

    n "su movimiento bucal no cesa y esas extrañas lenguas se mueven con más intensidad."

    p "Uuughh..."

    n "Sientes que estas se juntan en la base formando un anillo,"

    n "oprimiéndote con tanta fuerza"

    n "que tienes la sensación que quieren ahogarte la polla."

    n "Con esa misma presión, descienden a lo largo de tu miembro hasta el orificio del glande,"

    n "dónde logran sacar unas últimas gotas de tu lamentable polla."

    p "[neusname]..."

    p "por favor..."

    n "A pesar de tus intentos,"

    n "sigue desplazando su rostro verticalmente"

    n "sintiendo esas diminutas lenguas acariciando tu miembro cada vez que se acerca a ellas."

    n "En lo profundo de su esófago sientes una enérgica succión,"

    n "tan fuerte, que tienes la sensación que en lugar de tu esperma,"

    n "lo que al final logrará es arrancártela de cuajo."

    p "Uuughh..."

    n "El dolor se vuelve tan insoportable que eres incapaz de mantener los párpados separados."

    ###

    p "¡[neusname]!"

    n "Finalmente se detiene."

    n "Sin prisas, sientes que te va liberando de la presión de su garganta."

###

    n "Su rostro es de gozo y satisfacción."

    p "Eughh..."

    ne "¿Estás bien?"

    p "Ughh..."

    ne "Supongo que debes estar agotado."

    ne "Descansa un poco,"

    ne "te lo mereces."

    n "Incorporándose a cuatro patas se acerca a ti"

    n "y desciende su desnudo cuerpo contra el tuyo,"

    n "apoyando su cabeza sobre tu pecho."

    ne "Tu corazón sigue latiendo con fuerza."

    p "Hmm..."

    n "Levanta de nuevo su cabeza y se acerca a tus labios."

    n "Con dulzura te roba un apasionado beso."

    n "Sugerentemente se aparta de ti"

    n "mientras te mira con sus brillantes y húmedos ojos."

    n "De sus mejillas, ves desprenderse una lágrima."

    jump day06_neusAlone_happy
        # p "¿Qué pasa?"
        # ne "Nada."
        # if not gensex_YoureAMonster:
        #     ne "Simplemente,"
        #     extend " soy feliz."
        # n "Desciende su cabeza hasta tu cuello"
        # n "y percibes su tierno abrazo mientras sientes la humedad de sus lágrimas en tu piel."

#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
## # YOU DID SOMETHING WITH OTHERS.


label day06_neusAlone_whereAreThey_preference:

    call endtranslation

    if gensex_ILoveYouNeus:

        $ ntlong += 1

        $ nteye = "right04"
        show n_closefromup_mouth sad_Silentx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        $ nteye = "front02"
        show n_closefromup_mouth sad_Silentx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        p "¿Qué...?"

        $ ntlong += 1

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx002
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Realmente llegué a pensar que me amabas."

        $ nteye = "front05"
        show n_closefromup_mouth sad_Silentx06
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        menu:

            "Por supuesto que te amo.":
                call p_Help
                $pl.ch_pts("np", 1)

                if not p_prot_NotJustMasturbate_with_p_neus:

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx08
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Cómo puedes amarme si te doy asco?"

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿De dónde sacas que me das asco?"

                    $ nteye = "right02"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows angryx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Ayer ni siquiera me dejaste tocarte."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Ya ni hablemos de hacerme el amor..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        "No quería hacerlo con prisas y a la fuerza, quería que fuera algo especial.":
                            call p_Help

                            $ nteye = "front04"
                            show n_closefromup_mouth sad_Silentx05
                            show n_closefromup_eyebrows suspiciousx02
                            call n_closefromup_tears_tears
                            with dissolve
                            
                            ne "..."

                            $ nteye = "front05"
                            show n_closefromup_mouth sad_Talkingx002
                            show n_closefromup_eyebrows surprisex01
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Algo especial..."

                            if p_prot_NotJustMasturbate_with_p_didac or p_prot_NotJustMasturbate_with_p_txell:

                                if p_prot_NotJustMasturbate_with_p_didac and p_prot_NotJustMasturbate_with_p_txell:
                                    $pl.ch_pts("np", -5)

                                    $ nteye = "front01"
                                    show n_closefromup_mouth sad_Talkingx08
                                    show n_closefromup_eyebrows angryx03
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    ne "Con ellas no necesitabas que fuera especial, ¿verdad?"

                                    $ nteye = "front00"
                                    show n_closefromup_mouth sad_Silentx02
                                    show n_closefromup_eyebrows surprisex04
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    p "Con ellas es distinto."

                                elif p_prot_NotJustMasturbate_with_p_didac:
                                    $pl.ch_pts("np", -2)

                                    $ nteye = "front01"
                                    show n_closefromup_mouth sad_Talkingx09
                                    show n_closefromup_eyebrows suspiciousx03
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    ne "Con Dídac no necesitaba que fuera especial, ¿verdad?"

                                    $ nteye = "front05"
                                    show n_closefromup_mouth sad_Silentx07
                                    show n_closefromup_eyebrows suspiciousx04
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    p "Con Dídac es distinto."

                                elif p_prot_NotJustMasturbate_with_p_txell:
                                    $pl.ch_pts("np", -3)

                                    $ nteye = "front02"
                                    show n_closefromup_mouth sad_Talkingx10
                                    show n_closefromup_eyebrows suspiciousx04
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    ne "Con Meritxell no necesitaba que fuera especial, ¿verdad?"

                                    $ nteye = "front05"
                                    show n_closefromup_mouth sad_Silentx06
                                    show n_closefromup_eyebrows angryx02
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    p "Con Txell es distinto."

                                $ nteye = "right04"
                                show n_closefromup_mouth sad_Talkingx005
                                show n_closefromup_eyebrows angryx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Ya..."

                            else:

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Silentx02
                                show n_closefromup_eyebrows surprisex01
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Con ellas no hice nada tampoco."

                                $ nteye = "right01"
                                show n_closefromup_mouth sad_Talkingx02
                                show n_closefromup_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Ya..."

                                $ nteye = "right02"
                                show n_closefromup_mouth sad_Talkingx05
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Pero aún así..."

                                $ nteye = "front08"
                                show n_closefromup_mouth sad_Talkingx04
                                show n_closefromup_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Si realmente te pusiera cachondo,"

                                $ nteye = "left04"
                                show n_closefromup_mouth sad_Talkingx03
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "no necesitarías darme este tipo de excusas."

                        "Ayer no me pareció el mejor momento.":
                            call p_Help

                            $pl.ch_pts("np", -1)

                            $ nteye = "front01"
                            show n_closefromup_mouth sad_Silentx02
                            show n_closefromup_eyebrows surprisex05
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            $ nteye = "front03"
                            show n_closefromup_mouth sad_Talkingx07
                            show n_closefromup_eyebrows angryx03
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿Esa es tu excusa?"

                            $ nteye = "front04"
                            show n_closefromup_mouth sad_Silentx06
                            show n_closefromup_eyebrows angryx04
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Es la verdad."

                            $ nteye = "right05"
                            show n_closefromup_mouth sad_Talkingx04
                            show n_closefromup_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Ya..."

                        "Lo siento.":
                            call p_Help

                            $ nteye = "front01"
                            show n_closefromup_mouth sad_Silentx02
                            show n_closefromup_eyebrows surprisex05
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx03
                            show n_closefromup_eyebrows sadx08
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Ya..."

                            $ nteye = "front06"
                            show n_closefromup_mouth sadbiting_Silentx10
                            show n_closefromup_eyebrows sadx09
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ nteye = "right03"
                            show n_closefromup_mouth sad_Talkingx03
                            show n_closefromup_eyebrows sadx05
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Yo también lamento no estar a la altura..."

                        "...":
                            call p_Help
                            $pl.ch_pts("np", -5)

                            $ nteye = "front01"
                            show n_closefromup_mouth sad_Silentx06
                            show n_closefromup_eyebrows sadx01
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ nteye = "right04"
                            show n_closefromup_mouth sadbiting_Silentx08
                            show n_closefromup_eyebrows sadx08
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ gensex_ILoveYouNeus = False

                else:

                    if p_prot_NotJustMasturbate_with_p_didac or p_prot_NotJustMasturbate_with_p_txell:

                        $ nteye = "front04"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                    else:

                        $ nteye = "front02"
                        show n_closefromup_mouth sadbiting_Silentx04
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                    ne "..."

                    if p_prot_NotJustMasturbate_with_p_didac or p_prot_NotJustMasturbate_with_p_txell:

                        $ nteye = "right02"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Ya..."

                    else:

                        $pl.ch_pts("np", 3)

                        $ nteye = "front04"
                        show n_closefromup_mouth happy_Talkingx03
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Gracias..."

            "...":
                call p_Help
                $pl.ch_pts("np", -5)

                $ gensex_ILoveYouNeus = False

                $ ntlong += 1

                $ nteye = "front08"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                n "Una lágrima empieza a derramarse por su mejilla."

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx08
                call n_closefromup_tears_tears
                with dissolve

                ne "Me imagino que soy más estúpida de lo que recordaba."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero gracias por recordármelo."

                $ nteye = "right02"
                show n_closefromup_mouth sadbiting_Silentx10
                show n_closefromup_eyebrows sadx09
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front06"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx08
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ ntlong = 0

    if p_prot_NotJustMasturbate_with_p_didac and p_prot_NotJustMasturbate_with_p_txell:

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "Supongo que preferirías su compañía a la mía..."

        if gensex_YoureAMonster:

            $ nteye = "right04"
            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Al fin y al cabo sigues considerándome un monstruo."

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "right04"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Aunque quizás preferirías también su compañía..."

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

    # NOT FINISHED

    return
        #p "..."
        #ne "¿Me he equivocado?"




#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
##


label day06_neusAlone_pasSex_after_cumSwallow:

    ne "Simplemente,"

    ne "porque te ordené que no te tragaras ni una sola gota."

    if p_neus_cumOut_swallow:

        ne "Y ya viste lo que te pasó cuando no me hiciste caso."

    else:

        ne "Ya viste que luego prácticamente no me dejé ni una gota."

    return

