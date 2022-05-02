
## INSTRUCTIONS and others.



label warning02:

    centered "{size=52}{b}{color=#f00}Aviso{/color}{/b}:{/size}

        \n\n\nEsto no es un juego {color=969}porno{/color}.

        \n\nEs una {a=https://es.wikipedia.org/wiki/Novela_visual}novela visual{/a} para adultos,
        \nmuy retorcida y en ocasiones escalofriante,
        \nque contiene {color=969}porno{/color}."

    return
    
#####                                            

style inst_textstyle_title:
    font "fonts/gapstown-r.ttf"
    layout "subtitle"
    color "#fff"
    text_align 0.5
    size 45

style inst_textstyle:
    font "fonts/gapstown-r.ttf"
    layout "subtitle"
    color "#fff"
    text_align 0.5
    size 38

style inst_textstyle_touch:
    font "fonts/gapstown-r.ttf"
    layout "subtitle"
    color "#fff"
    text_align 0.5
    size 60


transform instB_01:
    xpos 0.05 ypos 0.1
transform instB_02:
    xpos 0.1 ypos 0.4
transform instB_03:
    xpos 0.1 ypos 0.6

screen general_instructions():

    image "black"

    text (_("{image=gui/icons/instructions_hearts.jpg} Estos corazones no represetan amor, sino deseo.\nIrás viendo porque son importantes durante el juego.")) at instB_01:
        style "inst_textstyle"

    text (_("Puedes cambiar la puntuación de los corazones\ncon el {color=#fa0}Cheat Mode{/color}, pulsando la tecla \"c\".")) at instB_02:
            style "inst_textstyle"

    text (_("Para otros atajos de teclado, mira en {a=showmenu:help}Ayuda{/a}.\nEl juego no está terminado.")) at instB_03:
        style "inst_textstyle"

################################################################################################################
##############################################################################################################

screen general_instructions_touch():

    image "black"

    text (_("{image=gui/icons/instructions_hearts.jpg} Estos corazones no represetan amor, sino deseo.\nIrás viendo porque son importantes durante el juego.")) at instB_01:
        style "inst_textstyle"

    text (_("Puedes cambiar la puntuación de los corazones con el {color=#fa0}Cheat Mode{/color}, que se encuentra en {a=showmenu:preferences}opciones{/a}.")) at instB_02:
            style "inst_textstyle"

    text (_("Para otros atajos de teclado, mira en {a=showmenu:help}Ayuda{/a}.\nEl juego no está terminado.")) at instB_03:
        style "inst_textstyle"

################################################################################################################
##############################################################################################################

############# PC:  WINDOWS / LINUX / MAC (Keyboard system)

transform inst_title:
    xpos 0.03 ypos 0.03

transform inst_proceed:
    xpos 0.18 ypos 0.21

transform inst_rollback:
    xpos 0.45 ypos 0.03

transform inst_save:
    xpos 0.64 ypos 0.15

transform inst_skip:
    xpos 0.2 ypos 0.57

transform inst_cheat:
    xpos 0.75 ypos 0.57

screen pc_instructions():

    image "gui/icons/instructions_pc.jpg"

    text (_("Controles:")) at inst_title:
        style "inst_textstyle_title"

    text (_("Avanzar")) at inst_proceed:
        style "inst_textstyle"

    text (_("Volver atrás/ Ocultar texto")) at inst_rollback:
        style "inst_textstyle"

    text (_("Guardar")) at inst_save:
        style "inst_textstyle"

    text (_("Saltar texto")) at inst_skip:
        style "inst_textstyle"

    text (_("{color=#fa0}Cheat Mode{/color}")) at inst_cheat:
        style "inst_textstyle"

################################################################################################################
##############################################################################################################

################################################################################################################
##############################################################################################################

############# TOUCH

transform inst_t_title:
    xpos 0.03 ypos 0.03

transform inst_t_proceed:
    xpos 0.55 ypos 0.3

transform inst_t_rollback:
    xpos 0.035 ypos 0.3

transform inst_t_other:
    xpos 0.3 ypos 0.88

screen touch_instructions():

    image "gui/icons/instructions_touch.jpg"

    text (_("Controles:")) at inst_t_title:
        style "inst_textstyle"

    text (_("Avanzar")) at inst_t_proceed:
        style "inst_textstyle_touch"

    text (_("Volver\natrás")) at inst_t_rollback:
        style "inst_textstyle_touch"

    text (_("Otras opciones")) at inst_t_other:
        style "inst_textstyle_touch"

################################################################################################################
##############################################################################################################

label callHep:
    call screen help()
    return

label callPreferences:
    call screen preferences()
    return

label instructions02:

    window hide

    if renpy.variant("pc"):
        show screen pc_instructions()
        with dissolve

        pause

        hide screen pc_instructions
        with dissolve

    else:
        show screen touch_instructions()
        with dissolve

        pause

        hide screen touch_instructions
        with dissolve

    return

label instructions03:

    if renpy.variant("pc"):

        show screen general_instructions()
        with dissolve

        pause

        hide screen general_instructions
        with dissolve

    else:

        show screen general_instructions_touch()
        with dissolve

        pause

        hide screen general_instructions_touch
        with dissolve

    return


################################################################################################
############################################################################################
#### OLD


define startmenudisclaimer_ADULT = (_("{color=#757}{size=30}AVISO: SOLO PARA ADULTOS{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}Contenido solo apto para adultos mayores de 18 años.\nIncluye imágenes prolongadas de intensa violencia e imágenes con contenido sexual explícito.{/font}{/size}"))

define startmenudisclaimer_ALPHA = (_("\n\n{color=#757}{size=30}VERSIÓN INACABADA{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}El juego sigue estando en desarrollo. Pedimos perdón por nuestra terrible gramática. Hacemos lo mejor posible, esperamos mejorar en próximas versiones.{/font}{/size}"))

define startmenudisclaimer_PATREON = (_("\n\n{color=#757}{size=30}PATREON{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}Comprueba {a=https://www.patreon.com/jonnymelabo}nuestra página web{/a} para asegurarte que estás usando la última versión y de las últimas noticias.{/font}{/size}"))

define startmenudisclaimer_DISCLAIMER = (_("\n\n{color=#757}{size=30}EXENCIÓN DE RESPONSABILIDAD{/size}{/color}{size=21}{font=fonts/chinrg__.ttf}\nToda coincidencia con algún videojuego o juego de mesa, tienen intención humorística y/o de rendir homenaje.{/font}{/size}"))

           

label startmenudisclaimer:

    #"[config.variants]" #To check if it´s using Android, TV or PC variant.

    scene black with fade

    if Steam_check == False:
        centered "{color=#757}{size=30}AVISO: SOLO PARA ADULTOS{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}Contenido solo apto para adultos  mayores de 18 años.\nIncluye imágenes prolongadas de intensa violencia e imágenes con contenido sexual explícito.{/font}{/size}

                  \n\n{color=#757}{size=30}VERSIÓN INACABADA{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}El juego sigue estando en desarrollo. Pedimos perdón por nuestra terrible gramática. Hacemos lo mejor posible, esperamos mejorar en próximas versiones.{/font}{/size}

                  \n\n{color=#757}{size=30}PATREON{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}Comprueba {a=https://www.patreon.com/jonnymelabo}nuestra página web{/a} para asegurarte que estás usando la última versión y de las últimas noticias.{/font}{/size}
                  
                  \n\n{color=#757}{size=30}EXENCIÓN DE RESPONSABILIDAD{/size}{/color}{size=21}{font=fonts/chinrg__.ttf}\nToda coincidencia con algún videojuego o juego de mesa, tienen intención humorística y/o de rendir homenaje.{/font}{/size}"
    else:
        centered "{color=#757}{size=30}AVISO: SOLO PARA ADULTOS{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}Contenido solo apto para adultos  mayores de 18 años.\nIncluye imágenes prolongadas de intensa violencia e imágenes con contenido sexual explícito.{/font}{/size}

                  \n\n{color=#757}{size=30}VERSIÓN INACABADA{/size}{/color}\n{size=21}{font=fonts/chinrg__.ttf}El juego sigue estando en desarrollo. Pedimos perdón por nuestra terrible gramática. Hacemos lo mejor posible, esperamos mejorar en próximas versiones.{/font}{/size}
                  
                  \n\n{color=#757}{size=30}EXENCIÓN DE RESPONSABILIDAD{/size}{/color}{size=21}{font=fonts/chinrg__.ttf}\nToda coincidencia con algún videojuego o juego de mesa, tienen intención humorística y/o de rendir homenaje.{/font}{/size}"
    with dissolve

    return
    


# label instructions:
    
#     scene black
        
#     centered "{size=22}Atajos de ratón (y teclado):{/size}
        
#        {size=18}\n\n{image=gui/icons/mouse_left.png} : Avanzar y seleccionar. ({color=#757}Enter{/color}).
        
#         \n\n{image=gui/icons/mouse_right.png} : Ir al menú. ({color=#757}Esc{/color}).
        
#         \n\n{image=gui/icons/mouse_middle.png} : Para retroceder. ({color=#757}Re Pág{/color}/{color=#757}Av Pág{/color}).

#         \n   (Pulsarlo, para esconder interfaz, igual que {color=#757}H{/color}).

#         \n\n{size=14}(No es recomendable retroceder cuando haya animaciones){/size}.
        
#         \n\n{color=#757}P{/color}: Ocultar/Mostrar Puntuaciones. 
        
#         \n\n{color=#757}I{/color}: Ocultar/Mostrar Historia. {color=#757}M{/color}: Silenciar Juego.
        
#         \n\n{color=#757}Ctrl{/color} (Sujetándolo): Para avanzar.
#         \n   ({color=#757}Tab{/color}, sino quieres sujetar botón).
        
#         \n\n{color=#757}F{/color}: Pantalla completa/Ventana. {color=#757}S{/color}: Captura de pantalla.
        
#         \n\nEl juego no está terminado.{/size}
       
#         \n\n" with dissolve
    
#     centered "{size=22}Atajos de ratón (y teclado) para{/size} {size=32}{color=#9ab}PLATINUM{/color} {size=32} y {color=#fa0}PREMIUM{/color}:{/size}
        
#         {size=18}\n\n{image=gui/icons/mouse_middle_premium.png} : Cuando retrocedas, podrás elegir otra opción.
        
#         \n\n{color=#fa0}F5{/color}: Guardado Rápido. {color=#fa0}F6{/color}: Cargado Rápido.
        
#         \n\n{color=#fa0}C{/color}: {size=22}Cheat Mode{/size}: Podrás añadir/restar puntos a voluntad.{/size}
       
#         \n\n" with dissolve
    
#     return