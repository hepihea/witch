screen premium_dashboard():
    style_group "premium_dashboard"
    zorder 10

    default window_transparent = False

    mousearea:
        if renpy.mobile:
            area (556, 25, 224, 440)
        else:
            area (556, 25, 224, 420)
        hovered SetVariable("can_click", False)
        unhovered SetVariable("can_click", True)

    frame:
        if renpy.mobile:
            xysize (224, 440)
        else:
            xysize (224, 420)
        background Solid("#404040", alpha=0.5)

        xpos 556
        ypos 25

        if window_transparent:
            at set_alpha(0.1)

        vbox:
            xpos 18
            ypos 19
            spacing 2

            #hbox:
                #spacing 21

                #text "Your Roll" color "#399" size 15
                #text "Her Roll" color "#c63" size 15

            hbox:
                xpos -22
                spacing 2

                fixed:
                    fit_first True

                    add "dice_you"
                    text DynamicDisplayable(dynamic_first_dice) color "#9cc" size 25 xalign 0.5 yalign 0.5

                    if mc_body.flashing_1:
                        at blink
                fixed:
                    fit_first True

                    add "dice_you"
                    text DynamicDisplayable(dynamic_first_dice) color "#9cc" size 25 xalign 0.5 yalign 0.5

                    if mc_body.flashing_1:
                        at blink

                null width 6

                if current_girl.difficulty and current_girl.result != "Not rolled" and current_girl.total_fail >= 4 or current_girl.total_success >= 7:
                    fixed:
                        fit_first True

                        add "dice_didac"
                        text "[current_girl.first_dice]" color "#ca9" size 25 xalign 0.5 yalign 0.5
                    fixed:
                        fit_first True

                        add "dice_didac"
                        text "[current_girl.second_dice]" color "#ca9" size 25 xalign 0.5 yalign 0.5

            grid 2 1:
                spacing 10
                
                fixed:
                    xsize 100
                    ysize 30

                    text "[current_girl.last_action_name]" color "#9cc" size 12 xoffset -4

                if current_girl.difficulty > 0 and current_girl.total_fail >= 4 or current_girl.total_success >= 7:
                    text "Rolled" color "#ca9" size 15
                else:
                    text "Not Rolled" color "#ca9" size 15

            grid 2 1:
                spacing 10

                fixed:
                    xsize 90
                    ysize 20

                    text "Difficulty: [mc_body.difficulty]" color "#9cc" size 12

                if current_girl.total_fail >= 4 or current_girl.total_success >= 7:
                    text "Difficulty: [current_girl.difficulty]" color "#ca9" size 12
                else:
                    text ""

            grid 2 1:
                spacing 10

                if "pass" in mc_body.result:
                    text "SUCCESS" color "#693" size 15
                elif "fail" in mc_body.result:
                    text "FAILURE" color "#c33" size 15
                else:
                    text "" size 15

                if "pass" in current_girl.result and current_girl.total_fail >= 4 or current_girl.total_success >= 7:
                    text "SUCCESS" color "#693" size 15
                elif "fail" in current_girl.result and current_girl.total_fail >= 4 or current_girl.total_success >= 7:
                    text "FAILURE" color "#c33" size 15
                else:
                    text "" size 15

            null height 1

            text "You" color "#399" size 15 xoffset -15
            hbox:
                spacing 7

                add "icon_pleasure_you"
                text "[mc_body.pleasure] " color "#9cc" size 13 yalign 0.5
                bar:
                    xysize (118, 11)
                    #range 200
                    range mc_body.max_pleasure[4]
                    value mc_body.pleasure
                    left_bar "bar_pleasure_you"
                    left_gutter 0
                    right_bar get_bar(current=mc_body.orgasm)
                    thumb None
                    yalign 0.5

            hbox:
                spacing 7

                add "icon_orgasm_you"
                text "[mc_body.orgasm]/3"color "#9cc" size 13 yalign 0.5

            null height 10

            text "Didac" color "#c63" size 15 xoffset -15
            hbox:
                spacing 7

                add "icon_pleasure_didac"
                text "[current_girl.pleasure] " color "#ca9" size 13 yalign 0.5
                bar:
                    xysize (118, 11)
                    value current_girl.pleasure
                    #range 200
                    range current_girl.max_pleasure[4]
                    left_bar "bar_pleasure_didac"
                    left_gutter 0
                    right_bar get_bar(current=current_girl.orgasm)
                    thumb None
                    yalign 0.5

            hbox:
                spacing 7

                add "icon_enslavery_didac"
                text "[current_girl.enslavement]" color "#ca9" size 13 yalign 0.5

            hbox:
                spacing 7

                add "icon_orgasm_didac"
                text "[current_girl.orgasm]" color "#ca9" size 13 yalign 0.5

            fixed:
                xalign 0.23
                yoffset -8

                if renpy.get_screen("dummy_screen"):
                    imagebutton:
                        idle "images/sexbattle/premium_dashboard/but_exit_idle.webp"
                        hover "images/sexbattle/premium_dashboard/but_exit_hover.webp"

                        action Jump("game_exit")

                imagebutton:
                    idle "images/sexbattle/premium_dashboard/but_eye_show_idle.webp"
                    hover "images/sexbattle/premium_dashboard/but_eye_show_hover.webp"

                    action ToggleScreenVariable("window_transparent", True, False)

                    xpos 80

