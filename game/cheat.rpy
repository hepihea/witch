
## TO LOOK FOR variables.



## By GUS (Renpy Español)
##########################################################################################
############################################################################################################
############################################################################################################
##########################################################################################

### For the console of RENPY:
# for i in dir(store): # In theory this is the ONE!
#     if i[0] == "_":
#         continue
#     value = getattr(store, i)
#     if value == False or value == 0 or value == 0.0:
#         continue
#     if isinstance(value, renpy.game.Preferences):
#         continue
#     if value == True:
#         print i, value
#     elif isinstance(value, int) and value != 0:
#         print i, value
#     elif isinstance(value, float) and value != 0.0:
#         print i, value

label printingVariables:

        ###abrir el archivo
    python:
        f = open('C:/Users/Usuario/Downloads/Nueva carpeta (17)/workfile.txt', 'w+')

        for i in dir(store): # In theory this is the ONE!
            if i[0] == "_":
                continue
            value = getattr(store, i)
            if value == False or value == "" or value == 0 or value == 0.0:
                continue
            # if isinstance(value, Transform()):
            #     print "Too many ATLTransform."
            if isinstance(value, renpy.game.Preferences):
                continue
            if value == True:
            #if isinstance(value, bool) and value == True:
                print i, value
            elif isinstance(value, int) and value != 0:
                print i, value
            elif isinstance(value, float) and value != 0.0:
                print i, value

            #escribir las variables (quizá haya que dar un mejor formato)
            f.write(str(i) + " = " + str(value) + "\n")
            ###cerrar el archivo
        f.close()

    return

##########################################################################################
############################################################################################################
############################################################################################################
##########################################################################################

## By GUS (Alternative) (Renpy Español)
# 
# init python:
#     import repr
#     import string
#     #from io import open

#     def imprimir_variablViewer():

#         aRepr = repr.Repr()
#         aRepr.maxstring = 120

#         entries = [ ]
#         deleted_entries = set()

#         for sn, d in renpy.python.store_dicts.items():

#             if sn.startswith("store._"):
#                 continue

#             for vn in d.ever_been_changed:

#                 if vn.startswith("__00"):
#                     continue

#                 if vn.startswith("_") and not vn.startswith("__"):
#                     continue

#                 if vn not in d:
#                     value = "deleted"
#                 else:
#                     value = aRepr.repr(d[vn])

#                 if vn == "nvl_list":
#                     continue

#                 name = (sn + "." + vn)[6:]

#                 if vn not in d:
#                     deleted_entries.add(name)

#                 entries.append((name, value))

#         entries.sort(key=lambda e : e[0])
#         f = open('/Users/~/Documents/renpy_projects/workfile.txt', 'w+')

#         for e in entries:
#             line = str(e).translate(string.punctuation)
#             f.write(line + "\n")
#         f.close()


###DON'T DELETE THIS:
#######################################################################################################
#######################################################################################################
###################################################
###################################################

## What the fuck is this?

# label start:
#     scene bg room
#     pause
#     $ imprimir_variablViewer()
#     "OK"
#     pause
#     return


#######################################################################################################
#######################################################################################################
###################################################
###################################################

##if _preferences.language == "english":

    ##call endtranslation

## To see variables inside the RENPY console.
###################################################

#### To find TRUE, FALSE and Points in Console Renpy.

# for i in dir(store): # PROBABLY NOT USE
#     value = getattr(store, i)
#     if isinstance(value, bool):
#         print i, value
#     elif isinstance(value, int):
#         print i, value

#### To find TRUE, (not FALSE) and Points in Console Renpy. (In theory, it´s not really working)

# for i in dir(store): # PROBABLY NOT USE.
#     value = getattr(store, i)
#     if value == True:
#         print i, value
#     elif isinstance(value, int):
#         print i, value
# #
# for i in dir(store): # PROBABLY NOT USE.
#     if i[0] == "_":
#         continue
#     value = getattr(store, i)
#     if value == True:
#         print i, value
#     elif isinstance(value, int):
#         print i, value
#     elif isinstance(value, float):
#         print i, value


# for i in dir(store): # In theory this is the ONE!
#     if i[0] == "_":
#         continue
#     value = getattr(store, i)
#     if value == False or value == 0 or value == 0.0:
#         continue
#     if isinstance(value, renpy.game.Preferences):
#         continue
#     if value == True:
#         print i, value
#     elif isinstance(value, int) and value != 0:
#         print i, value
#     elif isinstance(value, float) and value != 0.0:
#         print i, value

# init python:

