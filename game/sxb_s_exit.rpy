default afternight04_LeavingSexBattle = False

label game_exit:

    hide screen premium_dashboard

    menu afternigh04_sexwithDidac_exit_question:

        pt "¿Estoy seguro que quiero dejar a Dídac así y terminar sin que me haya corrido las tres veces?"
        
        "<Decirle a Dídac que prefieres no seguir e ir a dormir>":
            
            call p_Help

            $pl.ch_pts("dp",-5)

            jump afternigh04_sexwithDidac_exit_choice

        "<Seguir>":
            
            call p_Help

            if PlatinumHelp:
                show screen premium_dashboard() 
            call screen dummy_screen()

            return

label afternigh04_sexwithDidac_exit_choice:

    #call Remove

    hide screen dummy_screen 
    hide screen premium_dashboard
    call afternigh04_sexwithDidac_RemoveAll_scene

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx02_a
        show afternight04_sexbattle_d_eyes 02_a
        show afternight04_sexbattle_d_pupils front02_a
        show afternight04_sexbattle_d_eyebrows suspiciousx01_a
        with dissolve

    d "¿Por qué paras?"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx03_a
        show afternight04_sexbattle_d_eyes 00_a
        show afternight04_sexbattle_d_pupils front00_a
        show afternight04_sexbattle_d_eyebrows surprisex01_a
        with dissolve

    p "Lo siento Dídac,"

    extend " pero creo que todo esto ha sido una mala idea."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx03_a
        show afternight04_sexbattle_d_eyes 00_a
        show afternight04_sexbattle_d_pupils front00_a
        show afternight04_sexbattle_d_eyebrows angryx01_a
        with dissolve

    d "¡¿Cómo?!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx06_a
        show afternight04_sexbattle_d_eyes 07_a
        show afternight04_sexbattle_d_pupils front07_a
        show afternight04_sexbattle_d_eyebrows angryx03_a
        with dissolve

    p "Creo que lo mejor es dejar esto y que nos vayamos a dormir."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx05_a
        show afternight04_sexbattle_d_eyes 04_a
        show afternight04_sexbattle_d_pupils front04_a
        show afternight04_sexbattle_d_eyebrows angryx04_a
        with dissolve

    d "Estás de broma..."

    extend " ¿Verdad?"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx04_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx04_a
        with dissolve

    p "No,"

    extend " lo digo muy en serio."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx07_a
        show afternight04_sexbattle_d_eyes 02_a
        show afternight04_sexbattle_d_pupils front02_a
        show afternight04_sexbattle_d_eyebrows angryx05_a
        with dissolve

    d "¡¿Es que estás mal de la puta cabeza?!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx04_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils front05_a
        show afternight04_sexbattle_d_eyebrows angryx04_a
        with dissolve

    if current_girl.orgasm == 0:

        d "¡Si ni siquiera me he corrido una sola vez!"

    elif current_girl.orgasm == 1:

        d "¡Después de que me haya corrido!"

    else :

        d "¡Después de que me haya corrido [current_girl.orgasm] veces!"

    ##

    if mc_body.orgasm == 1:

        d "¡Y te hayas corrido!"

    elif mc_body.orgasm == 2:

        d "¡Y te hayas corrido [mc_body.orgasm] veces!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Talkingx06_a
        show afternight04_sexbattle_d_eyes 01_a
        show afternight04_sexbattle_d_pupils front01_a
        show afternight04_sexbattle_d_eyebrows angryx04_a
        with dissolve

    d "¡¿Ahora quieres dejarlo?!"

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx07_a
        show afternight04_sexbattle_d_eyes 03_a
        show afternight04_sexbattle_d_pupils front03_a
        show afternight04_sexbattle_d_eyebrows angryx03_a
        with dissolve

    p "Sí."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx08_a
        show afternight04_sexbattle_d_eyes 03_a
        show afternight04_sexbattle_d_pupils right03_a
        show afternight04_sexbattle_d_eyebrows angryx05_a
        with dissolve

    p "Lo siento,"

    extend " pero prefiero no continuar."

    if current_pose.id == "pose_1":
        show afternight04_sexbattle_d_mouth sad_Silentx09_a
        show afternight04_sexbattle_d_eyes 05_a
        show afternight04_sexbattle_d_pupils right05_a
        show afternight04_sexbattle_d_eyebrows angryx02_a
        with dissolve

    d "..."

    scene afternight04_sexbattle_background_a
    with hpunch

    n "Con una ira incontenible sale de un salto y se dirige a cierta velocidad hasta el cuarto de baño"

    n "dónde cierra la puerta con un fuerte golpe."

    p "..."

    pt "Podría haber terminado peor..."

    n "Puesto que el cuarto de baño está ocupado, decides que lo más sensato es limpiarte como puedes en la cocina"

    scene beds_night_lightOff_blindUp_DemptyMCempty
    with dissolve

    n "e ir a la habitación a intentar conciliar el sueño."

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    with dissolve

    pt "Espero que Dídac no me haga nada raro mientras duerma..."

    scene black with fade
    window hide dissolve
    pause

    jump morning05