screen dummy_screen(show_bg=False, show_expressions=[]):

    modal True
    default areas = current_pose.store

    on "show":
        action If(show_bg, true=[Function(renpy.scene), Function(renpy.show, name=current_pose.bg), Function(show_expressions_func, show_expressions)])

    vbox:
        xalign 1.2
        yalign 0.5
        spacing 15

        for i, pose in current_girl.store.iteritems():
            textbutton (pose.name):
                action [SetVariable('current_pose', current_girl.switch_pose(i)), SetScreenVariable(name='areas', value=current_girl.switch_pose(i).store), Hide("actions")]

    for i in areas:
        imagebutton:
            idle "part_empty_"
            hover "circle_hover"
            focus_mask True

            action If(can_click, true=Show("actions", act=i))
            xpos i.x
            ypos i.y

            at zoom_button(i.zoom)

screen actions(act):
    modal True

    default mouse_pos = renpy.get_mouse_pos()
    default inner_circle = False
    default total_actions = len(act.store.values())

    # Make sure we return back when player clicks on empty screen
    imagebutton:
        idle Solid("#00000000")
        hover Solid("#00000000")

        action Hide("actions")

    if act.name == "Pussy":
        if renpy.variant("pc"):
            frame:
                background Solid("#00000050")
                xsize len(act.name) * 20 + 5
                ysize 36

                xpos mouse_pos[0] - 50
                ypos mouse_pos[1] - 150

                text act.name font "fonts/Comic Book.otf" size 25 xalign 0.5 yalign 0.5

            fixed:

                xpos mouse_pos[0] - 150
                ypos mouse_pos[1] - 150

                $ part = act.get_action("Pussy_Fingers")
                button:
                    xysize (309, 303)

                    idle_background "images/sexbattle/dice_roll/circleout_finger_idle.webp"
                    hover_background "images/sexbattle/dice_roll/circleout_finger_hover.webp"
                    selected_idle_background "images/sexbattle/dice_roll/circleout_finger_select.webp"

                    focus_mask True

                    sensitive act.get_action("Pussy_Fingers").is_sensitive()
                    selected current_girl.last_action_name == "Pussy_Fingers"
                    action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(part)]

                button:
                    xysize (309, 303)
                    idle_background "images/sexbattle/dice_roll/circleout_dick_idle.webp"
                    hover_background "images/sexbattle/dice_roll/circleout_dick_hover.webp"
                    selected_idle_background "images/sexbattle/dice_roll/circleout_dick_select.webp"

                    focus_mask True

                    action SetScreenVariable("inner_circle", True)

                button:
                    xysize (309, 303)
                    idle_background "images/sexbattle/dice_roll/circleout_tongue_idle.webp"
                    hover_background "images/sexbattle/dice_roll/circleout_tongue_hover.webp"
                    selected_idle_background "images/sexbattle/dice_roll/circleout_tongue_select.webp"

                    focus_mask True

                    sensitive act.get_action("Pussy_Tongue").is_sensitive()
                    selected current_girl.last_action_name == "Pussy_Tongue"
                    action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Pussy_Tongue"))]

        else:
            frame:
                xysize (78*3, 80)
                background Solid("#00000050")

                xpos mouse_pos[0] - 50
                ypos mouse_pos[1]

                fixed:
                    xsize len(act.name) * 20 + 5
                    ysize 36

                    xalign 0.5
                    ypos -50
                    add Solid("#00000050")

                    text act.name font "fonts/Comic Book.otf" size 25 xalign 0.5 yalign 0.5 xmaximum 250

                hbox:
                    yalign 0.5
                    spacing 10

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_finger_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_finger_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_finger_select.webp"

                        sensitive act.get_action("Pussy_Fingers").is_sensitive()
                        selected current_girl.last_action_name == "Pussy_Fingers"
                        action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Pussy_Fingers"))]

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_tongue_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_tongue_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_tongue_select.webp"

                        sensitive act.get_action("Pussy_Tongue").is_sensitive()
                        selected current_girl.last_action_name == "Pussy_Tongue"
                        action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Pussy_Tongue"))]

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_dick_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_dick_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_dick_select.webp"

                        action SetScreenVariable("inner_circle", True)

    elif act.name == "Anal hole":
        if renpy.variant("pc"):
            frame:
                background Solid("#00000050")
                xsize len(act.name) * 20 + 5
                ysize 36

                xpos mouse_pos[0] - 50
                ypos mouse_pos[1] - 150

                text act.name font "fonts/Comic Book.otf" size 25 xalign 0.5 yalign 0.5

            fixed:

                xpos mouse_pos[0] - 150
                ypos mouse_pos[1] - 150

                $ part = act.get_action("Anal_Fingers")
                imagebutton:
                    idle "images/sexbattle/dice_roll/circleout_finger_idle.webp"
                    hover "images/sexbattle/dice_roll/circleout_finger_hover.webp"
                    selected_idle "images/sexbattle/dice_roll/circleout_finger_select.webp"

                    focus_mask True

                    sensitive act.get_action("Anal_Fingers").is_sensitive()
                    selected current_girl.last_action_name == "Anal_Fingers"
                    action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(part)]

                imagebutton:
                    idle "images/sexbattle/dice_roll/circleout_dick_idle.webp"
                    hover "images/sexbattle/dice_roll/circleout_dick_hover.webp"
                    selected_idle "images/sexbattle/dice_roll/circleout_dick_select.webp"

                    focus_mask True

                    action SetScreenVariable("inner_circle", True)

                imagebutton:
                    idle "images/sexbattle/dice_roll/circleout_tongue_idle.webp"
                    hover "images/sexbattle/dice_roll/circleout_tongue_hover.webp"
                    selected_idle "images/sexbattle/dice_roll/circleout_tongue_select.webp"

                    focus_mask True

                    sensitive act.get_action("Anal_Tongue").is_sensitive()
                    selected current_girl.last_action_name == "Anal_Tongue"
                    action Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Anal_Tongue"))

        else:
            frame:
                xysize (78*3, 80)
                background Solid("#00000050")

                xpos mouse_pos[0] - 50
                ypos mouse_pos[1]

                fixed:
                    xsize len(act.name) * 20 + 5
                    ysize 36

                    xalign 0.5
                    ypos -50
                    add Solid("#00000050")

                    text act.name font "fonts/Comic Book.otf" size 25 xalign 0.5 yalign 0.5 xmaximum 250

                hbox:
                    yalign 0.5
                    spacing 10

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_finger_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_finger_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_finger_select.webp"

                        sensitive act.get_action("Anal_Fingers").is_sensitive()
                        selected current_girl.last_action_name == "Anal_Fingers"
                        action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Anal_Fingers"))]

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_tongue_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_tongue_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_tongue_select.webp"

                        sensitive act.get_action("Anal_Tongue").is_sensitive()
                        selected current_girl.last_action_name == "Anal_Tongue"
                        action [Hide("actions"), SetField(mc_body, "dick_speed", 0), DoAction(act.get_action("Anal_Tongue"))]

                    imagebutton:
                        idle "images/sexbattle/dice_roll/mobile_dick_idle.webp"
                        hover "images/sexbattle/dice_roll/mobile_dick_hover.webp"
                        selected_idle "images/sexbattle/dice_roll/mobile_dick_select.webp"

                        action SetScreenVariable("inner_circle", True)

    else:
        frame:
            xysize (78*total_actions, 80)
            background Solid("#00000050")

            xpos mouse_pos[0] - 50
            ypos mouse_pos[1]

            fixed:
                xsize len(act.name) * 20 + 5
                ysize 36

                xalign 0.5
                ypos -50
                add Solid("#00000050")

                text act.name font "fonts/Comic Book.otf" size 25 xalign 0.5 yalign 0.5 xmaximum 250

            hbox:
                yalign 0.5
                spacing 10

                for i, j in act.store.iteritems():
                    imagebutton:
                        idle j.idle
                        hover j.hover

                        sensitive j.is_sensitive()
                        action Hide("actions"), Function(j.do)

    if inner_circle:
        $ current_dick = mc_body.get_current_action("dick")
        $ dick_action = act.get_action(current_dick)
        $ part_name = act.name.split("_")[0]
        if part_name == "Anal hole":
            $ part_name = "Anal"
        if "Pussy" in act.name:
            $ dick_action_up = act.get_action(get_dick_action())
            $ dick_action_down = act.get_action(get_dick_action(level="down"))
        elif "Anal hole" in act.name:
            $ dick_action_up = act.get_action(get_dick_action(kind="Anal hole"))
            $ dick_action_down = act.get_action(get_dick_action(kind="Anal hole", level="down"))
        else:
            $ dick_action_up = act.get_action(get_dick_action(kind="Mouth"))
            $ dick_action_down = act.get_action(get_dick_action(kind="Mouth", level="down"))

        if renpy.variant("pc"):
            fixed:
                xpos mouse_pos[0] - 150
                ypos mouse_pos[1] - 150

                imagebutton:
                    idle dick_action_down.image + "L_idle.webp"
                    hover dick_action_down.image + "L_hover.webp"
                    insensitive dick_action_down.image + "L_block.webp"

                    focus_mask True

                    sensitive dick_action_down.is_sensitive() and current_dick != "" and (current_dick != "Pussy_dick_out" or current_dick == "Anal_dick_out")
                    action Hide("actions"), If(current_dick == "Pussy_dick_out" or current_dick == "Anal_dick_out", true=mc_body.clear_dick, false=[ SetField(mc_body, "dick_speed", 0), Function(dick_action_down.do) ])

                imagebutton:
                    idle dick_action_up.image + "R_idle.webp"
                    hover dick_action_up.image + "R_hover.webp"

                    focus_mask True

                    sensitive dick_action_up.is_sensitive() and current_dick != "dick_deeps"
                    action Hide("actions"), SetField(mc_body, "dick_speed", 0), Function(dick_action_up.do)

                imagebutton:
                    idle get_dick_speed_image("images/sexbattle/dice_roll/circlein_velL_0", "_idle.webp", 0, 2, "down")
                    hover get_dick_speed_image("images/sexbattle/dice_roll/circlein_velL_0", "_hover.webp", 0, 2, "down")
                    insensitive "images/sexbattle/dice_roll/circlein_velL_00_block.webp"

                    focus_mask True

                    sensitive mc_body.dick_speed > 0 and part_name in current_dick
                    action Hide("actions"), SetField(mc_body, "dick_speed", mc_body.dick_speed-1), DoAction(dick_action)

                imagebutton:
                    idle get_dick_speed_image("images/sexbattle/dice_roll/circlein_velR_0", "_idle.webp", 1, 3, "up")
                    hover get_dick_speed_image("images/sexbattle/dice_roll/circlein_velR_0", "_hover.webp", 1, 3, "up")

                    focus_mask True

                    sensitive mc_body.dick_speed < 3 and part_name in current_dick and (current_dick != "Pussy_dick_out" and current_dick != "Anal_dick_out")
                    action Hide("actions"), SetField(mc_body, "dick_speed", mc_body.dick_speed+1), DoAction(dick_action)

        else:
            frame:
                xysize ((78*4)+10, 80)
                background Solid("#00000050")

                xpos mouse_pos[0] - 150
                ypos mouse_pos[1] - 150

                fixed:
                    xsize 13 * 16 + 5
                    ysize 26

                    xalign 0.5
                    ypos -50
                    add Solid("#00000050")

                    text "Pussy Actions" font "fonts/Comic Book.otf" size 20 xalign 0.5 yalign 0.5 xmaximum 250

                hbox:
                    yalign 0.5
                    spacing 10

                    imagebutton:
                        idle dick_action_down.image + "L_idle_mobile.webp"
                        hover dick_action_down.image + "L_hover_mobile.webp"
                        insensitive dick_action_down.image + "L_block_mobile.webp"

                        focus_mask True

                        sensitive dick_action_down.is_sensitive() and current_dick != ""
                        action Hide("actions"), If(current_dick == "Pussy_dick_out" or current_dick == "Anal_dick_out", true=mc_body.clear_dick, false=[ SetField(mc_body, "dick_speed", 0), Function(dick_action_down.do) ])

                    imagebutton:
                        idle dick_action_up.image + "R_idle_mobile.webp"
                        hover dick_action_up.image + "R_hover_mobile.webp"

                        focus_mask True

                        sensitive dick_action_up.is_sensitive() and current_dick != "dick_deeps"
                        action Hide("actions"), SetField(mc_body, "dick_speed", 0), Function(dick_action_up.do)

                    text "|" yalign 0.5

                    imagebutton:
                        idle get_dick_speed_image("images/sexbattle/dice_roll/circlein_velL_0", "_idle_mobile.webp", 0, 2, "down")
                        hover get_dick_speed_image("images/sexbattle/dice_roll/circlein_velL_0", "_hover_mobile.webp", 0, 2, "down")
                        insensitive "images/sexbattle/dice_roll/circlein_velL_00_block_mobile.webp"

                        focus_mask True

                        sensitive mc_body.dick_speed > 0 and part_name in current_dick
                        action Hide("actions"), SetField(mc_body, "dick_speed", mc_body.dick_speed-1), DoAction(dick_action)

                    imagebutton:
                        idle get_dick_speed_image("images/sexbattle/dice_roll/circlein_velR_0", "_idle_mobile.webp", 1, 3, "up")
                        hover get_dick_speed_image("images/sexbattle/dice_roll/circlein_velR_0", "_hover_mobile.webp", 1, 3, "up")

                        focus_mask True

                        sensitive mc_body.dick_speed < 3 and part_name in current_dick and (current_dick != "Pussy_dick_out" and current_dick != "Anal_dick_out")
                        action Hide("actions"), SetField(mc_body, "dick_speed", mc_body.dick_speed+1), DoAction(dick_action)

style premium_dashboard_text is text:
    font "fonts/Comic Book.otf"