#     walkthrough_patreon = __("esta {a=https://www.patreon.com/posts/8830789}{size=32}guía{/size}{/a}")
#     update_patreon_eng = "{a=https://www.patreon.com/jonnymelabo}update{/a}"

#     if Steam_check:
#         walkthrough_patreon = __("una guía")
#         update_patreon_eng = "update"

########################################################################################################
########################################################################################################
####################################################
####################################################



screen cheat_system():

    if PlatinumHelp == True:
        add Solid("#000") alpha 0.75
        add "border_dream" zoom 0.5

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25

            text (_("{color=#fa0}{size=30}Cheat Mode{/size}{/color}"))
                
            hbox:
                spacing 10

                textbutton "{size=45}--{/size}":
                    action SetField(pl, "np", pl.np-10)
                textbutton "{size=45}-{/size}":
                    action SetField(pl, "np", pl.np-1)
                text "{image=gui/icons/heart_n.png}" + "{color=#969} [pl.np]{/color}"
                textbutton "{size=45}+{/size}":
                    action SetField(pl, "np", pl.np+1)
                textbutton "{size=45}++{/size}":
                    action SetField(pl, "np", pl.np+10)
                
                
                    
            hbox:
                spacing 10

                textbutton "{size=45}--{/size}":
                    action SetField(pl, "dp", pl.dp-10)
                textbutton "{size=45}-{/size}":
                    action SetField(pl, "dp", pl.dp-1)
                text "{image=gui/icons/heart_d.png}" + "{color=#c63} [pl.dp]{/color}"
                textbutton "{size=45}+{/size}":
                    action SetField(pl, "dp", pl.dp+1)
                textbutton "{size=45}++{/size}":
                    action SetField(pl, "dp", pl.dp+10)
                

            hbox:
                spacing 10

                textbutton "{size=45}--{/size}":
                    action SetField(pl, "mp", pl.mp-10)
                textbutton "{size=45}-{/size}":
                    action SetField(pl, "mp", pl.mp-1)
                text "{image=gui/icons/heart_m.png}" + "{color=#a93} [pl.mp]{/color}"
                textbutton "{size=45}+{/size}":
                    action SetField(pl, "mp", pl.mp+1)
                textbutton "{size=45}+{/size}":
                    action SetField(pl, "mp", pl.mp+10)
                
                

            if not renpy.variant("pc"):

                hbox:
                    spacing 10
                    style_prefix "check"

                    textbutton (_("{size=50}Cerrar{/size}")):
                        action Hide("cheat_system")
                        xalign 0.5

label PlatinumHelp_label:


    menu:
        "En opciones podrás {color=#0c0}activar{/color} o {color=#f00}desactivar{/color} esta {color=#fa0}ayuda{/color} (Aunque es posible que la barra no siempre aparezca)."

        "{color=#f00}Desactivar{/color} {color=#fa0}Ayuda Platinum{/color}\n(Jugar tal y cómo fue diseñada esta novela visual).":
            call p_Help
            $ PlatinumHelp = False

        "{color=#0c0}Activar{/color} {color=#fa0}Ayuda Platinum{/color}\n(Jugar sabiendo los puntos que te da cada elección).":
            call p_Help
            $ PlatinumHelp = True

    return

