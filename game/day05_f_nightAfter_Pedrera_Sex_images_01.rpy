screen Points_PedreraSex():

    #default tt = Tooltip("No button selected.")

    if PlatinumHelp == True:

        zorder 99

        default hideDPoints = "<"
        
        #if Tendolarsversion == True:
        key "p" action ToggleScreenVariable('hideDPoints', True, False)
        
        #if Tendolarsversion == True:
        hbox:
            xalign 0.0
            yalign 0.0

            if hideDPoints == "<":
                frame:
                    background  "#000a"
                    hbox:

                        # MC PLEASURE

                        imagebutton:
                            idle 'gui/icons/dungeon/dun_ple_pos_mc.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text(_("Tu placer") + ": {}".format(p_prot.closeOrgasmTotal), style="dungeon_tooltip")

                        bar:
                            style "dungeon_bars"
                            value p_prot.closeOrgasmTotal
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            # if p_prot.max_pleasure[0]:
                            #     range 50
                            # elif p_prot.max_pleasure[1]:
                            #     range 75

                            range p_prot.max_pleasure[p_prot.orgasm]
                        text "{size=15} {/size}"

                        # DIDAC PLEASURE

                        imagebutton:
                            idle 'gui/icons/ple_d.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text(_("Placer de Dídac") + ": {}".format(p_didac.closeOrgasmTotal), style="dungeon_tooltip")

                        bar:
                            style "dungeon_bars"
                            value p_didac.closeOrgasmTotal
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            # if p_prot.max_pleasure[0]:
                            #     range 50
                            # elif p_prot.max_pleasure[1]:
                            #     range 75

                            range p_didac.max_pleasure[p_didac.orgasm]
                        text "{size=15} {/size}"

                        # TXELL PLEASURE

                        imagebutton:
                            idle 'gui/icons/ple_m.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text(_("Placer de Txell") + ": {}".format(p_txell.closeOrgasmTotal), style="dungeon_tooltip")

                        bar:
                            style "dungeon_bars"
                            value p_txell.closeOrgasmTotal
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            # if p_prot.max_pleasure[0]:
                            #     range 50
                            # elif p_prot.max_pleasure[1]:
                            #     range 75

                            range p_txell.max_pleasure[p_txell.orgasm]
                        text "{size=15} {/size}"

                        # NEUS PLEASURE

                        imagebutton:
                            idle 'gui/icons/ple_n.png'
                            hover "gui/icons/dungeon/dun_ple_hover_def.png" 
                            action NullAction() align (.5, .5)
                            hover_foreground Text(_("Placer de Neus") + ": {}".format(p_neus.closeOrgasmTotal), style="dungeon_tooltip")

                        bar:
                            style "dungeon_bars"
                            value p_neus.closeOrgasmTotal
                            left_bar "gui/slider/horizontal_hover_bar_dungeon_sti.png"
                            right_bar "gui/slider/horizontal_idle_bar_dungeon_empty.png"
                            # if p_prot.max_pleasure[0]:
                            #     range 50
                            # elif p_prot.max_pleasure[1]:
                            #     range 75

                            range p_neus.max_pleasure[p_neus.orgasm]
                        text "{size=15} {/size}"