label jumpday:

    scene black

    $ walkthrough_patreon = (_("{a=https://www.patreon.com/posts/8830789}{size=32}guía{/size}{/a}"))
    $ update_patreon_eng = "{a=https://www.patreon.com/jonnymelabo}update{/a}"

    if Steam_check:
        $ walkthrough_patreon = (_("una guía"))
        $ update_patreon_eng = "update"

    menu jumpday_question:

        "Puedes empezar el juego desde el {color=#fcf}principio{/color} o desde otro punto. Está ordenado siguiendo esta [walkthrough_patreon!t] paso a paso."

        "Desde el principio.":

            jump afternoon01

        "Desde otro día.":

            jump jumpday_question_days

    menu jumpday_question_days:

        "El juego son 5 días."

        "día 03.":

            jump jumpday_question_day03

        "día 04.":

            jump jumpday_question_day04

        "día 05.":

            jump jumpday_question_day05_a

        "Atrás.":

            jump jumpday_question

    menu jumpday_question_day03:

        "Día 3"

        "Mañana.":

            play music "audio/sfx/birds01.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "birds01"

            jump beforemorning03_pro
            # jump untilday03

        "Noche en la Pedrera.":

            ### renpy.music.get_playing()  ### To know the music is playing.

            play music "audio/music/neus_theme.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "neus_theme"

            scene night03_bg_street_pedrera_door_opened02
            show neus_body ld_default:
                neus_body_atright_position
            show neus_head:
                neus_body_atright_position
            show neus_arms ld_rest:
                neus_body_atright_position
            show neus_exp_blush 05:
                neus_exp_atright_position
            show neus_exp_mouth sad_Silentx03:
                neus_exp_atright_position
            show neus_exp_eyes 03:
                neus_exp_atright_position
            show neus_exp_iris left03:
                neus_exp_atright_position
            show neus_exp_eyebrows angryx01:
                neus_exp_atright_position
            show neus_exp_glasses:
                neus_exp_atright_position
            show neus_exp_hairfront:
                neus_exp_atright_position

            jump night03_MidnightProblem04_GoUp

        "Noche en casa.":

            jump afternight03_pro

        "Atrás.":

            jump jumpday_question_days

    menu jumpday_question_day04:

        "Día 4"

        "Mañana.":

            play music "audio/sfx/birds01.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "birds01"

            scene black

            jump morning04_pro
            #jump untilday04

        "Tarde, (Dónde puedes forzar a Dídac)":

            play music "audio/music/alcaknight/aura.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "aura"

            scene aftermorning04_bg fittingroomin

            jump aftermorning04_FittingRoom_Whynot_Staying_pro
            #jump untilda04_DidacRape

        "Cita en el museo.":

            jump afternoon04_TxellMacba_pro

        "Segunda cita con Neus.":

            jump night04_restaurant_pro
            #jump untilday04_NeusDate02

        "Intimar con Neus (o posibilidad de forzarla).":

            play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "forever_dreaming"

            scene bg dark_a
            show n_closefromup_body ld:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_blush 02:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_eyes 02:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_iris front02:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_eyebrows normal:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_tears 00_00:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_mouth happy_Silentx01:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_glasses:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_hair_front:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_prothand empty:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0
            show n_closefromup_prothandchin empty:
                zoom 0.9 xalign 0.5 yalign 0.45 rotate 0

            jump night04_Neus_DoILeave_pro

            #jump untilday04_NeusDate02_Rape

        "Justo antes del minijuego con Dídac.":

            play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "deadly_roulette"

            scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little
            show bg livingroom_roomOthersLingerie_night_LightOff_blur01:
                subpixel True
                alpha 0.0 
                easein_quad 2.0 alpha 1.0
            show didacfbodybelow naked:
                dfbody_atright_closex2
            show didacfbodybelow_panties yellowblack:
                dfbody_atright_closex2
            show didacfbodybelow_naked_drops 00:
                dfbody_atright_closex2
            show didacfbodytop brayellowblack:
                dfbody_atright_closex2
            show didacfbodytop_naked_drops 00:
                dfbody_atright_closex2
            show didacfhandl hip_naked:
                dfbody_atright_closex2
            show didacfhandl_hip_naked_drops 00:
                dfbody_atright_closex2
            show didacf_blush 02:
                dfexpressions_atright_closex2
            show didacf_eyes 04:
                dfexpressions_atright_closex2
            show didacf_pupils down04:
                dfexpressions_atright_closex2
            show didacf_eyebrows sadx01:
                dfexpressions_atright_closex2
            show didacfbodytop_hair:
                dfbody_atright_closex2
            show didacf_mouth sadbiting_Silentx05:
                dfexpressions_atright_closex2
            show didacfhandr leg_naked:
                dfbody_atright_closex2
            show didacfhandr_leg_naked_drops 00:
                dfbody_atright_closex2
            with dissolve

            jump afternight04_Didac_FuckMe_pro
            #jump untilday04_beforeMiniGame

        "Atrás.":

            jump jumpday_question_days

    menu jumpday_question_day05_a:

        "Día 5 - mañana, tarde"

        "Mañana.":
            $ DidacPregnant = True # Just because I forgot to add it.
            jump morning05_pro
            #jump untilday05
        "Playa.":
            $ DidacPregnant = True
            jump aftermorning05_pro
            #jump untilday05_beach_beginning
        "Playa, un balón te despierta.":
            $ DidacPregnant = True
            jump aftermorning05_BallWakeUp_pro
            #jump untilday05_beach_ballWakeUp
        "Playa, segundo despertar.":
            $ DidacPregnant = True
            jump aftermorning05_AfterDeepsea_WakeUp_pro
            #jump untilday05_beach_handjobWakeUp
        "Segunda cita con la rubia.":
            $ DidacPregnant = True
            jump afternoon05_TxellWorkPlace_pro
            #jump untilday05_txellSecondDate
        "Esperando a la rubia en la biblioteca.":
            play music "audio/music/alcaknight/Sinfonia.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "Sinfonia"
            $ DidacPregnant = True
            jump afternoon05_Library_pro
            #jump untilday05_txellLibrary
        "<Siguiente>":
            jump jumpday_question_day05_b
        "<Elegir otro día>":

            jump jumpday_question_days

    menu jumpday_question_day05_b:

        "Día 05 - noche"

        "Última cita con Neus.":
            $ DidacPregnant = True
            jump night05_NeusLastDate_pro
            #jump untilday05_NeusThirdDate
        "Última cita, después del interrogatorio.":
            $ DidacPregnant = True
            jump night05_Interrogation_After_pro
            #jump untilday05_AfterInterrogation
        "Última cita, en el baño.":
            $ DidacPregnant = True
            jump night05_Park_WC_pro
            #jump untilday05_toilet
        "Última cita, las tres puertas.":
            play music "audio/music/kevinmacleod/vanishing.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "vanishing"
            $ DidacPregnant = True
            jump night05_NeusLastDate_HotelKrueger_Door_General_pro
            #jump untilday05_threeDoors
        "Última cita, la noria.":

            play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 2.0 fadeout 2.0
            $ music_play = "almost_new_kevin"

            scene bg night05_bg_tibidabo_park_00:
                truecenter
                zoom 0.6 xpos 0.6 ypos 0.4
            show neus_arm_r sd:
                neus_body_atright_position
            show neus_body sd_default:
                neus_body_atright_position
            show neus_head:
                neus_body_atright_position
            show neus_arm_l sd:
                neus_body_atright_position
            
            show neus_exp_blush 02:
                neus_exp_atright_position
            show neus_exp_mouth sadbiting_Silentx04:
                neus_exp_atright_position
            show neus_exp_eyes 04:
                neus_exp_atright_position
            show neus_exp_iris left04:
                neus_exp_atright_position
            show neus_exp_tears empty:
                neus_exp_atright_position
            show neus_exp_eyebrows sadx04:
                neus_exp_atright_position
            show neus_exp_glasses:
                neus_exp_atright_position
            show neus_exp_hairfront:
                neus_exp_atright_position

            show night05_bg_tibidabo_park_00:
                zoom 0.75 xpos 1.65 ypos 0.4 # Noria

            jump night05_NeusLastDate_Noria_Question_pro
            #jump night05_NeusLastDate_After_HotelKrueger_Leaving_pro
            #jump untilda05_Noria

        # "Hacerlo con Neus.":
        #     jump afternight05_Pedrera_Sex_pro

        "<Siguiente>":
            jump jumpday_question_day05_c
        "<Anterior>":
            jump jumpday_question_day05_a
        "<Elegir otro día>":
            jump jumpday_question_days

    menu jumpday_question_day05_c:
        "Día 05 - madrugada"

        "Después de no obedecer.":
            jump afternight05_Pedrera_Strangle_LastBeat_pro

        "Ahora es cosa tuya.":

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious

            show didacf_mouth sad_Silentx03
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows serious

            jump afternight05_Pedrera_Sex_DTChoose_previous_pro


        "<Anterior>":
            jump jumpday_question_day05_b
        "<Elegir otro día>":
            jump jumpday_question_days

# label untilday03:

#     python:
#         pl.np = 10
#         pl.dp = 1
#         pl.mp = 2

#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True

#     jump beforemorning03

# label untilday04:

#     python:
#         pl.np = 38
#         pl.dp = 10
#         pl.mp = 9

#         afternight03_Didac_AfterShower_Melons = True
#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True

#     jump morning04

# label untilda04_DidacRape: # Bad Ending

#     python:
#         pl.np = 38
#         pl.dp = 25
#         pl.mp = 9

#     jump morning04_aftermorning04_Mast001_NotsoHappyEnding

# label untilday04_TxellDate:

#     python:
#         pl.np = 38
#         pl.dp = 28
#         pl.mp = 10

#         aftermorning04_Mast001_AnalFast_insert = True
#         aftermorning04_Mast001_Anal_happy = True
#         aftermorning04_Mast001_Anal_insert = True
#         aftermorning04_Mast001_PussyFastAfter_Happy = True
#         aftermorning04_Mast001_PussyFast_insert = True
#         aftermorning04_bg_fittingroom_mast_Fast = True
#         afternight03_Didac_AfterShower_Melons = True
#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         afternoon04_TxellMacbaDate = True
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         morning04_DidacHotforyou_Cond = True
#         morning04_ShoppingDidac_Cond = True
#         morning04_Shopping_didaccum_Cond = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True

#     jump afternoon04_TxellMacba

# label untilday04_NeusDate02:

#     python:
#         pl.np = 38
#         pl.dp = 28
#         pl.mp = 55

#         Cartq = 13
#         KnowTxellwasEscort_Cond = True
#         Martq = 1
#         TxellSlave = 1
#         aftermorning04_Mast001_AnalFast_insert = True
#         aftermorning04_Mast001_Anal_happy = True
#         aftermorning04_Mast001_Anal_insert = True
#         aftermorning04_Mast001_PussyFastAfter_Happy = True
#         aftermorning04_Mast001_PussyFast_insert = True
#         aftermorning04_bg_fittingroom_mast_Fast = True
#         afternight03_Didac_AfterShower_Melons = True
#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         afternoon04_MACBA_TxellTruth_Cond = True
#         afternoon04_Q_ClassicArt = True
#         afternoon04_TxellMacbaDate = True
#         afternoon04_macba_TxellGrabYourBalls_Cond = True
#         afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
#         afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
#         afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
#         afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = True
#         inMACBAq = 9
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         morning04_DidacHotforyou_Cond = True
#         morning04_ShoppingDidac_Cond = True
#         morning04_Shopping_didaccum_Cond = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True

#     jump night04_restaurant

# label untilday04_NeusDate02_Rape:

#     python:

#         pl.np = 87
#         pl.dp = 28
#         pl.mp = 55

#         Cartq = 13
#         KnowTxellwasEscort_Cond = True
#         Martq = 1
#         Nfjob = 9
#         TxellSlave = 1
#         aftermorning04_Mast001_AnalFast_insert = True
#         aftermorning04_Mast001_Anal_happy = True
#         aftermorning04_Mast001_Anal_insert = True
#         aftermorning04_Mast001_PussyFastAfter_Happy = True
#         aftermorning04_Mast001_PussyFast_insert = True
#         aftermorning04_bg_fittingroom_mast_Fast = True
#         afternight03_Didac_AfterShower_Melons = True
#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         afternoon04_MACBA_TxellTruth_Cond = True
#         afternoon04_Q_ClassicArt = True
#         afternoon04_TxellMacbaDate = True
#         afternoon04_macba_TxellGrabYourBalls_Cond = True
#         afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
#         afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
#         afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
#         afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = True
#         inMACBAq = 9
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         morning04_DidacHotforyou_Cond = True
#         morning04_ShoppingDidac_Cond = True
#         morning04_Shopping_didaccum_Cond = True
#         night03_2ndDateInsidePedreraWithNeus = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True
#         night04_Neus_KissFrenchmade = True
#         night04_QuestionEggs = True
#         night04_QuestionMeat = True
#         night04_QuestionMilk = True

#     jump night04_Neus_ReallyLike_Kiss_Continue

# label untilday04_beforeMiniGame:

#     python:

#         pl.np = 102
#         pl.dp = 34
#         pl.mp = 55

#         Cartq = 13
#         KnowTxellwasEscort_Cond = True
#         Martq = 1
#         Nfjob = 9
#         TxellSlave = 1
#         aftermorning04_Mast001_AnalFast_insert = True
#         aftermorning04_Mast001_Anal_happy = True
#         aftermorning04_Mast001_Anal_insert = True
#         aftermorning04_Mast001_PussyFastAfter_Happy = True
#         aftermorning04_Mast001_PussyFast_insert = True
#         aftermorning04_bg_fittingroom_mast_Fast = True
#         afternight03_Didac_AfterShower_Melons = True
#         afternight04_condom_on = True
#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         afternoon04_MACBA_TxellTruth_Cond = True
#         afternoon04_Q_ClassicArt = True
#         afternoon04_TxellMacbaDate = True
#         afternoon04_macba_TxellGrabYourBalls_Cond = True
#         afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
#         afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
#         afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
#         afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = True
#         inMACBAq = 9
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         morning04_DidacHotforyou_Cond = True
#         morning04_ShoppingDidac_Cond = True
#         morning04_Shopping_didaccum_Cond = True
#         mouse_visible = True
#         neus_glasses = True
#         night03_2ndDateInsidePedreraWithNeus = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True
#         night04_Neus_Blowjob_Cum_Affirmative = True
#         night04_Neus_Blowjob_Cumming_inmouth = True
#         night04_Neus_KissFrenchmade = True
#         night04_Neus_Promise_IPromise_Darkness_Cond = True
#         night04_QuestionEggs = True
#         night04_QuestionMeat = True
#         night04_QuestionMilk = True
#         night04_pedrera_blowjob_021_cumin = True
#         night04_pedrera_blowjob_pov02_ghosts_005 = True
#         night04_pedrera_blowjob_pov_004_Con_eyes_front05 = True
#         night04_pedrera_blowjob_pov_004_Con_mouth_Tongue = True
#         night04_pedrera_blowjob_pov_006_Con_Body_LickBelowDick = True
#         night04_pedrera_blowjob_pov_009_Con_Body = True
#         night04_pedrera_blowjob_pov_010_blush_Con_01 = True
#         night04_pedrera_blowjob_pov_010_eyebrows_Con_surprise = True
#         night04_pedrera_blowjob_pov_010_eyes_Con_camera03_03 = True
#         night04_pedrera_blowjob_pov_Conditional_027 = True
#         night04_pedrera_blowjob_DONE = True


#     jump afternight04_Didac_OralSexOrKiss_LikeAnimals


# label untilday05:

#     python:

#         pl.np = 102
#         pl.dp = 49
#         pl.mp = 55

#         Cartq = 13
#         DidacMCPregnant = True
#         DidacPregnant = True
#         KnowTxellwasEscort_Cond = True
#         Martq = 1
#         Nfjob = 9
#         TxellSlave = 1
#         aftermorning04_Mast001_AnalFast_insert = True
#         aftermorning04_Mast001_Anal_happy = True
#         aftermorning04_Mast001_Anal_insert = True
#         aftermorning04_Mast001_PussyFastAfter_Happy = True
#         aftermorning04_Mast001_PussyFast_insert = True
#         aftermorning04_bg_fittingroom_mast_Fast = True
#         afternight03_Didac_AfterShower_Melons = True


#         afternight04__Anal_dick_deep_Done = 5 # Anal
#         afternight04__Anal_dick_low_Done = 5
#         afternight04__Anal_dick_med_Done = 5
#         #afternight04__Anal_dick_out_Done = 5
#         #afternight04__Anal_Fingers_Done = 0
#         afternight04__Anal_Tongue_Done = 5 # Anilingus/ Rim Job

#         afternight04__Anal_dick_deep_Success = 5 # Anal
#         afternight04__Anal_dick_low_Success = 5
#         afternight04__Anal_dick_med_Success = 5
#         #afternight04__Anal_dick_out_Success = 0
#         #afternight04__Anal_Fingers_Success = 0
#         afternight04__Anal_Tongue_Success = 5 # Anilingus/ Rim Job

#         afternight04_Anal_dick_deep_Speed_0_Done = 5
#         afternight04_Anal_dick_deep_Speed_0_Success = 5
#         afternight04_Anal_dick_deep_Speed_1_Done = 5
#         afternight04_Anal_dick_deep_Speed_1_Success = 5
#         afternight04_Anal_dick_deep_Speed_2_Done = 5
#         afternight04_Anal_dick_deep_Speed_2_Success = 5
#         afternight04_Anal_dick_deep_Speed_3_Done = 5
#         afternight04_Anal_dick_deep_Speed_3_Success = 5
#         afternight04_Anal_dick_med_Speed_0_Done = 5
#         afternight04_Anal_dick_med_Speed_0_Success = 5
#         afternight04_Anal_dick_med_Speed_1_Done = 5
#         afternight04_Anal_dick_med_Speed_1_Success = 5
#         afternight04_Anal_dick_med_Speed_2_Done = 5
#         afternight04_Anal_dick_med_Speed_2_Success = 5
#         afternight04_Anal_dick_med_Speed_3_Done = 5
#         afternight04_Anal_dick_med_Speed_3_Success = 5
#         afternight04_Anal_dick_low_Speed_0_Done = 5
#         afternight04_Anal_dick_low_Speed_0_Success = 5
#         afternight04_Anal_dick_low_Speed_1_Done = 5
#         afternight04_Anal_dick_low_Speed_1_Success = 5
#         afternight04_Anal_dick_low_Speed_2_Done = 5
#         afternight04_Anal_dick_low_Speed_2_Success = 5
#         afternight04_Anal_dick_low_Speed_3_Done = 5
#         afternight04_Anal_dick_low_Speed_3_Success = 5

#         afternight04_CumInMouth = 1
#         afternight04_CumInThroat =1

#         afternight04_Pussy_dick_deep_Speed_0_Done = 5
#         afternight04_Pussy_dick_deep_Speed_0_Success = 5
#         afternight04_Pussy_dick_deep_Speed_1_Done = 5
#         afternight04_Pussy_dick_deep_Speed_1_Success = 5
#         afternight04_Pussy_dick_deep_Speed_2_Done = 5
#         afternight04_Pussy_dick_deep_Speed_2_Success = 5
#         afternight04_Pussy_dick_deep_Speed_3_Done = 5
#         afternight04_Pussy_dick_deep_Speed_3_Success = 5
#         afternight04_Pussy_dick_med_Speed_0_Done = 5
#         afternight04_Pussy_dick_med_Speed_0_Success = 5
#         afternight04_Pussy_dick_med_Speed_1_Done = 5
#         afternight04_Pussy_dick_med_Speed_1_Success = 5
#         afternight04_Pussy_dick_med_Speed_2_Done = 5
#         afternight04_Pussy_dick_med_Speed_2_Success = 5
#         afternight04_Pussy_dick_med_Speed_3_Done = 5
#         afternight04_Pussy_dick_med_Speed_3_Success = 5
#         afternight04_Pussy_dick_low_Speed_0_Done = 5
#         afternight04_Pussy_dick_low_Speed_0_Success = 5
#         afternight04_Pussy_dick_low_Speed_1_Done = 5
#         afternight04_Pussy_dick_low_Speed_1_Success = 5
#         afternight04_Pussy_dick_low_Speed_2_Done = 5
#         afternight04_Pussy_dick_low_Speed_2_Success = 5
#         afternight04_Pussy_dick_low_Speed_3_Done = 5
#         afternight04_Pussy_dick_low_Speed_3_Success = 5

#         afternight04__MMouth_Tongue_Deep_Done = 5
#         afternight04__MMouth_Tongue_Deep_Success = 5
#         afternight04__MMouth_dick_Deep_Done = 5
#         afternight04__MMouth_dick_Deep_Success = 5
#         afternight04__MMouth_dick_Deep_Success_Cond = True
#         afternight04__Anal_Fingers_Done = 5
#         afternight04__Anal_Fingers_Success = 5
#         afternight04__Boob_Grab_Both_Done = 15
#         afternight04__Boob_Grab_Both_Success = 15
#         afternight04__Boob_Slap_Both_Done = 15
#         afternight04__Boob_Slap_Both_Success = 15
#         afternight04__Buttock_Massage_Both_Done = 15
#         afternight04__Buttock_Massage_Both_Success = 15
#         afternight04__Buttock_Slap_Both_Done = 15
#         afternight04__Buttock_Slap_Both_Success = 15
#         afternight04__LBoob_Grab_Done = 15
#         afternight04__LBoob_Grab_Success = 15
#         afternight04__LBoob_Slap_Done = 15
#         afternight04__LBoob_Slap_Success = 15
#         afternight04__RBoob_Grab_Done = 15
#         afternight04__RBoob_Grab_Success = 15
#         afternight04__RBoob_Slap_Done = 15
#         afternight04__RBoob_Slap_Success = 15
#         afternight04__LLeg_Massage_Done = 15
#         afternight04__LLeg_Massage_Success = 15
#         afternight04__LNipple_Lick_Done = 15
#         afternight04__LNipple_Lick_Success = 15
#         afternight04__LNipple_Pinch_Done = 15
#         afternight04__LNipple_Pinch_Success = 15

#         afternight04__LButtock_Grab_Done = 15
#         afternight04__LButtock_Grab_Success = 15
#         afternight04__LButtock_Slap_Done = 15
#         afternight04__LButtock_Slap_Success = 15
#         afternight04__RButtock_Grab_Done = 15
#         afternight04__RButtock_Grab_Success = 15
#         afternight04__RButtock_Slap_Done = 15
#         afternight04__RButtock_Slap_Success = 15
#         afternight04__RLeg_Massage_Done = 15
#         afternight04__RLeg_Massage_Success = 15
#         afternight04__RNipple_Lick_Done = 15
#         afternight04__RNipple_Lick_Success = 15
#         afternight04__RNipple_Pinch_Done = 15
#         afternight04__RNipple_Pinch_Success = 15

#         afternight04__Leg_Massage_Both_Done = 15
#         afternight04__Leg_Massage_Both_Success = 15
#         afternight04__MBelly_Massage_Done = 15
#         afternight04__MBelly_Massage_Success = 15
#         afternight04__MClitoris_Massage_Done = 15
#         afternight04__MClitoris_Massage_Success = 15
#         afternight04__MMouth_Fingers_Done = 15
#         afternight04__MMouth_Fingers_Succcess = 15

#         afternight04__MMouth_Tongue_Done = 15
#         afternight04__MMouth_Tongue_Success = 15
#         afternight04__MMouth_dick_Done = 15
#         afternight04__MMouth_dick_Success = 15

#         afternight04__MStomach_Massage_Done = 15
#         afternight04__MStomach_Massage_Success = 15
#         afternight04__Nipple_Lick_Both_Done = 15
#         afternight04__Nipple_Lick_Both_Success = 15
#         afternight04__Nipple_Pinch_Both_Done = 15
#         afternight04__Nipple_Pinch_Both_Success = 15

#         afternight04__Pussy_Fingers_Done = 15
#         afternight04__Pussy_Fingers_Success = 15
#         afternight04__Pussy_Tongue_Done = 15
#         afternight04__Pussy_Tongue_Success = 15

#         afternight04__Remove_Done = 5
#         afternight04__Remove_Success = 5

#         mc_body.orgasm = 3

#         afternight04_condom_broken = True
#         afternight04_condom_on = True
#         afternight04_didac_orgasms = 6
#         girl_1.orgasm = 6
#         afternight04_pregnant = True
#         afternight04_mc_orgasms = 3

#         afternight04_sexbattle_started = True

#         afternoon02_ShowerAbs = True
#         afternoon02_ShowerBack = True
#         afternoon02_ShowerPiernas = True
#         afternoon02_didac_beforeshower_ambulance = True
#         afternoon04_MACBA_TxellTruth_Cond = True
#         afternoon04_Q_ClassicArt = True
#         afternoon04_TxellMacbaDate = True
#         afternoon04_macba_TxellGrabYourBalls_Cond = True
#         afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
#         afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
#         afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
#         afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = True

#         can_click = True # What?!

#         inMACBAq = 9
#         morning03_Meritxell_Phonenumber_Accepted = True
#         morning03_Neus_Wall_Grabbing = True
#         morning04_DidacHotforyou = True
#         morning04_DidacHotforyou_Cond = True
#         morning04_ShoppingDidac_Cond = True
#         morning04_Shopping_didaccum_Cond = True
#         mouse_visible = True
#         neus_glasses = True
#         night03_2ndDateInsidePedreraWithNeus = True
#         night03_MidnightProblem03_Gentleman_Gentes = True
#         night03_MidnightProblem04_GoUp_Boolean = True
#         night03_NeusFall_NotPanties = True
#         night03_Neus_ugly = True
#         night03_PedreraHome = True
#         night04_Neus_Blowjob_Cum_Affirmative = True
#         night04_Neus_Blowjob_Cumming_inmouth = True
#         night04_Neus_KissFrenchmade = True
#         night04_Neus_Promise_IPromise_Darkness_Cond = True
#         night04_QuestionEggs = True
#         night04_QuestionMeat = True
#         night04_QuestionMilk = True
#         night04_pedrera_blowjob_021_cumin = True
#         night04_pedrera_blowjob_pov02_ghosts_005 = True
#         night04_pedrera_blowjob_pov_004_Con_eyes_front05 = True
#         night04_pedrera_blowjob_pov_004_Con_mouth_Tongue = True
#         night04_pedrera_blowjob_pov_006_Con_Body_LickBelowDick = True
#         night04_pedrera_blowjob_pov_009_Con_Body = True
#         night04_pedrera_blowjob_pov_010_blush_Con_01 = True
#         night04_pedrera_blowjob_pov_010_eyebrows_Con_surprise = True
#         night04_pedrera_blowjob_pov_010_eyes_Con_camera03_03 = True
#         night04_pedrera_blowjob_pov_Conditional_027 = True
#         night04_pedrera_blowjob_DONE = True

#     jump morning05

# label untilday05_beach_beginning:

#     jump aftermorning05

# label untilday05_beach_ballWakeUp:

#     jump aftermorning05_BallWakeUp

# label untilday05_beach_handjobWakeUp:

#     jump aftermorning05_AfterDeepsea_WakeUp

# label untilday05_txellSecondDate:

#     jump afternoon05_TxellWorkPlace

# label untilday05_txellLibrary:

#     jump afternoon05_Library

# label untilday05_NeusThirdDate:

#     jump night05_NeusLastDate

# label untilday05_AfterInterrogation:

#     jump night05_Interrogation_After

# label untilday05_toilet:

#     jump night05_Park_WC

# label untilday05_threeDoors:

#     jump night05_NeusLastDate_HotelKrueger_Door_General

# label untilda05_Noria:

#     jump night05_NeusLastDate_After_HotelKrueger_Leaving




    ## How to extract conditionals, Look up. And don´t forget to Go to PREFERENCES in the Renpy Launcher and activate "Console Output"





##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################
##############################################################

    ### To move the mouse.

#screen force_mouse_move():
    #on "show":
        #action MouseMove(x=590, y=595, duration=.3)
    #timer .5 action Hide('force_mouse_move')

#show screen force_mouse_move

##############################################################
##############################################################

    ### Para que el título aparezca de forma extraña con fondo negro.

#image chapter2:
    #Text(_("El principio es la mitad del todo"), slow_cps = 27, size = 65, font = "fonts/BERNHC.TTF", color = "#ffffff")

##############################################################
##############################################################
